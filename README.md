# AI Wiki

> A complete, visual guide to Artificial Intelligence — from first principles to the 2026 research frontier.
> **Three volumes · 43 chapters · 200+ diagrams · 500+ curated external references.**

<p align="center">
  <a href="index.html"><img alt="Volume I" src="https://img.shields.io/badge/Vol_I-Foundations-7c5cff?style=for-the-badge"></a>
  <a href="AI-Wiki-II/index.html"><img alt="Volume II" src="https://img.shields.io/badge/Vol_II-Agentic_Frontier-22d3ee?style=for-the-badge"></a>
  <a href="AI-Wiki-III/index.html"><img alt="Volume III" src="https://img.shields.io/badge/Vol_III-Research_Frontier-ff5ca8?style=for-the-badge"></a>
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-34d399">
  <img alt="Built-with" src="https://img.shields.io/badge/Built%20with-HTML_+_SVG-ff8a5c">
  <img alt="Year" src="https://img.shields.io/badge/Verified-April_2026-fbbf24">
</p>

---

## Table of Contents

- [What's inside](#whats-inside)
- [Quick start (view locally)](#quick-start-view-locally)
- [Folder structure](#folder-structure)
- [Design principles](#design-principles)
- [Contributing](#contributing)
- [Deploy on GitHub Pages](#deploy-on-github-pages)
- [License](#license)
- [Credits](#credits)

---

## What's inside

Three independent but cumulative volumes. Read in order if you're new; skip to Volume III if you already ship LLMs.

### Volume I — Foundations → Frontier LLMs · [read →](index.html)

Linear algebra through transformer architectures, training, alignment, and modern agents. Ten chapters.

| # | Chapter |
|---|---|
| 01 | Introduction to AI |
| 02 | Math Foundations |
| 03 | Machine Learning |
| 04 | Neural Networks |
| 05 | Deep Learning |
| 06 | NLP & Transformers |
| 07 | Large Language Models |
| 08 | Training & Fine-tuning |
| 09 | Alignment & RLHF |
| 10 | Agents & Frontier |

### Volume II — The Agentic Frontier · [read →](AI-Wiki-II/index.html)

The practitioner's toolkit: local models, prompting, RAG, MCP, agents, production. Twelve chapters.

| # | Chapter |
|---|---|
| 01 | From Chatbot to Agent |
| 02 | Local Models (Ollama & LM Studio) |
| 03 | The Art of Prompting |
| 04 | Context Engineering |
| 05 | Retrieval-Augmented Generation |
| 06 | Skills & Reusable Prompts |
| 07 | MCP — the Model Context Protocol |
| 08 | Agent Architectures |
| 09 | Multi-Agent Systems |
| 10 | Interpretability |
| 11 | Evals, Safety & Observability |
| 12 | Frontier 2026 & Capstone |

**Appendix:** [Resources](AI-Wiki-II/resources.html) · [Vocabulary](AI-Wiki-II/vocabulary.html) · [Use Cases by Domain (2026)](AI-Wiki-II/use-cases.html)

### Volume III — The Research Frontier · [read →](AI-Wiki-III/index.html)

The 2026 research map: post-transformer architectures, world models, reasoning, systems, open problems, AGI debates. Twenty-one chapters across six parts.

| Part | Chapters |
|------|---|
| **I · Architecture** | Post-Attention · Mamba & SSMs · BLT · Sparse Revolution |
| **II · World Models** | JEPA · Sora/Veo/Genie · Embodied · Model-Based RL |
| **III · Reasoning** | RL on Verifiable · Inference Compute · Memory/Titans · Faithfulness |
| **IV · Systems & Control** | Meta-Prompting · Orchestration · Deterministic Gates |
| **V · Open Problems** | Interp Frontier · Alignment · Benchmark Crisis |
| **VI · Big Picture** | AI for Science · Scaling Debates · Compute & AGI |

Every chapter ships with a collapsible ELI5 summary, a "Further Learning" box (videos · papers · talks · code), a timeline ribbon, and a side-by-side "Debate" callout where the field disagrees.

---

## Quick start (view locally)

No build step. This is static HTML with SVG diagrams and external CSS/JS (KaTeX + Prism via CDN).

```bash
git clone https://github.com/xD4O/AI-Wiki.git
cd AI-Wiki
python3 -m http.server 8000
# open http://localhost:8000
```

Or just open `index.html` in a browser for Vol I, `AI-Wiki-II/index.html` for Vol II, `AI-Wiki-III/index.html` for Vol III.

---

## Folder structure

```
AI-Wiki/
├── index.html                     Volume I home
├── resources.html                 Volume I resources
├── vocabulary.html                Volume I glossary
├── chapters/                      Volume I chapters 01–10
├── assets/css/styles.css          Volume I design system
├── assets/js/main.js              theme toggle, KaTeX renderer
│
├── AI-Wiki-II/                    Volume II — the practitioner book
│   ├── index.html
│   ├── resources.html
│   ├── vocabulary.html
│   ├── use-cases.html             AI use cases by domain, 2026
│   ├── chapters/                  chapters 01–12
│   └── assets/                    Vol-II CSS/JS (extends Vol I)
│
├── AI-Wiki-III/                   Volume III — the research book
│   ├── index.html
│   ├── resources.html
│   ├── vocabulary.html
│   ├── chapters/                  chapters 01–21
│   └── assets/                    Vol-III CSS/JS (extends Vol II; adds
│                                  collapsibles, debate grid, timeline ribbons)
│
├── docs/
│   └── plans/                     original planning docs (historical)
│       ├── VOLUME-II-PLAN.md
│       ├── VOLUME-II-PLAN.html
│       ├── VOLUME-III-PLAN.md
│       └── VOLUME-III-PLAN.html
│
├── tools/
│   └── url_validator.py           run before opening a PR
│
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── broken-link.md
│       ├── factual-correction.md
│       └── new-chapter.md
│
├── README.md                      this file
├── CONTRIBUTING.md                how to contribute
├── LICENSE                        MIT
└── .gitignore
```

Each volume is fully self-contained: you can host any one independently. The shared sidebar "Getting Started" block cross-links all three, so navigation works whether a visitor lands on Vol I, Vol II, or Vol III.

---

## Design principles

- **HTML-first.** No build system, no framework. Every page is readable in a plain browser, forever.
- **Professional diagrams only.** Every architectural concept is a hand-authored SVG with gradients, filters, and consistent palette. No ASCII art.
- **Short over long.** Intuition first, rigor second, history in asides.
- **Receipts.** Every non-obvious claim links to a primary source — paper, blog post, or author's talk.
- **Collapsible ELI5 + Further Learning** on every Vol III chapter, so you can switch registers mid-read.
- **Live-debate callouts** (Vol III) where the field disagrees, with both sides' strongest argument side-by-side.
- **Dark mode by default**, with a light-mode toggle persisted per-reader.
- **Accessible without a network** once the KaTeX/Prism CDN bundles are cached.

---

## Contributing

Contributions welcome. The scope ranges from a single typo-fix to a whole new chapter. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide, including:

- Chapter style guide (matching the existing voice)
- Diagram conventions (SVG palette, gradient defs, `.diagram` wrapper)
- URL-validator script (run before opening a PR — no dead links!)
- Where to propose new chapters vs. amendments to existing ones
- How to report factual errors (file an issue with the primary source)

**Quick types of contributions:**

| What | How |
|------|-----|
| **Typo or broken link** | Open a PR. One-line fixes get merged quickly. |
| **New primary source for a chapter** | PR the addition into the chapter's `<details class="further">` list and the volume's `resources.html`. |
| **Content correction** | File an issue with the primary source that contradicts the current text. |
| **New chapter proposal** | Open a **discussion** first — chapter slots are load-bearing. |
| **Translation** | Open a discussion. Translations can live in a sibling folder (`AI-Wiki-II-es/`, etc.). |
| **New use case in the 2026 list** | PR into [`AI-Wiki-II/use-cases.html`](AI-Wiki-II/use-cases.html). Include a verifiable vendor / product. |

---

## Deploy on GitHub Pages

This repo is ready to host on GitHub Pages without modification.

1. Push to `main`.
2. Repository → **Settings** → **Pages** → **Source: Deploy from a branch** → `main` / `(root)` → **Save**.
3. Wait ~1 minute; the site appears at `https://xd4o.github.io/AI-Wiki/`.

The three volumes become:

- Vol I — `https://xd4o.github.io/AI-Wiki/`
- Vol II — `https://xd4o.github.io/AI-Wiki/AI-Wiki-II/`
- Vol III — `https://xd4o.github.io/AI-Wiki/AI-Wiki-III/`

---

## License

MIT — see [LICENSE](LICENSE). You are free to use, modify, and redistribute, including commercially, provided attribution remains.

Embedded external materials (papers on arXiv, documentation, talks) are linked rather than re-hosted. Those works retain their original licenses — respect them.

---

## Credits

**Created by [Duy Dao](https://github.com/xD4O)** ([@_cyr4x](https://x.com/_cyr4x)).

Content co-authored with Anthropic's Claude (Opus 4.7 / 4.6, 1M-context) under interactive supervision. Every claim linked to a primary source has been validated; speculative items were removed during the April 2026 review pass.

If you find this useful, please ⭐ star the repo and share it. That's how small-project discovery works on GitHub.

---

<p align="center">
  <a href="https://github.com/xD4O/AI-Wiki"><strong>⭐ Star on GitHub</strong></a>
  &nbsp;·&nbsp;
  <a href="https://x.com/_cyr4x">@_cyr4x on X</a>
  &nbsp;·&nbsp;
  AI Wiki · April 2026
</p>
