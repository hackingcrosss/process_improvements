# Executive summary — Red team process evaluation

**Run id:** `2026-05-11-1417`
**Date:** 2026-05-11
**Author:** Process evaluation pipeline (`engagement-lifecycle-review` + `tiber-dora-alignment` evaluators)

---

## Scope of review

8 prose process documents were evaluated end-to-end:

| Document | Engagement type | Findings (after dedup) |
|---|---|---|
| RedTeam_Methodology_v0.3.docx | cross-cutting (methodology) | 22 |
| Research_Methodology_v0.2.docx | cross-cutting (research) | 19 |
| Exercises_Process_v1.1.docx | exercise | 26 |
| Operations_Process_v1.0.docx | operation | 17 |
| ThreatScenarios_Process_v1.1.docx | threat-scenario | 18 |
| PhysicalSocial_Process_v1.0.docx | cross-cutting (physical) | 19 |
| PhysicalSocial_Questionnaire_Process_v1.0.docx | template | 12 |
| BloodhoundEnterprise_Process_v0.1.docx | cross-cutting (tooling) | 13 |
| **Total (deduped)** | | **146** |

Each artefact was selected per the project's input-selection rules (`.docx` preferred over `.pdf`, highest version only). The two evaluators ran independently and findings were deduplicated and clustered before reporting.

### Scope and limitations of this run

