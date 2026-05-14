# Remediation backlog — Run 2026-05-11-1417

Findings grouped by recommended owner. Within each group, sorted by severity then effort (S before L).
Quick critical fixes appear first.

## Red team lead (61 items)

- **[HIGH | effort S]** (ThreatScenarios_Process_v1.1.docx) Physical scope is not addressed — neither in-scope nor explicitly out-of-scope — In the Scope subsection, add a one-line statement on physical scope: by default out-of-scope for tool-focused Threat Scenarios, but explicitly in-scope when the scenario subject is a physical control (e.g. badge system, datacentre access, visitor flow). _(id: `lifecycle-threatscenarios-007`)_
- **[HIGH | effort S]** (Operations_Process_v1.0.docx) Codename convention does not require the fictional-character theme — Update the CODENAME section to state that Operation codenames must be drawn from known fictional characters (movies / TV / books), with examples and a register of used names to avoid collisions. _(id: `lifecycle-operations-002`)_
- **[HIGH | effort S]** (Operations_Process_v1.0.docx) Physical scope is mentioned in passing but never explicitly scoped or made optional — Add a Scope subsection that explicitly addresses cyber + physical: state default in/out of scope, link to the Physical/Social process and questionnaire, and require the RoE to record physical scope per engagement. _(id: `lifecycle-operations-008`)_
- **[HIGH | effort S]** (Exercises_Process_v1.1.docx) Codename convention does not require the fictional-character theme — Update the CODENAME section to require codenames drawn from known fictional characters (movies, TV, books), and to be logged in the engagement register. Provide one or two illustrative examples. _(id: `lifecycle-exercises-003`)_
- **[HIGH | effort S]** (RedTeam_Methodology_v0.3.docx) Codename convention (mandatory codename, fictional-character theme for Exercises and Operations) is absent — Add a 'Codename Assignment' section to the methodology stating: every engagement (Exercise/Operation/Threat Scenario) is assigned a codename before authorization; Exercises and Operations follow the fictional-character theme; Threat Scenarios follow the team's alternative convention. Reference the codename register. _(id: `lifecycle-rtmeth-002`)_
- **[HIGH | effort S]** (RedTeam_Methodology_v0.3.docx) Physical scope not addressed in the methodology despite being explicitly in the team's remit — Add a 'Physical scope' subsection that confirms physical assessments are in scope, identifies the additional sign-offs required (site/facility owner, Legal), and references the PhysicalSocial Process document and questionnaire. _(id: `lifecycle-rtmeth-007`)_
- **[HIGH | effort S]** (PhysicalSocial_Process_v1.0.docx) No codename assignment or fictional-character theme requirement — Add a 'Codename' subsection to Planning requiring assignment of a unique codename per the team's theme convention and recording it on the Get-out-of-jail letter and the engagement register. _(id: `lifecycle-physoc-002`)_
- **[HIGH | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) No questionnaire owner, distribution authority, or response custodian identified — Add an 'Ownership and Custody' section naming the questionnaire owner, the office-side respondent role, the central reviewer, the storage repository (with access controls), and the response SLA. _(id: `lifecycle-physocq-002`)_
- **[HIGH | effort M]** (Operations_Process_v1.0.docx) Operation execution flow lacks the assumed-breach setup phase — Add an explicit 'Assumed-Breach Setup' phase before Initial Foothold (or replace Initial Foothold) that describes how the WT provisions the foothold, how scenarios are defined up front, and how scenario-driven execution differs from full kill-chain emulation. _(id: `lifecycle-operations-001`)_
- **[HIGH | effort M]** (RedTeam_Methodology_v0.3.docx) Scoping section is a 4-bullet capability checklist; lacks asset/criticality scoping, exclusions, and target selection method — Rewrite the Scoping section to describe how scope is determined and recorded: identification of critical/important functions, in-scope and explicitly out-of-scope assets, identities and networks, time windows, blue-team-awareness rule per engagement type, and scoping document template. The current 'capability checklist' content should be moved to a separate 'Engagement feasibility' subsection. _(id: `lifecycle-rtmeth-014`)_
- **[HIGH | effort M]** (Research_Methodology_v0.2.docx) Hypothesis-to-validation lifecycle lacks an explicit lab/sandbox environment and authorization gate — Add a 'Lab & Authorization' subsection requiring techniques be first reproduced in a named isolated lab, with documented authorization (and a stricter gate for any reproduction that needs prod-like or production data). _(id: `lifecycle-research-002`)_
- **[HIGH | effort M]** (Research_Methodology_v0.2.docx) Handover from Research to Engagement playbooks is implicit and not gated — Define promotion criteria from Experimental -> Operational and require a 'tradecraft release note' that updates Exercise / Operation / Threat-Scenario playbooks and the ATT&CK technique map when a new capability lands. _(id: `lifecycle-research-005`)_
- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) Physical/social process is not linked to the Exercise / Operation / Threat-Scenario engagement taxonomy — Add a 'Relationship to engagement types' section that maps Physical Pentest / Audit / Questionnaire to Exercise, Operation and Threat Scenario, clarifies the stealth posture in each, and removes or relabels the 'Figure 1 - Threat Scenarios Phases' caption so it does not imply a Threat Scenario when the section describes a stealthy Pentest. _(id: `lifecycle-physoc-001`)_
- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) Physical and social engineering is run as a parallel track, not integrated with TIBER-EU / DORA TLPT — Add a 'TIBER-EU / DORA TLPT alignment' section that (a) confirms physical and social vectors are eligible legs of a TLPT, (b) specifies that when run under TLPT the TI-derived scenarios drive the physical pretexts and objectives, and (c) routes the physical leg through the same control-team / white-team and attestation pathway as the cyber leg. Verify the exact framework text before publication. _(id: `tdora-physoc-001`)_
- **[MEDIUM | effort S]** (ThreatScenarios_Process_v1.1.docx) CODENAME section is positioned after Scope/Threat Actors/Scenarios but states it must be chosen 'before starting the planning phase' — Move 'CODENAME' to be the first subsection of Planning and add a sentence on where the codename register lives (which document, who has access). _(id: `lifecycle-threatscenarios-008`)_
- **[MEDIUM | effort S]** (ThreatScenarios_Process_v1.1.docx) Report section lacks a finding taxonomy / severity model and evidence requirements — Reference the team's reporting template explicitly and document the severity scale used. Specify the minimum evidence required per finding (screenshot, OPLOG line(s), artefact path). _(id: `lifecycle-threatscenarios-013`)_
- **[MEDIUM | effort S]** (ThreatScenarios_Process_v1.1.docx) Clean-up obligation is in the Report section and is conditional ('as appropriate'), not a controlled close-out gate — Promote clean-up to its own gated step at the end of Execution, with a checklist (accounts, files, persistence, scheduled jobs, config changes) and an explicit sign-off recorded in the engagement record. _(id: `lifecycle-threatscenarios-014`)_
- **[MEDIUM | effort S]** (Exercises_Process_v1.1.docx) No lessons-learned capture mechanism into the team knowledge base — Add a Closure step 'Lessons learned': structured retro covering RT, WT and (where appropriate) BT input, captured in the team knowledge base using a fixed template; include explicit follow-up actions and owners. _(id: `lifecycle-exercises-007`)_
- **[MEDIUM | effort S]** (Exercises_Process_v1.1.docx) Diagrams referenced but not ingested / not described in prose — Either re-ingest the document with diagram extraction enabled, or add prose descriptions / captions next to each figure reference (Phase ownership matrix, timeline, deconfliction flow, kill chain). Critical for the diagram-consistency evaluator to be meaningful. _(id: `lifecycle-exercises-012`)_
- **[MEDIUM | effort S]** (Exercises_Process_v1.1.docx) Use of 'Unified Kill Chain' is fine but no mapping to TIBER-EU 'flags / legs / objectives' construct — Add a paragraph in RT Test mapping Unified Kill Chain phases to TIBER-EU 'legs / flags / objectives'. Require ATT&CK technique IDs at each step. Provide a sample mapping table. _(id: `tdora-exercises-012`)_
- **[MEDIUM | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) Cleanup / rollback responsibility is described informally and lacks a verification gate — Require peer-reviewed cleanup verification: a second team member checks the OPLOG against environment state and signs off; record the sign-off in the engagement file. _(id: `lifecycle-bhe-010`)_
- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Three engagement types named but Purple Team is presented inconsistently as a fourth type — Rewrite the introduction to list the three engagement types and describe Purple Teaming separately as a mandatory close-out across all three. Align with the team's published engagement taxonomy. _(id: `lifecycle-rtmeth-001`)_
- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Exercise type described as 'TIBER-Like' without committing to TIBER-EU phase model or actor model — Replace 'TIBER-Like' with one of two precise statements: (i) Exercises are run as TIBER-EU / DORA TLPT engagements and follow Preparation → TI → RTT → Closure with TCT/CT/WT/TI/RT actors; or (ii) Exercises are inspired by TIBER-EU but are not TLPT and do not satisfy DORA Art.26 — adjust the rest of the doc accordingly. _(id: `lifecycle-rtmeth-010`)_
- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Threat Scenario description omits internal-tool abuse scope (GitLab/Jenkins/CI/CD/secret stores) and joint-planning structure — Update the Threat Scenario paragraph to describe the assumed-breach, demonstrative, joint-planning structure and call out the typical internal-tool targets (GitLab, Jenkins, CI/CD, internal SaaS, secret stores, ticketing). State explicitly that stealth is not in scope. _(id: `lifecycle-rtmeth-016`)_
- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Operation defined as 'opportunistic, outside formalized engagement' — inconsistent with assumed-breach model; weakens authorization — Rewrite the Operations paragraph: 'Operations are assumed-breach, scenario-scoped engagements with formal authorization, codename, and a small set of pre-defined objectives. They are typically used to test specific hypotheses or prove risks, and follow the Operations Process document.' Drop the 'outside the context of a formalized engagement' wording. _(id: `lifecycle-rtmeth-017`)_
- **[MEDIUM | effort S]** (Research_Methodology_v0.2.docx) Physical / social-engineering tradecraft research not explicitly in or out of scope — Add an explicit line clarifying scope of physical / social-engineering tradecraft research; align with the physical-social process docs. _(id: `lifecycle-research-009`)_
- **[MEDIUM | effort S]** (Research_Methodology_v0.2.docx) OPSEC and detection notes mandated but no separation between research-time and engagement-time disclosure — Introduce a small handling tier on OPSEC / detection notes (e.g. RT-only, share-with-purple, releasable) so capability documentation is shared safely. _(id: `lifecycle-research-015`)_
- **[MEDIUM | effort S]** (Research_Methodology_v0.2.docx) Research provenance not bound to engagement deliverables - traceability risk for TLPT attestation — Require engagement deliverables (RTT report, closure report, attestation pack) to cite the Research Repository and Tool Repository IDs of the techniques and capabilities used, so research provenance is auditable for TLPT. _(id: `tdora-research-002`)_
- **[MEDIUM | effort S]** (PhysicalSocial_Process_v1.0.docx) Blue-team notification posture is undefined - secrecy clause names only Local CISO and Local Facilities Manager — Add a 'Notification matrix' to Planning specifying for each assessment type who is in the know (white team) and who is blind (blue team / SOC), and when and how disclosure happens after the test. _(id: `lifecycle-physoc-013`)_
- **[MEDIUM | effort S]** (PhysicalSocial_Process_v1.0.docx) Weaponization step has no inventory, hand-back or implant-removal control — Add a hardware-implant inventory, chain-of-custody log, and explicit 'recovery and decommissioning' close-out step. _(id: `lifecycle-physoc-015`)_
- **[MEDIUM | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Introduction copy describes a different scope than the questionnaire actually covers — Rewrite the Introduction to state that this is a periodic Physical Security Questionnaire issued to Euronext office locations (per CMDB criticality), referencing the parent PhysicalSocial process for the engagement-led testing flow. _(id: `lifecycle-physocq-001`)_
- **[MEDIUM | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Periodicity adjustment logic is described informally and not bound to the maturity score — Add a Maturity-to-Periodicity table (e.g. Maturity ≥0.9 → 36 months, 0.7-0.9 → 24, 0.5-0.7 → 12, <0.5 → 6) and codify the override rule for sites with open critical findings. _(id: `lifecycle-physocq-005`)_
- **[MEDIUM | effort M]** (ThreatScenarios_Process_v1.1.docx) OPLOG format is suggested rather than required, and storage / access controls are not specified — Mandate a single OPLOG storage location (or a small approved set), specify access controls, retention period and a standard export schema (CSV/JSON) so logs are usable by IR. Personal note-taking apps remain acceptable as scratch but the canonical OPLOG must live in the approved location. _(id: `lifecycle-threatscenarios-011`)_
- **[MEDIUM | effort M]** (Operations_Process_v1.0.docx) Scoping phase is implicit; objectives are defined 'at the end of the 1st phase' with no scoping artefact — Introduce a named Scoping step with a scoping document template (in-scope, out-of-scope, objectives, success criteria, constraints, third-party dependencies) and require WT sign-off before the RT Test begins. Replace 'anything is in scope' with explicit boundaries. _(id: `lifecycle-operations-010`)_
- **[MEDIUM | effort M]** (Exercises_Process_v1.1.docx) Stealth / OPSEC posture and detection-as-result not explicitly captured as a phase outcome — Add an 'OPSEC and detection capture' note to the RT Test phase: stealth is in scope; the RT records every BT detection event (or absence thereof) per TTP; produce time-to-detect / time-to-contain metrics as a Closure deliverable. _(id: `lifecycle-exercises-010`)_
- **[MEDIUM | effort M]** (Exercises_Process_v1.1.docx) Reporting deliverable lacks defined finding taxonomy and severity model — Define the reporting taxonomy: severity rubric, mandatory evidence fields, ATT&CK technique ID per finding, and scenario-to-finding linkage. Provide a report template. _(id: `lifecycle-exercises-015`)_
- **[MEDIUM | effort M]** (RedTeam_Methodology_v0.3.docx) Safety / blast-radius controls limited to 'Forbidden Attacks' list; no testing-in-prod safeguards or rollback model — Expand the Forbidden Attacks section into a 'Safety & blast-radius controls' section: lab-first testing requirement (already present), explicit rollback/cleanup expectations for persistence and registry artefacts, change-window communication with WT, and pre-action notification triggers for high-impact actions. _(id: `lifecycle-rtmeth-011`)_
- **[MEDIUM | effort M]** (PhysicalSocial_Process_v1.0.docx) No safe handover from physical foothold to cyber post-exploitation team — Document the physical-to-cyber and cyber-to-physical handover including authorization re-confirmation, network segmentation/kill-switch and termination criteria. _(id: `lifecycle-physoc-018`)_
- **[LOW | effort S]** (ThreatScenarios_Process_v1.1.docx) CODENAME section does not state the convention or pattern to use — Document the Threat-Scenario codename convention explicitly (theme or 'no theme', allowed character set, register location). Cross-reference the Exercises and Operations conventions so the difference is intentional, not accidental. _(id: `lifecycle-threatscenarios-009`)_
- **[LOW | effort S]** (ThreatScenarios_Process_v1.1.docx) LLM-assisted scenario generation is recommended without guardrails on confidentiality / hallucination — Add a short paragraph to Scenarios Description on approved LLM use: which tools are approved, what may not be shared (codenames, real internal tool names, credentials), and that LLM output must be peer-reviewed before adoption. _(id: `lifecycle-threatscenarios-016`)_
- **[LOW | effort S]** (Operations_Process_v1.0.docx) OPLOG storage and integrity controls are unspecified — Mandate a central OPLOG repository with access control and audit trail; permit individual note-taking only as a working copy that is mirrored daily into the central store. _(id: `lifecycle-operations-012`)_
- **[LOW | effort S]** (Exercises_Process_v1.1.docx) Document-wide drift between 'Exercise' and 'Operation' terminology — Search/replace 'operation' with 'exercise' everywhere except where a deliberate cross-reference is intended; align with the Exercise / Operation / Threat Scenario taxonomy. _(id: `lifecycle-exercises-014`)_
- **[LOW | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) Acronym 'AET' used without definition — Expand AET on first use and link to the team charter / RACI; add a glossary if more in-house acronyms are introduced. _(id: `lifecycle-bhe-005`)_
- **[LOW | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) Document is at v0.1 'First Draft' and 16 months old without review evidence — Promote the document out of Draft, add owner / approver / next-review-date in a control block, and schedule an annual review. _(id: `lifecycle-bhe-015`)_
- **[LOW | effort S]** (RedTeam_Methodology_v0.3.docx) OPLOG free-format ('OneNote example') with no central retention or chain-of-custody rules — Define a central OPLOG location (shared, access-controlled), a minimum retention period, chain-of-custody / read-only export expectations, and a rule that personal OneNotes are working copies that must be transferred to the central log at engagement close. _(id: `lifecycle-rtmeth-015`)_
- **[LOW | effort S]** (RedTeam_Methodology_v0.3.docx) Versioning shows last update Oct 2024 (v0.3) and version still pre-1.0 for the central methodology — Promote the methodology to v1.0 once the gaps in this review are closed, add an approval/signoff line and an explicit review cadence (e.g. annual), and name a document owner. _(id: `lifecycle-rtmeth-018`)_
- **[LOW | effort S]** (RedTeam_Methodology_v0.3.docx) Engagement-type matrix referenced but unreadable in ingested content (axis labels duplicated, no axis values) — Replace the embedded matrix with either a properly captioned figure that survives DOCX export, or a small text table that places Threat Scenario / Operation / Exercise along the stealth and adversary-emulation axes explicitly. _(id: `lifecycle-rtmeth-019`)_
- **[LOW | effort S]** (RedTeam_Methodology_v0.3.docx) Terminology drift: 'WT' used but undefined; 'white cards (leg ups)' not aligned with TIBER-EU 'leg-ups' — Add a glossary entry for White Team (WT) and align 'white cards / leg ups' wording with TIBER-EU 'leg-ups' so reviewers and auditors can map the terminology. _(id: `tdora-rtmeth-012`)_
- **[LOW | effort S]** (Research_Methodology_v0.2.docx) Knowledge-capture mechanism named but not anchored: Research Repository is the wiki/register/deck? — Explicitly designate the Research Repository (or a sibling wiki) as the lessons-learned register, with an owner and a cadence for review. _(id: `lifecycle-research-012`)_
- **[LOW | effort S]** (PhysicalSocial_Process_v1.0.docx) Maturity / Vulnerability Score formulae are referenced but not rendered — Render the formulae (LaTeX or image with alt-text) inline and provide a worked example so the Maturity calculation is reproducible. _(id: `lifecycle-physoc-017`)_
- **[LOW | effort S]** (PhysicalSocial_Process_v1.0.docx) TIBER-EU terminology not used (no White Team, Control Team, TI provider, attestation) — When publishing the TLPT addendum, adopt TIBER-EU role names and provide a mapping from the existing 'Local CISO / Local Facilities Manager' wording to White Team / Control Team membership. _(id: `tdora-physoc-012`)_
- **[LOW | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Several figure references but no rendered diagrams; reproducibility of evidence is at risk — Re-export the document with figures embedded, or maintain an Annex (PDF) with worked examples; verify ingestion captures them. _(id: `lifecycle-physocq-011`)_
- **[LOW | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Typo / wording — 'wether' instead of 'whether' — Spell-check pass; fix 'wether' to 'whether' and review for similar typos. _(id: `lifecycle-physocq-012`)_
- **[INFORMATIONAL | effort S]** (Operations_Process_v1.0.docx) Deconfliction process references Figure 2 that is not present in the ingested content — Add an explicit cross-reference to the deconfliction diagram (resources/diagrams/deconfliction.drawio) in the Deconfliction section, including a one-line summary of the workflow it depicts. _(id: `lifecycle-operations-014`)_
- **[INFORMATIONAL | effort S]** (Operations_Process_v1.0.docx) Attack-path prioritisation table is informative but not linked to a governing register — Cross-reference the Attack Paths management file from this SOP, name its owner and review cadence, and ensure each Operation's chosen paths are pulled from it (rather than ad-hoc) for traceability. _(id: `lifecycle-operations-016`)_
- **[INFORMATIONAL | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) Tooling-process doc does not state which engagement type(s) consume BloodHound output — Add a 'Use in Engagements' section explicitly mapping BHE output into Exercise (recon, post-exploitation pathing), Operation (assumed-breach pathing) and Threat Scenario (joint walk-through of AD abuse paths) lifecycles, and state that BHE is a tooling methodology, not an engagement type itself. _(id: `lifecycle-bhe-001`)_
- **[INFORMATIONAL | effort S]** (Research_Methodology_v0.2.docx) Research methodology correctly positioned as cross-cutting; engagement-execution phases not applicable — Keep the cross-cutting positioning; ensure engagement-specific SOPs reference this document so research provenance is auditable from any engagement deliverable. _(id: `lifecycle-research-001`)_
- **[INFORMATIONAL | effort S]** (Research_Methodology_v0.2.docx) Document does not claim TIBER-EU / DORA TLPT alignment - largely out of scope for this evaluator — No TLPT alignment is claimed and none is required for this doc. Confirm by adding a one-line note that this methodology is engagement-type agnostic and is referenced (not itself governed) by any TIBER-EU / DORA TLPT engagement. _(id: `tdora-research-001`)_
- **[INFORMATIONAL | effort S]** (Research_Methodology_v0.2.docx) Internal research intake is not a substitute for an independent TI provider on TLPT engagements — Add one sentence clarifying that for TIBER-EU / DORA TLPT engagements the regulator-mandated independent TI provider and TTI report are still required; this internal research process is supplementary input, not a substitute. _(id: `tdora-research-003`)_
- **[INFORMATIONAL | effort S]** (Research_Methodology_v0.2.docx) Jurisdictional ambiguity: Euronext operates across multiple NCAs - research process should be jurisdiction-agnostic — Add a one-line jurisdictional note: this methodology is jurisdiction-agnostic; specific TIBER-XX / NCA / DORA TLPT obligations are inherited from the engagement scoping document. _(id: `tdora-research-005`)_
- **[INFORMATIONAL | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Engagement lifecycle phases beyond questionnaire scope are correctly absent — Confirm in the Introduction that the questionnaire is a scoping input artefact only and that engagement lifecycle phases live in the parent process and engagement SOPs. _(id: `lifecycle-physocq-014`)_

## Legal/Risk + Red team lead (4 items)

- **[HIGH | effort M]** (Research_Methodology_v0.2.docx) No legal / IP / responsible-disclosure review for capabilities derived from external research — Add a Legal/IP review gate to Capability Development covering third-party-code licensing, customer/vendor disclosure obligations, and a documented decision to publish, embargo, or keep internal. _(id: `lifecycle-research-003`)_
- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) Authorization chain is limited to Local CISO + Local Facilities Manager - no Legal, HR, Group Security or law-enforcement liaison — Expand authorization to require: Legal counter-signature, HR acknowledgement, Group Security awareness, landlord/building-security notification where premises are shared, and a documented decision on local law-enforcement pre-notification per jurisdiction. _(id: `lifecycle-physoc-006`)_
- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) No social-engineering rules: targeting limits, pretext approval, recording legality, executive carve-outs — Add a Social-engineering rules subsection covering target carve-outs, pretext approval, audio/video recording legality per jurisdiction, sock-puppet account governance and post-engagement decommissioning. _(id: `lifecycle-physoc-008`)_
- **[LOW | effort S]** (Exercises_Process_v1.1.docx) Data-handling references the US 'Privacy of Information Act (PIA)' instead of GDPR / EU regimes — Update the Data Handling section to reference GDPR (personal data), market-sensitive / inside information (MAR), client/financial data, and remove the US-style 'Privacy of Information Act' wording. _(id: `lifecycle-exercises-013`)_

## Red team lead / Risk & Compliance (3 items)

- **[CRITICAL | effort L]** (RedTeam_Methodology_v0.3.docx) TIBER-EU Preparation elements absent: GTL, scoping doc, engagement letter, critical-functions ID, provider procurement — Add a Preparation section to the methodology covering: GTL consumption, engagement letter template, critical/important-functions identification, and procurement criteria for independent TI and RT providers (or internal-tester arrangements). Verify each item against the live TIBER-EU v2 text and the DORA RTS on TLPT. _(id: `tdora-rtmeth-002`)_
- **[HIGH | effort M]** (RedTeam_Methodology_v0.3.docx) Methodology calls Exercises 'TIBER-Like' without committing to the TIBER-EU phase model or DORA TLPT requirements — Replace 'TIBER-Like' with one of two precise positions: (a) Exercises are run as TIBER-EU / DORA TLPT and follow the prescribed phases, actors, and artefacts (cross-reference per-NCA TIBER-XX guidance); or (b) Exercises are inspired by TIBER-EU but do not satisfy DORA Art.26 / TLPT — and remove any implication that they do. Verify against the live TIBER-EU v2 framework text and the relevant national TIBER-XX implementation. _(id: `tdora-rtmeth-001`)_
- **[HIGH | effort M]** (RedTeam_Methodology_v0.3.docx) Scoping does not reference DORA 'critical or important functions' nor commit to live-production testing under controls — Rewrite Scoping to reference Euronext's register of critical / important functions, describe how scope is derived from them, and confirm that production systems are in scope under controlled conditions. Verify the wording against DORA Art.26 and the RTS on TLPT. _(id: `tdora-rtmeth-009`)_

## Red team lead + Compliance (5 items)

- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) TIBER-EU Preparation phase elements (GTL, engagement letter, critical-functions identification, provider procurement) only partially present — Add explicit Preparation deliverables to the Initiation phase (or to the TLPT addendum): GTL ingestion, engagement letter, critical-or-important-functions list, provider procurement / qualification record. Cite DORA Art.26 and TIBER-EU Preparation when used. _(id: `tdora-exercises-002`)_
- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) White Team described, but no Control Team distinct from White Team / no TIBER Cyber Team / TCT engagement — Add (in the TLPT addendum or this SOP): Control Team identification distinct from WT where the framework requires it; named interface to the TCT / lead overseer; explicit naming of the institution-side test owner. _(id: `tdora-exercises-004`)_
- **[LOW | effort S]** (Exercises_Process_v1.1.docx) Terminology drift: 'White Team' usage may diverge from TIBER-EU 'White Team' role definition — Clarify WT/CT split for TLPT-framed Exercises (or document the deliberate combination). Keep current single-WT model for non-TLPT Exercises. _(id: `tdora-exercises-015`)_
- **[INFORMATIONAL | effort S]** (Exercises_Process_v1.1.docx) Doc is silent on TIBER-EU / DORA-TLPT applicability for Exercises — Add an Introduction paragraph noting that the Exercise may be performed as a TIBER-EU / DORA TLPT and that, when so framed, the addendum 'Exercise as TLPT' applies (control team, TI provider independence, attestation, etc.). _(id: `lifecycle-exercises-011`)_
- **[INFORMATIONAL | effort S]** (Exercises_Process_v1.1.docx) Exercise SOP does not position itself relative to TIBER-EU / DORA TLPT — Add an Introduction paragraph stating: (a) most Exercises are internal; (b) where an Exercise is run as a TIBER-EU / DORA TLPT, the TLPT addendum applies and overrides this SOP where they conflict; (c) the trigger criteria (entity in scope of DORA TLPT, designation by lead overseer). _(id: `tdora-exercises-001`)_

## Red team lead + Legal/Risk (7 items)

- **[CRITICAL | effort M]** (Exercises_Process_v1.1.docx) Authorization chain incomplete: no named legal sign-off, no kill-switch / abort criteria, no safe-words — Add an 'Authorization & Kill-switch' subsection: (1) named legal/risk sign-off prerequisite, (2) explicit abort criteria, (3) safe-word + 24/7 contact channel between RT lead and WT lead, (4) what 'stop' means operationally. _(id: `lifecycle-exercises-005`)_
- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) Initiation phase blurs scoping and authorization, lacks engagement letter / RoE sign-off gate — Restructure Initiation around named deliverables: scoping document + engagement letter + signed RoE. Make 'all three signed' a hard gate before Targeted TI commences. _(id: `lifecycle-exercises-008`)_
- **[MEDIUM | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) User-account-impact rule is sound but lacks a defined approver and audit trail — Specify the format and storage of the user written permission (e.g. ticket with manager approval), require IAM counter-signature for service or privileged accounts, and reference the engagement file where the artefact is stored. _(id: `lifecycle-bhe-011`)_
- **[MEDIUM | effort M]** (Research_Methodology_v0.2.docx) AI-enrichment layer described without governance, prompt provenance, or data-handling rules — Add an 'AI Enrichment governance' paragraph covering approved model/tenant, data-classification rules for inputs, prompt and version control, and how AI outputs are logged for audit. _(id: `lifecycle-research-004`)_
- **[MEDIUM | effort M]** (Research_Methodology_v0.2.docx) Reproduction of techniques against prod-like environments needs DORA test-risk-management framing — Add a paragraph that escalates a reproduction to TLPT test-risk-management controls when the environment touched is shared with critical or important functions; require control-team authorisation and reference DORA Art.26 safety controls. _(id: `tdora-research-004`)_
- **[LOW | effort S]** (Research_Methodology_v0.2.docx) Research Repository governance light on access control, retention, and classification — Document classification, retention, and audited access patterns for the Research Repository and the REDS Jira project; cross-reference internal data-classification policy. _(id: `lifecycle-research-011`)_
- **[INFORMATIONAL | effort S]** (PhysicalSocial_Process_v1.0.docx) NCA-specific guidance not referenced for any Euronext jurisdiction — Add a per-jurisdiction reference list and review it on each cycle so authorization, attestation and competent-authority notifications use the current national TIBER-XX or DORA RTS text. _(id: `tdora-physoc-010`)_

