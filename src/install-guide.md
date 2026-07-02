# Install Guide

Irodori Table ships desktop installers from GitHub Releases:

<https://github.com/hjosugi/irodori-table/releases>

Use the newest release for normal desktop installs. `cargo install` is only for
Rust binaries such as the headless `irodori-server`; it does not install the
desktop application.

## Downloads by OS

| OS | Recommended asset | Notes |
| --- | --- | --- |
| Windows | `.msi` or setup `.exe` | Download the Windows installer asset and run it from Explorer. |
| macOS | `.dmg` | Open the disk image, move Irodori Table to Applications, then launch it. |
| Linux | `.deb` or `.AppImage` | Use `.deb` on Debian/Ubuntu-style systems. Use AppImage for portable local runs. |

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

## Linux

For Debian or Ubuntu-style systems, download the `.deb` and install it with your
package manager:

```bash
sudo apt install ./path/to/downloaded-package.deb
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

## Headless server

Rust users can install the headless server directly from Git:

```bash
cargo install --git https://github.com/hjosugi/irodori-table irodori-server
```

For release channel details and future package-manager plans, see
[Distribution and updates](distribution.md).
