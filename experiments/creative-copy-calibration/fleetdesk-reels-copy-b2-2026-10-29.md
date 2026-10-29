# FleetDesk Reels | B2 revision and preproduction packet

date: 2026-10-29
status: DRAFT / CREATOR APPROVAL PENDING / VIDEO CAPTURE BLOCKED UNTIL EVIDENCE CHECK
source: experiments/creative-copy-calibration/fleetdesk-reels-copy-test-01-2026-10-29.md
locked_original: variant B, unchanged in predecessor
creator_fact: "B лучше" (preferred to A), no stated rationale or public approval
owner: Social Content Creative 0.1.0 QUALIFIED, Authorial Voice 0.4 CANDIDATE / NOT QUALIFIED (applied EXTEND)
source_code: https://github.com/prostoali2207-gif/uae-drive-suite/blob/main/supabase/migrations/20261027141500_activate_fully_signed_draft_contracts.sql
purpose: exploratory copy craft on a real documented project; Instagram audience/offer/campaign strategy not inferred

## B2 spoken draft (NEW VERSION, not a replacement for locked B)

Клиент подписал договор. Можно сразу ставить «Активен»?

А если в договоре есть второй водитель? Его подпись тоже нужна. И подпись менеджера.

В FleetDesk мы прописали правило: договор должен автоматически стать активным только после всех обязательных подписей. И только если аренда ещё действует.

Одна недостающая подпись, и автоматическая активация не сработает.

## What changed from B and why (professional judgment, not user explanation)
- Keep B's real rule-based dilemma; avoid claiming verified real UI mismatch as in A.
- Remove "Казалось бы", generic abstractions ("одно слово ... проверяемый смысл"), and the weak spoken epilogue "работу правила на живом договоре ...".
- Keep the actual important distinction: main client, manager, every additional driver, and still-valid end datetime; one unsigned participant stops **automatic** transition.
- Deliver a concrete final consequence instead of an advertising CTA or a moral.
- The only confirmed user rating so far is B > A; B2 itself is not independently assessed.
- No mandatory joke. The specific business logic is more relevant than arbitrary dark-humor material for this post.

## Source/claim verification
Evidence in SQL function `internal.activate_fully_signed_draft_contract`:
- Active status update only for `status = 'Draft'`.
- `client_signature` present and `manager_signature` present.
- No additional `contract_drivers` row with blank `signature`.
- Contract end date/time in Asia/Dubai is in the future.
- Trigger called after relevant signature updates on contracts or contract_drivers.
- The function is visible in source repository. Whether this migration was deployed and works correctly with the current production app remains **UNVERIFIED**. Writing "мы прописали правило" is supported; claiming "мы уже устранили ошибки / теперь в production всё автоматически работает" is NOT supported.
- Phrase "должен автоматически стать активным" intentionally describes intended rule, not proof of live operational success.

## Video shot/intention plan (conditional, no invented footage)
1. 0-3 s: display anonymized **demo** contract with a client signature state and prominent Draft status. If no sanitized/staged dataset exists, show a schematic with DEMO label; do not portray a real customer's recorded incident.
2. 3-9 s: detail row for a second driver and manager, visibly incomplete signatures; do not show real signatures, names or IDs.
3. 9-17 s: check sequence highlighting required signers + unexpired contract. Prefer actual verified app interface; otherwise use a labeled diagram based on implementation rule.
4. 17-23 s: show the trigger condition or a verified staging transition after final required signature. Never edit a staged transition to imply a production event.
5. End on "автоматическая активация не сработает" with interface emphasis, not a forced promotional CTA.

## Required before public video
- Confirm production/staging deployment of migration; test normal case, missing client, missing manager, missing driver and expired rental. Avoid touching real contracts solely for filming.
- Record anonymized/screensafe captures with access permission. Never reveal passport, Emirates ID, driver licence, actual signatures, contacts or contract financial data.
- If a real demonstration cannot be verified, portray a code explanation or labeled simulation transparently. Consider pausing video release until evidence capture exists.
- No background music. Natural interface sounds or speech only, following creator constraint.
- Get specific owner approval for wording and publishing; this text is not approved/published.

## Editorial checks (manually verifiable)
- Russian conversational spoken clauses; no artificial hype, "не X, а Y" formula, long display dashes or fake customer dialogue.
- Two factual anchors: multiple required signatures and valid term, both confirmed in code.
- The dramatic situation is hypothetical/conditional; not a documented quotation from a customer.
- Semantics and wording of B2 checked via local quality gate; script contains no known prohibited joke-template phrases.
- Creator still must evaluate B2; no view/retention/conversion claim.
