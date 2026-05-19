---
name: cv-profile-extractor
description: Extract a structured candidate profile from an ingested CV/resume, cover letter, or portfolio. Emits JSON conforming to schemas/cv/cv-profile.schema.json with evidence for important claims.
---

# When to use

Use after `document-ingest --domain cv` has produced `workdir/<slug>/meta.json` and `content.md` for a candidate artefact.

# Required reading

- `schemas/cv/cv-profile.schema.json`
- `workdir/<slug>/meta.json`
- `workdir/<slug>/content.md` or `captions.md` if present

# Output

Write `analysis/<slug>/cv-profile.json`.

# Procedure

1. Confirm the artefact type from `meta.json.doc_type_guess`: `cv`, `cover-letter`, `portfolio`, or `job-description`.
2. Extract only facts supported by the document. For every major item include evidence:
   - section/page/heading when available
   - exact quote or concise observation
3. Normalize dates to `YYYY-MM` when possible. Use `null` for current/present end dates.
4. Extract:
   - candidate identity and contact channels
   - links such as LinkedIn, GitHub, portfolio, publications
   - work experience with company, title, dates, location, summary, achievements, technologies
   - education
   - certifications
   - skills and tools
   - languages
   - projects/publications/awards if present
5. Record extraction uncertainty in `warnings[]`, not by inventing facts.
6. Do not infer protected characteristics or use them for evaluation.

# Anti-patterns

- Do not calculate candidate fit here. That belongs to `cv-job-match-review`.
- Do not treat missing data as a negative signal; mark it as missing/unclear.
- Do not expose unnecessary sensitive details beyond what is needed for the analysis product.
