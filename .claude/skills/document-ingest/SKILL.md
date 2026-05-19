---
name: document-ingest
description: Domain-neutral ingestion for documents and diagrams. Converts supported source artefacts into normalized markdown, graph JSON, or image-caption placeholders under workdir/<artefact-slug>/, then writes meta.json with generic classification plus optional domain hints.
---

# When to use

Use this skill as the first step for any document-analysis domain: process reviews, CV/resume analysis, policy review, contract analysis, knowledge-base reconciliation, etc.

Domain evaluators must consume the normalized outputs from `workdir/<slug>/` rather than reading source files directly.

# Inputs and outputs

- **Input:** path to a single artefact file, usually under `inputs/`.
- **Optional domain hint:** `generic`, `process`, or `cv`. The domain hint affects classification and selection policy only; extraction remains generic.
- **Output directory:** `workdir/<artefact-slug>/`.
- **Output files:**
  - `content.md` — normalized markdown/text for prose docs, PDFs, slide decks, plain text, and markdown.
  - `diagram.json` — `{ "nodes": [...], "edges": [...], "groups": [...] }` for diagrams.
  - `captions.md.todo` — placeholder for image/OCR/vision processing when an image is ingested.
  - `meta.json` — domain-neutral metadata and classification.

# `meta.json` shape

```json
{
  "source_path": "...",
  "rel_path": "...",
  "slug": "...",
  "file_name": "...",
  "extension": ".docx",
  "content_files": ["content.md"],
  "requested_domain": "generic|process|cv",
  "doc_family_guess": "process|cv|governance|template|diagram|image|slide-deck|unknown",
  "document_kind_guess": "prose-document|slide-deck|diagram|image|unknown",
  "doc_type_guess": "free-form type, e.g. cv, job-description, methodology, engagement-sop",
  "domain_hints": {
    "process": {
      "doc_type_guess": "methodology|engagement-sop|research-process|diagram|policy|template|unknown",
      "engagement_type_guess": "exercise|operation|threat-scenario|cross-cutting|unknown"
    }
  },
  "engagement_type_guess": "process compatibility field; null outside process docs",
  "tooling_used": "...",
  "warnings": []
}
```

`doc_type_guess` and evaluator names are intentionally free-form. Domain-specific evaluators should validate against their own schemas.

# Procedure

1. **Select inputs** when running a batch:
   - Generic: `python3 .claude/skills/document-ingest/select_inputs.py inputs --domain generic`
   - Process: `python3 .claude/skills/document-ingest/select_inputs.py inputs --domain process`
   - CV: `python3 .claude/skills/document-ingest/select_inputs.py inputs --domain cv`
2. **Ingest one artefact:**
   - `python3 .claude/skills/document-ingest/ingest_one.py <path> --domain <domain>`
3. **Check `workdir/<slug>/meta.json`**. If there are warnings, pass them through to the evaluator or final report.
4. **Do not invoke domain evaluators from ingest.** Ingest only normalizes content and classifies.

# Extraction behavior

- `.docx` → `content.md` via `docx_to_md.py`.
- `.pptx` → `content.md` via `pptx_to_md.py`; one section per slide.
- `.pdf` → `content.md` via `pdftotext` if installed; otherwise warning only.
- `.drawio` / `.xml` → `diagram.json` via `drawio_to_graph.py`.
- `.vsdx` → `diagram.json` via `vsdx_to_graph.py`.
- `.md` / `.markdown` / `.txt` → copied to `content.md`.
- `.png` / `.jpg` / `.jpeg` / `.svg` → creates `captions.md.todo`; a future OCR/vision pass should populate `captions.md`.

# Domain boundaries

This skill must stay domain-neutral:

- It may guess that a file looks like a CV, process document, policy, template, diagram, etc.
- It must not decide whether a CV is a good candidate, whether a process is compliant, or whether a policy is adequate.
- It may place domain-specific hints under `domain_hints`, but evaluators own authoritative interpretation.

# Compatibility

The existing `process-ingest` skill is now a compatibility wrapper around this generic layer. Existing process evaluators can still read top-level `doc_type_guess` and `engagement_type_guess` from `meta.json`.
