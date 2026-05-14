# Themes — Run 2026-05-11-1417

Clusters of findings that share an underlying weakness. Within each theme, findings are sorted by severity then artefact.

## TIBER-EU / DORA TLPT misalignment (83 findings)
_Severity mix: critical: 9, high: 31, medium: 25, low: 8, informational: 10_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, Exercises_Process_v1.1.docx, Operations_Process_v1.0.docx, PhysicalSocial_Process_v1.0.docx, PhysicalSocial_Questionnaire_Process_v1.0.docx, RedTeam_Methodology_v0.3.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-threatscenarios-001` (critical, ThreatScenarios_Process_v1.1.docx) — No purple-team close-out described, despite Threat Scenario format requiring blue team in the room
- `lifecycle-threatscenarios-002` (critical, ThreatScenarios_Process_v1.1.docx) — No authorization / Rules-of-Engagement section: no legal sign-off, no kill-switch, no abort criteria [merged: lifecycle-threatscenarios-002, tdora-threatscenarios-004, tdora-threatscenarios-007]
- `lifecycle-operations-003` (critical, Operations_Process_v1.0.docx) — No purple-teaming close-out with the blue team
- `lifecycle-operations-007` (critical, Operations_Process_v1.0.docx) — Authorization phase is implicit; no legal sign-off, RoE artefact, safe-words, or abort criteria defined
- `lifecycle-exercises-001` (critical, Exercises_Process_v1.1.docx) — No mandatory purple-team close-out / replay with the blue team [merged: lifecycle-exercises-001, lifecycle-exercises-002, lifecycle-exercises-006, lifecycle-exercises-017, tdora-exercises-005]
- `lifecycle-rtmeth-003` (critical, RedTeam_Methodology_v0.3.docx) — Authorization, Rules of Engagement, legal sign-off and kill-switch / abort criteria are not described
- `tdora-rtmeth-002` (critical, RedTeam_Methodology_v0.3.docx) — TIBER-EU Preparation elements absent: GTL, scoping doc, engagement letter, critical-functions ID, provider procurement [merged: tdora-rtmeth-002, tdora-rtmeth-004, tdora-rtmeth-005, tdora-rtmeth-006]
- `lifecycle-physoc-003` (critical, PhysicalSocial_Process_v1.0.docx) — No purple-teaming close-out with blue team and physical security [merged: lifecycle-physoc-003, tdora-physoc-005]
- `tdora-physoc-002` (critical, PhysicalSocial_Process_v1.0.docx) — All four TIBER-EU phases are absent for the physical leg [merged: lifecycle-physoc-004, lifecycle-physoc-014, lifecycle-physoc-016, tdora-physoc-002]
- `tdora-threatscenarios-002` (high, ThreatScenarios_Process_v1.1.docx) — Document does not state that Threat Scenarios are not TLPT, leaving a misalignment risk if cited as DORA evidence
- `lifecycle-operations-004` (high, Operations_Process_v1.0.docx) — No threat-hunt handover from red findings [merged: lifecycle-operations-004, lifecycle-operations-005, lifecycle-operations-006, tdora-operations-004]
- `tdora-operations-002` (high, Operations_Process_v1.0.docx) — 'White Team' role conflates TIBER-EU White Team and Control Team responsibilities
- `lifecycle-exercises-004` (high, Exercises_Process_v1.1.docx) — Physical scope not explicitly addressed (in or out of scope) [merged: lifecycle-exercises-004, tdora-exercises-008]
- `lifecycle-exercises-008` (high, Exercises_Process_v1.1.docx) — Initiation phase blurs scoping and authorization, lacks engagement letter / RoE sign-off gate
- `tdora-exercises-002` (high, Exercises_Process_v1.1.docx) — TIBER-EU Preparation phase elements (GTL, engagement letter, critical-functions identification, provider procurement) only partially present
- `tdora-exercises-003` (high, Exercises_Process_v1.1.docx) — Threat Intelligence provider independence not addressed; TI and RT appear conflated
- `tdora-exercises-004` (high, Exercises_Process_v1.1.docx) — White Team described, but no Control Team distinct from White Team / no TIBER Cyber Team / TCT engagement
- `tdora-exercises-006` (high, Exercises_Process_v1.1.docx) — No coordination with competent authority / lead overseer described
- `tdora-exercises-007` (high, Exercises_Process_v1.1.docx) — Tester requirements (DORA Art.27) not addressed: internal vs external testers, qualifications, rotation
- `tdora-exercises-009` (high, Exercises_Process_v1.1.docx) — Risk-management of the test itself underspecified: no kill-switch, no safe-harbours / indemnities, no rollback plan
- `lifecycle-bhe-003` (high, BloodhoundEnterprise_Process_v0.1.docx) — No data-handling, retention or classification rules for collected AD/Entra graph data
- `lifecycle-bhe-004` (high, BloodhoundEnterprise_Process_v0.1.docx) — Tenant access uses application accounts only; SAML/SSO and MFA not yet implemented
- `lifecycle-bhe-007` (high, BloodhoundEnterprise_Process_v0.1.docx) — No purple-team close-out / blue-team handover for BHE-derived findings [merged: lifecycle-bhe-007, lifecycle-bhe-008, lifecycle-bhe-014, tdora-bhe-002]
- `lifecycle-rtmeth-002` (high, RedTeam_Methodology_v0.3.docx) — Codename convention (mandatory codename, fictional-character theme for Exercises and Operations) is absent [merged: lifecycle-rtmeth-002, lifecycle-rtmeth-005, lifecycle-rtmeth-006, lifecycle-rtmeth-008, lifecycle-rtmeth-009, lifecycle-rtmeth-020]
- `lifecycle-rtmeth-004` (high, RedTeam_Methodology_v0.3.docx) — Purple-teaming close-out described as conditional collaboration, not as a mandatory close-out for every engagement [merged: lifecycle-rtmeth-004, tdora-rtmeth-011]
- `tdora-rtmeth-003` (high, RedTeam_Methodology_v0.3.docx) — Threat Intelligence phase: no Targeted Threat Intelligence (TTI) report, no independent TI provider, no scenario-derivation method [merged: lifecycle-rtmeth-013, tdora-rtmeth-003]
- `lifecycle-rtmeth-014` (high, RedTeam_Methodology_v0.3.docx) — Scoping section is a 4-bullet capability checklist; lacks asset/criticality scoping, exclusions, and target selection method
- `tdora-rtmeth-001` (high, RedTeam_Methodology_v0.3.docx) — Methodology calls Exercises 'TIBER-Like' without committing to the TIBER-EU phase model or DORA TLPT requirements
- `tdora-rtmeth-007` (high, RedTeam_Methodology_v0.3.docx) — Risk management of the test itself: no kill-switch, no rollback / safe-harbour clauses, no formal indemnity for testers
- `tdora-rtmeth-008` (high, RedTeam_Methodology_v0.3.docx) — Data Handling references US 'Privacy of Information Act (PIA)' — no GDPR / DORA legal basis cited
- `tdora-rtmeth-009` (high, RedTeam_Methodology_v0.3.docx) — Scoping does not reference DORA 'critical or important functions' nor commit to live-production testing under controls
- `lifecycle-research-007` (high, Research_Methodology_v0.2.docx) — Research methodology silent on threat-hunt hypothesis generation as a deliberate output
- `lifecycle-physoc-001` (high, PhysicalSocial_Process_v1.0.docx) — Physical/social process is not linked to the Exercise / Operation / Threat-Scenario engagement taxonomy [merged: lifecycle-physoc-001, lifecycle-physoc-010]
- `lifecycle-physoc-006` (high, PhysicalSocial_Process_v1.0.docx) — Authorization chain is limited to Local CISO + Local Facilities Manager - no Legal, HR, Group Security or law-enforcement liaison [merged: lifecycle-physoc-006, lifecycle-physoc-011, tdora-physoc-003]
- `lifecycle-physoc-009` (high, PhysicalSocial_Process_v1.0.docx) — No data-handling rules for material acquired during the engagement (photos, building maps, credentials, badge clones) [merged: lifecycle-physoc-009, tdora-physoc-008]
- `tdora-physoc-001` (high, PhysicalSocial_Process_v1.0.docx) — Physical and social engineering is run as a parallel track, not integrated with TIBER-EU / DORA TLPT [merged: tdora-physoc-001, tdora-physoc-006, tdora-physoc-007]
- `tdora-physoc-004` (high, PhysicalSocial_Process_v1.0.docx) — No Targeted Threat Intelligence input drives physical scenarios
- `tdora-physoc-009` (high, PhysicalSocial_Process_v1.0.docx) — No GDPR lawful-basis statement for personal data captured during physical and social testing
- `lifecycle-physocq-003` (high, PhysicalSocial_Questionnaire_Process_v1.0.docx) — No data-protection / GDPR handling for questionnaire responses
- `lifecycle-physocq-006` (high, PhysicalSocial_Questionnaire_Process_v1.0.docx) — No risk-screen for regulated environments, trading floors, customer-facing or vulnerable-people areas [merged: lifecycle-physocq-006, lifecycle-physocq-008, lifecycle-physocq-013]
- `lifecycle-threatscenarios-013` (medium, ThreatScenarios_Process_v1.1.docx) — Report section lacks a finding taxonomy / severity model and evidence requirements [merged: lifecycle-threatscenarios-013, tdora-threatscenarios-005]
- `tdora-threatscenarios-003` (medium, ThreatScenarios_Process_v1.1.docx) — Operator-driven threat-actor selection is not informed by a TTI product; acceptable here but should be stated so it cannot be cited as TIBER
- `tdora-threatscenarios-006` (medium, ThreatScenarios_Process_v1.1.docx) — No jurisdictional / regulated-entity scope statement — Euronext spans multiple NCAs
- `lifecycle-operations-009` (medium, Operations_Process_v1.0.docx) — Kill-switch authority is asserted but not procedurally defined
- `lifecycle-operations-010` (medium, Operations_Process_v1.0.docx) — Scoping phase is implicit; objectives are defined 'at the end of the 1st phase' with no scoping artefact [merged: lifecycle-operations-010, lifecycle-operations-011]
- `lifecycle-operations-015` (medium, Operations_Process_v1.0.docx) — Leg-up authorization criteria and audit trail not defined
- `tdora-operations-003` (medium, Operations_Process_v1.0.docx) — Threat intelligence sourcing does not distinguish open-source feeds from a TIBER-EU Targeted Threat Intelligence (TTI) report
- `tdora-operations-005` (medium, Operations_Process_v1.0.docx) — Critical / important functions (DORA terminology) are not used to drive scope
- `lifecycle-exercises-009` (medium, Exercises_Process_v1.1.docx) — TI provider independence not addressed; TI appears to be performed by the same team as RT
- `lifecycle-exercises-016` (medium, Exercises_Process_v1.1.docx) — Leg-Up process lacks logging requirements and impact on results / detection metrics [merged: lifecycle-exercises-016, tdora-exercises-013]
- `tdora-exercises-014` (medium, Exercises_Process_v1.1.docx) — Document refers to 'a company' generically; jurisdictional applicability under DORA is not stated [merged: lifecycle-exercises-018, tdora-exercises-014]
- `tdora-exercises-010` (medium, Exercises_Process_v1.1.docx) — Data-protection clauses do not anchor on GDPR / DORA / sector regulation
- `tdora-exercises-011` (medium, Exercises_Process_v1.1.docx) — Scenarios derived from TI but no Targeted Threat Intelligence Report deliverable named
- `tdora-exercises-012` (medium, Exercises_Process_v1.1.docx) — Use of 'Unified Kill Chain' is fine but no mapping to TIBER-EU 'flags / legs / objectives' construct
- `tdora-bhe-003` (medium, BloodhoundEnterprise_Process_v0.1.docx) — Sensitive AD/Entra graph data is uploaded to a SaaS tenant without DORA-aligned ICT third-party / data-handling controls in the document
- `lifecycle-rtmeth-001` (medium, RedTeam_Methodology_v0.3.docx) — Three engagement types named but Purple Team is presented inconsistently as a fourth type [merged: lifecycle-rtmeth-001, tdora-rtmeth-013]
- `lifecycle-rtmeth-010` (medium, RedTeam_Methodology_v0.3.docx) — Exercise type described as 'TIBER-Like' without committing to TIBER-EU phase model or actor model
- `lifecycle-rtmeth-011` (medium, RedTeam_Methodology_v0.3.docx) — Safety / blast-radius controls limited to 'Forbidden Attacks' list; no testing-in-prod safeguards or rollback model
- `lifecycle-rtmeth-012` (medium, RedTeam_Methodology_v0.3.docx) — Data Handling references PIA (US act) and 'WT Point of Contact' but never defines WT or applies GDPR / EU data protection
- `tdora-rtmeth-010` (medium, RedTeam_Methodology_v0.3.docx) — Jurisdictional ambiguity: methodology silent on which Euronext regulated entity / NCA the framework applies under
- `lifecycle-research-006` (medium, Research_Methodology_v0.2.docx) — Purple-team feedback loop named but not defined as a gated close-out
- `tdora-research-002` (medium, Research_Methodology_v0.2.docx) — Research provenance not bound to engagement deliverables - traceability risk for TLPT attestation
- `tdora-research-004` (medium, Research_Methodology_v0.2.docx) — Reproduction of techniques against prod-like environments needs DORA test-risk-management framing
- `lifecycle-physoc-013` (medium, PhysicalSocial_Process_v1.0.docx) — Blue-team notification posture is undefined - secrecy clause names only Local CISO and Local Facilities Manager
- `tdora-physoc-011` (medium, PhysicalSocial_Process_v1.0.docx) — Critical / important functions not used to scope physical testing
- `tdora-exercises-015` (low, Exercises_Process_v1.1.docx) — Terminology drift: 'White Team' usage may diverge from TIBER-EU 'White Team' role definition
- `lifecycle-bhe-015` (low, BloodhoundEnterprise_Process_v0.1.docx) — Document is at v0.1 'First Draft' and 16 months old without review evidence
- `lifecycle-rtmeth-015` (low, RedTeam_Methodology_v0.3.docx) — OPLOG free-format ('OneNote example') with no central retention or chain-of-custody rules
- `lifecycle-rtmeth-018` (low, RedTeam_Methodology_v0.3.docx) — Versioning shows last update Oct 2024 (v0.3) and version still pre-1.0 for the central methodology
- `tdora-rtmeth-012` (low, RedTeam_Methodology_v0.3.docx) — Terminology drift: 'WT' used but undefined; 'white cards (leg ups)' not aligned with TIBER-EU 'leg-ups'
- `tdora-physoc-012` (low, PhysicalSocial_Process_v1.0.docx) — TIBER-EU terminology not used (no White Team, Control Team, TI provider, attestation)
- `lifecycle-physocq-010` (low, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Stolen-asset IR section does not link to the corporate IR process or define notification timing
- `lifecycle-physocq-012` (low, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Typo / wording — 'wether' instead of 'whether'
- `tdora-threatscenarios-001` (informational, ThreatScenarios_Process_v1.1.docx) — Document does not claim TLPT / TIBER-EU alignment; engagement type is Threat Scenario, which is not TLPT-eligible
- `tdora-operations-001` (informational, Operations_Process_v1.0.docx) — SOP makes no reference to TIBER-EU or DORA TLPT; positioning vs the regulator-aligned framework is not stated [merged: tdora-operations-001, tdora-operations-006]
- `lifecycle-exercises-011` (informational, Exercises_Process_v1.1.docx) — Doc is silent on TIBER-EU / DORA-TLPT applicability for Exercises
- `tdora-exercises-001` (informational, Exercises_Process_v1.1.docx) — Exercise SOP does not position itself relative to TIBER-EU / DORA TLPT
- `lifecycle-bhe-001` (informational, BloodhoundEnterprise_Process_v0.1.docx) — Tooling-process doc does not state which engagement type(s) consume BloodHound output [merged: lifecycle-bhe-001, lifecycle-bhe-016, lifecycle-bhe-018, tdora-bhe-001]
- `tdora-research-001` (informational, Research_Methodology_v0.2.docx) — Document does not claim TIBER-EU / DORA TLPT alignment - largely out of scope for this evaluator
- `tdora-research-003` (informational, Research_Methodology_v0.2.docx) — Internal research intake is not a substitute for an independent TI provider on TLPT engagements
- `tdora-research-005` (informational, Research_Methodology_v0.2.docx) — Jurisdictional ambiguity: Euronext operates across multiple NCAs - research process should be jurisdiction-agnostic
- `lifecycle-physocq-014` (informational, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Engagement lifecycle phases beyond questionnaire scope are correctly absent [merged: lifecycle-physocq-014, tdora-physocq-001]
- `tdora-physocq-002` (informational, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Questionnaire could surface DORA 'critical or important function' status of each office

## Authorization / RoE clarity (23 findings)
_Severity mix: critical: 1, high: 10, medium: 9, low: 2, informational: 1_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, Exercises_Process_v1.1.docx, Operations_Process_v1.0.docx, PhysicalSocial_Process_v1.0.docx, PhysicalSocial_Questionnaire_Process_v1.0.docx, RedTeam_Methodology_v0.3.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-exercises-005` (critical, Exercises_Process_v1.1.docx) — Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words
- `lifecycle-operations-001` (high, Operations_Process_v1.0.docx) — Operation execution flow lacks the assumed-breach setup phase
- `lifecycle-operations-002` (high, Operations_Process_v1.0.docx) — Codename convention does not require the fictional-character theme
- `lifecycle-operations-008` (high, Operations_Process_v1.0.docx) — Physical scope is mentioned in passing but never explicitly scoped or made optional
- `lifecycle-bhe-002` (high, BloodhoundEnterprise_Process_v0.1.docx) — No formal authorization / RoE for continuous AD enumeration, only an informal SOC heads-up
- `lifecycle-rtmeth-007` (high, RedTeam_Methodology_v0.3.docx) — Physical scope not addressed in the methodology despite being explicitly in the team's remit
- `lifecycle-research-002` (high, Research_Methodology_v0.2.docx) — Hypothesis-to-validation lifecycle lacks an explicit lab/sandbox environment and authorization gate
- `lifecycle-research-005` (high, Research_Methodology_v0.2.docx) — Handover from Research to Engagement playbooks is implicit and not gated
- `lifecycle-physoc-002` (high, PhysicalSocial_Process_v1.0.docx) — No codename assignment or fictional-character theme requirement
- `lifecycle-physoc-008` (high, PhysicalSocial_Process_v1.0.docx) — No social-engineering rules: targeting limits, pretext approval, recording legality, executive carve-outs [merged: lifecycle-physoc-008, lifecycle-physoc-012]
- `lifecycle-physocq-007` (high, PhysicalSocial_Questionnaire_Process_v1.0.docx) — No authorization / sign-off chain triggered by questionnaire responses
- `lifecycle-threatscenarios-011` (medium, ThreatScenarios_Process_v1.1.docx) — OPLOG format is suggested rather than required, and storage / access controls are not specified
- `lifecycle-threatscenarios-014` (medium, ThreatScenarios_Process_v1.1.docx) — Clean-up obligation is in the Report section and is conditional ('as appropriate'), not a controlled close-out gate
- `lifecycle-bhe-010` (medium, BloodhoundEnterprise_Process_v0.1.docx) — Cleanup / rollback responsibility is described informally and lacks a verification gate
- `lifecycle-bhe-011` (medium, BloodhoundEnterprise_Process_v0.1.docx) — User-account-impact rule is sound but lacks a defined approver and audit trail [merged: lifecycle-bhe-011, lifecycle-bhe-017]
- `lifecycle-rtmeth-017` (medium, RedTeam_Methodology_v0.3.docx) — Operation defined as 'opportunistic, outside formalized engagement' — inconsistent with assumed-breach model; weakens authorization
- `lifecycle-research-015` (medium, Research_Methodology_v0.2.docx) — OPSEC and detection notes mandated but no separation between research-time and engagement-time disclosure
- `lifecycle-physoc-007` (medium, PhysicalSocial_Process_v1.0.docx) — Get-out-of-jail letter does not explicitly cover indemnification, insurance, bail funding or counsel access
- `lifecycle-physoc-015` (medium, PhysicalSocial_Process_v1.0.docx) — Weaponization step has no inventory, hand-back or implant-removal control
- `lifecycle-physoc-018` (medium, PhysicalSocial_Process_v1.0.docx) — No safe handover from physical foothold to cyber post-exploitation team
- `lifecycle-threatscenarios-015` (low, ThreatScenarios_Process_v1.1.docx) — Threat-actor selection guidance focuses on insiders but does not exclude relevant external actors
- `lifecycle-operations-012` (low, Operations_Process_v1.0.docx) — OPLOG storage and integrity controls are unspecified
- `tdora-physoc-010` (informational, PhysicalSocial_Process_v1.0.docx) — NCA-specific guidance not referenced for any Euronext jurisdiction

