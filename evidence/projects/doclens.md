# DocLens evidence packet

- project_id: `doclens`
- project_name: `DocLens`
- repository_or_system_refs:
  - https://github.com/prostoali2207-gif/doclens
  - https://github.com/prostoali2207-gif/doclens/blob/main/README.md
  - https://github.com/prostoali2207-gif/doclens/blob/main/package.json
- user_role: GitHub repository owner/maintainer account; author of cited PRs.
- time_scope: August 2026 evidence reviewed.
- problem_or_goal: The README defines a universal mobile-first document OCR application; repository work extends this into document scanning/crop flows and Android packaging.

## Artifacts

- PR #1 — Improve hybrid document auto-crop:
  https://github.com/prostoali2207-gif/doclens/pull/1
- PR #3 — Add automatic Android APK build:
  https://github.com/prostoali2207-gif/doclens/pull/3
- PR #4 — Restore ML Kit as primary Android crop:
  https://github.com/prostoali2207-gif/doclens/pull/4
- PR #6 — Add manual crop review for every native scan:
  https://github.com/prostoali2207-gif/doclens/pull/6
- PR #7 — Keep ML Kit crop and open immediate editable review (closed, not merged):
  https://github.com/prostoali2207-gif/doclens/pull/7

## Observable work

- The web code declares React, Vite, TypeScript, Tesseract.js and scanic.
- Repository structure includes Android and API layers.
- PR #1 adds a hybrid document-boundary approach using OpenCV-oriented contour/Hough/GrabCut mechanisms and candidate scoring.
- PR #3 adds GitHub Actions CI to build an Android debug APK with Java/Gradle.
- PR #4 restores Google ML Kit Document Scanner as the primary Android scanner after testing.
- PR #6 adds a manual crop-review flow.
- PR #7 is explicitly closed because that direction was wrong for the native Android flow, preserving the ML Kit single edit path instead.

## Observable outcomes

- The repository demonstrates an iterative document-scanning/OCR product path across web and Android.
- It also records a rejected implementation direction rather than representing every experiment as successful.

## Limitations / unknowns

- No verified OCR accuracy benchmark, production adoption, user count or commercial result was found.
- The evidence does not support a claim that a proprietary OCR/ML model was trained.
- README scope may lag later Android/crop PR history; PRs are used as the more specific implementation evidence.

## Claim candidates

- Has built and iterated a mobile-first OCR/document-scanning application using existing OCR/scanning technologies and Android/web flows.
- Has worked with Tesseract.js, Android ML Kit and document-boundary/cropping approaches in a real repository.

- last_verified_at: `2026-09-04`
