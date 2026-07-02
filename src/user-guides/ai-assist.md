# AI Assist

AI features are optional. Deterministic completion and editor workflows work
without a model or cloud provider.

## Provider Setup

Configured providers share one abstraction across SQL generation and chat. Local
providers can run on-device; cloud providers require user-supplied credentials
stored outside the repository.

## Read-Only Agent Mode

The schema-aware chat sidebar can inspect context and propose SQL. Read-only
agent mode is cancellable and should not execute writes without explicit user
action.

## Privacy Expectations

Only enable a cloud provider when the schema or prompt content is appropriate for
that provider. Keep privacy mode and redaction settings enabled when sharing
logs, screenshots, or reports.
