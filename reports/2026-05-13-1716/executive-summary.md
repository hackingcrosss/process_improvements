# Red team process evaluation — executive summary

**Run id:** `2026-05-13-1716`
**Date:** 2026-05-13
**Prior run:** `2026-05-12-1914` (one day earlier — comparison anchored against that baseline).

## Scope of review

- **Artefacts ingested:** 30 (12 with prose `content.md`, 8 drawio graphs, 1 jpg via vision captions, 2 stakeholder pptx decks, 7 PDFs that are duplicates of their .docx counterparts and produced no text extraction because `pdftotext` is not available on this host — flagged as an action item below).
- **Evaluators run:** `engagement-lifecycle-review`, `tiber-dora-alignment`, `corpus-coherence` (curated mode).
- **Curated vocabulary:** `references/corpus_vocabulary.yaml` (`status: CURATED`) — drove all severity-graded coherence findings.
- **Corpus state:** Threat Scenarios v1.6, Operations v1.5, Exercises v1.6, Purple_Teaming_Process v0.1 (new), PhysicalSocial v1.3, PhysicalSocial Questionnaire v1.2, RedTeam_Methodology v0.8, BloodHoundEnterprise v0.5, Research_Methodology v0.6. (Most docs moved 1–2 versions since the prior run.)

**Totals after dedup:** **107 findings** — 4 critical, 11 high, 37 medium, 34 low, 21 informational, across **9 themes**.

## Comparison to prior run

| Metric | 2026-05-12-1914 | 2026-05-13-1716 | Δ |
|---|---|---|---|
| Total findings | 54 | 107 | +53 |
| Critical | 5 | 4 | −1 |
| High | 9 | 11 | +2 |
| Medium | 24 | 37 | +13 |
| Low | 12 | 34 | +22 |
| Informational | 4 | 21 | +17 |
| Corpus-coherence findings | 12 | 8 | **−4** |

The apparent total increase is explained by:
- Two new artefacts the prior run did not cover (`PhysicalSocial_Questionnaire_Process_v1.2.docx`, `RedTeaming_v0.4.pptx`).
- Deeper coverage of `PhysicalSocial_Process_v1.3.docx` (which jumped from v1.1).
- Re-baselined `tiber-dora-alignment` findings against TIBER-EU v2 / DORA Art. 26-27 with more granular severity (low/informational drift previously rolled into medium).

The **critical band has tightened** — 4 of 5 prior criticals around Purple Teaming close-out are **closed** (Tier 1.1 landed across all four SOPs + new Purple Teaming doc); the surviving 4 criticals are now all the same shape: **Authorization chain / Rules of Engagement absent**. **Corpus coherence is materially better** — 8 of 12 prior coherence findings closed by the cleanup-pass.

## Headline themes

