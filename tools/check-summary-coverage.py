#!/usr/bin/env python3
"""Fail when a src/**/*.md page is missing from SUMMARY.md.

mdBook only renders chapters listed in SUMMARY.md. A page that exists in src/
but is not listed silently disappears from the published site, and every link
to it returns 404 (see issue #6). Stdlib only; run from anywhere.
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"


def main() -> int:
    summary = (SRC / "SUMMARY.md").read_text(encoding="utf-8")
    listed = set()
    for match in re.finditer(r"\]\(([^)#]+\.md)\)", summary):
        target = (SRC / match.group(1)).resolve()
        if target.exists():
            listed.add(target)

    missing = [
        page.relative_to(SRC)
        for page in sorted(SRC.rglob("*.md"))
        if page.name != "SUMMARY.md" and page.resolve() not in listed
    ]

    if missing:
        print(
            "Pages not listed in SUMMARY.md — mdBook will not render them,"
            " so links to them 404 on the published site:"
        )
        for rel in missing:
            print(f"  src/{rel}")
        print("\nAdd each page to src/SUMMARY.md, or move it out of src/.")
        return 1

    print(f"SUMMARY coverage OK: {len(listed)} pages listed, no unlisted src pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
