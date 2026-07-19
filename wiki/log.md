# Wiki Log

Append-only timeline of wiki operations. Newest entries at the bottom.

Entry header format (mandatory, parseable by `grep "^## \[" wiki/log.md`):
`## [YYYY-MM-DD] <operation> | <short title>`

Allowed operations:
- `ingest` — a raw source was processed into wiki content.
- `query` — an answer was generated from wiki pages.
- `lint` — a health-check pass over wiki structure/content.
- `meta` — schema/index/log/structure maintenance.

---

## [2026-07-16] meta | Instantiate template for Phase 1B BRS
- Bound the wiki domain to the Phase 1B Bioregulatory Systems (BRS) medicine course at Imperial College London.
- Defined the study goal, scope boundary, primary tag `brs`, and medicine-specific entity and concept categories.
- Rewrote the project README and synchronized the domain shown in the wiki index.
- Created `raw/` and `wiki/` subfolders for sources and page types.
- Files touched: `AGENTS.md`, `README.md`, `.gitignore`, `wiki/index.md`, `wiki/log.md`, `raw/{pdfs,web-clips,notes,assets}/`, `wiki/{sources,entities,concepts,analyses}/`.

## [2026-07-16] meta | Add topic folders under raw/pdfs
- Created eleven topic subfolders under `raw/pdfs/` matching the Phase 1B BRS topic list.
- Updated `AGENTS.md` repository layout to document the topic folder structure.
- Files touched: `raw/pdfs/{cardiovascular-and-resp,dermatology,development-and-aging,endocrinology,gastroenterology,msk-and-rheumatology,neurology-and-neuroscience,pharmacology-and-therapeutics,population-health,psychiatry,urology-and-renal}/`, `AGENTS.md`, `wiki/log.md`.

## [2026-07-16] meta | Build HTML study site + Dev & Aging notes/Anki
- Created `site/` study hub: home page linking all 11 BRS topics; placeholder pages for empty topics.
- Built Development & Aging hub plus three lecture note pages with diagrams/tables from the ingested PDFs.
- Generated Anki decks (`.apkg`) for lectures 1.1–1.2, 1.3, and 1.4 under `site/anki/`.
- Files touched: `site/index.html`, `site/css/styles.css`, `site/topics/*`, `site/topics/development-and-aging/*`, `site/anki/*`, `README.md`, `wiki/log.md`.

## [2026-07-16] meta | Urology & Renal lecture notes + Anki
- Built Urology & Renal hub and five lecture note pages from PDFs 11.1, 11.2, 11.4, 11.7, and 11.10.
- Generated matching Anki decks under `site/anki/`; home page badge updated to “5 lectures ready”.
- Files touched: `site/topics/urology-and-renal/*`, `site/topics/urology-and-renal.html`, `site/index.html`, `site/anki/11.*.apkg`, `wiki/log.md`.

## [2026-07-16] meta | Full rebuild of all lecture pages and Anki decks
- Re-extracted all 8 lecture PDFs in reading order (fixes Notion column-jumbled text).
- Rebuilt every Development & Aging and Urology & Renal note page to include every Q&A and explanatory block from the PDFs.
- Regenerated all 8 Anki decks (~642 cards total) with full coverage.
- Card counts: 1.1–1.2 (86), 1.3 (34), 1.4 (61), 11.1 (109), 11.2 (87), 11.4 (100), 11.7 (55), 11.10 (110).
- Files touched: `site/topics/development-and-aging/*`, `site/topics/urology-and-renal/*`, `site/anki/*.apkg`, `site/_extracted/reading_order/*`, `wiki/log.md`.

## [2026-07-16] meta | MSK & Rheumatology lecture notes + Anki
- Built MSK & Rheumatology hub and four lecture note pages from PDFs 10.1, 10.2, 10.3, and 10.5.
- Generated matching Anki decks with full PDF Q&A coverage (358 cards total).
- Card counts: 10.1 (93), 10.2 (87), 10.3 (98), 10.5 (80).
- Files touched: `site/topics/msk-and-rheumatology/*`, `site/topics/msk-and-rheumatology.html`, `site/index.html`, `site/anki/10.*.apkg`, `site/_extracted/reading_order/msk-and-rheumatology__*`, `wiki/log.md`.

## [2026-07-16] meta | Dermatology lecture notes + Anki
- Built Dermatology hub and three lecture note pages from PDFs 9.1, 9.3, and 9.5.
- Generated matching Anki decks with full PDF Q&A coverage (294 cards total).
- Card counts: 9.1 (94), 9.3 (132), 9.5 (68).
- Files touched: `site/topics/dermatology/*`, `site/topics/dermatology.html`, `site/index.html`, `site/anki/9.*.apkg`, `site/_extracted/reading_order/dermatology__*`, `wiki/log.md`.