## Threat-hunt and IR-support coverage (9 findings)
_Severity mix: high: 2, medium: 5, low: 2_

Appears across: Operations_Process_v1.0.docx, PhysicalSocial_Questionnaire_Process_v1.0.docx, RedTeam_Methodology_v0.3.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-threatscenarios-003` (high, ThreatScenarios_Process_v1.1.docx) — Planning is red-team-only; Threat Scenarios require joint planning with the blue team
- `lifecycle-research-008` (high, Research_Methodology_v0.2.docx) — Adjacent remit not addressed: research input to IR runbooks and to threat-hunting during external tests / live incidents
- `lifecycle-threatscenarios-012` (medium, ThreatScenarios_Process_v1.1.docx) — Execution phases (Reconnaissance / Exploit / Escalation) read as a stealth kill-chain rather than a demonstrative walk-through
- `lifecycle-rtmeth-016` (medium, RedTeam_Methodology_v0.3.docx) — Threat Scenario description omits internal-tool abuse scope (GitLab/Jenkins/CI/CD/secret stores) and joint-planning structure
- `lifecycle-research-009` (medium, Research_Methodology_v0.2.docx) — Physical / social-engineering tradecraft research not explicitly in or out of scope
- `lifecycle-physocq-001` (medium, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Introduction copy describes a different scope than the questionnaire actually covers
- `lifecycle-physocq-009` (medium, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Social-engineering and tailgating posture not surveyed
- `lifecycle-operations-013` (low, Operations_Process_v1.0.docx) — Clean-up step is described as a final note rather than a tracked phase
- `lifecycle-rtmeth-019` (low, RedTeam_Methodology_v0.3.docx) — Engagement-type matrix referenced but unreadable in ingested content (axis labels duplicated, no axis values)

## Codename + theme convention gaps (7 findings)
_Severity mix: high: 2, medium: 1, low: 4_

Appears across: Exercises_Process_v1.1.docx, PhysicalSocial_Questionnaire_Process_v1.0.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-exercises-003` (high, Exercises_Process_v1.1.docx) — Codename convention does not require the fictional-character theme
- `lifecycle-physocq-002` (high, PhysicalSocial_Questionnaire_Process_v1.0.docx) — No questionnaire owner, distribution authority, or response custodian identified [merged: lifecycle-physocq-002, lifecycle-physocq-004]
- `lifecycle-threatscenarios-008` (medium, ThreatScenarios_Process_v1.1.docx) — CODENAME section is positioned after Scope/Threat Actors/Scenarios but states it must be chosen 'before starting the planning phase'
- `lifecycle-threatscenarios-009` (low, ThreatScenarios_Process_v1.1.docx) — CODENAME section does not state the convention or pattern to use
- `lifecycle-threatscenarios-016` (low, ThreatScenarios_Process_v1.1.docx) — LLM-assisted scenario generation is recommended without guardrails on confidentiality / hallucination
- `lifecycle-exercises-014` (low, Exercises_Process_v1.1.docx) — Document-wide drift between 'Exercise' and 'Operation' terminology
- `lifecycle-research-014` (low, Research_Methodology_v0.2.docx) — Document at v0.2 - sub-1.0 status not flagged for downstream consumers

