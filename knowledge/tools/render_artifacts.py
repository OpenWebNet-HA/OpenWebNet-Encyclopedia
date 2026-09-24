"""Render deterministic public Machine KB artifacts exclusively from the shared IR."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from serialization import jsonl_bytes

RENDER_FORMAT_VERSION = "0.1.0"


def inline_markdown(nodes: list[dict[str, Any]]) -> str:
    result: list[str] = []
    for node in nodes:
        kind = node["type"]
        if kind in {"text", "escape"}:
            result.append(node["text"])
        elif kind == "codespan":
            result.append(f"`{node['text']}`")
        elif kind in {"strong", "em", "del"}:
            marker = {"strong": "**", "em": "*", "del": "~~"}[kind]
            result.append(marker + inline_markdown(node["children"]) + marker)
        elif kind == "link":
            result.append(f"[{inline_markdown(node['children'])}]({node['target']})")
        elif kind == "image":
            result.append(f"![{inline_markdown(node['children'])}]({node['target']})")
        elif kind == "break":
            result.append("  \n")
        else:
            raise ValueError(f"unsupported IR inline node {kind}")
    return "".join(result)


def block_markdown(block: dict[str, Any], indent: str = "") -> str:
    kind = block["type"]
    if kind == "paragraph":
        return indent + inline_markdown(block["inline"])
    if kind == "code":
        fence = "```"
        while fence in block["text"]:
            fence += "`"
        language = block["language"]
        return f"{indent}{fence}{language}\n{block['text']}\n{indent}{fence}"
    if kind == "table":
        header = "| " + " | ".join(inline_markdown(cell["inline"]) for cell in block["header"]) + " |"
        separator = "| " + " | ".join("---" for _ in block["header"]) + " |"
        rows = ["| " + " | ".join(inline_markdown(cell["inline"]) for cell in row) + " |" for row in block["rows"]]
        return "\n".join([indent + header, indent + separator, *(indent + row for row in rows)])
    if kind == "list":
        lines: list[str] = []
        for position, item in enumerate(block["items"], block["start"] or 1):
            marker = f"{position}." if block["ordered"] else "-"
            child = "\n\n".join(block_markdown(value, indent + "  ") for value in item["blocks"])
            lines.append(f"{indent}{marker} {child.lstrip()}")
        return "\n".join(lines)
    if kind == "blockquote":
        body = "\n\n".join(block_markdown(value) for value in block["blocks"])
        return "\n".join(f"> {line}" if line else ">" for line in body.splitlines())
    if kind == "rule":
        return indent + "---"
    raise ValueError(f"unsupported IR block node {kind}")


def block_text(block: dict[str, Any]) -> str:
    """Use Markdown structure as neutral plain text for retrieval; do not add interpretation."""
    if block["type"] == "code":
        return block["text"]
    return block_markdown(block)


def qualifications(section: dict[str, Any]) -> dict[str, list[str]]:
    names = {"applicability": "applicability_cues", "cautions": "caution_cues",
             "uncertainty": "uncertainty_cues", "provenance_references": "provenance_cues"}
    return {target: sorted({item for block in section["blocks"] for item in block[source]})
            for source, target in names.items()}


def section_path(document: dict[str, Any], section: dict[str, Any]) -> list[str]:
    by_id = {entry["id"]: entry for entry in document["sections"]}
    result = []
    current: dict[str, Any] | None = section
    while current:
        if current["title"]:
            result.append(current["title"])
        current = by_id.get(current["parent"])
    return list(reversed(result))


def corpus(ir: dict[str, Any]) -> bytes:
    lines = ["# OpenWebNet Encyclopedia Machine KB Corpus", "",
             "Generated deterministically from canonical documentation. Practical Guides are excluded.", ""]
    for document in ir["documents"]:
        context = document["namespace_context"]
        lines.extend([f"# Document: {document['id']}", "", f"Source path: `{document['path']}`",
                      f"Namespace context: `{context['namespace']}`", f"Area: `{context['area']}`", ""])
        for section in document["sections"]:
            if not section["title"] and not section["blocks"]:
                continue
            heading = "#" * min(section["level"] + 1, 6)
            title = section["title"] or "Preamble"
            lines.extend([f"{heading} {title}", "", f"Section ID: `{section['id']}`", ""])
            cue = qualifications(section)
            for label, values in (("Applicability cues", cue["applicability_cues"]),
                                  ("Cautions", cue["caution_cues"]),
                                  ("Uncertainty", cue["uncertainty_cues"]),
                                  ("Provenance cues", cue["provenance_cues"])):
                if values:
                    lines.append(f"{label}: " + ", ".join(f"`{value}`" for value in values))
            if any(cue.values()):
                lines.append("")
            lines.extend(value for block in section["blocks"] for value in (block_markdown(block), ""))
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def chunk_records(ir: dict[str, Any], identities: dict[str, str],
                  section_references: dict[str, list[str]],
                  namespace_ids: dict[str, str]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    records = []
    candidate = emitted = empty = 0
    for document in ir["documents"]:
        for section in document["sections"]:
            candidate += 1
            if not section["blocks"]:
                empty += 1
                continue
            identity = identities.get(section["id"])
            if identity is None:
                raise ValueError(f"missing curated retrieval chunk identity for {section['id']}")
            cue = qualifications(section)
            text = "\n\n".join(block_text(block) for block in section["blocks"])
            if not text.strip():
                empty += 1
                continue
            records.append({
                "document_id": document["id"], "format_version": RENDER_FORMAT_VERSION,
                "id": identity, "kind": "retrieval_chunk", "label": section["title"] or "Preamble",
                "namespace_context": section["namespace_context"], "privacy": section["privacy"],
                "provenance": section["provenance"], "qualification_cues": cue,
                "reference_ids": sorted({document["source_id"], namespace_ids[document["id"]],
                                         *section_references.get(section["id"], [])}, key=str.encode),
                "section_id": section["id"], "section_path": section_path(document, section),
                "source_path": document["path"], "text": text,
            })
            emitted += 1
    records.sort(key=lambda record: record["id"].encode("ascii"))
    return records, {"candidate_sections": candidate, "empty_sections": empty, "emitted_chunks": emitted}


def load_chunk_identities(path: Path) -> dict[str, str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or any(not isinstance(key, str) or not isinstance(item, str) for key, item in value.items()):
        raise ValueError("chunk identity mapping must be a JSON object of strings")
    return value


def bootstrap_chunk_identities(ir: dict[str, Any]) -> dict[str, str]:
    sections = [section["id"] for document in ir["documents"] for section in document["sections"] if section["blocks"]]
    return {section_id: f"ownkb:chunk:r{number:06d}" for number, section_id in enumerate(sorted(sections), 1)}
