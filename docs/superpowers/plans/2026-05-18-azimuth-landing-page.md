# Azimuth Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a single hand-built static landing page for Azimuth on GitHub Pages at `https://akagou.github.io/azimuth/`, plus a small `AGENTS.md`.

**Architecture:** One `index.html` + one `styles.css` + vendored assets. No framework, no build step, no runtime dependencies. Optional ≤30-line inline progressive-enhancement JS. Deployed via GitHub Pages from `main` root.

**Tech Stack:** Static HTML5, hand-written CSS (custom properties), self-hosted Source Serif 4 woff2 (2 weights), system mono stack, inline SVG. Python stdlib only for verification scripts. `gh` CLI for Pages.

**Repo root (note the spaces — quote every path):** `/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth`

**Source spec:** `docs/superpowers/specs/2026-05-18-azimuth-landing-page-design.md`

---

## File Structure

| File | Responsibility |
|---|---|
| `index.html` | All page markup + copy. Semantic landmarks. |
| `styles.css` | All styling: tokens, type, layout, responsive, a11y. |
| `assets/serif-400.woff2`, `assets/serif-600.woff2` | Self-hosted Source Serif 4 (OFL). |
| `assets/azimuth-mark.svg` | Bearing mark — wordmark glyph + section marker. |
| `assets/favicon.svg` | Favicon (bearing mark). |
| `.nojekyll` | Pages serves `assets/` verbatim (no Jekyll). |
| `NOTICE` | Attribution (PRD compliance requirement). |
| `AGENTS.md` | Project orientation for agents/contributors. |
| `README.md` | Updated: one-liner + live URL + status. |
| `scripts/check_contrast.py` | Stdlib WCAG contrast verifier (dev-only, committed). |

`LICENSE` (Apache-2.0) and `.gitignore` already exist — do not alter `LICENSE`.

---

## Task 1: Repo scaffolding

**Files:**
- Create: `.nojekyll`
- Create: `NOTICE`
- Create: `assets/.gitkeep`
- Modify: `README.md`

- [ ] **Step 1: Create `.nojekyll` (empty file)**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
touch .nojekyll
mkdir -p assets && touch assets/.gitkeep
```

- [ ] **Step 2: Write `NOTICE`**

```
Azimuth
Copyright 2026 Azimuth contributors

