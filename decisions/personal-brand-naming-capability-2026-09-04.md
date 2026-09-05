# Personal Brand Naming / Verbal Identity capability — applied decision

decision_id: PBGS-NAMING-001
date: 2026-09-04
status: active
owner: User / Personal Brand Growth System
architect_classification: CAPABILITY
upstream_action: BUILD NEW COMPLETED AS CANDIDATE / NOT QUALIFIED

## Target job

Select and govern a durable public personal-brand name/handle (initially Instagram `@username`) without inventing expertise, positioning, achievements or commercial claims.

This is not a new professional core and not a visual-identity task.

## Agent Architect classification

Primary: **CAPABILITY — Naming / Verbal Identity**.

Composition:
- Personal Brand Strategy / Positioning specialization -> supplies brand identity, audience/market role and long-horizon constraints.
- Market & Competitive Intelligence -> supplies current competitor/category naming evidence and collision context.
- Naming / Verbal Identity capability -> owns naming territories, candidate generation, linguistic/semantic judgment, distinctiveness, memorability, accessibility, longevity and shortlist rationale.
- Deterministic/platform checks -> exact syntax, handle/domain availability checks and exact-string collision checks.
- Legal/trademark specialist -> owns formal clearance when commercial protection matters.
- Visual/Brand Identity -> consumes the selected name; it does not own naming merely because it designs the wordmark/logo.

## Reuse decisions

### Spline Brand Identity Agent
**REJECT as naming owner.**

Reason:
- project-specific to Spline;
- current contract explicitly treats `Spline` as already selected and says not to reopen naming;
- owns visual positioning, logo/wordmark, typography/color and identity system;
- no transferable qualification evidence for personal-brand naming.

Useful retained precedent only:
- evidence-first decisions;
- distinctiveness/similarity caution;
- stress-test the selected identity in real channels.

### Market & Competitive Intelligence 1.0.0
**REUSE for research inputs only.**

It may establish current market/competitor evidence and bounded implications. It does not own the final naming decision.

### Growth Strategy & Experiment Portfolio v0.1
**REUSE candidate input boundary only; NOT QUALIFIED.**

Its current frozen candidate contract can supply downstream strategic constraints when applicable, but it does not currently encode naming craft.

### Social Content Creative 0.1.0
**REJECT as naming owner; REUSE as optional creative challenger.**

Its qualified boundary includes materially distinct creative divergence, but naming ownership remains with Brand Naming Practitioner. Use it only when separation of divergence and convergence adds value. Its qualification does not transfer to naming craft.

## Applied naming principles

Use these as professional decision criteria, not as a mechanical score that replaces judgment:

1. **Brand fit** — candidate must fit the approved personal-brand positioning/identity.
2. **Distinctiveness** — avoid generic category labels and confusingly similar names.
3. **Memorability** — favor structures that can be recalled and repeated accurately.
4. **Accessibility** — easy to pronounce, hear, type and spell for the intended audience/languages.
5. **Longevity** — avoid unnecessary lock-in to one tool, trend, technology or narrow service if the personal brand is expected to broaden.
6. **Conciseness** — remove unnecessary words, punctuation and random numeric suffixes where possible.
7. **Semantic / linguistic safety** — inspect unintended meanings and cultural/language problems in relevant markets.
8. **Platform portability** — prefer a base handle that can survive different username character rules across important channels.
9. **Protectability / collision risk** — perform preliminary search/screening; formal trademark clearance remains legal work when required.
10. **Truth boundary** — a handle may not imply a verified role, expertise level, credential or achievement that the evidence/claim ledger does not support.

## Process

Current v0.2 candidate sequence:

`FRAME -> LOCK CRITERIA -> DIVERGE -> COUNTER-TERRITORY CHECK -> GENERATE -> SCREEN -> FIRST-READ + ORAL/TYPED TEST -> NATURALNESS/CONTRIVANCE CRITIQUE -> CONSISTENCY CHECK -> COMPARE -> HANDOFF`

