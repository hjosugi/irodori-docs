# Windows Development

This guide covers local desktop development on Windows. The Tauri desktop shell
should run on the Windows host because it depends on the Windows WebView2 and
MSVC toolchain. WSL is useful for some Rust-only work, but it is not the primary
path for desktop UI development.

## Prerequisites

- Windows 10 or Windows 11 on x64.
- Git.
- Node.js 24.x, matching the repository `.nvmrc`.
- Rust from `rustup`; the repository pins Rust 1.96.0 in `rust-toolchain.toml`.
- Visual Studio 2022 Build Tools with the **Desktop development with C++**
  workload, including MSVC and a Windows SDK.
- Microsoft Edge WebView2 Runtime. It is already present on most current Windows
  installs; install the Evergreen Runtime if Tauri reports that WebView2 is
  missing.
- Optional: Docker Desktop or Podman Desktop for sample database containers.

## Setup

Use PowerShell or Git Bash from the `irodori-table` repository root:

```powershell
rustup toolchain install
npm --prefix apps/desktop ci
node tools/dev/doctor.mjs
```

If GNU Make is available, the repository shortcuts are also supported:

```powershell
make setup
make doctor
```

## Run the desktop app

Start the Tauri development shell:

```powershell
npm --prefix apps/desktop run tauri -- dev
```

Or, when `make` is available:

```powershell
make desktop-dev
```

The development command starts Vite on `http://localhost:1420` and launches the
desktop shell. Launching a debug binary directly without Vite running will show a
blank window or a connection-refused message.

## Common checks

```powershell
npm --prefix apps/desktop run format:check
npm --prefix apps/desktop run lint
npm --prefix apps/desktop run test
npm --prefix apps/desktop run build:verified
```

Use `cargo test --workspace` for Rust backend changes.

## Sample databases

Sample database containers live in the sibling `irodori-samples` repository.
Clone it next to `irodori-table` when you need local integration fixtures:

```powershell
git clone https://github.com/hjosugi/irodori-samples ../irodori-samples
```

Then use Docker Desktop or Podman Desktop as the container engine.
