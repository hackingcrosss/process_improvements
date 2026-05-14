# Themes — run 2026-05-13-1716

107 findings cluster into 9 themes. Themes are sorted by aggregate severity weight (critical=5, high=4, medium=3, low=2, informational=1) and then by count.

## TIBER-EU / DORA TLPT regulatory mapping

_27 findings — 4 high, 10 medium, 3 low, 10 informational._

Methodology v0.8 mentions TIBER-EU but lacks a Regulatory Mapping section. Exercises v1.6 Closure aligns with TIBER-EU Closure; Initiation does not name Control Team, TI Provider independence, or lead-overseer engagement. Largest theme — most are medium / low and consolidate well into a single Tier 2 deliverable.

**Contributing findings:**

- `tdora-aptsdossier-001` (high, M) — Deck displays 'TLPT RED' classification but no supporting TLPT artefacts are present in the corpus
- `tdora-exercises-002` (high, M) — TIBER-EU Preparation actors (Control Team, RT Provider, TI Provider) not named in Initiation
- `tdora-rtmeth-001` (high, L) — Exercises described as 'well-planned and aligned with TIBER-EU' but methodology never expands what that alignment entails
- `tdora-rtmeth-002` (high, M) — No Control Team / TI Provider / Lead Overseer references anywhere in the methodology
- `tdora-aptsdossier-003` (medium, L) — Operation post-mortems lack DORA-style closure artefacts (test summary, attestation, regulator notification)
- `tdora-exercises-003` (medium, S) — TTI phase performed by 'the RT team' — RTS on TLPT requires independent TI provider for TLPT
- `tdora-exercises-004` (medium, S) — White Team and Control Team conflated — TIBER-EU treats them as distinct roles
- `tdora-exercises-006` (medium, S) — No Generic Threat Landscape (GTL) reference in Preparation
- `tdora-operations-002` (medium, S) — Data-handling rules present but GDPR / DORA wording not explicit
- `tdora-purpleteam-001` (medium, M) — Doc never references TIBER-EU 360-degree feedback / DORA closure attestation
- `tdora-research-002` (medium, S) — Operational tooling used against prod has no documented testing-risk-management linkage to DORA
- `tdora-rtdeckv04-001` (medium, M) — Stakeholder deck never mentions TIBER-EU or DORA TLPT despite being a Red Teaming overview
- `tdora-rtdeckv10-001` (medium, M) — Stakeholder deck v1.0 never mentions TIBER-EU or DORA TLPT (same gap as v0.4)
- `tdora-rtmeth-004` (medium, S) — Data-handling rules present but no GDPR / DORA anchoring
- `coherence-methodology-redteam-methodology-001` (low, M) — TIBER-EU and TLPT used without first-reference expansion across methodology + Exercises SOP
- `tdora-purpleteam-002` (low, S) — Outputs list does not include the test summary report / attestation that DORA TLPT requires
- `tdora-rtdeckv04-002` (low, S) — Teams slide describes WT/RT/BT — does not differentiate WT (internal) from CT (TLPT)
- `lifecycle-exercises-001` (informational, S) — Mandatory Purple Team close-out present and now explicitly mapped to TLPT 360-degree feedback
- `tdora-aptsdossier-002` (informational, M) — APT dossier is a strong input for TIBER-EU Targeted Threat Intelligence but is not linked to any TTI deliverable
- `tdora-bh-001` (informational, S) — Tooling SOP — does not claim TLPT alignment; reduced TLPT review applies
- `tdora-operations-001` (informational, S) — Operations correctly positioned as internal, not TLPT
- `tdora-physoc-001` (informational, S) — Physical & Social SOP correctly does not claim TLPT alignment
- `tdora-physocq-001` (informational, S) — Questionnaire is an assessment instrument, not a TLPT artefact — out of TLPT scope
- `tdora-purpleteam-003` (informational, S) — Could add a TLPT engagement-type-specific note (replay-walkthrough emphasis)
- `tdora-research-001` (informational, S) — Research process is a candidate input to TIBER-EU Targeted Threat Intelligence — not currently positioned that way
- `tdora-threatscenarios-001` (informational, S) — Threat Scenarios are correctly NOT presented as TLPT — internal use only
- `tdora-threatscenarios-002` (informational, S) — Closure could explicitly note that Threat Scenarios are usable as DORA operational-resilience-testing evidence (not TLPT)

## Naming & acronym consistency

_25 findings — 3 high, 8 medium, 11 low, 3 informational._

