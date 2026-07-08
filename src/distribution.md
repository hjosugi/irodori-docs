# Distribution & Updates

How users get Irodori Table and how it updates.

- Current stable GitHub Release: **0.7.32** (`v0.7.32`, published
  2026-07-05).
- Current lightweight prerelease: **0.7.34** (`v0.7.34`, published
  2026-07-08).

## Already in place

`.github/workflows/release.yml` — on a `v*` tag push, `tauri-action` builds
a lightweight **Linux AppImage** and creates a GitHub prerelease. The manual
`stable` workflow channel is defined for updater artifacts plus signed Windows
and signed/notarized macOS artifacts, but it requires the platform signing and
notarization secrets before it can publish.

## Channel matrix

| Channel | For | Status | Notes |
| --- | --- | --- | --- |
| GitHub Releases (Linux AppImage) | Linux users | ✅ exists | tag pushes publish the lightweight AppImage prerelease lane |
| Signed Windows/macOS releases | end users | ⬜ blocked | stable workflow is wired; platform signing/notarization secrets are still required |
| Tauri in-app updater | end users (auto-update) | ⬜ blocked | stable workflow can publish `latest.json` after updater and platform signing gates pass |
| Terminal package download | Linux users | ✅ exists | use `gh release download` and run the `.AppImage` |
| `cargo install --git` | Rust devs (headless server) | ✅ exists | installs `irodori-server` from the historical `irodori-kit v0.5.0` tag, not the desktop app |
| crates.io | Rust devs | ⬜ later | crates.io forbids git/path deps; all `irodori-*` must be published first |
| Homebrew cask / Scoop / winget | mac/Windows | ⬜ later | manifests auto-bumped from releases |
| AUR / Flatpak | Linux | ⬜ later | from releases |

Public registration text, support/privacy/disclaimer URLs, and package manager
channel notes are collected in [store-registration.md](store-registration.md).
Package-manager manifests are still a future packaging task; do not link to
template paths until those files exist in `irodori-table`.

## Quick terminal install

Use GitHub CLI to fetch the newest stable AppImage without opening a browser:

```bash
tmp="$(mktemp -d)"
gh release download --repo hjosugi/irodori-table --pattern "*.AppImage" --dir "$tmp"
chmod +x "$tmp"/*.AppImage
"$tmp"/*.AppImage
```

Use an explicit tag to test a lightweight prerelease:

```bash
tmp="$(mktemp -d)"
gh release download v0.7.34 --repo hjosugi/irodori-table --pattern "*.AppImage" --dir "$tmp"
chmod +x "$tmp"/*.AppImage
"$tmp"/*.AppImage
```

The current checked assets are:

- `v0.7.32`: `Irodori.Table_0.7.32_amd64.AppImage`
- `v0.7.34`: `Irodori.Table_0.7.34_amd64.AppImage`

Current `v0.7.x` releases do not publish `.deb`, `.rpm`, `.dmg`, `.msi`, setup
`.exe`, updater, or macOS app archive assets.

## On "cargo is fastest"

`cargo install` only installs Rust binaries. It is not a desktop app installer:
the Tauri app bundles a webview, native packaging metadata, and a built frontend.
Use GitHub Release installers for the desktop app.

For the headless local HTTP API, install `irodori-server` from the last
`irodori-kit` tag that shipped it as a workspace package:

```bash
cargo install --git https://github.com/hjosugi/irodori-kit --tag v0.5.0 --locked irodori-server
```

The old `irodori-table` repo command is no longer correct because
`irodori-server` moved to `irodori-kit`.

## Recommended order

1. **Keep lightweight tags moving** so Linux AppImage prereleases continue to
   publish from main.
2. **Finish stable signing gates** by adding the Windows signing and macOS
   signing/notarization secrets required by `release.yml`.
3. **Dispatch the `stable` workflow** for an existing `v*` tag after the secrets
   are present; verify updater `latest.json`, signatures, and platform assets
   before marking the release stable.
4. **Keep desktop terminal installs package-based** with `gh release download`;
   keep `cargo install` scoped to the historical `irodori-kit` headless server.
5. **Package managers** (brew/scoop/winget/AUR/Flatpak) once the stable assets
   and checksums are durable enough for manifests.
