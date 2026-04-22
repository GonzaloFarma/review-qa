# Copilot Instructions for review-qa

This repository builds executive QA review slides for quarterly stakeholder presentations at Farmacity Group. The project prioritizes business-facing storytelling over technical dashboards.

## Project Context

**Purpose:** Help Gonzalo Estevez present QA team value through 2 slides (5–10 min oral review) to non-technical owners and sponsors.

**Constraints:**
- Review format: exactly 2 slides, 1440×840px canvas
- Audience: business stakeholders, not technical teams
- Language: concise Spanish, business-focused
- Tone: avoid Jira terminology; frame work as impact (prevention, risk reduction, confidence)

**Next review:** Friday, April 24, 2026.

## Source of Truth

- **Active context:** `docs/contexto/qa_review_context.md` — all narrative decisions and data caveats
- **Main dataset:** `docs/jira-cvs/Jira (Q1).csv` (covers 3 sprints in Q1)
- **Capacity dataset:** `docs/jira-cvs/Capacity (sprint 3).csv` (partial, complements main dataset)
- **Session decisions:** `AGENTS.md` — long-form repo guidelines, read when starting a session

Keep slide artifacts (HTML) at repo root. Store visual references in `docs/ejemplos-html/` only if reusable.

## Architecture & Key Conventions

### Project Structure

```
slider-01.html, slider-02.html
  ↓ (static HTML/CSS slides)
docs/
  ├── contexto/qa_review_context.md     (narrative + metric definitions)
  ├── jira-cvs/                         (operational data)
  ├── ejemplos-html/                    (visual reference fragments)
  └── notas.txt                         (unstructured brief)
scripts/
  └── q1_metrics.py                     (Jira CSV parsing and Q1 sprint extraction)
```

### HTML & CSS Patterns

- **2-space indentation** for all markup and styles
- **CSS tokens in `:root:`** for colors, fonts, shadows (see existing tokens in slider-01.html)
- **Semantic sectioning** with readable block structure
- **Lowercase kebab-case** for class names and filenames
- **Fonts:** Fraunces (display, serif) and IBM Plex Sans (body, sans-serif) via Google Fonts
- **Color palette:** navy (`--ink: #102247`), emerald (`#14936b`), cyan (`#0f8ea8`), amber (`#c88a16`), with soft variants
- **Canvas size:** 1440×840px, white background, no overflow

### Data Processing Pattern

The project uses Python for CSV parsing (`scripts/q1_metrics.py`):

- Reads Jira export from `docs/jira-cvs/Jira (Q1).csv`
- Sprint columns are duplicated (columns 136–145); read them together
- **Data caveat:** `Campo personalizado (Criticidad)` is empty; use `Prioridad` as severity proxy
- Date parsing: Spanish locale (ene, feb, mar, etc.) → ISO datetime
- Q1 sprint windows are hardcoded (Sprint 1: Jan 6–28, Sprint 2: Jan 29–Feb 18, Sprint 3: Feb 19–Mar 11)

If analyzing CSV directly in Python: import from `scripts/q1_metrics.py` or replicate the parsing logic.

### Copy & Narrative Rules

- **Translate Jira into business language:** bugs → "issues caught before production", QA tasks → "quality assurance activities", etc.
- **Avoid raw metrics without context:** don't show "187 bugs" without explaining what that prevented or improved
- **Metric definitions must align with `qa_review_context.md`** before appearing on a slide
- **Spanish only** in final slides; use business terminology, not tool-native wording

### Testing & Validation

There is no automated test suite. Validate slides manually before commit:

1. **Start local HTTP server** (required; Playwright CLI blocks direct `file://` access):
   ```bash
   python -m http.server 4173
   # or from WSL, expose to Windows:
   python3 -m http.server 4173 --bind 0.0.0.0
   ```

2. **Open slides in browser** at `http://localhost:4173/slider-01.html` (Windows) or `http://localhost:4173/slider-02.html`

3. **For layout changes, use Playwright CLI:**
   ```bash
   npm run pw:chrome
   ```
   This opens Chrome with local slide files; verify:
   - No overflow or clipped content at 1440×840
   - Typography, spacing, visual hierarchy match design
   - Color contrast is sufficient

4. **Verify data accuracy:**
   - Check metrics against `docs/jira-cvs/Jira (Q1).csv` and `docs/contexto/qa_review_context.md`
   - If metric changed, update context doc first

## Commands

| Task | Command |
|------|---------|
| List workspace files | `rg --files` |
| Review active context | `cat docs/contexto/qa_review_context.md` |
| Open slides in Chrome (with Playwright) | `npm run pw:chrome` |
| Start local HTTP server (Windows) | `python -m http.server 4173` |
| Start local HTTP server (WSL → Windows) | `python3 -m http.server 4173 --bind 0.0.0.0` |
| Check staging | `git status --short` |

## Commit & PR Guidelines

- **Commit messages:** short imperative form, e.g., `Refactor slide 01 executive layout`, `Add Q1 performance metrics`
- **Co-authored-by trailer:** always include `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`
- **PR description:** brief summary of narrative or visual change, data source(s) touched, screenshot if layout changed, any open interpretation issues

## Things to Watch For

- **Jira export quirks:** Sprint columns are duplicated; aggregate them when filtering by sprint
- **Severity confusion:** `Criticidad` field is empty; proxy with `Prioridad` and state this assumption explicitly in context
- **Metrics clarity:** "bugs avoided" is an inference unless a dedicated source field confirms it; frame carefully
- **CSV encoding:** file uses UTF-8 with BOM; Python parser handles this, but be explicit in other tools
- **Deprecated artifacts:** `slider-01.html` and `slider-02.html` are repurposed from an older project; reuse structure but replace old narrative
- **Two-slide constraint:** resist scope creep; all storytelling must fit 2 slides + 5–10 min oral delivery

## When to Update Documentation

If a session clarifies data definitions, identifies new data caveats, or establishes a new narrative direction, update `AGENTS.md` and `docs/contexto/qa_review_context.md` so future sessions inherit the decision.
