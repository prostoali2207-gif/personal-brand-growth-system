# FleetDesk evidence packet

- project_id: `fleetdesk`
- project_name: `FleetDesk / uae-drive-suite`
- repository_or_system_refs:
  - https://github.com/prostoali2207-gif/uae-drive-suite
  - https://github.com/prostoali2207-gif/uae-drive-suite/blob/main/README.md
  - https://github.com/prostoali2207-gif/uae-drive-suite/blob/main/package.json
- user_role: GitHub repository owner/maintainer account; author of the cited pull requests and commits.
- time_scope: evidence reviewed from July-August 2026 repository history.
- problem_or_goal: The repository README defines FleetDesk as a UAE car-rental management SaaS intended to make daily rental operations faster, clearer and less manual.

## Artifacts

- PR #1 — Add additional contract drivers foundation:
  https://github.com/prostoali2207-gif/uae-drive-suite/pull/1
- PR #2 — Add parking import from Salik PDF:
  https://github.com/prostoali2207-gif/uae-drive-suite/pull/2
- PR #4 — Add read-only FleetDesk GPT Actions API:
  https://github.com/prostoali2207-gif/uae-drive-suite/pull/4
- PR #14 — Fix signed contract WhatsApp PDF link:
  https://github.com/prostoali2207-gif/uae-drive-suite/pull/14
- Commit `5f0c2fbd8db7c6aea03619929b3a1d204acada46` — Add secure FleetDesk storage download bridge:
  https://github.com/prostoali2207-gif/uae-drive-suite/commit/5f0c2fbd8db7c6aea03619929b3a1d204acada46
- Commit `9e9d7ac636a877c10d9256a1efb0d5e27a2afe15` — Fix contract PDF to show deposit in rental summary:
  https://github.com/prostoali2207-gif/uae-drive-suite/commit/9e9d7ac636a877c10d9256a1efb0d5e27a2afe15
- Commit `70d6c0d9dfe79ccfb3e07885229bad10d2f134cd` — Allow customer signing after manager signature:
  https://github.com/prostoali2207-gif/uae-drive-suite/commit/70d6c0d9dfe79ccfb3e07885229bad10d2f134cd

## Observable work

- Product areas in the README include fleet, clients, contracts, payments, deposits, fines, Salik, reports, PDF contracts and company settings.
- The codebase declares React, TypeScript, Vite, Supabase, TanStack Query, jsPDF/pdf-lib/pdfjs, XLSX, Zod, Playwright and Vitest among its dependencies/dev dependencies.
- PR #1 adds contract-driver persistence and tenant-safe RLS foundations.
- PR #2 adds Salik-PDF parking import with validation, matching and duplicate protection.
- PR #4 adds a protected read-only API for contract search and vehicle availability, Bearer API-key authentication, owner isolation and an OpenAPI schema for GPT Actions.
- PR #14 changes signed-contract sharing to use a persistent public Supabase Storage URL.

## Observable outcomes

- The cited PRs are merged into the repository history.
- FleetDesk has a GitHub-traceable integration surface for GPT Actions and multiple operational car-rental workflows.
- These are product/engineering outcomes. No revenue, user-count, adoption, time-saved or business-impact figure is established by this packet.

## Limitations / unknowns

- No verified customer count, company count, revenue, MRR, retention or production load metric was found in the reviewed GitHub evidence.
- No claim of scale or market success is supported by this packet.
- Repository authorship supports contribution/maintenance claims; it does not by itself quantify what percentage of every subsystem was personally coded without AI/tool assistance.

## Claim candidates

- Developed and maintains an applied car-rental SaaS with operational workflows, Supabase-backed data, PDF/import flows and API integrations.
- Integrated a real business application with GPT Actions through a protected read-only API.

- last_verified_at: `2026-09-04`
