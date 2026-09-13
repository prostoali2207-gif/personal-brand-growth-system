# Initial commercial content portfolio v2 — 2026-09-13

## Superseded 2026-09-13
Use `decisions/initial-commercial-content-portfolio-v3-2026-09-13.md`. Breadth is now distributed across assets; a landing asset no longer needs CRM as a depth signal.

decision_id: PBGS-PORTFOLIO-002
date: 2026-09-13
status: SUPERSEDED / LANDING-TO-CRM FIRST-ASSET MODEL INVALIDATED
owning_composition:
- Market & Competitive Intelligence 1.0.0 — QUALIFIED inputs
- Growth Strategy & Experiment Portfolio v0.1 — CANDIDATE / NOT QUALIFIED
- Content Portfolio & Launch Sequencing — APPLIED CAPABILITY / NOT A QUALIFIED CORE
upstream:
- decisions/commercial-offer-service-positioning-v1-2026-09-13.md
- decisions/audience-channel-role-strategy-v2-2026-09-13.md

## Portfolio objective

Make a non-technical business prospect understand two things:

1. the visible service front door is websites / landing pages;
2. the work can continue into CRM, automation and custom systems when the business needs more than a page.

Do this through real work, not a flat services list.

## Initial sequence hypothesis

### 1. PARTS-FLOW-01 — "Сайт — это только начало заявки"
Source:
auto-parts landing + BayerCRM.

Portfolio role:
**FRONT-DOOR OFFER + DEPTH SIGNAL**

Verified proof:
`Landing -> Edge Function -> requests/request_items/request_photos -> manager in BayerCRM`.

Buyer meaning:
a landing page can collect a structured request and pass it into the working process/CRM.

Important:
do not require the viewer to understand Edge Functions or backend.

Commercial relevance:
directly represents Website/Landing while proving CRM/integration depth.

### 2. PARTS-UX-01 — "Форма должна повторять реальную заявку"
Source:
auto-parts landing.

Candidate evidence opportunity:
multiple parts per vehicle / photo-backed request data.

Portfolio role:
**WEBSITE/LANDING PRODUCT JUDGMENT**

Buyer meaning:
a useful site/landing is not decoration; the request flow should fit what the customer actually needs to submit.

Need exact evidence verification before public scripting.

### 3. BAYER-NEXT-01 — "CRM должна показывать, что делать дальше"
Source:
BayerCRM.

Portfolio role:
**CRM SERVICE RANGE**

Verified basis:
clear request status / next action is an explicit product priority; mobile-first/minimal workflow is documented.

Buyer meaning:
CRM is useful when the team can see the next action, not when it is just another table.

Do not claim measured productivity improvement.

### 4. FLEET-AUTO-01 — "Известное правило можно убрать из ручной работы"
Source:
FleetDesk.

Portfolio role:
**AUTOMATION DEPTH**

Verified proof:
contract/vehicle state rule.

Buyer meaning:
when the next state follows a known rule, part of the process can live in the system instead of being another manual step.

Existing FleetDesk script may be reused only after buyer-language rebrief; its previous portfolio sequence is superseded.

### 5. CUSTOM-SYSTEM-01 — "Когда сайта и готовой CRM уже мало"
Source:
FleetDesk + BayerCRM, only with bounded evidence.

Portfolio role:
**CUSTOM SYSTEM CAPABILITY**

Buyer meaning:
some workflows need a purpose-built internal tool rather than more plugins/spreadsheets.

Do not imply every business needs custom software.

### 6. AI-METHOD-01 — "Как я проверяю AI-агентов, а не просто пишу длинный prompt"
Source:
professional-ai-agents.

Portfolio role:
**SECONDARY TECHNICAL CREDIBILITY**

Audience:
technical peers / sophisticated buyers.

Rule:
not part of the first commercial category-establishment sequence unless first-party evidence later shows it improves qualified commercial demand.

## Why PARTS-FLOW-01 goes first

It is currently the strongest evidence-backed bridge between:
- the most understandable entry service: landing/site;
- a deeper differentiator: CRM/integration;
- a real project artifact;
- non-technical buyer language.

It therefore demonstrates breadth **without** making breadth itself the topic.

## What is deliberately NOT first

- "I make websites, CRM, automation and AI";
- FleetDesk feature walkthrough;
- professional-agent qualification;
- generic AI tutorial;
- generic introduction/about-me video;
- custom-system complexity.

## Content mix principle

Early portfolio should move outward from the buyer's most legible need:

`website/landing -> what happens after the enquiry -> CRM -> automation -> custom system -> optional technical/AI depth`.

This mirrors the commercial offer ladder.

Do not encode a permanent posting quota from this sequence.

## HYPOTHESIS PBGS-HYP-PORT-002

Leading with a real landing-to-CRM case will establish both commercial relevance and deeper capability more clearly than either:
- a generic services intro; or
- a technically led AI/system post.

Formal adjudication requires Measurement.

## Next handoff

`PBGS-PORTFOLIO-002 -> Content Architecture v0.4`

First asset:
`PARTS-FLOW-01`.

Exact public language remains blocked on final channel-language decision, but architecture may proceed.
