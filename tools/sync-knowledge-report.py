#!/usr/bin/env python3
"""Mirror the irodori-table knowledge refresh report into this book.

Fetches the generated registry/knowledge-refresh-report.md from the table
repo's main branch, wraps it with a provenance header, and rewrites
src/knowledge-refresh-report.md. Idempotent: running it twice produces the
same bytes, so the sync workflow only commits when the upstream report
actually changed. Stdlib only.
"""
import sys
import urllib.request
from pathlib import Path

SOURCE_URL = (
    "https://raw.githubusercontent.com/hjosugi/irodori-table/main/"
    "registry/knowledge-refresh-report.md"
)
TARGET = Path(__file__).resolve().parent.parent / "src" / "knowledge-refresh-report.md"

HEADER = """# Knowledge Refresh Report

Mirrored from the `irodori-table` generated report
[`registry/knowledge-refresh-report.md`](https://github.com/hjosugi/irodori-table/blob/main/registry/knowledge-refresh-report.md),
produced by the monthly scheduled knowledge refresh (`knowledge-refresh.yml`,
1st of each month). The source of truth is the table repo; this mirror is
refreshed automatically by `knowledge-report-sync.yml` (daily check and
manual dispatch).
"""


def main() -> int:
    request = urllib.request.Request(
        SOURCE_URL, headers={"User-Agent": "irodori-docs-report-sync"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        upstream = response.read().decode("utf-8")

    lines = upstream.splitlines()
    if not lines or not lines[0].startswith("# "):
        print("unexpected upstream format: missing title heading", file=sys.stderr)
        return 1
    body = "\n".join(lines[1:]).lstrip("\n")

    rendered = f"{HEADER}\n{body}\n"
    if TARGET.exists() and TARGET.read_text(encoding="utf-8") == rendered:
        print("knowledge-refresh-report: up to date")
        return 0
    TARGET.write_text(rendered, encoding="utf-8")
    print(f"knowledge-refresh-report: updated {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
