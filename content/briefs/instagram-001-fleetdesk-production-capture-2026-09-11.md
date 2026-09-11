# Production Capture Plan — PBGS-IG-001 FleetDesk

plan_id: PBGS-CAPTURE-001
date: 2026-09-11
status: READY_TO_CAPTURE
upstream_brief: content/briefs/instagram-001-fleetdesk-contract-operational-state-2026-09-11.md
capture_core: Video Capture & Camera Operations v0.4 candidate — CANDIDATE / NOT QUALIFIED / DEVELOPMENT_PASS
capture_core_issue: professional-ai-agents#294

## Locked intent

Create a short Instagram Reel that communicates:
"В прокате договор — это не просто PDF. Это центр всей операции."

Must prove with real FleetDesk material that:
- contract links to client and car;
- payments/fines/Salik may link to the contract;
- contract status affects vehicle status through documented automation.

Do not claim:
- quantified savings;
- error reduction;
- revenue impact;
- sole authorship;
- that WhatsApp integration is already live/finished.

## Capture mode

Primary mode:
**screen-recorded product proof + voice-over.**

No face is required for this artifact.

Why:
- the product/system itself is the proof;
- removes unnecessary camera complexity;
- minimizes PII exposure risk compared with filming an active workplace;
- gives Post-Production clean source to annotate and pace.

## Capture package

### Source 1 — Contract context

Job:
establish that the content is about a real rental contract inside FleetDesk.

Capture:
- open a safe/test/redacted contract;
- show the contract screen or contract list;
- hold the screen still briefly before scrolling/tapping.

Operator:
- use a test/dummy contract if possible;
- if real data is used, redact or avoid every client name, phone, passport/EID/license number, contract UUID and sensitive financial detail.

QC:
- text/UI is sharp and readable;
- no notifications appear;
- no private data visible;
- no fast scrolling.

### Source 2 — Contract -> car/client relationship

Job:
prove that the contract belongs to a vehicle and client.

Capture:
- record the relevant contract area showing vehicle/client relationship;
- if UI exposes private data, capture a sanitized/test record or crop tightly enough to show only structural labels.

QC:
- viewer can understand "contract -> car/client" without needing narration alone.

### Source 3 — Related operational modules

Job:
show that FleetDesk is not only a contract document.

Capture short clean clips of:
- Contracts;
- Fleet;
- Payments;
- Fines;
- Salik.

Do not rapidly swipe through everything.
Each module clip should begin and end on a stable frame.

QC:
- module identity is legible;
- no sensitive rows/details readable.

### Source 4 — State logic proof

Job:
communicate:
Active/Expiring Soon contract -> car Rented;
Completed/Cancelled + no other active contract -> car Available.

Preferred capture:
- safe test/demo state change in FleetDesk, if it can be shown without altering production data.

Fallback:
- do NOT mutate live production for the video;
- provide screen captures of the relevant states and let Post-Production create a truthful annotated flow based on the verified repository rule.

This fallback is preferred over performing risky live actions solely for content.

### Source 5 — System relationship map assets

Job:
give Post-Production clean building blocks for:
Contract -> Client
Contract -> Car
Contract -> Payments
Contract -> Fines
Contract -> Salik

Capture requirement:
- no fake system diagram is required at capture stage;
- supply real UI screenshots/screens plus the verified relationship list from the brief.
Post-Production may build the simplified graphic as a communication layer while preserving actual relationships.

## Voice-over capture

Record separately after screen capture.

Script:
"В прокате договор — это не просто PDF. Это центр всей операции.

В FleetDesk контракт связан с конкретным клиентом и машиной.

Статус договора меняется по сроку аренды.

Активный договор переводит машину в Rented. Когда аренда завершена и другого активного договора нет — машина возвращается в Available.

К этому же договору могут быть привязаны платежи, штрафы и Salik.

То есть мы строим не набор экранов. Мы строим состояние бизнеса, где одна операция меняет связанные части системы.

Вот что я называю: реальная операционная проблема — работающая система."

Audio execution:
- quiet room;
- phone close enough that speech is clear;
- do a 10-second test first and listen back;
- avoid AC/traffic noise where possible;
- record 2 full takes;
- then record the hook and payoff as separate backup takes.

Do not add music at capture stage.

## Screen-recording operator sequence

1. Turn on Do Not Disturb.
2. Close unrelated apps/tabs.
3. Prepare only safe/test/redacted FleetDesk records.
4. Start screen recording.
5. Hold each starting screen stable before any touch.
6. Perform one action at a time.
7. Stop scrolling once the relevant proof is visible.
8. Hold the ending frame before moving to the next clip.
9. Record separate clips rather than one long chaotic walkthrough.
10. Replay every clip immediately and check privacy + readability.

## Minimum source set

Required before handoff to Post:
- 1 clean Contract clip;
- 1 contract/car/client relationship clip;
- 1 Fleet clip;
- 1 Payments clip;
- 1 Fines clip;
- 1 Salik clip;
- evidence/screens for state logic;
- 2 full voice-over takes;
- separate hook backup;
- separate payoff backup.

## Source QC

media observed: NO

Therefore:
- this plan is READY_TO_CAPTURE;
- SOURCE_READY_FOR_POST cannot be claimed yet.

After capture, review each source for:
- PII/security exposure;
- readability;
- orientation;
- notification contamination;
- accidental taps/navigation errors;
- missing proof;
- speech clarity;
- coverage completeness.

Any clip exposing private customer data = REJECT / RESHOOT.

## Handoff to Post

After source QC passes:
- route to qualified Video Editing & Post-Production;
- preserve exact claims and relationships;
- Post may create diagrams/annotations from verified relationships;
- Post must not imply additional automation or business outcomes;
- known limitation: no public performance/result claim exists yet.