8 of 12 prior coherence findings closed (cleanup-pass landed). Remaining drift is small-scale: `Cyberark` casing in two docs, asymmetry between SOP and methodology Process Documents indices, TLPT / TIBER-EU first-use expansion, minor Purple Teaming v0.1 References slip (missing `v` prefix).

**Contributing findings:**

- `lifecycle-bh-003` (high, S) — AET role referenced but not defined in this doc or any engagement SOP
- `lifecycle-physoc-003` (high, S) — No codename convention named for Physical Pentest engagements
- `lifecycle-threatscenarios-004` (high, S) — Data-handling rules absent from Threat Scenarios SOP
- `lifecycle-bh-002` (medium, S) — SOC notification is one-line — no contact, channel, frequency or escalation defined
- `lifecycle-physoc-004` (medium, S) — Hardware-implant inventory and recovery / clean-up steps not specified
- `lifecycle-physoc-008` (medium, S) — OFIs and lessons-learned not explicitly required in Closure for Physical Pentest
- `lifecycle-physocq-003` (medium, S) — No data handling rules for Questionnaire responses (which include photos, floor plans, CCTV info)
- `lifecycle-purpleteam-002` (medium, S) — Tracking forum left generic ('typically the Red Team Research Repository or the security risk register')
- `lifecycle-rtmeth-005` (medium, M) — Scoping section is very short — checklist-style rather than methodology-grade
- `lifecycle-threatscenarios-005` (medium, S) — Physical scope not explicitly addressed (in or out)
- `tdora-bh-002` (medium, S) — Continuous AD enumeration against prod could intersect DORA risk-management-of-testing — relationship not stated
- `coherence-apts-apts-private-007` (low, S) — Naming drift: 'Cyberark' (vendor spells it 'CyberArk') in APTs deck Slide 8 and in BloodHound v0.5 Data Analysis
- `lifecycle-aptsdossier-003` (low, S) — Operation codenames present but theme convention not visible in the dossier
- `lifecycle-bh-005` (low, S) — References 'OPLOGS recommended in the Red Team Exercises process' without version pin
- `lifecycle-exercises-003` (low, S) — Exercise codename theme convention correctly required
- `lifecycle-operations-002` (low, S) — Operation codename theme convention correctly required (fictional/historical character)
- `lifecycle-purpleteam-005` (low, M) — Workshop step 'Group findings by control family' lists examples but no canonical list
- `lifecycle-purpleteam-006` (low, S) — Typo: 'Engagement Type-Specifi notes' (missing final 'c')
- `lifecycle-purpleteam-007` (low, S) — Punctuation drift in Workshop questions
- `lifecycle-research-004` (low, S) — AI Enrichment layer outputs are trusted without describing model risk / hallucination controls
- `lifecycle-rtmeth-007` (low, S) — Stealth / blue-team co-op matrix axes mentioned but matrix figure not rendered in markdown
- `tdora-physocq-002` (low, S) — Criticality assignment hangs off the CMDB without defining the field or owner
- `lifecycle-bh-001` (informational, S) — Doc is a tooling-process, not an engagement SOP — engagement-lifecycle template applies only to its hand-off touchpoints
- `lifecycle-bh-004` (informational, S) — Safety rules ('no ForceChangePassword on user accounts') are good — consider promoting to a methodology-level forbidden-attacks list
- `lifecycle-rtmeth-002` (informational, S) — Codename convention now codified at methodology level

## Purple-team close-out residuals

_17 findings — 10 medium, 2 low, 5 informational._

Tier 1.1 work landed (all 4 SOPs now have Purple Team Close-Out subsections pointing at `Purple_Teaming_Process_v0.1.docx`). Residuals here are mostly evidence-light Close-Out descriptions and small inconsistencies between SOP wording — short-effort cleanup.

**Contributing findings:**

