# Professional GAP classification — Personal Brand Growth System

decision_id: PBGS-PROF-GAP-001  
date: 2026-09-04  
decision_owner: User / Personal Brand Growth System  
owning_professional_core: Agent Architect v1.2 methodology  
status: active

## Question

Which professional competencies required for the Personal Brand Growth System are already covered by current qualified/released cores or candidates, which should be composed from existing capabilities, and which are genuine professional gaps?

No new professional core may be created from this decision record.

## Upstream baseline verified

Professional source of truth:
- `prostoali2207-gif/professional-ai-agents`
- verified branch: `main`
- verified commit: `e0ac746e294f3b076d9448adf01753b5eacee789`

Applied source of truth:
- `prostoali2207-gif/personal-brand-growth-system`
- `AGENTS.md`
- `professional-cores/registry.md`

Architect rules applied:
- inspect reusable cores before rebuilding a profession;
- matching titles are not compatibility evidence;
- prefer the least complex architecture that meets the task;
- historical qualification does not automatically transfer to a new composition/domain;
- candidates may be used in applied work but must remain labeled NOT QUALIFIED;
- do not create a new core without a demonstrated responsibility/judgment gap.

## Current reusable professional inventory

Qualified library entries at the verified upstream state:
- Paid Media / Performance Marketing 1.0.0
- Video Editing & Post-Production 0.1.0
- Growth Experimentation & Measurement 1.2.0
- Market & Competitive Intelligence 1.0.0
- Social Content Creative 0.1.0
- Sales / Lead Conversion 0.5.0

Qualified/released but not yet represented in the current library catalog:
- Content Architecture & Creative Structure v0.4

Relevant current candidates/research tracks:
- Growth Strategy & Experiment Portfolio v0.1 — frozen candidate / NOT QUALIFIED
- Automotive Commercial Capture Direction v0.1 — EXTEND track attached to Social Content Creative / NOT QUALIFIED
- Social Community, Listening & Reputation Management — research/design track with BUILD NEW disposition; no released core

## Final classification matrix

| Target competence | Primary classification | Existing composition / boundary | Applied decision | Upstream action |
|---|---|---|---|---|
| Personal Brand Strategy / Positioning | **SPECIALIZATION** | Market & Competitive Intelligence -> Growth Strategy & Experiment Portfolio candidate | Do not create a Personal Brand Strategy core. Treat personal-brand positioning as a domain specialization/delta of the strategy layer unless later evidence demonstrates a separate stable profession boundary. | **NO SEND** now. Revisit only if repeated applied evidence demonstrates an EXTEND or BUILD NEW requirement. |
| Own-channel audit / channel intelligence | **DETERMINISTIC TOOL + REUSE** | Deterministic account/access/integration inventory + Growth Experimentation & Measurement + Market Intelligence + Strategy candidate for interpretation/decision | Keep account discovery, ownership/access, connectors, publishing authority, analytics access and last-verification state as observable inventory. Use existing cores only for interpretation and downstream decisions. | **NO SEND**. This is not evidence for a new professional core. |
| Community / Social Listening / Reputation | **BUILD NEW** | Adjacent cores explicitly do not own community stewardship, moderation judgment, social-listening validity, reputation issue assessment or crisis governance | Genuine professional responsibility gap. Existing research already demonstrates a separate reusable core boundary. Do not implement or qualify from the applied repo. | **ELIGIBLE FOR UPSTREAM** because BUILD NEW is already evidence-backed in `professional-ai-agents`. No new upstream work is triggered by this record alone. |
| Professional capture / photography / cinematography | **CAPABILITY**; existing automotive precedent = **EXTEND** | Social Content Creative owns visual storytelling/light shoot direction but not deep principal-photography craft; Video Post-Production is downstream. Automotive Capture Direction already uses EXTEND rather than a new top-level agent. | For Personal Brand, do not create a Capture Agent. Route capture as a modular capability attached to the creative/production layer. The automotive candidate is precedent, not transferable qualification for personal-brand capture. | **NO NEW SEND yet for Personal Brand capture.** Only a demonstrated reusable EXTEND delta may be sent upstream. Existing automotive EXTEND already exists upstream. |
| Organic publishing / distribution execution | **DETERMINISTIC TOOL + REUSE**; standalone Publisher agent = **REJECT** | Strategy owns channel role/decision; Social Content Creative owns platform-native creative; human/authorized publisher owns release authority; tooling owns upload/schedule/publish/verify mechanics | Model publishing as an authorized deterministic workflow/integration with idempotency, permissions, verification and audit state. Do not create an Organic Publisher professional core without evidence of irreducible professional judgment beyond existing owners. | **NO SEND**. Tool/integration work belongs in the applied system. |
| Content architecture / creative structure | **REUSE** | Content Architecture & Creative Structure v0.4 released contract | Use exact released contract inside its boundary. Track upstream catalog inconsistency separately; it is not a competence GAP. | **NO SEND as GAP**. Registry maintenance is separate from profession design. |
| Social content creation | **REUSE** | Social Content Creative 0.1.0 qualified | Use for exact social copy/creative execution from approved brief and verified facts. Do not transfer strategy, publishing or community authority into it. | **NO SEND**. |
| Market / competitor / buyer / platform evidence | **REUSE** | Market & Competitive Intelligence 1.0.0 qualified | Use for current evidence and bounded implications; final positioning/strategy remains downstream. | **NO SEND**. |
| Measurement / growth learning | **REUSE** | Growth Experimentation & Measurement 1.2.0 qualified | Use for measurement integrity, experiment interpretation and bounded action evidence. | **NO SEND**. |
| Video editing / finishing / delivery QC | **REUSE** | Video Editing & Post-Production 0.1.0 qualified | Use downstream of approved/captured source media. Principal photography remains out of scope. | **NO SEND**. |
| Commercial inbound conversion | **REUSE** | Sales / Lead Conversion 0.5.0 qualified | Use only for qualified commercial inbound after appropriate handoff. Does not own community/channel stewardship. | **NO SEND**. |
| Paid amplification of proven content | **REUSE** | Paid Media / Performance Marketing 1.0.0 qualified | Use only when paid promotion is authorized and strategically justified. | **NO SEND**. |