## Red team lead + Risk (3 items)

- **[HIGH | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) No authorization / sign-off chain triggered by questionnaire responses — Add an 'Approvals and Escalation' section with a sign-off matrix (site, security, red team, risk) and a rule that any Critical or High finding is escalated immediately rather than waiting for periodic review. _(id: `lifecycle-physocq-007`)_
- **[HIGH | effort M]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) No risk-screen for regulated environments, trading floors, customer-facing or vulnerable-people areas — Add a 'Site Context' question block covering: hosts critical/important DORA function (Y/N), trading or market-data infrastructure on-site, customer-facing footprint, presence of vulnerable people, and any regulator-mandated controls. Use the answers to gate sign-off. _(id: `lifecycle-physocq-006`)_
- **[INFORMATIONAL | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Questionnaire could surface DORA 'critical or important function' status of each office — Add a Site Context question identifying whether the office supports a DORA critical or important function, and use the answer (alongside CMDB criticality) to drive questionnaire periodicity and sign-off escalation. This also makes the artefact reusable as DORA Art.5 record-keeping evidence. _(id: `tdora-physocq-002`)_

## Red team lead / Legal & Risk (2 items)

- **[CRITICAL | effort M]** (RedTeam_Methodology_v0.3.docx) Authorization, Rules of Engagement, legal sign-off and kill-switch / abort criteria are not described — Add a dedicated 'Authorization & Rules of Engagement' section that points to a mandatory RoE template covering: approving authority, legal/risk sign-off, safe-words, kill-switch, abort criteria, blue-team notification rules per engagement type, and indemnities. Make sign-off a hard pre-execution gate. _(id: `lifecycle-rtmeth-003`)_
- **[HIGH | effort M]** (RedTeam_Methodology_v0.3.docx) Risk management of the test itself: no kill-switch, no rollback / safe-harbour clauses, no formal indemnity for testers — Add a 'Test risk management' subsection: kill-switch ownership, abort criteria, rollback expectations for persistence/registry artefacts, safe-harbour / indemnity language for testers. Reference the RoE template. _(id: `tdora-rtmeth-007`)_

## Red team lead / Purple team (2 items)

- **[CRITICAL | effort M]** (Operations_Process_v1.0.docx) No purple-teaming close-out with the blue team — Add an explicit 'Purple-team close-out' subsection under Closure: a mandatory live workshop with the BT to replay the scenario, map BT detections (or absence) against each TTP, and capture defensive improvements. Make the workshop a gating step before the Operation can be marked complete. _(id: `lifecycle-operations-003`)_
- **[HIGH | effort S]** (RedTeam_Methodology_v0.3.docx) Purple-teaming close-out described as conditional collaboration, not as a mandatory close-out for every engagement — Replace 'can happen' with explicit mandate: 'A purple-team close-out is required at the end of every Exercise, Operation and Threat Scenario. The Purple Teaming Process document defines the replay format, attendee list, alert/log correlation matrix, and improvement backlog.'. _(id: `lifecycle-rtmeth-004`)_

## Compliance + Red team lead + Legal (1 items)

- **[HIGH | effort L]** (Exercises_Process_v1.1.docx) No coordination with competent authority / lead overseer described — Add (in TLPT addendum) a section 'Authority coordination': identifying the lead overseer for each in-scope Euronext entity, the notification trigger and channel, the attestation deliverable, and the mutual-recognition workflow. Flag jurisdictional ambiguity where multiple NCAs could claim primacy. _(id: `tdora-exercises-006`)_

## Compliance + Red team lead + Procurement (1 items)

- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) Tester requirements (DORA Art.27) not addressed: internal vs external testers, qualifications, rotation — Add a 'Tester requirements' subsection citing DORA Art.27: criteria for external testers; conditions for using internal testers (rotation, independence); approval workflow when internal testers are used for a TLPT. _(id: `tdora-exercises-007`)_