- **17 unsupported files were excluded.** Most notably `inputs/Methodology/RedTeaming_v1.0.pptx` — the master red-teaming deck — and four older versions of the same deck were not evaluated because the ingest pipeline does not yet read `.pptx`. The full list is in the appendix. **Recommend**: extend ingest to handle `.pptx` and re-run, since the master deck is plausibly the most-referenced artefact internally.
- **9 diagrams + 1 image were ingested but not standalone-evaluated.** They are parked in `workdir/` for a future `diagram-consistency` evaluator that cross-checks figures against the prose. Several prose docs reference figures the ingest could not render — these gaps are tracked as low/medium findings.
- **`references/euronext-internal-taxonomy.md` is a placeholder.** No `EURONEXT-INTERNAL` framework references appear in any finding. Findings are anchored to TIBER-EU, DORA-TLPT, MITRE ATT&CK, PTES, NIST SP 800-115, and OSSTMM only. **Recommend**: populate the internal taxonomy so the next run produces GRC-routable IDs.
- **Many TIBER-EU and DORA TLPT references are cited from memory** (per the evaluator's anti-fabrication rule) and carry `confidence: "low"`. Treat these as starting points to verify against live regulation text and the live TIBER-EU v2 framework / RTS on TLPT before publication.

---

## Headline findings

Severity breakdown after dedup: **11 critical, 50 high, 48 medium, 23 low, 14 informational**.

Five themes account for ~95% of the volume; the rest are long-tail items captured in `themes.md` and `findings-register.csv`.

1. **TIBER-EU / DORA TLPT misalignment** is the dominant theme (83 findings, 9 critical, 31 high). Across every prose document the regulator-aligned vocabulary (TIBER-EU phases, Control Team distinct from White Team, independent TI provider, TCT engagement, attestation, mutual recognition) is either absent or implicit. The methodology calls Exercises *"TIBER-Like"* without committing to the phase or actor model, and the Data Handling section references a US statute ("Privacy of Information Act") rather than GDPR / DORA. If any engagement is ever cited as TLPT evidence — even informally — this gap will be queried under examination.
2. **Mandatory purple-team close-out is missing or weak** in Threat Scenarios, Operations, Exercises, BloodhoundEnterprise, and the central methodology. For Threat Scenarios this is the most striking gap because joint blue-team participation is the *defining feature* of the engagement type per the team's own taxonomy.
3. **Authorization, RoE, kill-switch, abort criteria, and safe-words** are missing or implicit across most SOPs (23 findings, 1 critical, 10 high). For physical engagements no operator check-in / emergency-contact protocol is defined at all — a personal-safety risk, not just a paperwork one.
4. **Codename + theme convention is undocumented** in the central methodology (7 findings). Individual SOPs reference codenames but only Exercises and Operations need the fictional-character theme; the methodology should state this once, authoritatively, and reference a codename register to avoid collisions.
5. **Threat-hunt handover and IR-support remit are largely silent** (9 findings). The team's actual responsibilities — turning red findings into hunt hypotheses, supporting external red-team-against-Euronext exercises, helping during live incidents — are absent from the methodology and most SOPs. This understates the team's value and creates a documentation gap with SOC / IR.

---

## Top 10 risks (severity-ranked, with proposed owner)

| # | Severity | Artefact | Title | Owner |
|---|---|---|---|---|
| 1 | Critical | ThreatScenarios_Process_v1.1.docx | No purple-team close-out — contradicts the defining feature of the engagement type | Red team lead + Purple/SOC |
| 2 | Critical | ThreatScenarios_Process_v1.1.docx | No authorization / RoE / kill-switch / safe-words | Red team lead + Legal/Risk |
| 3 | Critical | Operations_Process_v1.0.docx | No purple-teaming close-out | Red team lead + Purple/SOC |
| 4 | Critical | Operations_Process_v1.0.docx | Authorization phase is implicit; no legal sign-off, RoE, safe-words, or abort criteria | Red team lead + Legal/Risk |
| 5 | Critical | Exercises_Process_v1.1.docx | No mandatory purple-team close-out / replay with the blue team | Red team lead + Purple/SOC |
| 6 | Critical | RedTeam_Methodology_v0.3.docx | Authorization, RoE, legal sign-off, kill-switch / abort criteria not described | Red team lead + Legal/Risk |
| 7 | Critical | RedTeam_Methodology_v0.3.docx | TIBER-EU Preparation elements absent (GTL, scoping doc, engagement letter, critical-functions ID, provider procurement) | Red team lead + Risk/Compliance |
| 8 | Critical | PhysicalSocial_Process_v1.0.docx | No purple-teaming close-out with blue team and physical security | Red team lead + Physical security |
| 9 | Critical | PhysicalSocial_Process_v1.0.docx | No kill-switch, abort criteria or operator check-in / emergency-contact protocol | Red team lead + Physical security |
| 10 | Critical | PhysicalSocial_Process_v1.0.docx | All four TIBER-EU phases absent for the physical leg — physical run as a parallel track, not integrated with TLPT | Red team lead + Risk/Compliance |

The full ranked backlog (146 items, grouped by owner and sorted by severity × effort) is in `remediation-backlog.md`.

---

## What's well-covered

A whole-document report risks reading as all-negative. Several things are genuinely strong and should be preserved:

- The **three-engagement taxonomy** (Exercises / Operations / Threat Scenarios) is consistently named and gives the team a defensible, internally-coherent framing that many institutions lack.
- The **PhysicalSocial process** explicitly addresses cyber + physical integration intent, names a "Get-out-of-jail letter", and lists a Vulnerability / Maturity scoring construct — most red teams have no physical doc at all.
- The **Research methodology exists** as a written document with a hypothesis-to-validation lifecycle and a Research Repository concept — this is rare and worth defending.
- The **Operations SOP's leg-up / deconfliction concept** is described as a controlled mechanic.
- The **BloodhoundEnterprise process** identifies cleanup, user-account-impact, and the conscious choice to disable detections during enumeration — operational details typically missing in tool-usage docs.

The findings are about hardening these, not replacing them.

---

## Recommended next steps

### Quick wins (this quarter)

- **Codify the codename + fictional-character convention** once in `RedTeam_Methodology_v0.3.docx` (S effort). Each SOP can then reference it instead of redefining it.
- **Add an authoritative purple-team close-out section** to every engagement SOP that currently lacks it (S effort each). Specify attendees, agenda, output artefact.
- **Replace every reference to "Privacy of Information Act" with GDPR + DORA** (S effort). This single edit removes a regulator-alignment concern that runs across multiple docs.
- **Add an explicit "physical scope: in / out" line** to every engagement SOP that is silent on it (S effort each).

### Structural changes (next quarter)

- **Decide TLPT positioning, then commit.** Either Exercises are TIBER-EU / DORA TLPT engagements (and the methodology is updated to mirror the TIBER-EU phase + actor model), or they are inspired by TIBER-EU but explicitly not TLPT. The current "TIBER-Like" wording is the worst of both worlds.
- **Define the Control Team distinct from the White Team.** Several SOPs conflate the two; under TLPT they have different mandates and reporting lines.
- **Populate the internal taxonomy** at `references/euronext-internal-taxonomy.md` so the next pipeline run can tag findings with your internal control IDs and feed GRC directly.
- **Make threat-hunt handover and IR-support remit explicit** in the methodology and the relevant SOPs — both as engagement deliverables and as the team's standing responsibilities.
- **Extend the ingest pipeline to `.pptx`** so the master red-teaming deck is in the next evaluation.

### For the next pipeline run

- Add a `diagram-consistency` evaluator that cross-checks the 9 ingested diagrams against the prose docs (figures referenced but missing, actors named in prose but not in diagram, flows without labels).
- Add `roe-authorization-review` as a dedicated evaluator now that we know this is the second-largest theme.
- Re-run after populating the internal taxonomy so findings carry both external (TIBER-EU / DORA / ATT&CK) and internal (Euronext) anchors.

---

## Files in this run

- `executive-summary.md` (this file)
- `findings-register.csv` — 146 deduped findings, RFC-4180 quoted, one row per finding with merged_from attribution
- `remediation-backlog.md` — findings grouped by recommended owner, sorted severity × effort
- `themes.md` — 10 themes with contributing finding ids

---

## Appendix — Files not evaluated in this run

The input selector flagged 17 files as unsupported because the ingest pipeline does not yet read these formats. Extending ingest to `.pptx` is the highest-value gap, as it would unlock the master red-teaming deck and the APT reference deck.

```
.pptx  (master decks):
  - Methodology/RedTeaming_v1.0.pptx   ← highest priority
  - Methodology/RedTeaming_v0.1..v0.4.pptx (older versions)
  - APTs/APTs.pptx
  - APTs/APTs_private.pptx

.xlsx  (operational data):
  - APTs/All.xlsx
  - Methodology/AttackPaths_v0.1.xlsx
  - Methodology/Bloodhound_KPIs.xlsx
  - Methodology/ResearchTopics.xlsx
  - Methodology/VRC-AdHoc-Build-Version_v1.8.xlsx
  - Engagements/0. Threat Scenarios/ThreatScenarios_Services_v0.1.xlsx
  - Physical & Social/PhysicalLocations_Framework_v0.1.xlsx

.xmind  (mind maps):
  - Resources & Diagrams/RT_Infra.xmind
  - Resources & Diagrams/Resources.xmind
  - Resources & Diagrams/Shellcode_Execution.xmind
```

Diagrams (`.drawio`) and one `.jpg` were ingested into `workdir/` but not standalone-evaluated; they will feed a future `diagram-consistency` evaluator without requiring re-ingest.
