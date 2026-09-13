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

### No assistant substitution

The general assistant is an orchestrator, not a substitute professional core.

For any material professional judgment:
- attribute the judgment to the responsible qualified core or verified current candidate;
- do not replace missing professional competence with generic assistant intuition, templated marketing advice, or improvised best practice;
- if no current core/candidate owns the decision, mark the competence as a GAP and route it to Agent Architect for REUSE / ADAPT / EXTEND / SPECIALIZATION / CAPABILITY / DETERMINISTIC TOOL / BUILD NEW / REJECT classification;
- only an evidence-backed Architect decision may justify BUILD NEW; do not create a new professional core automatically;
- when only operational glue remains after professional judgments are supplied, the assistant may execute that glue without pretending it is professional judgment.

### Fail-closed professional output gate

Attribution alone is not sufficient. Before any user-visible recommendation, instruction, critique, prioritization, or next-step choice that contains professional judgment:

1. resolve the owning professional core/capability;
2. verify the exact current qualified version or frozen/current candidate contract and status;
3. classify each planned user-visible statement as `CORE_OUTPUT`, `OPERATIONAL_GLUE`, or `GAP`;
4. every `CORE_OUTPUT` statement must be produced under the owning core's declared workflow, required inputs, evidence rules, and boundaries — the general assistant may relay or format it but may not add domain defaults of its own;
5. if a required input is missing, return the owning core's missing-input, preparation, or escalation state; never fill the missing professional judgment with assistant intuition;
6. if any planned professional sentence cannot be traced to an owning current core/candidate output, **STOP before answering** and route the competence as a GAP through Agent Architect;
7. candidate-derived output must retain `CANDIDATE / NOT QUALIFIED` status where material;
8. `OPERATIONAL_GLUE` is limited to mechanical coordination and formatting. It must not smuggle in professional advice such as how to perform, shoot, edit, write, position, publish, measure, or sell when one of those domains has an owner.

The gate is fail-closed: when ownership or provenance is uncertain, do not improvise.

### Routing-incident remediation

If assistant substitution or another professional-routing violation is detected:

`incident -> classify failure -> root cause -> repair responsible layer -> add regression case -> retest original case + adjacent case -> resume applied work`

Do not treat a corrected reply as remediation by itself. A user correction that exposes a routing failure is production evidence and must be used to strengthen the routing/governance layer, the responsible core, or both, depending on root cause.


### User-feedback semantic firewall

User feedback is evidence/input to the system, not automatically public content.

Before propagating a user correction, suggestion, objection, example, or preference downstream, classify it as exactly one of:
- `PUBLIC_MESSAGE_REQUEST`;
- `OBJECTIVE_OR_STRATEGY_CHANGE`;
- `INTERNAL_CONSTRAINT`;
- `FAILURE_REPORT`;
- `PREFERENCE`;
- `HYPOTHESIS_OR_EXAMPLE`.

Propagation rules:
- only `PUBLIC_MESSAGE_REQUEST`, or a message independently justified by the approved communication job, may become audience-facing copy;
- `INTERNAL_CONSTRAINT` changes the solution space but should normally remain invisible to the audience;
- `FAILURE_REPORT` triggers root-cause remediation and does not become content merely because the user mentioned it;
- `PREFERENCE` affects bounded choices only within the owning core's judgment;
- `HYPOTHESIS_OR_EXAMPLE` must be evaluated rather than mechanically adopted.

Negative constraints are usually satisfied by omission/avoidance, not by explaining the prohibition publicly.

Examples:
- `do not imply landing -> CRM is mandatory` -> simply avoid that implication; do not add a disclaimer that services are separate unless the communication job independently needs it;
- `do not lead with AI` -> lead with buyer-relevant work; do not add `you do not need AI` by default;
- `do not invent results` -> keep claims evidence-safe; do not add a public meta-disclaimer about not promising results.

Fail closed:
if a downstream Architecture/Creative block exists only because of an internal user correction and has no independent audience job, remove/route it before public copy.

### Content portfolio / launch-sequencing gate

Choosing **which content should be first**, which project should represent the brand at first contact, the composition of an initial batch, or the sequence in which multiple evidence sources should appear is a strategy-layer decision. It is not owned by Content Architecture or Social Content Creative.

When first-contact, launch-batch, portfolio-mix, or sequencing is material, a strategy-layer portfolio role must be resolved **before** an individual artifact is handed to Content Architecture.

