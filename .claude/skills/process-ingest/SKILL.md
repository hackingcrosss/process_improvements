---
name: process-ingest
description: Convert a red team process artefact (.docx, .pdf, .pptx, .vsdx, .drawio, .png/.jpg/.svg) into a normalized form (markdown for prose / slide decks, JSON node-edge graph for diagrams, vision-extracted captions for images) under workdir/<artefact-slug>/. Run this before any evaluator skill.
---

# When to use

Use this skill as the first step when a user asks to evaluate a process document or diagram, or when called by `/evaluate`. Output is written to `workdir/<artefact-slug>/` and is consumed by all evaluator skills.

# Inputs and outputs

- **Input:** absolute path to a single artefact file (typically under `inputs/`).
- **Output directory:** `workdir/<artefact-slug>/` where `<artefact-slug>` is the input filename, lowercased, non-alphanumerics replaced with `-`.
- **Output files:**
  - `content.md` — normalized markdown for prose docs (preserve heading levels and lists).
  - `diagram.json` — `{ "nodes": [{id, label, kind?}], "edges": [{from, to, label?}], "groups": [{id, label, members:[...]}] }` for diagrams.
  - `captions.md` — for raster images, a vision-derived structured caption (actors, flows, trust boundaries, decision points).
  - `meta.json` — `{ "source_path", "doc_type_guess", "engagement_type_guess", "tooling_used", "warnings": [] }`.

`doc_type_guess` is one of: `methodology`, `engagement-sop`, `research-process`, `diagram`, `policy`, `template`, `unknown`.
`engagement_type_guess` is one of: `exercise`, `operation`, `threat-scenario`, `cross-cutting`, `unknown`.

# Procedure

1. **Resolve workdir.** Compute slug, create `workdir/<slug>/` if missing.
2. **Pick a path based on extension:**
   - `.docx` → run `python3 .claude/skills/process-ingest/docx_to_md.py <input> <workdir>` to produce `content.md`. If pandoc is available, prefer `pandoc -f docx -t gfm` and reconcile.
   - `.pptx` → run `python3 .claude/skills/process-ingest/pptx_to_md.py <input> <workdir>`. Output is `content.md` with one `## Slide N — <title>` section per slide in canonical presentation order, preserving bullet indent, tables, and speaker notes (rendered as `> **Notes:** ...` blockquotes). Images / charts / SmartArt are not extracted; their presence is marked `[image]` / `[chart-or-smartart]` so evaluators can tell a slide isn't text-only. Record in `meta.json.warnings` if a non-trivial fraction of slides have media-only content (an evaluator may want to do a vision pass on those).
   - `.pdf` → if `pdftotext` is available, use it; otherwise read the PDF with the Read tool (use `pages` for >10 pages) and write `content.md` from what you observe.
   - `.vsdx` → run `python3 .claude/skills/process-ingest/vsdx_to_graph.py <input> <workdir>`. Visio files are zipped XML.
   - `.drawio` / `.xml` → run `python3 .claude/skills/process-ingest/drawio_to_graph.py <input> <workdir>`. Drawio files are XML (sometimes mxfile-wrapped + base64-deflated). The script handles both.
   - `.png` / `.jpg` / `.jpeg` / `.svg` → use the Read tool on the image to view it, then write `captions.md` describing actors (boxes), flows (arrows with labels), trust boundaries (dashed lines / swimlanes), decision points (diamonds), and any text that looks like a phase name or codename. Be specific: `Actor "Red team operator" → Flow "submits TI request" → Actor "Threat intel cell"`.
3. **Classify.** After extraction, scan headings and key phrases to fill `meta.json`:
   - `engagement_type_guess`: look for "exercise", "OSINT", "APT simulation", "initial access" → exercise; "operation", "assumed breach", "scenario" without "blue team" → operation; "threat scenario", "blue team collaboration", "no stealth", "tool abuse", "GitLab", "Jenkins" → threat-scenario; methodology / framework docs that span all → cross-cutting.
   - `doc_type_guess`: methodology / engagement-sop / research-process / diagram / policy / template.
4. **Always write `meta.json`**, even on partial success — record any warnings (e.g. "pdf had embedded images, text-only extracted").
5. **Do not** invoke evaluator skills from here. Print a one-line summary: `ingest ok: <slug> [doc=<doc_type_guess>, engagement=<engagement_type_guess>]`.

# Edge cases

- Multi-language docs: extract verbatim, do not translate.
- Tracked changes in .docx: prefer the accepted text, mention pending revisions in `meta.json` warnings.
- Diagrams embedded inside .docx: emit `content.md` for the prose and a separate `diagram-<n>.json` per embedded diagram if you can extract them; otherwise note in warnings.
- Empty or unreadable file: write `meta.json` with `"warnings": ["unreadable"]` and exit cleanly.
