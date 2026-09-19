#!/usr/bin/env python3
"""Deterministic integrity checks derived from the Encyclopedia Core Values.

This checker enforces only rules that can be decided mechanically with high
confidence. Semantic truth, source authority, applicability, and contradiction
resolution remain review tasks and are intentionally not converted into hard
lint failures.
"""

from __future__ import annotations

import argparse
import ipaddress
import re
import sys
from pathlib import Path

from check_esg import human_pages


REQUIRED_FILES = (
    "project/encyclopedia-core-values.md",
    "project/encyclopedia-style-guide.md",
    "sources/manifest.yaml",
)

SAFE_CONTEXT = re.compile(
    r"\b(?:example|synthetic|illustrative|placeholder|redacted|documentation)\b",
    re.IGNORECASE,
)

OCTET = r"(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})"
IPV4 = re.compile(rf"(?<![0-9]){OCTET}(?:\.{OCTET}){{3}}(?![0-9])")
MAC = re.compile(
    r"(?i)(?<![0-9a-f])(?:[0-9a-f]{2}[:-]){5}[0-9a-f]{2}(?![0-9a-f])"
)
PRIVATE_USER_PATH = re.compile(
    r"(?i)(?:/home/[^/\s]+|/users/[^/\s]+|[a-z]:\\users\\[^\\\s]+)"
)
CREDENTIAL_ASSIGNMENT = re.compile(
    r"(?i)\b(?:password|passwd|secret|api[ _-]?key|access[ _-]?token|cookie)\b"
    r"\s*[:=]\s*[\"']?[^\s\"'<>]{4,}"
)
DEVICE_ID_CONTEXT = re.compile(
    r"(?i)\b(?:observed|captured|physical device id|device id|device identifier)\b"
)
HEX8 = re.compile(r"(?i)\b[0-9a-f]{8}\b")

PRIVATE_NETWORKS = tuple(
    ipaddress.ip_network(value)
    for value in (
        "10.0.0.0/8",
        "100.64.0.0/10",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.168.0.0/16",
    )
)

NON_IDENTIFYING_MACS = {
    "00:00:00:00:00:00",
    "00-00-00-00-00-00",
    "ff:ff:ff:ff:ff:ff",
    "ff-ff-ff-ff-ff-ff",
}


def safe_context(line: str) -> bool:
    return bool(SAFE_CONTEXT.search(line))


def is_private_ipv4(token: str) -> bool:
    address = ipaddress.ip_address(token)
    return any(address in network for network in PRIVATE_NETWORKS)


def check(root: Path) -> tuple[list[str], list[str], dict[str, int]]:
    objective: list[str] = []
    candidates: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            objective.append(f"REQUIRED_FILE {relative}: missing")

    pages = human_pages(root)
    for path in pages:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)

        for number, line in enumerate(text.splitlines(), 1):
            explicit_safe_context = safe_context(line)

            for match in IPV4.finditer(line):
                token = match.group(0)
                if is_private_ipv4(token) and not explicit_safe_context:
                    objective.append(
                        f"PRIVATE_IPV4 {rel}:{number}: {token} "
                        "requires an explicit synthetic/example context or a placeholder"
                    )

            for match in MAC.finditer(line):
                token = match.group(0)
                if (
                    token.lower() not in NON_IDENTIFYING_MACS
                    and not explicit_safe_context
                ):
                    objective.append(
                        f"MAC_ADDRESS {rel}:{number}: concrete MAC-like value {token}"
                    )

            for match in PRIVATE_USER_PATH.finditer(line):
                token = match.group(0)
                if not explicit_safe_context:
                    objective.append(
                        f"PRIVATE_PATH {rel}:{number}: user-specific path {token}"
                    )

            if CREDENTIAL_ASSIGNMENT.search(line) and not explicit_safe_context:
                candidates.append(
                    f"CREDENTIAL_CANDIDATE {rel}:{number}: review possible concrete credential"
                )

            if DEVICE_ID_CONTEXT.search(line) and not explicit_safe_context:
                for match in HEX8.finditer(line):
                    candidates.append(
                        f"INSTANCE_ID_CANDIDATE {rel}:{number}: {match.group(0)}"
                    )

    stats = {
        "human_pages": len(pages),
        "objective_failures": len(objective),
        "review_candidates": len(candidates),
    }
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
