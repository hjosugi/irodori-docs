# Data Verification And Migration

Last checked: 2026-06-28 JST.

This page records the current product contract for migration planning, data
verification, and result-grid repair helpers. It separates what is implemented
today from the target live diff architecture.

## Current Desktop Scope

The desktop app currently ships SQL generation and review workflows, not an
end-to-end data mover.

- **Migration Studio** generates a plan, source SQL, target SQL, diff SQL, and a
  runbook.
- The default migration shape is Hive -> Snowflake.
- Planner engines include Hive, Snowflake, PostgreSQL, Oracle, MySQL/MariaDB,
  Redshift, Databricks/Spark SQL, Trino/Presto, DuckDB/DuckDB-Wasm, Apache
  Iceberg REST, and AWS S3 Tables.
- Generated validation SQL uses source and target row-hash manifests, row count,
  key count, min/max hash fingerprints, manifest tables, and row-level diff SQL.
- The desktop planner exposes Parquet/CSV extraction formats. The shared
  `irodori-sql` migration helpers also include TSV-oriented load snippets for
  workflows where Hive text exports are unavoidable.
- DuckDB/Iceberg paths generate `INSTALL/LOAD iceberg`, `CREATE SECRET`, and
  `ATTACH ... TYPE ICEBERG` patterns for local or browser-side DuckDB compute.

The current planner does not connect to both databases, execute the generated
SQL, or reconcile results by itself. The user reviews the SQL/runbook and runs it
through the normal query workflow or an external migration runner.

## Result-Grid Repair Workflow

Editable results are intentionally review-oriented.

- The grid uses **Save Changes** for pending edits.
- Editable updates require a direct single-table result with a visible primary
  key or unique key.
- Refresh with unsaved result changes asks for confirmation before discarding
  work.
- **Row SQL** turns the selected result row into a reviewable transaction:

```sql
-- Generated from the selected result row. Review before running.
-- Edit the SET values, then run this transaction.
BEGIN;
UPDATE "schema"."table"
SET
  "column" = 'new value'
WHERE
  "id" = 42
;
COMMIT;
```

SQL Server uses `BEGIN TRANSACTION;` and bracket identifiers; MySQL/MariaDB/TiDB
use backticks. JSON-like result values are serialized as SQL string literals
before insertion into the editor. The generated SQL is never executed
automatically.

## Editor Support

The SQL editor is CodeMirror 6 based. Current editor behavior includes:

- dialect-aware highlighting and completion;
- Vim mode;
- format and comment toggle commands;
- run current, run selection, and run all flows;
- query history;
- search and replace through the CodeMirror search panel opened by
  `Ctrl`/`Cmd+F`.

## Target Live Diff Architecture

The future live data-diff capability should be a separate execution boundary. It
should compare two sources without pulling whole tables unless the cheap gates
fail.

The target tiers are:

1. **Count and table fingerprint**: row count plus order-independent aggregate of
   row hashes.
2. **Partition or hash-bucket fingerprint**: localize mismatches to small key
   ranges.
3. **Failed-bucket row diff**: compare `(key, row_hash)` manifests and fetch full
   rows only for changed keys.

For 100B-row scale, the product contract is to push hashing and bucketing into
the source engines, stream narrow manifests, spill to disk when needed, and keep
the UI cancellable. The UI should present summary status, bucket heatmap, row
list, cell-level differences, and exportable evidence.

## Not Yet Implemented

- Live source-target execution and reconciliation.
- Recursive bucket localization.
- Bucket heatmap UI.
- Headless `/v1/diff` API.
- Automatic reconciliation script export beyond selected-row `UPDATE` generation.

## Safety Rules

- Keep migration credentials in connection profiles or secret storage, not in
  shareable URLs or exported runbooks.
- For DuckDB-Wasm and Iceberg REST, verify endpoint reachability and CORS before
  relying on a browser-only flow.
- Prefer Parquet for Hive -> Snowflake. Use text formats only when unavoidable,
  and keep delimiter/null-token policies explicit.
- Keep generated Row SQL in the editor for human review before execution.