This product includes software developed by the Azimuth project
(https://github.com/akagou/azimuth).

Licensed under the Apache License, Version 2.0. See LICENSE.

Bundled fonts:
- Source Serif 4 — Copyright 2014-2023 Adobe (https://github.com/adobe-fonts/source-serif),
  licensed under the SIL Open Font License 1.1.
```

- [ ] **Step 3: Overwrite `README.md`**

```markdown
# Azimuth

Context-first methodology — design-time governance for multi-agent workflows.

**Live:** https://akagou.github.io/azimuth/

Moving from automated to agentic is a design problem, not a runtime problem.
Azimuth is where you design the governance in — before the model, before the
orchestrator.

## Status

`azimuth/v1alpha` — pre-1.0, reference implementation. Breaking changes
possible until `v1`. Apache-2.0.

This repository currently hosts the landing page. The toolkit and Consultant
skill land next. See `docs/` for the PRD and design specs.

## Develop

```
python3 -m http.server 8000
```

Then open http://localhost:8000.
```

- [ ] **Step 4: Verify tree**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
ls -a && cat .nojekyll | wc -c
```
Expected: `.nojekyll`, `NOTICE`, `README.md`, `assets/` present; `.nojekyll` byte count `0`.

- [ ] **Step 5: Commit**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git add .nojekyll NOTICE assets/.gitkeep README.md
git commit -m "chore: scaffold landing page repo (nojekyll, NOTICE, README)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Vendor fonts and SVG assets

**Files:**
- Create: `assets/serif-400.woff2`
- Create: `assets/serif-600.woff2`
- Create: `assets/azimuth-mark.svg`
- Create: `assets/favicon.svg`
- Delete: `assets/.gitkeep`

- [ ] **Step 1: Download Source Serif 4 woff2 (pinned, OFL)**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth/assets"
curl -fsSL -o serif-400.woff2 "https://cdn.jsdelivr.net/npm/@fontsource/source-serif-4@5.2.5/files/source-serif-4-latin-400-normal.woff2"
curl -fsSL -o serif-600.woff2 "https://cdn.jsdelivr.net/npm/@fontsource/source-serif-4@5.2.5/files/source-serif-4-latin-600-normal.woff2"
rm -f .gitkeep
```

- [ ] **Step 2: Verify fonts downloaded and are woff2**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth/assets"
ls -l serif-400.woff2 serif-600.woff2
file serif-400.woff2
```
Expected: both files non-empty (>10 KB each); `file` reports `Web Open Font Format (Version 2)` or similar. If a download is empty/HTML, the pinned version path changed — try `@fontsource/source-serif-4@5/files/...` and re-verify.

- [ ] **Step 3: Write `assets/azimuth-mark.svg`** (bearing dial + accent needle at 38°)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" role="img" aria-label="Azimuth bearing mark">
  <circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="2"/>
  <g stroke="currentColor" stroke-width="2" stroke-linecap="round">
    <line x1="32" y1="6"  x2="32" y2="13"/>
    <line x1="32" y1="51" x2="32" y2="58"/>
    <line x1="6"  y1="32" x2="13" y2="32"/>
    <line x1="51" y1="32" x2="58" y2="32"/>
  </g>
  <line x1="32" y1="32" x2="48" y2="12" stroke="#5FB3A3" stroke-width="3" stroke-linecap="round"/>
  <circle cx="32" cy="32" r="3.5" fill="#5FB3A3"/>
</svg>
```

- [ ] **Step 4: Write `assets/favicon.svg`** (same mark, dark tile so it reads in light browser chrome)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="12" fill="#0E1418"/>
  <circle cx="32" cy="32" r="20" stroke="#D6E0E4" stroke-width="2.5" fill="none"/>
  <line x1="32" y1="32" x2="45" y2="16" stroke="#5FB3A3" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="32" cy="32" r="3" fill="#5FB3A3"/>
</svg>
```

- [ ] **Step 5: Commit**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git add assets/serif-400.woff2 assets/serif-600.woff2 assets/azimuth-mark.svg assets/favicon.svg
git rm --cached assets/.gitkeep 2>/dev/null; true
git commit -m "assets: vendor Source Serif 4 (OFL) + bearing mark and favicon

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Stylesheet

**Files:**
- Create: `styles.css`

- [ ] **Step 1: Write `styles.css`** (complete file)

```css
/* ===== Azimuth — instrument frame + manifesto voice ===== */
@font-face {
  font-family: "Source Serif 4";
  src: url("./assets/serif-400.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
}
@font-face {
  font-family: "Source Serif 4";
  src: url("./assets/serif-600.woff2") format("woff2");
  font-weight: 600; font-style: normal; font-display: swap;
}

:root {
  --ink: #0E1418;
  --surface: #11181C;
  --hairline: #243239;
  --text: #D6E0E4;
  --muted: #7E939B;
  --accent: #5FB3A3;
  --serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --mono: ui-monospace, "SF Mono", "Menlo", "Cascadia Mono", monospace;
  --maxw: 1080px;
  --readw: 640px;
}

*, *::before, *::after { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
}

body {
  margin: 0;
  background: var(--ink);
  color: var(--text);
  font-family: var(--serif);
  font-size: 18px;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
}

a { color: var(--accent); text-underline-offset: 3px; }
a:focus-visible, button:focus-visible, .btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.skip {
  position: absolute; left: -9999px; top: 0;
  background: var(--accent); color: var(--ink);
  padding: 10px 16px; font-family: var(--mono); font-size: 13px; z-index: 10;
}
.skip:focus { left: 12px; top: 12px; }

.wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 28px; }
.eyebrow {
  font-family: var(--mono); font-size: 12px; font-weight: 400;
  letter-spacing: .18em; text-transform: uppercase; color: var(--muted);
}
.section { border-top: 1px solid var(--hairline); padding: 84px 0; }
.section h2 {
  font-size: 14px; font-family: var(--mono); font-weight: 400;
  letter-spacing: .16em; text-transform: uppercase; color: var(--muted);
  margin: 0 0 36px; display: flex; align-items: center; gap: 12px;
}
.section h2 .mark { width: 18px; height: 18px; color: var(--muted); flex: none; }
.read { max-width: var(--readw); }

/* ---- top bar ---- */
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 22px 0; border-bottom: 1px solid var(--hairline);
}
.brand { display: flex; align-items: center; gap: 11px; font-weight: 600; font-size: 19px; color: var(--text); text-decoration: none; }
.brand .mark { width: 24px; height: 24px; color: var(--text); }
.nav { display: flex; align-items: center; gap: 26px; font-family: var(--mono); font-size: 13px; }
.nav a { color: var(--muted); text-decoration: none; }
.nav a:hover { color: var(--text); }
.nav a.gh { color: var(--text); }
@media (max-width: 680px) { .nav a:not(.gh) { display: none; } }

/* ---- hero ---- */
.hero { padding: 104px 0 96px; }
.hero .eyebrow { margin-bottom: 26px; }
.hero h1 {
  font-size: clamp(2.4rem, 6vw, 4rem); line-height: 1.08;
  font-weight: 600; letter-spacing: -.015em; margin: 0 0 24px; max-width: 16ch;
}
.hero p { font-size: clamp(1.05rem, 2vw, 1.3rem); color: var(--text); max-width: 52ch; margin: 0 0 40px; }
.cta { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
.btn {
  font-family: var(--mono); font-size: 14px; text-decoration: none;
  padding: 13px 22px; border-radius: 4px; display: inline-block;
}
.btn-primary { background: var(--accent); color: var(--ink); font-weight: 600; }
.btn-primary:hover { filter: brightness(1.08); }
.btn-ghost { color: var(--text); border: 1px solid var(--hairline); }
.btn-ghost:hover { border-color: var(--muted); }

/* ---- argument ---- */
.movement { margin-bottom: 44px; }
.movement .num {
  font-family: var(--mono); font-size: 13px; color: var(--accent);
  letter-spacing: .12em; display: block; margin-bottom: 10px;
}
.movement h3 { font-size: 1.5rem; font-weight: 600; margin: 0 0 12px; line-height: 1.25; }
.movement p { margin: 0; color: var(--text); }
.pull {
  border-left: 2px solid var(--accent); padding: 6px 0 6px 24px;
  font-size: 1.5rem; line-height: 1.4; color: var(--text);
  margin: 56px 0; max-width: var(--readw);
}
.footnote { font-family: var(--mono); font-size: 12.5px; color: var(--muted); margin-top: 40px; }
.footnote code { color: var(--text); }

/* ---- primitives ---- */
.grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: var(--hairline); border: 1px solid var(--hairline); }
@media (max-width: 760px) { .grid3 { grid-template-columns: 1fr; } }
.prim { background: var(--ink); padding: 32px 28px; }
.prim .label { font-family: var(--mono); font-size: 12px; letter-spacing: .14em; text-transform: uppercase; color: var(--accent); }
.prim h3 { font-size: 1.3rem; font-weight: 600; margin: 14px 0 12px; }
.prim p { margin: 0; font-size: 1rem; color: var(--text); }
.prim code { font-family: var(--mono); font-size: .9em; color: var(--text); background: var(--surface); padding: 1px 6px; border-radius: 3px; }

/* ---- adopt ---- */
.adopt .lead { font-size: 1.3rem; margin: 0 0 28px; }
.qs { list-style: none; margin: 0 0 28px; padding: 0; }
.qs li { padding: 16px 0; border-top: 1px solid var(--hairline); font-size: 1.15rem; }
.qs li:last-child { border-bottom: 1px solid var(--hairline); }
.adopt .close { color: var(--text); }
.adopt code { font-family: var(--mono); font-size: .92em; color: var(--accent); }

/* ---- status strip ---- */
.status { background: var(--surface); border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }
.status .wrap { padding-top: 40px; padding-bottom: 40px; }
.status p { font-family: var(--mono); font-size: 14px; line-height: 1.8; color: var(--muted); margin: 0; }
.status code { color: var(--text); }

/* ---- footer ---- */
footer { padding: 48px 0 64px; }
footer .row { display: flex; flex-wrap: wrap; gap: 24px; font-family: var(--mono); font-size: 13px; }
footer a { color: var(--muted); text-decoration: none; }
footer a:hover { color: var(--text); }
footer .copy { color: var(--muted); margin-top: 18px; font-family: var(--mono); font-size: 12px; }

/* ---- progressive fade-in (JS adds .reveal; gated by reduced-motion) ---- */
.reveal { opacity: 0; transform: translateY(12px); transition: opacity .6s ease, transform .6s ease; }
.reveal.in { opacity: 1; transform: none; }
```

- [ ] **Step 2: Lint CSS for unbalanced braces**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
python3 -c "s=open('styles.css').read(); print('braces balanced:', s.count('{')==s.count('}'), s.count('{'), s.count('}'))"
```
Expected: `braces balanced: True` with equal counts.

- [ ] **Step 3: Commit**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git add styles.css
git commit -m "feat: landing page stylesheet (instrument tokens, type, a11y)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: Page markup

**Files:**
- Create: `index.html`

- [ ] **Step 1: Write `index.html`** (complete file — copy verbatim from spec §4)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Azimuth — context-first methodology</title>
<meta name="description" content="Moving from automated to agentic is a design problem, not a runtime problem. Azimuth is where you design the governance in — before the model, before the orchestrator.">
<link rel="icon" href="./assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="./styles.css">
<meta property="og:title" content="Your agentic workflows are still just automation.">
<meta property="og:description" content="Azimuth — context-first methodology. Design-time governance for multi-agent workflows.">
<meta property="og:type" content="website">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<div class="wrap">
  <header class="topbar">
    <a class="brand" href="./">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 64 64" width="24" height="24" fill="none">
          <circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="3"/>
          <line x1="32" y1="32" x2="48" y2="12" stroke="#5FB3A3" stroke-width="4" stroke-linecap="round"/>
          <circle cx="32" cy="32" r="4" fill="#5FB3A3"/>
        </svg>
      </span>
      Azimuth
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="#argument">Argument</a>
      <a href="#primitives">Primitives</a>
      <a href="#adopt">Adopt</a>
      <a class="gh" href="https://github.com/akagou/azimuth">GitHub ↗</a>
    </nav>
  </header>
</div>

<main id="main">
  <section class="wrap hero">
    <p class="eyebrow">Azimuth · context-first methodology</p>
    <h1>Your agentic workflows are still just automation.</h1>
    <p>Moving from automated to agentic is a design problem, not a runtime problem. Azimuth is where you design the governance in — before the model, before the orchestrator.</p>
    <div class="cta">
      <a class="btn btn-primary" href="#argument">Read the argument →</a>
      <a class="btn btn-ghost" href="https://github.com/akagou/azimuth">View on GitHub</a>
    </div>
  </section>

  <section id="argument" class="section">
    <div class="wrap">
      <h2><span class="mark" aria-hidden="true"><svg viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="4"/><line x1="32" y1="32" x2="48" y2="12" stroke="#5FB3A3" stroke-width="5" stroke-linecap="round"/></svg></span>The argument</h2>
      <div class="read">
        <div class="movement reveal">
          <span class="num">i</span>
          <h3>The question you can't answer</h3>
          <p>Your CTO asks one thing: if the model makes a wrong call, can you show exactly why, and who approved it? Most agentic systems can't. The process is scattered across six Python files, two prompt templates, and a doc that went stale two months ago.</p>
        </div>
        <div class="movement reveal">
          <span class="num">ii</span>
          <h3>It's a design problem</h3>
          <p>Frameworks execute agent graphs well. None of them answer the questions that matter in a high-stakes workflow: what is the contract for each agent? Where must a human <em>decide</em> — not just approve? What domain knowledge has to exist before the workflow runs? You cannot bolt these onto a system that was never designed for them.</p>
        </div>
        <div class="movement reveal">
          <span class="num">iii</span>
          <h3>Governance is a file you author</h3>
          <p>Every other approach runs at inference time or after the fact — monitoring, guardrails, audit logs. Azimuth runs at design time. The context spec is written once and executes unmodified on any conformant runtime. Governance stops being a system you operate and becomes a file you author.</p>
        </div>
        <blockquote class="pull">The context stack survives every technology change because it was never about the technology.</blockquote>
        <p class="footnote">Prior art is documented honestly — see <code>docs/07-prior-art.md</code>. The novelty is naming and packaging the discipline, not claiming the parts are new.</p>
      </div>
    </div>
  </section>

  <section id="primitives" class="section">
    <div class="wrap">
      <h2><span class="mark" aria-hidden="true"><svg viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="4"/><line x1="32" y1="32" x2="48" y2="12" stroke="#5FB3A3" stroke-width="5" stroke-linecap="round"/></svg></span>Three primitives</h2>
      <p class="read" style="margin:0 0 36px;color:var(--text)">Three primitives, unified in one portable, validated spec. None of them is provided at design time by any runtime.</p>
      <div class="grid3">
        <div class="prim">
          <span class="label">SME Input Packs</span>
          <h3>Expert knowledge, typed</h3>
          <p>Domain knowledge as a typed, validated artifact: named answerer, role, evidence links, confidence rating, sign-off. Not a freeform prompt. Inspectable, versionable, auditable.</p>
        </div>
        <div class="prim">
          <span class="label">Gates</span>
          <h3>Typed contracts</h3>
          <p>Every workflow transition passes a gate that returns <code>PASS</code>, <code>FAIL</code>, or <code>ESCALATE</code> — owned by a named human role, with an explicit checklist. The workflow cannot advance on an agent's say-so.</p>
        </div>
        <div class="prim">
          <span class="label">Evidence binding</span>
          <h3>Structural audit trail</h3>
          <p>Every claim in every artifact cites a source: an upstream artifact section, a data tag, or a specific SME answer. The audit trail is structural, not optional.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="adopt" class="section adopt">
    <div class="wrap read">
      <h2><span class="mark" aria-hidden="true"><svg viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="26" stroke="currentColor" stroke-width="4"/><line x1="32" y1="32" x2="48" y2="12" stroke="#5FB3A3" stroke-width="5" stroke-linecap="round"/></svg></span>How adoption works</h2>
      <p class="lead">You never hand-write YAML. You talk to the Azimuth Consultant. It asks three questions:</p>
      <ul class="qs">
        <li>What decision does the workflow produce?</li>
        <li>Where must a human decide, with real judgment?</li>
        <li>What knowledge lives only in your domain experts?</li>
      </ul>
      <p class="close">The answers become a <strong>Context Design Document</strong> — prose your stakeholders can read. It compiles to a validated <code>context-spec.yaml</code> that any conformant runtime executes.</p>
    </div>
  </section>

  <section class="status">
    <div class="wrap">
      <p>Azimuth is <code>azimuth/v1alpha</code> — pre-1.0, a reference implementation. Breaking changes are possible until <code>v1</code>. Apache-2.0, patent grant included. This repository currently hosts the landing page; the toolkit and Consultant skill land next.</p>
    </div>
  </section>

  <footer class="wrap">
    <div class="row">
      <a href="https://github.com/akagou/azimuth">GitHub</a>
      <a href="https://github.com/akagou/azimuth/blob/main/LICENSE">Apache-2.0</a>
      <a href="https://github.com/akagou/azimuth/security/advisories">Security</a>
      <a href="https://github.com/akagou/azimuth/blob/main/docs">Prior art</a>
    </div>
    <p class="copy">© 2026 Azimuth contributors.</p>
  </footer>
</main>

<script>
(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.reveal').forEach(function (e) { e.classList.add('in'); });
    return;
  }
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(function (e) { e.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(function (e) { io.observe(e); });
})();
</script>
</body>
</html>
```

- [ ] **Step 2: Verify HTML well-formedness (tag balance via stdlib parser)**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
python3 - <<'PY'
from html.parser import HTMLParser
VOID={'meta','link','br','img','hr','input','area','base','col','embed','source','track','wbr'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.bad=[]
    def handle_starttag(s,t,a):
        if t not in VOID and t!='!doctype': s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        else: s.bad.append((t,list(s.st)))
p=P(); p.feed(open('index.html',encoding='utf-8').read())
print('unclosed:', p.st)
print('mismatched:', p.bad)
PY
```
Expected: `unclosed: []` and `mismatched: []`. (SVG self-closing tags like `<circle .../>` are fine — parser treats them as start tags with no matching end, but they are inside balanced `<svg>`; if `unclosed` lists only nothing, you're good. If it lists `svg`, a `<svg>` is missing `</svg>` — fix.)

- [ ] **Step 3: Commit**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git add index.html
git commit -m "feat: landing page markup and copy

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: Accessibility & contrast verification

**Files:**
- Create: `scripts/check_contrast.py`

- [ ] **Step 1: Write `scripts/check_contrast.py`** (stdlib WCAG 2.1 contrast calc)

```python
#!/usr/bin/env python3
"""WCAG 2.1 contrast check for Azimuth color tokens. Stdlib only."""

def lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def lum(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)

INK = "#0E1418"
SURFACE = "#11181C"
CHECKS = [
    ("text on ink",        "#D6E0E4", INK,     4.5),
    ("muted on ink",       "#7E939B", INK,     4.5),
    ("accent on ink",      "#5FB3A3", INK,     3.0),  # links: also underlined
    ("ink on accent btn",  "#0E1418", "#5FB3A3", 4.5),
    ("muted on surface",   "#7E939B", SURFACE, 4.5),
    ("text on surface",    "#D6E0E4", SURFACE, 4.5),
]
fail = False
for name, fg, bg, mn in CHECKS:
    r = ratio(fg, bg)
    ok = r >= mn
    fail |= not ok
    print(f"{'PASS' if ok else 'FAIL'}  {name:22s} {r:5.2f} (min {mn})")
raise SystemExit(1 if fail else 0)
```

- [ ] **Step 2: Run the contrast check**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
python3 scripts/check_contrast.py; echo "exit=$?"
```
Expected: every line `PASS`, `exit=0`. If `muted on ink` or `muted on surface` FAILs, lighten `--muted` toward `#8AA0A8` in `styles.css` and re-run until all pass, then re-commit `styles.css` with message `fix: bump muted token for WCAG AA`.

- [ ] **Step 3: Manual a11y spot-check (local preview)**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
python3 -m http.server 8000 >/dev/null 2>&1 & echo $! > /tmp/azimuth_srv.pid
sleep 1
curl -s -o /dev/null -w "%{http_code} %{size_download}b\n" http://localhost:8000/
curl -s -o /dev/null -w "css %{http_code}\n" http://localhost:8000/styles.css
curl -s -o /dev/null -w "font %{http_code}\n" http://localhost:8000/assets/serif-400.woff2
kill "$(cat /tmp/azimuth_srv.pid)" 2>/dev/null
```
Expected: `200` for page (size > 4000b), `css 200`, `font 200`.

- [ ] **Step 4: Open in a browser and confirm (human/visual)**

Open `http://localhost:8000` (re-run server if needed). Confirm: serif renders (not Times fallback), one teal accent only, focus ring visible when tabbing, nav anchor links scroll, mobile width (~375px) collapses nav to wordmark + GitHub, no horizontal scroll. Note any issue and fix in `styles.css`/`index.html` before committing.

- [ ] **Step 5: Commit**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git add scripts/check_contrast.py styles.css index.html
git commit -m "test: WCAG contrast verifier; a11y spot-check pass

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: AGENTS.md

**Files:**
- Create: `AGENTS.md`

- [ ] **Step 1: Write `AGENTS.md`**

```markdown
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
index.html              # all markup + copy
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
```

- [ ] **Step 2: Verify and commit**

Run:
```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
test -s AGENTS.md && echo "AGENTS.md ok"
git add AGENTS.md
git commit -m "docs: add AGENTS.md project orientation

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```
Expected: `AGENTS.md ok`.

---

## Task 7: Deploy to GitHub Pages

**Files:** none (push + Pages config)

- [ ] **Step 1: Push `main`**

```bash
cd "/Users/alex_goumans/Claude/My EPAM/Applied AI/azimuth"
git push origin main
```

- [ ] **Step 2: Enable GitHub Pages (source = main root)**

```bash
gh api -X POST repos/akagou/azimuth/pages \
  -f "source[branch]=main" -f "source[path]=/" 2>/dev/null \
  || gh api -X PUT repos/akagou/azimuth/pages \
       -f "source[branch]=main" -f "source[path]=/"
```
If both fail (HTTP 403 — token lacks Pages scope), enable manually:
GitHub → repo **Settings → Pages** → Source: **Deploy from a branch** →
Branch: `main` `/ (root)` → Save. Then continue.

- [ ] **Step 3: Wait for build, verify live**

Run:
```bash
for i in 1 2 3 4 5 6 7 8 9 10; do
  code=$(curl -s -o /dev/null -w "%{http_code}" https://akagou.github.io/azimuth/)
  echo "attempt $i: $code"
  [ "$code" = "200" ] && break
  sleep 20
done
curl -s https://akagou.github.io/azimuth/ | grep -o "still just automation" | head -1
curl -s -o /dev/null -w "css %{http_code}\n"  https://akagou.github.io/azimuth/styles.css
curl -s -o /dev/null -w "font %{http_code}\n" https://akagou.github.io/azimuth/assets/serif-400.woff2
```
Expected: a `200`, the grep prints `still just automation`, `css 200`, `font 200`. First Pages build can take 1–3 min; if still non-200 after the loop, wait and re-run Step 3.

- [ ] **Step 4: Final human confirmation**

Open `https://akagou.github.io/azimuth/` in a browser. Confirm serif loads, single accent, layout matches the local preview, no broken assets (DevTools console clean). Done.

---

## Self-Review

**Spec coverage:**
- Identity / visual system (spec §2) → Task 3 (tokens, type, mark), Task 2 (SVG/fonts) ✓
- Page structure §3 (hero, argument, primitives, adopt, status, footer) → Task 4 ✓
- Copy §4 verbatim → Task 4 ✓
- Tech/files §5 (.nojekyll, relative paths, no deps, optional JS) → Tasks 1,3,4 ✓
- WCAG AA §1/§8 → Task 5 (contrast script + manual) ✓
- AGENTS.md §6 → Task 6 ✓
- NOTICE / Apache-2.0 intact §5 → Task 1 (NOTICE), constraint stated in Task 6 ✓
- Deploy Pages default URL §5 → Task 7 ✓
- Out-of-scope §7 (no analytics/newsletter/multipage/toggle/backend) → nothing in plan adds these ✓

**Placeholder scan:** No TBD/TODO. All files have complete content. Security footer link resolves to repo Security Advisories (no email placeholder). ✓

**Type/name consistency:** CSS classes used in `index.html` (`reveal`, `prim`, `grid3`, `movement`, `qs`, `pull`, `footnote`, `status`, `btn-primary`, `btn-ghost`, `eyebrow`, `read`, `mark`, `skip`, `topbar`, `brand`, `nav`) all defined in Task 3 `styles.css`. JS targets `.reveal` / `.in` — both defined in CSS. Font-family `"Source Serif 4"` matches `@font-face` and vendored filenames `serif-400/600.woff2` (Task 2). ✓

No gaps. Plan ready.
