"""Structural claim atomicity checks and source-context materialization."""
from __future__ import annotations

import re

DEICTIC = re.compile(r"^(?:this|these|those|it|they|such|the former|the latter)\b", re.I)
LEAD_IN = re.compile(r"\b(?:defines|establishes|includes|contains|comprises|as follows|following)\s*:?$", re.I)
VERB = re.compile(
    r"\b(?:is|are|was|were|be|being|been|has|have|had|does|do|did|must|shall|"
    r"should|can|may|will|reports?|defines?|establishes?|includes?|contains?|"
    r"uses?|selects?|sets?|maps?|identifies?|represents?|requires?|supports?|"
    r"provides?|preserves?|applies?|enters?|finishes?|exercises?|offers?|declares?|"
    r"prohibits?|retains?|means?|occupies?|corresponds?|remains?|keeps?|fails?|"
    r"returns?|sends?|receives?|stores?|links?|matches?|distinguishes?|records?)\b",
    re.I,
)
WORD = re.compile(r"[A-Za-z0-9]+")
STRIP_MARKUP = re.compile(r"[^A-Za-z0-9]+")

def atomicity_reasons(statement: str) -> list[str]:
    value = statement.strip()
    reasons: list[str] = []
    if not value:
        return ["empty"]
    if value.endswith(":"):
        reasons.append("bare-lead-in")
    if DEICTIC.search(value):
        reasons.append("deictic-referent")
    if LEAD_IN.search(value):
        reasons.append("missing-defined-content")
    words = WORD.findall(value)
    if len(words) < 5 or (len(words) < 16 and not VERB.search(value)):
        reasons.append("non-propositional-fragment")
    return sorted(set(reasons))

def block_text(block: dict) -> str:
    kind = block.get("type")
    if kind == "paragraph":
        return str(block.get("text", "")).strip()
    if kind == "table":
        rows = [block.get("header", [])] + list(block.get("rows", []))
        return "; ".join(" | ".join(str(cell).strip() for cell in row) for row in rows if row)
    if kind == "list":
        values = []
        for item in block.get("items", []):
            text = " ".join(block_text(child) for child in item.get("blocks", []))
            if text:
                values.append(text)
        return "; ".join(values)
    return str(block.get("text", "")).strip()

def _tokens(value: str) -> set[str]:
    return {token.casefold() for token in WORD.findall(value) if len(token) > 1}

def best_block_indexes(statement: str, section: dict) -> list[int]:
    target = _tokens(statement)
    ranked = []
    for index, block in enumerate(section.get("blocks", [])):
        text = block_text(block)
        tokens = _tokens(text)
        overlap = len(target & tokens)
        containment = int(STRIP_MARKUP.sub("", statement).casefold() in
                          STRIP_MARKUP.sub("", text).casefold())
        ranked.append((containment, overlap, -abs(len(tokens)-len(target)), -index, index))
    if not ranked:
        raise ValueError("claim section has no source blocks")
    best = max(ranked)[-1]
    return [best]

def materialize_statement(statement: str, section: dict, block_indexes: list[int]) -> str:
    if not atomicity_reasons(statement):
        return statement.strip()
    blocks = section.get("blocks", [])
    index = block_indexes[0]
    block = blocks[index]
    context = block_text(block)
    if statement.strip().endswith(":") and index + 1 < len(blocks):
        following = block_text(blocks[index + 1])
        if following:
            context = f"{context} {following}"
    assertion = statement.strip().rstrip(" :;.")
    kind = str(block.get("type", "block")).replace("_", " ")
    return (f"In {section['title']}, the governing source {kind} context is: {context} "
            f"Within that context, the atomic assertion is: {assertion}.")


def validate_atomicity_review(statement: str, section: dict, review: dict) -> str:
    if set(review) != {"block_indexes", "mode", "review_status"}:
        raise ValueError("atomicity review has unknown or missing fields")
    if review["review_status"] != "reviewed-phase16b":
        raise ValueError("atomicity review is not approved")
    expected = best_block_indexes(statement, section)
    if review["block_indexes"] != expected:
        raise ValueError("atomicity source block mapping is stale")
    reasons = atomicity_reasons(statement)
    expected_mode = "materialized" if reasons else "self_contained"
    if review["mode"] != expected_mode:
        raise ValueError("atomicity disposition disagrees with structural contract")
    rendered = materialize_statement(statement, section, expected)
    residual = atomicity_reasons(rendered)
    if residual:
        raise ValueError("materialized claim is still structurally incomplete: " + ",".join(residual))
    return rendered
