# Import And Migration Studio

Import/export and migration planning are separate workflows: import moves data
into a table, while Migration Studio plans schema and data verification steps.

## Import

Preview incoming CSV, TSV, JSON, and NDJSON data before writing it. Check inferred
columns, target table names, null handling, and delimiter/quote settings before
running an import.

## Migration Studio

Migration Studio compares source and target metadata, builds preview SQL, and
surfaces destructive changes before execution. The reusable planning and
data-diff primitives live in `irodori-migration`; the desktop app supplies live
connections, jobs, cancellation, and UI review.

## Verification

Use row counts, checksums, bucket fingerprints, and row-level diffs to verify a
migration. For very large tables, prefer bucketed verification first and inspect
only the failed buckets.
