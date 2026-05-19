---
description: Run a domain-configured document analysis pipeline.
argument-hint: "<domain> [<filename in inputs/> | all] [--job-description <path>]"
---

# /analyze

Run the generic document-analysis pipeline using a domain config from `.claude/domains/<domain>.json`.

Examples:

- `/analyze process all`
- `/analyze cv inputs/candidates/alice-cv.pdf --job-description inputs/jobs/security-engineer.md`
- `/analyze generic all` for ingest-only normalization.

## Argument handling

1. Parse the first token as `domain`. If omitted, use `generic`.
2. Load `.claude/domains/<domain>.json` before doing any work.
3. If the remaining argument is empty or `all`, run that domain's selector command.
4. Otherwise treat the remaining non-option token as a single input path and ingest exactly that file.
5. Preserve domain-specific options, e.g. `--job-description`, for evaluator skills.

## Generic pipeline

For each selected artefact:

1. **Ingest.** Use `document-ingest` with the domain hint from the config. Wait for `workdir/<slug>/meta.json`.
2. **Run domain evaluators.** Run each evaluator listed in `evaluators[]`. Evaluators are independent unless their skill docs say otherwise.
3. **Validate outputs.** Validate any finding-like JSON arrays against `schemas/finding.schema.json`; validate structured domain products against their domain schemas.

After all artefacts:

4. **Run corpus evaluators** listed in `corpus_evaluators[]`, if any.
5. **Run synthesizer** listed in `synthesizer`, if any.
6. **Print a closing summary** with processed artefacts, output paths, validation failures, and selector exclusions/unsupported formats.

## Domain configs

Domain configs live under `.claude/domains/` and define:

```json
{
  "domain": "cv",
  "selector": { "script": ".claude/skills/document-ingest/select_inputs.py", "args": ["inputs", "--domain", "cv"] },
  "ingest": { "script": ".claude/skills/document-ingest/ingest_one.py", "args": ["--domain", "cv"] },
  "evaluators": ["cv-profile-extractor", "cv-consistency-review"],
  "corpus_evaluators": [],
  "synthesizer": "cv-synthesizer"
}
```

## Operational rules

- Do not modify files in `inputs/`.
- All scratch and normalized content belongs in `workdir/`.
- Machine-readable evaluator output belongs in domain-specific subdirectories under `findings/` or `analysis/`.
- User-facing reports belong in `reports/<run-id>/`.
- Domain evaluators must not assume the input family solely from filenames; always check `meta.json` and the normalized content.
