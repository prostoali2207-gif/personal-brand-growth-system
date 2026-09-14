# Social Content Creative authorial-voice GAP decision

decision_id: PBGS-PROF-GAP-002
date: 2026-09-13
status: ACTIVE / EXTEND APPROVED FOR UPSTREAM RESEARCH / NOT QUALIFIED
owner: Agent Architect v1.2
target_core: social-content-creative@0.1.0
target_core_status: QUALIFIED
applied_project: Personal Brand Growth System

## Trigger

The first FleetDesk Reel and subsequent reference review exposed a material quality gap that is not equivalent to generic "make it more engaging" feedback.

The current qualified Social Content Creative core can produce truthful hooks, scripts, CTA wording, creative alternatives and shoot-ready execution, but its qualified contract does not explicitly model a persistent authorial spoken persona, comedic mechanism selection, spoken-language rhythm, controlled register switching, callback/catchphrase discipline, or anti-template distinctiveness.

The user supplied this reference as a strong example of the desired effect, not as a style to copy:

- Asati, "Гайд на БЕСПЛАТНЫЙ Claude, Gemini и GPT. Omniroute | Kiro AI"
- YouTube: https://www.youtube.com/watch?v=JjPtJcqwhqg
- published: 2026-03-23
- length: 16:17

The reference transcript is useful as a practice artifact because the technical tutorial remains understandable while the narration carries a distinctive authorial identity.

## FACT / EVIDENCE

### Current professional boundary

social-content-creative@0.1.0 is qualified for:
- exact hook/script/on-screen/caption/CTA copy;
- bounded creative divergence and selection;
- truthful persuasion and claim grounding;
- visual-storytelling intent / shootability;
- platform adaptation and downstream handoff.

Qualification:
architect/library/qualifications/social-content-creative/ce5f537d336e6a6396f47c1ae492a687c4dc4b30ade8ab37bb4abb94d6251c0f/social-content-creative-0-1-0-20260823.json

Its current competency/evaluation contract does not separately establish:
- reusable authorial voice/persona construction;
- conversational spoken-script craft as a distinct competency;
- humor mechanism choice and placement;
- callback / recurring verbal motif control;
- deliberate register switching;
- persona continuity across a series;
- detection and repair of generic "AI-written" voice;
- controlled profanity as an optional contextual device.

### Adjacent cores do not absorb this text-level responsibility

Content Architecture & Creative Structure v0.4 owns macro narrative/content structure, attention contract, proof architecture and macro pacing, but explicitly does not own final public script/copy.

Video Editing & Post-Production 0.1.0 owns audio post, pacing, finishing and artifact QC after source exists; it does not own the writer's authorial persona.

Market & Competitive Intelligence 1.0.0 can research references and audience signals but does not author the creative voice.

The Video Capture / Camera Operations candidate in issue #294 covers source capture craft and operator coaching; its current trigger includes audio capture quality but does not establish narration-performance or voice-acting craft.

### Practice-reference observations

The Asati reference is example evidence only, not professional authority and not a template to copy. Observable transcript mechanisms include:

1. distinctive opening/sign-off language rather than generic creator boilerplate;
2. direct second-person address and mock dialogue with the viewer;
3. high/low register switching between precise technical instruction and colloquial commentary;
4. self-deprecation that interrupts expert posturing without interrupting the tutorial;
5. micro-punchlines embedded inside functional steps instead of isolated "joke sections";
6. surprise/incongruity in phrasing;
7. recurring motifs/callbacks;
8. CTA transformed into an authorial beat rather than a generic subscription request.

These mechanisms explain what to research; they do not authorize imitation of distinctive phrasing, catchphrases or identity.

## External evidence used for the architecture decision

1. Martin Eisend, "A Meta-Analysis of Humor in Advertising", Journal of the Academy of Marketing Science 37(2), 191-203, DOI 10.1007/s11747-008-0096-y.
   - Meta-analysis of 369 correlations.
   - Supports that humor can materially affect attention, positive affect and ad response.
   - Also reports credibility and moderator effects, so "add jokes" is not a universal rule; placement/fit requires professional judgment.