## Evidence refs

Upstream architecture / library:
- `professional-ai-agents/AGENTS.md`
- `professional-ai-agents/architect/SKILL.md`
- `professional-ai-agents/architect/library/catalog.json`
- `professional-ai-agents/docs/qualification-results/content-architecture-v04-qualified-2026-09-02.md`

Strategy boundary:
- `professional-ai-agents/architect/research/growth-strategy-experiment-portfolio/candidate-professional-model-v0.1.md`
- `professional-ai-agents/architect/research/market-competitive-intelligence/profession-reconstruction-v0.1.md`
- `professional-ai-agents/architect/research/market-competitive-intelligence/competency-and-knowledge-model-v0.1.md`

Community / listening / reputation:
- `professional-ai-agents/architect/research/social-community-listening-reputation/competency-gap-register-v0.1.md`
- `professional-ai-agents/architect/research/social-community-listening-reputation/competency-matrix-v0.1.md`
- `professional-ai-agents/architect/research/social-community-listening-reputation/evaluation-plan-v0.1.md`

Capture:
- `professional-ai-agents#229`
- `professional-ai-agents#230`
- `professional-ai-agents/architect/research/automotive-capture-direction/profession-reconstruction-and-reuse-v0.1.md` (current PR track; candidate / NOT QUALIFIED)
- `professional-ai-agents#271`

Publishing boundary:
- `professional-ai-agents/architect/library/cores/social-content-creative/0.1.0/evidence-and-reuse.md`
- `professional-ai-agents/architect/research/social-community-listening-reputation/authority-matrix-v0.1.md`

Applied repository:
- `personal-brand-growth-system/AGENTS.md`
- `personal-brand-growth-system/professional-cores/registry.md`
- `personal-brand-growth-system/channels/inventory.md`

## Alternatives considered and rejected

### One universal Personal Brand / SMM agent
**REJECT.** It would collapse distinct strategy, evidence, creative, measurement, community, publishing-authority and execution boundaries that already have reusable professional ownership.

### Separate Channel Audit agent
**REJECT.** Most channel/account audit fields are directly observable system/integration state. Professional interpretation is already owned by existing research, measurement and strategy layers.

### Separate Organic Publisher agent
**REJECT.** Current evidence supports deterministic execution plus explicit release authority, not a new stable profession core.

### Reuse Automotive Capture Direction as-is for Personal Brand
**REJECT.** The current candidate is automotive-domain specific and NOT QUALIFIED. Its architecture can be used as precedent, but its professional/evaluation evidence does not automatically transfer to personal-brand capture.

### Make Market Intelligence choose positioning
**REJECT.** Its qualified boundary stops at evidence and bounded implications; strategy remains downstream.

## Constraints / locks created

1. **Applied repo is the authoritative place for the complete GAP classification matrix.**
2. **Do not create professional cores from this repository.**
3. **Do not send REUSE, SPECIALIZATION, CAPABILITY, DETERMINISTIC TOOL or REJECT decisions upstream merely to mirror applied architecture.**
4. **Only evidence-backed BUILD NEW or EXTEND requirements are candidates for upstream Agent Architect work.**
5. A candidate used in applied work must retain its exact upstream candidate status and contract.
6. Domain-specific candidate qualification does not transfer to another domain by analogy.
7. Publishing side effects require explicit authority and observed execution verification.
8. Registry inconsistency is maintenance, not evidence of a new profession.

## Upstream escalation rule

Use this gate before creating any task in `professional-ai-agents`:

`applied problem -> evidence of repeated/material professional failure -> existing core/candidate compatibility check -> alternatives/composition check -> Agent Architect classification -> only proven BUILD NEW or EXTEND -> upstream research/qualification work`

A classification of SPECIALIZATION, CAPABILITY or ADAPT does **not** automatically imply upstream work. Escalate only if the delta changes reusable professional behavior and the evidence supports EXTEND/BUILD NEW under Agent Architect methodology.

## Revisit triggers

Reopen this decision only when one of the following occurs:
- a relevant upstream core/candidate/version/status changes;
- repeated Personal Brand work exposes a material decision class not covered by the current composition;
- capture work demonstrates a reusable non-automotive professional delta;
- organic distribution requires irreducible professional judgment not reducible to strategy + creative + deterministic publishing;
- community/listening/reputation receives a new upstream candidate/release state;
- platform/tool constraints materially change the execution boundary.

Do not reopen merely because a new role title sounds useful.
