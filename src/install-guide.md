# Install Guide

Irodori Table ships desktop installers from GitHub Releases. The latest public
release checked for this guide is `v0.6.0`, published on 2026-07-02:

<https://github.com/hjosugi/irodori-table/releases>

Use the newest release for normal desktop installs. `cargo install` does not
install the desktop application. It is only for the separate headless
`irodori-server` binary in `irodori-kit`.

This guide is for packaged desktop installs. Source build prerequisites and
WebView troubleshooting live in the platform development guides:
[Windows](windows-development.md), [macOS](macos-development.md), and
[Linux](linux-development.md).

## Quick terminal install

The shortest terminal path uses GitHub CLI. Install `gh` first if your shell
does not already have it. When no release tag is passed, `gh release download`
downloads assets from the latest release.

### Linux: Debian or Ubuntu

```bash
tmp="$(mktemp -d)"
gh release download --repo hjosugi/irodori-table --pattern "*.deb" --dir "$tmp"
sudo apt install "$tmp"/*.deb
```

### Linux: Fedora, RHEL, or compatible

```bash
tmp="$(mktemp -d)"
gh release download --repo hjosugi/irodori-table --pattern "*.rpm" --dir "$tmp"
sudo dnf install "$tmp"/*.rpm
```

### Linux: portable AppImage

```bash
mkdir -p "$HOME/Applications"
gh release download --repo hjosugi/irodori-table --pattern "*.AppImage" --dir "$HOME/Applications"
chmod +x "$HOME/Applications"/Irodori*.AppImage
"$HOME/Applications"/Irodori*.AppImage
```

### macOS

```bash
mkdir -p "$HOME/Downloads/irodori-table"
gh release download --repo hjosugi/irodori-table --pattern "*.dmg" --dir "$HOME/Downloads/irodori-table"
open "$HOME/Downloads/irodori-table"/*.dmg
```

Move **Irodori Table** to Applications from the mounted disk image. The current
preview release includes an Apple Silicon `.dmg`; use a source build for Intel
macOS until an Intel `.dmg` is published.

### Windows PowerShell

```powershell
$dir = New-Item -ItemType Directory -Force "$env:TEMP\irodori-table"
gh release download --repo hjosugi/irodori-table --pattern "*.msi" --dir $dir.FullName
$msi = Get-ChildItem $dir.FullName -Filter "*.msi" | Select-Object -First 1
Start-Process $msi.FullName -Wait
```

## Downloads by OS

| OS | Recommended asset | Notes |
| --- | --- | --- |
| Windows | `.msi` or setup `.exe` | Download the Windows installer asset and run it from Explorer. |
| macOS | `.dmg` | Open the disk image, move Irodori Table to Applications, then launch it. Current preview assets are Apple Silicon only. |
| Linux | `.deb`, `.rpm`, or `.AppImage` | Use `.deb` on Debian/Ubuntu-style systems, `.rpm` on Fedora/RHEL-style systems, or AppImage for portable local runs. |

## Windows

1. Download the Windows installer from the release assets.
2. Run the installer.
3. Launch **Irodori Table** from the Start menu.

If Windows SmartScreen appears for a development-preview build, verify that the
installer came from the official GitHub release page before continuing.

## macOS

1. Download the `.dmg` from the release assets.
2. Open the disk image and move **Irodori Table** into Applications.
3. Launch it from Applications.

During the development-preview phase, macOS may require **Control-click > Open**
the first time you run a downloaded build.

The current preview release publishes an Apple Silicon `.dmg`. Intel macOS users
should build from source until an Intel `.dmg` appears in the release assets.

## Linux

For Debian or Ubuntu-style systems, download the `.deb` and install it with your
package manager:

```bash
sudo apt install ./path/to/downloaded-package.deb
```

For Fedora, RHEL, or compatible distributions, download the `.rpm` and install
it with your package manager:

```bash
sudo dnf install ./path/to/downloaded-package.rpm
```

For other desktop distributions, download the AppImage, make it executable, and
run it:

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
headless server from `irodori-kit`:

```bash
cargo install --git https://github.com/hjosugi/irodori-kit --tag v0.5.0 --locked irodori-server
```

See [Headless local data API](headless-data-api.md) for runtime configuration.