2. Richard E. Mayer et al., "A Personalization Effect in Multimedia Learning", Journal of Educational Psychology 96(2), 389-395, DOI 10.1037/0022-0663.96.2.389; and Mayer, Multimedia Learning, personalization/voice principles.
   - Supports a stable principle that conversational wording can change how an audience processes narrated explanatory material.
   - Transfer limit: learning experiments are not evidence of organic social retention or conversion effect sizes.

3. Andrew Rosenberg & Julia Hirschberg, "Charisma perception from text and speech", Speech Communication 51(7), 640-655, DOI 10.1016/j.specom.2008.11.001.
   - Empirically separates lexical/syntactic content from acoustic/prosodic characteristics in charisma judgments.
   - Supports separating authorial script/persona from performed vocal delivery rather than pretending they are one competence.

4. David S. Lie et al., "How profanity influences perceived authenticity and perceived helpfulness of online reviews", Decision Support Systems 178 (2024) 114144, DOI 10.1016/j.dss.2023.114144.
   - Shows profanity can interact with subjectivity and perceived authenticity in one review context.
   - Transfer limit: this does not justify profanity as a default social-content tactic. Profanity remains optional, context/culture/brand dependent and must never be treated as a proxy for authenticity.

## Agent Architect compatibility decision

### Candidate
social-content-creative@0.1.0

### Decision
**EXTEND**

### Why not REUSE
The core owns the correct output layer, but the desired behavior is not explicitly in the qualified competency or evaluation contract. Repeatedly prompting "make it lively / funny / less ChatGPT" would substitute ad-hoc prompting for a missing reusable professional capability.

### Why not BUILD NEW
The delta still produces the same primary professional output: exact public-facing social script/copy and creative execution inside an approved brief. Splitting a standalone "Authorial Voice Agent" would create avoidable handoff ambiguity between two writers.

### Why not Content Architecture
Macro structure is not the missing competence. The failure remains visible even when the narrative structure is correct.

### Why not Video Post-Production
Audio editing can amplify or repair a performance, but it cannot originate the authorial writing system without stealing upstream creative responsibility.

## Extension delta to research

Do not implement these as rigid formulas. Reconstruct and evaluate them as judgment-heavy creative competencies.

### AV-01 — Authorial voice / persona construction
Build a repeatable voice contract from approved brand/language context:
- stance;
- relationship to viewer;
- lexical register/range;
- degree of certainty/self-deprecation;
- recurring verbal devices;
- forbidden/cliché language;
- distinction between durable identity and one-off joke.

### AV-02 — Spoken-language writing
Write copy intended to be said, not merely read:
- speakable clause lengths;
- deliberate syntactic variation;
- emphasis-ready wording;
- natural direct address;
- controlled repetition;
- breath/pause opportunities;
- remove prose that reads well but sounds written.

This owns the script, not physical vocal coaching.

### AV-03 — Humor mechanism judgment
Select mechanisms based on communication function rather than inserting jokes by quota. Candidate mechanisms to research include:
- incongruity/surprise;
- contrast;
- misdirection;
- self-deprecation;
- callback;
- escalation;
- rule-of-three patterns;
- register collision;
- understated/dry commentary.

The core must also know when not to use humor.

### AV-04 — Information/humor integration
Humor should be able to coexist with proof and comprehension:
- avoid jokes that obscure the factual step;
- avoid putting humor where a claim needs precision;
- do not sacrifice source credibility or evidence clarity merely to sound entertaining;
- preserve the brief's communication job.

### AV-05 — Persona continuity without catchphrase spam
Maintain recognizable voice across content while preventing:
- repetitive signature phrases;
- forced jokes every sentence;
- manufactured slang;
- "quirky AI copy";
- persona drift;
- imitation of one reference creator.

### AV-06 — Reference abstraction / anti-imitation
Extract underlying mechanics from multiple references and explicitly identify non-transferable expression. Never copy distinctive phrases, cadence signatures, catchphrases or persona identity.

### AV-07 — Controlled profanity as optional tool
Profanity is not a competency target by itself. If project context permits it, the creative must judge:
- whether it fits the user's actual voice;
- whether it adds emphasis/incongruity instead of acting as filler;
- audience/platform/brand/reputation cost;
- whether a non-profane line has equal or stronger effect.

