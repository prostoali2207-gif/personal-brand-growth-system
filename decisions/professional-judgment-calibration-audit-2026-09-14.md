# Professional Judgment Calibration — PBGS audit checkpoint

date: 2026-09-14
status: ACTIVE / DEVELOPMENT EVIDENCE
upstream_issues:
- professional-ai-agents#307 — professional independence from user assumptions
- professional-ai-agents#308 — earned boldness, depth and decisiveness

## Production diagnosis

Two distinct defects were observed:
1. user input could receive too much evidential/professional authority;
2. valid safety/truth controls could dominate selection and produce cautious, generic or overly explained output.

## Existing upstream capability reused

No new core was required.

Reused:
- `docs/runtime-judgment-and-opportunity.md`;
- `architect/methodology/creative-profession-architecture.md`;
- existing Agent Architect judgment-independence evaluation design.

## Applied repair

PBGS AGENTS now requires:
- user-input authority classification;
- semantic firewall for user feedback;
- judgment calibration before material recommendations;
- evidence-calibrated convergence;
- objection materiality;
- anti-option-dump behavior;
- unknown-unknown check;
- creative anti-safe-median/depth gate.

Applied wiring commit:
`f7266f6711a2862d933f88651347f75113b8c77c`.

## Audit evidence

Professional repo branch:
`research/pbgs-cross-core-judgment-audit-307-308`.

Stage A:
production/static audit completed; robust cross-core independence/boldness NOT established.

Stage B:
8/8 visible development cases passed after runtime wiring; no critical flags.

Limits:
- visible fixtures;
- self-scored development run;
- no independent held-out judge;
- no stochastic reliability claim.

## Localized owner-specific tracks still open

- Content Architecture #306 — internal constraint/public message surface;
- Social Content Creative Authorial Voice #302 — creator-native vs safe pedagogic collapse.

## Production rule

Do not describe #307/#308 as solved or qualified.
Launch-level artifacts still require human review.
Use development outputs to test the repair, not as proof of independent professional reliability.