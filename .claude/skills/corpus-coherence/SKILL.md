---
name: corpus-coherence
description: Cross-document consistency checks across the entire ingested corpus in workdir/. Role-agnostic: detects naming drift, acronym conflicts, undefined terms, phase mismatches, RACI conflicts, broken cross-references, version misalignments, and orphan actors. Runs once per evaluation pass over all artefacts. Soft-finding (informational) mode pre-curation; severity-graded mode once references/corpus_vocabulary.yaml is curated. Emits findings JSON files conforming to schemas/finding.schema.json.
---

# When to use

Run **once** per evaluation pass, **after** `process-ingest` has produced `workdir/<slug>/` for every artefact in the run and **after** all per-artefact evaluators have written their findings. This skill operates across the whole corpus, not per artefact. Write findings to `findings/_corpus/corpus-coherence.json` as a JSON array.

# Required reading before evaluating

- `schemas/finding.schema.json` — output contract. Every finding must validate against it; `evaluator: "corpus-coherence"`.
- `workdir/*/meta.json` — enumerates artefacts in this run.
- `workdir/*/content.md`, `workdir/*/diagram.json`, `workdir/*/captions.md` (whichever exist) — the corpus content.
- `references/corpus_vocabulary.yaml` — curated ground truth (may not exist on first run).
- `references/euronext-internal-taxonomy.md` — internal control IDs (placeholder for now).

# Modes (picked automatically)

- **Curated mode** — `references/corpus_vocabulary.yaml` exists and `status` is not `draft` or `placeholder`. The yaml is ground truth. Drift against curated entries → severity per the table below. Drift on entities not yet in the yaml → `informational`.
- **Bootstrap mode** — no curated yaml (or it is still draft/placeholder). All findings emitted as `informational`. Write a draft vocabulary to `workdir/_coherence/corpus_vocabulary.yaml` for the user to curate and promote.

Never write to `references/` — that path is curated by the user only.

# Procedure

1. **Enumerate the corpus.** List every `workdir/*/` with a `meta.json`. Record slug → meta + available content files. Skip `_coherence/` and any directory without `meta.json`.

2. **Extract candidate entities per artefact.** From `content.md` (prose) and `diagram.json` / `captions.md` (diagrams), pull:
   - **Teams / roles** — named teams or job titles ("Red Team Lead", "Threat Intelligence", "Purple Team", "Blue Team").
   - **Tools / systems** — products and platforms ("GitLab", "Jenkins", "Cobalt Strike", "BloodHound", internal SaaS names).
   - **Acronyms with their definitions** — patterns like `XYZ (Expansion)`, `XYZ: Expansion`, or definitions in glossary sections.
   - **Process phases** — numbered sections or named lifecycle steps ("Scoping", "OSINT", "Initial Access", "Purple-team close-out").
   - **RACI assignments** — sentences attributing responsible / accountable / approver roles to actors.
   - **Cross-references** — explicit pointers like "see §4.2 of <doc>", "Appendix B of <doc>", file names referenced in prose, hyperlinks present in diagrams.
   - **Version claims** — "the current v2.0 of <policy>", "per <doc> v1.1".

3. **Reconcile across artefacts.** For each category, cluster strings likely referring to the same entity (case differences, abbreviations, plural/singular, paraphrases).

   When `references/corpus_vocabulary.yaml` exists, apply curated entries as follows:

   - A corpus string matching `canonical` or any string in `acceptable_short_forms` → **no finding** (this is an allowed form).
   - A corpus string matching any string in `variants_to_reconcile` → emit a `naming_drift` finding rewriting it to `canonical`.
   - A corpus string close to but not matching either list (fuzzy cluster member) → emit a **low-confidence** drift candidate so the user can add it to `variants_to_reconcile` on the next curation pass.
   - For acronyms: use `canonical_expansion` as the correct meaning; emit `acronym_conflict` findings against any corpus use matching an entry in `non_canonical_uses`, using its `rewrite_to` hint in the recommendation.
   - **Backward-compat:** if an entry uses only the legacy `variants_seen` field (no `acceptable_short_forms` / `variants_to_reconcile` split), treat the entire `variants_seen` list as `variants_to_reconcile` and emit `naming_drift` findings accordingly.

