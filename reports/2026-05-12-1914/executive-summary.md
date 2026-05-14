# Executive summary — Red Team process review
_Run id: 2026-05-12-1914  ·  Date: 2026-05-12  ·  Post-quick-win + Tier 1.1 (Purple Teaming) re-evaluation_

## Scope of review

- **Artefacts reviewed:** 21 (10 prose docs + 8 diagrams + 2 image/legacy artefacts skipped per ingest rules); 49 superseded/older-version files filtered by selection rules.
- **Evaluators run:** `engagement-lifecycle-review`, `tiber-dora-alignment`, `corpus-coherence` (curated mode).
- **Findings (post-dedup):** 54 — critical 5, high 9, medium 24, low 12, informational 4.
- **vs prior run** (2026-05-12-1520): 181 findings, 12 critical, 63 high. **This run: 54 findings, 5 critical, 9 high.** Material improvement driven by user-applied quick-wins (vocabulary, Closure rename, codename theme, OFI glossary) and Tier 1.1 (Purple-team close-out added to all SOPs + new Purple_Teaming_Process_v0.1.docx).

## Headline themes (post-fix)

- **Authorization, RoE and kill-switch (Tier 1.2 — DORA defensibility)** — 5 findings (4c/1h/0m/0l/0i). Example: `lifecycle-exercises-001` — Authorization phase still implicit: no named legal sign-off, no kill-switch / abort criteria, no safe-words.
- **TIBER-EU / DORA TLPT regulatory mapping** — 8 findings (0c/3h/2m/1l/2i). Example: `lifecycle-exercises-002` — TIBER-EU role mapping (TLPT Authority, Control Team, TI Provider, RT Provider) not made explicit in Initiation.
- **Other / general process-quality findings** — 9 findings (0c/2h/3m/3l/1i). Example: `lifecycle-operations-002` — Section opens 'two main teams' but describes three (RT, BT, WT).
- **Acronym disambiguation and undefined acronyms (PoC, VRC, CMDB, AET, IST, CTI)** — 4 findings (0c/2h/2m/0l/0i). Example: `coherence-003` — Acronym conflict: 'WT PoC' / 'RT PoC' in Exercises v1.4 Deconfliction; Operations v1.3 was rewritten to full form.
- **Cross-doc naming drift (One Note, Bloodhound, PoC, Sharphound)** — 7 findings (0c/1h/3m/3l/0i). Example: `coherence-001` — Naming drift: 'One Note' in methodology v0.6 OPLOGS section; three SOPs already fixed to 'OneNote'.
- **Operator safety (physical engagements)** — 3 findings (1c/0h/2m/0l/0i). Example: `lifecycle-physoc-001` — Operator safety protocol still absent: no scheduled check-ins, no abort/kill-switch wording, no emergency contacts.

## What was closed since the last run

The 2026-05-12 quick-wins + Tier 1.1 work closed (or substantially reduced) these themes:

- **Purple-team close-out** — was 13 findings (4 critical, 3 high). Now 4 medium follow-ups (cross-reference version-pinning + Euronext-specific role mapping for the new v0.1 doc).
- **Codename + theme convention** — was 11 findings. Now 0 (theme documented in methodology v0.6 and all three engagement SOPs).
- **Report → Closure phase name** — was 1 high. Now closed (Threat Scenarios renamed; opening sentence has minor lingering "report" wording, captured as low).
- **Cross-doc naming drift** (CobaltStrike, OneNote, defending teams, Cyberark, Tier Zero, CTI, repository name prefixes) — was many. Now 4 residual items: `One Note` in methodology OPLOGS, `Bloodhound` in Operations Research & Preparation, `WT/RT PoC` in Exercises Deconfliction, `Sharphound` in BloodHound v0.3 Introduction.
- **Broken cross-reference to Purple Teaming Process document** — was medium broken-xref. Now resolved (doc exists at `inputs/Engagements/3. Purple Teaming/docs/Purple_Teaming_Process_v0.1.docx`); remaining: version-pinning the references in the methodology and 4 SOPs (5 medium items).
- **OFI glossary** — OFI now in methodology glossary and introduced in all engagement SOP Closure phases.
- **`TI` vs `CTI` acronym drift in Operations** — closed; Operations v1.3 now uses `TI team` / `TI news` consistently.

## Top risks