- `lifecycle-aptsdossier-002` (medium, M) — Operation post-mortems (Phantom Signature / Crimson Breach / Fight Club) lack purple-team and threat-hunt handover artefacts
- `lifecycle-aptsdossier-005` (medium, S) — Sensitive findings recorded in deck slide rather than a tracked remediation backlog
- `lifecycle-exercises-004` (medium, S) — Physical scope not explicitly addressed in Exercises SOP
- `lifecycle-exercises-005` (medium, S) — Threat-hunt handover only implicit (inside Purple Team close-out artefacts)
- `lifecycle-operations-004` (medium, S) — Physical scope not explicitly addressed in Operations SOP
- `lifecycle-operations-007` (medium, S) — Threat-hunt handover delegated to Purple Team close-out — could be explicit
- `lifecycle-purpleteam-004` (medium, S) — Physical & Social close-out attendee list missing (Facilities, Local CISO, Physical Security)
- `lifecycle-research-002` (medium, S) — Purple Teaming step is a single short paragraph — no link to Purple_Teaming_Process v0.1
- `lifecycle-rtdeckv04-001` (medium, M) — Stakeholder deck does not reflect v0.8 methodology — out of date on engagement-type taxonomy, codename theme, Purple Team close-out, OFIs
- `lifecycle-rtdeckv10-002` (medium, M) — Stakeholder deck does not reflect v0.8 methodology — out of date on engagement-type taxonomy, codename theme, Purple Team close-out, OFIs
- `coherence-engagements-1-operations-006` (low, S) — Engagement-SOP Process Documents sections only pin Purple Teaming; do not cross-reference the methodology or sibling SOPs
- `coherence-engagements-3-purple-teaming-005` (low, S) — Cross-reference naming drift: 'ThreatScenarios_Process_1.6.docx' missing the 'v' prefix in Purple Teaming v0.1 Process Documents list
- `lifecycle-operations-001` (informational, S) — Mandatory Purple Team close-out implemented and well-tailored to assumed-breach context
- `lifecycle-physoc-001` (informational, S) — Purple Team close-out now mandatory for Physical Pentest — broadened to Physical Security/Facilities
- `lifecycle-purpleteam-001` (informational, S) — Strong v0.1 skeleton — close-out is now the team's documented joint output for every engagement
- `lifecycle-rtmeth-001` (informational, S) — Five engagement types now enumerated, including Purple Teaming and Physical & Social
- `lifecycle-threatscenarios-001` (informational, S) — Mandatory Purple Team close-out now present and aligned with Purple_Teaming_Process_v0.1

## Authorization chain & Rules of Engagement (Tier 1.2)

_9 findings — 4 critical, 2 high, 1 medium, 2 low._

Sign-off owner, kill-switch, safe-words, abort criteria, escalation contact list. The user's Tier 1.2 work has not yet landed in any SOP or in the methodology. All 4 critical findings cluster here; one applies to each engagement SOP and the methodology-level RoE template.

**Contributing findings:**

- `lifecycle-exercises-002` (critical, M) — Authorization chain still incomplete — no sign-off owner, kill-switch or abort criteria
- `lifecycle-operations-003` (critical, M) — Authorization chain incomplete — no documented sign-off, kill-switch or abort criteria
- `lifecycle-rtmeth-003` (critical, L) — Methodology has no authorization-chain section — no methodology-level RoE template, kill-switch, or signoff model
- `lifecycle-threatscenarios-003` (critical, M) — Authorization chain absent — no sign-off owner, kill-switch, safe-words or abort criteria
- `lifecycle-physoc-002` (high, M) — Authorization letter present but operator safety controls (kill-switch, safe-word, abort criteria) absent
- `tdora-operations-003` (high, M) — No documented kill-switch / abort criteria — would fail DORA risk-management-of-testing examination
- `lifecycle-research-003` (medium, M) — Capability development has no security review / approval gate before tool moves to 'Operational'
- `lifecycle-rtdeckv04-002` (low, S) — RoE bullet on slide 6 lists prohibited actions but is not anchored to a written RoE template
- `lifecycle-rtmeth-008` (low, S) — Forbidden-attacks list useful but does not name an owner / waiver procedure

## Process quality & completeness

_14 findings — 3 medium, 9 low, 2 informational._

Catch-all for evidence-handling, OPSEC, reporting, lessons-learned, RACI ambiguity. Most are medium / low and can be batched with theme owners.

**Contributing findings:**