4. **Run the checks.** For each cluster / pattern, apply the table below.

| Check | Trigger | Severity (curated mode) | Severity (bootstrap mode) | Category |
|---|---|---|---|---|
| `naming_drift` | ≥2 string variants for the same entity across ≥2 docs | medium (low if cosmetic only, e.g. casing) | informational | `naming-convention` |
| `acronym_conflict` | Same acronym expanded two different ways across docs | high | informational | `internal-inconsistency` |
| `undefined_term` | Term used in ≥2 docs, defined in none | low | informational | `ambiguity` |
| `phase_mismatch` | Same lifecycle described with different phase names or ordering across docs | high | informational | `internal-inconsistency` |
| `raci_conflict` | Same activity assigned A or R to different actors across docs | high | informational | `internal-inconsistency` |
| `broken_xref` | A cross-reference target (section, appendix, file) not found anywhere in the corpus | medium | informational | `missing-evidence` |
| `version_misalignment` | A doc references another doc without a version, and the corpus contains multiple versions of the referenced doc | low | informational | `ambiguity` |
| `orphan_actor` | Team/role appears in workflows but no charter / methodology / responsibility doc defines its remit | medium | informational | `completeness-gap` |

5. **Emit findings.** One finding per drift cluster (not per affected doc — list all variants in one finding's evidence). For each finding:

   - `finding_id`: `coherence-<primary-slug-short>-NNN` (zero-padded). Primary slug = the doc with the most authoritative/earliest occurrence; tie-break alphabetically.
   - `evaluator`: `"corpus-coherence"`.
   - `artefact.path`: the primary artefact's path under `workdir/`.
   - `artefact.doc_type`: from the primary artefact's `meta.json` if known, else `unknown`.
   - `artefact.engagement_type`: `"cross-cutting"`.
   - `section_ref`: section of the primary artefact where the variant first appears, or `null` for corpus-wide observations (e.g. `orphan_actor`).
   - `severity`: per the table above, modulated by mode.
   - `category`: per the table above.
   - `title`: ≤140 chars, name the conflict explicitly, e.g. `Naming drift: 'Red Team Lead' / 'RT Manager' / 'Head of Offensive Security' refer to the same role`.
   - `evidence.quote_or_observation`: enumerate every variant with `<slug>:<section_ref> -> "<exact quote>"`, separated by ` || `.
   - `evidence.expected`: curated mode → the canonical form from the yaml. Bootstrap mode → `"DRAFT — pending vocabulary curation"`.
   - `framework_refs`: at least one. Default `{ framework: "OTHER", ref: "internal corpus consistency" }`. Use `EURONEXT-INTERNAL` once `references/euronext-internal-taxonomy.md` is populated and a control id maps (e.g. codename convention → `RT-METH-*`).
   - `recommendation.text`: curated mode → `"Align all artefacts to '<canonical>'"`. Bootstrap mode → `"Decide canonical form and record in references/corpus_vocabulary.yaml"`.
   - `recommendation.effort`: `S` for naming/acronym/version drift; `M` for phase/RACI/xref reconciliation; `L` for `orphan_actor` (likely needs new doc).
   - `recommendation.owner_hint`: `"Red team lead"` by default. For taxonomy or RACI conflicts use `"Red team lead + relevant control owner"`.
   - `confidence`: `high` when curated yaml drives the call; `medium` for bootstrap inferences with clear clustering; `low` for fuzzy matches where it's unclear whether two strings refer to the same entity.

6. **Bootstrap mode only — write the draft vocabulary.** Write `workdir/_coherence/corpus_vocabulary.yaml` with the shape below. The user will curate, then copy to `references/corpus_vocabulary.yaml` to promote it to ground truth.

   ```yaml
   # DRAFT — generated by corpus-coherence on <YYYY-MM-DD>.
   # Curate canonicals, resolve conflicts, drop noise, then copy to references/.
   generated_at: <YYYY-MM-DD>
   status: draft

   teams_and_roles:
     - canonical: <best guess>
       variants_seen: ["<variant>", ...]
       sources: ["<slug>:<section_ref>", ...]
       confidence: high|medium|low

   tools_and_systems:
     - canonical: <best guess>
       variants_seen: [...]
       sources: [...]
       confidence: ...

   acronyms:
     - acronym: <ABC>
       expansions_seen:
         - { text: "<expansion 1>", sources: [...] }
         - { text: "<expansion 2>", sources: [...] }
       conflict: true|false

   phases:
     - lifecycle: <Exercise|Operation|Threat Scenario|cross-cutting>
       proposed_canonical: ["<phase 1>", "<phase 2>", ...]
       variants_seen_by_source:
         "<slug>": ["<phase as written>", ...]

   raci:
     - activity: <activity>
       proposed_responsible: <actor>
       proposed_accountable: <actor>
       conflicts_seen: ["<slug>:<section_ref> -> <actor as written>", ...]

   cross_references:
     - source: "<slug>:<section_ref>"
       target_text: "<as written>"
       resolved: true|false
       resolved_target: "<slug>:<section_ref>"  # when resolved

   versions_referenced:
     - target_doc_logical_name: <name>
       referenced_without_version_in: ["<slug>", ...]
       versions_present_in_corpus: ["<vX>", ...]

   orphan_actors:
     - actor: <name>
       appears_in: ["<slug>:<section_ref>", ...]
       defined_in: null
   ```

   If a section has no candidates, emit it as an empty list (do not omit it) so the structure is stable for diffing across runs.

# Curated vocabulary shape

When the user curates the draft and promotes it to `references/corpus_vocabulary.yaml`, entries typically evolve into the richer shape below. The bootstrap dumps everything into `variants_seen`; curation splits each entry into "allowed forms" and "drift to reconcile":

```yaml
status: curated   # any value other than "draft" / "placeholder" flips the skill into curated mode

teams_and_roles:
  - canonical: Blue Team
    acceptable_short_forms: ["BT"]                                # also OK in docs (canonical preferred on first reference)
    variants_to_reconcile: ["defenders", "defending teams"]       # drift — flag and rewrite
    sources: ["<slug>:<section_ref>", ...]
    confidence: high

tools_and_systems:
  - canonical: Cobalt Strike
    acceptable_short_forms: []
    variants_to_reconcile: ["CobaltStrike"]                       # vendor's spelling is two words
    sources: [...]
    confidence: high

acronyms:
  - acronym: PoC
    canonical_expansion: "Proof of Concept"
    non_canonical_uses:
      - text: "Point of Contact"
        rewrite_to: "spell out 'Point of Contact' on full reference, or use 'PoC contact' as a distinct shorthand"
        sources: [...]
    conflict: true
```

`phases`, `raci`, `cross_references`, `versions_referenced`, and `orphan_actors` retain the bootstrap shape — they don't have the variants problem.

The skill reads whichever shape it finds. An entry can be partially curated (some fields still in `variants_seen`, others split). Adding `acceptable_short_forms` / `variants_to_reconcile` to an entry overrides `variants_seen` if both are present.

# Anti-patterns to avoid

- Do **not** emit hard severities in bootstrap mode. The point of soft mode is to surface candidates without crying wolf before the user has curated the vocabulary.
- Do **not** write to `references/`. That directory is curated ground truth, never machine-written.
- Do **not** flag intra-document variation. A single doc using "RT Lead" in one paragraph and "Red Team Lead" in another is a per-artefact concern. This skill is corpus-level.
- Do **not** duplicate per-artefact evaluator findings. If `engagement-lifecycle-review` already flagged a missing codename inside one doc, only flag codename inconsistency *between* docs here.
- Do **not** treat short diagram labels (e.g. "RT" in a swimlane) as drift on their own — note them but rate `low` / cosmetic if the same diagram or its captions expand the term elsewhere.
- Do **not** invent canonicals for entities that appear in only one doc — single-doc terminology is vocabulary, not drift.
- Do **not** silently skip artefacts. If an artefact has no `content.md`, record it in the finding output (or in a `workdir/_coherence/skipped.txt`) so the user can see what was excluded from the corpus pass.