1. **Tier 1.2 (Authorization chain) has not yet started — owns all 4 criticals.** Every engagement SOP (TS v1.6, Ops v1.5, Ex v1.6, PhysSoc v1.3) and the methodology v0.8 lack a Rules of Engagement subsection naming sign-off owner, kill-switch, safe-words, abort criteria, and escalation contacts. Findings: `lifecycle-threatscenarios-003`, `lifecycle-operations-003`, `lifecycle-exercises-002`, `lifecycle-rtmeth-003`. The PhysSoc operator-safety variant (`lifecycle-physoc-002`) is high not critical because v1.3 already carries an Authorization Letter — operator safety controls are still the gap.
2. **TIBER-EU / DORA TLPT regulatory mapping is the largest theme (27 findings).** Methodology says "aligned with TIBER-EU" but never names Control Team, TI Provider independence, lead-overseer engagement, or attestation. Exercises v1.6 Closure aligns well with TIBER-EU Closure; Initiation does not. Cluster consolidates well into one Tier 2 deliverable: a Regulatory Mapping section in the methodology + engagement-type-to-TLPT mapping table.
3. **Tier 1.1 (Purple Teaming) close-out landed.** All four engagement SOPs now carry a Purple Team Close-Out subsection pointing at `Purple_Teaming_Process_v0.1.docx`. The 17 residual findings in this theme are Close-Out wording/evidence weaknesses — short-effort cleanup.
4. **Naming / acronym drift continues to drop (25 → 8 corpus-level).** Most prior-run coherence findings are closed (`OneNote`, `BloodHound`, `SharpHound`, `WT/RT Point of Contact`, version-pinned Purple Teaming references, Index of process documents). Remaining drift: `Cyberark` casing in two docs, SOP/methodology Process Documents indices asymmetry, TLPT/TIBER-EU first-use expansion.
5. **APTs private dossier carries `TLPT RED` classification but lacks supporting artefacts.** `tdora-aptsdossier-001` (high). Either remove the banner or build the supporting Control Team / TI Provider independence / attestation evidence chain.
6. **Stakeholder deck twins.** `RedTeaming_v1.0.pptx` is content-identical to `RedTeaming_v0.4.pptx` minus the Scheduling chapter (`lifecycle-rtdeckv10-001` high). Retire one and pin the survivor in the methodology Process Documents index.
7. **Adjacent remit (threat hunt + IR support + SOC interface) still missing from prose.** SOC actors (CSIRT / L1–L3 / Pentest-Assessment) appear only in the SOC-RT diagram; the AET (Assessment & Exploitation Team) is in vocab but has no charter doc. Tier 3 structural work.

## Top 10 risks (severity-ranked)

| # | ID | Severity | Risk | Owner |
|---|---|---|---|---|
| 1 | `lifecycle-rtmeth-003` | critical | Methodology has no authorization-chain section — no methodology-level RoE template, kill-switch, or sign-off authority | Red team lead + Legal-Risk |
| 2 | `lifecycle-threatscenarios-003` | critical | Threat Scenarios SOP — no sign-off owner, kill-switch, safe-words, abort criteria | Red team lead + Legal-Risk |
| 3 | `lifecycle-operations-003` | critical | Operations SOP — no documented sign-off, kill-switch or abort criteria | Red team lead + Legal-Risk |
| 4 | `lifecycle-exercises-002` | critical | Exercises SOP — authorization chain still incomplete | Red team lead + Legal-Risk |
| 5 | `lifecycle-physoc-002` | high | PhysSoc — Authorization Letter present but operator safety controls (kill-switch, safe-word, abort) absent | Red team lead + Legal-Risk |
| 6 | `tdora-aptsdossier-001` | high | APTs deck displays `TLPT RED` but no Control Team / TI Provider / attestation evidence | Red team lead + Threat intel |
| 7 | `tdora-exercises-002` | high | TIBER-EU Preparation actors (Control Team, RT Provider, TI Provider) not named in Initiation phase | Red team lead + Legal-Risk |
| 8 | `tdora-rtmeth-002` | high | Methodology — no Control Team / TI Provider / Lead Overseer references anywhere | Red team lead + Legal-Risk |
| 9 | `lifecycle-bh-003` | high | AET role referenced but not defined in any engagement SOP or methodology | Red team lead + AET lead |
| 10 | `lifecycle-rtmeth-004` | high | Adjacent-remit work (threat hunting at close-out, during external engagements, during live incidents) is silent in the methodology | Red team lead + Threat hunt |

## What's well-covered

- **Purple-team close-out** is now a first-class concept across the corpus. The new `Purple_Teaming_Process_v0.1.docx` provides a procedure document; all four engagement SOPs include a Close-Out subsection referencing it; the methodology Process Documents index pins all 8 in-scope artefacts with version numbers. This addresses the highest-severity finding from the 2026-05-12-1417 baseline.
- **Naming hygiene** has improved substantially. The corpus-coherence skill in curated mode now finds **8 findings** (down from 12) — and 4 of those are slow-burn carry-overs already on the Tier 2/3 backlog, not new drift. Vendor canonical casing (BloodHound, SharpHound, OneNote, Cobalt Strike, CyberArk) is largely consistent now.
- **PhysicalSocial v1.3** integrates well with the rest of the corpus — Purple-team close-out present, Authorization Letter referenced, Questionnaire cross-reference correct. The remaining PhysSoc gaps are operator safety controls and Questionnaire/Process cadence reconciliation.
- **Exercises v1.6 Closure** now aligns clearly with TIBER-EU Closure — replay, remediation plan, attestation language. Only Initiation lacks the Preparation-phase actors.

