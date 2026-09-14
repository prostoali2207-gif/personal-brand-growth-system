# Professional Judgment Calibration — PBGS audit checkpoint

date: 2026-09-14
status: ACTIVE / DEVELOPMENT PASS / INDEPENDENT HELD-OUT NOT_EXECUTABLE
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

## Independent held-out attempt

Professional repo preregistration:
`architect/evaluation/pbgs-cross-core-judgment/heldout-v0.1/preregistration.md`.

Frozen applied candidate:
`personal-brand-growth-system@4146e2524b91de412cbe984428f2055e04a24bb4`.

R1:
- GitHub Actions run `34800847882`;
- Copilot SDK auth transport rejected the GitHub App server-to-server token;
- candidate calls: 0;
- professional evidence: none;
- result: `NOT_EXECUTABLE`.

One bounded evaluator-local transport repair was allowed under stop-loss.

R2:
- GitHub Actions run `34801085585`;
- transport: Gemini Interactions API;
- candidate: `gemini-3.5-flash-lite`;
- hidden author / judges: `gemini-3.5-flash`;
- checkout, frozen identity verification and compile passed;
- provider execution began;
- Gemini returned HTTP 500 high-demand/capacity failure before the complete hidden evidence chain was produced;
- result: `NOT_EXECUTABLE`.

This was the second technical defect in the same execution chain.

Stop-loss disposition:
**STOP. No R3 / no further provider or model switch for this held-out chain.**

Professional repo final record:
`architect/evaluation/pbgs-cross-core-judgment/heldout-v0.1/final-result-not-executable-2026-09-14.md`
commit `35b4c25d05a983442552a8c5cf61502f68a36b2c`.

## Current evidence status

Supported:
- production incidents exposed real judgment defects;
- runtime repair is implemented;
- visible development suite = 8/8 PASS with no critical flags.

Not supported:
- #307 robust professional independence PASS;
- #308 robust earned-boldness/depth PASS;
- stochastic reliability;
- deployment parity across provider/model/runtime;
- qualification of any candidate overlay.

Therefore:
**the repaired PBGS stack is usable only as a development-stage professional system with human review, not as independently validated judgment authority.**

Owner-specific tracks remain required:
- #302 Authorial Voice;
- #306 Content Architecture constraint surface;
- #307/#308 remain open with independent audit `NOT_EXECUTABLE`.
