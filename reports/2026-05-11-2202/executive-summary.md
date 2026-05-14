# Executive summary - Red team process evaluation (cumulative)

**Run id:** `2026-05-11-2202`  
**Date:** 2026-05-11  
**Author:** Process evaluation pipeline (`engagement-lifecycle-review` + `tiber-dora-alignment` evaluators)  
**Previous run referenced:** `reports/2026-05-11-1417/` (8 prose docs, 146 deduped findings)

---

## What's new since 2026-05-11-1417

The master Red Teaming deck (`Methodology/RedTeaming_v1.0.pptx`) has now been ingested and evaluated, bringing this run to **9 artefacts (8 prose .docx + 1 .pptx) and 216 deduped findings**. The deck is the team's most visible internal explainer, so its content gaps reach a broader audience than the SOPs.

**Top deck findings:**
- **[CRITICAL]** `lifecycle-rtdeck-003` - Mandatory purple-team close-out is not mentioned  
- **[HIGH]** `lifecycle-rtdeck-001` - Deck does not distinguish the three engagement types (Exercise / Operation / Threat Scenario)  
- **[HIGH]** `lifecycle-rtdeck-002` - Codename + fictional-character theme convention not mentioned  
- **[HIGH]** `lifecycle-rtdeck-004` - Adjacent remit (threat hunt at close, hunt support, IR support) absent  
- **[HIGH]** `lifecycle-rtdeck-005` - Physical scope is not addressed  

**Reinforcements with the prose docs (deck is silent where the SOPs are silent):** TIBER-EU / DORA TLPT framing is absent; codename + theme convention is not stated; purple-team close-out is not mentioned; physical scope is not addressed; adjacent remit (threat hunt, IR support) is absent.

**Contradictions with the prose docs:** Slide 11 asserts "Blue Team (BT): TBD - Unaware of the exercise, must carry-on with normal activities" as a universal property of red teaming. This contradicts `ThreatScenarios_Process_v1.1.docx`, where the defining feature of a Threat Scenario is **joint walk-through with the blue team in the room**, and it understates the partially-collaborative shape of Operations. The deck also names individual operators ("Renato Cruz and José Barbosa") on slide 11 - acceptable in per-engagement RoE, not in a persistent master explainer.

**New gap surfaced by the deck only:** 15 of 27 slides carry `[chart-or-smartart]` placeholders with no prose caption. Phase numbering (Phases 0-4) is presented only inside the visuals, so the deck does not stand alone as a textual methodology. This is both a content-readability concern and a documentation gap - the team's visual story is not captured in text. See theme `Diagram & visual readability` in `themes.md`.

---

## Scope of review

9 artefacts were evaluated end-to-end (8 prose `.docx` + 1 master `.pptx` deck). Cyber + physical are both in scope. Diagrams were ingested but not standalone-evaluated (parked for a future `diagram-consistency` evaluator).

| # | Document | Engagement type | Findings (after dedup) |
|---|---|---|---|
| 1 | RedTeam_Methodology_v0.3.docx | cross-cutting (methodology) | 29 |
| 2 | Research_Methodology_v0.2.docx | cross-cutting (research) | 20 |
| 3 | RedTeaming_v1.0.pptx (master deck) | cross-cutting (deck) | 24 |
| 4 | Exercises_Process_v1.1.docx | exercise | 31 |
| 5 | Operations_Process_v1.0.docx | operation | 22 |
| 6 | ThreatScenarios_Process_v1.1.docx | threat-scenario | 23 |
| 7 | PhysicalSocial_Process_v1.0.docx | cross-cutting (physical) | 30 |
| 8 | PhysicalSocial_Questionnaire_Process_v1.0.docx | template | 16 |
| 9 | BloodhoundEnterprise_Process_v0.1.docx | cross-cutting (tooling) | 21 |
| | **Total (deduped)** | | **216** |

### Scope and limitations of this run

