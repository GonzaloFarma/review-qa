# Repository Guidelines

## Project Structure & Source of Truth

This repository is the working space for QA review slides presented to business stakeholders in Farmacity Group. The active source of truth is `docs/contexto/qa_review_context.md`. Any session-level clarification, decision, or scope change that becomes stable should be folded back into this `AGENTS.md`.

Current key assets:

- `slider-01.html` and `slider-02.html` are deprecated artifacts from a previous initiative, but they must be reused as the structural base for the new slides.
- `docs/jira-cvs/Jira (Q1).csv` is the main operational dataset for Q1.
- `docs/jira-cvs/Capacity (sprint 3).csv` is a complementary dataset and currently only covers part of the capacity story.
- `docs/ejemplos-html/` contains reusable visual references and layout fragments.
- `docs/notas.txt` captures the unstructured brief that kicked off this phase.

Keep final presentation artifacts at the repo root unless a future restructuring is intentional and documented.

## Current Project Context

The purpose of this repository is not to build generic QA dashboards. It is to help Gonzalo Estevez present the QA team with more executive clarity, stronger business framing, and better stakeholder perception during quarterly reviews.

Constraints that define the work:

- Review format: 2 slides, 5 to 10 minutes of oral storytelling.
- Audience: owners, sponsors, and stakeholders who do not need Jira-level technical detail.
- Tone: business-facing, concise, visual, and easy to process quickly.
- Goal: show QA as a function that protects releases, reduces operational risk, and improves delivery confidence.

Current initial narrative under evaluation:

- Slide 1: Q1 team performance, completion by sprint, work mix by format and cross-team activity, bug share vs implementation QA vs internal work.
- Slide 2: Q1 bug management, bug volume by sprint, avoided bugs and rework caught before production, and bug severity split.

These two slides should evolve together as one story, not as isolated charts.

## Data Caveats Learned In Session

- The main Jira export uses 10 duplicated `Sprint` columns. Q1 analysis must read them together.
- `Campo personalizado (Criticidad)` is empty across the current Q1 export.
- Until that improves, severity-based storytelling should use `Prioridad` as a proxy and state that assumption explicitly.
- The CSV does not cleanly separate internal QA work from implementation support work.
- Any metric framed as `bugs evitados` is an inference unless a stricter source field is introduced.

## Working Canvas & Visual Direction

- Active canvas: `1440x840`
- Background: white, aligned to the shared Canva system
- Copy language: Spanish, written for business stakeholders
- Avoid Jira IDs and tool-native wording in the UI
- Prefer compact executive blocks over dense tables

When reworking `slider-01.html` and `slider-02.html`, preserve what is reusable and replace what is tied to the old project.

## Workflow by Phases

Work in deliberate phases instead of trying to solve the whole presentation at once.

Phase 1:

- Organize repository setup and versioning
- Normalize README and AGENTS context
- Align narrative, data sources, and slide methodology

Phase 2 onward:

- Define business storyline for each slide
- Extract and validate the metrics that really support that storyline
- Rebuild slide layouts in HTML/CSS
- Validate locally with Playwright CLI
- Refine copy and stakeholder framing

## Build, Test, and Development Commands

There is no build pipeline. Work directly on the HTML artifacts and validate them locally.

- `rg --files` lists the workspace files
- `cat docs/contexto/qa_review_context.md` reviews the active context
- `npm run pw:chrome` opens Playwright CLI in Chrome for layout validation
- `git status --short` checks the current versioned scope

If tooling grows later, document the exact command here and keep it lean.

## Coding Style & Naming Conventions

Follow the existing static HTML/CSS conventions:

- Use 2-space indentation in HTML and CSS
- Prefer semantic sectioning and readable markup blocks
- Keep CSS tokens in `:root`
- Use lowercase kebab-case for classes and files

Copy must stay stakeholder-facing:

- Prefer concise Spanish wording
- Translate technical work into impact, risk, confidence, throughput, prevention, and outcomes
- Avoid exposing raw Jira taxonomy unless it is transformed into business meaning

## Comportamiento específico para código

Antes de escribir cualquier solución:

- Si el requerimiento tiene una suposición falsa o incompleta, marcala antes de codear
- Indicá siempre si la solución genera deuda técnica o no escala, aunque no te lo pida
- Si hay dos enfoques válidos, mostralos con tradeoffs reales, no elijas por mí sin explicar

## Restricciones de output

- Sin comentarios que expliquen lo obvio
- Sin abstracciones prematuras
- Sin cierres motivacionales
- Si el requerimiento es ambiguo, preguntá lo mínimo necesario antes de proceder

## Testing Guidelines

There is no automated test suite yet. Validate changes manually before delivery:

- Open `slider-01.html` and `slider-02.html` in a desktop browser
- Use Playwright CLI in Chrome when layout or spacing changes
- Confirm the slide fits the `1440x840` canvas without overflow or clipped sections
- Check typography, spacing, visual hierarchy, and contrast
- Verify any metric or statement against `docs/contexto/qa_review_context.md` and the CSV sources in `docs/jira-cvs/`

When creating new variants, name them clearly and keep deprecated files only while they still serve as a reusable base.

## Commit & Pull Request Guidelines

The repository already exists on GitHub at `GonzaloFarma/review-qa`. Use short imperative commit messages such as:

- `Add repository baseline docs`
- `Rewrite AGENTS for Q1 QA review context`
- `Refactor slide 01 executive layout`

For pull requests, include:

- A short summary of the narrative or visual change
- The data source updated or introduced
- A screenshot when the layout changes
- Any open issue around copy, branding, or data interpretation