## Legal & Privacy / Red team lead (1 items)

- **[HIGH | effort S]** (RedTeam_Methodology_v0.3.docx) Data Handling references US 'Privacy of Information Act (PIA)' — no GDPR / DORA legal basis cited — Replace the 'Privacy of Information Act (PIA)' reference with GDPR (and the applicable national data-protection law where engagements occur) and align the data categories with the lawful-basis and special-category framing. Where engagements are TIBER-EU framed, add a reference to the framework's data-handling expectations. _(id: `tdora-rtmeth-008`)_

## Legal / DPO (1 items)

- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) No GDPR lawful-basis statement for personal data captured during physical and social testing — Add a GDPR / data-protection section covering lawful basis, DPIA, retention, deletion and per-jurisdiction position on recording. Engage the DPO before next physical test. _(id: `tdora-physoc-009`)_

## Legal/DPO + Red team lead (1 items)

- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) No data-handling rules for material acquired during the engagement (photos, building maps, credentials, badge clones) — Add a 'Data handling and evidence custody' subsection prescribing encryption, access control, retention, secure destruction, and GDPR lawful-basis text for material captured during physical/social testing. _(id: `lifecycle-physoc-009`)_

## Legal/Risk + Data Protection Officer (1 items)

- **[HIGH | effort M]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) No data-protection / GDPR handling for questionnaire responses — Add a Data Handling section: state the lawful basis, require redaction of personal data in evidence (e.g. blur badge photos, mask names in access logs), mandate encrypted transit, define storage system + access control, and set a retention/destruction schedule consistent with the parent PhysicalSocial process. _(id: `lifecycle-physocq-003`)_

