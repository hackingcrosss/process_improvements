---
name: cv-synthesizer
description: Aggregate CV profile, job-match evaluation, consistency findings, and privacy findings into recruiter-facing reports under reports/<run-id>/.
---

# When to use

Use after CV evaluators have written their outputs under `analysis/<slug>/` and `findings/<slug>/`.

# Inputs

- `analysis/<slug>/cv-profile.json`
- `analysis/<slug>/cv-evaluation.json` if job matching was run
- `findings/<slug>/cv-*.json`
- optional job description content under `workdir/<job-slug>/content.md`

# Outputs

Write to `reports/<YYYY-MM-DD-HHMM>/`:

- `candidate-summary.md`
- `job-match-summary.md` when a job description/rubric is present
- `evidence-matrix.csv`
- `interview-questions.md`
- `privacy-notes.md` when privacy findings exist

# Procedure

1. Validate structured JSON against the CV schemas.
2. Summarize the candidate profile using only evidenced facts.
3. If a job evaluation exists, summarize must-have and nice-to-have matches.
4. Produce an evidence matrix with requirement → candidate evidence → confidence.
5. Produce interview questions focused on unclear or partial evidence.
6. Include privacy notes separately so sensitive data is not repeated in the main candidate summary.

# Guardrails

- Do not include protected characteristics in the main summary.
- Do not fabricate scores or ranks.
- Keep language neutral, job-relevant, and evidence-based.
