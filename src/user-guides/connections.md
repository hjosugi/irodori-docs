# Connections

Connections bind editor tabs, browser metadata, result history, and diagnostics
to a database source.

## Daily Flow

1. Create or duplicate a profile from the connection manager.
2. Keep profiles organized in folders when working across projects.
3. Test the profile before opening an editor tab.
4. Bind a tab to the connection before running SQL.

## Transport And Secrets

Profiles can use direct sockets, SSH, SOCKS/HTTP proxies, and ordered proxy
chains where the engine supports them. Store reusable hops separately so several
profiles can share the same transport path.

Exported connection definitions exclude secrets. Re-enter credentials after
importing a profile on another machine.

## Troubleshooting

Use connection diagnostics first. They separate DNS/network/proxy failures from
database authentication and feature support errors. When a connector is not part
of the default build, install the marketplace connector or choose an engine that
is shipped in the current desktop binary.
