# Remediation backlog — run 2026-05-13-1716

107 findings grouped by recommended owner. Within each group, items are sorted **critical → informational** then **S → L** effort (early wins first).

**How to read this:**
- Severity in brackets, effort after the slash: `[critical | M]`.
- Each line is one actionable item — click the `finding_id` to find the full evidence in `findings-register.csv`.

## Red team lead
_62 findings._

- **[high | S]** `lifecycle-bh-003` — AET role referenced but not defined in this doc or any engagement SOP. _Either expand AET on first use in this doc or in RedTeam_Methodology Glossary._
- **[high | S]** `lifecycle-physoc-003` — No codename convention named for Physical Pentest engagements. _Add a 'Codename' bullet to Planning saying the Physical Pentest receives a codename per the team theme (standalone) or inherits the parent engagement's codename._
- **[high | S]** `lifecycle-rtdeckv10-001` — RedTeaming_v1.0.pptx is content-identical to RedTeaming_v0.4.pptx minus the Scheduling chapter — likely older / shorter twin. _Rename one of the two decks to disambiguate (purpose-suffix), or retire the duplicate._
- **[high | S]** `lifecycle-threatscenarios-004` — Data-handling rules absent from Threat Scenarios SOP. _Lift the Data Handling section from Operations_Process v1._
- **[high | M]** `lifecycle-rtmeth-004` — Adjacent-remit work (threat hunting at close-out, during external engagements, during live incidents) is not described. _Add an 'Adjacent Responsibilities' section describing threat-hunt close-out, external-engagement support and incident-response support._
- **[medium | S]** `lifecycle-aptsdossier-005` — Sensitive findings recorded in deck slide rather than a tracked remediation backlog. _Migrate slide-8 items into the tracking forum chosen by the Purple Teaming process and reference Jira/Confluence IDs from this slide._
- **[medium | S]** `lifecycle-exercises-004` — Physical scope not explicitly addressed in Exercises SOP. _Add a one-line entry in Initiation Phase outputs: 'Physical scope decision (in / out) — when in scope, follow PhysicalSocial_Process v1._
- **[medium | S]** `lifecycle-operations-004` — Physical scope not explicitly addressed in Operations SOP. _Add a sentence in Research & Preparation: 'If the Operation has a physical dimension, the PhysicalSocial_Process must be followed in parallel and a Get-out-of-jail letter prepared._
- **[medium | S]** `lifecycle-operations-005` — Threat Intelligence Team not listed in Teams & Responsibilities (asymmetry with Exercises SOP). _Clarify TI team status in Operations Teams & Responsibilities to match the curated RACI._
- **[medium | S]** `lifecycle-physoc-004` — Hardware-implant inventory and recovery / clean-up steps not specified. _Add a 'Implant Inventory & Recovery' subsection to Closure (or Execution) — register every dropped item, who is to retrieve it, and confirmation when recovered._
- **[medium | S]** `lifecycle-physoc-008` — OFIs and lessons-learned not explicitly required in Closure for Physical Pentest. _Add OFI + lessons-learned to Closure with consistent wording._
- **[medium | S]** `lifecycle-physocq-002` — Discrepancy between this doc and PhysicalSocial_Process v1.3 on Questionnaire periodicity. _Pick one doc as authoritative on Questionnaire cadence (the Questionnaire SOP is the natural home) and have the other reference it; align formulas._
- **[medium | S]** `lifecycle-purpleteam-004` — Physical & Social close-out attendee list missing (Facilities, Local CISO, Physical Security). _Add attendee list to Physical & Social subsection: Local CISO, Local Facilities Manager, Physical Security lead._
- **[medium | S]** `lifecycle-research-002` — Purple Teaming step is a single short paragraph — no link to Purple_Teaming_Process v0.1. _Cross-link to Purple_Teaming_Process v0._
- **[medium | S]** `lifecycle-threatscenarios-005` — Physical scope not explicitly addressed (in or out). _Add one sentence in Scope stating that physical attacks are usually out of scope for Threat Scenarios (handled by PhysicalSocial_Process) unless the abused tool has a physical-access dimension._
- **[medium | S]** `lifecycle-threatscenarios-006` — Lessons-learned capture mechanism implicit — needs a concrete output target. _Add a line to Closure: 'Lessons-learned must be filed in the RT Research Repository under the engagement codename with the lessons-learned tag._
- **[medium | S]** `tdora-exercises-004` — White Team and Control Team conflated — TIBER-EU treats them as distinct roles. _Add a paragraph distinguishing CT (TLPT-mode) from WT (internal-mode)._
- **[medium | M]** `lifecycle-aptsdossier-002` — Operation post-mortems (Phantom Signature / Crimson Breach / Fight Club) lack purple-team and threat-hunt handover artefacts. _Either (a) link each operation slide to its Purple Team close-out output set, or (b) refactor the dossier so operation post-mortems live in a separate engagement-results register and are not interleaved with threat-actor reference material._
- **[medium | M]** `lifecycle-research-003` — Capability development has no security review / approval gate before tool moves to 'Operational'. _Add an Experimental -> Operational approval gate: peer review, lab-validation requirement, OPSEC sign-off, named approver._
- **[medium | M]** `lifecycle-rtdeckv04-001` — Stakeholder deck does not reflect v0.8 methodology — out of date on engagement-type taxonomy, codename theme, Purple Team close-out, OFIs. _Coordinated refresh once methodology v0._
- **[medium | M]** `lifecycle-rtdeckv10-002` — Stakeholder deck does not reflect v0.8 methodology — out of date on engagement-type taxonomy, codename theme, Purple Team close-out, OFIs. _Coordinated refresh once methodology v0._
- **[medium | M]** `lifecycle-rtmeth-005` — Scoping section is very short — checklist-style rather than methodology-grade. _Expand Scoping into a fuller section with the dimensions above; keep the capability self-check as a sub-bullet._
- **[low | S]** `coherence-apts-apts-private-007` — Naming drift: 'Cyberark' (vendor spells it 'CyberArk') in APTs deck Slide 8 and in BloodHound v0.5 Data Analysis. _Two targeted edits: APTs deck Slide 8 prose, and BloodHound v0._
- **[low | S]** `coherence-engagements-1-operations-006` — Engagement-SOP Process Documents sections only pin Purple Teaming; do not cross-reference the methodology or sibling SOPs. _Pick option (a) or (b) and apply consistently across the four engagement SOPs (Operations, Exercises, Threat Scenarios, PhysicalSocial)._
- **[low | S]** `coherence-engagements-3-purple-teaming-005` — Cross-reference naming drift: 'ThreatScenarios_Process_1.6.docx' missing the 'v' prefix in Purple Teaming v0.1 Process Documents list. _Single character edit on next revision._
- **[low | S]** `lifecycle-aptsdossier-003` — Operation codenames present but theme convention not visible in the dossier. _Add a footnote stating which fictional reference each codename derives from, or migrate any non-conforming names in the register._
- **[low | S]** `lifecycle-bh-005` — References 'OPLOGS recommended in the Red Team Exercises process' without version pin. _Pin the version._
- **[low | S]** `lifecycle-exercises-003` — Exercise codename theme convention correctly required. _No change._
- **[low | S]** `lifecycle-exercises-007` — Process Documents list lists only Purple_Teaming_Process. _Add ThreatScenarios_Process v1._
- **[low | S]** `lifecycle-operations-002` — Operation codename theme convention correctly required (fictional/historical character). _No change._
- **[low | S]** `lifecycle-operations-006` — Process Documents list lists only Purple_Teaming_Process — siblings not pinned. _Add ThreatScenarios_Process v1._
- **[low | S]** `lifecycle-physoc-006` — Figure 1 captioned 'Threat Scenarios Phases' in a Physical Pentest doc — copy-paste from Threat Scenarios SOP. _Fix the figure caption._
- **[low | S]** `lifecycle-physoc-007` — Process Documents list lists only Purple_Teaming_Process. _Add PhysicalSocial_Questionnaire_Process v1._
- **[low | S]** `lifecycle-physocq-004` — Vulnerability Score / Maturity formulas referenced but not rendered (likely lost in docx -> md ingest). _Render the formulas as plain text or table to survive PDF/markdown conversion; alternatively cross-reference a worked example._
- **[low | S]** `lifecycle-physocq-005` — Empty rows in Versioning table. _Editorial — trim the blank rows._
- **[low | S]** `lifecycle-purpleteam-006` — Typo: 'Engagement Type-Specifi notes' (missing final 'c'). _Fix typo before v1._
- **[low | S]** `lifecycle-purpleteam-007` — Punctuation drift in Workshop questions. _Editorial pass before v1._
- **[low | S]** `lifecycle-purpleteam-008` — Filename of Threat Scenarios SOP is missing leading 'v' (e.g. 'ThreatScenarios_Process_1.6.docx'). _Add the 'v' prefix to the version number for consistency._
- **[low | S]** `lifecycle-research-005` — Out-of-scope list excludes 'Purely defensive guidance without offensive relevance' — could exclude legitimate hunt-hypothesis sources. _Reword to 'Purely defensive guidance with no offensive-relevant signal'; keep the human reviewer judging the signal._
- **[low | S]** `lifecycle-rtdeckv04-002` — RoE bullet on slide 6 lists prohibited actions but is not anchored to a written RoE template. _Once the methodology RoE section exists, link to it from this slide._
- **[low | S]** `lifecycle-rtdeckv04-003` — Named individuals (Renato Cruz, José Barbosa) pinned in stakeholder deck — staffing churn risk. _Generalise to roles or replace with a link to a maintained team page._
- **[low | S]** `lifecycle-rtdeckv04-004` — Deck names Cobalt Strike but no OPSEC or rotation considerations are presented to stakeholders. _Add a slide summarising the team's OPSEC posture and IoC-rotation discipline for stakeholders._
- **[low | S]** `lifecycle-rtdeckv10-003` — Named individuals (Renato Cruz, José Barbosa) pinned in stakeholder deck — staffing churn risk. _Generalise to roles or link._
- **[low | S]** `lifecycle-rtmeth-006` — Process Documents list contains 'Research_Methodology_0.6.docx' missing leading 'v' (and minor). _Fix the version prefix._
- **[low | S]** `lifecycle-rtmeth-007` — Stealth / blue-team co-op matrix axes mentioned but matrix figure not rendered in markdown. _Replace the matrix figure with a 2x2 or 3x3 table in markdown so the relationship is plain even without the original visual._
- **[low | S]** `lifecycle-threatscenarios-002` — Codename theme exemption correctly documented for Threat Scenarios. _No change._
- **[low | S]** `lifecycle-threatscenarios-007` — Cross-references mention only Purple_Teaming_Process; siblings (Operations, Exercises, Methodology) not listed. _Expand the Process Documents list to include all sibling SOPs and the methodology._
- **[low | S]** `tdora-rtdeckv04-002` — Teams slide describes WT/RT/BT — does not differentiate WT (internal) from CT (TLPT). _When the deck is refreshed, add WT vs CT framing._
- **[low | M]** `coherence-methodology-redteam-methodology-001` — TIBER-EU and TLPT used without first-reference expansion across methodology + Exercises SOP. _Resolves with Tier 2 Regulatory mapping work._
- **[low | M]** `coherence-methodology-redteaming-v1-0-pptx-004` — Stakeholder decks (RedTeaming v0.4 + v1.0) still out of sync with methodology v0.8. _Carry-over from prior run finding -010._
- **[informational | S]** `lifecycle-bh-001` — Doc is a tooling-process, not an engagement SOP — engagement-lifecycle template applies only to its hand-off touchpoints. _Keep as a tooling-process doc; ensure cross-references from Operations_Process and Exercises_Process to this doc remain pinned at version._
- **[informational | S]** `lifecycle-bh-004` — Safety rules ('no ForceChangePassword on user accounts') are good — consider promoting to a methodology-level forbidden-attacks list. _Add a sentence: 'See RedTeam_Methodology v0._
- **[informational | S]** `lifecycle-exercises-001` — Mandatory Purple Team close-out present and now explicitly mapped to TLPT 360-degree feedback. _Keep close-out section cross-referenced with Purple_Teaming_Process_v0._
- **[informational | S]** `lifecycle-operations-001` — Mandatory Purple Team close-out implemented and well-tailored to assumed-breach context. _Keep close-out section pinned to Purple_Teaming_Process_v0._
- **[informational | S]** `lifecycle-physoc-001` — Purple Team close-out now mandatory for Physical Pentest — broadened to Physical Security/Facilities. _Keep close-out section pinned to Purple_Teaming_Process_v0._
- **[informational | S]** `lifecycle-physocq-001` — Doc is a Questionnaire scoring / scheduling SOP — limited overlap with engagement lifecycle template. _Continue to treat this as a scoring/scheduling instrument._
- **[informational | S]** `lifecycle-purpleteam-001` — Strong v0.1 skeleton — close-out is now the team's documented joint output for every engagement. _Continue to v1._
- **[informational | S]** `lifecycle-research-001` — Research methodology is well-structured (Intake / Repository / Deep Dive / Capability Dev / Engagement / Feedback). _Hold._
- **[informational | S]** `lifecycle-rtmeth-001` — Five engagement types now enumerated, including Purple Teaming and Physical & Social. _Hold — keep cross-references pinned at version on each SOP revision._
- **[informational | S]** `lifecycle-rtmeth-002` — Codename convention now codified at methodology level. _Hold._
- **[informational | S]** `lifecycle-threatscenarios-001` — Mandatory Purple Team close-out now present and aligned with Purple_Teaming_Process_v0.1. _Keep close-out section pinned to Purple_Teaming_Process_v0._
- **[informational | S]** `tdora-bh-001` — Tooling SOP — does not claim TLPT alignment; reduced TLPT review applies. _Hold._

