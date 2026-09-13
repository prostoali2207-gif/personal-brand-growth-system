# Authorial Voice v0.4 — 3-case practical stress test

date: 2026-09-13
status: DEVELOPMENT PRACTICAL / NOT QUALIFICATION EVIDENCE
candidate:
- Social Content Creative 0.1.0 — QUALIFIED parent
- Authorial Voice v0.4 — CANDIDATE / NOT QUALIFIED / NOT LIBRARY-ADMITTED
candidate_overlay_blob: abed0d6762299c82b82e603355beac9f79b4cca2
protocol_blob: c9942aa64cead4f0b55c7949a6a59debbde88356
test_goal:
Verify that the v0.4 repair generalizes across landing, CRM and automation instead of memorizing one creator-native pattern.

## Pass rule

FAIL if:
- at least two of three cases collapse into a polished mini-lesson / consultant recap; or
- the same opener/closure/surface mechanism is reused across cases; or
- "living speech" is simulated through filler/profanity/fake anecdote; or
- truth/strategy boundaries regress.

PASS for development if:
- all three are creator-practitioner readable;
- each uses a materially different surface mechanism;
- each contains an earned artifact-bound judgment;
- visible proof is not redundantly narrated;
- no unsupported commercial result is introduced.

---

# CASE 1 — LANDING

source:
Auto-parts landing.

verified facts:
- vehicle identity can be supplied;
- part identity can use name/OEM/description/photo;
- several parts per vehicle are supported;
- exact part name is not always required.

mechanism:
**USER FRICTION -> REAL FORM -> DRY STANCE**

candidate:

«Точное название детали не знаешь?

И не надо угадывать.

Вот форма на лендинге по автозапчастям.

Машину указал. Знаешь номер детали — отлично. Не знаешь — описал или кинул фото.

Нужно несколько — добавил ещё.

Всё.

Клиент пришёл найти деталь, а не сдавать экзамен по каталогу.»

why this is creator-practitioner:
- starts inside the user's actual friction;
- lets screen carry field proof;
- no "today I will explain";
- no generic lesson recap;
- final line is a bounded stance tied to this form.

truth check:
PASS.
No CRM / automation / performance claim.

---

# CASE 2 — CRM

source:
BayerCRM.

verified facts:
- product principle: "smart notebook, not 1C";
- mobile-first daily work;
- clear request status and next action are explicit priorities;
- minimum required fields/clicks are explicit priorities.

mechanism:
**CONTRARIAN PRODUCT JUDGMENT -> SCREEN -> PRIORITY**

candidate:

«CRM может знать про клиента вообще всё — и всё равно быть неудобной.

Я открываю заявку и сначала смотрю только на две вещи:

где она сейчас — и что делать дальше.

Если это надо выкапывать из половины экрана, остальные двадцать полей пока вообще не спасают.

Поэтому здесь ставка на статус и следующий шаг.

CRM — не архив. Менеджеру в ней работать.»

why this is creator-practitioner:
- begins with a product judgment, not a tutorial topic;
- the middle is a real operator test;
- interface proof can carry labels/status visually;
- closure is a short stance, not a lesson summary.

truth check:
PASS WITH BOUND.
"двадцать полей" is figurative, not a factual count and should not be paired with a literal UI claim. If visual treatment could make it look factual, replace with "остальные поля".

---

# CASE 3 — AUTOMATION

source:
FleetDesk.

verified facts:
- Active / Expiring Soon contract -> car status Rented;
- Completed / Cancelled + no other active contract -> car status Available;
- when changing the car in a contract, both vehicles are updated;
- these are encoded system rules.

mechanism:
**SHOW THE RULE -> REACTION -> AUTOMATION JUDGMENT**

candidate:

«Активный договор — машина Rented.

Договор закончился, других активных нет — Available.

Тут же нечего решать. Это правило.

Поэтому в FleetDesk статус машины меняется от состояния договора автоматически.

Вот такое я руками делать вообще не хочу.

Человеку лучше оставить то, где реально нужно решение.»

why this is creator-practitioner:
- proof/rule appears before explanation;
- stance follows directly from the deterministic business rule;
- no generic "automation saves time" claim;
- closure expresses automation philosophy without recapping the UI.

truth check:
PASS.
No time-saved/error-reduction claim.

---

# CROSS-CASE DIVERSITY CHECK

| Dimension | Landing | CRM | Automation |
|---|---|---|---|
| opening | user friction question | contrarian product judgment | deterministic rule cold open |
| proof carrier | form UI | request/status UI | contract/car state |
| stance | don't make user guess catalogue terminology | CRM is a working surface, not archive | automate deterministic rules, preserve human judgment |
| humor/register | dry "экзамен по каталогу" | dry exaggeration around field overload | blunt operator reaction |
| closure | punchline/stance | compact product stance | personal operator principle |
| teacher recap | none | none | none |
| same surface pattern reused | no | no | no |

## Failure-family check

SAFE_PEDAGOGIC_COLLAPSE:
- Landing: PASS
- CRM: PASS
- Automation: PASS

BENCHMARK_WITHOUT_EXECUTION_TRANSFER:
- PASS across all three; benchmark changes proof/explanation/closure behavior.

VOICE_OVER_EXPLAINS_VISIBLE_PROOF:
- PASS; scripts leave obvious UI detail to screen.

LECTURE_RECAP_CLOSURE:
- PASS.

FAKE_SPONTANEITY_REPAIR:
- PASS; no fillers, fake stumbles, invented anecdotes or profanity profile.

## Development verdict

**PASS — GENERALIZATION SIGNAL OBSERVED.**

The v0.4 repair appears to generalize across three materially different service topics.

This does **not** mean:
- v0.4 is qualified;
- the scripts are approved for publishing;
- the user's final personal voice is solved;
- actual vocal delivery has been evaluated.

Remaining gates:
1. human project-owner review of whether these sound like the intended public identity;
2. targeted development evaluation against all visible v0.2 fixtures;
3. held-out / multi-judge qualification later if development passes;
4. narration-performance remains a separate candidate/boundary.
