# Azimuth Landing Page — Design Spec

**Date:** 2026-05-18
**Status:** Approved (design); pending spec review
**Scope:** A single static landing page for GitHub Pages, plus a small `AGENTS.md`. No toolkit, skills, or validator code in this session — those are future phases.

---

## 1. Goal

Ship the methodology home for Azimuth (formerly Cairn): the context-first manifesto as a single, hand-built static page. It must be citable and credible *before* any toolkit ships (PRD risk mitigation: methodology-first brand). Provocation-first message. Production-grade design — not Lovable, not AI-template SaaS.

**Done when:**
- `index.html` + `styles.css` + assets render the page below
- Deployed via GitHub Pages at `https://akagou.github.io/azimuth/`
- WCAG 2.1 AA: contrast verified, semantic HTML, visible focus, `prefers-reduced-motion` honored
- Zero build step, zero JS framework, zero runtime dependencies
- `AGENTS.md` committed

---

## 2. Identity

Instrument frame + manifesto voice. A sharp argument set inside a precise engineering instrument. The name *azimuth* means a compass bearing — the bearing/needle motif is the logo and the recurring section marker.

### Visual system

| Token | Value | Use |
|---|---|---|
| `--ink` | `#0E1418` | Page background |
| `--surface` | `#11181C` | Cards, strips |
| `--hairline` | `#243239` | 1px rules, card borders |
| `--text` | `#D6E0E4` | Body text |
| `--muted` | `#7E939B` | Eyebrows, captions, labels |
| `--accent` | `#5FB3A3` | Needle, links, primary CTA — the **only** accent |

- No gradients, no glassmorphism, no drop-shadow stacks. Flat + hairline.
- Contrast: `--text` on `--ink` ≈ 11:1; `--muted` on `--ink` ≈ 4.7:1 (AA for ≥16px). Accent used for non-text-critical emphasis; link text underlined so color is not the only signal.
- Type: **two self-hosted woff2 faces, max.**
  - Mono — eyebrows, labels, code, status strip. (Self-host one; system mono fallback stack: `ui-monospace, "SF Mono", Menlo, monospace`.)
  - Serif — manifesto prose and headlines. Quality readable serif (e.g. Newsreader / Source Serif 4), self-hosted woff2. Fallback: `Georgia, serif`.
  - No Google Fonts CDN (privacy + offline + slop avoidance). `font-display: swap`.
- Motion: CSS only. Subtle fade/translate on scroll-in via IntersectionObserver is optional and gated behind `prefers-reduced-motion: no-preference`. No parallax, no autoplay.

### Bearing mark
Inline SVG: a thin circle, tick marks, one accent needle at ~38°. Used as: favicon, wordmark glyph beside "Azimuth", and a small repeated marker before each section heading. Single SVG, recolored via `currentColor`/accent.

---

## 3. Page structure

Single `index.html`. Sticky-free top bar (wordmark left, anchor links + GitHub right). Mobile: single column, nav collapses to wordmark + GitHub only (no hamburger JS needed).

1. **Hero**
2. **The argument** (editorial column, ~640px max-width)
3. **Three primitives**
4. **How adoption works**
5. **Status strip**
6. **Footer**

Anchor nav: `#argument`, `#primitives`, `#adopt`.

---

## 4. Copy (draft — redline freely)

Voice rules: terse declaratives, one idea per line, concrete nouns, opinionated. Banned lexicon: unlock, seamless, empower, leverage, landscape, realm, dive/delve, elevate, robust, journey, game-changer, "in today's world", em-dash-glued slot-fill. No metaphor inflation (no rail/shelf/load-bearing-as-adjective).

### Hero
> **Eyebrow:** AZIMUTH · context-first methodology
> **Headline:** Your agentic workflows are still just automation.
> **Sub:** Moving from automated to agentic is a design problem, not a runtime problem. Azimuth is where you design the governance in — before the model, before the orchestrator.
> **CTA primary:** Read the argument →
> **CTA secondary:** View on GitHub

### The argument

**i. The question you can't answer**
Your CTO asks one thing: if the model makes a wrong call, can you show exactly why, and who approved it? Most agentic systems can't. The process is scattered across six Python files, two prompt templates, and a doc that went stale two months ago.

**ii. It's a design problem**
Frameworks execute agent graphs well. None of them answer the questions that matter in a high-stakes workflow: What is the contract for each agent? Where must a human *decide* — not just approve? What domain knowledge has to exist before the workflow runs? You cannot bolt these onto a system that was never designed for them.

