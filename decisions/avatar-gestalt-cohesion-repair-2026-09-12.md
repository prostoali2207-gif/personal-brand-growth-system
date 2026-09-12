# Avatar gestalt-cohesion repair — 2026-09-12

decision_id: PBGS-AVATAR-GESTALT-P1-001
date: 2026-09-12
status: RENDER REVISE / NARROW P1
owner:
- Visual Design / Art Direction 0.3.0-candidate — CANDIDATE / NOT QUALIFIED
challenger:
- Social Content Creative 0.1.0 — qualified library artifact used for social/avatar-read stress test

subject:
- current primary avatar / Cut Block two-module mark

## Trigger

Independent critique identified a concrete small-size gestalt risk:
the graphite and terracotta modules may remain individually legible but fail to assemble perceptually into one coherent object at 32 px.

This is a valid P1 review trigger under the current source-of-truth reopen rules.

## Observed issue

At 32 px:
- both modules remain visible;
- color hierarchy remains intact;
- the negative-space relationship remains visible;
- but the cream gap can become the strongest separator;
- first read can become "dark shape + orange shape" rather than one authored mark.

Therefore:
- SMALL-SIZE LEGIBILITY: PASS
- SMALL-SIZE GESTALT COHESION: PARTIAL / REVISE

## Root cause

Classification: IMPLEMENTATION / GEOMETRY RELATIONSHIP.

The problem is not color, brand personality, positioning, or the Cut Block concept.
The problem is the width and continuity of the separating negative space at avatar size.

## Repair contract

Preserve:
- Cut Block concept;
- two-module hierarchy;
- dominant graphite module;
- subordinate terracotta module;
- warm cream field;
- flat 2D language;
- no text, initials or handle dependency;
- no generic AI symbolism;
- no shield/hex/cube/pinwheel treatment.

Change only:
- module relationship at the central joint;
- gap width and local curvature;
- one controlled interlock/contact cue.

Target:
- at 32 px, perceive one mark first and two parts second.

Hard anti-regressions:
- no dominant S / Z / C / G / arrow read;
- no literal doorway/house read;
- no play-button read;
- no closed badge/container;
- no visual bridge that looks accidental or mechanically impossible.

## Acceptance

A repair may replace the current primary only if:
- GESTALT COHESION @ 32 PX: PASS
- 32 PX LEGIBILITY: PASS
- 64 PX LEGIBILITY: PASS
- BRAND PERSONALITY FIT: PASS
- DISTINCTIVENESS: PASS
- NO DOMINANT LETTER/ARROW/DOOR READ: PASS

Until then, the current primary remains authoritative.