Do not converge on the first plausible handle or silently turn a user-suggested territory into the whole search space.

## Current factual blockers

- Applied `brand-claims/` contains no approved public identity/capability claims yet.
- The current applied repo has no approved final Personal Brand Positioning decision.
- Channel inventory currently contains the schema but no verified Instagram handle/account record.
- Therefore a profession-grade **final** handle cannot yet be asserted from the repo as a completed naming decision.

## Current personal-brand naming mode

Do **not** impose a name-led identity or require `Ali` in the handle.

The current Brand Naming Practitioner v0.2 candidate explicitly allows:
- name-led identity;
- person-alias identity;
- concept-led identity;
- open exploration across modes.

For personal-brand candidates, test the likely first-read identity type (person/alias vs role/title vs place/project/company), naturalness vs contrivance, oral-to-typed robustness, lowercase segmentation, polysemy, and context-sensitive collision relevance.

Historical hypotheses such as `alibuilds`, `builtbyali`, `prostoali`, `alioperator` and other prior shortlist items are decision history only unless explicitly reopened.

The current selected downstream identity state remains governed by `source-of-truth/current-brand-identity.md`.

## Evidence / methodology

Repository:
- `professional-ai-agents/architect/SKILL.md`
- `professional-ai-agents/architect/methodology/professional-core-reuse.md`
- `professional-ai-agents/architect/methodology/creative-profession-architecture.md`
- `professional-ai-agents/architect/evaluation/foundation-eval-plan.md`
- `auto-parts-landing/.agents/skills/brand-identity-agent/SKILL.md`
- `personal-brand-growth-system/decisions/professional-gap-classification-2026-09-04.md`

External professional references:
- Lexicon Branding, Brand Naming: 5 Step Process (updated 2026-03-25): https://www.lexiconbranding.com/brand-naming-process/
- Catchword, Just Name It / naming process: https://catchwordbranding.com/catchthis/just-name-it-catchwords-comprehensive-naming-guide/
- Catchword naming criteria: https://catchwordbranding.com/wp-content/uploads/2014/10/CW_NamingGuide_100914.pdf
- WIPO materials on personal-name distinctiveness and trademark identity: https://www.wipo.int/en/web/amc/processes/process2/report/html/report

## Upstream status

The original `NO SEND` reopen trigger was met by repeated materially different naming work (Spline/company-brand naming plus personal-brand/social-handle naming).

Agent Architect upstream decision remains:
- **BUILD NEW reusable capability package** `Brand Naming Practitioner`;
- not a new top-level professional core.

### Historical v0.1
- candidate: `v0.1.0-candidate`;
- status: **FROZEN / NOT QUALIFIED**;
- Stage A: `59/59 PASS`;
- independent qualification terminal state: **NOT_EXECUTABLE / STOP**;
- no professional PASS/REVISE/FAIL was established;
- authoritative terminal record:
  `professional-ai-agents/architect/evaluation/brand-naming-practitioner/terminal-record-v0.1-not-executable.json`;
- issue `#275`, terminal PR `#279`.

### Current operational candidate v0.2
Production naming failures from the 2026-09-04/05 applied work triggered an evidence-backed revision through Agent Architect.

- current candidate: **`v0.2.0-candidate`**;
- status: **CANDIDATE / NOT QUALIFIED**;
- issue: `professional-ai-agents#282`;
- implementation PR: `professional-ai-agents#283`;
- model:
  `professional-ai-agents/architect/evaluation/brand-naming-practitioner/v0.2/professional-model-candidate-v0.2.md`;
- skill:
  `professional-ai-agents/architect/evaluation/brand-naming-practitioner/v0.2/candidate/SKILL.md`;
- targeted development/regression families: 12;
- no fresh independent qualification PASS exists yet.

Current applied naming work should use **v0.2**, never present it as qualified, and preserve the v0.1 stop-loss history rather than treating v0.2 as a retry of the stopped v0.1 chain.
