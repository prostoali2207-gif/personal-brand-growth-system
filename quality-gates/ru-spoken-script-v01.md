# Russian spoken-copy quality gate v0.1

Date: 2026-10-26
Status: APPLIED PROJECT EDITORIAL GATE / EXPERIMENTAL, NOT QUALIFIED
Scope: Russian spoken Reels/Shorts scripts, captions, personal-brand public posts and approved copy drafts. Excludes quoted source material, code, documentation, structured transaction data, religious quotations and other material whose literal wording must be preserved.

## Ownership and classification
- Professional owner of exact social copy: Social Content Creative 0.1.0, QUALIFIED.
- Authorial Voice v0.4: CANDIDATE / NOT QUALIFIED as last recorded at `decisions/social-content-authorial-voice-gap-2026-09-13.md`; authorial voice / spoken-language craft is an Architect-classified **EXTEND** delta. Do not present it as qualified and do not overwrite the immutable parent model.
- Content Architecture v0.4: qualified/released for macro structure, not exact copy.
- Research provenance: Market & Competitive Intelligence 1.0.0 qualified.
- Mechanical editor: **DETERMINISTIC TOOL**, `scripts/check-ru-script-style.cjs`. Not a new agent or new profession; regex findings are candidate issues for human review, not proof of AI authorship.
- Applying this project-level quality gate does not resolve/qualify the upstream authorial-voice candidate.

## Trigger
Run before handing a public-facing Russian copy draft to the user, reviewer, video editing, approval or publication. Preserve user preference: plain, credible, articulate, natural spoken Russian. Avoid false sophistication. Business facts and user/project evidence remain the primary content.

## Gate A: mechanical block (project editorial preference)
- No Unicode em dash (U+2014) or en dash (U+2013) in final authored RU social/spoken text.
- Rewrite the sentence to express its meaning with natural punctuation, sentence breaks or a different clause. **Never blindly replace a grammatical dash with a hyphen**.
- This is Ali's authorial typography preference, not a universal rule of Russian grammar or an AI detector. Do not strip punctuation from exact source quotations, legal document data, code, or third-party artifacts.

## Gate B: reviewable signs
Flag these as review targets, not blanket language prohibitions:
- Formulaic antithesis: `не X, а Y`, `не просто X, а Y`, `не про X, а про Y`, `это не X. Это Y`.
- Unmotivated hype: `революционный`, `новый уровень`, `уникальный`, `бесшовный` without specific claim evidence.
- Presenter boilerplate: `важно отметить`, `давайте разберёмся`, `и вот почему`, `а теперь самое интересное`, `знакомо?`, `представьте себе` when a real fact or concrete action would do.
- Three consecutive micro-sentences, a mandatory triplet, or repetitive opening and closing frames if they are placeholders rather than task-specific communication.
- Meta-claims of value, theatrical curiosity, generic inspirational ending, unsupported before/after or audience pain, over-explaining an obvious screenshot.
- Identical sentence openings, syntactic rhythm, pseudo-conversational language, repeated catchphrases across a series.

These signals are correlated or perceived conventions in some datasets, mostly English. None alone proves AI authorship; transfer to Russian and to this creator is an applied hypothesis. Human work may correctly use a dash, triad or contrast. Apply the user's editorial preference without claiming universality.

## Gate C: editorial read-aloud
1. Does the opening identify the real subject, viewer problem or useful question? No fictitious crisis or mystery.
2. Are at least two substantive facts or actual decisions anchored to checked source evidence, when the piece's job is a real-case story? Avoid invented benefits and figures.
3. Can a Russian speaker say each line naturally, without sounding like a polished corporate statement or having to explain jargon?
4. Does a claim earn its place? Remove any line that just congratulates the project, names generic value or repeats the footage.
5. Does the audience understand what happened, why a specific choice was made and what can be verified? Narrative form is chosen for the material, not imposed as a template.
6. Avoid a compulsory moral/conclusion. Stop on the last meaningful fact when that is stronger.
7. Do not transfer quoted creator style or a single user's preferred variant into universal professional superiority.

## Execution and verification
1. Fact/evidence ledger and approved communication job -> draft.
2. Run `node scripts/check-ru-script-style.cjs --strict path/to/script.txt`; resolve all BLOCK findings and review warnings. For an intentional contrast, write a short justification in the review packet.
3. Read aloud and critique for filler, unnatural phrasing, informational density and actual speaking rhythm. Recheck after edits.
4. Record `mechanical=PASS`, `editorial=REVIEWED`, `facts=VERIFIED/PARTIAL`, `voice_extension=CANDIDATE`; don't call anything approved/published without human gate.
5. When testing variants, keep original A/B immutable, record a newly edited B2 outside the locked comparison, seek fresh evaluation. Single reviewer preference is not a public-performance result.
6. Don't let the mechanical check rewrite claims, context, legal terms, quotations or precise source data.

## Regression fixtures
- U+2014/U+2013 -> BLOCK.
- Syntactic `не X, а Y` and `не просто` -> REVIEW.
- `важно отметить`, `революционный`, `и знаете что?` -> REVIEW.
- Matter-of-fact narration and ordinary factual negative clauses -> PASS.
- CLI `--strict` exits nonzero for any finding; ordinary CLI reports warnings but only blocks dashes.
- Mandatory read-aloud review cannot be replaced by passing automated lint.

## Evidence classes and sources
**USER PREFERENCE**: 2026-10-26, Test 04 user preferred B as more solid; noticed long em dashes and negative parallelism as recurring ChatGPT signatures. Do not infer authorial performance uplift from taste feedback.

**QUANTITATIVE WEB EVIDENCE (ENGLISH)**:
- Pew Research Center, 2026-08-20: https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/ . English web-corpus increase in em dash usage and AI-associated vocab; no single feature proves authorship.
- Washington Post, 2025: https://www.washingtonpost.com/technology/interactive/2025/how-detect-chatgpt-em-dash/ . Observational analysis of shared ChatGPT chats and common format/contrast expressions.
- Cambridge University Press & Assessment, 2024-03-28: https://www.cambridge.org/gb/news-and-insights/does-chat-gpt-make-the-grade-cambridge-research . Small study highlights repetition, tautology and connector patterns.

**USER COMPLAINTS (ANECDOTAL / NOT POPULATION PREVALENCE)**:
- Reddit 2025-10-01: https://www.reddit.com/r/CasualConversation/comments/1nvgy2l/anyone_else_now_avoiding_emdashes_because_of_chat/ . Original discussion flags em dash and `not X, but Y`.
- Reddit 2025-06-16: https://www.reddit.com/r/ChatGPT/comments/1lczwg9/its_gotten_to_the_point_where_i_notice_chatgpts/ . One reader's perception of `that's not X, it's Y` in spoken videos.

**RUSSIAN LANGUAGE CONTEXT (EDITORIAL OBSERVATION)**:
- RBC Life, 2026-03-12: https://www.rbc.ru/life/news/69b261699a79471f525d3a96 . Interview points to templates, semantic repeats and overly polished prose; not a validated detector.

Evidence ceiling: these sources justify a cautious editorial review list; they cannot supply a verified detector of AI writing, universal disallowed grammar list, guaranteed engagement improvement or actual Russian conversion uplift.

## Original failure record
Test 04 A/B both used long punctuation dashes, and B text contained recurring explanatory staging. User's correction is a real style failure in the produced draft. Root layer is the applied editorial acceptance gate and unresolved spoken authorial-voice qualification, not video finishing. Repair includes deterministic lint, documented human gate and regression testing.
