#!/usr/bin/env python3
"""Generate deterministic candidates for contradiction and epistemic-drift review.

The output is an audit queue, not a factual verdict.  Exact literals can be
compared mechanically; whether two uses conflict still requires the established
evidence and applicability context.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

from check_esg import human_pages, iter_fences, mask_code


RANGE = re.compile(r"(?<![\w.])(?:-?\d+)\.\.(?:-?\d+)(?![\w.])")
FRAME = re.compile(r"`(\*[^`\n]*?##)`")
OBSERVATION = re.compile(r"\b(?:observed|captured|experiment(?:al|ally)?)\b", re.I)
UNIVERSAL = re.compile(r"\b(?:always|never|every|all|universal(?:ly)?)\b", re.I)
IMPLEMENTATION = re.compile(r"\b(?:database|catalogue|implementation)\b", re.I)
PROMOTION = re.compile(r"\b(?:proves?|guarantees?|universally defines?|is the protocol)\b", re.I)
ABSENCE = re.compile(r"\b(?:does not exist|do not exist|no [^.\n]{0,60} exists|never exists)\b", re.I)
CONFLICT_SUBJECTS = {
    "what17": re.compile(r"\bWHAT\s*`?17\b|`WHAT 17`", re.I),
    "dim32": re.compile(r"`DIMENSION 32`|DIMENSION\s*`?32\b", re.I),
    "dim38": re.compile(r"`DIMENSION 38`|DIMENSION\s*`?38\b", re.I),
    "hmac": re.compile(r"\bHMAC\b", re.I),
    "zigbee": re.compile(r"\bZigBee\b", re.I),
}


def add_index(index: dict[str, list[str]], token: str, path: Path, number: int) -> None:
    index[token].append(f"{path}:{number}")


def audit(root: Path) -> tuple[dict[str, int], list[str]]:
    pages = human_pages(root)
    ranges: dict[str, list[str]] = defaultdict(list)
    frames: dict[str, list[str]] = defaultdict(list)
    candidates: list[str] = []
    conflict_mentions = {name: 0 for name in CONFLICT_SUBJECTS}

    for absolute in pages:
        path = absolute.relative_to(root)
        text = absolute.read_text(encoding="utf-8")
        plain = mask_code(text)
        for number, line in enumerate(text.splitlines(), 1):
            for match in RANGE.finditer(line):
                add_index(ranges, match.group(0), path, number)
            for match in FRAME.finditer(line):
                add_index(frames, match.group(1), path, number)
            plain_line = plain.splitlines()[number - 1] if number <= len(plain.splitlines()) else ""
            if OBSERVATION.search(plain_line) and UNIVERSAL.search(plain_line):
                candidates.append(f"OBSERVED_UNIVERSAL {path}:{number}: {line.strip()}")
            if IMPLEMENTATION.search(plain_line) and PROMOTION.search(plain_line):
                candidates.append(f"IMPLEMENTATION_PROMOTION {path}:{number}: {line.strip()}")
            if ABSENCE.search(plain_line):
                candidates.append(f"ABSENCE_CLAIM {path}:{number}: {line.strip()}")
            for name, pattern in CONFLICT_SUBJECTS.items():
                if pattern.search(line):
                    conflict_mentions[name] += 1

        for start, _end, _info, body in iter_fences(text):
            frame_lines = [line for _number, line in body if re.search(r"\*.*##\s*$", line)]
            if len(frame_lines) >= 2 and not any(" -> " in line for line in frame_lines):
                candidates.append(
                    f"UNLABELLED_MULTI_FRAME {path}:{start}: {len(frame_lines)} frame lines"
                )

    repeated_ranges = {token: sites for token, sites in ranges.items() if len(sites) > 1}
    repeated_frames = {token: sites for token, sites in frames.items() if len(sites) > 1}
    for token, sites in sorted(repeated_ranges.items()):
        candidates.append(f"REPEATED_RANGE {token}: " + ", ".join(sites))
    for token, sites in sorted(repeated_frames.items()):
        candidates.append(f"REPEATED_FRAME {token}: " + ", ".join(sites))

    stats = {
        "human_pages": len(pages),
        "range_occurrences": sum(map(len, ranges.values())),
        "unique_ranges": len(ranges),
        "repeated_ranges": len(repeated_ranges),
        "frame_occurrences": sum(map(len, frames.values())),
        "unique_frames": len(frames),
        "repeated_frames": len(repeated_frames),
        "semantic_candidates": sum(
            item.startswith(
                ("OBSERVED_UNIVERSAL", "IMPLEMENTATION_PROMOTION", "ABSENCE_CLAIM", "UNLABELLED")
            )
            for item in candidates
        ),
        **{f"mentions_{name}": count for name, count in conflict_mentions.items()},
    }
    return stats, candidates


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--show-candidates", action="store_true")
    args = parser.parse_args()
    stats, candidates = audit(Path(args.root).resolve())
    print("STATS " + " ".join(f"{key}={value}" for key, value in stats.items()))
    if args.show_candidates:
        for candidate in candidates:
            print("REVIEW " + candidate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
