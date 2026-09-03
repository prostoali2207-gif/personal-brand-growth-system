# Source of truth

Durable project-specific facts live here. This layer stores facts and provenance, not marketing interpretation.

## Record rule

For each material fact record:

- `id`
- `statement`
- `scope`
- `status`: `verified | provisional | superseded | disputed`
- `source_type`
- `source_ref`
- `verified_at`
- `verified_by`
- `supersedes` / `superseded_by` when applicable
- `notes` only when needed to explain scope or uncertainty

Do not store a fact as verified when the source only supports an inference.

## What belongs here

Examples: ownership of a repository/product, confirmed project role, verified product capability, confirmed public channel/account identity, approved operational constraints, and stable project facts required by multiple downstream workflows.

Volatile metrics belong in `analytics/`; evidence bundles belong in `evidence/projects/`; public-facing claims belong in `brand-claims/`.