| # | Severity | ID | Title | Why it matters | Owner |
|---|---|---|---|---|---|
| 1 | critical | `lifecycle-exercises-001` | Authorization phase still implicit: no named legal sign-off, no kill-switch / abort criteria, no safe-words | An Authorization subsection (post-Initiation / pre-Targeted TI): sign-off authorities, RoE, safe-words, abort criteria, Control Team and TLP | Red team lead + Legal/Risk + Control Team |
| 2 | critical | `lifecycle-operations-001` | Authorization phase implicit: no legal sign-off, no RoE artefact, no safe-words, no kill-switch / abort criteria | An Authorization phase between Research & Preparation and Red Team Test: sign-off authority, RoE, safe-words, abort/kill-switch. | Red team lead + Legal/Risk |
| 3 | critical | `lifecycle-physoc-001` | Operator safety protocol still absent: no scheduled check-ins, no abort/kill-switch wording, no emergency contacts | An 'Operator safety protocol' subsection: scheduled check-in cadence; abort/kill-switch; emergency contacts (medical, legal, in-country POC) | Red team lead + Legal/HR |
| 4 | critical | `lifecycle-threatscenarios-001` | Authorization phase still absent: no legal sign-off, no RoE artefact, no kill-switch, no safe-words, no abort criteria | An Authorization subsection in Planning naming: who signs off; RoE artefact location; named kill-switch / abort conditions; safe-words; who  | Red team lead + Legal/Risk |
| 5 | critical | `lifecycle-rtmeth-001` | Authorization chain, kill-switch and safe-words still not defined in the methodology | An 'Authorization and Engagement Controls' section: legal sign-off; RoE template + storage; safe-words; abort/kill-switch; escalation; WT re | Red team lead + Legal/Risk |
| 6 | high | `coherence-001` | Naming drift: 'One Note' in methodology v0.6 OPLOGS section; three SOPs already fixed to 'OneNote' | Align all artefacts to 'OneNote'. | Red team lead |
| 7 | high | `coherence-003` | Acronym conflict: 'WT PoC' / 'RT PoC' in Exercises v1.4 Deconfliction; Operations v1.3 was rewritten to full form | Align to 'WT Point of Contact' / 'RT Point of Contact'. PoC canonical = Proof of Concept; never abbreviate Point of Contact to PoC. | Red team lead |
| 8 | high | `lifecycle-operations-002` | Section opens 'two main teams' but describes three (RT, BT, WT) | Either 'three main teams' or reword to clarify WT as coordination/authorisation role. | Red team lead |
| 9 | high | `lifecycle-physoc-003` | 'VRC' acronym used in Questionnaire section without expansion | Expand VRC on first use in the Questionnaire section. | Red team lead |
| 10 | high | `lifecycle-exercises-002` | TIBER-EU role mapping (TLPT Authority, Control Team, TI Provider, RT Provider) not made explicit in Initiation | An explicit TIBER-EU role mapping in Initiation, naming who plays each external role within Euronext. | Red team lead + Legal/Risk |

## What is well covered (carried forward)

- **Deconfliction** — RT/WT/BT roles and decision tree consistent across Operations and Exercises SOPs; matched by the deconfliction.drawio diagram.
- **Data handling** — encryption in transit, secure transport, PIA halt-and-escalate consistent across all three engagement SOPs and the methodology.
- **Threat-actor modelling** — APT taxonomy and Threat Profile Examples give a working language for adversary emulation, mapped to MITRE ATT&CK.
- **Research lifecycle** — `Research_Methodology_v0.4` and the matching `Research_Process_v0.8.drawio` are tightly aligned (intake → repository → deep dive → capability → engagements → feedback + purple teaming).
- **Purple-team close-out** — every engagement SOP (TS / Operations / Exercises / Physical & Social) now includes the mandatory Purple-team close-out subsection, anchored by the new `Purple_Teaming_Process_v0.1.docx`.
- **Codename + theme convention** — explicit in methodology v0.6 with the fictional/historical character theme codified for Operations and Exercises (Threat Scenarios exempt).
- **BloodHound process** — strong end-to-end procedural detail; v0.3 cleaned up `Tier Zero` / `Bloodhound` / `Cyberark` drift; remaining `Sharphound` is a one-character fix.

## Recommended next steps

**Cleanup pass (S-effort, this week)**

1. Naming drift residuals: `One Note` → `OneNote` in `RedTeam_Methodology_v0.6.docx`; `Bloodhound` → `BloodHound` in `Operations_Process_v1.3.docx`; `WT PoC` / `RT PoC` → spell out in `Exercises_Process_v1.4.docx`; `Sharphound` → `SharpHound` in `BloodhoundEnterprise_Process_v0.3.docx`.
2. Pin the `Purple Teaming Process document` cross-references across the methodology and 4 SOPs to `Purple_Teaming_Process_v0.1.docx`.
3. Operations SOP: fix the "two main teams" / three-teams contradiction.
4. Research Methodology: fix the "Feeback" typo.
5. PhysSoc: expand `VRC` and `CMDB` on first use.

**Tier 1.2 (this quarter, M-L effort) — Authorization chain**

6. Author an `Authorization and Engagement Controls` section in `RedTeam_Methodology_v0.7`: legal sign-off authority, RoE template + storage, safe-words, abort/kill-switch criteria, escalation path, WT relationship per engagement type.
7. Add per-engagement-type `Authorization` subsections to TS, Operations, Exercises, and PhysSoc SOPs.
8. For PhysSoc specifically, add an `Operator safety protocol` subsection (check-ins, abort word, emergency contacts) — operator-welfare critical.

**Tier 2 (next quarter, M-effort) — Regulatory mapping and methodology completeness**

9. Add a `Regulatory mapping` section to `RedTeam_Methodology` expanding TLPT / TIBER-EU / CBEST, mapping engagement types to TLPT phases, naming supervisors per Euronext entity, and referencing DORA Art. 26-27.
10. Add a `Tier model` subsection defining T0/T1/T2 with Euronext examples.
11. Add an `Ancillary remit` section: threat hunt at engagement close (handover to SOC); external red team support; live IR support.
12. Add an `Index of process documents` section; cross-reference PhysSoc, Research Methodology, BloodHound process, Purple Teaming process.
13. Refresh the stakeholder deck `RedTeaming_v1.0.pptx` to mirror v0.6 methodology updates.

**Tier 3 (longer term)**

14. SOC interface subsection (CSIRT / L1-L3 / Pentest-Assessment touchpoints with RT engagements).
15. AET charter — add `Assessment & Exploitation Team` subsection to the methodology with charter and RACI.
16. Populate `references/euronext-internal-taxonomy.md` so future runs can tag findings with internal control IDs.
17. Promote `Purple_Teaming_Process` to v1.0: customise with Euronext-specific named roles, tracking forum URL, and version-pinned references.

---
_Files: `findings-register.csv` · `themes.md` · `remediation-backlog.md`._