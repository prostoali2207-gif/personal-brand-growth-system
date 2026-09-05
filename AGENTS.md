# Applied repository operating rules

## Purpose

This repository is the operational source of truth for the personal-brand system. It is not a professional-core factory and must not duplicate profession models, qualification infrastructure, or reusable professional knowledge from `prostoali2207-gif/professional-ai-agents`.

Current scope is infrastructure only. Do not infer or invent positioning, audience strategy, content strategy, commercial claims, experience, clients, results, metrics, technologies used, or achievements.

## Professional-core routing

Before a material professional decision:

1. identify the profession/capability that owns the decision;
2. inspect the current `professional-ai-agents` Professional Core Library and exact artifact/version;
3. use a qualified core only inside its declared responsibility, runtime, authority, evidence, and handoff boundary;
4. a current candidate may be used in applied work only after its current/frozen candidate contract and status are verified in `professional-ai-agents`;
5. never label a candidate as qualified or library-admitted;
6. if no existing core/candidate covers the competence, record a GAP and route the classification question to Agent Architect; do not create a new core automatically.

Qualified status is version-specific and does not transfer project context automatically. Re-check the upstream registry/status when the decision is material or when a stored reference may be stale.

See `professional-cores/registry.md`.

## Evidence and truth

The brand must describe real work.

Material statements must be classified as one of:

- `FACT/EVIDENCE` — directly supported by a traceable source;
- `CORE JUDGMENT` — professional interpretation/recommendation from the named core;
- `HYPOTHESIS` — testable but not established;
- `USER DECISION` — an explicit approved choice, not evidence that the choice is true.

A claim may become public only when its evidence and scope are recorded in `brand-claims/` and its status permits public use.

Preferred project evidence includes repository files, commits, pull requests, issues, deployments, product artifacts, screenshots/recordings, system logs, connected analytics, and other directly observable results. Do not turn chat recollection into a verified claim when primary evidence is available.

## Repository authority order

For project-specific facts, prefer the most direct current evidence in this order when applicable:

1. observable source artifact or connected system state;
2. `source-of-truth/` record with current provenance;
3. project evidence packet in `evidence/projects/`;
4. approved claim record in `brand-claims/`;
5. decision/hypothesis records;
6. chat/history only as a lead requiring verification.

Newer evidence does not automatically win if authority, scope, identity, or applicability are unclear. Record supersession explicitly.

## Current identity checkpoint

Before any task that depends on the current public identity — including naming, avatar/profile image direction, bio, profile design, channel setup, visual identity, or content packaging — first read:

- `source-of-truth/current-brand-identity.md`

Treat that file as the canonical current project identity state. Do not recover a current name/handle from old chat history or superseded naming decisions when this checkpoint exists.

If the file says a handle is selected but platform availability is still pending, preserve that exact distinction: the selected identity is current for downstream creative direction, while account activation/availability remains unverified.

## Applied workflow

Typical flow, only when the task reaches those stages:

`evidence/projects -> Market & Competitive Intelligence -> approved strategy/decision layer -> Content Architecture -> Social Content Creative -> production/capture -> Video Editing & Post-Production -> approval/publishing -> Growth Experimentation & Measurement -> next decision`

Commercial inbound may hand off to `Sales / Lead Conversion`. Paid promotion of approved content may hand off to `Paid Media / Performance Marketing`.

This workflow is routing guidance, not permission to invent missing strategy or to execute side effects.

## Side-effect authority

Reading, organizing, analyzing, drafting, and preparing reversible repository artifacts are allowed when requested.

Publishing, sending external messages as the user, changing paid-media spend, deleting production data, or making other consequential external changes require explicit delegation for that action unless an existing project instruction clearly grants it.

## Directory contracts

- `source-of-truth/` — durable project facts, scope and provenance rules.
- `evidence/projects/` — evidence packets for real projects/work.
- `brand-claims/` — claim ledger and public-use status.
- `channels/` — channel/account inventory and operational state.
- `decisions/` — decisions and hypotheses with evidence links and status.
- `content/briefs/` — approved/working briefs and preserved constraints.
- `content/published/` — records of actual published artifacts and URLs/IDs when verified.
- `experiments/` — experiment definitions, locks, status and decisions.
- `analytics/` — measured observations, snapshots and analysis records.
- `handoffs/` — traceable transfers between professional cores.
- `professional-cores/` — local routing registry only; never copy/modify upstream core behavior here.

## Handoff minimum

Every material handoff should record:

`from_core -> to_core -> task -> authoritative inputs -> verified facts/claims -> locked constraints -> unknowns -> authority boundary -> requested output -> evidence/provenance refs`

The receiving core must not silently rewrite upstream locked decisions. If required input is missing or conflicting, return the issue to the accountable owner/core.

## No silent strategy

Until explicitly authorized, do not create positioning, target audience, editorial pillars, funnel strategy, posting cadence, platform role, content calendar, CTA strategy, or growth targets merely to fill empty repository sections.
