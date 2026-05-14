# Executive summary — Red Team process review
_Run id: 2026-05-12-1520  ·  Date: 2026-05-12_

## Scope of review

- **Artefacts reviewed:** 18 (10 prose docs + 8 diagrams; 4 superseded versions and 2 ingest-blocked artefacts excluded per project rules).
- **Evaluators run:** `corpus-coherence`, `engagement-lifecycle-review`, `tiber-dora-alignment`.
- **Findings (post-dedup):** 181 — critical 12, high 63, medium 62, low 30, informational 14.
- **Mode:** `corpus-coherence` ran in **curated** mode against `references/corpus_vocabulary.yaml`.

## Headline themes

- **TIBER-EU / DORA TLPT regulatory alignment** — 59 findings (4c/20h/20m/5l/10i). Example: `lifecycle-exercises-001` — No clean-up / environment restoration step before report sign-off || Closure phase missing TIBER-EU mandated artefacts (replay, 360 feedback.
- **Physical scope and social-engineering completeness** — 18 findings (0c/12h/5m/1l/0i). Example: `lifecycle-operations-008` — Physical scope is mentioned in passing but never explicitly scoped or made optional.
- **Other / general process-quality findings** — 29 findings (0c/9h/9m/10l/1i). Example: `lifecycle-threatscenarios-003` — Planning is red-team-only; Threat Scenarios require joint planning with the blue team.
- **Purple-team close-out missing or weak** — 13 findings (4c/3h/3m/2l/1i). Example: `lifecycle-rtdeck-003` — Remediation tracking and lessons-learned capture not described || Adjacent remit (threat hunt at close, hunt support, IR support) absent || .
- **Authorization, RoE and kill-switch clarity** — 8 findings (3c/2h/3m/0l/0i). Example: `lifecycle-exercises-005` — Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words.
- **Data handling, OPSEC, and safety controls** — 12 findings (1c/3h/7m/1l/0i). Example: `lifecycle-physoc-005` — No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site.
- **Codename and theme convention** — 11 findings (0c/4h/3m/3l/1i). Example: `lifecycle-exercises-003` — Codename convention does not require the fictional-character theme.

## Top risks

| # | Severity | ID | Title | Why it matters | Owner |
|---|---|---|---|---|---|
| 1 | critical | `lifecycle-rtdeck-003` | Remediation tracking and lessons-learned capture not described \|\| Adjacent remit (threat hunt at close, hunt support, IR | Methodology should state that every engagement of every type concludes with a purple-team close-out with the blue team, used to convert offensive findings into  | Red team lead, Purple team |
| 2 | critical | `lifecycle-exercises-001` | No clean-up / environment restoration step before report sign-off \|\| Closure phase missing TIBER-EU mandated artefacts ( | A defined purple-team close-out workshop with the blue team that walks through TTPs used, detections triggered/missed, and agrees defensive improvements; mandat | Red team lead + Blue team lead |
| 3 | critical | `lifecycle-exercises-005` | Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words | Authorization section must name the legal sign-off owner, list explicit abort criteria (production impact, real incident, business event), and define a safe-wor | Red team lead + Legal/Risk |
| 4 | critical | `lifecycle-operations-003` | No purple-teaming close-out with the blue team | A mandatory joint replay / purple-team workshop with the Blue Team after every Operation, with documented attendees, agenda, detection-vs-action mapping, and ag | Red team lead / Purple team |
| 5 | critical | `lifecycle-operations-007` | Authorization phase is implicit; no legal sign-off, RoE artefact, safe-words, or abort criteria defined | An Authorization phase describing: who signs the engagement letter (legal, risk, business owner), where the RoE document lives, safe-words for abort, kill-switc | Red team lead / Legal-Risk |
| 6 | critical | `lifecycle-physoc-003` | Closure artefacts (replay, 360 feedback, remediation plan, attestation) are absent \|\| No purple-teaming close-out with b | A mandatory purple-team close-out phase that walks blue team, SOC and physical security through what was done, when, and what should have been detected or stopp | Purple team / Red team lead |
| 7 | critical | `lifecycle-physoc-005` | No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site | A documented operator safety protocol: scheduled check-ins to a named control point, abort/kill-switch wording, emergency contacts (medical, legal, in-country), | Red team lead / Legal / HR |
| 8 | critical | `lifecycle-rtmeth-003` | Authorization, Rules of Engagement, legal sign-off and kill-switch / abort criteria are not described | A methodology must define the authorization chain (sign-off authorities), the Rules of Engagement contents, safe-words, abort/kill-switch conditions, and what t | Red team lead / Legal & Risk |
| 9 | critical | `lifecycle-threatscenarios-001` | No purple-team close-out described, despite Threat Scenario format requiring blue team in the room | An explicit purple-team close-out phase where red and blue jointly walk through each scenario, discuss observed detections and controls, and agree defensive imp | Red team lead with Purple team / SOC |
| 10 | critical | `lifecycle-threatscenarios-002` | No Control Team / White Team role defined; Execution acts on production tools without a named institution-side test owne | A named authorization section identifying who signs off (system owner, CISO/Head of Security, Legal), the abort/kill-switch criteria, who can invoke them, the s | Red team lead with Legal/Risk |

## What is well covered

The corpus already shows real maturity in several areas — the report would mislead leadership if it sounded uniformly negative:

- **Deconfliction.** The deconfliction process is described consistently across the Operations and Exercises SOPs and is matched by a clear deconfliction.drawio diagram. Roles (RT/WT/BT) and the decision tree (what to share, when, under what conditions) are explicit.
- **Data-handling controls during engagements.** All three engagement SOPs and the methodology converge on a defensible data-handling protocol (encryption in transit, secure transport, PIA-sensitive data halt-and-escalate). Wording is nearly identical across docs — a sign of deliberate alignment rather than copy-drift.
- **Threat-actor modelling.** The APT taxonomy (Slide 4 of `apts-apts-private`) and the Threat Profile Examples in the methodology give the team a working language for adversary emulation, mapped to MITRE ATT&CK.
- **Research lifecycle.** `Research_Methodology` and the matching `Research_Process.drawio` diagram are tightly aligned — phases, decision points, and human-validation gates appear in both with consistent language. This is the only sub-corpus where prose and diagram agree end-to-end.
- **BloodHound Enterprise operational guidance.** The process doc gives concrete, auditable steps for tenant setup, collection scheduling, and remediation analysis — a strong example for the other tool-specific SOPs to follow.

## Recommended next steps

**Quick wins (this quarter, S-effort):**

1. Apply the curated-vocabulary rewrite set: `CTI`→`TI`, `defending teams`→`Blue Team`, `CobaltStrike`→`Cobalt Strike`, `One Note`→`OneNote`, `Bloodhound`→`BloodHound`, `Cyberark`→`CyberArk`, `Tier Zero`→`Tier 0`, repository name prefixes. Single find/replace pass across the corpus.
2. Disambiguate `PoC` (Proof of Concept vs Point of Contact) — high-risk for regulator-facing artefacts.
3. Rename Threat Scenarios `Report` section to `Closure` and align its sub-structure to the Operations/Exercises SOPs.
4. Document the codename fictional-character theme convention in all three engagement SOPs and the methodology.
5. Add `OFI = Opportunities For Improvement` to the methodology glossary and require an OFI block in every SOP's Closure phase.

**Structural changes (next quarter, M/L-effort):**

6. Add a `Purple-team close-out` subsection to each engagement-type SOP's closing phase — the methodology promises it; the SOPs do not implement it. Either author `Purple_Teaming_Process.docx` to anchor the cross-reference or rewrite the methodology to point to per-SOP sections.
7. Add a `Regulatory mapping` subsection to the methodology that expands TLPT / TIBER-EU / CBEST, summarises TIBER-EU phases (TLPT Authority, TI Provider, RT Provider, Control Team), and maps which engagement type corresponds to a regulator-mandated TLPT.
8. Add a `Tier model` subsection defining T0/T1/T2 criteria and examples; align notation across `apts` and `BloodHound_Process`.
9. Reconcile the canonical `RedTeamProcess.drawio` execution-phase taxonomy (`Preparation / Intrusion / Breach`) with the SOPs (Unified Kill Chain). Either update the diagram or add a per-engagement-type mapping table to the methodology.
10. Add an `External actors and SOC interface` subsection (methodology and/or each SOP's Deconfliction section) defining CSIRT / L1-L3 / Pentest-Assessment touchpoints with RT engagements.
11. Refresh `RedTeam_Methodology` (currently v0.3, Oct 2024 — older than every SOP it references) to v1.0: include `Physical & Social`, `Research_Methodology`, BloodHound process; pin SOP versions; add the Purple-team, Regulatory mapping, Tier model, and codename-theme subsections above.
12. Populate `references/euronext-internal-taxonomy.md` so evaluators can tag findings with `EURONEXT-INTERNAL` control IDs in future runs.

---

_Findings register: `findings-register.csv` · Themes: `themes.md` · Backlog (by owner): `remediation-backlog.md`._