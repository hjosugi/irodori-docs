# irodori-docs

Documentation for [Irodori Table](https://github.com/hjosugi/irodori-table),
published as an [mdBook](https://rust-lang.github.io/mdBook/).

- **Online:** https://hjosugi.github.io/irodori-docs/ (deployed from `main` via GitHub Pages)
- **Markdown:** every page is a plain `.md` under [`src/`](src/) — clone or download the repo for the raw source
- **PDF:** open the book online and use the **print icon** (top bar) → *Save as PDF*

## Build locally

```sh
cargo install mdbook
mdbook serve   # live preview at http://localhost:3000
mdbook build   # static site in ./book
```

## Layout

- `src/SUMMARY.md` — the table of contents
- `src/*.md` — hand-written planning, architecture, reference, and policy docs
- `src/cheatsheets/`, `src/data-source-support-status.md` — **generated** reference
  pages that originate from the irodori-table repo's tooling
  (`tools/docs/support-status.mjs`, `tools/knowledge/cheatsheet.mjs`) and are
  synced into this repo.

The hand-written docs are sourced here; the generated pages are mirrored from
irodori-table so the published book stays in one place.

Public product pages such as support, privacy, disclaimer, distribution, and
store/package registration also live here. The `irodori-table` repository keeps
only app source, packaging templates, and generated/app-consumed documentation.