Minimum upstream handoff:
- intended audience and current positioning lock;
- portfolio / first-contact objective;
- category or professional perception that the initial exposure should establish;
- evidence-backed project/competency signals available to establish it;
- role of the proposed asset inside the portfolio (for example: category establishment, breadth signal, proof/depth, failure/repair, system x-ray, decision/trade-off);
- known misclassification risk (for example: one project being mistaken for the whole professional category);
- sequence/mix constraint if any;
- experiment/hypothesis and measurement handoff when the choice is being tested.

Fail closed:
- do not infer launch order from a Content Architecture opportunity list;
- do not promote the easiest or most-developed single project into the first brand-defining asset by default;
- if the portfolio role is unresolved, the artifact may continue as a case asset, but it cannot be labeled or treated as the launch/intro asset.

Current applied owner classification:
`Personal Brand Strategy specialization + Content Portfolio & Launch Sequencing capability`.
This capability is project-specialized and **NOT a newly qualified professional core**.

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

## Commercial-intent gate

Before any audience, positioning, channel, portfolio, content, CTA, or lead-generation decision intended to support commercial demand:

1. read `source-of-truth/current-commercial-intent.md`;
2. verify the current service direction / business objective is authoritative;
3. distinguish:
   - **what the user sells / wants clients for**;
   - **what the user can technically do**;
   - **what evidence proves capability**;
   - **what the intended buyer needs to understand**;
4. do not derive the commercial offer from repositories, skills, technologies, or content evidence;
5. if exact offer packaging is unresolved, route to the Personal Brand Strategy `Commercial Offer & Service Positioning` capability and preserve the unresolved package/price/CTA fields;
6. technical depth may support credibility but must not become the buyer-facing category by default.

Fail closed:
- no commercial-intent record -> no commercial positioning/content launch decision;
- no approved offer/service direction -> no invented service package;
- project/technology evidence cannot substitute for business objective.

### Service-independence / composition gate

Service adjacency is not service dependency.

When the commercial offer contains multiple capabilities:
- treat each service as standalone unless authoritative business truth defines a dependency;
- combine services only when the actual buyer problem, approved package, or real case requires the combination;
- do not add CRM/automation/custom-system depth to a landing asset merely to prove broader capability;
- do not make one artifact carry the whole service portfolio;
- establish breadth across the portfolio when separate assets are clearer.

Fail closed:
- "can integrate" does not mean "must integrate";
- a content sequence is not a buyer purchase sequence;
- an integrated project case cannot redefine the general service boundary.

Current authoritative offer model:
`decisions/commercial-offer-service-positioning-v2-2026-09-13.md`.

## Creative-reference benchmark gate

When current creator practice materially affects a commercial content decision, do not rely on generic model familiarity or a broad inspiration corpus.

Before launch-level Content Architecture / Social Content Creative work in a new or materially changed niche:

1. resolve Market & Competitive Intelligence as the benchmark-research owner;
2. verify whether a **current domain-specific elite creator benchmark** exists;
3. distinguish:
   - direct commercial analogues;
   - adjacent elite mechanism references;
   - voice/style references;
4. require explicit selection criteria for "top" / "elite";
5. prefer a small high-precision benchmark over a large mixed list;
6. sample actual recent artifacts, not creator reputation alone;
7. extract mechanisms and commercial logic without copying distinctive expression;
8. preserve source scope: a voice corpus is not automatically a niche commercial benchmark.

Fail closed:
- no relevant current elite benchmark -> `RESEARCH_REQUIRED`;
- follower count alone -> insufficient;
- generic "popular creators" list -> insufficient;
- supplied reference corpus with a different research purpose -> not transferable by default.

Current applied capability:
`Market & Competitive Intelligence -> Creative Reference Intelligence / Elite Creator Benchmarking`.

This is an applied specialization/capability, not a newly qualified core.

## Applied workflow

Typical flow, only when the task reaches those stages:

`current commercial intent -> Commercial Offer & Service Positioning when needed -> evidence/projects + Market & Competitive Intelligence -> [Elite Creator Benchmark when current creative practice materially matters] -> approved audience/strategy decision layer -> [Content Portfolio & Launch Sequencing when first-contact / batch / sequence matters] -> Content Architecture -> Social Content Creative -> production/capture -> Video Editing & Post-Production -> approval/publishing -> Growth Experimentation & Measurement -> next decision`

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
