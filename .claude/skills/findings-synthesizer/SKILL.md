---
name: findings-synthesizer
description: Aggregate per-evaluator findings JSON files in findings/<slug>/ (or across all artefacts) into an executive summary (markdown), a findings register (CSV), and a remediation backlog ranked by severity x effort. Deduplicates overlapping findings between evaluators and groups by theme.
---

# When to use

After all evaluators have written their JSON arrays under `findings/<slug>/*.json`. Can be run for a single artefact or for all.

# Inputs

- One or more files matching `findings/**/*.json`, each a JSON array of objects validating against `schemas/finding.schema.json`.

# Outputs

Write to `reports/<run-id>/`, where `<run-id>` is `YYYY-MM-DD-HHMM`:

- `executive-summary.md` — 1-2 page narrative for leadership: what was reviewed, headline themes, the top ~10 risks, and the recommended remediation sequence.
- `findings-register.csv` — one row per (deduped) finding with columns: `finding_id, evaluator(s), artefact, engagement_type, severity, category, title, evidence, expected, framework_refs, recommendation, effort, owner_hint, confidence`.
- `remediation-backlog.md` — findings grouped by recommended owner, sorted within each group by severity then effort (S before L). Each item is a one-line actionable bullet.
- `themes.md` — clusters of findings that point to the same underlying weakness (e.g. "weak handover from red to blue", "unclear authorization chain"). Each theme includes the contributing finding ids.

# Procedure

1. **Load all findings** into memory. Validate each against `schemas/finding.schema.json`. Drop invalid entries to a `reports/<run-id>/invalid-findings.json` file with the reason; do not silently ignore.

2. **Deduplicate.** Two findings are duplicates if:
   - Same artefact path AND same `section_ref` AND same `category`, OR
   - Substantially overlapping `title` + `evidence.quote_or_observation` (use a fuzzy match; when in doubt, keep both and merge in step 3).
   When merging, keep the highest severity, union the `framework_refs`, and record both evaluator names in a `merged_from` field of the register CSV.

3. **Cluster into themes.** Group findings whose recommendations would be addressed by the same remediation effort. Common themes to look for explicitly:
   - Authorization / RoE clarity
   - Engagement-type confusion (artefact mixes Exercise / Operation / Threat Scenario expectations)
   - Codename + theme convention gaps
   - Purple-teaming close-out weakness
   - Threat-hunt and IR-support coverage
   - Physical scope completeness
   - TIBER-EU / DORA TLPT misalignment
   - Reporting / remediation tracking
   - Diagram-narrative inconsistency

4. **Severity x effort prioritization.** Sort the backlog by:
   - Severity rank: critical(0) > high(1) > medium(2) > low(3) > informational(4)
   - Effort within severity: S(0) > M(1) > L(2)
   This produces an early-wins-first list. Quick critical fixes go first.

5. **Write the executive summary.** Required sections:
   - **Scope of review:** which artefacts, which evaluators ran, the run id and date.
   - **Headline themes:** 3-7 bullets, each citing finding-id evidence.
   - **Top risks (max 10):** title, severity, why it matters in one sentence, recommended owner.
   - **What's well-covered:** at least one paragraph noting strengths — leadership reports are more credible when they aren't all-negative.
   - **Recommended next steps:** quick wins this quarter, structural changes next quarter.
   - Keep it tight. Two pages max in rendered form.

6. **Write the CSV.** Be careful with newlines and commas in `evidence` — quote-and-escape per RFC 4180. Use UTF-8.

# Anti-patterns to avoid

- Do **not** invent findings that no evaluator produced.
- Do **not** soften severity to make the report look better.
- Do **not** drop a finding just because two evaluators raised similar things — merge with attribution instead.
- Do **not** emit empty themes; if a theme has 1 finding, fold it into a more general one or drop it.
