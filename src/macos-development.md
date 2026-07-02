# macOS Development

This guide covers local desktop development on macOS. Tauri uses the system
WebKit/WKWebView stack on macOS, so no WebKitGTK packages are needed.

## Prerequisites

- macOS on Apple Silicon or Intel.
- Xcode Command Line Tools:

  ```bash
  xcode-select --install
  ```

- Node.js 24.x, matching the repository `.nvmrc`.
- Rust from `rustup`; the repository pins Rust 1.96.0 in `rust-toolchain.toml`.
- npm for reproducible dependency installs.
- Optional: Docker Desktop or Podman for sample database containers.

## Setup

From the `irodori-table` repository root:

```bash
rustup toolchain install
make setup
make doctor
```

The root is not an npm workspace. Prefer the root `Makefile` shortcuts, or run
desktop scripts with `npm --prefix apps/desktop ...`.

## Run the desktop app

```bash
make desktop-dev
```

`make desktop-dev` starts Vite on `http://localhost:1420` and launches the Tauri
desktop shell. If you start a debug binary directly without Vite running, the
window will be blank or show a connection-refused message.

## Common checks

```bash
make desktop-format-check
make desktop-lint
make desktop-test
make desktop-build-verified
```

Use `cargo test --workspace` for Rust backend changes.

## Sample databases

Sample database containers live in the sibling `irodori-samples` repository:

```bash
git clone https://github.com/hjosugi/irodori-samples ../irodori-samples
make db-up DB=postgres
make db-verify DB=postgres
```

Use the container engine that works best on your machine. The development doctor
detects Docker or Podman when either is available.
