# User-feedback constraint leakage incident — 2026-09-13

decision_id: PBGS-PROF-GAP-007
status: ACTIVE / ROOT-CAUSE CONFIRMED
trigger: human project-owner correction during ORIENTATION-01 review

## Incident

The user previously corrected an upstream strategic mistake:
`do not imply that landing -> CRM is a mandatory service sequence`.

That correction was correctly captured as an internal service-independence constraint.

However, ORIENTATION-01 Content Architecture then promoted the internal guard into a public communication block:
`B3 — INDEPENDENCE`.

Social Content Creative subsequently verbalized that block with lines such as:
- `И нет, это не обязательно всё сразу.`
- `Нужен только лендинг — значит лендинг.`

The audience was therefore made to hear an internal design correction that existed only because the system had previously made a mistake.

## Failure class

`INTERNAL_CONSTRAINT_TO_PUBLIC_MESSAGE_LEAK`

Related systemic pattern:
`USER_FEEDBACK_OVERLITERALIZATION`.

## Root cause

### 1. Applied orchestration defect — PRIMARY

The system lacked an explicit semantic firewall between:
- user feedback about system behavior;
- internal constraints/guards;
- actual intended audience communication.

As a result, a user correction was treated as content material instead of as a boundary on future decisions.

### 2. Content Architecture v0.4 gap — PROFESSIONAL

The qualified core distinguishes HARD / COMMUNICATION / CONTEXTUAL / PREFERENCE constraints and packages MUST_PRESERVE locks.

But the current exact qualified artifact does not explicitly require classification of whether a constraint is:
- INTERNAL_ONLY;
- PUBLIC_MESSAGE_CANDIDATE;
- PUBLIC_MESSAGE_REQUIRED.

Therefore a correct HARD constraint can still be incorrectly promoted into a semantic block.

### 3. Social Content Creative — DOWNSTREAM, NOT ROOT

Creative received the independence clarification as an explicit architecture block and rendered it.

Creative should not be treated as the primary repair target for this incident because silently deleting a locked architecture block would itself cross its boundary.

## Agent Architect classification

- BUILD NEW: REJECT
- new profession: REJECT
- applied orchestration: REPAIR
- deterministic governance gate: ADD
- Content Architecture: EXTEND / NEW REVISION TRACK from qualified v0.4; do not mutate released v0.4
- Social Content Creative / Authorial Voice: RETEST after upstream repair; no mutation justified by this incident alone

## New semantic rule

User feedback must first be classified as one of:
- `PUBLIC_MESSAGE_REQUEST` — user explicitly wants this communicated to the audience;
- `OBJECTIVE_OR_STRATEGY_CHANGE` — changes what the system is trying to achieve;
- `INTERNAL_CONSTRAINT` — restricts future decisions but is not itself audience content;
- `FAILURE_REPORT` — evidence that the system/artifact failed;
- `PREFERENCE` — user taste/input for selection;
- `HYPOTHESIS_OR_EXAMPLE` — something to evaluate, not automatically adopt.

Only `PUBLIC_MESSAGE_REQUEST`, or content independently justified by the approved communication job, may be promoted into public copy.

An `INTERNAL_CONSTRAINT` should normally be satisfied by **absence of the prohibited implication**, not by explaining the constraint to the audience.

## Negative-constraint rule

Examples:

- `do not imply every landing needs CRM`
  -> correct execution: a landing asset simply stands alone;
  -> incorrect execution: `не всем нужен CRM, иногда нужен только лендинг` unless that distinction itself is audience-relevant.

- `do not lead with AI`
  -> correct execution: lead with buyer problem/service;
  -> incorrect execution: `не всем нужен AI` unless the content job is explicitly about AI misconceptions.

- `do not overclaim authorship`
  -> correct execution: use evidence-safe authorship wording;
  -> incorrect execution: add a public disclaimer about authorship when not relevant.

## Regression cases

### UFC-01 — negative user correction
Input: user says `не надо связывать лендинг и CRM как обязательную цепочку`.
Expected: store as INTERNAL_CONSTRAINT; future standalone landing content simply avoids the dependency.
Hard fail: public copy explains that services can be purchased separately without an independent audience reason.

### UFC-02 — AI category guard
Input: `не превращай бренд в AI-news/AI-first аккаунт`.
Expected: AI stays secondary.
Hard fail: orientation copy says `вам не обязательно нужен AI` merely because this guard exists.

### UFC-03 — claim-safety guard
Input: `не придумывай результаты/цифры`.
Expected: claims remain evidence-safe.
Hard fail: public script contains meta-disclaimer `я не буду обещать вам результаты` without communication justification.

### UFC-04 — explicit public request control
Input: user explicitly says `в ролике скажи, что можно заказать только лендинг отдельно`.
Expected: may become public message because user explicitly requested the audience message, subject to strategy/truth checks.

## Applied consequence

ORIENTATION-01 architecture v1 and Creative v1/v2 are invalid as production inputs.

Rebuild from the original communication job only:
`new viewer quickly understands the range of work Ali does`.

Service-independence remains an invisible internal guard.