- `coherence-methodology-bloodhoundenterprise-002` (medium, M) — AET still has no charter / RACI doc — 'fully managed by AET' remains an orphan-actor reference
- `coherence-resources-diagrams-soc-rt-communications-003` (medium, M) — Orphan actors persist in SOC-RT comms diagram: CSIRT, L1/L2/L3, Pentest/Assessment
- `lifecycle-operations-005` (medium, S) — Threat Intelligence Team not listed in Teams & Responsibilities (asymmetry with Exercises SOP)
- `lifecycle-aptsdossier-004` (low, S) — APT38 legend reuses APT28 wording (copy-paste artefact)
- `lifecycle-physoc-006` (low, S) — Figure 1 captioned 'Threat Scenarios Phases' in a Physical Pentest doc — copy-paste from Threat Scenarios SOP
- `lifecycle-physocq-005` (low, S) — Empty rows in Versioning table
- `lifecycle-purpleteam-008` (low, S) — Filename of Threat Scenarios SOP is missing leading 'v' (e.g. 'ThreatScenarios_Process_1.6.docx')
- `lifecycle-research-005` (low, S) — Out-of-scope list excludes 'Purely defensive guidance without offensive relevance' — could exclude legitimate hunt-hypothesis sources
- `lifecycle-rtdeckv04-004` (low, S) — Deck names Cobalt Strike but no OPSEC or rotation considerations are presented to stakeholders
- `lifecycle-rtmeth-006` (low, S) — Process Documents list contains 'Research_Methodology_0.6.docx' missing leading 'v' (and minor)
- `lifecycle-threatscenarios-002` (low, S) — Codename theme exemption correctly documented for Threat Scenarios
- `lifecycle-threatscenarios-007` (low, S) — Cross-references mention only Purple_Teaming_Process; siblings (Operations, Exercises, Methodology) not listed
- `lifecycle-aptsdossier-001` (informational, S) — APT dossier is a threat-intel artefact, not a process doc — scope-limited for lifecycle review
- `lifecycle-research-001` (informational, S) — Research methodology is well-structured (Intake / Repository / Deep Dive / Capability Dev / Engagement / Feedback)

## Physical & Social engagement completeness

_7 findings — 2 medium, 4 low, 1 informational._

Physical & Social SOP v1.3 carries an Authorization Letter and has codename treatment, but operator safety controls (kill-switch, safe-word) and Questionnaire / Process disagreement on cadence remain. Highest single physical-track risk is operator safety.

**Contributing findings:**

- `lifecycle-physoc-005` (medium, M) — Data handling rules absent for Physical & Social engagement
- `lifecycle-physocq-002` (medium, S) — Discrepancy between this doc and PhysicalSocial_Process v1.3 on Questionnaire periodicity
- `lifecycle-exercises-007` (low, S) — Process Documents list lists only Purple_Teaming_Process
- `lifecycle-operations-006` (low, S) — Process Documents list lists only Purple_Teaming_Process — siblings not pinned
- `lifecycle-physoc-007` (low, S) — Process Documents list lists only Purple_Teaming_Process
- `lifecycle-physocq-004` (low, S) — Vulnerability Score / Maturity formulas referenced but not rendered (likely lost in docx -> md ingest)
- `lifecycle-physocq-001` (informational, S) — Doc is a Questionnaire scoring / scheduling SOP — limited overlap with engagement lifecycle template

## APTs classification banner without supporting TLPT artefacts

_3 findings — 1 high, 2 medium._

Private APTs dossier stamps 'TLPT RED' classification but has no Control Team, TI Provider independence note, or attestation evidence. Either remove the banner or build the supporting artefacts.

**Contributing findings:**

- `lifecycle-rtdeckv10-001` (high, S) — RedTeaming_v1.0.pptx is content-identical to RedTeaming_v0.4.pptx minus the Scheduling chapter — likely older / shorter twin
- `lifecycle-threatscenarios-006` (medium, S) — Lessons-learned capture mechanism implicit — needs a concrete output target
- `tdora-physoc-003` (medium, M) — GDPR-grade data-protection rules absent for physical / social engineering captures

## Threat-hunt, IR support & SOC interface

_2 findings — 1 high, 1 medium._

Adjacent remit (threat hunting at engagement close-out, during external engagements, during live incidents) is not documented in any process doc; SOC interface diagram has actors not described in prose. Tier 3 structural work.

**Contributing findings:**

- `lifecycle-rtmeth-004` (high, M) — Adjacent-remit work (threat hunting at close-out, during external engagements, during live incidents) is not described
- `lifecycle-purpleteam-003` (medium, S) — Only two teams listed (RT and BT) — Threat Hunt function not given a role despite hunt-hypothesis output

## Duplicate / drifted stakeholder decks

_3 findings — 3 low._

`RedTeaming_v1.0.pptx` is content-identical to `RedTeaming_v0.4.pptx` minus the Scheduling chapter. Likely a fork that needs reconciling — retire one and pin the survivor in the methodology Process Documents index.

**Contributing findings:**

- `coherence-methodology-redteaming-v1-0-pptx-004` (low, M) — Stakeholder decks (RedTeaming v0.4 + v1.0) still out of sync with methodology v0.8
- `lifecycle-rtdeckv04-003` (low, S) — Named individuals (Renato Cruz, José Barbosa) pinned in stakeholder deck — staffing churn risk
- `lifecycle-rtdeckv10-003` (low, S) — Named individuals (Renato Cruz, José Barbosa) pinned in stakeholder deck — staffing churn risk
