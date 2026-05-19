---
name: cv-privacy-review
description: Identify sensitive or hiring-irrelevant personal data in CV/resume artefacts and recommend redaction or exclusion from evaluation. Emits finding-style JSON conforming to schemas/finding.schema.json.
---

# When to use

Use after `document-ingest --domain cv` and preferably after `cv-profile-extractor`.

# Required reading

- `schemas/finding.schema.json`
- `workdir/<slug>/meta.json`
- `workdir/<slug>/content.md`
- `analysis/<slug>/cv-profile.json` when available

# Output

Write `findings/<slug>/cv-privacy-review.json` as a JSON array.

# Checks

Flag or redact, as appropriate:

- date of birth / age
- photograph reference
- marital/family status
- religion or political affiliation
- health/disability information
- full street address when city/country is enough
- national ID/passport/tax number
- salary history if not requested
- nationality/citizenship where not job-legally required

# Severity guidance

- `high`: special-category personal data or government IDs exposed.
- `medium`: sensitive personal information irrelevant to hiring.
- `low`: over-specific contact/location data.
- `informational`: privacy hygiene suggestion.

# Guardrails

- This evaluator is not a legal opinion.
- Do not delete source files. Only recommend redaction in reports or derived outputs.
- Do not use flagged sensitive attributes in `cv-job-match-review`.