- **Input selection rules still hold.** Per project convention, `.docx` is preferred over `.pdf` for the same logical doc, and only the highest version is analysed. **45 files were excluded** as superseded versions / duplicate format variants - including four older `RedTeaming_v0.x.pptx` versions, six older `Research_Process_vX.drawio` versions, and various `.pdf` doubles of the analysed `.docx` files.
- **`APTs/APTs.pptx` was correctly identified as a legacy `.ppt` binary with a misleading `.pptx` extension and not ingested.** The ingest pipeline emitted a warning recommending conversion to true `.pptx` and re-ingest.
- **10 files remain unsupported** because the ingest pipeline does not yet read these formats (`.xlsx` operational spreadsheets, `.xmind` mind maps, and the legacy-binary `APTs.pptx`). Full list in the appendix.
- **9 diagrams + 1 image were ingested but not standalone-evaluated.** They live in `workdir/` for a future `diagram-consistency` evaluator that will cross-check figures against the prose.
- **`references/euronext-internal-taxonomy.md` is still a placeholder.** No `EURONEXT-INTERNAL` framework references appear in any finding; anchors remain external (TIBER-EU, DORA-TLPT, MITRE ATT&CK, PTES, NIST SP 800-115, OSSTMM).
- **Many TIBER-EU and DORA TLPT references are cited from memory** (per the evaluator's anti-fabrication rule) and carry `confidence: "low"`. The recommendation to verify these against live regulation text (DORA Regulation (EU) 2022/2554 Art.26-27, the related RTS on TLPT, and the live TIBER-EU v2 framework) before publication still stands.

---

## Headline findings

Severity breakdown after dedup: **13 critical**, **79 high**, **72 medium**, **32 low**, **20 informational**.

Theme rollup (full breakdown in `themes.md`):

- **TIBER-EU / DORA TLPT misalignment**: 112 findings
- **Physical scope completeness**: 34 findings
- **Safety, OPSEC & data protection**: 28 findings
- **Authorization / RoE clarity**: 27 findings
- **Purple-team close-out**: 22 findings
- **Reporting & remediation tracking**: 21 findings

1. **TIBER-EU / DORA TLPT misalignment** remains the dominant theme (112 findings). Across every prose document **and the new master deck** the regulator-aligned vocabulary - TIBER-EU phases (Preparation / TI / RTT / Closure), Control Team distinct from White Team, independent TI provider, TCT engagement, attestation, mutual recognition - is either absent or implicit. The methodology continues to call Exercises *"TIBER-Like"* without committing to the phase or actor model, and the Data Handling section still references a US statute ("Privacy of Information Act") rather than GDPR / DORA. The deck does not name TIBER-EU, TLPT, lead overseer, attestation or control team anywhere, while describing a full external-style kill-chain with C2 tooling - leadership / audit audiences may misread this as a description of how Euronext does TLPT.
2. **Mandatory purple-team close-out is missing or weak** in the methodology, the deck, Exercises, Operations, Threat Scenarios, BloodhoundEnterprise and the physical SOP. For Threat Scenarios this remains the most striking gap because joint blue-team participation is the defining feature of the engagement type per the team's own taxonomy.
3. **Authorization, RoE, kill-switch, abort criteria, and safe-words** are missing or implicit across most SOPs and the deck. For physical engagements no operator check-in / emergency-contact protocol is defined - a personal-safety risk, not just paperwork.
4. **Codename + theme convention is undocumented** in the central methodology and silent on the deck (which is the master explainer). Individual SOPs reference codenames inconsistently.
5. **Threat-hunt handover and IR-support remit are largely silent.** The team's adjacent responsibilities - turning red findings into hunt hypotheses, supporting external red-team-against-Euronext exercises, helping during live incidents - are absent from the methodology, the deck and most SOPs. This understates the team's value and creates a documentation gap with SOC / IR.
6. **(New) Deck contradicts the engagement-type taxonomy.** Slide 11 asserts 'Blue Team unaware' as a universal property of red teaming, which conflicts with the ThreatScenarios SOP (collaborative walk-through) and understates the Operations shape. Slide 11 also names individual operators in a persistent explainer deck. See dedicated theme in `themes.md`.

---

## Top 10 risks (severity-ranked, with proposed owner)

| # | Severity | Artefact | Title | Owner |
|---|---|---|---|---|
| 1 | Critical | Exercises_Process_v1.1.docx | No mandatory purple-team close-out / replay with the blue team | Red team lead + Blue team lead |
| 2 | Critical | Exercises_Process_v1.1.docx | Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words | Red team lead + Legal/Risk |
| 3 | Critical | Operations_Process_v1.0.docx | No purple-teaming close-out with the blue team | Red team lead / Purple team |
| 4 | Critical | Operations_Process_v1.0.docx | Authorization phase is implicit; no legal sign-off, RoE artefact, safe-words, or abort criteria defined | Red team lead / Legal-Risk |
| 5 | Critical | PhysicalSocial_Process_v1.0.docx | No purple-teaming close-out with blue team and physical security | Purple team / Red team lead |
| 6 | Critical | PhysicalSocial_Process_v1.0.docx | No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site | Red team lead / Legal / HR |
| 7 | Critical | RedTeaming_v1.0.pptx (master deck) | Mandatory purple-team close-out is not mentioned | Red team lead, Purple team |
| 8 | Critical | RedTeam_Methodology_v0.3.docx | Authorization, Rules of Engagement, legal sign-off and kill-switch / abort criteria are not described | Red team lead / Legal & Risk |
| 9 | Critical | ThreatScenarios_Process_v1.1.docx | No purple-team close-out described, despite Threat Scenario format requiring blue team in the room | Red team lead with Purple team / SOC |
| 10 | Critical | ThreatScenarios_Process_v1.1.docx | No authorization / Rules-of-Engagement section: no legal sign-off, no kill-switch, no abort criteria | Red team lead with Legal/Risk |

The full ranked backlog (216 items, grouped by owner and sorted severity x effort) is in `remediation-backlog.md`.

---

## What's well-covered

Several things are genuinely strong across the corpus and should be preserved as remediation proceeds:

- The **three-engagement taxonomy** (Exercises / Operations / Threat Scenarios) is consistently named and gives the team a defensible, internally-coherent framing that many institutions lack. The deck does not enumerate it explicitly - one of the deck's top remediation items - but the prose SOPs do.
- The **PhysicalSocial process** explicitly addresses cyber + physical integration intent, names a "Get-out-of-jail letter", and lists a Vulnerability / Maturity scoring construct - most red teams have no physical doc at all.
- The **Research methodology exists** as a written document with a hypothesis-to-validation lifecycle and a Research Repository concept - rare and worth defending.
- The **Operations SOP's leg-up / deconfliction concept** is described as a controlled mechanic; the deck picks the concept up but should add the approval-and-log requirement.
- The **BloodhoundEnterprise process** identifies cleanup, user-account-impact, and the conscious choice to disable detections during enumeration - operational details typically missing in tool-usage docs.
- The **master deck has an "Importance" and "Requirements" framing** that makes a decent entry point for leadership audiences once content gaps are filled in.

The findings are about hardening these, not replacing them.

---

## Recommended next steps

### Quick wins (this quarter)

- **Codify the codename + fictional-character convention** once in `RedTeam_Methodology_v0.3.docx` AND add a corresponding slide to the master deck (S effort). Per-type SOPs then reference it.
- **Add a positioning statement to the master deck**: "this deck describes the internal red-teaming methodology; TLPT runs require additional TIBER-EU-mandated actors (Control Team, independent TI provider) and artefacts (TTI, attestation)." (S effort) This single line removes the largest misread risk on the deck.
- **Add an authoritative purple-team close-out section** to every engagement SOP and a Closure slide to the deck (S effort each). Specify attendees, agenda, output artefact.
- **Replace every reference to "Privacy of Information Act" with GDPR + DORA** (S effort). This single edit removes a regulator-alignment concern that runs across multiple docs.
- **Add an explicit "physical scope: in / out" line** to every engagement SOP that is silent on it, and a physical-scope slide to the deck (S effort each).
- **Re-word the deck's slide 11 "Blue Team unaware"** so the property is conditional on engagement type, and add a clarifying line that Threat Scenarios are explicitly collaborative (S effort).
- **Remove individual operator names from the master deck** and replace with team role; named operators belong in per-engagement RoE / authorization artefacts (S effort).
- **Add prose captions to the deck's 15 `[chart-or-smartart]` slides** so the deck reads on its own when printed, screen-shared at low resolution, or shown to an auditor (M effort).
- **Apply a classification / distribution label to the master deck** given it names operators and discusses C2 infrastructure (S effort).

### Structural changes (next quarter)

- **Decide TLPT positioning, then commit.** Either Exercises are TIBER-EU / DORA TLPT engagements (and the methodology and deck are updated to mirror the TIBER-EU phase + actor model), or they are inspired by TIBER-EU but explicitly not TLPT. The current "TIBER-Like" wording is the worst of both worlds.
- **Define the Control Team distinct from the White Team.** Several SOPs and the deck conflate the two; under TLPT they have different mandates and reporting lines.
- **Address Targeted Threat Intelligence provider independence.** The deck states the Red Team performs TTI itself, which is a TIBER-EU misalignment when applied to TLPT runs.
- **Populate the internal taxonomy** at `references/euronext-internal-taxonomy.md` so the next run can tag findings with Euronext control IDs and feed GRC directly.
- **Make threat-hunt handover and IR-support remit explicit** in the methodology, the deck and the relevant SOPs - both as engagement deliverables and as the team's standing responsibilities.
- **Verify all `confidence: "low"` TIBER-EU / DORA citations** against live regulation text (DORA Regulation (EU) 2022/2554 Art.26-27, related RTS on TLPT, TIBER-EU v2 framework) before any external use.

### For the next pipeline run

- Run the `diagram-consistency` evaluator against the 10 ingested visuals (9 `.drawio` + 1 `.jpg`) to cross-check figures against the prose docs and the deck's phase / actor visuals.
- Add `roe-authorization-review` as a dedicated evaluator (this is the third-largest theme).
- Extend ingest to `.xlsx` so the operational spreadsheets (`AttackPaths_v0.1`, `Bloodhound_KPIs`, `ResearchTopics`, `VRC-AdHoc-Build-Version`, `ThreatScenarios_Services`, `PhysicalLocations_Framework`) become reviewable.
- Convert `APTs/APTs.pptx` from legacy `.ppt` to true `.pptx` (PowerPoint / LibreOffice round-trip) and re-ingest.
- Re-run after populating the internal taxonomy so findings carry both external (TIBER-EU / DORA / ATT&CK) and internal (Euronext) anchors.

---

## Files in this run

- `executive-summary.md` (this file)
- `findings-register.csv` - 216 deduped findings, RFC-4180 quoted, UTF-8, one row per finding with merged_from attribution
- `remediation-backlog.md` - findings grouped by recommended owner, sorted severity x effort
- `themes.md` - 12 themes (including the new 'Deck contradicts engagement-type taxonomy') with contributing finding ids

The prior run `reports/2026-05-11-1417/` remains on disk for continuity; it is not modified or deleted.

---

## Appendix - Files not evaluated in this run

### Unsupported formats (10 files)

The ingest pipeline does not yet read these formats. The legacy `.ppt` binary (`APTs.pptx`) was correctly detected and skipped.

```
.xlsx  (operational data):
  - APTs/All.xlsx
  - Engagements/0. Threat Scenarios/ThreatScenarios_Services_v0.1.xlsx
  - Methodology/AttackPaths_v0.1.xlsx
  - Methodology/Bloodhound_KPIs.xlsx
  - Methodology/ResearchTopics.xlsx
  - Methodology/VRC-AdHoc-Build-Version_v1.8.xlsx
  - Physical & Social/PhysicalLocations_Framework_v0.1.xlsx

.xmind  (mind maps):
  - Resources & Diagrams/RT_Infra.xmind
  - Resources & Diagrams/Resources.xmind
  - Resources & Diagrams/Shellcode_Execution.xmind

Legacy binary mislabelled .pptx (detected and skipped):
  - APTs/APTs.pptx
```

### Superseded by selection rules

- 4 older `Methodology/RedTeaming_v0.x.pptx` versions dropped in favour of v1.0.
- 6 older `Methodology/Diagrams/Research_Process_v0.x.drawio` versions dropped in favour of v0.7.
- Older `.docx` versions of every engagement SOP dropped in favour of the highest version.
- `.pdf` doubles of analysed `.docx` files excluded per project rule.
- `APTs/APTs_private.pptx` is in scope and was selected but is a stub; no findings were emitted (no SOP / methodology content).

Diagrams (`.drawio`) and one `.jpg` were ingested into `workdir/` but not standalone-evaluated; they will feed a future `diagram-consistency` evaluator without requiring re-ingest.