**iii. Governance is a file you author**
Every other approach runs at inference time or after the fact — monitoring, guardrails, audit logs. Azimuth runs at design time. The context spec is written once and executes unmodified on any conformant runtime. Governance stops being a system you operate and becomes a file you author.

> **Pull-quote:** The context stack survives every technology change because it was never about the technology.

*Footnote line (muted, small):* Prior art is documented honestly — see `docs/07-prior-art.md`. The novelty is naming and packaging the discipline, not claiming the parts are new.

### Three primitives
Section intro: Three primitives, unified in one portable, validated spec. None of them is provided at design time by any runtime.

1. **SME Input Packs** — Domain knowledge as a typed, validated artifact: named answerer, role, evidence links, confidence rating, sign-off. Not a freeform prompt. Inspectable, versionable, auditable.
2. **Gates as typed contracts** — Every workflow transition passes a gate that returns `PASS`, `FAIL`, or `ESCALATE` — owned by a named human role, with an explicit checklist. The workflow cannot advance on an agent's say-so.
3. **Evidence binding** — Every claim in every artifact cites a source: an upstream artifact section, a data tag, or a specific SME answer. The audit trail is structural, not optional.

### How adoption works
You never hand-write YAML. You talk to the Azimuth Consultant. It asks three questions:

- What decision does the workflow produce?
- Where must a human decide, with real judgment?
- What knowledge lives only in your domain experts?

The answers become a **Context Design Document** — prose your stakeholders can read. It compiles to a validated `context-spec.yaml` that any conformant runtime executes.

### Status strip
Azimuth is `azimuth/v1alpha` — pre-1.0, a reference implementation. Breaking changes are possible until `v1`. Apache-2.0, patent grant included. This repository currently hosts the landing page; the toolkit and Consultant skill land next.

### Footer
`GitHub` · `Apache-2.0` · `Security` (→ repo Security Advisories, no email needed) · `Prior art` · © 2026 Azimuth contributors.

---

## 5. Tech & files

```
azimuth/
├── index.html
├── styles.css
├── .nojekyll                # Pages serves assets/ verbatim, no Jekyll
├── assets/
│   ├── mono.woff2
│   ├── serif.woff2
│   ├── azimuth-mark.svg
│   └── favicon.svg
├── AGENTS.md
├── README.md                # updated: one-liner + live URL + status
├── LICENSE                  # existing Apache-2.0 (do not alter)
└── NOTICE                   # add: attribution file (PRD compliance req)
```

- All asset paths relative (`./styles.css`, `assets/...`) — works under the `/azimuth/` Pages base path.
- Optional JS: a single inline `<script>` for smooth-scroll + reduced-motion-gated fade-in. ≤30 lines, no file, no deps. Page is fully functional with JS disabled.
- `.nojekyll` required so Pages does not run Jekyll over `assets/`.
- Deploy: GitHub Pages, source = `main` branch, root. URL `https://akagou.github.io/azimuth/`. No custom domain (decided).

---

## 6. AGENTS.md (content outline)

Small, ~1 screen. Sections:
- **What Azimuth is** — one paragraph: context-first methodology, design-time governance for multi-agent workflows; the three primitives named.
- **This repo right now** — landing page only. Toolkit / Consultant skill are future phases. PRD lives at `docs/`.
- **Layout** — file tree (the one above).
- **Develop** — `python3 -m http.server` from repo root; open `http://localhost:8000`.
- **Deploy** — push to `main`; GitHub Pages serves root.
- **Copy & voice rules** — terse declarative, banned lexicon list, no AI-slop, one idea per line.
- **Hard constraints** — zero build, no JS framework/deps, WCAG 2.1 AA, keep `LICENSE`/`NOTICE` intact (legal — do not alter without review), self-host fonts.

---

## 7. Out of scope (YAGNI)

Analytics, newsletter/email capture, multi-page docs site, dark/light toggle, animation beyond fades, any backend, cookie banner, custom domain, the toolkit/skills/validator.

---

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Reads as generic dev-tool slop | Instrument identity + serif manifesto voice + self-hosted type; no gradient/glass; copy reviewed against banned lexicon |
| Pages base-path breaks assets | All relative paths; `.nojekyll`; verify deployed URL before "done" |
| Font flash / privacy | Self-host woff2, `font-display: swap`, system fallbacks |
| Accessibility miss (PRD NFR-A2 is AA) | Contrast tokens pre-checked; semantic landmarks; focus-visible; reduced-motion |
| Name/apiVersion drift (Cairn→Azimuth) | All spec/copy uses `azimuth/v1alpha`, `pip install azimuth` |
