# Repository Guidelines

## Project Structure & Source of Truth

This repository is the working space for QA review slides presented to business stakeholders in Farmacity Group.

Primary source of truth:

- `docs/contexto/qa_review_context.md`

Operational maintenance guide:

- `docs/contexto/slide_maintenance_system.md`

Current production artifacts:

- `slider-01.html` for delivery, improvements, and innovation
- `slider-02.html` for risk and bugs
- `slider-03.html` for TeAyudo ticketing

Reference artifact:

- `slider-q1.html` remains only as the source layout used to split the original unified slide into `slider-01` and `slider-02`

Main data assets:

- `docs/jira-cvs/Jira (Q1).csv`
- `docs/jira-cvs/Jira-mejoras (Q1).csv`
- `docs/jira-cvs/Jira-error (Q1).csv`
- `docs/contexto/q1_metrics_baseline.md`
- `docs/contexto/teayudo_ticketera_q1.json`
- `docs/story/q1-data-team.md`
- `docs/capturas/slider-03.png`

Keep final presentation artifacts at the repo root unless a future restructuring is intentional and documented.

## Current Project Context

The purpose of this repository is not to build generic QA dashboards. It is to help Gonzalo Estevez present the QA team with executive clarity, stronger business framing, and better stakeholder perception during quarterly reviews.

Current working model:

- `3` horizontal slides
- `5` to `10` minutes of oral storytelling across the sequence
- business-facing, concise, visual copy
- minimal Jira-native wording in visible UI

Current narrative split:

- `slider-01.html`: delivery, improvements, and innovation
- `slider-02.html`: risk, bugs, and priority
- `slider-03.html`: ticketing behavior in TeAyudo

Current direction:

- simplify as much as possible without losing executive meaning
- prefer stable layout and easy data refresh over new visual exploration
- when something feels dense, simplify copy or numbers before changing structure

## Data Caveats

- The main Jira export uses `10` duplicated `Sprint` columns. Q1 analysis must read them together.
- `Campo personalizado (Criticidad)` is empty in the current Q1 export.
- Severity storytelling should use `Prioridad` as a proxy until a better source exists.
- `Tiempo Trabajado` is incomplete, so any hour metric must be labeled as `horas registradas en Jira`.
- A ticket belongs to the Q1 cut if it appears in any Q1 sprint column, even if it closes later.
- `Capacity (Q1).csv` is exploratory only and should not be treated as executive truth.
- `slider-03` currently uses manually transcribed data from `docs/capturas/slider-03.png`, normalized in `docs/contexto/teayudo_ticketera_q1.json`.

## Working Canvas & Visual Direction

- Active canvas: `1440x840`
- Main visual reference available in repo: `docs/ejemplos/slider-equipo/`
- Shared palette base:
  - `#211274`
  - `#5ba698`
  - `#d7d8d8`
  - `#ff3131`
  - `#00dd88`
  - `#49a5ef`
  - `#ffd359`
  - `#ffffff`
- Shared typography: `Montserrat`
- Background direction: white base with subtle executive treatment, no heavy dashboards

Stable UI principles:

- keep the current slide architecture
- keep block hierarchy stable
- keep titles and main panels in place unless a redesign is explicitly requested
- prefer compact executive cards over dense tables
- prefer updating data and short copy instead of redesigning components

## Workflow

Use this order by default:

1. Validate which slide is affected
2. Confirm numbers and short labels from the corresponding source
3. Update the slide HTML
4. Run manual visual validation
5. Fold stable changes back into docs

## Build, Test, and Development Commands

There is no build pipeline. Work directly on the HTML artifacts and validate them locally.

- `rg --files` lists the workspace files
- `cat docs/contexto/qa_review_context.md` reviews the active project context
- `cat docs/contexto/slide_maintenance_system.md` reviews the maintenance rules
- `python3 -m http.server 4173 --bind 0.0.0.0` serves the repo locally
- `npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-01.html /tmp/slider-01.png`
- `npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-02.html /tmp/slider-02.png`
- `npx playwright screenshot --device='Desktop Chrome HiDPI' --viewport-size=1440,840 http://127.0.0.1:4173/slider-03.html /tmp/slider-03.png`
- `git status --short` checks the current versioned scope

## Coding Style & Naming Conventions

Follow the existing static HTML/CSS conventions:

- use 2-space indentation in HTML and CSS
- prefer semantic sectioning and readable markup blocks
- keep CSS tokens in `:root`
- use lowercase kebab-case for classes and files

Copy must stay stakeholder-facing:

- concise Spanish wording
- convert technical work into impact, risk, confidence, throughput, prevention, and outcomes
- avoid raw Jira taxonomy in visible UI unless explicitly needed

## Specific Code Behavior

Antes de escribir cualquier solución:

- si el requerimiento tiene una suposición falsa o incompleta, marcala antes de codear
- indicá si la solución genera deuda técnica o no escala, aunque no te lo pidan
- si hay dos enfoques válidos, mostrálos con tradeoffs reales

## Output Restrictions

- sin comentarios que expliquen lo obvio
- sin abstracciones prematuras
- sin cierres motivacionales
- si el requerimiento es ambiguo, preguntá lo mínimo necesario antes de proceder

## Testing Guidelines

There is no automated test suite yet. Validate changes manually before delivery:

- open the affected slide in a desktop browser
- serve the repo through local HTTP before using Playwright
- confirm the slide fits `1440x840` without overflow or clipping
- check typography, spacing, visual hierarchy, and contrast
- verify numbers against the corresponding context/story/data source
- if `slider-q1.html` is edited for reference reasons, validate it separately

## Commit & Pull Request Guidelines

The repository already exists on GitHub at `GonzaloFarma/review-qa`.

Use short imperative commit messages such as:

- `Update slide 01 metrics`
- `Refine slide 02 bug story`
- `Refresh slide 03 ticketing data`

For pull requests, include:

- a short summary of the narrative or visual change
- the data source updated or introduced
- a screenshot when the layout changes
- any open issue around copy, branding, or data interpretation
