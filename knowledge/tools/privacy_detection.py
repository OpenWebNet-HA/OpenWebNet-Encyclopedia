"""Central privacy classification and sanitization semantics.

The detector is contextual: it recognizes installed Device identifiers from
their governing words and formatting, while leaving unrelated public
eight-hexadecimal values alone.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

OCTET = r"(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})"
HEX8_PATTERN = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{8}(?![0-9a-f])")
MARKUP = frozenset(chr(96) + "*_[]()")
QUALIFIER = r"(?:installed|observed|physical|scanned|test|tested|captured|interviewed|light-control-only)"
DEVICE_ID_CONTEXT_PATTERN = re.compile(
    rf"(?ix)(?P<context>\b(?:(?P<qualifier>{QUALIFIER})\s+)?"
    rf"(?:(?P<device>devices?)(?:\s+(?P<label>ids?|identifiers?))?"
    rf"|(?P<unit>units?)(?:\s+(?P<unitlabel>ids?|identifiers?)))\b)"
)
DEVICE_ID_PATTERN = re.compile(
    rf"(?ix)\b(?:{QUALIFIER}\s+)?(?:device|unit)(?:\s+(?:id|identifier))?\b"
    rf"(?!\s+(?:type|model|class|family|firmware|catalog(?:ue)?|code))"
    rf"[^0-9a-f\n]{{0,48}}(?P<value>[0-9a-f]{{8}})"
)
DEVICE_ID_LIST_PATTERN = re.compile(
    rf"(?ix)\b(?:(?:{QUALIFIER})\s+)?devices?(?:\s+(?:ids?|identifiers?))?\b"
    rf"(?!\s+(?:types|models|classes|families|firmware|catalog(?:ue)?|codes))"
    rf"(?:(?!\n\s*\n).){{0,420}}?(?P<value>[0-9a-f]{{8}})"
)

@dataclass(frozen=True)
class SensitiveMatch:
    value_class: str
    start: int
    end: int
    value: str
    replacement: str

def _plain_markdown(text: str) -> str:
    return "".join(" " if char in MARKUP else char for char in text)

def installed_device_id_matches(text: str) -> list[SensitiveMatch]:
    plain = _plain_markdown(text)
    matches: list[SensitiveMatch] = []
    seen: set[tuple[int, int]] = set()
    for context in DEVICE_ID_CONTEXT_PATTERN.finditer(plain):
        tail = plain[context.end():]
        blocked = re.match(r"(?ix)\s+(?:types?|models?|classes?|families|firmware|catalog(?:ue)?|codes?)\b", tail)
        if blocked:
            continue
        explicit = bool(context.group("qualifier") or context.group("label") or context.group("unitlabel"))
        plural = (context.group("device") or context.group("unit") or "").lower().endswith("s")
        limit = 420 if explicit or plural else 96
        end = min(len(plain), context.end() + limit)
        blank = re.search(r"\n\s*\n", plain[context.end():end])
        if blank:
            end = context.end() + blank.start()
        field_boundary = re.search(r'(?<!\\)"|[{}]', plain[context.end():end])
        if field_boundary:
            end = context.end() + field_boundary.start()
        if not explicit and not plural:
            stop = re.search(r"[.!?]|\n", plain[context.end():end])
            if stop:
                end = context.end() + stop.start()
        for token in HEX8_PATTERN.finditer(plain, context.end(), end):
            key = (token.start(), token.end())
            if key in seen:
                continue
            seen.add(key)
            matches.append(SensitiveMatch("device_id", token.start(), token.end(),
                                          text[token.start():token.end()], "[DEVICE_ID]"))
    return sorted(matches, key=lambda match: (match.start, match.end))

NETWORK_TRANSFORMS = (
    ("network_address", re.compile(rf"(?<![0-9]){OCTET}(?:\.{OCTET}){{3}}(?![0-9])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(rf"(?<![0-9]){OCTET}(?:\*{OCTET}){{3}}(?![0-9])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}(?![0-9a-f:])"), "[NETWORK_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?![0-9a-f])"), "[MAC_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"), "[INSTANCE_IDENTIFIER]"),
    ("person_identifier", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"), "[PERSONAL_IDENTIFIER]"),
    ("other", re.compile(r"(?i)(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"), "[LOCAL_PATH]"),
    ("credential", re.compile(r"(?i)\b(password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s*[:=]\s*[\"']?[^\s\"'<>]{4,}"), r"\1=[REDACTED]"),
)

def device_id_values(text: str) -> set[str]:
    return {match.value for match in installed_device_id_matches(text)}

def sanitize_privacy_text(text: str) -> tuple[str, list[str]]:
    removed: set[str] = set()
    for value_class, pattern, replacement in NETWORK_TRANSFORMS:
        text, count = pattern.subn(replacement, text)
        if count:
            removed.add(value_class)
    matches = installed_device_id_matches(text)
    if matches:
        pieces = []
        cursor = 0
        for match in matches:
            pieces.extend((text[cursor:match.start], match.replacement))
            cursor = match.end
        pieces.append(text[cursor:])
        text = "".join(pieces)
        removed.add("device_id")
    return text, sorted(removed)