## Legal/Risk + Red team lead + Compliance (1 items)

- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) Risk-management of the test itself underspecified: no kill-switch, no safe-harbours / indemnities, no rollback plan — Add a 'Risk management of the test' subsection (in the TLPT addendum and this SOP): kill-switch and abort authority; safe-harbour / indemnity clauses for internal and external testers; rollback procedure; crisis-comms plan if a test triggers a real incident response. _(id: `tdora-exercises-009`)_

## Purple team / Red team lead (1 items)

- **[CRITICAL | effort M]** (PhysicalSocial_Process_v1.0.docx) No purple-teaming close-out with blue team and physical security — Add a 'Purple-team close-out' section after Report that mandates a joint replay with blue team, SOC and physical security covering timeline, IoCs/physical indicators, detection gaps and agreed control improvements. _(id: `lifecycle-physoc-003`)_

## Red team lead + AD/IAM owner (1 items)

- **[HIGH | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) Remediation section names no owner, no tracking system, no severity model and no SLA — Define a remediation workflow: who receives findings, in which ticketing system, severity per Tier-0 reachability, SLA per severity, and an explicit re-test loop using the next scheduled BHE collection to verify closure. _(id: `lifecycle-bhe-006`)_

## Red team lead + Blue team lead (1 items)

- **[CRITICAL | effort M]** (Exercises_Process_v1.1.docx) No mandatory purple-team close-out / replay with the blue team — Add a mandatory 'Purple-team replay' step in Closure: a working session with the BT walking the kill chain step-by-step, mapping each TTP to detections/preventions in place, and agreeing concrete defensive improvements. Capture as a deliverable (report annex or separate replay note). _(id: `lifecycle-exercises-001`)_

