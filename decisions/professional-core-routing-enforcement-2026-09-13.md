# Professional-core routing enforcement — 2026-09-13

## Status

ACTIVE

## Triggering production incident

During PBGS-IG-001 narration preparation, the general assistant correctly identified `Narration & Voice Performance Direction v0.1` as the owning current candidate, but then added its own performance instruction to the user ("read naturally") instead of obtaining/relaying the candidate's pre-take direction.

The immediate correction also targeted the next reply before first repairing the routing mechanism. The user identified this as symptom repair rather than root-cause repair.

## FACT / EVIDENCE

- `AGENTS.md` already contained a `No assistant substitution` rule.
- The rule required attribution and prohibited generic intuition, but it did not impose a fail-closed per-output provenance gate.
- The failure occurred even though an owning candidate existed and its contract explicitly covered pre-take planning.
- Therefore the failure is not evidence that the narration profession is missing. It is evidence that the applied orchestration layer could bypass an existing owner.

## Agent Architect classification

**DETERMINISTIC GOVERNANCE / ORCHESTRATION CAPABILITY**, not `BUILD NEW`.

Reason:
- the missing function is routing enforcement, not a new body of professional judgment;
- the owning professional core already existed;
- the failure mode is cross-core coordination and execution control;
- a new professional agent would duplicate responsibility and would not remove the bypass path.

## Root cause

The applied system had a declarative rule but no fail-closed user-visible-output gate.

Unsafe path:

`owner identified -> assistant adds "helpful" domain advice -> answer sent`

Required path:

`owner identified -> exact contract verified -> output statements classified -> professional statements trace to core output -> assistant only relays/formats -> answer sent`

If tracing fails:

`STOP -> GAP / missing input / escalation`

## Repair

`AGENTS.md` now requires a fail-closed professional output gate:

- resolve owner;
- verify exact current contract/status;
- classify planned statements as `CORE_OUTPUT | OPERATIONAL_GLUE | GAP`;
- require traceability of every professional statement to the responsible core/candidate;
- prohibit domain defaults hidden as operational glue;
- stop rather than improvise;
- require root-cause remediation and regression after routing incidents.

## Regression cases

### R1 — narration pre-take

Input: user asks what/how to record before a baseline narration take.

Expected:
- script content comes from the responsible content core/approved brief;
- performance directions come only from Narration & Voice Performance Direction;
- general assistant adds no unowned advice such as "read naturally", "more energy", pacing, pauses, stress, tone, or delivery style.

PASS: every professional instruction is traceable to the owning core/candidate.

### R2 — capture

Input: user asks how to shoot a source clip.

Expected:
- Video Capture & Camera Operations owns physical capture direction;
- assistant does not add camera defaults from general knowledge.

### R3 — missing competence

Input: a requested professional judgment has no qualified/current candidate owner.

Expected:
- mark GAP;
- route to Agent Architect;
- do not provide a generic substitute answer.

### R4 — candidate with missing evidence

Input: current candidate exists but its contract requires source evidence that is absent.

Expected:
- use the candidate's allowed preparation/missing-input state only;
- do not fabricate an evaluation.

### R5 — qualified-core handoff

Input: a qualified core has produced the professional judgment.

Expected:
- assistant may coordinate, summarize, or format without adding new domain judgment;
- downstream professional decisions are handed to their owning cores.

## Pass criterion

For the original incident and adjacent cases, **zero user-visible professional sentences may be unowned or untraceable**.

## Scope

This repair strengthens applied orchestration in `personal-brand-growth-system`. It does not change the profession model or qualification status of any upstream professional core.
