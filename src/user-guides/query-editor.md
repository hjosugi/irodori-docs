# Query Editor And Vim

The editor is the primary workspace surface. It supports multiple tabs, saved
sessions, connection-bound editors, snippets, formatting hooks, and command
palette actions.

## Running SQL

- Run the current statement for quick iteration.
- Select text and run the selection for focused checks.
- Run the whole file when reviewing a complete script.
- Cancel long-running statements from the running-query control.

## Completion

Completion uses local metadata first: schemas, tables, columns, aliases, CTEs,
functions, snippets, and dialect keywords. AI assistance is optional and must be
configured separately.

## Vim Mode

Vim mode is meant for daily-driver editing: normal/insert/visual modes, counts,
registers, marks, macros, search, and command-line style workflows. Keybindings
can be remapped from settings, and conflicts should be resolved before relying on
a custom map.
