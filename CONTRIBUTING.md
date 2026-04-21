# Contributing to AI Wiki

Thanks for taking the time to contribute! This guide explains what kinds of contributions are welcome and how to get them merged with minimum friction.

## Table of Contents

- [Ground rules](#ground-rules)
- [Types of contributions](#types-of-contributions)
- [Before you open a PR](#before-you-open-a-pr)
- [Style guide](#style-guide)
  - [Prose](#prose)
  - [SVG diagrams](#svg-diagrams)
  - [Code blocks](#code-blocks)
  - [Chapter template](#chapter-template)
- [Running the URL validator](#running-the-url-validator)
- [Local development](#local-development)
- [Commit &amp; PR conventions](#commit--pr-conventions)
- [Code of conduct](#code-of-conduct)

---

## Ground rules

1. **Be specific.** A PR that says "improve chapter 07" with no further detail will bounce. Name the claim, cite a source, propose an edit.
2. **Cite primary sources.** Papers, docs, author blogs, official talks. Not Twitter hot takes. When the field is contested (see Vol III), include *both* sides.
3. **Verify URLs.** Every external link in the PR must resolve. Run the URL validator described below.
4. **No prompt injection.** This is a documentation site about AI, not an attack surface. Any hidden instructions targeting future AI readers will be rejected.
5. **Preserve the voice.** The prose is deliberately compact, opinionated where warranted, honest about uncertainty. See [Style guide — Prose](#prose).

---

## Types of contributions

| Type | Where | How |
|------|-------|-----|
| **Typo / grammar** | Any HTML or MD file | One-line PR. Merged fast. |
| **Broken link** | Any chapter `<a href="...">` | PR with the corrected URL, or strip the link if the source is truly gone. |
| **New primary source** | A chapter's `<details class="further">` block **and** the volume's `resources.html` | PR with link + one-sentence description of what the source covers. |
| **Factual correction** | Any chapter prose | Open an **issue** first with the primary source that contradicts the text; discuss; then PR. |
| **Additional chapter section** | An existing chapter | Open a **discussion** first to avoid duplicate work; PR if agreed. |
| **New chapter** | A volume | Open a **discussion**. Volumes have a deliberately fixed chapter count; new chapters usually require reshuffling adjacent ones. |
| **Translation** | New sibling folder (`AI-Wiki-II-es/` etc.) | Open a **discussion**; translations are welcome but have their own coordination problem. |
| **Use-case addition** | [`AI-Wiki-II/use-cases.html`](AI-Wiki-II/use-cases.html) | PR. Include a verifiable vendor or product and a maturity tag (`shipped` / `emerging` / `experimental`). |
| **New vocabulary term** | `vocabulary.html` in the relevant volume | PR. One-sentence definition, chapter reference. |

---

## Before you open a PR

1. Fork the repo, create a branch named after your change (`fix/chapter-07-bpe-link`, `content/ch05-graphrag-update`, …).
2. Make your change.
3. Run the URL validator (see below). No new broken links.
4. Open the page(s) you touched in a browser — both light and dark mode — and verify nothing renders badly.
5. Commit with a conventional message (see [Commit conventions](#commit--pr-conventions)).
6. Open the PR. In the description, say:
   - **What** the change is.
   - **Why** it is correct (with primary source if applicable).
   - **Where** in the wiki you touched (chapter numbers).

Small PRs merge faster. One focused change per PR.

---

## Style guide

### Prose

- **Short sentences.** Twenty words where thirty would do.
- **Active voice.** "Mamba replaces attention," not "attention is replaced by Mamba."
- **Concrete over abstract.** Name the paper, the company, the year. Use numbers when you have them.
- **No hedge-creep.** "May" once is fine; "may arguably potentially" is not.
- **Callouts for asides.** Use `<div class="callout tip|note|warn|danger">`. Use `<div class="callout.debate">` only in Vol III where the field is genuinely split.
- **Honest about uncertainty.** If a claim is debated, say so. If a model name is speculative, flag it. Better to say "we don't know yet" than to fake confidence.

### SVG diagrams

All diagrams are hand-authored SVG — no screenshots, no ASCII. If you add a diagram:

1. Use the shared palette only (see `assets/css/styles.css` `:root` block):
   `#7c5cff` (accent) · `#22d3ee` (cyan) · `#ff5ca8` (pink) · `#34d399` (green) · `#fbbf24` (yellow) · `#ff8a5c` (warm).
2. Wrap with `<div class="diagram">` + inline `<svg viewBox="...">` + `<span class="diagram-caption">`.
3. Use `font-family="-apple-system, Inter, sans-serif"` inside the SVG.
4. For depth, use the `<filter id="drop-shadow">` pattern already in Vol III chapters:
   `<feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity="0.35"/>`.
5. Gradients via `<linearGradient>` in `<defs>` — match the 4-stop gradient style used across the wiki.
6. Provide `role="img"` + `aria-label` on every `<svg>` for accessibility.

### Code blocks

- Python / Bash / JSON only in code blocks (those are the Prism languages loaded).
- `<pre><code class="language-python">...</code></pre>`.
- Runnable where possible. Stub imports rather than elaborate setup.
- Keep under 30 lines unless the reference implementation genuinely needs more.

### Chapter template

Every chapter follows this skeleton. Copy from an existing chapter in the same volume to preserve the exact markup:

```html
<header class="chapter-header">
  <div class="chapter-meta">
    <span class="chapter-num">CHAPTER 07</span>
    <span class="pill pill-cyan">Part II · Context &amp; Memory</span>
  </div>
  <h1>Chapter Title</h1>
  <p class="chapter-lede">One-paragraph elevator pitch.</p>
</header>

<!-- Vol III only -->
<div class="timeline-ribbon"> ... dated events ... </div>
<details class="eli5">
  <summary><span class="eli5-icon">🧒</span> ELI5 — explain like I'm five</summary>
  <div class="eli5-body"> ... </div>
</details>

<div class="toc">
  <h4>In this chapter</h4>
  <ul> ... anchor links ... </ul>
</div>

<!-- sections with h2 + id, at least one polished SVG diagram -->

<!-- Vol III only -->
<div class="debate-grid">
  <div class="debate-side pro"> ... </div>
  <div class="debate-side con"> ... </div>
</div>

<div class="open-questions">
  <h4>❓ Open questions</h4>
  <ul> ... </ul>
</div>

<details class="further">
  <summary>📚 Further learning — videos, papers, code</summary>
  <div class="further-body">
    <ul>
      <li><span class="kind paper">paper</span><a href="...">Title</a></li>
      <li><span class="kind video">video</span><a href="...">Title</a></li>
    </ul>
  </div>
</details>

<nav class="pager"> prev / next </nav>
```

Kind-pills supported: `paper · video · blog · talk · code · docs`.

---

## Running the URL validator

Every external link in every HTML file must resolve. Before opening a PR:

```bash
# from the repo root
python3 tools/url_validator.py
```

(The validator script used during the April 2026 review pass is committed to `tools/url_validator.py`. It uses a browser User-Agent and distinguishes truly-broken URLs from bot-protected-but-valid ones.)

If your PR introduces any URL returning a 4xx / 5xx / network error that is **not** the legitimate 403/429 bot-protection category, fix it before requesting review.

---

## Local development

```bash
git clone https://github.com/xD4O/AI-Wiki.git
cd AI-Wiki
python3 -m http.server 8000
# open http://localhost:8000
```

The site is static. Reload your browser after each file save. KaTeX math and Prism syntax highlighting load from a CDN, so you need a network connection the first time each page loads.

### Testing multiple volumes

- Vol I: `http://localhost:8000/`
- Vol II: `http://localhost:8000/AI-Wiki-II/`
- Vol III: `http://localhost:8000/AI-Wiki-III/`

All three share the same content-wide layout, but each has its own `assets/css/styles.css`. Vol III's CSS is a superset of Vol II's, which is a superset of Vol I's — if you're editing shared styles, consider which volume(s) need the update.

---

## Commit &amp; PR conventions

### Commit messages

Conventional Commits style — prefix with an intent:

```
fix: correct BPE failure example in Vol II Ch 03
content: add Contextual Retrieval note to Vol II Ch 05
feat: add use-cases domain for Insurance
docs: expand CONTRIBUTING with translation process
chore: refresh vault-mirror zip
```

### PRs

- **Title:** one line, imperative mood, max 72 chars.
- **Body:**
  - What changed.
  - Why it's correct (link to primary source for factual edits).
  - Which files touched.
  - Screenshot or diff snippet for visual changes.
- **One topic per PR.** Don't bundle a typo fix with a new chapter.

---

## Code of conduct

Be decent. This is a small personal project shared with the public. Constructive disagreement is welcome; personal attacks are not. The maintainer may close any issue or PR that violates basic civility without further discussion.

---

Questions? Open an issue or ping [@_cyr4x](https://x.com/_cyr4x). Thanks for contributing.
