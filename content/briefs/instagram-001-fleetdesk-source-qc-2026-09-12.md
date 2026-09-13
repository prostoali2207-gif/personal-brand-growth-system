# Source-media QC — PBGS-IG-001 FleetDesk

date: 2026-09-12
last_updated: 2026-09-13
source_file: Screen_Recording_20260912_195400_Chrome.mp4
duration: ~32.9s
resolution: 1080x2340
video: H.264, vertical
audio_track: none
status: KEEP_WITH_LIMITATION / TEST_DATA_CONFIRMED
capture_core: Video Capture & Camera Operations v0.4 — CANDIDATE / NOT QUALIFIED / STAGE_A_PASS; development B0/B1 rerun on v0.4 still pending upstream

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

The visible records appeared intentionally synthetic/test-like during source QC:
- phone numbers use a sequential +97150000020x pattern;
- one visible email uses example.com;
- vehicle plates use SHOW-52xx;
- Emirates ID fields shown are blank.

On 2026-09-13 the project owner explicitly confirmed that the supplied recording uses **test data**.

Therefore the prior human-confirmation privacy blocker is resolved for this exact source file. No real-person identity is treated as evidence from the capture.

This confirmation does not change claim scope: the recording demonstrates UI/product state only and must not be used to imply real customer outcomes, real balances, real contract counts or real operational performance.

## QC decision

Decision: KEEP_WITH_LIMITATION.

Why keep:
- vertical, sharp and readable;
- UI state is stable enough for editorial crops;
- the recording gives real product evidence for contract relationships and financial modules;
- Fleet states clearly show Rented / Available;
- no audio contamination because source has no audio track;
- test-data status is now explicitly confirmed by the project owner.

Limitations:
1. The source is one continuous navigation recording rather than clean separate clips.
2. Visible names/phones are synthetic test records. They no longer create a privacy blocker for this exact file, but Post may still crop them when they distract from the communication job.
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

Do not use the Clients list as a hero visual unless it serves a specific communication purpose; it is visually dense and not needed for the current proof path.

## Remaining capture before Post handoff

Required:
- approved spoken script;
- real voice-over source takes under the responsible narration/performance owner once available;
- separate hook backup;
- separate payoff backup.

Strongly recommended:
- one clean dedicated Payments clip;
- one clean dedicated Fines clip;
- one clean dedicated Salik clip;
- one safe state-transition demo using test data, OR keep the state-transition explanation as a verified diagram/annotation rather than pretending it was directly demonstrated.

## Source readiness

media observed: YES
test-data confirmation: YES

This source alone is NOT SOURCE_READY_FOR_POST as a complete package because spoken-source performance is still missing.
It is a usable visual component of the package: KEEP_WITH_LIMITATION.

## Upstream status correction

The previous version labeled Video Capture & Camera Operations v0.4 as DEVELOPMENT_PASS. Current upstream issue #294 does not support that status: v0.4 is frozen with Stage A PASS, while the required v0.4 B0/B1 development rerun is still pending. This record now uses the verified upstream status and makes no qualification/development-pass claim.
