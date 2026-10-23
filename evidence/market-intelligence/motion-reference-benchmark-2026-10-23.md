# Motion reference benchmark for Ali's Reels: inspected set v1

record_id: PBGS-MCI-MOTION-002
date: 2026-10-23
status: PARTIAL / BOUNDED / NOT AN ELITE-CALIBRATED BENCHMARK
responds_to: `handoffs/claude-motion-reference-research-2026-10-23.md` (PBGS-HANDOFF-CLAUDE-MOTION-001)
builds_on: `evidence/market-intelligence/motion-design-reference-discovery-2026-10-23.md` (PBGS-MCI-MOTION-001)
method: Creative Reference Intelligence v0.4 (CANDIDATE / NOT QUALIFIED) with independent source paths; research owner Market & Competitive Intelligence 1.0.0 (QUALIFIED)

benchmark_status: PARTIAL
generation_allowed: BOUNDED (capture, proof selection and a timecoded storyboard may proceed; no style-dependent final render and no claim of elite-calibrated visuals)

## How the videos were observed (read this first)

No human watched these videos. Each was run through vidIQ's automated video analysis (`vidiq_watch_shortform_content`, `vidiq_video_watch`) with a fixed craft prompt, and the analysis text was recorded. Timecodes below are as reported by that analysis. Spot check performed: for three of the four, the returned first-frame image was compared with the analyzer's first-frame description and matched. The analyzer also made errors: for the mrdataanalyst video it quoted tooltip text that differs from the visible tooltip in the returned frame, and for the Kaydee video it asserted exact easing curves, which an automated frame review cannot measure. Treat structure, timing and layout as usable; treat exact text, numbers and easing claims as unverified. Anyone about to rely on a specific timecode should scrub the original once.

Evidence class for everything below: `ANALYZER_OBSERVED`. Nothing here establishes commercial outcomes. Views and outlier scores were not used as quality evidence.

## Inspected references (4)

