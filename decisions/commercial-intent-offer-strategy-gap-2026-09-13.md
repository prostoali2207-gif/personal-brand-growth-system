# Commercial Intent / Offer Strategy GAP — 2026-09-13

decision_id: PBGS-PROF-GAP-004
date: 2026-09-13
status: ACTIVE / ROOT-CAUSE CLASSIFIED
owner: Agent Architect v1.2 methodology
trigger: user could not understand PBGS-LAUNCH-01 and identified that the content read more like AI/technical positioning than client-facing promotion for websites/landings/CRM/automation services

## Incident

The applied system built audience, positioning and content from verified project evidence without first locking the user's commercial objective.

As a result:
- technical capabilities became category signals;
- professional-agent engineering was elevated into launch content;
- implementation terms such as backend/qualified/evaluation appeared in a first-contact script for ordinary business clients;
- the produced content demonstrated capability but did not clearly serve the user's intended commercial direction.

The failure is not repaired by simplifying vocabulary inside the same script.

## FACT / EVIDENCE

### Missing authoritative input

Before this incident, `source-of-truth/` contained identity/project evidence but no current commercial-intent/offer record.

Growth Strategy & Experiment Portfolio v0.1 begins its workflow from:
`business objective -> evidence audit -> ...`

Its model does not authorize inventing the business objective from the project portfolio.

Therefore the applied system crossed a required-input boundary.

### Current user-confirmed commercial direction

The user wants the personal brand to attract ordinary business clients for practical digital work including:
- websites / landing pages;
- CRM;
- automation;
- integrations / related systems.

The buyer does not need to understand AI, backend or agent engineering in order to become a client.

AI remains evidence / implementation capability, not the default commercial category.

This is now recorded in:
`source-of-truth/current-commercial-intent.md`.

## Root cause

Two-layer failure:

1. **SOURCE-OF-TRUTH GAP**
   - no commercial objective / service direction was locked before strategy.

2. **APPLIED ORCHESTRATION FAILURE**
   - strategy was allowed to proceed despite the missing required business-objective input;
   - project evidence was incorrectly promoted into commercial positioning.

This incident does not prove that Content Architecture or Social Content Creative is weak.

## Agent Architect compatibility

### Market & Competitive Intelligence 1.0.0
**REUSE**
- research buyer problems, alternatives, competitor offers and market language.
- does not choose the user's commercial offer by itself.

### Growth Strategy & Experiment Portfolio v0.1 — CANDIDATE / NOT QUALIFIED
**REUSE / ADAPT through Personal Brand Strategy specialization**
- can work from an authoritative business objective;
- must not invent that objective from technical evidence.

### Sales / Lead Conversion 0.5.0
**REUSE downstream**
- owns qualified inbound and conversion conversations;
- does not define the upstream service portfolio.

### Conversion Strategy & Landing Page Architecture (#246)
**REJECT as owner of the personal-brand service offer**
- its scope is page-level commercial/conversion architecture;
- it may later consume an approved offer when building the user's own landing page.

### Content Architecture / Social Content Creative
**REJECT as offer owners**
- downstream only.

## Classification

### Immediate root repair
**MISSING AUTHORITATIVE BUSINESS INPUT + ORCHESTRATION GATE**

### Remaining professional decision class
**SPECIALIZATION + CAPABILITY: Commercial Offer & Service Positioning**
inside the current Personal Brand Strategy layer.

Current evidence is insufficient for `BUILD NEW`.

Reason:
- the immediate failure came from missing business truth, not absence of creative competence;
- offer/service packaging is adjacent to positioning/strategy;
- exact reusable professional boundary is not yet demonstrated across multiple applied contexts;
- a new professional core would be premature.

## Applied responsibility of Commercial Offer & Service Positioning

Own, when explicitly invoked:
- which services are actually being offered now;
- which buyer problem each service addresses;
- service/category hierarchy;
- what belongs in the front-door offer vs proof/technical depth;
- whether AI is an offer, a differentiator, an implementation method or irrelevant to the buyer-facing message;
- offer scope and non-offer boundaries;
- handoff constraints to content and sales.

Does not own:
- final social copy;
- exact landing-page copy;
- sales closing;
- unsupported results/pricing/guarantees;
- technical implementation.

## Required gate

Before audience/positioning/content work that has commercial intent:

`CURRENT COMMERCIAL INTENT -> OFFER/SERVICE POSITIONING -> MARKET/AUDIENCE STRATEGY -> CONTENT PORTFOLIO -> CONTENT ARCHITECTURE -> CREATIVE`

Fail closed if the first two layers are absent.

## Dependent artifacts invalidated for launch use

The following were produced from the wrong upstream commercial assumption and must not continue as launch decisions until strategy is rerun:
- `decisions/audience-channel-role-strategy-2026-09-11.md`;
- `decisions/initial-content-portfolio-launch-sequence-v1-2026-09-13.md`;
- `content/briefs/instagram-launch-001-multi-project-category-architecture-2026-09-13.md`;
- `content/briefs/instagram-launch-001-authorial-voice-v02-2026-09-13.md`.

Project evidence and the broad identity thesis may be reused, but their commercial interpretation must be re-evaluated.

## Regression cases

### CO-01 — technical portfolio without business objective
Input:
multiple strong technical projects, no authoritative current commercial objective.

Expected:
BLOCK / request authoritative business direction.
Do not infer the offer from repositories.

### CO-02 — non-technical buyer
Input:
ordinary business buyer seeking a landing/CRM/automation outcome.

Expected:
buyer-facing communication uses business/problem language.
Technical terms appear only when necessary and translated.

### CO-03 — AI as implementation capability
Input:
real AI-agent competence exists but the buyer is purchasing a landing/CRM/automation service.

Expected:
AI may support proof/differentiation.
Do not make AI the primary category automatically.

### CO-04 — technical audience content
Input:
explicit approved objective targets builders/AI peers.

Expected:
technical agent/evaluation language may be appropriate.
Do not apply the non-technical buyer simplification universally.

### CO-05 — exact offer unresolved
Input:
commercial direction known, exact packages/pricing not yet approved.

Expected:
strategy may work at service-category level with explicit bounds.
Content must not invent package, price, guarantee or CTA.

## Upstream action

**NO SEND now.**

Escalate to `professional-ai-agents` only if repeated applied work demonstrates a reusable professional behavior gap that cannot be contained in Personal Brand Strategy specialization or an existing commercial-strategy profession.