## Physical / social scope completeness (6 findings)
_Severity mix: critical: 1, high: 1, medium: 2, low: 2_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, PhysicalSocial_Process_v1.0.docx, PhysicalSocial_Questionnaire_Process_v1.0.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-physoc-005` (critical, PhysicalSocial_Process_v1.0.docx) — No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site
- `lifecycle-threatscenarios-007` (high, ThreatScenarios_Process_v1.1.docx) — Physical scope is not addressed — neither in-scope nor explicitly out-of-scope
- `lifecycle-bhe-012` (medium, BloodhoundEnterprise_Process_v0.1.docx) — Doc covers on-prem AD but only nods at Entra ID; cloud-identity attack paths under-treated [merged: lifecycle-bhe-012, lifecycle-bhe-013]
- `lifecycle-physocq-005` (medium, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Periodicity adjustment logic is described informally and not bound to the maturity score
- `lifecycle-physoc-017` (low, PhysicalSocial_Process_v1.0.docx) — Maturity / Vulnerability Score formulae are referenced but not rendered
- `lifecycle-physocq-011` (low, PhysicalSocial_Questionnaire_Process_v1.0.docx) — Several figure references but no rendered diagrams; reproducibility of evidence is at risk

## Process completeness / lifecycle gaps (5 findings)
_Severity mix: medium: 2, low: 3_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, Exercises_Process_v1.1.docx, Research_Methodology_v0.2.docx.

**Contributing finding ids:**
- `lifecycle-exercises-015` (medium, Exercises_Process_v1.1.docx) — Reporting deliverable lacks defined finding taxonomy and severity model
- `lifecycle-research-004` (medium, Research_Methodology_v0.2.docx) — AI-enrichment layer described without governance, prompt provenance, or data-handling rules
- `lifecycle-exercises-013` (low, Exercises_Process_v1.1.docx) — Data-handling references the US 'Privacy of Information Act (PIA)' instead of GDPR / EU regimes
- `lifecycle-bhe-005` (low, BloodhoundEnterprise_Process_v0.1.docx) — Acronym 'AET' used without definition
- `lifecycle-research-011` (low, Research_Methodology_v0.2.docx) — Research Repository governance light on access control, retention, and classification

## Purple-teaming close-out weakness (4 findings)
_Severity mix: high: 1, medium: 1, low: 1, informational: 1_

Appears across: Exercises_Process_v1.1.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-threatscenarios-004` (high, ThreatScenarios_Process_v1.1.docx) — No threat-hunt handover from Threat Scenario findings to the hunt team [merged: lifecycle-threatscenarios-004, lifecycle-threatscenarios-005, lifecycle-threatscenarios-006]
- `lifecycle-exercises-007` (medium, Exercises_Process_v1.1.docx) — No lessons-learned capture mechanism into the team knowledge base
- `lifecycle-research-012` (low, Research_Methodology_v0.2.docx) — Knowledge-capture mechanism named but not anchored: Research Repository is the wiki/register/deck?
- `lifecycle-research-001` (informational, Research_Methodology_v0.2.docx) — Research methodology correctly positioned as cross-cutting; engagement-execution phases not applicable