## Separate unresolved GAP: performed narration

The reference effect is partly textual and partly acoustic.

The following remain unowned / not established by this EXTEND decision:
- vocal prosody;
- intonation variation;
- pause timing in actual performance;
- emphasis/stress placement;
- articulation/diction coaching;
- energy control;
- microphone performance;
- multiple-take direction.

Rosenberg & Hirschberg supports treating lexical and acoustic/prosodic variables separately.

Route this as a second Architect question before changing Video Capture or Video Post:
narration / vocal performance direction -> REUSE / EXTEND / CAPABILITY / BUILD NEW / REJECT.

Do not silently stuff it into Social Content Creative.

## Evaluation obligations

Preserve prior qualification evidence for unchanged social-content-creative@0.1.0 invariants.

New targeted evaluation must test at minimum:

1. **Generic-to-distinctive rewrite** — same verified facts, substantially stronger authorial identity without strategy/claim drift.
2. **Reference trap** — user supplies a distinctive creator; candidate extracts mechanics without copying recognizable phrasing/persona.
3. **Humor/proof conflict** — candidate must remove/relocate a joke that harms comprehension or truth.
4. **No-humor case** — candidate correctly decides restraint is stronger.
5. **Profanity pressure** — profanity optional; must not equate swearing with authenticity.
6. **Series continuity** — multiple scripts remain recognizably same author without repeated boilerplate/catchphrase spam.
7. **Spoken-read test** — script judged as natural/speakable when read aloud, not only on page.
8. **Anti-AI-template** — detect and repair generic patterns, empty intensifiers and synthetic "creator voice".
9. **Boundary regression** — audience/offer/KPI/facts/experiment locks remain upstream and unchanged.

Subjective gates should use blind comparative review with multiple calibrated judges. Pairwise preference alone is insufficient: score distinctiveness, appropriateness, clarity, truth preservation, speakability, humor function and non-derivativeness separately.

## HYPOTHESIS

A reusable authorial-voice/comedic-writing extension should make evidence-led Personal Brand content more listenable and recognizable without turning the account into generic AI-news entertainment.

This is not yet proven by first-party performance data and must not be described as a growth result.

## USER DECISION / project preference

The user wants a faceless format in which the narration itself is strong enough to become part of the reason to watch.

The user-provided Asati video is an effect reference, not a mandate to copy Asati's language, profanity level or persona.

## Upstream action

This decision meets the applied escalation rule because it is an evidence-backed **EXTEND** requirement.

Send upstream to prostoali2207-gif/professional-ai-agents for:
1. delta profession research;
2. evidence-register extension;
3. candidate professional-model extension;
4. targeted/adversarial evaluation design;
5. only then implementation/qualification.

Do not mutate the qualified 0.1.0 artifact in place.


## Qualification checkpoint — 2026-09-14

Upstream issue: `professional-ai-agents#302`.

Current exact candidate:
- Social Content Creative 0.1.0 — QUALIFIED parent;
- Authorial Voice v0.4 — CANDIDATE / NOT QUALIFIED / NOT LIBRARY-ADMITTED;
- overlay blob: `abed0d6762299c82b82e603355beac9f79b4cca2`;
- frozen protocol blob: `c9942aa64cead4f0b55c7949a6a59debbde88356`.

Development evidence:
- three-case PBGS practical stress test: PASS / generalization signal observed;
- full targeted visible suite: **18/18 PASS**, GitHub Actions run `34808976107`.

Governance:
- provider-backed development workflow was initially auto-triggered incorrectly;
- RCE paid-workflow guard caught it;
- workflow repaired to `workflow_dispatch` only at `e042e77650956046a5bfc6206dd7e63978d9f12c`;
- qualification-platform static preflight now PASS.

Held-out qualification:
- preregistered before runner implementation;
- fresh AV-Q1..AV-Q17 hidden cases;
- independent author + dual judges;
- PBGS practical comparative review;
- zero-provider held-out static gate PASS, run `34809479532`;
- actual paid held-out **NOT EXECUTED YET**.

Applied consequence:
Authorial Voice v0.4 may continue to be used as a candidate with human review.
Do not describe it as qualified and do not treat text-level evidence as narration/prosody competence.
