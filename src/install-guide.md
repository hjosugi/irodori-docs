# Install Guide

Irodori Table publishes desktop packages from GitHub Releases. The release
state checked for this guide is:

- latest stable GitHub Release: `v0.7.32`, published on 2026-07-05;
- latest lightweight prerelease: `v0.7.34`, published on 2026-07-08.

<https://github.com/hjosugi/irodori-table/releases>

The current `v0.7.x` release lane publishes a Linux AppImage only. Windows,
macOS, updater, `.deb`, and `.rpm` artifacts are intentionally omitted until the
signed stable release lane is restored. `cargo install` does not install the
desktop application. It is only for the separate headless `irodori-server`
binary from the older `irodori-kit v0.5.0` tag.

This guide is for packaged desktop installs. Source build prerequisites and
WebView troubleshooting live in the platform development guides:
[Windows](windows-development.md), [macOS](macos-development.md), and
[Linux](linux-development.md).

## Quick terminal install

The shortest terminal path uses GitHub CLI. Install `gh` first if your shell
does not already have it. When no release tag is passed, `gh release download`
downloads assets from the latest release.

### Linux: portable AppImage

```bash
mkdir -p "$HOME/Applications"
gh release download --repo hjosugi/irodori-table --pattern "*.AppImage" --dir "$HOME/Applications"
chmod +x "$HOME/Applications"/Irodori*.AppImage
"$HOME/Applications"/Irodori*.AppImage
```

To test the newest lightweight prerelease instead of the latest stable release,
pass the tag explicitly:

```bash
gh release download v0.7.34 --repo hjosugi/irodori-table --pattern "*.AppImage" --dir "$HOME/Applications"
```

## Downloads by OS

| OS | Recommended asset | Notes |
| --- | --- | --- |
| Linux | `.AppImage` | Current `v0.7.x` releases publish `Irodori.Table_<version>_amd64.AppImage`. |
| Windows | Source build | Current `v0.7.x` releases do not publish `.msi` or setup `.exe` assets. |
| macOS | Source build | Current `v0.7.x` releases do not publish `.dmg` assets. |

## Windows

Current `v0.7.x` releases do not publish Windows installers. Build from source
with the [Windows development guide](windows-development.md) until the signed
stable release lane is restored.

## macOS

Current `v0.7.x` releases do not publish macOS disk images. Build from source
with the [macOS development guide](macos-development.md) until the signed and
notarized stable release lane is restored.

## Linux

Download the AppImage, make it executable, and run it:

```bash
chmod +x ./Irodori*.AppImage
./Irodori*.AppImage
```

Some distributions ship FUSE 3 by default while AppImage still expects FUSE 2.
If the AppImage does not launch, either install the distribution's FUSE 2
package or run it in extract-and-run mode:

```bash
APPIMAGE_EXTRACT_AND_RUN=1 ./Irodori*.AppImage
```

For release channel details and future package-manager plans, see
[Distribution and updates](distribution.md).

## Headless server

Rust users who need the local HTTP API, not the desktop app, can install the
headless server from the last `irodori-kit` tag that shipped it as a workspace
package:

```bash
cargo install --git https://github.com/hjosugi/irodori-kit --tag v0.5.0 --locked irodori-server
```

See [Headless local data API](headless-data-api.md) for runtime configuration.
