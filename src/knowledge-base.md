# Local Knowledge Base

Irodori should keep a local, searchable memory of database specifications, release notes, DB-client product expectations, AI integration docs, and implementation notes.

The goal is to make future implementation and bug fixing less dependent on memory or scattered browser tabs.

## Storage

- Generated SQLite DB: `knowledge/irodori-knowledge.sqlite`
- Schema: `knowledge/schema.sql`
- Source registry: `knowledge/sources.json`
- Refresh script: `tools/knowledge/refresh.mjs`
- Analysis script: `tools/knowledge/analyze.mjs`
- Query script: `tools/knowledge/query.mjs`

The SQLite DB is intentionally ignored by Git. The schema and source registry are tracked.

## Task Navigation

Use this document for the knowledge-base system itself: source registry shape,
refresh/query workflow, source policy, and what kinds of facts belong in the local
store. It should not duplicate the product backlog.

- Product capability strategy belongs in
  [data-source-coverage-strategy.md](data-source-coverage-strategy.md) and
  [data-source-support-status.md](data-source-support-status.md).
- Release/task direction belongs in [roadmap-1.0.md](roadmap-1.0.md).
- Current code ownership belongs in
  [implementation-architecture.md](implementation-architecture.md).
- Parallel-worker ownership and handoffs belong in
  [parallel-agent-architecture.md](parallel-agent-architecture.md) and the
  table repo's `registry/agent-workstreams.json`.

When a task depends on vendor behavior or DB-client precedent, query this knowledge
base first, then record the implementation outcome in the owning task doc. A
knowledge snapshot or source-registry update is evidence for future work; it does
not by itself close a product feature without linked implementation and verification.

## Source Registry Schema

`knowledge/sources.json` is a JSON array. Each entry is one stable source that can
be registered into the `sources` table from `knowledge/schema.sql`.

Required fields:

- `id`: stable lowercase kebab-case identifier. Do not rename it after snapshots or
  facts may reference it; add a replacement source instead.
- `name`: human-readable source name.
- `product`: product, project, or service this source documents.
- `category`: source family. Current values are `database`, `db_client`, `ai`, and
  `tooling`.
- `sourceType`: document kind. Current values are `spec`, `release_notes`,
  `driver_docs`, `product_docs`, and `oss_project`.
- `url`: canonical upstream URL. It must be unique across the registry.

Optional fields:

- `official`: defaults to `true`; set to `false` only for clearly labeled
  non-official references.
- `cadence`: refresh expectation such as `weekly` or `monthly`; defaults to
  `monthly`.
- `enabled`: defaults to `true`; set to `false` to keep a source registered but
  skip network refresh.
- `fetchHeaders`: extra HTTP request headers for this source, merged over the
  refresh defaults (`accept`, `accept-language: en`, and the bot user-agent).
  Use it for upstreams that need a specific header to serve stable content.
- `notes`: short reason this source matters to Irodori implementation work.

The refresh script maps `sourceType` to the SQLite `source_type` column and keeps
`official`, `cadence`, `enabled`, and `notes` synchronized on every run.

## Usage

Initialize the DB and register sources without network access:

```bash
node tools/knowledge/refresh.mjs --no-fetch
```

Fetch the first few sources:

```bash
node tools/knowledge/refresh.mjs --limit 5
```

Fetch one source:

```bash
node tools/knowledge/refresh.mjs --source sqlite-changes
```

List registered sources:

```bash
node tools/knowledge/query.mjs
```

Search snapshots:

```bash
node tools/knowledge/query.mjs "ALTER TABLE"
```

Generate local facts and implementation notes from the latest stored snapshots:

```bash
node tools/knowledge/analyze.mjs
```

Preview generated facts without writing:

```bash
node tools/knowledge/analyze.mjs --dry-run
```

Analyze only text segments added since the previous stored snapshot for each
source. This is the recommended mode for routine refreshes because it focuses
implementation notes on new upstream behavior:

```bash
node tools/knowledge/analyze.mjs --changed-only
```

On the first snapshot for a source, `--changed-only` falls back to full analysis
so the source can be seeded. Add `--strict-changed` to skip sources without a
previous snapshot.

List or search generated facts and implementation notes:

```bash
node tools/knowledge/query.mjs --facts auth
node tools/knowledge/query.mjs --notes driver
```

## What To Store

- Official release notes and migration notes.
- SQL syntax/reference pages.
- Non-SQL source references: Cypher, time-series SQL/native query docs, document/KV/search APIs, and distributed SQL operational metadata.
- Catalog/introspection references.
- Driver documentation and behavior changes.
- DB client feature docs and market scans.
- Source-specific GUI docs such as Neo4j Browser, InfluxDB UI/Data Explorer, MongoDB Compass, RedisInsight, and DbGate.
- AI/Copilot/MCP integration docs.
- Manual facts discovered while fixing bugs.
- Implementation notes linking a source fact to an Irodori component.

## Source Policy

- Prefer official docs and release notes.
- Keep coverage across database specs, database release notes, DB-client product
  docs, AI/MCP references, and type/tooling references.
- Use versioned URLs where the upstream publishes stable versioned specs.
- Keep IDs stable even if a URL redirects or an upstream page is renamed.
- Add new `category` or `sourceType` values only with a matching documentation
  update here and downstream handling in the refresh/query code when needed.
- Run JSON validation and `node tools/knowledge/refresh.mjs --no-fetch` before
  marking registry changes done.
- Store URL, source product, fetch time, and hash for every snapshot.
- Summarize implementation facts in our own words.
- Do not store proprietary docs that we do not have rights to retain.
- Do not treat scraped docs as vendored source code.

## Automation Direction

- Local: run the refresh script manually while developing.
- Scheduled: the `knowledge-refresh.yml` GitHub Actions job runs on the 1st of
  each month, fetches all enabled sources, regenerates the cheatsheets and the
  app knowledge pack, and opens one consolidated PR whose body is the run
  digest. The digest is committed as `registry/knowledge-refresh-report.md` and
  mirrored automatically to
  [knowledge-refresh-report.md](knowledge-refresh-report.md) by this repo's
  `knowledge-report-sync.yml` workflow (daily check and manual dispatch) — no
  manual docs step remains in the monthly cycle.
- Static delivery: the app never fetches upstream docs. `tools/knowledge/pack.mjs`
  derives `registry/knowledge-pack.json` and the app-bundled copy from the
  committed `knowledge/pack-facts.json`; the in-app Knowledge panel reads the
  bundled pack and can refresh on demand from the published registry copy.
- Large index builds: source snapshots, generated facts, implementation notes,
  schema metadata, and query-history search indexes must be built through the
  shared job runtime with progress, cancellation, checkpoint/resume, bounded
  memory, and disk-backed state where needed.
- Smarter extraction: `tools/knowledge/analyze.mjs` starts with deterministic
  rule-based classification for versions, breaking changes, SQL syntax,
  authentication, metadata, result UI, visualization, and driver-impacting
  changes. Add per-product extractors when a source needs higher precision.
- ML/evaluation: any model-ranking or provider-evaluation dataset derived from
  knowledge snapshots must record source IDs, snapshot hashes, privacy inputs,
  metrics, and artifact hashes so runs are reproducible and auditable.
- Integration: surface relevant facts in the app when implementing a dialect feature or debugging a query issue.
