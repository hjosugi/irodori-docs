# Distribution & updates

How users get Irodori Table and how it updates. Current public release:
**0.6.0** (`v0.6.0`, published 2026-07-02).

## Already in place

`.github/workflows/release.yml` — on a `v*` tag push, `tauri-action` builds
installers for **macOS**, **Windows** (`.msi`/NSIS), and **Linux**
(`.deb`/`.rpm`/`.AppImage`) on the matrix runners and creates a GitHub Release.
The download channel is live today; publish a release tag such as `v0.6.0`.

## Channel matrix

| Channel | For | Status | Notes |
| --- | --- | --- | --- |
| GitHub Releases (installers) | end users | ✅ exists | `release.yml`; cut by tagging the current release, e.g. `v0.6.0` |
| Tauri in-app updater | end users (auto-update) | ⬜ next | the fastest *update* path for the GUI; needs a signing key |
| Terminal installer download | end users | ✅ exists | use `gh release download` and install the `.deb`, `.rpm`, `.AppImage`, `.dmg`, or `.msi` |
| `cargo install --git` | Rust devs (headless server) | ✅ exists | installs `irodori-server` from `irodori-kit`, not the desktop app |
| crates.io | Rust devs | ⬜ later | crates.io forbids git/path deps; all `irodori-*` must be published first |
| Homebrew cask / Scoop / winget | mac/Windows | ⬜ later | manifests auto-bumped from releases |
| AUR / Flatpak | Linux | ⬜ later | from releases |

Public registration text, support/privacy/disclaimer URLs, and package manager
channel notes are collected in [store-registration.md](store-registration.md).
Package-manager manifests are still a future packaging task; do not link to
template paths until those files exist in `irodori-table`.

## Quick terminal install

Use GitHub CLI to fetch the newest matching release asset without opening a
browser. When no release tag is passed, `gh release download` uses the latest
release:

```bash
tmp="$(mktemp -d)"
gh release download --repo hjosugi/irodori-table --pattern "*.deb" --dir "$tmp"
sudo apt install "$tmp"/*.deb
```

Replace the pattern and install command as needed:

| Platform | Pattern | Install command |
| --- | --- | --- |
| Debian/Ubuntu | `*.deb` | `sudo apt install "$tmp"/*.deb` |
| Fedora/RHEL | `*.rpm` | `sudo dnf install "$tmp"/*.rpm` |
| Linux portable | `*.AppImage` | `chmod +x "$tmp"/*.AppImage && "$tmp"/*.AppImage` |
| macOS | `*.dmg` | `open "$tmp"/*.dmg` |
| Windows PowerShell | `*.msi` | launch the downloaded `.msi` |

The current `v0.6.0` assets are:

- `Irodori.Table_0.6.0_amd64.deb`
- `Irodori.Table-0.6.0-1.x86_64.rpm`
- `Irodori.Table_0.6.0_amd64.AppImage`
- `Irodori.Table_0.6.0_x64_en-US.msi`
- `Irodori.Table_0.6.0_x64-setup.exe`
- `Irodori.Table_0.6.0_aarch64.dmg`
- `Irodori.Table_aarch64.app.tar.gz`

## On "cargo is fastest"

`cargo install` only installs Rust binaries. It is not a desktop app installer:
the Tauri app bundles a webview, native packaging metadata, and a built frontend.
Use GitHub Release installers for the desktop app.

For the headless local HTTP API, install `irodori-server` from `irodori-kit`:

```bash
cargo install --git https://github.com/hjosugi/irodori-kit --tag v0.5.0 --locked irodori-server
```

The old `irodori-table` repo command is no longer correct because
`irodori-server` moved to `irodori-kit`.

## Recommended order

1. **Tag the current release** → installers ship immediately (channel already
   built; for the current docs, that means `v0.6.0`).
2. **Tauri updater** for in-app auto-update (the real "get updates" for the GUI):
   - `cd apps/desktop && npm run tauri signer generate` → keypair.
   - Add the private key as the `TAURI_SIGNING_PRIVATE_KEY` GitHub Actions secret.
   - In `tauri.conf.json`: set `bundle.createUpdaterArtifacts = true` and
     `plugins.updater` with the public key + an `endpoints` entry pointing at the
     releases `latest.json` (tauri-action emits it per release).
3. **Keep desktop terminal installs installer-based** — document
   `gh release download` paths for release assets; keep `cargo install` scoped
   to the `irodori-kit` headless server.
4. **Package managers** (brew/scoop/winget/AUR/Flatpak) once you want them — each
   is a small manifest auto-updated from the GitHub Release assets.