### R1. Kraya, WhatsApp CRM follow-up demo (native Instagram analog, DIRECT)
- URL: https://www.instagram.com/reel/Dc0y6QKs8uY/ (account @kraya.ai)
- Observed version: 9:16, 20.97 s, Instagram Reel
- Timecodes: 00:00 first frame is a talking-head reaction with an orange hook banner in the top fifth; 00:01 hard cut to the real CRM/WhatsApp screen filmed over the shoulder; 00:04-00:13 proof moment, a stylus scrolls through a day-by-day automated message sequence on the real interface; 00:14-00:17 reply stops the sequence; 00:18-00:20 last frame, wide shot with CTA banner "comment LINK".
- Hook: outcome claim ("100+ clients in 3 hours") as a banner over a face.
- Typography: solid colored banners, one role per color (hook, explanation, CTA), uppercase sans, placed top fifth and about 20% above the bottom edge.
- Pacing and transitions: hard cuts every 2-4 s, no decorative transitions; camera focuses on the interface physically, no digital zoom.
- Mute test: the analyzer judged the message fully readable without sound, because each step is mirrored by banner text and the pointer. The reel itself carries a pop track.
- Class: DIRECT for the commercial job (show a real automation to a business owner). It is not a motion-design craft reference.
- Clears: real-interface proof, one claim per scene, mute-readable text sequence, safe-zone banner placement.
- Does not establish: motion craft quality, whether the claim is true, any sales result.
- Decision for Ali: ADAPT. Take the pointer-led proof on a cropped real panel and the one-claim-per-banner rhythm. REJECT the talking head (Ali's content has no face and no images of women), the music, the "comment LINK" CTA and the copy of the colored banner system.

### R2. Roomonitor 2.0 platform explainer, ArcFrame (studio film, DIRECT-ADJACENT for mechanism)
- Maker page: https://arcframe.agency/projects/roomonitor-2-platform-explainer/ (2026)
- Observed version: YouTube https://youtu.be/PBhGkeqs2nw, 16:9, 32 s, silent (no music, no voice, no SFX per the analysis)
- Version discrepancy: the maker's page says 57 seconds and mentions vertical and square exports; the YouTube file observed is 32 seconds, 16:9. The vertical cutdowns were not linked and not observed.
- Timecodes: 00:00 first frame, isometric 3D dashboard mockup with channel icons and a two-line headline (problem: many channels, one inbox); 00:00-00:03 the angled UI snaps flat and a badge pops in; 00:08-00:10 real chat inbox, a thread is selected, a reply is generated, status pill "resolved by assistant" springs in at 00:10; 00:12-00:24 rule configuration screen, second status pill at 00:24; 00:16-00:18 typography-only break; 00:26-00:32 dark map dispatch view, slow continuous zoom, last frame.
- Mechanism: `one incoming request -> visible state change -> resolved badge`, repeated at three levels of the same system.
- Transitions: scale and push between UI layers, perspective-to-flat snap to move from overview to detail; the analyzer read these as carrying meaning (overview to execution).
- Mute test: fully understandable silent, text carries every beat.
- Class: ADJACENT_ELITE for UI-motion mechanism (maker's claim of craft; not independently corroborated).
- Clears: state-change visualization on real-looking UI, music-free structure, hierarchy (one headline, UI as proof).
- Does not establish: vertical performance (16:9 observed), cost fit for a solo provider, buyer outcome, or that the UI is a real client product (maker-supplied).
- Decision for Ali: ADOPT the state-change badge idea (a visible status flip that confirms the work happened). ADAPT the perspective-to-flat entry only if it fits a vertical crop. REJECT the three-tier structure (too long), the Spanish copy and the studio's layout.

### R3. Kaydee, Spotify UI motion piece (native TikTok, ADJACENT, mostly rejected)
- URL: https://www.tiktok.com/@kaydee.c0/video/7668413419451682070
- Observed version: 16:9 (not vertical), 13.5-13.7 s
- Timecodes: 00:00 grid of hollow circles; 00:00-00:03 grid tilts and resolves into a brand logo; 00:03-00:05 color flip and kinetic particle; 00:08-00:11 fast zoom into a lyrics view with one highlighted word; 00:13 creator title card.
- Mute test: partially survives; the cuts are timed to an audio beat.
- Class: VOICE_STYLE_CRAFT only.
- Decision: REJECT as a template. It is a fan edit of another company's brand (rights and distinctiveness risk), horizontal, beat-dependent, and has no business-owner proof job. The only transferable observation is that muted UI chrome next to one highlighted element keeps hierarchy clear.

### R4. mrdataanalyst, dashboard in 3 minutes (native TikTok, counter-example)
- URL: https://www.tiktok.com/@mrdataanalyst/video/7673553206785379617
- Observed version: 9:16, 10.2-11.4 s
- Timecodes: 00:00 headline in the upper third over a 16:9 desktop screen recording letterboxed in a vertical frame; 00:00-00:10 single continuous take, cursor hovers over charts, no cuts, no zoom, no pan; last frame same layout.
- Mute test: passes via the headline.
- Class: DIRECT format, but a negative reference.
- Failure observed in the returned frame: the whole desktop is shown unzoomed, so interface text is unreadable at phone size.
- Decision: REJECT the layout. Rule derived: never place a full desktop screenshot unzoomed in 9:16; crop to the single panel that carries the proof.

## Discovered, NOT inspected

These stay `DISCOVERED / NOT INSPECTED`. The moving files were found but could not be played by the tools available in this session.
- PEDRA, EFTsim: https://www.pedra.tv/work/eftsim (film on Vimeo and a studio-hosted mp4; maker lists a Video of the Day award dated 2025-09-16). Not watched.
- PEDRA, MakerBOS: https://www.pedra.tv/work/makerbos (same maker origin, so not independent). Not watched.
- BUCK, Zapier Motion Library: https://buck.co/work/zapier-motion-library (nine clips on Mux, no playable stream exposed). Not watched.
- Ordinary Folk, Webflow Ecommerce: https://www.ordinaryfolk.co/project/webflow-ecommerce (not re-fetched in this pass). Not watched.
- Third source path (juried or curated motion work): only the PEDRA award reference above was reached, and not as a watched film. This path is effectively open.

## Why the status is PARTIAL and not READY

1. Only one music-free film was inspected, and it is 16:9, 32 s.
2. The only DIRECT native vertical analog with real software (R1) uses music and a talking head, which Ali's rules exclude.
3. The curated/juried motion path has no inspected film.
4. All observation is automated analysis, not a person watching.
5. No real or approved Ali project screen has been supplied for proof (see open conflicts).

## Motion design vocabulary (from R1 and R2 only, R3 and R4 as limits)

- Opening frame: real interface visible from frame one, one headline stating the buyer's problem or outcome in the top fifth, no logo or intro card (R1, R2).
- Hierarchy: one headline plus one highlighted element at a time; dim interface chrome (R2, R3).
- Intended movement: movement exists to move attention to the next piece of proof. In R1 it is a pointer on the real screen; in R2 it is a selection and a spring-in status badge.
- Interface proof: crop to one panel and enlarge until every word is readable at phone size (R1 camera crops, R4 failure).
- State change: show the before state, the action, and an unmistakable resolved state (badge or status pill) (R2).
- Transition system: hard cuts at 2-4 s (R1) or scale/push that expresses overview to detail (R2); no decorative wipes.
- Text behavior: one claim per scene, short sentences, color roles consistent across the piece (R1 banners, R2 headers).
- 9:16 reading pattern: headline in the top fifth, proof in the middle, bottom 20% clear for platform interface (R1; matches the earlier showcase standard).
- No-music adaptation: both R1 and R2 are readable with sound off, but R1 relied on a beat for cadence. Without music, rhythm must come from the text-change interval (2-4 s) and the timing of status flips. This adaptation is untested.

## One testable mechanism (recommendation, not a look)

Mechanism: `one incoming request -> status changes on a real panel -> visible resolved state`, in 12-20 s, cropped to a single legible panel, with a top-fifth headline stating the owner's problem, text-led rhythm and no music.

Hypothesis to test, not a claim: a Reel that shows a visible state change on one cropped real panel holds attention better than a static screen recording of the same system (R4-style). Measure on Ali's first two or three posts: average watch time or completion, saves, and count and quality of direct inquiries. A sample this small can only show direction, so decide next steps from it with that limit in mind.

## Open conflicts that need Ali's decision

1. Real proof versus fictional example. The handoff requires real Ali project screens and forbids fictitious interfaces. Ali's saved preference for product Reels is a fictional, general-purpose example that every business owner understands, instead of his real CRM (too niche). Resolution options for Ali: (a) a real screen cropped to a generic-readable moment (for example a status change on the DasMotors landing request path or a FleetDesk contract status), (b) a clearly labeled demonstration on neutral data. Until Ali chooses, no proof asset is selected.
2. Audience. The handoff says "nontechnical UAE business owner". Ali stated that the audience is not tied to the UAE and the Instagram is in Russian. This record follows Ali's statement.
3. Handle. The handoff calls @nosignoutside not approved by default. Ali stated the handle was chosen long ago. This record does not put any handle in storyboard content; CTA and handle come from `source-of-truth/current-brand-identity.md` at production time.

## GAP

Original motion art direction as a stand-alone professional competence is still not covered by a qualified core. Social Content Creative owns the buyer story, Video Editing & Post-Production owns assembly and finish. This record does not impersonate a Motion Design professional.

## Handoff

1. Ali: choose the proof asset and the real-versus-neutral question above.
2. Social Content Creative 0.1.0: approved buyer story, exact on-screen text and verified claims for one request-to-resolved sequence.
3. Video Editing & Post-Production 0.1.0: timecoded vertical storyboard and edit using the vocabulary above, then artifact-first QC (decode the file, check every critical word at phone size, run a muted playback).
4. Before any style-dependent final render: re-open this benchmark and either inspect a vertical music-free UI film or accept `BOUNDED` explicitly.

This record authorizes no rendering, publishing, asset change or commercial claim.
