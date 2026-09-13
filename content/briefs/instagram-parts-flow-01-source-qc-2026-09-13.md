# PARTS-FLOW-01 — source proof / media QC

date: 2026-09-13
status: FUNCTIONAL_PROOF_PASS / VISUAL_SOURCE_INCOMPLETE
asset: PARTS-FLOW-01
owners:
- factual path: repository evidence
- content proof requirement: Content Architecture & Creative Structure v0.4 — QUALIFIED
- public script: Social Content Creative 0.1.0 + Authorial Voice v0.2 candidate

## Functional proof — PASS

Verified from current auto-parts-landing repository:

`Landing -> Edge Function -> requests + request_items + request-photos -> manager in BayerCRM`.

Additional verified details:
- one request can contain multiple parts for one vehicle;
- photo-backed part data is supported;
- frontend uses the existing `create-landing-request` path;
- a live BayerCRM multi-part smoke submission was verified on 2026-09-05;
- that smoke request produced one request and two `request_items`;
- the QA record was then removed and the request-number counter restored.

Evidence:
- `prostoali2207-gif/auto-parts-landing/docs/CRM_INTEGRATION.md`
- `prostoali2207-gif/auto-parts-landing/docs/v7-request-flow-enhancement-contract.md`
- `prostoali2207-gif/auto-parts-landing/docs/commercial-finalization.md`

## Current visual/source state

### Landing side
Repository contains rendered/proof assets and the request-flow implementation.

However the currently enumerated `.proof-assets` are not sufficient by filename/provenance alone to certify the exact public sequence required by PARTS-FLOW-01.

Do not pretend an unrelated render proves the submission path.

### BayerCRM side
Current repo contains:
- `Dashboard.tsx`;
- `RequestDetail.tsx`;
- `RequestStatus.tsx`;
- public request form and related workflow surfaces.

This proves the UI/workflow exists in code, but there is no current exact visual capture bound here that demonstrates the same submitted landing request appearing in the manager CRM.

## Verdict

**The script claim is evidence-safe.**

**The Reel is not yet SOURCE_READY_FOR_POST** because the visual proof transition still needs one clean current capture:

`landing request submission -> corresponding BayerCRM request/destination`.

This is a source-asset problem, not a script/strategy problem.

## Required source capture

Minimum:
1. real landing request surface;
2. visible request fields sufficient to understand vehicle / parts / photo structure;
3. submit/accepted state if safe to demonstrate;
4. real BayerCRM destination showing the corresponding request;
5. no private client data;
6. test/demo data only if a new demonstration record is created;
7. remove/clean the demonstration record afterwards if the production system should not retain it.

Do not invent a fake CRM screen or redraw the transition as if observed.

## Handoff

Once current visual proof exists:
- Content Creative can bind exact visuals to the approved candidate script;
- Narration & Voice Performance Direction v0.1 candidate may prepare/review the human voice take;
- Video Editing & Post-Production receives the accepted source package.

Until then:
**SCRIPT_READY_FOR_HUMAN_REVIEW / SOURCE_MEDIA_NOT_READY.**