## OPSEC, safety, deconfliction (4 findings)
_Severity mix: high: 2, medium: 2_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, Exercises_Process_v1.1.docx, Research_Methodology_v0.2.docx, ThreatScenarios_Process_v1.1.docx.

**Contributing finding ids:**
- `lifecycle-threatscenarios-010` (high, ThreatScenarios_Process_v1.1.docx) — Blast-radius / safety controls for production tool abuse are vague
- `lifecycle-research-003` (high, Research_Methodology_v0.2.docx) — No legal / IP / responsible-disclosure review for capabilities derived from external research [merged: lifecycle-research-003, lifecycle-research-010]
- `lifecycle-exercises-010` (medium, Exercises_Process_v1.1.docx) — Stealth / OPSEC posture and detection-as-result not explicitly captured as a phase outcome
- `lifecycle-bhe-009` (medium, BloodhoundEnterprise_Process_v0.1.docx) — Service-account privilege model is described but not safety-bounded (e.g. optional Local Admin everywhere)

## Diagram-narrative inconsistency (3 findings)
_Severity mix: medium: 1, low: 1, informational: 1_

Appears across: Exercises_Process_v1.1.docx, Operations_Process_v1.0.docx, Research_Methodology_v0.2.docx.

**Contributing finding ids:**
- `lifecycle-exercises-012` (medium, Exercises_Process_v1.1.docx) — Diagrams referenced but not ingested / not described in prose
- `lifecycle-research-013` (low, Research_Methodology_v0.2.docx) — Figure 1 referenced but no diagram present in this artefact
- `lifecycle-operations-014` (informational, Operations_Process_v1.0.docx) — Deconfliction process references Figure 2 that is not present in the ingested content

## Reporting / remediation tracking (2 findings)
_Severity mix: high: 1, informational: 1_

Appears across: BloodhoundEnterprise_Process_v0.1.docx, Operations_Process_v1.0.docx.

**Contributing finding ids:**
- `lifecycle-bhe-006` (high, BloodhoundEnterprise_Process_v0.1.docx) — Remediation section names no owner, no tracking system, no severity model and no SLA
- `lifecycle-operations-016` (informational, Operations_Process_v1.0.docx) — Attack-path prioritisation table is informative but not linked to a governing register
