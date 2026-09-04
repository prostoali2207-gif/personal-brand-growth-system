# Fahm Arabic evidence packet

- project_id: `fahm-arabic`
- project_name: `Fahm Arabic`
- repository_or_system_refs:
  - https://github.com/prostoali2207-gif/fahm-arabic
  - https://github.com/prostoali2207-gif/fahm-arabic/blob/main/README.md
- user_role: GitHub repository owner/maintainer account; author of cited PRs.
- time_scope: July 2026 evidence reviewed.
- problem_or_goal: The README defines a mobile-first Arabic learning application with Supabase-backed persistence, versioned exercises, structured evaluation, review scheduling and competency/mastery evidence.

## Artifacts

- PR #37 — Define versioned response and task contracts:
  https://github.com/prostoali2207-gif/fahm-arabic/pull/37
- PR #39 — Stage 2: handle revision conflicts and archived exercises:
  https://github.com/prostoali2207-gif/fahm-arabic/pull/39
- PR #40 — Stage 2: connect client revision-aware submissions:
  https://github.com/prostoali2207-gif/fahm-arabic/pull/40
- PR #41 — Stage 3: establish trusted next-action priority:
  https://github.com/prostoali2207-gif/fahm-arabic/pull/41
- PR #45 — Stage 3: verify next-action browser effects:
  https://github.com/prostoali2207-gif/fahm-arabic/pull/45

## Observable work

- README records Supabase authentication, versioned exercises, structured answer evaluation, uncertain-evaluation handling, idempotent attempt submission, server-backed checkpoints/resume, review scheduling and competency graph/mastery evidence.
- PR #37 defines versioned response/task contracts and deterministic contract tests.
- PRs #39-#40 add revision-aware server/client submission behavior and explicit revision-conflict handling.
- PRs #41-#45 build a trusted next-action router and verify refresh/back/offline/reconnect behavior through browser tests while asserting protected Supabase side effects.

## Observable outcomes

- The cited PRs are merged and provide traceable evidence of stateful product engineering, persistence boundaries and browser-effect testing.
- The evidence is about product/system behavior; it does not establish learner outcomes or commercial adoption.

## Limitations / unknowns

- No verified learner count, retention, learning-effectiveness metric or revenue was found.
- This project is supporting product-engineering evidence, not proof of AI consulting or commercial automation outcomes.

## Claim candidates

- Has built stateful Supabase-backed product workflows with idempotency, versioned contracts, offline/reconnect handling and browser-level tests.

- last_verified_at: `2026-09-04`
