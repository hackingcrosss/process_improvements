# Themes — run 2026-05-12-1520

Findings grouped by underlying weakness. Each finding appears in exactly one theme.

**Total findings (deduped):** 181.  **Themes with ≥2 findings:** 16.

## TIBER-EU / DORA TLPT regulatory alignment

59 findings (critical:4, high:20, medium:20, low:5, informational:10).

- `lifecycle-exercises-001` **critical** — No clean-up / environment restoration step before report sign-off || Closure phase missing TIBER-EU mandated artefacts (replay, 360 feedback  *(Exercises_Process_v1.1.docx)*
- `lifecycle-threatscenarios-002` **critical** — No Control Team / White Team role defined; Execution acts on production tools without a named institution-side test owner || No authorizatio  *(ThreatScenarios_Process_v1.1.docx)*
- `tdora-rtmeth-004` **critical** — TIBER-EU Preparation elements absent: GTL, scoping doc, engagement letter, critical-functions ID, provider procurement || Closure phase arte  *(RedTeam_Methodology_v0.3.docx)*
- `tdora-physoc-002` **critical** — Adjacent-remit gaps: physical/social process is silent on threat-hunt and IR-support roles || No remediation tracking or lessons-learned cap  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-exercises-004` **high** — 'Critical or important functions' (DORA terminology) not used; live-production scope not stated || Physical scope not explicitly addressed (  *(Exercises_Process_v1.1.docx)*
- `lifecycle-rtmeth-002` **high** — Methodology silent on engagement-team roles (lead, operator, threat intel, white team, control team) || Threat-hunt handover from red findin  *(RedTeam_Methodology_v0.3.docx)*
- `tdora-rtmeth-008` **high** — Data Handling references US 'Privacy of Information Act (PIA)' — no GDPR / DORA legal basis cited  *(RedTeam_Methodology_v0.3.docx)*
- `tdora-threatscenarios-002` **high** — Document does not state that Threat Scenarios are not TLPT, leaving a misalignment risk if cited as DORA evidence  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-operations-004` **high** — Closure does not produce TIBER-EU-style closure artefacts (replay, attestation, knowledge sharing) || No remediation tracking process descri  *(Operations_Process_v1.0.docx)*
- `lifecycle-physocq-006` **high** — No retention or versioning policy for completed questionnaire responses || No explicit linkage to the parent PhysicalSocial process or to en  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `tdora-exercises-002` **high** — TIBER-EU Preparation phase elements (GTL, engagement letter, critical-functions identification, provider procurement) only partially present  *(Exercises_Process_v1.1.docx)*
- `tdora-exercises-003` **high** — Threat Intelligence provider independence not addressed; TI and RT appear conflated  *(Exercises_Process_v1.1.docx)*
- `tdora-exercises-004` **high** — White Team described, but no Control Team distinct from White Team / no TIBER Cyber Team / TCT engagement  *(Exercises_Process_v1.1.docx)*
- `tdora-exercises-007` **high** — Tester requirements (DORA Art.27) not addressed: internal vs external testers, qualifications, rotation  *(Exercises_Process_v1.1.docx)*
- `tdora-exercises-009` **high** — Risk-management of the test itself underspecified: no kill-switch, no safe-harbours / indemnities, no rollback plan  *(Exercises_Process_v1.1.docx)*
- `tdora-operations-002` **high** — 'White Team' role conflates TIBER-EU White Team and Control Team responsibilities  *(Operations_Process_v1.0.docx)*
- `tdora-physoc-001` **high** — Tester-requirement provisions (DORA Art.27) are not addressed || Physical and social engineering is run as a parallel track, not integrated   *(PhysicalSocial_Process_v1.0.docx)*
- `tdora-physoc-004` **high** — No Targeted Threat Intelligence input drives physical scenarios  *(PhysicalSocial_Process_v1.0.docx)*
- `tdora-rtdeck-001` **high** — Master red-team explainer is silent on TIBER-EU and DORA TLPT  *(RedTeaming_v1.0.pptx)*
- `tdora-rtdeck-002` **high** — Actor model lists only White / Red / Blue Team — no Control Team or independent TI provider  *(RedTeaming_v1.0.pptx)*
- `tdora-rtmeth-001` **high** — Methodology calls Exercises 'TIBER-Like' without committing to the TIBER-EU phase model or DORA TLPT requirements  *(RedTeam_Methodology_v0.3.docx)*
- `tdora-rtmeth-009` **high** — Scoping does not reference DORA 'critical or important functions' nor commit to live-production testing under controls  *(RedTeam_Methodology_v0.3.docx)*
- `tdora-exercises-006` **high** — No coordination with competent authority / lead overseer described  *(Exercises_Process_v1.1.docx)*
- `tdora-rtmeth-003` **high** — Threat Planning lacks ATT&CK mapping and source/quality requirements for threat intelligence || Threat Intelligence phase: no Targeted Threa  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-exercises-009` **medium** — TI provider independence not addressed; TI appears to be performed by the same team as RT  *(Exercises_Process_v1.1.docx)*
- `lifecycle-exercises-016` **medium** — Leg-Up process lacks logging requirements and impact on results / detection metrics || Leg-Up handling not aligned with TIBER-EU transparenc  *(Exercises_Process_v1.1.docx)*
- `lifecycle-rtdeck-012` **medium** — Phase numbering (0–4) is used without defining each phase in prose  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtmeth-010` **medium** — Exercise type described as 'TIBER-Like' without committing to TIBER-EU phase model or actor model  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-rtmeth-012` **medium** — Data Handling references PIA (US act) and 'WT Point of Contact' but never defines WT or applies GDPR / EU data protection  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-threatscenarios-013` **medium** — No closure artefacts analogous to TIBER-EU Closure (replay, 360° feedback, remediation plan, internal attestation) || Report section lacks a  *(ThreatScenarios_Process_v1.1.docx)*
- ... and 29 more (see findings-register.csv).

## Other / general process-quality findings

29 findings (high:9, medium:9, low:10, informational:1).

- `lifecycle-threatscenarios-003` **high** — Planning is red-team-only; Threat Scenarios require joint planning with the blue team  *(ThreatScenarios_Process_v1.1.docx)*
- `coherence-exercises-011` **high** — RACI conflict: ownership of Threat Intelligence work inconsistent across engagement SOPs  *(engagements-2-exercises-exercises-process-v1-1-docx)*
- `lifecycle-bhe-004` **high** — Tenant access uses application accounts only; SAML/SSO and MFA not yet implemented  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-bhe-006` **high** — Remediation section names no owner, no tracking system, no severity model and no SLA  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-exercises-008` **high** — Initiation phase blurs scoping and authorization, lacks engagement letter / RoE sign-off gate  *(Exercises_Process_v1.1.docx)*
- `lifecycle-research-002` **high** — Hypothesis-to-validation lifecycle lacks an explicit lab/sandbox environment and authorization gate  *(Research_Methodology_v0.2.docx)*
- `lifecycle-research-003` **high** — Tool lifecycle states defined but no review cadence, owner, or retirement criteria || No legal / IP / responsible-disclosure review for capa  *(Research_Methodology_v0.2.docx)*
- `lifecycle-research-005` **high** — Handover from Research to Engagement playbooks is implicit and not gated  *(Research_Methodology_v0.2.docx)*
- `lifecycle-rtmeth-014` **high** — Scoping section is a 4-bullet capability checklist; lacks asset/criticality scoping, exclusions, and target selection method  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-bhe-011` **medium** — OPSEC guidance defers wholly to BHE tooltips and never states Euronext's own stance || User-account-impact rule is sound but lacks a defined  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-operations-015` **medium** — Leg-up authorization criteria and audit trail not defined  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-013` **medium** — Blue-team notification posture is undefined - secrecy clause names only Local CISO and Local Facilities Manager  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physoc-015` **medium** — Weaponization step has no inventory, hand-back or implant-removal control  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physocq-005` **medium** — Periodicity adjustment logic is described informally and not bound to the maturity score  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-rtdeck-010` **medium** — Leg-up mechanism lacks documentation / approval trail  *(RedTeaming_v1.0.pptx)*
- `lifecycle-operations-010` **medium** — Scoping phase is implicit; objectives are defined 'at the end of the 1st phase' with no scoping artefact || Unified Kill Chain is invoked bu  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-007` **medium** — Get-out-of-jail letter does not explicitly cover indemnification, insurance, bail funding or counsel access  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-threatscenarios-012` **medium** — Execution phases (Reconnaissance / Exploit / Escalation) read as a stealth kill-chain rather than a demonstrative walk-through  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-bhe-005` **low** — Acronym 'AET' used without definition  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-bhe-015` **low** — Document is at v0.1 'First Draft' and 16 months old without review evidence  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-operations-013` **low** — Clean-up step is described as a final note rather than a tracked phase  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-017` **low** — Maturity / Vulnerability Score formulae are referenced but not rendered  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physocq-012` **low** — Typo / wording — 'wether' instead of 'whether'  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-rtdeck-008` **low** — Likely typo: 'Framework to access results' should read 'assess'  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtdeck-014` **low** — Trailing slides 25–27 are empty in the ingested form  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtdeck-015` **low** — Deck carries no visible classification / handling label, yet contains C2-tooling detail  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtmeth-015` **low** — OPLOG free-format ('OneNote example') with no central retention or chain-of-custody rules  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-threatscenarios-015` **low** — Threat-actor selection guidance focuses on insiders but does not exclude relevant external actors  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-operations-016` **informational** — Attack-path prioritisation table is informative but not linked to a governing register  *(Operations_Process_v1.0.docx)*

## Physical scope and social-engineering completeness

18 findings (high:12, medium:5, low:1).

- `lifecycle-operations-008` **high** — Physical scope is mentioned in passing but never explicitly scoped or made optional  *(Operations_Process_v1.0.docx)*
- `lifecycle-physocq-002` **high** — Vulnerability score, controls coverage and maturity formulas are referenced but the equations are missing || No questionnaire owner, distrib  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-physocq-007` **high** — No authorization / sign-off chain triggered by questionnaire responses  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-rtdeck-005` **high** — Critical / important functions and jurisdictional scope not discussed || Physical scope is not addressed  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtmeth-007` **high** — Physical scope not addressed in the methodology despite being explicitly in the team's remit  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-threatscenarios-007` **high** — Physical scope is not addressed — neither in-scope nor explicitly out-of-scope  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-operations-001` **high** — Operation execution flow lacks the assumed-breach setup phase  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-001` **high** — Physical/social process is not linked to the Exercise / Operation / Threat-Scenario engagement taxonomy || No multi-jurisdictional handling   *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physoc-008` **high** — No social-engineering rules: targeting limits, pretext approval, recording legality, executive carve-outs || No no-go zones, building-evacua  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physoc-009` **high** — No data-handling rules for material acquired during the engagement (photos, building maps, credentials, badge clones) || No risk-management   *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physocq-003` **high** — No data-protection / GDPR handling for questionnaire responses  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `tdora-physoc-009` **high** — No GDPR lawful-basis statement for personal data captured during physical and social testing  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-physocq-001` **medium** — Introduction copy describes a different scope than the questionnaire actually covers  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-research-009` **medium** — Physical / social-engineering tradecraft research not explicitly in or out of scope  *(Research_Methodology_v0.2.docx)*
- `tdora-threatscenarios-006` **medium** — No jurisdictional / regulated-entity scope statement — Euronext spans multiple NCAs  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-bhe-012` **medium** — Doc covers on-prem AD but only nods at Entra ID; cloud-identity attack paths under-treated || Physical scope explicitly N/A but the document  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-physocq-009` **medium** — Social-engineering and tailgating posture not surveyed  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*
- `lifecycle-physocq-011` **low** — Several figure references but no rendered diagrams; reproducibility of evidence is at risk  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*

## Purple-team close-out missing or weak

13 findings (critical:4, high:3, medium:3, low:2, informational:1).

- `lifecycle-rtdeck-003` **critical** — Remediation tracking and lessons-learned capture not described || Adjacent remit (threat hunt at close, hunt support, IR support) absent ||   *(RedTeaming_v1.0.pptx)*
- `lifecycle-operations-003` **critical** — No purple-teaming close-out with the blue team  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-003` **critical** — Closure artefacts (replay, 360 feedback, remediation plan, attestation) are absent || No purple-teaming close-out with blue team and physica  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-threatscenarios-001` **critical** — No purple-team close-out described, despite Threat Scenario format requiring blue team in the room  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-bhe-007` **high** — No threat-hunt handover from BHE attack-path output || No lessons-learned / knowledge-base capture loop tied to BHE findings || No purple-te  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-rtmeth-004` **high** — Purple-teaming close-out described as conditional collaboration, not as a mandatory close-out for every engagement || Purple Team described   *(RedTeam_Methodology_v0.3.docx)*
- `coherence-rt-meth-009` **high** — Phase mismatch: methodology mandates purple-team close-out but it's absent from all three engagement SOPs  *(methodology-redteam-methodology-v0-3-docx)*
- `lifecycle-research-006` **medium** — Purple-team feedback loop named but not defined as a gated close-out  *(Research_Methodology_v0.2.docx)*
- `lifecycle-rtmeth-001` **medium** — Three engagement types named but Purple Team is presented inconsistently as a fourth type || Operations and Threat Scenarios should be expli  *(RedTeam_Methodology_v0.3.docx)*
- `coherence-rt-meth-010` **medium** — Broken cross-reference: 'Purple Teaming Process document' referenced but absent from the corpus  *(methodology-redteam-methodology-v0-3-docx)*
- `lifecycle-research-012` **low** — Knowledge-capture mechanism named but not anchored: Research Repository is the wiki/register/deck?  *(Research_Methodology_v0.2.docx)*
- `lifecycle-rtmeth-018` **low** — Versioning shows last update Oct 2024 (v0.3) and version still pre-1.0 for the central methodology  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-research-001` **informational** — Research methodology correctly positioned as cross-cutting; engagement-execution phases not applicable  *(Research_Methodology_v0.2.docx)*

## Data handling, OPSEC, and safety controls

12 findings (critical:1, high:3, medium:7, low:1).

- `lifecycle-physoc-005` **critical** — No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-bhe-003` **high** — No data-handling, retention or classification rules for collected AD/Entra graph data  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-threatscenarios-010` **high** — Blast-radius / safety controls for production tool abuse are vague  *(ThreatScenarios_Process_v1.1.docx)*
- `tdora-rtmeth-007` **high** — Risk management of the test itself: no kill-switch, no rollback / safe-harbour clauses, no formal indemnity for testers  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-bhe-009` **medium** — Service-account privilege model is described but not safety-bounded (e.g. optional Local Admin everywhere)  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-bhe-010` **medium** — Cleanup / rollback responsibility is described informally and lacks a verification gate  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-research-015` **medium** — OPSEC and detection notes mandated but no separation between research-time and engagement-time disclosure  *(Research_Methodology_v0.2.docx)*
- `lifecycle-rtdeck-009` **medium** — Operators named in the body of the deck  *(RedTeaming_v1.0.pptx)*
- `lifecycle-threatscenarios-014` **medium** — Clean-up obligation is in the Report section and is conditional ('as appropriate'), not a controlled close-out gate  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-research-004` **medium** — AI-enrichment layer described without governance, prompt provenance, or data-handling rules  *(Research_Methodology_v0.2.docx)*
- `lifecycle-rtmeth-011` **medium** — Safety / blast-radius controls limited to 'Forbidden Attacks' list; no testing-in-prod safeguards or rollback model  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-exercises-013` **low** — Data-handling references the US 'Privacy of Information Act (PIA)' instead of GDPR / EU regimes  *(Exercises_Process_v1.1.docx)*

## Codename and theme convention

11 findings (high:4, medium:3, low:3, informational:1).

- `lifecycle-exercises-003` **high** — Codename convention does not require the fictional-character theme  *(Exercises_Process_v1.1.docx)*
- `lifecycle-operations-002` **high** — Codename convention does not require the fictional-character theme  *(Operations_Process_v1.0.docx)*
- `lifecycle-physoc-002` **high** — No codename assignment or fictional-character theme requirement  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-rtdeck-002` **high** — Codename + fictional-character theme convention not mentioned  *(RedTeaming_v1.0.pptx)*
- `coherence-threat-scenarios-016` **medium** — Codename theme convention (fictional characters for Operations and Exercises) not documented in any SOP or methodology  *(engagements-0-threat-scenarios-threatscenarios-process-v1-1-docx)*
- `lifecycle-rtmeth-017` **medium** — Operation defined as 'opportunistic, outside formalized engagement' — inconsistent with assumed-breach model; weakens authorization  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-threatscenarios-008` **medium** — CODENAME section is positioned after Scope/Threat Actors/Scenarios but states it must be chosen 'before starting the planning phase'  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-exercises-014` **low** — Document-wide drift between 'Exercise' and 'Operation' terminology  *(Exercises_Process_v1.1.docx)*
- `lifecycle-threatscenarios-009` **low** — CODENAME section does not state the convention or pattern to use  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-threatscenarios-016` **low** — LLM-assisted scenario generation is recommended without guardrails on confidentiality / hallucination  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-bhe-001` **informational** — No codename convention in scope (correctly), but cross-reference to engagement docs is missing || Tooling-process doc; out of scope for dire  *(BloodhoundEnterprise_Process_v0.1.docx)*

## Authorization, RoE and kill-switch clarity

8 findings (critical:3, high:2, medium:3).

- `lifecycle-exercises-005` **critical** — Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words  *(Exercises_Process_v1.1.docx)*
- `lifecycle-operations-007` **critical** — Authorization phase is implicit; no legal sign-off, RoE artefact, safe-words, or abort criteria defined  *(Operations_Process_v1.0.docx)*
- `lifecycle-rtmeth-003` **critical** — Authorization, Rules of Engagement, legal sign-off and kill-switch / abort criteria are not described  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-bhe-002` **high** — No formal authorization / RoE for continuous AD enumeration, only an informal SOC heads-up  *(BloodhoundEnterprise_Process_v0.1.docx)*
- `lifecycle-physoc-006` **high** — Authorization chain is limited to Local CISO + Local Facilities Manager - no Legal, HR, Group Security or law-enforcement liaison || No iden  *(PhysicalSocial_Process_v1.0.docx)*
- `lifecycle-operations-009` **medium** — Kill-switch authority is asserted but not procedurally defined  *(Operations_Process_v1.0.docx)*
- `lifecycle-rtdeck-007` **medium** — RoE bullet on Slide 6 lists a few prohibitions but does not name authorization chain, kill-switch, safe-words or evidence handling  *(RedTeaming_v1.0.pptx)*
- `lifecycle-physoc-018` **medium** — No safe handover from physical foothold to cyber post-exploitation team  *(PhysicalSocial_Process_v1.0.docx)*

## Engagement-type stealth vs collaboration handling

5 findings (high:2, medium:2, low:1).

- `lifecycle-rtdeck-006` **high** — 'Blue Team unaware' framing treated as universal — wrong for Threat Scenarios  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtdeck-001` **high** — Deck does not distinguish the three engagement types (Exercise / Operation / Threat Scenario)  *(RedTeaming_v1.0.pptx)*
- `lifecycle-rtmeth-016` **medium** — Threat Scenario description omits internal-tool abuse scope (GitLab/Jenkins/CI/CD/secret stores) and joint-planning structure  *(RedTeam_Methodology_v0.3.docx)*
- `lifecycle-exercises-010` **medium** — Stealth / OPSEC posture and detection-as-result not explicitly captured as a phase outcome  *(Exercises_Process_v1.1.docx)*
- `lifecycle-rtmeth-019` **low** — Engagement-type matrix referenced but unreadable in ingested content (axis labels duplicated, no axis values)  *(RedTeam_Methodology_v0.3.docx)*

## Broken cross-references and missing supporting docs

5 findings (high:1, medium:2, low:2).

- `lifecycle-rtdeck-011` **high** — Substantive phase / team / scheduling content is locked inside [chart-or-smartart] placeholders with no prose caption  *(RedTeaming_v1.0.pptx)*
- `lifecycle-exercises-012` **medium** — Diagrams referenced but not ingested / not described in prose  *(Exercises_Process_v1.1.docx)*
- `lifecycle-exercises-015` **medium** — Reporting deliverable lacks defined finding taxonomy and severity model  *(Exercises_Process_v1.1.docx)*
- `lifecycle-research-011` **low** — Research Repository governance light on access control, retention, and classification  *(Research_Methodology_v0.2.docx)*
- `lifecycle-research-013` **low** — Figure 1 referenced but no diagram present in this artefact  *(Research_Methodology_v0.2.docx)*

## Cross-doc naming drift (cosmetic + structural)

5 findings (medium:3, low:2).

- `coherence-cross-cutting-003` **medium** — Naming drift: 'defending teams' used corpus-wide; canonical is 'Blue Team'  *(engagements-1-operations-operations-process-v1-0-docx)*
- `coherence-research-meth-006` **medium** — Naming drift: internal repositories referenced without their qualifying prefix  *(methodology-research-methodology-v0-2-docx)*
- `coherence-cross-cutting-004` **medium** — Naming drift: standalone 'Operator' / 'Operators' used in multiple docs; canonical is 'Red Team Operator'  *(methodology-redteam-methodology-v0-3-docx)*
- `coherence-tools-005` **low** — Cosmetic tool/system naming drift: 'CobaltStrike', 'One Note', 'Bloodhound', 'Cyberark', 'Tier Zero'  *(methodology-redteam-methodology-v0-3-docx)*
- `lifecycle-research-014` **low** — Document at v0.2 - sub-1.0 status not flagged for downstream consumers  *(Research_Methodology_v0.2.docx)*

## Threat-hunt and IR-support coverage

4 findings (high:2, medium:1, low:1).

- `lifecycle-research-007` **high** — Research methodology silent on threat-hunt hypothesis generation as a deliberate output  *(Research_Methodology_v0.2.docx)*
- `lifecycle-research-008` **high** — Adjacent remit not addressed: research input to IR runbooks and to threat-hunting during external tests / live incidents  *(Research_Methodology_v0.2.docx)*
- `lifecycle-threatscenarios-011` **medium** — OPLOG format is suggested rather than required, and storage / access controls are not specified  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-physocq-010` **low** — Stolen-asset IR section does not link to the corporate IR process or define notification timing  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*

## Reporting / Closure / OFI structure and remediation tracking

3 findings (high:1, medium:1, low:1).

- `lifecycle-threatscenarios-006` **high** — No remediation tracking: report is the final artefact, with no follow-through on findings || No lessons-learned / knowledge-base capture mec  *(ThreatScenarios_Process_v1.1.docx)*
- `lifecycle-exercises-007` **medium** — No lessons-learned capture mechanism into the team knowledge base  *(Exercises_Process_v1.1.docx)*
- `coherence-rt-process-diag-015` **low** — OFI acronym used in canonical diagram and spelled out once in Operations; no OFI block in Exercises or Threat Scenarios SOPs  *(resources-diagrams-redteamprocess-drawio)*

## Orphan actors (AET, SOC structure, Tools team)

3 findings (medium:3).

- `coherence-apts-017` **medium** — Orphan actor: 'Tools team' named in apts; no charter or RACI in the corpus  *(apts-apts-private-pptx)*
- `coherence-bloodhound-013` **medium** — Orphan actor: AET (Assessment & Exploitation Team) named as owner of BloodHound tenant access; no charter doc defines its remit  *(methodology-bloodhoundenterprise-process-v0-1-docx)*
- `coherence-soc-rt-comms-diag-012` **medium** — Orphan actors: CSIRT, L1/L2/L3, Pentest/Assessment defined in SOC-RT comms diagram but absent from every engagement SOP  *(resources-diagrams-soc-rt-communications-drawio)*

## Cross-doc acronym conflict (PoC, CTI, TIBER, etc.)

2 findings (high:2).

- `coherence-operations-001` **high** — Acronym conflict: 'PoC' used as both 'Proof of Concept' and 'Point of Contact'  *(engagements-1-operations-operations-process-v1-0-docx)*
- `coherence-operations-002` **high** — Acronym conflict: 'CTI' used in Operations; canonical is 'TI' (Threat Intelligence)  *(engagements-1-operations-operations-process-v1-0-docx)*

## Phase mismatch across engagement SOPs and canonical diagram

2 findings (high:2).

- `coherence-rt-process-diag-008` **high** — Phase mismatch: RT Test sub-phases differ across the canonical diagram and the three engagement SOPs  *(resources-diagrams-redteamprocess-drawio)*
- `coherence-threat-scenarios-007` **high** — Phase mismatch: closing phase named 'Report' in Threat Scenarios SOP, 'Closure' in Operations and Exercises SOPs and the canonical diagram  *(engagements-0-threat-scenarios-threatscenarios-process-v1-1-docx)*

## Diagram-narrative inconsistency (diagrams as canonical reference)

2 findings (low:1, informational:1).

- `lifecycle-operations-012` **low** — OPLOG storage and integrity controls are unspecified  *(Operations_Process_v1.0.docx)*
- `lifecycle-operations-014` **informational** — Deconfliction process references Figure 2 that is not present in the ingested content  *(Operations_Process_v1.0.docx)*
