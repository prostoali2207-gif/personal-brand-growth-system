# Content Brief PBGS-IG-001 — From business operation to working system

brief_id: PBGS-IG-001
date: 2026-09-11
status: REVISED / CREATOR REWORK REQUIRED
channel: Instagram
architecture: PBGS-CA-01 with CA-03 proof layer
source_project: FleetDesk
creator_core: Social Content Creative 0.1.0 — QUALIFIED per library manifest
release_authority: human only


## Strategic role lock

Owner: Growth Strategy & Experiment Portfolio v0.1 — CANDIDATE / NOT QUALIFIED, under the active audience/channel strategy.

- FleetDesk is **evidence of capability / a case from real work**, not the offer being sold by this Reel.
- The strategic objective is to build credible professional demand around the demonstrated ability to turn real operational problems into working systems and make future qualified project conversations possible.
- Therefore this Reel must not become a FleetDesk feature tour, product advertisement, or exhaustive proof of every module.
- Product details are included only when they support the higher-level proof: real operational problem -> system reasoning -> working implementation.
- The viewer takeaway should be transferable beyond car rental: "this person/team can reason about an operational problem and build a working system around it."

## Communication job

Start from a **cross-industry operational systems principle**, then use FleetDesk only as concrete proof that the principle was implemented in real software.

The Reel must answer a transferable question:

> What separates a screen that stores data from a system that actually reflects business rules and connected operational state?

FleetDesk is the evidence layer, not the subject category.

The viewer should not need to run a car-rental business to recognize the principle or see the capability.

## Audience relevance

Primary:
- owner-operators, operations leaders and digitally responsible managers in small-to-mid-sized service businesses with fragmented workflows, disconnected objects or manual handoffs.

Secondary:
- builders interested in operational SaaS / automation architecture.

Car-rental operators are **not** the target category for this Reel. Rental is only the current proof environment.

## Exact truth packet

VERIFIED:
- FleetDesk is a UAE car-rental management SaaS.
- It is documented as production and used by company managers.
- Contracts reference a client and car.
- Payments can reference a contract.
- Fines can reference a contract.
- Salik can reference a contract.
- contract status is automatically computed from end date.
- Active/Expiring Soon contracts set the car status to Rented.
- Completed/Cancelled contracts can return a car to Available when no other active contract exists.
- FleetDesk includes fleet, clients, contracts, payments, fines, Salik and reports.

NOT APPROVED / DO NOT CLAIM:
- exact time saved;
- exact error reduction;
- revenue impact;
- customer count;
- sole authorship;
- "everything is fully automated";
- WhatsApp integration is currently live/finished.

## Creative mechanism

Opening family:
cross-industry system correction.

Core idea:
"A business system is not defined by how many screens it has. It is defined by whether real business rules connect the objects and change operational state."

Proof mechanism:
state one general systems principle -> show one compact FleetDesk example -> return immediately to the transferable principle.

FleetDesk proof should be brief:
- contract linked to client + car;
- contract status follows rental term;
- active contract changes the car to Rented;
- completed/cancelled can return the car to Available when no other active contract exists;
- payments/fines/Salik can link to the same contract.

Do **not** explain rental operations as the main lesson.

Payoff:
viewer understands that the demonstrated capability is modeling real operations into connected software, regardless of vertical.

## Hook direction — CREATOR TO REWORK

Preferred opening job:
correct a common systems misconception without naming car rental first.

Mechanism examples, not approved final copy:
- "Интерфейс ещё не делает продукт системой."
- "Система начинается там, где действие меняет связанные части бизнеса."
- "Хранить данные — одно. Отражать реальные правила бизнеса — совсем другое."

Avoid:
- "В прокате..."
- FleetDesk feature-list openings;
- niche-specific terminology before the transferable principle is established.

## Spoken script status

The prior rental-first script is **superseded**.

Social Content Creative must generate a new authorial script under the following locked sequence:

