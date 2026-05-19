---
description: Analyze one or more CV/resume artefacts using the CV domain pipeline.
argument-hint: "[<cv path in inputs/> | all] [--job-description <path>] [--rubric <path>]"
---

# /analyze-cv

Run the CV document-analysis pipeline. This is a convenience wrapper around `/analyze cv ...` using `.claude/domains/cv.json`.

## Pipeline

1. Ingest each CV/resume/cover-letter/job-description artefact with `document-ingest --domain cv`.
2. Run:
   - `cv-profile-extractor`
   - `cv-consistency-review`
   - `cv-privacy-review`
   - `cv-job-match-review` when a job description or rubric is provided
3. Validate against:
   - `schemas/cv/cv-profile.schema.json`
   - `schemas/cv/cv-evaluation.schema.json`
   - `schemas/finding.schema.json` for finding-style issues
4. Run `cv-synthesizer` to create a candidate-facing or recruiter-facing report under `reports/<run-id>/`.

## Guardrails

- Do not score or rank candidates using protected characteristics.
- Ignore or redact age, photo, marital status, religion, health/disability information, and exact home address unless the user explicitly asks for a privacy/redaction report.
- All job-fit claims must cite evidence from the CV, cover letter, portfolio, or job description.
- Missing evidence must be reported as `unclear`, not assumed negative.
