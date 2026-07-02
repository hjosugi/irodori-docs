# Results Grid And Export

The result grid is optimized for repeated inspection, copying, and export from
large result sets.

## Inspecting Results

- Scroll large pages without loading the entire result into memory.
- Use row details when a record is wider than the visible grid.
- Keep filters and sorting scoped to the loaded page unless a server-side
  workflow is explicitly available.

## Copy And Export

Use copy for small selected ranges. Use export for reproducible files:

- CSV/TSV with header and delimiter controls
- JSON and NDJSON
- SQL insert/upsert scripts where supported
- Avro and Parquet for columnar workflows

Native save dialogs are used by desktop exports, including spreadsheet-friendly
formats.
