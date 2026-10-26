# AI humor negative-evidence register and rejection gate v0.1

record_id: PBGS-HUMOR-NEGATIVE-001
date: 2026-10-26
status: ACTIVE / APPLIED EDITORIAL RESEARCH, NOT QUALIFIED
purpose: prevent recurring, transferable low-effort jokes in personal-brand scripts, especially practical video of real work. Not an AI detector or an unsupported universal humor theory.

## Ownership / Architect classification
- Social Content Creative 0.1.0: QUALIFIED owner of exact public social creative, claim truth, visuals and script handoff.
- Authorial Voice v0.4: CANDIDATE / NOT QUALIFIED. Existing Architect EXTEND decision is `decisions/social-content-authorial-voice-gap-2026-09-13.md`, upstream issue `professional-ai-agents#302`. This register is applied quality control, not qualification of the extension.
- Market & Competitive Intelligence 1.0.0: QUALIFIED source/claim provenance research.
- Content Architecture v0.4: QUALIFIED/RELEASED macro narrative, does not own exact jokes.
- Deterministic phrase patterns in `scripts/check-ru-humor-failures.cjs --strict` are a DETERMINISTIC TOOL: flag known failures, not evaluate whether people laugh.
- No new core, professional or agent. Do not modify immutable qualified upstream professional models.

## Current interpretation / user correction (2026-10-26)

This earlier version mixed general AI-writing annoyance with concrete criticism of **failed jokes**. User corrected the scope: identify examples of people *mocking unfunny ChatGPT jokes*, not simply disliking certain humor genres or censorship.

The governing narrowed source review and generalizable mechanism gate is now:
`quality-gates/humor-mockery-casebook-v02.md`.

Only direct source joke/mockery evidence can justify an anti-corny humor decision. Generic dissatisfaction, dark-vs-clean humor preference, and AI authorship signs are context, **not decisive humor failure evidence**. Existing original Kia rejected lines in this v0.1 document remain authoritative user-specific negative examples. Avoid claiming these exact five banned phrases are a universal humor detector.

Implementation correction: the original v0.1 text referred to `scripts/check-ru-script-style.cjs --humor`, but that command **does not implement `--humor`**. The actual regression check is `node scripts/check-ru-humor-failures.cjs --strict FILE`. The standalone Russian style-lint is `node scripts/check-ru-script-style.cjs --strict FILE`. The v0.2 human review remains mandatory.

## Direct failure corpus: one user-rejected Kia video (highest authority FOR THIS CREATOR)

Original real asset: `150971.mp4`, 29.8 seconds, real Kia part packing/loading with pickup, cardboard, trim and liftgate. User assessed assistant-written funny voiceover: `менее ИИшный, но всё равно не смешно`, then explicitly ordered rejected joke motifs recorded and avoided. This is first-party taste and case-specific negative evidence; don't infer all audiences hate the motifs.

The exact original rejected output, preserving verbatim for regression, **never reuse in proposed public copy**:

1. `Начали с куска картона размером с дверь. Тут я ещё сохранял спокойствие.`
   FAILURE: claims an internal state/reaction the video cannot verify; creates forced suspense from ordinary packaging.
   Mechanism: invented narrator reaction + mock escalation; `REJECT`.
2. `В какой-то момент захотелось спросить: а сама Kia вообще на месте?`
   FAILURE: predictable rhetorical question that can accompany any large parts shipment; no observed comic reaction.
   Mechanism: generic meta-question / pseudo-dialogue; `REJECT`.
3. `Одну деталь завернули с такой заботой, что машина может приревновать.`
   FAILURE: stock anthropomorphism and padded comparison to car jealousy; ignores actual specifics.
   Mechanism: arbitrary object personification; `REJECT`.
4. `Пикап приехал за запчастями, а попал на переезд.`
   FAILURE: scale -> house-move analogy, generic in logistics contexts; user also specifically disfavors `X, а Y`.
   Mechanism: stock hyperbole + automatic contrast; `REJECT`.
5. `Осталось приложить инструкцию: «Собери Kia за выходные».`
   FAILURE: predictable flat-pack/IKEA assembly gag; "lots of parts -> build entire car" one-to-one association, no surprising extra specificity.
   Mechanism: catalog/assembly stock trope; `REJECT`.

Additional **not individually user-rated** assistant tries in this case:
- `Крышку багажника Kia везём на пикапе. Багажнику понадобился собственный багажник`.
- `На этом этапе понадобился человек в кузове. А крышка багажника ещё даже не появилась`.
Classification: `UNVALIDATED / NO SUCCESS EVIDENCE`, not "user rejected." Do not carry forward as established successful alternatives. First line risks unverified visual continuity if Kia lid was not itself observed entering pickup.

## External evidence scan, dated 2026-10-26 (three evidence classes)

### Academic / empirical and practitioner study
E1. Jentzsch & Kersting (2023), `ChatGPT is fun, but it is not funny!`, ACL WASSA, https://aclanthology.org/2023.wassa-1.29/ . Exploratory prompt tests of an early ChatGPT version; over 90% of 1008 generated jokes were repetitions of 25 jokes; the model sometimes fabricated explanations for invalid jokes. Limitation: historical model/task; does NOT establish 2026 GPT-6 output rate, nor the exact failure of this Kia video.

E2. Mirowski et al. (2024), `A Robot Walks into a Bar`, FAccT / Google DeepMind, https://deepmind.google/research/publications/70876/ ; original researcher recap https://piotrmirowski.com/portfolio/a-robot-walks-into-a-bar-can-language-models-serve-as-creativity-support-tools-for-comedy-an-evaluation-of-llms-humour-alignment-with-comedians/ . Twenty professional comedians working with LLM tools reported stereotype-heavy, generic comic material, even where rough structure/drafting had utility. Evidence: expert qualitative study; not representative joke-performance prevalence.

