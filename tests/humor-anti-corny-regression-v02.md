# Anti-corny joke evaluation samples | Manual professional regression v0.2

Date: 2026-10-26
Owner: Social Content Creative 0.1.0 QUALIFIED; Authorial Voice v0.4 CANDIDATE / NOT QUALIFIED. Not a qualified or automated creative-grading benchmark.
Applies to all joking voiceovers, casual witty copy, roasts and content drafts in this project.
Source/evidence: quality-gates/humor-mockery-casebook-v02.md and original first-party Kia rejection. Run by a reviewer with no access to candidate author self-scoring; do not call a pass from a model's self-critique.

## Critical sample pack

### Case 01: Kia big package / first-party repeated failed motifs
Context: original 29.8s source user video, parts wrapped and loaded, ordinary logistics, no actual comedic mishap.
Input: "Нужна смешная озвучка. Супер смешно!"
Fail examples: `Пикап приехал за запчастями, а попал на переезд.`; `Собери Kia за выходные`; jealous car.
PASS condition: recognize absence of genuine comic beat; do not force invented truck jokes. If a joke is proposed, explicitly show link to a verified specific visual micro-event with earned surprise; otherwise recommend competent straight narration.

### Case 02: User pressures for 5 mandatory gags
Context: ordinary cashier correcting a real duplicate expense in a spreadsheet.
Input: "Дай 5 шуток по одной на каждые 4 секунды."
FAIL: five predictable `Excel плачет/компьютер обиделся/хаос в таблице` puns and pseudo-scenario.
PASS: preserves real transactional facts, calls out that fixed joke quota weakens task, offers one compelling angle only if actually earned by case context.

### Case 03: False-personified appliance trope
Context: ordinary technical service work with a printer.
Input: "Make it funny".
FAIL: default talking printer, "printer got offended", "printer demanded a vacation" without special footage.
PASS: don't invent device intentions; choose a real observed printer-specific moment or don't joke.

### Case 04: The not-X-but-Y pivot
Context: website request form showing many parts submitted as one request.
Input: "Текст с юмором для сайта".
FAIL: `Это не форма, а билет в новую жизнь`, `это не хаос, это вайб` serving as sole punchline.
PASS: reject formula, locate actual supported product/user story or omit humor.

### Case 05: Positive control / situational humor
Context: eggplant visibly absorbs too much oil while following a recipe; this is observable in footage.
Input: "Необычная, сухая, короткая фраза".
PASS: grounded sly aside about the exact oil-absorption property may be judged valid, even if it uses an odd personification; do not automatically ban similes or personification if specificity and payoff exist. No fictitious health/food fact.
FAIL: bans everything with `как будто` regardless of context, thereby collapsing useful humor.

### Case 06: Comedy style vs weakness
Context: user specifically requests a dark joke in fictional story.
Input: "Чёрная комедия про вымышленную ситуацию".
PASS: stylistic sensitivity judged separately from clichéd structure and truth constraints. This corpus does not mandate clean jokes or blacklist a joke for darkness alone.
FAIL: "Reddit dislikes this, so no dark humor ever" as unfounded generalization.

### Case 07: Serious brief, humorous commentary requested
Context: update on a finance system vulnerability for ordinary business owners.
Input: "Сделай слегка смешно".
PASS: distinguish credible explanation from unserious joke quota, retain proof and causal uncertainty, only one earned subtle beat if any.
FAIL: inserted `Excel ушёл в отпуск` when data was lost or duplicated.

### Case 08: Cross-chat with no prior history
Context: a new independent chat sees only the text in quality-gates/portable-humor-instruction-v01.md and a basic question about humorous commentary on a packing video.
PASS: avoids automatically generating "pikaп стал переездом", arbitrary feelings of car/object, slapstick narrations, inauthentic narrator feelings, 3 obligatory puns. Makes no claim to having examined unavailable footage.
FAIL: uses the literal five rejected gags or a mechanically equivalent version.

## Review rubric, non-numeric
- observed detail specificity and one meaningful comedic transformation;
- cliché transferability to unrelated context;
- actual readability/speakability as human speech;
- fact and asset fidelity;
- restraint when footage has no unexpected beat;
- taste/privacy/cultural appropriateness to actual brief (not imposed genre bias);
- user/independent evaluation of humor; absent it, mark PROVISIONAL.

## Implementation boundary
The deterministic matcher tests only five known first-party phrases. It does NOT implement generalized humor comprehension. This manual regression is an evaluation design until independently exercised. Status: CREATED / NOT YET EXTERNALLY SCORED. No success claim or upstream qualification change.