## Red team lead + IAM team (1 items)

- **[HIGH | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) Tenant access uses application accounts only; SAML/SSO and MFA not yet implemented — Track SAML/SSO + MFA enablement as a remediation item with an owner and date; in the meantime document compensating controls (named local accounts, password vaulting, enforced MFA at the app layer, quarterly access review) and a break-glass procedure. _(id: `lifecycle-bhe-004`)_

## Red team lead + IR lead (1 items)

- **[HIGH | effort M]** (Research_Methodology_v0.2.docx) Adjacent remit not addressed: research input to IR runbooks and to threat-hunting during external tests / live incidents — Add a section describing the three adjacent-remit flows: research -> IR runbook updates, research / RT support during external assessments, research / RT support during live incidents - including triggers and owners. _(id: `lifecycle-research-008`)_

## Red team lead + Legal/Risk + DPO (1 items)

- **[HIGH | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) No data-handling, retention or classification rules for collected AD/Entra graph data — Add a 'Data Handling' section: classify BHE collection data, define retention (e.g. snapshots purged N days after engagement close), state where the SaaS tenant stores data and the GDPR basis, and require Legal/Risk sign-off for any external sharing of attack-path graphs. _(id: `lifecycle-bhe-003`)_

## Red team lead + Legal/Risk + Facilities (1 items)

