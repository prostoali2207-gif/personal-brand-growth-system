# Content Brief PBGS-IG-001 — FleetDesk: contract as operational state

brief_id: PBGS-IG-001
date: 2026-09-11
status: DRAFT / CREATOR OUTPUT READY FOR HUMAN REVIEW
channel: Instagram
architecture: PBGS-CA-01 with CA-03 proof layer
source_project: FleetDesk
creator_core: Social Content Creative 0.1.0 — QUALIFIED per library manifest
release_authority: human only

## Communication job

Show a UAE business operator that FleetDesk is not merely a collection of screens: a rental contract is modeled as an operational object connected to the car, client, payments, fines and Salik, with system state changing around it.

## Audience relevance

Primary:
- rental / service-business owner-operators and operations managers who deal with multiple connected operational objects.

Secondary:
- builders interested in operational SaaS / automation architecture.

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
specific operational correction.

Core idea:
"A rental contract is not just a PDF. It is a state-changing object inside the business system."

Proof mechanism:
visual relationship map + real FleetDesk screens / repository-backed system rules.

Payoff:
viewer understands the difference between a document UI and an operational system.

## Candidate hook set

A — recommended:
"В прокате договор — это не просто PDF. Это центр всей операции."

B:
"Если договор не меняет состояние машины и не связывает платежи, штрафы и Salik — это просто документ, не система."

C:
"Вот разница между CRM-экраном и настоящей операционной системой проката."

Selection:
A. It is simplest, truthful, concrete and leaves proof burden the content can satisfy.

## Draft spoken / on-screen script

HOOK
"В прокате договор — это не просто PDF. Это центр всей операции."

DEVELOPMENT
"В FleetDesk контракт связан с конкретным клиентом и машиной."

PROOF 1
"Статус договора меняется по сроку аренды."

PROOF 2
"Активный договор переводит машину в Rented. Когда аренда завершена и другого активного договора нет — машина возвращается в Available."

PROOF 3
"К этому же договору могут быть привязаны платежи, штрафы и Salik."

PAYOFF
"То есть мы строим не набор экранов. Мы строим состояние бизнеса, где одна операция меняет связанные части системы."

CLOSURE
"Вот что я называю: реальная операционная проблема -> работающая система."

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
- FleetDesk contract screen or contract list.
- On-screen text: "Договор ≠ просто PDF"
- communication job: immediate category correction.

SHOT/VISUAL 2 — relationship map
- simple real-data-derived map:
  Contract -> Client
  Contract -> Car
  Contract -> Payments
  Contract -> Fines
  Contract -> Salik
- do not add relationships not present in schema.

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
explain the modeling decision: a rental contract should be treated as an operational state object, not only a document.

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