1. **GENERAL PROBLEM / PRINCIPLE**
   A business tool can display/store objects without actually modeling how those objects affect one another.

2. **REAL PROOF**
   Use FleetDesk for one compact example:
   contract -> client/car -> status rule -> vehicle state.
   Payments/fines/Salik may appear only as supporting proof, not as a feature list.

3. **TRANSFERABLE PAYOFF**
   The capability demonstrated is translating operational rules into a working connected system.

4. **CLOSURE**
   Brand/idea closure only. No sales CTA until strategy approves it.

The final wording belongs to Social Content Creative; authorial-voice candidate work must remain explicitly CANDIDATE / NOT QUALIFIED until its evaluation completes.

## Claim ledger

1. "FleetDesk contract is linked to client and car"
Evidence: FLEETDESK_CONTEXT.md / contracts schema
Status: VERIFIED

2. "Contract status changes by rental term"
Evidence: contracts_set_status + refresh_contract_statuses description
Status: VERIFIED

3. "Active/Expiring Soon contract sets car to Rented"
Evidence: FLEETDESK_CONTEXT.md vehicle-status automation
Status: VERIFIED

4. "Completed/Cancelled can return car to Available if no other active contract"
Evidence: FLEETDESK_CONTEXT.md vehicle-status automation
Status: VERIFIED

5. "Payments/fines/Salik can link to contract"
Evidence: DB schema
Status: VERIFIED

6. "We build a business-state system, not a set of screens"
Type: CORE JUDGMENT / positioning expression
Status: ALLOWED as interpretation, not quantified outcome.

## Visual execution

SHOT/VISUAL 1 — hook
- abstract-but-real business-system framing using the existing FleetDesk recording as background proof, not as a rental-specific lesson.
- on-screen wording should express the general system principle.
- communication job: make the idea relevant before the viewer decides "this is only about car rental".

SHOT/VISUAL 2 — compact proof map
- show only the minimum relationship path needed to prove connected system logic:
  Contract -> Client
  Contract -> Car
  Contract status -> Vehicle state
- optional supporting references: Payments / Fines / Salik.
- do not add relationships not present in schema.
- do not dwell on module inventory.

SHOT/VISUAL 3 — state logic
- show or animate:
  Active contract -> Car: Rented
  Completed/Cancelled + no active contract -> Car: Available
- communication job: prove state change.

SHOT/VISUAL 4 — real product proof
- brief FleetDesk UI screen(s) showing relevant modules.
- avoid exposing client PII, contract IDs, phone numbers or financial data.

SHOT/VISUAL 5 — payoff
- return to simplified system map.
- on-screen text may express "операция -> состояние системы".

## Production bounds

- Screen recordings must use safe/test/redacted data.
- No client documents, names, phone numbers, IDs, contract UUIDs or sensitive financial detail.
- No generic AI imagery needed.
- No music requirement is introduced here.
- Final edit, pacing, audio treatment and caption implementation belong to Video Editing & Post-Production.

## CTA

No conversion CTA approved upstream.

Current allowed closure is brand/idea closure only:
"Вот что я называю: реальная операционная проблема -> работающая система."

Do not add "пиши мне", "закажи", "могу сделать вам", lead magnet or sales CTA without strategy approval.

## LinkedIn adaptation seed

Do not copy the Reel verbatim.

Opening job:
explain the broader modeling decision: operational software becomes useful when business rules connect objects and state, not merely when data is displayed in separate screens.

Suggested structure:
1. contract as system object;
2. relationships to client/car/payments/fines/Salik;
3. state automation;
4. why this boundary matters for operational software;
5. explicit limitation: no quantified impact claim;
6. repository/product proof.

Exact LinkedIn copy is a separate Creator artifact.

## Review gate

Before production:
- confirm screenshots can be captured without private client data;
- verify current production schema still matches cited state rules;
- human approves public use of FleetDesk name/screens.

Before publishing:
- human release approval required.
