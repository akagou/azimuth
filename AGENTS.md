# AGENTS.md

## What Azimuth is

Azimuth is the reference implementation of the **context-first methodology**:
design-time governance for multi-agent workflows. It is not a runtime. It is a
declarative, portable, validated spec that defines workflow stages, agent
missions, human decision **gates**, **SME input packs** (typed expert
knowledge), and **evidence binding** (every claim cites a source) —
independent of the model or orchestrator that executes it.

## This repo, right now

Landing page only. The Python toolkit (`validate`, `dry-run`) and the
Consultant/discovery/compile skills are future phases. The PRD and design
specs live in `docs/`.

## Layout

```
index.html               # all markup + copy
styles.css               # all styling (tokens, type, layout, a11y)
assets/                  # vendored fonts (woff2), bearing mark, favicon
scripts/check_contrast.py# WCAG contrast verifier (stdlib)
.nojekyll                # GitHub Pages serves assets/ verbatim
LICENSE / NOTICE         # Apache-2.0 + attribution — do not alter (legal)
docs/                    # PRD, design specs, plans
```

## Develop

```
python3 -m http.server 8000   # then open http://localhost:8000
python3 scripts/check_contrast.py   # must exit 0 before shipping
```

## Deploy

Push to `main`. GitHub Pages serves the repo root at
`https://akagou.github.io/azimuth/`. No build step.

## Copy & voice rules

- Terse declaratives. One idea per line. Concrete nouns. Opinionated.
- Banned lexicon: unlock, seamless, empower, leverage, landscape, realm,
  dive/delve, elevate, robust, journey, game-changer, "in today's world".
- No metaphor inflation. No AI-template phrasing.

## Hard constraints

- Zero build step. No JS framework. No runtime dependencies.
- WCAG 2.1 AA — run `check_contrast.py`; keep visible focus + reduced-motion.
- Self-host fonts (no font CDN at runtime). Two faces max.
- Do not alter `LICENSE` or `NOTICE` without legal review.
- All asset paths relative (works under the `/azimuth/` Pages base path).
