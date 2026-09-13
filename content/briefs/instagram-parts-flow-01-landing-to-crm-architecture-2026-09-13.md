# PARTS-FLOW-01 — Landing -> CRM buyer-facing architecture

date: 2026-09-13
status: ARCHITECTURE READY WITH BOUNDS / PUBLIC COPY LANGUAGE UNRESOLVED
portfolio_decision: PBGS-PORTFOLIO-002
owning_core: Content Architecture & Creative Structure Practitioner v0.4 — QUALIFIED / RELEASED exact-version artifact
channel: Instagram
role: FRONT-DOOR OFFER + DEPTH SIGNAL
source_project: Auto-parts landing + BayerCRM

## COMMUNICATION_JOB

Show a non-technical business owner that a landing page can be the visible front door of a real enquiry workflow rather than an isolated page.

The asset must communicate:

`customer submits request -> business receives a structured request in CRM`

Commercial implication:
the user's website/landing capability can connect into deeper CRM/process work when the business needs it.

Do not turn that implication into a guarantee or unsupported performance claim.

## ATTENTION_CONTRACT

Selected opening family:
**PROCESS QUESTION / DEMONSTRATION**

Opening job:
create one buyer-legible question:

**what happens after a customer sends the form?**

Why this family:
- immediately relevant to a website/landing buyer;
- the payoff is directly observable in the verified landing-to-CRM path;
- requires no technical vocabulary;
- allows the deeper CRM capability to be demonstrated rather than listed.

Rejected opening families:

### "Your leads are getting lost"
REJECT:
would imply an evidenced loss/problem state that has not been established for this project or the viewer.

### "Backend / integration"
REJECT:
implementation-first and inappropriate for the primary non-technical buyer.

### "AI built this"
REJECT:
wrong commercial category and not required for the communication job.

## INFORMATION_ORDER

### B1 — CUSTOMER ACTION
Job:
show the visible business-facing entrypoint.

Information:
customer opens the landing/request surface and submits a parts request.

Proof:
real landing UI.

Visual requirement:
the viewer must understand the action without reading code or implementation labels.

### B2 — REQUEST HAS BUSINESS STRUCTURE
Job:
show that this is not merely a generic contact message.

Information:
the implemented request flow can carry structured request data, including multiple parts per vehicle and photos where the real interface demonstrates them.

Proof:
real form/request fields and/or submitted request artifact.

Boundary:
do not claim every landing project needs this exact structure.

### B3 — BUSINESS RECEIVES IT IN CRM
Job:
deliver the main proof/payoff.

Information:
the request proceeds into BayerCRM for the manager.

Proof:
real BayerCRM request surface or repo-backed observable destination.

Visual requirement:
make the relationship `landing request -> CRM request` unmistakable.

Technical implementation:
Edge Function / database tables are not required in the primary presentation.

### B4 — COMMERCIAL MEANING
Job:
translate proof into the service category.

Required meaning:
a website/landing can be built as part of the business's enquiry flow, not merely as a disconnected page.

Creator may express this in ordinary buyer language.

Do not claim:
- more leads;
- faster response;
- no lost requests;
- conversion improvement;
- revenue impact;
unless separately evidenced.

### B5 — DEPTH SIGNAL
Job:
briefly establish that if the business needs it, the work can continue beyond the page into CRM/integration.

This should remain secondary to the landing-page service.

No service-list dump.

## PROOF_PLAN

Strongest proof sequence:
1. real landing request surface;
2. one understandable request submission;
3. real corresponding BayerCRM request/destination;
4. simple visual connection between the two.

Optional supporting proof:
- repo-backed diagram only if the real transition cannot be shown clearly.

Rejected proof substitutes:
- code montage;
- generic automation graphics;
- logos only;
- AI visuals;
- backend terminology without buyer meaning.

## PACING_INTENT

Relative short-form bands:

- 15–20% — question / customer action;
- 30–35% — landing request demonstration;
- 30–35% — CRM destination / proof;
- 15–20% — business meaning + depth signal.

Priority:
the landing-to-CRM relationship must receive more attention than technical implementation.

If the asset is too dense:
remove implementation detail first.

## VISUAL_COMMUNICATION_REQUIREMENTS

Must show:
- the actual landing or request interface;
- the actual business-relevant request data;
- the CRM receiving/destination state.

Recurring visual grammar:
`customer action -> submitted request -> manager/system destination`.

Do not show:
- source code as primary proof;
- fake dashboards;
- technical labels that the primary viewer cannot decode;
- irrelevant 3D/hero visuals unless they directly help explain the request path.

## CREATOR_HANDOFF

### MUST_PRESERVE
- non-technical buyer;
- Website/Landing is the front-door service;
- CRM/integration is the deeper capability signal;
- verified landing -> BayerCRM relationship;
- no performance claims;
- no AI/category drift;
- no implementation jargon as the communication job.

### BOUNDED
- exact hook wording;
- authorial humor;
- whether "CRM" itself is spoken or only shown/labeled;
- exact closing line.

### MAY_CHOOSE
- metaphor only if it keeps the workflow accurate;
- conversational register;
- how much of the request form is shown;
- visual connector/annotation.

### UNRESOLVED NON-BLOCKING
- exact CTA is not approved;
- exact service package/pricing is not approved.

### BLOCKED PORTION
**Final public copy language.**

Owner:
upstream commercial/channel strategy + user decision.

Need:
choose the intended commercial language market:
- Russian;
- English;
- bilingual/mixed.

Architecture remains valid across those options; exact script should not be finalized until this is locked.

### MUST_ESCALATE
- stronger authorship claim;
- performance/result claim;
- need to describe unverified client outcome;
- request to make AI the primary message;
- source media cannot actually demonstrate the landing-to-CRM relationship.

## VERDICT

**READY FOR SOURCE-ASSET CHECK AND CREATIVE ONCE PUBLIC LANGUAGE IS LOCKED.**

The correct first asset is a buyer-facing real-work demonstration, not an AI explainer and not a generic services introduction.
