---
name: cv-job-match-review
description: Compare an extracted CV profile against a job description and/or hiring rubric. Emits schemas/cv/cv-evaluation.schema.json and optional finding-style gaps.
---

# When to use

Use after `cv-profile-extractor`. This evaluator requires at least one of:

- an ingested job-description artefact, or
- a rubric under `references/cv/hiring-rubrics/`.

# Required reading

- `schemas/cv/cv-profile.schema.json`
- `schemas/cv/cv-evaluation.schema.json`
- `analysis/<candidate-slug>/cv-profile.json`
- job description `workdir/<job-slug>/content.md` when supplied
- rubric YAML/JSON when supplied
- `references/cv/skills-taxonomy.yaml` when present

# Output

Write `analysis/<candidate-slug>/cv-evaluation.json`.

Optionally write `findings/<candidate-slug>/cv-job-match-review.json` for gaps or evidence issues that benefit from finding-style tracking.

# Procedure

1. Parse job requirements into:
   - must-have requirements
   - nice-to-have requirements
   - responsibilities
   - seniority/years guidance
   - domain/tooling/certification requirements
2. Match candidate evidence to each requirement.
3. For each requirement, mark one of:
   - `strong_match`
   - `partial_match`
   - `unclear`
   - `not_evidenced`
4. Cite evidence from the CV/cover letter/portfolio for every match.
5. Produce neutral interview questions for `partial_match`, `unclear`, and high-impact `not_evidenced` items.
6. Do not calculate a single opaque score unless the user provides an explicit rubric with weights.

# Guardrails

- Missing evidence is not proof of missing ability.
- Do not use protected characteristics or proxies.
- Do not rank candidates unless the user provides a validated, job-relevant ranking rubric.
- Keep recommendations phrased as hiring-process actions: screen, clarify, interview focus, or reject only if explicit must-have evidence is absent under the provided rubric.
