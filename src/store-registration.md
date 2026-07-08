# Store and Package Registration

This is the public registration pack for Irodori Table. It collects the text,
URLs, IDs, assets, and per-channel checklist needed for app stores and package
managers. Keep secrets, tax/banking data, personal addresses, signing
certificates, app-specific passwords, and store account IDs out of this file.
Use a private local note or private archive for operational submission notes.

Current public release state:

- stable GitHub Release: `v0.7.32`;
- latest lightweight prerelease: `v0.7.34`;
- current `v0.7.x` assets: Linux AppImage only.

## Public listing metadata

| Field | Value |
| --- | --- |
| Product name | Irodori Table |
| Generic name | SQL workbench / database client |
| App identifier | `dev.irodori.table` |
| Repository | <https://github.com/hjosugi/irodori-table> |
| Homepage | <https://hjosugi.github.io/irodori-docs/> |
| Releases | <https://github.com/hjosugi/irodori-table/releases> |
| Documentation | <https://hjosugi.github.io/irodori-docs/> |
| Support URL | <https://hjosugi.github.io/irodori-docs/support.html> |
| Privacy URL | <https://hjosugi.github.io/irodori-docs/privacy.html> |
| Disclaimer URL | <https://hjosugi.github.io/irodori-docs/disclaimer.html> |
| License | `MIT OR 0BSD` |
| Source license URL | <https://github.com/hjosugi/irodori-table/blob/main/LICENSE> |
| Category | Developer Tools, Database, Productivity |
| Age rating baseline | Developer tool; no user-generated public content |
| Paid content | None |
| Ads / tracking | None in this repository |
| Account required | No hosted Irodori account required |
| Primary binary | Tauri desktop app |
| Headless binary | `irodori-server` from historical `irodori-kit v0.5.0` |

## Package IDs

| Channel | Suggested ID |
| --- | --- |
| Tauri app identifier | `dev.irodori.table` |
| GitHub Releases | `irodori-table` |
| Homebrew cask | `irodori-table` |
| Scoop | `irodori-table` |
| winget | `Irodori.Table` |
| Chocolatey | `irodori-table` |
| AUR binary package | `irodori-table-bin` |
| Flatpak | `dev.irodori.table` |
| Snap | `irodori-table` |
| crates.io binary crate | None yet; `irodori-server` is git-installable from `irodori-kit` |

## Listing copy

Short description:

> Open-source SQL workbench for querying, inspecting, and editing data across
> multiple database engines.

Japanese short description:

> 複数のデータベースを軽く扱うためのオープンソース SQL ワークベンチ。

Long description:

> Irodori Table is an open-source desktop database workbench built with Rust,
> Tauri, React, and CodeMirror. It focuses on fast SQL editing, schema-aware
> completion, Vim-friendly keyboard workflows, large-result browsing, query plan
> inspection, import/export, and extension-ready database connectivity.
>
> The app is local-first and does not require a hosted Irodori account. It
> connects to database servers, local files, and optional AI/model providers only
> when configured by the user.
>
> Irodori Table is currently a development preview. Review SQL, backups, and
> target connections before running destructive commands.

Japanese long description:

> Irodori Table は Rust / Tauri / React / CodeMirror で作られた
> オープンソースのデスクトップ DB ワークベンチです。SQL 編集、schema-aware
> completion、Vim に配慮したキーボード操作、大きな結果セットの閲覧、query plan
> の確認、import/export、拡張可能な接続機構を重視しています。
>
> ホスト型の Irodori アカウントは不要です。ユーザーが設定したデータベース、
> ローカルファイル、任意の AI/model provider にだけ接続します。
>
> 現在は development preview です。破壊的な SQL を実行する前に、対象接続、
> バックアップ、実行内容を必ず確認してください。

Feature bullets:

- SQL editor with CodeMirror, formatting, snippets, command palette workflows,
  and Vim mode.
- Schema navigation, metadata inspection, completion, ERD, and query plan views.
- Result grid designed for large result sets with copy/export and row details.
- Connection workflows for local and remote database engines.
- Local-first desktop app with open-source release artifacts.
- Extension-oriented architecture for future connector packages.

Keywords:

`SQL`, `database`, `PostgreSQL`, `MySQL`, `SQLite`, `DuckDB`, `Tauri`, `Rust`,
`developer tools`, `query editor`, `data browser`, `database client`, `Vim`.

## Required public pages

These pages are published from this mdBook by GitHub Pages:

- <https://hjosugi.github.io/irodori-docs/support.html>
- <https://hjosugi.github.io/irodori-docs/privacy.html>
- <https://hjosugi.github.io/irodori-docs/disclaimer.html>

The corresponding editable Markdown sources are:

- [support.md](support.md)
- [privacy.md](privacy.md)
- [disclaimer.md](disclaimer.md)

## Asset inventory