- **[HIGH | effort S]** (Exercises_Process_v1.1.docx) Physical scope not explicitly addressed (in or out of scope) — Add an explicit 'Physical scope' subsection under Initiation/Requirements. Default to 'must be agreed in writing as in or out of scope per exercise' and list the additional authorizations required if in scope (facilities, HR, building security). _(id: `lifecycle-exercises-004`)_

## Red team lead + Purple team / Detection Engineering (1 items)

- **[HIGH | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) No purple-team close-out / blue-team handover for BHE-derived findings — Add a 'Purple-team Handover' subsection requiring a debrief with SOC/Detection Engineering after each BHE remediation cycle: review prioritised attack paths, verify detection coverage for SharpHound collection and the abused edges, and log detection gaps into the backlog. _(id: `lifecycle-bhe-007`)_

## Red team lead + SOC lead + Legal/Risk (1 items)

- **[HIGH | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) No formal authorization / RoE for continuous AD enumeration, only an informal SOC heads-up — Reference (or include) an authorization template covering: which domains and OUs are in scope for SharpHound enumeration, the named approver, the formal SOC suppression/allowlisting agreement (not 'disregard alerts'), kill-switch / pause procedure, and reauthorization cadence. _(id: `lifecycle-bhe-002`)_

## Red team lead + TI lead (1 items)

- **[CRITICAL | effort L]** (PhysicalSocial_Process_v1.0.docx) All four TIBER-EU phases are absent for the physical leg — Add a TLPT-mode addendum that maps each Physical Pentest stage to the TIBER-EU phases: TTI-derived pretexts and objectives, control-team-supervised execution, replay-and-attestation closure. Keep the internal Maturity flow as the non-TLPT path. _(id: `tdora-physoc-002`)_

## Red team lead + Threat hunt (1 items)

- **[HIGH | effort S]** (Research_Methodology_v0.2.docx) Research methodology silent on threat-hunt hypothesis generation as a deliberate output — Add a 'Threat-hunt hypothesis output' artefact to Deep Dive and Capability Development; require it to be shared with the threat-hunt function on a defined cadence. _(id: `lifecycle-research-007`)_

## Red team lead / Legal / HR (1 items)

- **[CRITICAL | effort M]** (PhysicalSocial_Process_v1.0.docx) No kill-switch, abort criteria or check-in / emergency-contact protocol for operators on site — Add a 'Operator safety and check-ins' subsection to Planning specifying: control-point contact, mandatory check-in cadence, missed-check-in escalation, abort trigger words, in-country emergency contacts (medical / legal), permitted hours and clothing/identification. _(id: `lifecycle-physoc-005`)_

## Red team lead / Legal-Risk (1 items)

- **[CRITICAL | effort M]** (Operations_Process_v1.0.docx) Authorization phase is implicit; no legal sign-off, RoE artefact, safe-words, or abort criteria defined — Add an explicit Authorization section before Research & Preparation listing: the engagement letter / RoE owner, required signatories (legal, risk, business owner), safe-word convention, kill-switch authority, abort criteria, and a pre-flight checklist that must be signed before any RT activity. _(id: `lifecycle-operations-007`)_

## Red team lead / Risk-Compliance (3 items)

- **[HIGH | effort M]** (Operations_Process_v1.0.docx) 'White Team' role conflates TIBER-EU White Team and Control Team responsibilities — Either (a) introduce a separate Control Team role with the start/stop/approve authority and reduce White Team to the awareness/communication role per TIBER-EU, or (b) add a glossary note that this SOP uses 'White Team' as a combined CT+WT role for internal Operations and that for TLPT-aligned engagements the two roles are split. Verify TIBER-EU role definitions against the live framework. _(id: `tdora-operations-002`)_
- **[MEDIUM | effort S]** (Operations_Process_v1.0.docx) Critical / important functions (DORA terminology) are not used to drive scope — Add to Scoping a requirement that each Operation's objectives reference one or more critical or important functions from the institution's register, so that Operations evidence is reusable for DORA reporting. Verify the precise DORA article references against the live regulation. _(id: `tdora-operations-005`)_
- **[INFORMATIONAL | effort S]** (Operations_Process_v1.0.docx) SOP makes no reference to TIBER-EU or DORA TLPT; positioning vs the regulator-aligned framework is not stated — Add a one-paragraph 'Regulatory positioning' note clarifying that Operations are internal scenario-driven testing and are NOT TLPT, with a forward reference to the document that does govern TLPT-aligned engagements (likely the Exercises SOP or a dedicated TLPT procedure). Verify the exact DORA / TIBER-EU clauses cited against the live regulation text. _(id: `tdora-operations-001`)_

## Red team lead / Threat hunt (1 items)

- **[HIGH | effort M]** (Operations_Process_v1.0.docx) No threat-hunt handover from red findings — Add a Threat-Hunt Handover step in Closure: a structured artefact (per-TTP hunt hypothesis, data sources, expected telemetry, time horizon) that is delivered to the hunt team and tracked to closure. _(id: `lifecycle-operations-004`)_

## Red team lead with Compliance (2 items)

- **[HIGH | effort S]** (ThreatScenarios_Process_v1.1.docx) Document does not state that Threat Scenarios are not TLPT, leaving a misalignment risk if cited as DORA evidence — Add a single 'Regulatory positioning' sentence in the Introduction: Threat Scenarios are internal control validation, not TLPT; TLPT-scoped activity follows the Exercise process. Cross-reference Exercises and Operations process documents. _(id: `tdora-threatscenarios-002`)_
- **[INFORMATIONAL | effort S]** (ThreatScenarios_Process_v1.1.docx) Document does not claim TLPT / TIBER-EU alignment; engagement type is Threat Scenario, which is not TLPT-eligible — Keep the current framing. Optionally add a one-line statement near the Introduction that this process is not TLPT and that TLPT-scoped engagements follow the Exercise process under TIBER-EU. Verify the framework references against the live DORA regulation text and RTS on TLPT. _(id: `tdora-threatscenarios-001`)_

