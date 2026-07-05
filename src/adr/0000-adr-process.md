# 0000 - ADR Process

Status: accepted

## Context

Irodori docs include architecture decisions that explain durable product and
implementation choices. The series started at `0001`, but contributors need a
stable place that explains how new decisions are named, scoped, and updated.

## Decision

Use Architecture Decision Records under `src/adr/` for decisions that affect
public architecture, repo boundaries, extension contracts, release policy, or
long-lived developer workflow.

ADR files follow this naming convention:

```text
NNNN-short-title.md
```

Use four digits, keep titles lowercase with hyphens, and never renumber existing
ADRs. Each ADR should include:

- status: proposed, accepted, superseded, or rejected;
- context: the problem or constraint that forced a decision;
- decision: the chosen rule or direction;
- consequences: tradeoffs and follow-up work.

When a decision changes, add a new ADR and mark the old one as superseded with a
link to the replacement. Small clarifications can be edited in place when they do
not change the decision.

## Consequences

- Contributors have a documented process before adding `0002` and later ADRs.
- Historical decisions stay stable and linkable.
- Public docs can explain why the implementation is shaped a certain way without
mixing durable decisions into transient roadmap pages.
