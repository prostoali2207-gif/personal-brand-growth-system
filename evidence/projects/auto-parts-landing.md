# Auto Parts Landing evidence packet

- project_id: `auto-parts-landing`
- project_name: `Auto Parts Landing`
- repository_or_system_refs:
  - https://github.com/prostoali2207-gif/auto-parts-landing
  - https://github.com/prostoali2207-gif/auto-parts-landing/blob/main/README.md
  - https://github.com/prostoali2207-gif/auto-parts-landing/blob/main/package.json
  - https://github.com/prostoali2207-gif/auto-parts-landing/blob/main/app/page.tsx
- user_role: GitHub repository owner/maintainer account; author of cited PRs.
- time_scope: August-September 2026 evidence reviewed.
- problem_or_goal: Build and iterate a focused automotive-parts request landing with an existing CRM request flow rather than an ecommerce catalog.

## Artifacts

- PR #21 — Finalize Spline commercial landing:
  https://github.com/prostoali2207-gif/auto-parts-landing/pull/21
- PR #22 — Fix production smoke success selector:
  https://github.com/prostoali2207-gif/auto-parts-landing/pull/22
- PR #31 — Fix V7 process motion browser compatibility:
  https://github.com/prostoali2207-gif/auto-parts-landing/pull/31
- PR #36 — Add real supplier visual proof to trust layer:
  https://github.com/prostoali2207-gif/auto-parts-landing/pull/36
- PR #39 — Improve trust media quality on mobile:
  https://github.com/prostoali2207-gif/auto-parts-landing/pull/39
- Issue #12 — Commercial launch: add real trust evidence and confirmed customer channels:
  https://github.com/prostoali2207-gif/auto-parts-landing/issues/12

## Observable work

- The project declares Next.js 16, React 19, TypeScript and Playwright.
- README states production deployment is managed by Vercel.
- The current page code calls Supabase Edge Function endpoints for `create-landing-request` and `track-landing-event`.
- PR history records repeated mobile/desktop rendered review, Playwright regression gates, browser-compatibility fixes, purposeful-motion refinements and real supplier media integration.
- PR #31 replaces a fragile browser-dependent animation mechanism with an IntersectionObserver-based trigger while preserving request/CRM behavior.
- PR #36 adds user-supplied real supplier visual proof with explicit truth boundaries.
- PR #39 replaces an over-compressed mobile proof video with a quality-preserving 1080x1920 derivative.

## Observable outcomes

- PR #22 states that the first production smoke after PR #21 successfully created CRM request #15; the smoke then failed only because its success-text selector matched two nodes.
- This supports a narrow end-to-end fact: the production landing request path reached the CRM successfully in that smoke.
- It does **not** establish that the landing generated 15 customers/leads or improved conversion.

## Limitations / unknowns

- No verified conversion-rate uplift, paid-traffic result, revenue, lead-quality improvement or customer acquisition figure was found.
- Supplier proof is bounded evidence of real supplier environments; it must not be expanded into unsupported warehouse, stock, affiliation or availability claims.

## Claim candidates

- Develops production-oriented landing pages with real CRM integration, browser/device regression testing and iterative release gates.
- Has implemented a verified landing -> Supabase Edge Function -> CRM request path.

- last_verified_at: `2026-09-04`