## Red team lead with Legal/Risk (1 items)

- **[CRITICAL | effort M]** (ThreatScenarios_Process_v1.1.docx) No authorization / Rules-of-Engagement section: no legal sign-off, no kill-switch, no abort criteria — Add a 'Rules of Engagement / Authorization' section to the Planning phase. As a minimum: named approver(s) per scope (system owner + Head of Red Team / CISO), explicit Legal sign-off where personal or production data is in scope, kill-switch and abort criteria, safe-word, and the contacts on call to invoke them. _(id: `lifecycle-threatscenarios-002`)_

## Red team lead with Purple team / SOC (1 items)

- **[CRITICAL | effort M]** (ThreatScenarios_Process_v1.1.docx) No purple-team close-out described, despite Threat Scenario format requiring blue team in the room — Add an explicit 'Purple-team close-out' phase between Execution and Report. Specify required attendees (red team operators, SOC/blue team representative, target system owner), the agenda (per-scenario walk-through, detections observed vs missed, control recommendations) and the output (jointly-signed action list feeding the Report). _(id: `lifecycle-threatscenarios-001`)_

## Red team lead with SOC/Blue team (1 items)

- **[HIGH | effort S]** (ThreatScenarios_Process_v1.1.docx) Planning is red-team-only; Threat Scenarios require joint planning with the blue team — Restructure Planning so that, after the red team's internal brainstorm, a mandatory joint planning workshop is held with the SOC / blue team and the system owner to agree scenarios, success criteria and the demonstration format. Document attendees and outputs. _(id: `lifecycle-threatscenarios-003`)_

## Red team lead with Threat hunt (1 items)

- **[HIGH | effort M]** (ThreatScenarios_Process_v1.1.docx) No threat-hunt handover from Threat Scenario findings to the hunt team — Add a 'Threat-hunt handover' subsection (after Purple-team close-out) describing how scenario outcomes translate into hunt hypotheses, what data sources are required, who owns each hunt, and how completed hunts feed back into the engagement record. _(id: `lifecycle-threatscenarios-004`)_

## Red team lead with system owner (1 items)

- **[HIGH | effort M]** (ThreatScenarios_Process_v1.1.docx) Blast-radius / safety controls for production tool abuse are vague — Add a 'Safety controls' subsection in Execution listing: dedicated test accounts/projects where possible, agreed execution windows, the change-management coordination point, a rollback plan and a named on-call contact authorised to pause/abort. _(id: `lifecycle-threatscenarios-010`)_

## Threat intel + Red team lead (1 items)

- **[HIGH | effort M]** (PhysicalSocial_Process_v1.0.docx) No Targeted Threat Intelligence input drives physical scenarios — Add a step that, when running under TLPT, the physical scenarios and pretexts are derived from a TTI report from an independent TI provider and mapped to MITRE ATT&CK techniques. _(id: `tdora-physoc-004`)_

## Threat intel / Red team lead (1 items)

- **[HIGH | effort L]** (RedTeam_Methodology_v0.3.docx) Threat Intelligence phase: no Targeted Threat Intelligence (TTI) report, no independent TI provider, no scenario-derivation method — Add a Threat Intelligence phase that requires a Targeted Threat Intelligence report, names the provider/function (with independence criteria), and shows how TTI drives scenario selection. Replace or supplement the legacy threat profiles with Euronext-specific, FMI-sector-relevant TTPs. _(id: `tdora-rtmeth-003`)_

## Threat intel lead + Red team lead + Compliance (1 items)

- **[HIGH | effort M]** (Exercises_Process_v1.1.docx) Threat Intelligence provider independence not addressed; TI and RT appear conflated — State explicitly that for TLPT-framed Exercises the TI provider must be independent of the RT provider, with a named Targeted Threat Intelligence Report deliverable. For internal Exercises, document that internal TI is acceptable but separation of responsibilities is recommended. _(id: `tdora-exercises-003`)_

## Compliance + Red team lead (1 items)

- **[MEDIUM | effort M]** (Exercises_Process_v1.1.docx) Document refers to 'a company' generically; jurisdictional applicability under DORA is not stated — Add an entity / jurisdiction applicability section: list in-scope Euronext entities, identify likely lead overseers, and link to per-entity TLPT addenda or NCA-specific guidance. _(id: `tdora-exercises-014`)_

## Compliance with Red team lead (1 items)

- **[MEDIUM | effort S]** (ThreatScenarios_Process_v1.1.docx) No jurisdictional / regulated-entity scope statement — Euronext spans multiple NCAs — Add a one-line scope-of-applicability statement: which Euronext regulated entities and jurisdictions the Threat Scenario process applies to. If multiple entities, note which NCA's TIBER-XX guidance is the reference point should the outputs be cited as resilience-testing evidence. _(id: `tdora-threatscenarios-006`)_

## Document author (2 items)

- **[LOW | effort S]** (Research_Methodology_v0.2.docx) Figure 1 referenced but no diagram present in this artefact — Either embed Figure 1 in the docx or link the canonical .drawio path so prose-to-diagram coherence can be reviewed in one pass. _(id: `lifecycle-research-013`)_
- **[LOW | effort S]** (Research_Methodology_v0.2.docx) Document at v0.2 - sub-1.0 status not flagged for downstream consumers — Add Status and Approver fields to the version table; mark v0.2 as Draft until reviewed by the red team lead. _(id: `lifecycle-research-014`)_

## IR / SOC liaison (1 items)

- **[LOW | effort S]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Stolen-asset IR section does not link to the corporate IR process or define notification timing — Cite the group-wide IR procedure by name and version, and specify the notification timing and reporting channel for stolen physical assets. _(id: `lifecycle-physocq-010`)_

## Legal/DPO + Compliance + Red team lead (1 items)

- **[MEDIUM | effort M]** (Exercises_Process_v1.1.docx) Data-protection clauses do not anchor on GDPR / DORA / sector regulation — Rewrite Data Handling around: GDPR (lawful basis, special categories), MAR/MiFID inside-information and client-data confidentiality, DORA TLPT confidentiality requirements. Provide a decision tree: encountered-data type -> required action (halt, notify, delete, retain under controls). _(id: `tdora-exercises-010`)_

## Legal/Risk (1 items)

- **[MEDIUM | effort M]** (PhysicalSocial_Process_v1.0.docx) Get-out-of-jail letter does not explicitly cover indemnification, insurance, bail funding or counsel access — Update the Get-out-of-jail letter template and policy to reference an indemnification clause, evidence of liability insurance, a 24/7 legal contact for detained operators, and bail/counsel funding commitments. _(id: `lifecycle-physoc-007`)_

## Purple team + Red team lead (1 items)

- **[MEDIUM | effort S]** (Research_Methodology_v0.2.docx) Purple-team feedback loop named but not defined as a gated close-out — Make purple-team close-out mandatory and define the structured artefacts it must produce that feed both the Research and Tool repositories (detection deltas, capability lifecycle changes, hunt hypotheses). _(id: `lifecycle-research-006`)_

## Red team lead + AD/IAM team (1 items)

