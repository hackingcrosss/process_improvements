---
description: Run the full process-evaluation pipeline (ingest -> evaluators -> synthesize) on one or all artefacts in inputs/.
argument-hint: "[<filename in inputs/> | all]"
---

# /evaluate

You are running the Euronext red team **process evaluation pipeline**.

## Argument handling

- If `$ARGUMENTS` is empty or `all`, build the candidate list by running `python3 .claude/skills/process-ingest/select_inputs.py inputs` and parsing the JSON output. Evaluate everything in `selected[]`.
- Otherwise treat `$ARGUMENTS` as a single filename inside `inputs/` and evaluate **exactly** that file — selection rules do not apply when a specific file is named.

## Selection rules (applied in `all` mode only)

The `select_inputs.py` helper enforces two project-level rules:

1. **Format preference:** for the same logical document, `.docx` wins over `.pdf` (the .docx carries headings/lists/tables the evaluators rely on).
2. **Version selection:** only the highest version is kept (e.g. `v2.0` over `v1.0`). Versions are detected at the end of the filename in patterns like `name v1.0`, `name_V2`, `name (1.0)`.

Other formats (`.vsdx`, `.drawio`, images) are independent groups and don't compete with prose docs.

The helper also returns `excluded[]` with a reason per dropped file. **Always include this list in the closing summary** so the user can spot a misnamed or surprisingly-excluded artefact.

## Pipeline (per artefact)

For each artefact:

1. **Ingest.** Invoke the `process-ingest` skill. Wait for `workdir/<slug>/meta.json` to be written. If the ingest reports unrecoverable failure, record it and skip the evaluators for this artefact.

2. **Run evaluators in parallel** (independent — emit them in a single message with multiple tool calls):
   - `engagement-lifecycle-review`
   - `tiber-dora-alignment`
   Each writes its JSON array under `findings/<slug>/`.

3. **Validate** each evaluator's output against `schemas/finding.schema.json`. Move any invalid entries to `findings/<slug>/_invalid.json` with a `reason` field; do not block the pipeline.

## After all artefacts are processed

4. **Corpus-level coherence.** Invoke the `corpus-coherence` skill **once** over the whole `workdir/`. It writes `findings/_corpus/corpus-coherence.json` and, in bootstrap mode, a draft vocabulary at `workdir/_coherence/corpus_vocabulary.yaml`. Validate its output against the schema (move invalid entries to `findings/_corpus/_invalid.json`). The skill auto-selects mode based on whether `references/corpus_vocabulary.yaml` exists and is curated.

5. **Synthesize.** Invoke `findings-synthesizer` to produce `reports/<YYYY-MM-DD-HHMM>/` with:
   - `executive-summary.md`
   - `findings-register.csv`
   - `remediation-backlog.md`
   - `themes.md`

6. **Print a closing summary to the user**: number of artefacts processed, finding counts by severity, the run id, the path to the executive summary, the count of corpus-coherence findings (and the mode — curated vs bootstrap), and — if any inputs were filtered out by the selection rules — a one-line-per-file list of `excluded[]` with the reason. Cap at ~15 lines.

## Operational rules

- **Do not** modify files in `inputs/` — they are source-of-truth.
- All scratch belongs in `workdir/` and `findings/`. Final user-facing outputs go in `reports/`.
- If `references/euronext-internal-taxonomy.md` is still the placeholder, evaluators should avoid `EURONEXT-INTERNAL` framework_refs and prefer external anchors (TIBER-EU, DORA-TLPT, MITRE-ATT&CK, PTES). Mention this in the executive summary as an action item.
- If an evaluator skill is added later (e.g. `roe-authorization-review`), update step 2 to invoke it. The synthesizer is already evaluator-agnostic.
- Maximize parallelism between evaluators within an artefact and between independent artefacts. Do **not** parallelize ingest and its own evaluators — evaluators depend on ingest output.