## [2026-07-16] meta | Neurology & Neuroscience lecture notes + Anki
- Built Neurology & Neuroscience hub and 16 lecture note pages from PDFs 3.2–3.17.
- Generated matching Anki decks with full PDF Q&A coverage (740 cards total).
- Card counts: 3.2 (59), 3.3 (20), 3.4 (48), 3.5 (5), 3.6 (114), 3.7 (12), 3.8 (53), 3.9 (3), 3.10 (153), 3.11 (10), 3.12 (42), 3.13 (2), 3.14 (30), 3.15 (8), 3.16 (168), 3.17 (13).
- Files touched: `site/topics/neurology-and-neuroscience/*`, `site/topics/neurology-and-neuroscience.html`, `site/index.html`, `site/anki/3.*.apkg`, `site/_extracted/reading_order/neurology-and-neuroscience__*`, `wiki/log.md`.

## [2026-07-16] meta | Psychiatry lecture notes + Anki
- Built Psychiatry hub and nine lecture note pages from PDFs 6.2–6.10.
- Generated matching Anki decks with full PDF Q&A coverage (593 cards total).
- Card counts: 6.2 (45), 6.3 (92), 6.4 (67), 6.5 (48), 6.6 (52), 6.7 (55), 6.8 (97), 6.9 (51), 6.10 (86).
- Files touched: `site/topics/psychiatry/*`, `site/topics/psychiatry.html`, `site/index.html`, `site/anki/6.*.apkg`, `site/_extracted/reading_order/psychiatry__*`, `wiki/log.md`.

## [2026-07-16] meta | Cardiovascular & Resp lecture notes + Anki
- Built Cardiovascular & Resp hub and 16 lecture note pages from PDFs 7.2–7.20 (available set).
- Generated matching Anki decks with full PDF Q&A coverage (1175 cards total).
- Card counts: 7.2 (69), 7.3 (85), 7.4 (17), 7.5 (93), 7.6 (132), 7.7 (102), 7.8 (109), 7.9 (19), 7.10 (113), 7.11 (164), 7.12 (62), 7.13 (92), 7.15 (13), 7.16 (73), 7.18 (30), 7.20 (2).
- Files touched: `site/topics/cardiovascular-and-resp/*`, `site/topics/cardiovascular-and-resp.html`, `site/index.html`, `site/anki/7.*.apkg`, `site/_extracted/reading_order/cardiovascular-and-resp__*`, `wiki/log.md`.

## [2026-07-16] meta | Gastroenterology lecture notes + Anki
- Built Gastroenterology hub and eight lecture note pages from available PDFs 8.1–8.14.
- Generated matching Anki decks with full PDF Q&A coverage (653 cards total).
- Card counts: 8.1 (107), 8.2 (93), 8.4 (10), 8.6 (80), 8.8 (57), 8.10 (167), 8.13 (120), 8.14 (19).
- Files touched: `site/topics/gastroenterology/*`, `site/topics/gastroenterology.html`, `site/index.html`, `site/anki/8.*.apkg`, `site/_extracted/reading_order/gastroenterology__*`, `wiki/log.md`.

## [2026-07-16] meta | Endocrinology lecture notes + Anki
- Built Endocrinology hub and 19 lecture note pages from PDFs 5.1–5.19.
- Generated matching Anki decks with full PDF Q&A coverage (876 cards total).
- Card counts: 5.1 (45), 5.2 (1), 5.3 (45), 5.4 (4), 5.5 (58), 5.6 (9), 5.7 (95), 5.8 (94), 5.9 (4), 5.10 (68), 5.11 (37), 5.12 (64), 5.13 (60), 5.14 (7), 5.15 (80), 5.16 (3), 5.17 (83), 5.18 (50), 5.19 (69).
- Files touched: `site/topics/endocrinology/*`, `site/topics/endocrinology.html`, `site/index.html`, `site/anki/5.*.apkg`, `site/_extracted/reading_order/endocrinology__*`, `wiki/log.md`.

## [2026-07-17] meta | Rename Anki decks to full lecture titles
- Renamed all 83 Anki deck files and internal deck names from short numeric labels to full lecture titles (e.g. `BRS::Endocrinology::5.1 Hypopituitarism`).
- Updated topic hub Anki download buttons and lecture page links to use the new filenames and show full topic names.
- Files touched: `site/anki/*.apkg`, `site/topics/*/index.html`, `site/topics/*/*.html`, `wiki/log.md`.

