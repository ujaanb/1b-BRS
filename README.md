# Phase 1B BRS Study Wiki

A personal study wiki for the Phase 1B Bioregulatory Systems (BRS) medicine course at Imperial College London. It integrates lectures, learning objectives, notes, and supporting sources into a cited, interconnected knowledge base for revision and assessment preparation.

## Study site

- **Public site:** [ujaanb.github.io/1b-BRS](https://ujaanb.github.io/1b-BRS/)
- Open [`site/index.html`](./site/index.html) locally for topic pages, lecture notes, practice questions, and Anki deck downloads.

## How to use it

1. Add one source at a time to the appropriate folder under `raw/`.
2. Ask the agent to ingest that source (wiki) and/or build lecture notes for the study site.
3. Review the takeaways before the agent writes or updates wiki pages.
4. Ask questions against the wiki; useful answers can be saved under `wiki/analyses/`.
5. Request a wiki health check periodically to identify gaps, stale claims, and broken links.

## Structure

```text
.
├── AGENTS.md           # operating schema and maintenance rules
├── README.md           # project introduction
├── docs/
│   └── LLM-WIKI.md     # reference description of the wiki pattern
├── raw/                # immutable source documents
│   └── pdfs/           # PDFs organised by BRS topic (see AGENTS.md)
├── site/               # HTML study hub (home + topic/lecture pages + Anki)
└── wiki/               # LLM-maintained knowledge pages
    ├── index.md        # canonical page catalog
    └── log.md          # append-only operation history
```

The domain and maintenance contract are defined in [`AGENTS.md`](./AGENTS.md). Start navigation from [`wiki/index.md`](./wiki/index.md).