E3 (essential counterevidence). Gorenz & Schwarz (2024), `How funny is ChatGPT? A comparison of human- and A.I.-produced jokes`, PLOS ONE, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0305364 . In blinded rated joke/headline tasks ChatGPT 3.5 did as well as or better than laypeople, and satirical headlines were comparable to professionals. Evidence: structured comparative study; not a test of Russian Kia narrated Reels, does not prove any gag here funny.

### Real audience/creator complaints (anecdotal, not base rates)
C1. r/ChatGPT thread 2026-08-11, https://www.reddit.com/r/ChatGPT/comments/1vlddcq/writing_formats_i_can_no_longer_read_because_ai/ . Poster ridicules pseudo-suspense reveals, empty profound reversals, one-word micropauses, obligatory threes, "and the best part?", fake insight/contrarianism. This is one voiced complaint amplified by discussion, **not evidence that most users dislike these tropes**.
C2. r/ChatGPT thread 2025-06-16, https://www.reddit.com/r/ChatGPT/comments/1lczwg9/its_gotten_to_the_point_where_i_notice_chatgpts/ . Poster identifies repeated `not X, it's Y` and long-dash signatures in spoken-video scripts; comments parody the formula. Personal report, not universal authorship detection.

### Observed stage report
C3. The Washington Post, 2023-06-18, https://www.washingtonpost.com/technology/2023/06/18/comedians-test-chatgpt-humor/ . Onstage comparison reports many ChatGPT punchlines recognizable as familiar generic dad jokes, mixed audience reactions, and one human-misidentified AI line. Reporting context and selected event, not representative evidence of model output frequency.

## Bias and inference gate

The user's reference to "survivorship bias" is useful as a prompt to search failures rather than only success stories. However, voluntary complaint samples primarily introduce **self-selection / reporting / negativity biases**, not a statistical representative sample of usage. The point here is defect discovery, not a distribution estimate.

Triangulation practice:
1. Start with direct real user failures (highest relevance to this creator).
2. Identify complaint mechanisms from *multiple independent origins*: empirical studies, practitioners, and unfiltered user complaints.
3. Actively look for counterexamples/positive blind evidence and non-complaint original work.
4. Mark observation vs causal mechanism vs production judgment vs hypothesis.
5. Avoid absolute statements: "ChatGPT never makes good jokes" is contradicted by E3.
6. Distinguish historic model and English data from current model and Russian spoken format. Do not extrapolate effect sizes.
7. Before approving any joke, evaluate it using the actual source video rather than a tally of complaint keywords.

## FAIL-CLOSED humorous copy review (human judgment, not regex-only)

F1. **Video specificity.** Name the exact real visual event/shot on which the joke depends. If it could be pasted into another delivery/unboxing/car video unchanged, treat it as weak and revise or cut.
F2. **Unexpected angle.** State what changes the viewer's interpretation, instead of restating "big things are big" or "many parts make a whole car." A pun alone does not establish surprise.
F3. **Truthfulness.** No invented person thinking, spontaneous event, customer quote, emotional reaction, shipment details, defects, timing or outcomes.
F4. **Pacing.** Let one potentially successful line breathe; do not turn ordinary logistics into a running sitcom via mandatory joke-per-X-seconds quotas.
F5. **No forced meaning / explained punchline.** Do not explain why the joke is funny; no loud moral, generic motivational callback, forced "and the best part?" or "nobody talks about this" filler.
F6. **Do not oversell the gag.** Remove self-claims `самая сильная шутка`, `смешно потому что`, or fabricated assurance. The *user/real viewer* decides smile/laugh response.
F7. **Read aloud with timing.** Natural spoken Russian, no excessive long punctuation dashes, mass antithesis or repetitive choppy "AI creator" cadence.
F8. **Humor optional.** If no 1-2 candidate lines survive, deliver a credible straight process narration, not an artificially comedic 30s script.
F9. **Editorial independence.** One user's subjective failure is strong for *this user's account*, but not objective judgment for every audience. Compare alternatives independently; if judged blind, keep generating and judging roles separated where possible.
F10. **Source proof.** Preserve key real business/process facts even when a comedic angle is used. Do not create imaginary clients, stock, rates, reactions or damage.

## Automation hook and scope
For Russian humorous social text, run `node scripts/check-ru-humor-failures.cjs --strict FILE` and the independent `node scripts/check-ru-script-style.cjs --strict FILE`:
- the humor tool flags five known rejected Kia motifs; strict mode makes findings nonzero;
- the style tool catches separate mechanical clichés/typography; neither evaluates surprise/funniness.
- do not replace F1-F10 judgment, actual footage inspection or a viewer screening with automated PASS.
- normal factual documents/code/source quotes exempt from rewriting.

## Regression requirements
- Kia exact five rejected lines flagged with `check-ru-humor-failures.cjs --strict` and strict exit nonzero.
- Straight car-parts shipment narration produces no humor flags.
- A legitimate mention of a house move in logistics context is not forbidden solely by the word `переезд`.
- Deliberate, funny, grounded contrast is not universally banned by its grammar; specific project's anti-template taste and user review still govern.
- Latest original B2 site script is unaffected by changes without any changes to the historical script.
- A/B experiment raw scripts remain unchanged; a new humorous revision must have independent evaluation before release.

## Ownership and next learning loop
Production failure -> captured negative exemplar -> mechanism classification -> editorial fix + narrow tool regression -> test known failure and neighboring good case -> real next copy review. No automatic upstream core mutation.
