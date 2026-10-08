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
PUBLIC_DOCUMENT_PATTERN = re.compile(
    r"(?i)\b(?:LE\d{5}[A-Z]{2}|RA\d{5}[A-Z]{2}(?:_[A-Z_0-9]+)?|"
    r"ST[-_]\d{8}(?:[-_](?:REV\d+[-_])?(?:EN|IT|FR|ES|DE|NL)(?:\.pdf)?)?)\b"
)
PRIVATE_PATH_PATTERN = re.compile(
    r"(?i)(?:(?<![a-z0-9/:.])|(?<=file://))(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"
)
QUALIFIER = r"(?:installed|observed|physical|scanned|test|tested|captured|interviewed|light-control-only)"
DEVICE_ID_CONTEXT_PATTERN = re.compile(
    rf"(?ix)(?P<context>\b(?:(?P<qualifier>{QUALIFIER})\s+)?"
    rf"(?:(?P<device>devices?)(?:\s+(?P<label>ids?|identifiers?))?"
    rf"|(?P<unit>units?)(?:\s+(?P<unitlabel>ids?|identifiers?)))\b)"
)
BLOCKED_DEVICE_CONTEXT_PATTERN = re.compile(
    r"(?ix)\s+(?:types?|models?|classes?|families|firmware|catalog(?:ue)?|codes?)\b"
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
    public_documents = [(m.start(), m.end()) for m in PUBLIC_DOCUMENT_PATTERN.finditer(text)]
    seen: set[tuple[int, int]] = set()
    for context in DEVICE_ID_CONTEXT_PATTERN.finditer(plain):
        blocked = BLOCKED_DEVICE_CONTEXT_PATTERN.match(plain, context.end())
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
            # Exact public technical-sheet identifiers are not installed Device IDs.
            # Keep this exception narrow: arbitrary eight-hexadecimal filenames
            # and identifiers still require sanitization in installed contexts.
            if any(start <= token.start() and token.end() <= end for start, end in public_documents):
                continue
            key = (token.start(), token.end())
            if key in seen:
                continue
            seen.add(key)
            matches.append(SensitiveMatch("device_id", token.start(), token.end(),
                                          text[token.start():token.end()], "[DEVICE_ID]"))
    return sorted(matches, key=lambda match: (match.start, match.end))

# Concrete Markdown credential literals are sanitized even for published defaults.
# Numeric ranges and masks are abstract domains, not credential values.
CREDENTIAL_LITERAL_PATTERN = re.compile(r"(?i)\b(password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s+`([A-Za-z0-9]{4,})`")

# Property/value tables and prose may put punctuation, qualifications, or a
# missing space between a credential label and its literal. Retain the label
# and qualifications, while removing the value before structural parsing.
CREDENTIAL_TABLE_PATTERN = re.compile(
    r"(?im)^(\|[^|\n]{0,60}\b(?:password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b\s*\|\s*`?)([0-9]{4,})(?=[`; ,|])"
)
CREDENTIAL_UNLOCK_PATTERN = re.compile(
    r"(?i)(\b(?:installer\s+)?unlock\s+code\s*`?)([A-Za-z0-9_]{4,})(?=[`; ,.]|$)"
)
# This exact factory credential is named in F455 recovery prose without a
# repeated label. It is a credential, not an abstract protocol value.
CREDENTIAL_FACTORY_PATTERN = re.compile(r"(?i)\bbasic_gw\b")
# A qualified factory/default value can occur later in the password cell.
# Match the credential context, rather than an unrelated number or domain.
CREDENTIAL_QUALIFIED_DEFAULT_PATTERN = re.compile(
    r"(?i)(\b(?:password|passwd)\b[^|\n]{0,160}?\b(?:manufacturer documentation|factory)\s+(?:default|value)\s+`)([A-Za-z0-9_]{4,})(?=`)"
)

NETWORK_TRANSFORMS = (
    ("credential", CREDENTIAL_LITERAL_PATTERN, r"\1 `[REDACTED]`"),
    ("credential", CREDENTIAL_TABLE_PATTERN, r"\1[REDACTED]"),
    ("credential", CREDENTIAL_UNLOCK_PATTERN, r"\1[REDACTED]"),
    ("credential", CREDENTIAL_FACTORY_PATTERN, "[REDACTED]"),
    ("credential", CREDENTIAL_QUALIFIED_DEFAULT_PATTERN, r"\1[REDACTED]"),
    ("network_address", re.compile(rf"(?<![0-9]){OCTET}(?:\.{OCTET}){{3}}(?![0-9])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(rf"(?<![0-9#*]){OCTET}(?:\*{OCTET}){{3}}(?![0-9#*])"), "[NETWORK_ADDRESS]"),
    ("network_address", re.compile(r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{1,4}:){2,7}[0-9a-f]{0,4}(?![0-9a-f:])"), "[NETWORK_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?![0-9a-f])"), "[MAC_ADDRESS]"),
    ("hardware_id", re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"), "[INSTANCE_IDENTIFIER]"),
    ("person_identifier", re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"), "[PERSONAL_IDENTIFIER]"),
    ("other", PRIVATE_PATH_PATTERN, "[LOCAL_PATH]"),
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