Current app/repository assets:

- `apps/desktop/src-tauri/icons/icon.png`
- `apps/desktop/src-tauri/icons/icon.icns`
- `apps/desktop/src-tauri/icons/icon.ico`
- `apps/desktop/src-tauri/icons/StoreLogo.png`
- `apps/desktop/src-tauri/icons/Square*.png`
- `src/irodori-icon.svg`

Still needed before store submission:

- screenshots for macOS, Windows, Linux;
- at least one 16:9 product screenshot showing the workbench;
- optional short demo GIF/video for stores that support rich media;
- signed/notarized release artifacts where the channel requires them;
- signed Windows and signed/notarized macOS `v0.7.x` artifacts;
- updater `latest.json` from a successful stable workflow dispatch;
- committed package-manager, desktop-entry, and appstream manifest templates if
  those channels become active.

## Channel checklist

### GitHub Releases

Status: lightweight Linux AppImage lane is live. The stable Windows/macOS/updater
lane is wired in `.github/workflows/release.yml` but blocked on platform signing
and notarization secrets.

Before publishing a release:

- run the release dry run;
- verify generated bindings and frontend build;
- verify release artifacts on each platform;
- fill release notes with known limitations and checksums;
- publish the draft release only after artifact names and signatures are stable.

### Tauri updater

Status: stable workflow lane is wired; publication is blocked until all stable
release signing gates pass.

Needed:

- configure the remaining Windows and macOS signing/notarization secrets;
- dispatch the `stable` workflow for an existing `v*` tag;
- verify updater `latest.json` and signatures before marking the release stable;
- document rollback when an updater artifact is bad.

### Homebrew cask

Status: planned; no template is committed yet.

Create a cask after the macOS release asset and sha256 are available. Submit to
the appropriate tap or to the project-owned tap first.

### Scoop

Status: planned; no template is committed yet.

Create a manifest after the Windows portable zip or installer strategy is
stable. A portable zip is usually cleaner for Scoop than an interactive
installer.

### winget

Status: planned; no template is committed yet.

Create manifests after the Windows installer URL, sha256, publisher name,
installer type, and installer switches are final.

### Chocolatey

Status: planned; no template is committed yet.

Create a package if Chocolatey is a target channel. Keep the install script
non-interactive and checksum-pinned.

### AUR

Status: planned; no template is committed yet.

Create a `PKGBUILD` for `irodori-table-bin` once the Linux AppImage artifact
name and checksum are stable.

### Flatpak / Flathub

Status: design work needed.

Flatpak needs a sandboxed runtime plan, file/network permissions, appstream
metadata, icon assets, and a stable build source. Treat this as a separate
packaging project.

### Snap

Status: design work needed.

Snap needs confinement choices, interface declarations, metadata, and store
review. Treat this as separate from the existing AppImage path.

### crates.io

Status: later.

The current git install path is:

```bash
cargo install --git https://github.com/hjosugi/irodori-kit --tag v0.5.0 --locked irodori-server
```

crates.io publication requires all `irodori-*` git/path dependencies to be
published or removed from the publishable crate graph.

## Private doc boundary

Keep this public:

- product description, screenshots, homepage/support/privacy URLs;
- package IDs, release URLs, checksums, and manifest plans;
- public troubleshooting and security-disclosure process.

Keep private:

- Apple Developer, Microsoft Partner Center, Snapcraft, Flathub, Chocolatey, and
  package registry account IDs;
- legal entity details, addresses, phone numbers, tax forms, and banking data;
- signing certificates, private keys, app-specific passwords, notarization
  credentials, API tokens, and recovery codes;
- review conversation history that includes account-specific data;
- release-blocking legal decisions that have not been approved for publication.

## Official references

Re-check these before submitting because store and package-manager requirements
change:

- Tauri distribution: <https://v2.tauri.app/distribute/>
- Tauri updater: <https://v2.tauri.app/plugin/updater/>
- Homebrew Cask Cookbook: <https://docs.brew.sh/Cask-Cookbook>
- Windows Package Manager manifests: <https://learn.microsoft.com/en-us/windows/package-manager/package/manifest>
- Scoop app manifests: <https://github.com/ScoopInstaller/Scoop/wiki/App-Manifests>
- Chocolatey package creation: <https://docs.chocolatey.org/en-us/create/create-packages/>
- Arch package guidelines: <https://wiki.archlinux.org/title/Arch_package_guidelines>
- Flathub submission: <https://docs.flathub.org/docs/for-app-authors/submission>
- Snapcraft release docs: <https://snapcraft.io/docs/releasing-your-app>
- App Store Connect app information: <https://developer.apple.com/help/app-store-connect/manage-app-information/set-app-information/>
- Microsoft Store developer account setup: <https://learn.microsoft.com/en-us/windows/apps/publish/partner-center/open-a-developer-account>