## Red team lead + Legal-Risk
_28 findings._

- **[critical | M]** `lifecycle-exercises-002` — Authorization chain still incomplete — no sign-off owner, kill-switch or abort criteria. _Add an Authorization & RoE subsection covering sign-off owner, abort criteria, kill-switch procedure, safe-word and escalation chain (Tier 1._
- **[critical | M]** `lifecycle-operations-003` — Authorization chain incomplete — no documented sign-off, kill-switch or abort criteria. _Add a dedicated 'Authorization & Rules of Engagement' subsection to Research & Preparation (Tier 1._
- **[critical | M]** `lifecycle-threatscenarios-003` — Authorization chain absent — no sign-off owner, kill-switch, safe-words or abort criteria. _Add an 'Authorization & Rules of Engagement' subsection to Planning, covering sign-off owner, abort criteria, kill-switch, safe-words and escalation contacts._
- **[critical | L]** `lifecycle-rtmeth-003` — Methodology has no authorization-chain section — no methodology-level RoE template, kill-switch, or signoff model. _Add an 'Authorization & Rules of Engagement' section to the methodology that the SOPs reference._
- **[high | M]** `lifecycle-physoc-002` — Authorization letter present but operator safety controls (kill-switch, safe-word, abort criteria) absent. _Add an 'Operator Safety & Abort Criteria' subsection to Planning covering kill-switch, safe-word, abort criteria, duress protocol, and a regular check-in cadence with the Local CISO._
- **[high | M]** `tdora-aptsdossier-001` — Deck displays 'TLPT RED' classification but no supporting TLPT artefacts are present in the corpus. _Either downgrade the classification banner on these slides if the engagements were not TLPT, or attach the regulator-mandated artefact set (TTI report, attestation, lead-overseer notice) to the operation summaries._
- **[high | M]** `tdora-exercises-002` — TIBER-EU Preparation actors (Control Team, RT Provider, TI Provider) not named in Initiation. _Add a 'TLPT alignment' callout to Initiation listing the Control Team, TI Provider and lead-overseer engagement when the Exercise is run as TLPT._
- **[high | M]** `tdora-operations-003` — No documented kill-switch / abort criteria — would fail DORA risk-management-of-testing examination. _Tier 1._
- **[high | M]** `tdora-rtmeth-002` — No Control Team / TI Provider / Lead Overseer references anywhere in the methodology. _Add a 'TLPT role mapping' subsection naming TCT, CT, TI Provider, RT Provider, WT and the financial entity, with notes on how each maps to existing Euronext teams._
- **[high | L]** `tdora-rtmeth-001` — Exercises described as 'well-planned and aligned with TIBER-EU' but methodology never expands what that alignment entails. _Add a 'Regulatory Mapping' section explaining TIBER-EU and DORA TLPT alignment: the four TIBER-EU phases, the regulator-mandated actors, when an Exercise qualifies as TLPT, and what additional artefacts must be produced._
- **[medium | S]** `lifecycle-physocq-003` — No data handling rules for Questionnaire responses (which include photos, floor plans, CCTV info). _Add a Response Handling subsection specifying storage location, access (least-privilege), retention and destruction._
- **[medium | S]** `lifecycle-purpleteam-002` — Tracking forum left generic ('typically the Red Team Research Repository or the security risk register'). _Pin forum at v1._
- **[medium | S]** `tdora-bh-002` — Continuous AD enumeration against prod could intersect DORA risk-management-of-testing — relationship not stated. _Add a 'Risk Management' note in v0._
- **[medium | S]** `tdora-exercises-003` — TTI phase performed by 'the RT team' — RTS on TLPT requires independent TI provider for TLPT. _Add a 'When run as TLPT' callout: 'the Targeted Threat Intelligence report is authored by an independent TI provider distinct from the Red Team provider; the internal RT may participate in scoping and review only._
- **[medium | S]** `tdora-research-002` — Operational tooling used against prod has no documented testing-risk-management linkage to DORA. _Add the cross-reference; verify clause against live DORA._
- **[medium | M]** `lifecycle-physoc-005` — Data handling rules absent for Physical & Social engagement. _Lift the Data Handling pattern from Operations_Process v1._
- **[medium | M]** `tdora-purpleteam-001` — Doc never references TIBER-EU 360-degree feedback / DORA closure attestation. _Add a 'TLPT close-out' subsection in v1._
- **[medium | M]** `tdora-rtdeckv04-001` — Stakeholder deck never mentions TIBER-EU or DORA TLPT despite being a Red Teaming overview. _Add a stakeholder-friendly 'How this relates to TIBER-EU / DORA TLPT' slide that names regulator-mandated actors and the closure attestation._
- **[medium | M]** `tdora-rtdeckv10-001` — Stakeholder deck v1.0 never mentions TIBER-EU or DORA TLPT (same gap as v0.4). _Same as for v0._
- **[medium | L]** `tdora-aptsdossier-003` — Operation post-mortems lack DORA-style closure artefacts (test summary, attestation, regulator notification). _Clarify the regulatory status of each historical operation; for any that should have been TLPT, retrospectively capture the test report and attestation._
- **[low | S]** `lifecycle-research-004` — AI Enrichment layer outputs are trusted without describing model risk / hallucination controls. _Add a short subsection on AI model-risk controls (citation requirement, hallucination signalling)._
- **[low | S]** `lifecycle-rtmeth-008` — Forbidden-attacks list useful but does not name an owner / waiver procedure. _Add an owner and waiver path for the Forbidden Attacks list (e._
- **[low | S]** `tdora-physocq-002` — Criticality assignment hangs off the CMDB without defining the field or owner. _Add a line naming the CMDB criticality field / owner, and ideally cross-reference the Euronext 'critical or important functions' register._
- **[low | S]** `tdora-purpleteam-002` — Outputs list does not include the test summary report / attestation that DORA TLPT requires. _Extend Outputs & Tracking in v1._
- **[informational | S]** `tdora-operations-001` — Operations correctly positioned as internal, not TLPT. _Optional: add a single sentence in Introduction stating 'Operations are internal exercises and must not be presented as TLPT (DORA Art._
- **[informational | S]** `tdora-physoc-001` — Physical & Social SOP correctly does not claim TLPT alignment. _When a Physical Pentest is run as a leg of a TLPT Exercise, ensure attendance of the Control Team and signoff from the TIBER Cyber Team / lead overseer; current SOP does not address this nesting._
- **[informational | S]** `tdora-purpleteam-003` — Could add a TLPT engagement-type-specific note (replay-walkthrough emphasis). _Add a 'TLPT' subsection covering replay walkthrough, ATT&CK-mapped test report, and joint attestation signatories._
- **[informational | S]** `tdora-threatscenarios-001` — Threat Scenarios are correctly NOT presented as TLPT — internal use only. _No change._

## Red team lead + Threat hunt
_3 findings._

- **[medium | S]** `lifecycle-exercises-005` — Threat-hunt handover only implicit (inside Purple Team close-out artefacts). _Add a 'Threat-Hunt Handover' subsection naming the recipient, deliverable and SLA — mirrors recommendation in Operations finding._
- **[medium | S]** `lifecycle-operations-007` — Threat-hunt handover delegated to Purple Team close-out — could be explicit. _Add a 'Threat-Hunt Handover' subsection naming the recipient (SOC threat-hunt function), the deliverable (hunt-hypothesis list) and a target acknowledgement SLA._
- **[medium | S]** `lifecycle-purpleteam-003` — Only two teams listed (RT and BT) — Threat Hunt function not given a role despite hunt-hypothesis output. _Add a sentence in Teams & Responsibilities clarifying which role on the BT side owns the hunt-hypothesis list and the consumption SLA._

## Legal-Risk
_4 findings._

- **[medium | S]** `tdora-operations-002` — Data-handling rules present but GDPR / DORA wording not explicit. _Add a one-line reference to GDPR legal basis and DORA risk-management-of-test obligations in Data Handling._
- **[medium | S]** `tdora-rtmeth-004` — Data-handling rules present but no GDPR / DORA anchoring. _Add a one-line reference to GDPR / DORA in Data Handling._
- **[informational | S]** `tdora-physocq-001` — Questionnaire is an assessment instrument, not a TLPT artefact — out of TLPT scope. _Optionally add a one-line statement: 'This Questionnaire feeds the Euronext physical-security maturity baseline and contributes to DORA basic operational-resilience-testing evidence for physical critical functions; it is not a TLPT instrument._
- **[informational | S]** `tdora-threatscenarios-002` — Closure could explicitly note that Threat Scenarios are usable as DORA operational-resilience-testing evidence (not TLPT). _Add a sentence to Closure positioning the Threat Scenario report as DORA basic-testing evidence, not TLPT._

## Threat intel
_3 findings._

- **[medium | S]** `tdora-exercises-006` — No Generic Threat Landscape (GTL) reference in Preparation. _Add a sentence in Initiation referencing the relevant GTL (e._
- **[low | S]** `lifecycle-aptsdossier-004` — APT38 legend reuses APT28 wording (copy-paste artefact). _Fix the legend wording on slide 7 and audit the other actor slides for similar copy-paste errors._
- **[informational | S]** `lifecycle-aptsdossier-001` — APT dossier is a threat-intel artefact, not a process doc — scope-limited for lifecycle review. _Treat this artefact as a threat-actor input to the Targeted Threat Intelligence phase of Exercises; defer detailed evaluation to a research-process or attack-coverage evaluator._

## Legal-Risk (+ Red team lead)
_1 findings._

- **[medium | M]** `tdora-physoc-003` — GDPR-grade data-protection rules absent for physical / social engineering captures. _Add a Data Handling subsection covering personal-data captures, sock-puppet account hygiene, badge-clone data destruction and retention._

## Red team lead + SOC
_1 findings._

- **[medium | S]** `lifecycle-bh-002` — SOC notification is one-line — no contact, channel, frequency or escalation defined. _Expand the SOC notification line into a small deconfliction subsection (owner, channel, refresh cadence, change-management)._

## Red team lead + AET lead
_1 findings._

- **[medium | M]** `coherence-methodology-bloodhoundenterprise-002` — AET still has no charter / RACI doc — 'fully managed by AET' remains an orphan-actor reference. _Carry-over from prior run finding -009._

## Red team lead + SOC manager
_1 findings._

- **[medium | M]** `coherence-resources-diagrams-soc-rt-communications-003` — Orphan actors persist in SOC-RT comms diagram: CSIRT, L1/L2/L3, Pentest/Assessment. _Carry-over from prior run finding -011._

## Red team lead + Purple team
_1 findings._

- **[low | M]** `lifecycle-purpleteam-005` — Workshop step 'Group findings by control family' lists examples but no canonical list. _Either reference ATT&CK Mitigation taxonomy or list the canonical Euronext control families in an Annex._

## Threat intel + Legal-Risk
_1 findings._

- **[informational | M]** `tdora-aptsdossier-002` — APT dossier is a strong input for TIBER-EU Targeted Threat Intelligence but is not linked to any TTI deliverable. _If/when Euronext positions an Exercise as a TLPT, ensure the TTI report references this dossier (or its successor) explicitly and that the TI provider is independent of the Red Team — verify against the live RTS on TLPT._

## Threat intel + Red team lead
_1 findings._

- **[informational | S]** `tdora-research-001` — Research process is a candidate input to TIBER-EU Targeted Threat Intelligence — not currently positioned that way. _Add the framing sentence in Process Overview._
