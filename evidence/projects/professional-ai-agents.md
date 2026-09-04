# professional-ai-agents evidence packet

- project_id: `professional-ai-agents`
- project_name: `professional-ai-agents`
- repository_or_system_refs:
  - https://github.com/prostoali2207-gif/professional-ai-agents
  - https://github.com/prostoali2207-gif/professional-ai-agents/blob/main/README.md
- user_role: GitHub repository owner/maintainer account; author of the cited issues/PRs/commits.
- time_scope: August-September 2026 evidence reviewed.
- problem_or_goal: The repository describes a system for engineering, researching, testing and strengthening specialized professional AI agents. Its stated model is profession -> competencies -> knowledge -> judgment -> workflows/tools -> evidence -> evaluation -> failure-driven improvement -> SKILL.

## Artifacts

- PR #252 — Record Content Architecture v0.4 qualification PASS:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/252
- Issue #265 — Create Qualification Reliability Engineer professional core:
  https://github.com/prostoali2207-gif/professional-ai-agents/issues/265
- PR #267 — Build Qualification Reliability Engineer v0.1 candidate:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/267
- PR #268 — Freeze Qualification Reliability Engineer v0.1 candidate:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/268
- PR #270 — Run QRE v0.1 Stage A zero-provider qualification:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/270
- PR #274 — Preregister QRE v0.1 Stage B calibration:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/274
- Issue #269 — QRE independent practical qualification:
  https://github.com/prostoali2207-gif/professional-ai-agents/issues/269
- PR #250 — Enforce qualification stop-loss across Agent Architect:
  https://github.com/prostoali2207-gif/professional-ai-agents/pull/250

## Observable work

- The repository separates profession modeling, evidence, evaluation, candidate freeze and qualification status.
- PR #267 implements a hybrid QRE candidate: a professional judgment layer plus a deterministic readiness guard; the PR records a 19-competency model, machine-readable readiness schema, deterministic guard and zero-provider regressions.
- PR #268 explicitly freezes that candidate while retaining the status `FROZEN_NOT_QUALIFIED`.
- PR #270 adds Stage A deterministic evaluator/harness evidence with zero provider/model calls.
- PR #274 preregisters Stage B calibration before candidate scoring.
- PR #250 operationalizes a qualification stop-loss that distinguishes technical execution-chain failure from professional candidate failure.
- PR #252 records a completed qualification PASS for Content Architecture v0.4.

## Observable outcomes

- The repository contains explicitly qualified professional-core evidence and multiple candidates/evaluation tracks with state kept distinct.
- The QRE track demonstrates deterministic preflight, candidate freezing, calibration preregistration and explicit not-qualified state rather than treating a completed prompt/skill as qualified.
- Qualification failures such as `NOT_EXECUTABLE` are preserved as infrastructure/evaluation outcomes rather than converted into unsupported professional PASS/FAIL claims.

## Limitations / unknowns

- Not every core/candidate in the repository is qualified.
- A candidate, preregistration or development PASS must not be described as a qualified reusable core unless its exact qualification record says so.
- Repository qualification results are engineering/evaluation evidence, not proof of commercial business impact.

## Claim candidates

- Builds specialized AI-agent systems using profession modeling, evidence, deterministic controls and explicit qualification/evaluation rather than treating agents as prompts alone.
- Works on AI evaluation/qualification infrastructure with fail-closed status, calibration and stop-loss mechanisms.

- last_verified_at: `2026-09-04`