## [2026-07-17] meta | Add ALL DECKS zip download per topic
- Created ZIP bundles of every lecture Anki deck for each topic under `site/anki/bundles/`.
- Added an `ALL DECKS — {Topic}` button on every topic hub and lecture page.
- Files touched: `site/anki/bundles/all-decks-*.zip`, `site/topics/*/*.html`, `site/css/styles.css`, `wiki/log.md`.

## [2026-07-17] meta | Population Health lecture notes + Anki
- Built two Population Health note pages from the combined course PDF, covering every Q&A and explanatory block.
- Generated two matching Anki decks with 36 cards total (18 per lecture) and an all-decks ZIP bundle.
- Flagged and corrected the PDF's reversed QALY utility labels while preserving the source wording elsewhere.
- Files touched: `site/topics/population-health/*`, `site/index.html`, `site/anki/population-health-*.apkg`, `site/anki/bundles/all-decks-population-health.zip`, `site/_extracted/reading_order/population-health__7_Population_Health_BRS.txt`, `wiki/log.md`.

## [2026-07-17] meta | Pharmacology & Therapeutics lecture notes + Anki
- Built the Pharmacology hub and eight core-drug lecture note pages from PDFs 1.2, 1.4, 1.6, 1.8, 1.10, 1.12, 1.14, and 1.16.
- Per curator request, Anki decks are named by the disease treated (Diabetes, Parkinson's Disease, Depression, Hypertension, Asthma, GORD & Peptic Ulcer Disease, CKD, Pain) rather than the full lecture title; 208 cards total.
- Card counts: Diabetes (30), Parkinson's Disease (34), Depression (28), Hypertension (22), Asthma (20), GORD & Peptic Ulcer Disease (24), CKD (24), Pain (26).
- Added the all-decks ZIP bundle and updated the home page tile to “8 lectures ready”.
- Files touched: `site/topics/pharmacology-and-therapeutics/*`, `site/index.html`, `site/anki/{diabetes,parkinsons-disease,depression,hypertension,asthma,gord-peptic-ulcer-disease,ckd,pain}.apkg`, `site/anki/generate_pharmacology.py`, `site/anki/bundles/all-decks-pharmacology-and-therapeutics.zip`, `site/_extracted/reading_order/pharmacology-and-therapeutics__*`, `wiki/log.md`.

## [2026-07-17] meta | Add interactive practice questions
- Added a configurable practice page with topic, session length, and SBA, VSAQ, or SAQ selection.
- Built a lecture-derived bank containing 4,126 SBAs, 436 VSAQs, and 1,882 SAQs across ten available topics; VSAQ model answers are limited to four words.
- Added automatic SBA/VSAQ marking, model-answer SAQ self-marking, progress, scores, and results.
- Added a Practice Questions navigation link to every study page with a site header.
- Files touched: `site/practice.html`, `site/js/practice.js`, `site/js/practice-question-bank.js`, `site/css/styles.css`, `site/index.html`, `site/topics/**/*.html`, `wiki/log.md`.

## [2026-07-17] meta | Track practice question completion
- Added per-topic SBA, VSAQ, and SAQ counters showing unique questions completed against the available total.
- Persisted completion on the current browser and device so progress survives page refreshes and repeat sessions.
- Counted a question as completed when an SBA/VSAQ is submitted or an SAQ is self-marked, regardless of score.
- Files touched: `site/practice.html`, `site/js/practice.js`, `site/css/styles.css`, `wiki/log.md`.

## [2026-07-17] meta | Simplify homepage navigation
- Removed the Development & Aging shortcut from the homepage header, leaving only Topics and Practice Questions.
- Files touched: `site/index.html`, `wiki/log.md`.

## [2026-07-17] meta | Configure public GitHub Pages site
- Added a GitHub Actions workflow to deploy the generated `site/` directory to GitHub Pages on pushes to `main`.
- Added the public study-site URL to the README and excluded the accidental nested `Untitled/` repository from version control.
- Raw source documents remain local because `raw/` is gitignored.
- Files touched: `.github/workflows/pages.yml`, `.gitignore`, `README.md`, `wiki/log.md`.

## [2026-07-19] meta | Add downloadable lecture tracker spreadsheet
- Created an Excel tracker listing all 93 BRS Study Hub lectures across 11 topics, with Yes/No columns for notes made, 1st/2nd round Anki, and practice questions.
- Inserted blank spacer rows between topic blocks and added a homepage download button for the file.
- Files touched: `site/downloads/brs-lecture-tracker.xlsx`, `site/index.html`, `site/css/styles.css`, `wiki/log.md`.
