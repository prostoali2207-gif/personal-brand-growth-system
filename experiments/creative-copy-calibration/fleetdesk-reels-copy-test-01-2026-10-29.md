# FleetDesk | Short-form spoken copy calibration 01

date: 2026-10-29
status: CREATOR RATED / B PREFERRED OVER A / B2 REVISION REQUESTED / NO PUBLICATION APPROVAL
source project: prostoali2207-gif/uae-drive-suite
source code: https://github.com/prostoali2207-gif/uae-drive-suite/blob/main/supabase/migrations/20261027141500_activate_fully_signed_draft_contracts.sql
source owner: Social Content Creative v0.1.0 QUALIFIED; spoken-language extension Authorial Voice v0.4 CANDIDATE NOT QUALIFIED
reference process: creative reference / authorial skill candidate, existing source reference recorded at decisions/social-content-authorial-voice-gap-2026-09-13.md. No claim of new independent elite benchmark.
genre: truthful real-project Reels script, not standalone humor.
audience input: the user's established owner-facing brand about sites, CRM, internal systems; NOT a car-sales ad.
hypothesis-only: a concrete UI contradiction plus actual rule will outperform generic tech feature copy in his own editorial assessment.
brief approval: NOT APPROVED; exploratory script calibration only. No strategic objective or channel publication decision inferred.

## Source of truth
- User directly reported signed contracts staying Draft and requested status transitions in the application (conversation context).
- Verified repository migration defines triggers on new client/manager/additional-driver signatures and sets Active only for Draft, all required signers present, and unexpired contract. Does NOT prove deployed migration or that every historical Draft became Active.
- Cannot assert current production effect, fewer errors, savings, happy users, deployment completion, or actual CRM visuals until observed.
- No named customers, signatures or private contract details should appear in public footage. Use fully anonymized demo or owner-authorized production capture.

## Locked variant A: inspectable UI contradiction
Вот договор. Подписи стоят. А в списке FleetDesk он всё ещё «Черновик».

Если статус отстаёт от документа, списку договоров уже не доверяешь.

Мы прописали проверку: клиент, менеджер и все дополнительные водители должны подписать договор. Плюс срок аренды ещё должен действовать.

Тогда система может перевести договор в «Активен».

Код уже есть. Теперь проверим на действующем договоре.

## Locked variant B: nonobvious business rule
Клиент подписал договор аренды. Казалось бы, можно ставить «Активен».

А если есть дополнительный водитель? Его подпись тоже нужна. И подпись менеджера.

Поэтому в FleetDesk прописали правило: статус меняется, только когда собраны все обязательные подписи и срок аренды ещё не вышел.

Вот так одно слово в списке получает проверяемый смысл.

Работу правила на живом договоре ещё нужно подтвердить.

## Independent-ish editorial self-review (NOT separate-model blind evaluation)
A:
- Proof: grounded in source-reported bug plus actual trigger; spoken first-shot visual is conditional on access to sanitized real UI.
- Mechanism: visible mismatch at second 1, reason, fix condition, honest verification.
- Weakness: direct first sentence "подписи стоят" assumes a fully signed screenshot we have not yet verified/obtained; release gate prevents this claim until visual proof. Voice not inherently witty.
B:
- Proof: contract requirement from migration; "Казалось бы" is rhetorical hypothetical not invented dialogue.
- Mechanism: point out underappreciated additional-driver signature, reveal complete rule.
- Weakness: weaker visual hook, mildly explanatory closer, less immediate tension.
Selection for review: A is the primary *draft candidate* IF sanitized, real mismatch and test capture exist. Otherwise B may be easier with diagram but still needs valid source visuals. Neither is declared strong or approved before first-party creator review.

## Release / test gates
1. User rates A or B or both poor. Explicit single question; do NOT use opposed good/bad checklists, per previous polarity inversion.
2. Confirm current deployment and reproduce signed-Draft state in authorized anonymized data or staged environment. Do not claim historical case on-camera without proof/screenshot.
3. Confirm rule actually fires on the final required signature and remains inactive for incomplete/expired agreements. Check current environment; migration on default branch only proves intended code.
4. Use anonymized footage. No client name, passport, Emirates ID, phone, signature, plate, or personal documents.
5. No music, user preference. Dialogue plus natural interface/click sound only. No claims about performance or conversion, and no CTA invented.
6. For publication, strategy/content architecture brief, assets, explicit creative approval and separate edit/publish handoff remain required.

## Review hypotheses
This is not a humor grade. Strong content selection should use real fact, visible contradiction, causal resolution, short spoken phrasing. No invented reaction or 'AI expert' image. The writer may choose to include zero jokes if none clearly improves the story.

## Creator result, 2026-10-29
Exact feedback: "Тест сценариев FleetDesk №1. Моя оценка: B лучше. Зафиксируй оценку, разберись в качестве текста и переходи к следующему этапу."
- User directly prefers variant **B** over **A** in this ONE comparison; original A and B preserved unchanged.
- No numerical rating, endorsement for publication, or explicit reason was supplied. Do not infer "B is universally better" or that the audience will watch longer.

### Diagnostic judgment (hypothesis, not user's stated reason)
- B's opening is a concrete decision dilemma, and the reveal of additional-driver + manager signatures is causally connected to its hook. No need to assert that there is a currently observed inconsistent UI.
- A's opening requires a verified shot of a fully signed contract still in Draft, which has not been captured; it also explains the issue in more abstract administrative terms ("списку уже не доверяешь") and suggests system distrust with no observed business outcome.
- B has flaws: a filler transition "Казалось бы"; vague abstract closing "одно слово ... проверяемый смысл"; an administrative "still needs checking" epilogue that weakens the viewer payoff. If user chooses B this does NOT automatically mean B is finished.
- Mechanism hypothesis to retest: audience-facing WHAT IF -> overlooked required signer -> precise validation rule. Do not force comedy; no user evidence asked for a joke in this artifact.

### Next stage
- Produce **B2 as a new version**, do not mutate locked B.
- Compress speech, replace vague closing with a causally useful fact, keep all caveats about code existence versus deployment verification in the production handoff.
- Build shoot plan on anonymized/staged footage only; verify the database trigger actually deployed and fires on last required signature before claiming observable production success.
- See `experiments/creative-copy-calibration/fleetdesk-reels-copy-b2-2026-10-29.md`.