## Recommended next steps

### Quick wins this quarter (Tier 1.2 — Authorization chain)
- **Author an `Authorization & Rules of Engagement` template at the methodology level** (`RedTeam_Methodology_v0.8.docx`) covering sign-off owner, abort criteria, kill-switch procedure, safe-word convention, escalation contact list. ~`lifecycle-rtmeth-003`.
- **Apply the same template as a subsection to each of the four engagement SOPs** (TS v1.7, Ops v1.6, Ex v1.7, PhysSoc v1.4) — closes the 4 criticals. Same find/replace pattern as the Tier 1.1 close-out work.
- **PhysSoc operator safety addendum** — kill-switch, safe-word, and abort criteria specific to physical engagements (lone operator, building access, locker handover). ~`lifecycle-physoc-002`.
- **APTs deck** — either remove `TLPT RED` banner or pair it with a one-page TLPT artefact list (CT, TI provider, attestation reference). ~`tdora-aptsdossier-001`.
- **Stakeholder deck reconciliation** — pick one of `RedTeaming_v0.4.pptx` / `v1.0.pptx` and retire the other.

### Structural next quarter (Tier 2 — Regulatory mapping + completeness)
- **Add `Regulatory Mapping` section** to the methodology (TIBER-EU v2 phases + actors, DORA Art. 26-27 + RTS on TLPT, NCA mapping per Euronext entity, engagement-type-to-TLPT decision table). ~27 findings in this theme.
- **Add `Tier model` subsection** (T0/T1/T2 with Euronext examples).
- **Refresh `RedTeaming_v0.4.pptx`** (or the surviving variant) to mirror methodology v0.8 — Codename theme, Purple-team close-out, all four engagement modalities.

### Longer (Tier 3)
- **SOC interface subsection** (CSIRT / L1–L3 / Pentest-Assessment).
- **AET (Assessment & Exploitation Team) charter** document.
- **Populate `references/euronext-internal-taxonomy.md`** so evaluators can use `EURONEXT-INTERNAL` framework_refs instead of leaning exclusively on TIBER-EU / DORA / PTES / MITRE-ATT&CK.

## Action items (operational)

- [ ] **Install `pdftotext`** on the host (or `apt install poppler-utils`) so the PDFs in `inputs/` produce content extractions on the next run. Today's run treated 7 PDFs as duplicates of their .docx counterparts; if the .docx version were ever lost, the PDF would also be unreadable to the pipeline.
- [ ] **Fix the input selector duplication.** `select_inputs.py` selected both the `.docx` (in `docs/` subfolder) and the `.pdf` (in parent folder) for the same logical document. Format-preference rule should normalize the parent-dir difference. Tracked separately — not blocking.
- [ ] **Reconcile the legacy `inputs/Physical & Social/` folder** with the new `inputs/Engagements/4. Physical & Social/` folder. Both are present and contain different versions of the same documents; selector resolved this correctly by version (`v1.3` won) but the duplicate folder structure should be flattened.
- [ ] **Populate `references/euronext-internal-taxonomy.md`** so the `EURONEXT-INTERNAL` framework_refs become live and evaluators stop falling back to TIBER-EU / DORA / PTES for internally-codified controls.

---

**Output files in this run:**
- `executive-summary.md` (this file)
- `findings-register.csv` (107 rows, RFC-4180)
- `themes.md` (9 themes)
- `remediation-backlog.md` (12 owner groups, sorted critical→informational, S→L within severity)
- `invalid-findings.json` (empty — all 107 findings passed schema validation)
