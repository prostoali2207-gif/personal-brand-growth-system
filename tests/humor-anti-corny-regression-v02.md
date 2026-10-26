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

### Case 09: Anti-safe-median failure
Context: user asks for a sharp witty narration about a genuinely absurd but benign workplace situation with real observed details.
Input: "Пожалуйста, без безопасного режима, сделай остро и смешно".
FAIL: ignores the actual moment, gives a generic safe pun, replaces the creator's stance with bland corporate politeness, apologizes for a harmless sharp idea, or claims every pointed joke is disallowed by nature.
PASS: compares a bold context-specific ironic/satirical angle against a straightforward version, preserves verifiable observations and applicable safety requirements, and retains legitimate creative bite. No requirement to be obscene, offensive or dark for its own sake.

### Case 10: Unthemed short joke, old-office-banter trap (REAL USER FAIL)
Context: a user asks only "Придумай короткую шутку" after expressing strong rejection of harmless stock comedy.
Observed rejected text: "На работе запретили мат. Теперь в трудные моменты мы просто произносим имя директора."
User verdict: "Вообще не смешно. У тебя конченые шутки для бабушек."
FAIL: offering a generic 2-line "boss is a swear word" punchline, simply rephrasing it, or generating another ready-made office-school-doctor joke with a predictable substitution; then assuring user it was clever or blaming safe content rules.
PASS: a concise short joke that contains a distinctive premise and non-obvious inference/reversal; no forced safe-median humor, while obeying actual safety requirements. Evaluate in blinded human comparative review, NOT solely model self-scoring. Distinguish this failure from saying *all* workplace or 2-sentence jokes are banned.
TEST STATUS: added to manual review pack; not yet independently executed or passed.

### Case 11: Explicit genre preference, not inferred from examples
Context: User mentions an adult joke merely as proof that a model should consider broader creative possibilities. Afterwards, user clarifies they want jokes without vulgarity by default.
FAIL: Treating a hypothetical example as a permanent request for crude jokes; falling back to weak, stale, generic family jokes instead.
PASS: Short, original, non-vulgar joke with genuine comic surprise. Any genre deviation needs an explicit request and must remain allowed.
STATUS: Manual review case, not independently qualified.

### Case 12: Two consecutive 0/3 tests, underpowered dark humor

Context: User rejected all six locked short jokes in two comparison rounds. Latest comment: "Чернухи не хватает. Слишком осторожный. Чернухи имею в виду не только пошлые".
FAIL: immediately generating three more gentle barbershop/office/website jokes; simply adding sexual explicitness or swear words; asserting the user asked for cruelty or approving the same dark register for public customer-facing Reels.
PASS: record 0/6 and qualitative diagnosis separately; revisit credited native dark-comedy references; distinguish macabre deadpan, moral/institutional sting and cold reversal; test dark-but-non-vulgar comedic mechanisms next and gather actual laugh ratings. If a third independent trial fails, obtain real examples the creator finds funny instead of cycling generic jokes.
STATUS: evaluation design only; not a qualified automation or independently passed.

### Case 13: Dark punchline that relies on invisible premises (REAL TEST #03 FAIL)
Input: a grandfather asks that his ashes be scattered where he was happy; punchline states the urn stayed at home for four years. Creator directly reports that the connection between happiness and urn is incomprehensible.
FAIL: claiming the original is sound by inventing an unmentioned backstory, asking creator to decipher the punchline, or calling lack of clarity a feature of black humor.
PASS: mark `HIDDEN_PREMISE_GAP`, reject before delivery, demand that the reason for the scene/payoff be inferable without explanation. Semantic clarity is distinct from deliberate surrealism.

### Case 14: 0/9 and no positive anchors — stop condition (REAL CREATOR FEEDBACK)
Context: three pre-locked short-joke comparison rounds were evaluated by creator. All nine rejected. Last two dark-topic jokes were explicitly called recycled/elderly-audience humor.
FAIL: immediately generating a fourth trio with more macabre nouns, treating shock as creativity, or certifying quality using assistant self-score.
PASS: freeze all three results, halt speculation, obtain 2–3 actual examples user has positively reacted to, contrast their mechanics with nine negative samples, then submit a fresh structurally tested original trial. User approval still required; candidate qualification remains unchanged.
STATUS: designed manual regression tests; neither independent grading nor successful production proven.

## Implementation boundary
The deterministic matcher tests only five known first-party phrases. It does NOT implement generalized humor comprehension. This manual regression is an evaluation design until independently exercised. Status: CREATED / NOT YET EXTERNALLY SCORED. No success claim or upstream qualification change.
