# Getting Started

This path gets a new user from install to a successful query without reading the
architecture notes.

## Install

Download the current desktop build from
<https://github.com/hjosugi/irodori-table/releases>. The Linux build is the most
actively exercised preview target.

For source builds, follow [Install guide](install-guide.md) first. It covers the
pinned Node/Rust toolchains and platform packages.

## Create A Connection

1. Open the connection manager.
2. Choose a database engine.
3. Enter host, port, database, user, and authentication details.
4. Use the diagnostic or test action before saving.

Secrets are stored through the local OS credential store where supported. Export
connection definitions without secrets when sharing project setup.

## Run The First Query

1. Open a SQL editor tab bound to the saved connection.
2. Type a query such as `select 1;`.
3. Run the current statement or selected text.
4. Cancel from the running-query control if the statement takes too long.

The editor is local-first. SQL is inserted, formatted, or generated in the
editor first; it is not sent to a database until you run it.

## Read Results

Results appear in the result grid. Use copy/export for a selected range or the
current page, switch result modes when available, and keep large exports bounded
by using the export flow instead of copying an entire result set.

Next reads:

- [Connections](user-guides/connections.md)
- [Query editor and Vim](user-guides/query-editor.md)
- [Results grid and export](user-guides/results-export.md)
