# Source-media QC — PBGS-IG-001 FleetDesk

date: 2026-09-12
source_file: Screen_Recording_20260912_195400_Chrome.mp4
duration: ~32.9s
resolution: 1080x2340
video: H.264, vertical
audio_track: none
status: KEEP_WITH_LIMITATION
capture_core: Video Capture & Camera Operations v0.4 — CANDIDATE / NOT QUALIFIED / DEVELOPMENT_PASS

## Observed source

The screen recording visibly includes:
- Contracts list;
- one contract detail;
- contract/client/vehicle relationship;
- contract Financials with Rent Outstanding, Traffic Fines, Salik;
- Fleet list with Rented / Available / Maintenance states;
- Clients list;
- Dashboard with unpaid fines, unpaid Salik, outstanding contract totals and fleet summary.

## Privacy / truth check

The visible records appear intentionally synthetic/test-like rather than production customer data:
- phone numbers use a sequential +97150000020x pattern;
- one visible email uses example.com;
- vehicle plates use SHOW-52xx;
- Emirates ID fields shown are blank.

No real-person identity is treated as verified from this capture.

Before public release, human must confirm these are test/synthetic records.

## QC decision

Decision: KEEP_WITH_LIMITATION.

Why keep:
- vertical, sharp and readable;
- UI state is stable enough for editorial crops;
- the recording gives real product evidence for contract relationships and financial modules;
- Fleet states clearly show Rented / Available;
- no audio contamination because source has no audio track.

Limitations:
1. The source is one continuous navigation recording rather than clean separate clips.
2. It shows client names/phones, even though they look synthetic. Publication should still crop/redact them unless human confirms test-data status.
3. It does not visibly demonstrate a state transition from contract status to vehicle status; it only shows the resulting states.
4. It does not independently prove the conditional rule:
   Completed/Cancelled + no other active contract -> Available.
   That rule remains repo-backed evidence and should be communicated through an annotation/diagram unless a safe test-state demo is captured.
5. Payments is visible inside Financials, but there is no dedicated clean Payments module shot.
6. Fines/Salik appear inside Financials and Dashboard; dedicated module shots are not present.
7. Browser chrome, status bar and recording indicator are visible and should be cropped/treated by Post.
8. No voice-over source is present.

## Usable sections

Use as source evidence for:
- hook/product reality;
- contract screen;
- contract -> client / vehicle;
- rent/fines/Salik linkage;
- Fleet status examples;
- Dashboard operational-state overview.

Do not use the Clients list as a hero visual unless cropped/redacted.

## Remaining capture before Post handoff

Required:
- 2 voice-over takes;
- separate hook backup;
- separate payoff backup.

Strongly recommended:
- one clean dedicated Payments clip;
- one clean dedicated Fines clip;
- one clean dedicated Salik clip;
- one safe state-transition demo using test data, OR keep the state-transition explanation as a verified diagram/annotation rather than pretending it was directly demonstrated.

## Source readiness

media observed: YES

This source alone is NOT SOURCE_READY_FOR_POST as a complete package.
It is a usable component of the package: KEEP_WITH_LIMITATION.
