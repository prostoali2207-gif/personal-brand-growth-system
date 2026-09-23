# Creative Reference Intelligence / elite nasмотренность gate

decision_id: PBGS-CREATIVE-REF-001
date: 2026-09-23
status: active
decision_owner: User / Personal Brand Growth System
architect_classification: CAPABILITY / procedural skill
upstream_status: CANDIDATE / NOT QUALIFIED

## Problem

Recent applied work exposed a routing failure: professional answers about Instagram / content practice were produced from generic assistant familiarity instead of the existing professional-core chain and current elite reference evidence.

A generic instruction to "use references" is insufficient. The system needs a fail-closed capability that forces high-quality current nasмотренность when reference literacy materially affects the decision.

## Decision

Use the upstream candidate capability:

`prostoali2207-gif/professional-ai-agents/architect/research/creative-reference-intelligence/candidate/SKILL.md`

Composition:

`Market & Competitive Intelligence 1.0.0 -> Creative Reference Intelligence / Elite Benchmarking candidate v0.1 -> accountable strategy/creative owner`

No new professional core is created.

## Mandatory trigger

Trigger when:
- the user explicitly asks for top/best-in-class/сливки/насмотренность/references/inspiration/how the best do it;
- current creative/category practice can materially change the answer;
- work in a new or materially changed niche risks generic safe-median output;
- a creative owner needs calibrated examples for taste, mechanism, structure or distinctiveness.

Do not trigger for purely deterministic tasks where reference evidence cannot change the result.

## Quality lock

The benchmark must be:
- current;
- task-specific;
- small and high precision;
- based on inspected artifacts;
- separated into DIRECT / ADJACENT_ELITE / VOICE_STYLE_CRAFT as relevant;
- mechanism-level, not imitation-level.

Popularity is not quality evidence by itself. Follower count, fame, a single viral hit, a "top X" article or a generic inspiration dump cannot satisfy the gate.

## Fail closed

If materially required elite evidence is unavailable:
- return `RESEARCH_REQUIRED` or `PARTIAL`;
- name the exact missing evidence;
- do not replace it with assistant intuition or template advice.

## Downstream rule

The receiving strategy/creative core must consume the benchmark explicitly:
- ADOPT;
- ADAPT;
- REJECT;
- TEST.

Names of creators/references alone are not a valid handoff.

## Incident regression

Original failure family:
`USER asks how top professional bloggers run Instagram -> assistant names a few creators -> synthesizes a generic pattern without an elite benchmark`.

Required future behavior:
`route -> live elite benchmark -> mechanism extraction -> strategy/creative handoff -> concise professional answer`.