- **[MEDIUM | effort S]** (BloodhoundEnterprise_Process_v0.1.docx) Service-account privilege model is described but not safety-bounded (e.g. optional Local Admin everywhere) — State Euronext's stance on the optional Local-Admin-everywhere grant (default: NO) and on LDAP cleartext fallback (default: blocked); record exceptions with a named approver and review date. _(id: `lifecycle-bhe-009`)_

## Red team lead + Awareness team (1 items)

- **[MEDIUM | effort M]** (PhysicalSocial_Questionnaire_Process_v1.0.docx) Social-engineering and tailgating posture not surveyed — Add a Social Engineering and Tailgating block covering visitor-escort enforcement, anti-tailgating measures, awareness training cadence, and reception protocol for unsolicited contacts. _(id: `lifecycle-physocq-009`)_

## Red team lead + Cloud security (1 items)

- **[MEDIUM | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) Doc covers on-prem AD but only nods at Entra ID; cloud-identity attack paths under-treated — Add an 'Entra ID' subsection covering collection setup, cloud Tier-0 baseline, hybrid attack paths, and a current-state note on whether cloud collection is enabled at Euronext. _(id: `lifecycle-bhe-012`)_

## Red team lead + Operational Resilience (1 items)

- **[MEDIUM | effort M]** (PhysicalSocial_Process_v1.0.docx) Critical / important functions not used to scope physical testing — Reconcile the location-criticality model with the entity's DORA register of critical or important functions; add an override that any location hosting a critical function automatically requires Pentest-grade testing. _(id: `tdora-physoc-011`)_

## Red team lead + Procurement + Legal/Compliance (1 items)

- **[MEDIUM | effort M]** (BloodhoundEnterprise_Process_v0.1.docx) Sensitive AD/Entra graph data is uploaded to a SaaS tenant without DORA-aligned ICT third-party / data-handling controls in the document — Reference the ICT third-party register entry for the BHE SaaS in this document (or in a linked Tooling Inventory), and ensure data-residency, exit-clause and sub-outsourcing items are tracked there. Verify the precise DORA articles cited against the live text. _(id: `tdora-bhe-003`)_

## Red team lead + White team lead (1 items)

- **[MEDIUM | effort S]** (Exercises_Process_v1.1.docx) Leg-Up process lacks logging requirements and impact on results / detection metrics — Update Leg-Ups section to require: (1) entry in an engagement leg-up log, (2) WT countersignature, (3) explicit tagging of any downstream finding as 'leg-up assisted' in the Closure report. _(id: `lifecycle-exercises-016`)_

## Red team lead / Legal & Privacy (1 items)

- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Data Handling references PIA (US act) and 'WT Point of Contact' but never defines WT or applies GDPR / EU data protection — Replace 'PIA' with the relevant EU legal basis (GDPR Art.6/9, applicable national law) and add explicit personal-data and confidential-data categories. Define the White Team / Control Team in a dedicated section so the 'WT Point of Contact' reference is anchored. _(id: `lifecycle-rtmeth-012`)_

## Red team lead / Threat intel (1 items)

- **[MEDIUM | effort S]** (Operations_Process_v1.0.docx) Threat intelligence sourcing does not distinguish open-source feeds from a TIBER-EU Targeted Threat Intelligence (TTI) report — Add a paragraph clarifying that Operations rely on opportunistic / internal CTI inputs and that any engagement intended to satisfy TLPT must additionally procure an independent TI provider producing a TTI report. Verify the TI-provider independence clause against the live RTS on TLPT. _(id: `tdora-operations-003`)_

## Red team lead / White team (3 items)

- **[MEDIUM | effort S]** (Operations_Process_v1.0.docx) Kill-switch authority is asserted but not procedurally defined — Add a Kill-Switch / Abort procedure: communication channel (out-of-band), safe-word, expected RT actions on abort (cease, preserve evidence, notify), and resumption protocol with WT sign-off. _(id: `lifecycle-operations-009`)_
- **[MEDIUM | effort S]** (Operations_Process_v1.0.docx) Leg-up authorization criteria and audit trail not defined — Add a Leg-Up procedure: written request from RT to WT, criteria for approval, mandatory recording in OPLOG and final report (including which objective was reached only with a leg-up), and rules for when a scenario should instead be marked 'not concluded'. _(id: `lifecycle-operations-015`)_
- **[LOW | effort S]** (Operations_Process_v1.0.docx) Clean-up step is described as a final note rather than a tracked phase — Replace the closing sentence with a Clean-Up checklist (per-artefact rows) that the RT operator and WT must jointly sign off; tie it to closure of the engagement ticket. _(id: `lifecycle-operations-013`)_

## Red team lead with Purple team (1 items)

- **[MEDIUM | effort M]** (ThreatScenarios_Process_v1.1.docx) Execution phases (Reconnaissance / Exploit / Escalation) read as a stealth kill-chain rather than a demonstrative walk-through — Reframe Execution to make the demonstrative nature explicit: keep Recon/Exploit/Escalation but add 'demonstration walk-through points' where the operator pauses to show the blue team the artefacts (logs, telemetry, alerts) that did or did not fire. Make clear this is not a stealth kill-chain. _(id: `lifecycle-threatscenarios-012`)_

## Red team lead with Threat intel (2 items)

- **[MEDIUM | effort S]** (ThreatScenarios_Process_v1.1.docx) Operator-driven threat-actor selection is not informed by a TTI product; acceptable here but should be stated so it cannot be cited as TIBER — Either (a) keep operator-driven threat-actor selection but note explicitly that this differs from TIBER-EU's TI phase, or (b) when a Threat Scenario is intended to feed broader TLPT preparation, document the consumption of an existing TTI/GTL produced for an Exercise so the inputs are traceable. _(id: `tdora-threatscenarios-003`)_
- **[LOW | effort S]** (ThreatScenarios_Process_v1.1.docx) Threat-actor selection guidance focuses on insiders but does not exclude relevant external actors — Update the Threat Actors guidance to include external-actor archetypes (compromised contractor, stolen-credential external attacker, supply-chain compromise) as candidates whenever the in-scope tool is reachable from outside the corporate perimeter or via a third party. _(id: `lifecycle-threatscenarios-015`)_

## Risk & Compliance / Red team lead (1 items)

- **[MEDIUM | effort S]** (RedTeam_Methodology_v0.3.docx) Jurisdictional ambiguity: methodology silent on which Euronext regulated entity / NCA the framework applies under — Add a short jurisdictional clause stating that for any engagement positioned as TIBER-EU / TLPT, the applicable NCA and the corresponding TIBER-XX implementation must be identified per engagement, with the lead overseer recorded in the engagement letter. _(id: `tdora-rtmeth-010`)_

## Threat intel lead (1 items)

- **[MEDIUM | effort M]** (Exercises_Process_v1.1.docx) Scenarios derived from TI but no Targeted Threat Intelligence Report deliverable named — Define a 'Targeted Threat Intelligence Report' deliverable in the TI phase, with template (threat actors, TTPs, attack hypotheses, scenario seeds, ATT&CK mapping), a named approver, and version control. _(id: `tdora-exercises-011`)_

## Threat intel lead + Red team lead (1 items)

- **[MEDIUM | effort S]** (Exercises_Process_v1.1.docx) TI provider independence not addressed; TI appears to be performed by the same team as RT — Add a paragraph in Targeted TI stating who can perform the TI (internal TI function, external provider) and confirming separation from the RT executors when feasible. Note that TLPT framing requires an independent TI provider. _(id: `lifecycle-exercises-009`)_
