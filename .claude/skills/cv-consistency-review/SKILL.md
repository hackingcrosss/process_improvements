---
name: cv-consistency-review
description: Review an extracted CV profile for chronology, evidence, formatting, and claim-consistency issues. Emits finding-style JSON conforming to schemas/finding.schema.json.
---

# When to use

Use after `cv-profile-extractor` has written `analysis/<slug>/cv-profile.json`.

# Required reading

- `schemas/finding.schema.json`
- `schemas/cv/cv-profile.schema.json`
- `analysis/<slug>/cv-profile.json`
- `workdir/<slug>/content.md` for evidence checks when needed

# Output

Write `findings/<slug>/cv-consistency-review.json` as a JSON array.

# Checks

- Missing or ambiguous dates for roles or education.
- Overlapping full-time roles that are not explained.
- Employment gaps that are visible from provided dates. Report as an interview clarification, not as a negative conclusion.
- Seniority claims unsupported by role scope or evidence.
- Skills listed without any usage evidence in experience/projects.
- Inconsistent names, emails, phone numbers, locations, company names, or role titles across a candidate bundle.
- Extraction-quality issues caused by unreadable PDF, OCR failure, or multi-column layout.

# Severity guidance

- `high`: contradiction that could materially affect hiring/recruiting decisions.
- `medium`: ambiguity needing recruiter or interview clarification.
- `low`: formatting/normalization issue.
- `informational`: useful clarification question or extraction caveat.

# Guardrails

- Do not penalize career breaks, parental leave, illness, unemployment, or gaps. Phrase neutrally: "clarify timeline".
- Do not infer age from graduation dates or use it in recommendations.
- Do not make credibility accusations; use evidence-based wording only.
