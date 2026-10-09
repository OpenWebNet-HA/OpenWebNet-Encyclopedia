#!/usr/bin/env python3
"""Deterministic mechanical checks for the human-facing encyclopedia.

The checker deliberately reports candidates for rules that cannot be decided
mechanically. A nonzero exit status is reserved for objective failures.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


HUMAN_ROOTS = (
    "README.md",
    "device-model",
    "diagnostics",
    "devices",
    "functional",
    "guides",
    "internals",
    "programming",
    "protocol",
    "reverse-engineering",
    "scenario-engine",
)

SUPPORT_ROOTS = ("assets", "project", "sources")


def human_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for name in HUMAN_ROOTS:
        path = root / name
        pages.extend([path] if path.is_file() else sorted(path.rglob("*.md")))
    return pages


def supporting_pages(root: Path) -> list[Path]:
    pages: list[Path] = []
    for name in SUPPORT_ROOTS:
        pages.extend(sorted((root / name).rglob("*.md")))
    return [p for p in pages if p.name != "ecv-esg-review-ledger.md"]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def github_slug(value: str) -> str:
    value = re.sub(r"`([^`]*)`", r"\1", value.strip().lower())
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^\w\- ]", "", value)
    return value.replace(" ", "-")


def heading_slugs(text: str) -> set[str]:
    counts: Counter[str] = Counter()
    slugs: set[str] = set()
    for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.MULTILINE):
        base = github_slug(match.group(2))
        suffix = counts[base]
        counts[base] += 1
        slugs.add(base if suffix == 0 else f"{base}-{suffix}")
    return slugs


def mask_code(text: str) -> str:
    """Preserve line layout while blanking fenced and inline code."""
    out: list[str] = []
    fenced = False
    marker = ""
    for line in text.splitlines(keepends=True):
        fence = re.match(r"^\s*(```+|~~~+)", line)
        if fence:
            token = fence.group(1)
            if not fenced:
                fenced, marker = True, token[0]
            elif token[0] == marker:
                fenced, marker = False, ""
            out.append("\n" if line.endswith("\n") else "")
            continue
        if fenced:
            out.append("\n" if line.endswith("\n") else "")
            continue
        out.append(re.sub(r"`[^`\n]*`", "", line))
    return "".join(out)


def iter_fences(text: str):
    lines = text.splitlines()
    start = None
    marker = None
    info = ""
    body: list[tuple[int, str]] = []
    for number, line in enumerate(lines, 1):
        match = re.match(r"^\s*(```+|~~~+)\s*([^ ]*)\s*$", line)
        if match:
            token = match.group(1)
            if start is None:
                start, marker, info, body = number, token[0], match.group(2), []
            elif token[0] == marker:
                yield start, number, info, body
                start, marker, info, body = None, None, "", []
            continue
        if start is not None:
            body.append((number, line))
    if start is not None:
        yield start, None, info, body


def check(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    human = human_pages(root)
    support = supporting_pages(root)
    pages = human + support
    objective: list[str] = []
    candidates: list[str] = []
    stats = {"human_pages": len(human), "support_pages": len(support)}

    known_paths = {p.resolve() for p in root.rglob("*")}
    heading_cache = {
        p.resolve(): heading_slugs(p.read_text(encoding="utf-8"))
        for p in root.rglob("*.md")
    }

    # Every human documentation directory containing Markdown has a README.
    human_dirs = {p.parent for p in human if p.name != "README.md"}
    for directory in sorted(human_dirs):
        if not (directory / "README.md").is_file():
            objective.append(f"LANDING {directory.relative_to(root)}: missing README.md")

    link_pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
    for path in pages:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        headings = list(re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.MULTILINE))
        h1 = [m for m in headings if len(m.group(1)) == 1]
        if len(h1) != 1:
            objective.append(f"HEADING {rel}: expected one H1, found {len(h1)}")
        if headings and len(headings[0].group(1)) != 1:
            objective.append(f"HEADING {rel}:{line_number(text, headings[0].start())}: first heading is not H1")
        for previous, current in zip(headings, headings[1:]):
            if len(current.group(1)) > len(previous.group(1)) + 1:
                objective.append(
                    f"HEADING {rel}:{line_number(text, current.start())}: "
                    f"level jumps H{len(previous.group(1))} to H{len(current.group(1))}"
                )

        for number, line in enumerate(text.splitlines(), 1):
            if "—" in line:
                objective.append(f"EM_DASH {rel}:{number}: {line.strip()}")
            if line.rstrip() != line:
                objective.append(f"TRAILING_WS {rel}:{number}")

        for match in link_pattern.finditer(text):
            label, destination = match.group(1), match.group(2).strip()
            if destination.startswith(("http://", "https://", "mailto:")):
                continue
            file_part, _, fragment = destination.partition("#")
            target = path if not file_part else (path.parent / unquote(file_part))
            target = target.resolve()
            if target.is_dir():
                target = (target / "README.md").resolve()
            if target not in known_paths:
                objective.append(
                    f"LINK {rel}:{line_number(text, match.start())}: missing {destination}"
                )
                continue
            if fragment and target.suffix.lower() == ".md":
                if unquote(fragment).lower() not in heading_cache.get(target, set()):
                    objective.append(
                        f"ANCHOR {rel}:{line_number(text, match.start())}: missing {destination}"
                    )
            clean_label = re.sub(r"`", "", label.strip())
            target_name = Path(file_part.rstrip("/")).name if file_part else ""
            obvious = {
                file_part.rstrip("/"),
                target_name,
                Path(target_name).stem,
            } - {"", ".", ".."}
            source_name = Path(target_name).suffix.lower() in {
                ".db", ".db3", ".sqlite", ".txt", ".pdf"
            }
            if (clean_label in obvious and not source_name) or clean_label.lower() == "readme":
                candidates.append(
                    f"LINK_LABEL {rel}:{line_number(text, match.start())}: "
                    f"[{label}]({destination})"
                )

        plain = mask_code(text)
        is_device_definition = rel.parts[:2] == ("devices", "definitions") and rel.name.startswith("own-dev-")
        strict_device_definition = False
        if is_device_definition:
            match = re.match(r"own-dev-(\d{4})-", rel.name)
            strict_device_definition = bool(match and int(match.group(1)) >= 11)
        if is_device_definition:
            if "## Source reconciliation" not in text:
                objective.append(f"DEVICE_SOURCE_RECONCILIATION {rel}: missing ## Source reconciliation")

            documentation = re.search(r"(?ms)^## Documentation\s*$\n(.*?)(?=^## |\\Z)", text)
            if documentation:
                start_line = line_number(text, documentation.start(1))
                for number, line in enumerate(documentation.group(1).splitlines(), start_line):
                    if not line.startswith("|") or "---" in line:
                        continue
                    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                    if not cells or cells[0].lower() in {"document", "document / source"}:
                        continue
                    doc_name = re.sub(r"\x60", "", cells[0]).lower()
                    normalized_cells = {re.sub(r"\x60", "", cell).lower() for cell in cells}
                    multi_product = (
                        "catalogue" in doc_name
                        or bool(normalized_cells & {
                            "product catalogue",
                            "historical product catalogue",
                            "compatibility table",
                            "system / product guide",
                        })
                    )
                    if multi_product and ".pdf)" in line.lower():
                        if "printed p" not in line.lower() or "pdf p" not in line.lower():
                            objective.append(
                                f"DEVICE_SOURCE_PAGE_LOCATION {rel}:{number}: "
                                "multi-product PDF row lacks printed/PDF page location"
                            )

            for pattern, code in (
                (r"(?<![\w`])OWN-DEV-[0-9]{4}\b", "DEVICE_BARE_IDENTIFIER"),
                (r"(?<![\w`])(WHO|WHAT|WHERE|DIMENSION)\s+[0-9]+\b", "DEVICE_BARE_PROTOCOL_LITERAL"),
                (r"\b(?:EN|AS|CONF)_[A-Z0-9_]+\.[A-Za-z0-9_]+\b", "DEVICE_BARE_DATABASE_LITERAL"),
                (r"(?<![.`\d])\d+\.\.\d+(?![.`\d])", "DEVICE_BARE_RANGE_LITERAL"),
                (r"(?<![\w`])[A-Z][A-Z0-9_]*(?:=|<>)[A-Za-z0-9_/-]+(?![\w`])", "DEVICE_BARE_ASSIGNMENT_LITERAL"),
            ):
                for match in re.finditer(pattern, plain):
                    objective.append(
                        f"{code} {rel}:{line_number(plain, match.start())}: {match.group(0)}"
                    )

            for match in re.finditer(r"(?<![\w`])DIM(?:1|2|3|6|30|32|35|38|310)\b", plain):
                objective.append(
                    f"DEVICE_DIM_SHORTHAND {rel}:{line_number(plain, match.start())}: {match.group(0)}"
                )

            for match in re.finditer(
                r"(?i)\b(?:Object|firmware id|condition record|conversion(?:-rule)? reference)\s+([0-9]+)\b",
                plain,
            ):
                objective.append(
                    f"DEVICE_BARE_NUMERIC_REFERENCE {rel}:{line_number(plain, match.start(1))}: {match.group(1)}"
                )

            current_h2 = ""
            current_heading = ""
            for number, line in enumerate(text.splitlines(), 1):
                h2 = re.match(r"^##\s+(.+?)\s*$", line)
                if h2:
                    current_h2 = h2.group(1).replace("`", "").lower()
                    current_heading = current_h2
                    continue
                h3 = re.match(r"^###\s+(.+?)\s*$", line)
                if h3:
                    current_heading = h3.group(1).replace("`", "").lower()
                    continue
                if not line.startswith("|"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if not cells:
                    continue

                if strict_device_definition and current_h2 == "summary" and len(cells) >= 2:
                    field, value = cells[0], cells[1]
                    if field in {
                        "Device ID", "Catalogue item", "Item model / modobj",
                        "Firmware definition", "Firmware definitions",
                        "Declared Modules", "Declared slots", "Object",
                    } and value not in {"Value", "---"} and "`" not in value:
                        objective.append(
                            f"DEVICE_SUMMARY_LITERAL {rel}:{number}: {field} -> {value}"
                        )
                    if field == "Firmware applicability" and value not in {"Value", "---"}:
                        remainder = re.sub(r"`[^`]*`", "", value)
                        if re.search(r"\d", remainder):
                            objective.append(
                                f"DEVICE_SUMMARY_FIRMWARE_LITERAL {rel}:{number}: {value}"
                            )
                    if field == "Commercial identities" and value not in {"Value", "---"}:
                        remainder = re.sub(r"`[^`]*`", "", value)
                        if re.sub(r"[\s,;/]+", "", remainder):
                            objective.append(
                                f"DEVICE_SUMMARY_COMMERCIAL_LITERAL {rel}:{number}: {value}"
                            )

                if current_h2 == "diagnostic applicability":
                    first = cells[0]
                    if re.fullmatch(r"DIMENSION\s+[0-9]+", first):
                        objective.append(
                            f"DEVICE_BARE_DIAGNOSTIC_SURFACE {rel}:{number}: {first}"
                        )

                if strict_device_definition and current_h2 in {"firmware-scoped configuration", "object configuration surfaces"}:
                    first = cells[0]
                    if re.fullmatch(r"[A-Z][A-Z0-9_]{0,63}", first):
                        objective.append(
                            f"DEVICE_BARE_FIELD_LITERAL {rel}:{number}: {first}"
                        )
                    header = [x.lower() for x in cells]
                    if "field" not in header and "---" not in cells and len(cells) >= 3 and first.startswith("`"):
                        domain = cells[1]
                        default = cells[2]
                        plain_domain = mask_code(domain).strip()
                        plain_default = mask_code(default).strip()
                        if re.search(r"(?<![.\d])\d+\.\.\d+(?![.\d])", plain_domain):
                            objective.append(
                                f"DEVICE_BARE_CONFIG_DOMAIN {rel}:{number}: {domain}"
                            )
                        if re.search(
                            r"(?<![\w])(?:SLA|PUL|CEN|GEN|GR|AMB|AUX|OFF|ON|O/I|UP/DOWN)(?![\w])",
                            plain_domain,
                        ):
                            objective.append(
                                f"DEVICE_BARE_CONFIG_ENUM {rel}:{number}: {domain}"
                            )
                        if re.fullmatch(r"\s*\d+(?:\s*/\s*\d+)*\s*", plain_domain):
                            objective.append(
                                f"DEVICE_BARE_CONFIG_DOMAIN {rel}:{number}: {domain}"
                            )
                        if re.fullmatch(r"(?:\d+(?:\.\d+)+|\d+|_)", plain_default):
                            objective.append(
                                f"DEVICE_BARE_CONFIG_DEFAULT {rel}:{number}: {default}"
                            )

        if path in human:
            for pattern, code in (
                (r"\binternal[ -]slot(?:s)?\b", "OBSOLETE_INTERNAL_SLOT"),
                (r"\blogical slot(?:s)?\b", "OBSOLETE_LOGICAL_SLOT"),
            ):
                for match in re.finditer(pattern, plain, re.IGNORECASE):
                    objective.append(
                        f"{code} {rel}:{line_number(plain, match.start())}: {match.group(0)}"
                    )

        # These are candidates because context decides whether code formatting is required.
        for pattern, code in (
            (r"(?<![\w`])(WHO|WHAT|WHERE|DIMENSION)\s+[0-9]+\b", "BARE_PROTOCOL_LITERAL"),
            (r"(?<![\w`])(A|PL)\s*=\s*[0-9]+\b", "BARE_ADDRESS_LITERAL"),
            (r"\b[A-Z]{2}_[A-Z0-9_]+\.[A-Za-z0-9_]+\b", "BARE_DATABASE_LITERAL"),
            (r"(?<![.\d])\d{1,6}\s*(?:–|-|\bto\b)\s*\d{1,6}(?![.\d])", "RANGE_NOTATION"),
        ):
            for match in re.finditer(pattern, plain):
                if code == "RANGE_NOTATION":
                    line_start = plain.rfind("\n", 0, match.start()) + 1
                    prefix = plain[line_start: match.start()].lower()
                    if re.search(r"\bpages?\b", prefix) or re.fullmatch(r"20\d{2}-\d{2}", match.group(0)):
                        continue
                candidates.append(
                    f"{code} {rel}:{line_number(plain, match.start())}: {match.group(0)}"
                )

        for start, end, info, body in iter_fences(text):
            if end is None:
                objective.append(f"FENCE {rel}:{start}: unclosed fence")
                continue
            frame_lines = [(n, line) for n, line in body if re.search(r"\*.*##\s*$", line)]
            preceding = "\n".join(text.splitlines()[max(0, start - 4): start - 1]).lower()
            transcript = bool(frame_lines) and (
                any(" -> " in line for _, line in frame_lines)
                or "transcript" in preceding
                or "exchange:" in preceding
            )
            if transcript:
                for number, line in frame_lines:
                    if not re.match(r"^[^:*]+ -> [^:]+: \S.*##\s*$", line):
                        objective.append(
                            f"TRANSCRIPT {rel}:{number}: frame lacks 'Source -> Destination: '"
                        )

        for match in re.finditer(r"`([0-9A-Fa-f]{8})`", text):
            token = match.group(1)
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            context = text[line_start: None if line_end < 0 else line_end]
            id_context = re.search(
                r"observed\s+(?:sensor\s+)?devices?|captured\s+devices?|physical device id|device id",
                context,
                re.IGNORECASE,
            )
            if id_context and token != token.upper():
                objective.append(
                    f"PHYSICAL_ID {rel}:{line_number(text, match.start())}: lowercase {token}"
                )

    # Exact long-paragraph duplication is a review candidate. Practical Guides
    # may repeat canonical material when needed to keep a workflow executable.
    paragraphs: dict[str, list[str]] = {}
    for path in human:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```|~~~.*?~~~", "", text, flags=re.DOTALL)
        for paragraph in re.split(r"\n\s*\n", text):
            normalized = " ".join(paragraph.split())
            if len(normalized) < 180 or normalized.startswith(("|", "#")):
                continue
            paragraphs.setdefault(normalized, []).append(str(path.relative_to(root)))
    for paragraph, paths in paragraphs.items():
        distinct = sorted(set(paths))
        if len(distinct) > 1:
            candidates.append(
                "DUPLICATE_PARAGRAPH " + ", ".join(distinct)
                + ": " + paragraph[:100]
            )

    if "## Conventions" in (root / "README.md").read_text(encoding="utf-8"):
        objective.append("ROOT_CONVENTIONS README.md: stale local conventions section")

    stats["objective_failures"] = len(objective)
    stats["review_candidates"] = len(candidates)
    return objective, candidates, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--show-candidates", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    objective, candidates, stats = check(root)
    print("STATS " + " ".join(f"{key}={value}" for key, value in stats.items()))
    for item in objective:
        print("FAIL " + item)
    if args.show_candidates:
        for item in candidates:
            print("REVIEW " + item)
    return 1 if objective else 0


if __name__ == "__main__":
    sys.exit(main())
