# Remediation backlog — run 2026-05-12-1520

Findings grouped by recommended owner, then sorted by severity → effort (early wins first).

**Severity legend:** critical → high → medium → low → informational. **Effort:** S (small, hours) / M (medium, days) / L (large, weeks).

## Red team lead
_82 items_

- **high/S** `coherence-operations-001` — Rewrite Point-of-Contact uses of 'PoC' to 'Point of Contact' (full form) or 'PoC-contact'. Apply across Operations, Exercises, and Physical & Social process docs.
- **high/S** `coherence-operations-002` — Rewrite 'CTI' / 'CTI team' / 'CTI news' to 'TI' / 'Threat Intelligence Team' / 'TI news' in Operations_Process_v1.0.
- **high/S** `lifecycle-exercises-003` — Update the CODENAME section to require codenames drawn from known fictional characters (movies, TV, books), and to be logged in the engagement register. Provide one or two illustrative examples.
- **high/S** `lifecycle-operations-002` — Update the CODENAME section to state that Operation codenames must be drawn from known fictional characters (movies / TV / books), with examples and a register of used names to avoid collisions.
- **high/S** `lifecycle-operations-008` — Add a Scope subsection that explicitly addresses cyber + physical: state default in/out of scope, link to the Physical/Social process and questionnaire, and require the RoE to record physical scope per engagement.
- **high/S** `lifecycle-physoc-002` — Add a 'Codename' subsection to Planning requiring assignment of a unique codename per the team's theme convention and recording it on the Get-out-of-jail letter and the engagement register.
- **high/S** `lifecycle-physocq-002` — Add an 'Ownership and Custody' section naming the questionnaire owner, the office-side respondent role, the central reviewer, the storage repository (with access controls), and the response SLA.
- **high/S** `lifecycle-rtdeck-002` — Add a slide describing the codename convention (fictional-character theme for Exercises/Operations, codename-required-but-theme-flexible for Threat Scenarios) and link it to the corresponding sections of the per-type process docs.
- **high/S** `lifecycle-rtdeck-005` — Add a slide on cyber + physical scope, referencing the existing PhysicalSocial process docs so the deck does not give the impression the team is cyber-only.
- **high/S** `lifecycle-rtdeck-006` — Re-word Slide 11 so blue-team awareness rules are conditional on engagement type, and add a clarifying line that Threat Scenarios are explicitly collaborative.
- **high/S** `lifecycle-rtmeth-002` — Add a 'Codename Assignment' section to the methodology stating: every engagement (Exercise/Operation/Threat Scenario) is assigned a codename before authorization; Exercises and Operations follow the fictional-character theme; Threat Scenarios follow the team's alternative convention. Reference the codename register.
- **high/S** `lifecycle-rtmeth-007` — Add a 'Physical scope' subsection that confirms physical assessments are in scope, identifies the additional sign-offs required (site/facility owner, Legal), and references the PhysicalSocial Process document and questionnaire.
- **high/S** `lifecycle-threatscenarios-006` — Add a 'Lessons learned' step at the end of every Threat Scenario: a short retrospective populated by the red team (and ideally co-signed by blue), captured in a named register/wiki page, used as input to the next Planning brainstorm.
- **high/S** `lifecycle-threatscenarios-007` — In the Scope subsection, add a one-line statement on physical scope: by default out-of-scope for tool-focused Threat Scenarios, but explicitly in-scope when the scenario subject is a physical control (e.g. badge system, datacentre access, visitor flow).
- **high/M** `coherence-rt-process-diag-008` — Update RedTeamProcess.drawio RT-Test swimlane to 'Initial Foothold / Network Propagation / Action on Objectives', and add a per-engagement-type phase-mapping table to the methodology.
- **high/M** `coherence-threat-scenarios-007` — Rename 'Report' to 'Closure' in ThreatScenarios_Process_v1.1.docx; align contents to the Closure structure (Outcome, Vulnerabilities, OFIs, Purple-team close-out).
- **high/M** `lifecycle-operations-001` — Add an explicit 'Assumed-Breach Setup' phase before Initial Foothold (or replace Initial Foothold) that describes how the WT provisions the foothold, how scenarios are defined up front, and how scenario-driven execution differs from full kill-chain emulation.
- **high/M** `lifecycle-physoc-001` — Add a 'Relationship to engagement types' section that maps Physical Pentest / Audit / Questionnaire to Exercise, Operation and Threat Scenario, clarifies the stealth posture in each, and removes or relabels the 'Figure 1 - Threat Scenarios Phases' caption so it does not imply a Threat Scenario when the section describes a stealthy Pentest.
- **high/M** `lifecycle-research-002` — Add a 'Lab & Authorization' subsection requiring techniques be first reproduced in a named isolated lab, with documented authorization (and a stricter gate for any reproduction that needs prod-like or production data).
- **high/M** `lifecycle-research-005` — Define promotion criteria from Experimental -> Operational and require a 'tradecraft release note' that updates Exercise / Operation / Threat-Scenario playbooks and the ATT&CK technique map when a new capability lands.
- **high/M** `lifecycle-rtdeck-001` — Add a dedicated section near the front of the deck describing Exercises, Operations and Threat Scenarios side by side (shape, stealth posture, blue-team awareness, typical regulator overlap) so internal audiences cannot confuse one for another.
- **high/M** `lifecycle-rtdeck-011` — Add prose captions to each chart/SmartArt slide that summarise the diagram in two or three sentences so the deck conveys methodology even when the visual is illegible or stripped during conversion to other formats.
- **high/M** `lifecycle-rtmeth-014` — Rewrite the Scoping section to describe how scope is determined and recorded: identification of critical/important functions, in-scope and explicitly out-of-scope assets, identities and networks, time windows, blue-team-awareness rule per engagement type, and scoping document template. The current 'capability checklist' content should be moved to a separate 'Engagement feasibility' subsection.
- **high/M** `tdora-physoc-001` — Add a 'TIBER-EU / DORA TLPT alignment' section that (a) confirms physical and social vectors are eligible legs of a TLPT, (b) specifies that when run under TLPT the TI-derived scenarios drive the physical pretexts and objectives, and (c) routes the physical leg through the same control-team / white-team and attestation pathway as the cyber leg. Verify the exact framework text before publication.
- **medium/S** `coherence-apts-017` — Define the Tools team in the methodology, or rewrite the apts slide to attribute the action to an existing defined role.
- **medium/S** `coherence-cross-cutting-003` — Rewrite 'defending teams' to 'Blue Team' (or 'BT' after first reference) in the OPLOGS sections of all three SOPs and the methodology.
- **medium/S** `coherence-research-meth-006` — Use the qualified canonicals on first reference in Research_Methodology and the methodology doc. Update the Research_Process.drawio swimlane labels to match.
- **medium/S** `coherence-threat-scenarios-016` — Add the codename theme convention to the CODENAME subsection of all three engagement SOPs and to the methodology glossary. Maintain a codename register recording the chosen character per codename.
- **medium/S** `lifecycle-bhe-010` — Require peer-reviewed cleanup verification: a second team member checks the OPLOG against environment state and signs off; record the sign-off in the engagement file.
- **medium/S** `lifecycle-exercises-007` — Add a Closure step 'Lessons learned': structured retro covering RT, WT and (where appropriate) BT input, captured in the team knowledge base using a fixed template; include explicit follow-up actions and owners.
- **medium/S** `lifecycle-exercises-012` — Either re-ingest the document with diagram extraction enabled, or add prose descriptions / captions next to each figure reference (Phase ownership matrix, timeline, deconfliction flow, kill chain). Critical for the diagram-consistency evaluator to be meaningful.
- **medium/S** `lifecycle-physoc-013` — Add a 'Notification matrix' to Planning specifying for each assessment type who is in the know (white team) and who is blind (blue team / SOC), and when and how disclosure happens after the test.
- **medium/S** `lifecycle-physoc-015` — Add a hardware-implant inventory, chain-of-custody log, and explicit 'recovery and decommissioning' close-out step.
- **medium/S** `lifecycle-physocq-001` — Rewrite the Introduction to state that this is a periodic Physical Security Questionnaire issued to Euronext office locations (per CMDB criticality), referencing the parent PhysicalSocial process for the engagement-led testing flow.
- **medium/S** `lifecycle-physocq-005` — Add a Maturity-to-Periodicity table (e.g. Maturity ≥0.9 → 36 months, 0.7-0.9 → 24, 0.5-0.7 → 12, <0.5 → 6) and codify the override rule for sites with open critical findings.
- **medium/S** `lifecycle-research-009` — Add an explicit line clarifying scope of physical / social-engineering tradecraft research; align with the physical-social process docs.
- **medium/S** `lifecycle-research-015` — Introduce a small handling tier on OPSEC / detection notes (e.g. RT-only, share-with-purple, releasable) so capability documentation is shared safely.
- **medium/S** `lifecycle-rtdeck-009` — Replace named individuals with the team role ('Offensive Engineering & Research / Red Team'); list named operators only in per-engagement authorisation documents that are versioned and access-controlled.
- **medium/S** `lifecycle-rtdeck-012` — Add a one-line label per phase on Slides 12–14 and a master 'Phases at a glance' slide that maps the internal phase numbers to PTES and to TIBER-EU phases.
- **medium/S** `lifecycle-rtmeth-001` — Rewrite the introduction to list the three engagement types and describe Purple Teaming separately as a mandatory close-out across all three. Align with the team's published engagement taxonomy.
- **medium/S** `lifecycle-rtmeth-010` — Replace 'TIBER-Like' with one of two precise statements: (i) Exercises are run as TIBER-EU / DORA TLPT engagements and follow Preparation → TI → RTT → Closure with TCT/CT/WT/TI/RT actors; or (ii) Exercises are inspired by TIBER-EU but are not TLPT and do not satisfy DORA Art.26 — adjust the rest of the doc accordingly.
- **medium/S** `lifecycle-rtmeth-016` — Update the Threat Scenario paragraph to describe the assumed-breach, demonstrative, joint-planning structure and call out the typical internal-tool targets (GitLab, Jenkins, CI/CD, internal SaaS, secret stores, ticketing). State explicitly that stealth is not in scope.
- **medium/S** `lifecycle-rtmeth-017` — Rewrite the Operations paragraph: 'Operations are assumed-breach, scenario-scoped engagements with formal authorization, codename, and a small set of pre-defined objectives. They are typically used to test specific hypotheses or prove risks, and follow the Operations Process document.' Drop the 'outside the context of a formalized engagement' wording.
- **medium/S** `lifecycle-threatscenarios-008` — Move 'CODENAME' to be the first subsection of Planning and add a sentence on where the codename register lives (which document, who has access).
- **medium/S** `lifecycle-threatscenarios-013` — Reference the team's reporting template explicitly and document the severity scale used. Specify the minimum evidence required per finding (screenshot, OPLOG line(s), artefact path).
- **medium/S** `lifecycle-threatscenarios-014` — Promote clean-up to its own gated step at the end of Execution, with a checklist (accounts, files, persistence, scheduled jobs, config changes) and an explicit sign-off recorded in the engagement record.
- **medium/S** `tdora-exercises-012` — Add a paragraph in RT Test mapping Unified Kill Chain phases to TIBER-EU 'legs / flags / objectives'. Require ATT&CK technique IDs at each step. Provide a sample mapping table.
- **medium/S** `tdora-research-002` — Require engagement deliverables (RTT report, closure report, attestation pack) to cite the Research Repository and Tool Repository IDs of the techniques and capabilities used, so research provenance is auditable for TLPT.
- **medium/M** `coherence-cross-cutting-004` — Use 'Red Team Operator' on first reference in each doc; 'RT Operator' acceptable thereafter. Replace bare 'Operator(s)' in physical-social and the methodology where the team affiliation is not obvious from context.
- **medium/M** `lifecycle-exercises-010` — Add an 'OPSEC and detection capture' note to the RT Test phase: stealth is in scope; the RT records every BT detection event (or absence thereof) per TTP; produce time-to-detect / time-to-contain metrics as a Closure deliverable.
- **medium/M** `lifecycle-exercises-015` — Define the reporting taxonomy: severity rubric, mandatory evidence fields, ATT&CK technique ID per finding, and scenario-to-finding linkage. Provide a report template.
- **medium/M** `lifecycle-operations-010` — Introduce a named Scoping step with a scoping document template (in-scope, out-of-scope, objectives, success criteria, constraints, third-party dependencies) and require WT sign-off before the RT Test begins. Replace 'anything is in scope' with explicit boundaries.
- **medium/M** `lifecycle-physoc-018` — Document the physical-to-cyber and cyber-to-physical handover including authorization re-confirmation, network segmentation/kill-switch and termination criteria.
- **medium/M** `lifecycle-rtmeth-011` — Expand the Forbidden Attacks section into a 'Safety & blast-radius controls' section: lab-first testing requirement (already present), explicit rollback/cleanup expectations for persistence and registry artefacts, change-window communication with WT, and pre-action notification triggers for high-impact actions.
- **medium/M** `lifecycle-threatscenarios-011` — Mandate a single OPLOG storage location (or a small approved set), specify access controls, retention period and a standard export schema (CSV/JSON) so logs are usable by IR. Personal note-taking apps remain acceptable as scratch but the canonical OPLOG must live in the approved location.
- **low/S** `coherence-rt-process-diag-015` — Introduce 'OFI (Opportunities For Improvement)' in the methodology glossary on first use; add an OFI block to the Closure/Report phase of every engagement-type SOP.
- **low/S** `coherence-tools-005` — Single corpus-wide find/replace pass for the listed cosmetic drift items. Low-risk cleanup.
- **low/S** `lifecycle-bhe-005` — Expand AET on first use and link to the team charter / RACI; add a glossary if more in-house acronyms are introduced.
- **low/S** `lifecycle-bhe-015` — Promote the document out of Draft, add owner / approver / next-review-date in a control block, and schedule an annual review.
- **low/S** `lifecycle-exercises-014` — Search/replace 'operation' with 'exercise' everywhere except where a deliberate cross-reference is intended; align with the Exercise / Operation / Threat Scenario taxonomy.
- **low/S** `lifecycle-operations-012` — Mandate a central OPLOG repository with access control and audit trail; permit individual note-taking only as a working copy that is mirrored daily into the central store.
- **low/S** `lifecycle-physoc-017` — Render the formulae (LaTeX or image with alt-text) inline and provide a worked example so the Maturity calculation is reproducible.
- **low/S** `lifecycle-physocq-011` — Re-export the document with figures embedded, or maintain an Annex (PDF) with worked examples; verify ingestion captures them.
- **low/S** `lifecycle-physocq-012` — Spell-check pass; fix 'wether' to 'whether' and review for similar typos.
- **low/S** `lifecycle-research-012` — Explicitly designate the Research Repository (or a sibling wiki) as the lessons-learned register, with an owner and a cadence for review.
- **low/S** `lifecycle-rtdeck-008` — Correct the typo and, while there, name the severity / scoring framework actually used (e.g. CVSS, internal severity model) so 'framework to assess results' is concrete rather than aspirational.
- **low/S** `lifecycle-rtdeck-014` — Confirm whether Slides 25–27 are intentionally blank; if so add titles, if not investigate ingest fidelity.
- **low/S** `lifecycle-rtmeth-015` — Define a central OPLOG location (shared, access-controlled), a minimum retention period, chain-of-custody / read-only export expectations, and a rule that personal OneNotes are working copies that must be transferred to the central log at engagement close.
- **low/S** `lifecycle-rtmeth-018` — Promote the methodology to v1.0 once the gaps in this review are closed, add an approval/signoff line and an explicit review cadence (e.g. annual), and name a document owner.
- **low/S** `lifecycle-rtmeth-019` — Replace the embedded matrix with either a properly captioned figure that survives DOCX export, or a small text table that places Threat Scenario / Operation / Exercise along the stealth and adversary-emulation axes explicitly.
- **low/S** `lifecycle-threatscenarios-009` — Document the Threat-Scenario codename convention explicitly (theme or 'no theme', allowed character set, register location). Cross-reference the Exercises and Operations conventions so the difference is intentional, not accidental.
- **low/S** `lifecycle-threatscenarios-016` — Add a short paragraph to Scenarios Description on approved LLM use: which tools are approved, what may not be shared (codenames, real internal tool names, credentials), and that LLM output must be peer-reviewed before adoption.
- **low/S** `tdora-physoc-012` — When publishing the TLPT addendum, adopt TIBER-EU role names and provide a mapping from the existing 'Local CISO / Local Facilities Manager' wording to White Team / Control Team membership.
- **low/S** `tdora-rtmeth-012` — Add a glossary entry for White Team (WT) and align 'white cards / leg ups' wording with TIBER-EU 'leg-ups' so reviewers and auditors can map the terminology.
- **informational/S** `lifecycle-bhe-001` — Add a 'Use in Engagements' section explicitly mapping BHE output into Exercise (recon, post-exploitation pathing), Operation (assumed-breach pathing) and Threat Scenario (joint walk-through of AD abuse paths) lifecycles, and state that BHE is a tooling methodology, not an engagement type itself.
- **informational/S** `lifecycle-operations-014` — Add an explicit cross-reference to the deconfliction diagram (resources/diagrams/deconfliction.drawio) in the Deconfliction section, including a one-line summary of the workflow it depicts.
- **informational/S** `lifecycle-operations-016` — Cross-reference the Attack Paths management file from this SOP, name its owner and review cadence, and ensure each Operation's chosen paths are pulled from it (rather than ad-hoc) for traceability.
- **informational/S** `lifecycle-physocq-014` — Confirm in the Introduction that the questionnaire is a scoping input artefact only and that engagement lifecycle phases live in the parent process and engagement SOPs.
- **informational/S** `lifecycle-research-001` — Keep the cross-cutting positioning; ensure engagement-specific SOPs reference this document so research provenance is auditable from any engagement deliverable.
- **informational/S** `tdora-research-001` — No TLPT alignment is claimed and none is required for this doc. Confirm by adding a one-line note that this methodology is engagement-type agnostic and is referenced (not itself governed) by any TIBER-EU / DORA TLPT engagement.
- **informational/S** `tdora-research-003` — Add one sentence clarifying that for TIBER-EU / DORA TLPT engagements the regulator-mandated independent TI provider and TTI report are still required; this internal research process is supplementary input, not a substitute.
- **informational/S** `tdora-research-005` — Add a one-line jurisdictional note: this methodology is jurisdiction-agnostic; specific TIBER-XX / NCA / DORA TLPT obligations are inherited from the engagement scoping document.

## Red team lead + Legal/Risk
_8 items_

- **critical/M** `lifecycle-exercises-005` — Add an 'Authorization & Kill-switch' subsection: (1) named legal/risk sign-off prerequisite, (2) explicit abort criteria, (3) safe-word + 24/7 contact channel between RT lead and WT lead, (4) what 'stop' means operationally.
- **high/M** `lifecycle-exercises-008` — Restructure Initiation around named deliverables: scoping document + engagement letter + signed RoE. Make 'all three signed' a hard gate before Targeted TI commences.
- **medium/S** `lifecycle-bhe-011` — Specify the format and storage of the user written permission (e.g. ticket with manager approval), require IAM counter-signature for service or privileged accounts, and reference the engagement file where the artefact is stored.
- **medium/M** `lifecycle-research-004` — Add an 'AI Enrichment governance' paragraph covering approved model/tenant, data-classification rules for inputs, prompt and version control, and how AI outputs are logged for audit.
- **medium/M** `tdora-research-004` — Add a paragraph that escalates a reproduction to TLPT test-risk-management controls when the environment touched is shared with critical or important functions; require control-team authorisation and reference DORA Art.26 safety controls.
- **low/S** `lifecycle-research-011` — Document classification, retention, and audited access patterns for the Research Repository and the REDS Jira project; cross-reference internal data-classification policy.
- **low/M** `coherence-apts-014` — Add a 'Regulatory mapping' subsection to the methodology that expands TLPT / TIBER-EU / CBEST, summarises TIBER-EU phases, and maps engagement types to a TLPT exercise. Add a 'Tier model' subsection defining T0/T1/T2 with criteria and examples.
- **informational/S** `tdora-physoc-010` — Add a per-jurisdiction reference list and review it on each cycle so authorization, attestation and competent-authority notifications use the current national TIBER-XX or DORA RTS text.

## Red team lead, Legal/Risk
_6 items_

- **high/M** `tdora-rtdeck-001` — Add a slide positioning the team's three engagement types against TIBER-EU v2 and DORA TLPT: which (Exercises) may be run under TIBER-EU with a Control Team / TI provider; which (Operations, Threat Scenarios) are internal-only and can be cited as DORA operational-resilience evidence but are not themselves TLPT.
- **high/M** `tdora-rtdeck-002` — If any engagement is to be positioned as TIBER-EU / TLPT, explicitly add Control Team and independent Threat Intelligence provider to the actor model and explain how internal-RT TTI is handled (separation of duties or external TI for TLPT runs). Otherwise state that the deck describes the internal, non-TLPT operating model only.
- **medium/S** `lifecycle-rtdeck-007` — Expand the RoE slide to enumerate authorisation chain, kill-switch / abort, safe-words, evidence handling and data-protection, and cross-reference the per-type process docs for full templates.
- **medium/S** `tdora-rtdeck-006` — Add a safety-controls slide naming kill-switch, rollback, safe-harbours / indemnities, and data-protection treatment; cross-reference per-type process docs for full procedures.
- **low/S** `lifecycle-rtdeck-015` — Apply a classification footer / cover-page marking, and decide whether C2 implementation detail belongs in the master explainer deck or in a separate tooling deck with tighter access controls.
- **low/S** `tdora-rtdeck-008` — Add a positioning statement that the deck describes the internal red-teaming methodology only and that TLPT runs require additional actors (Control Team, independent TI provider), additional artefacts (TTI, attestation) and authority coordination — with a pointer to the document or owner that governs TLPT engagement.

## Red team lead + Compliance
_5 items_

- **high/M** `tdora-exercises-002` — Add explicit Preparation deliverables to the Initiation phase (or to the TLPT addendum): GTL ingestion, engagement letter, critical-or-important-functions list, provider procurement / qualification record. Cite DORA Art.26 and TIBER-EU Preparation when used.
- **high/M** `tdora-exercises-004` — Add (in the TLPT addendum or this SOP): Control Team identification distinct from WT where the framework requires it; named interface to the TCT / lead overseer; explicit naming of the institution-side test owner.
- **low/S** `tdora-exercises-015` — Clarify WT/CT split for TLPT-framed Exercises (or document the deliberate combination). Keep current single-WT model for non-TLPT Exercises.
- **informational/S** `lifecycle-exercises-011` — Add an Introduction paragraph noting that the Exercise may be performed as a TIBER-EU / DORA TLPT and that, when so framed, the addendum 'Exercise as TLPT' applies (control team, TI provider independence, attestation, etc.).
- **informational/S** `tdora-exercises-001` — Add an Introduction paragraph stating: (a) most Exercises are internal; (b) where an Exercise is run as a TIBER-EU / DORA TLPT, the TLPT addendum applies and overrides this SOP where they conflict; (c) the trigger criteria (entity in scope of DORA TLPT, designation by lead overseer).

## Legal/Risk + Red team lead
_4 items_

- **high/M** `lifecycle-physoc-006` — Expand authorization to require: Legal counter-signature, HR acknowledgement, Group Security awareness, landlord/building-security notification where premises are shared, and a documented decision on local law-enforcement pre-notification per jurisdiction.
- **high/M** `lifecycle-physoc-008` — Add a Social-engineering rules subsection covering target carve-outs, pretext approval, audio/video recording legality per jurisdiction, sock-puppet account governance and post-engagement decommissioning.
- **high/M** `lifecycle-research-003` — Add a Legal/IP review gate to Capability Development covering third-party-code licensing, customer/vendor disclosure obligations, and a documented decision to publish, embargo, or keep internal.
- **low/S** `lifecycle-exercises-013` — Update the Data Handling section to reference GDPR (personal data), market-sensitive / inside information (MAR), client/financial data, and remove the US-style 'Privacy of Information Act' wording.

## Red team lead + Blue team lead
_3 items_

- **critical/M** `lifecycle-exercises-001` — Add a mandatory 'Purple-team replay' step in Closure: a working session with the BT walking the kill chain step-by-step, mapping each TTP to detections/preventions in place, and agreeing concrete defensive improvements. Capture as a deliverable (report annex or separate replay note).
- **high/M** `coherence-rt-meth-009` — Add a 'Purple-team close-out' subsection to the Closure/Report phase of each of the three engagement-type SOPs, with concrete RACI and outputs.
- **medium/L** `coherence-rt-meth-010` — Author 'Purple_Teaming_Process.docx' to anchor the cross-reference, OR rewrite the methodology to point to per-SOP purple-team subsections.

## Red team lead + Risk
_3 items_

- **high/S** `lifecycle-physocq-007` — Add an 'Approvals and Escalation' section with a sign-off matrix (site, security, red team, risk) and a rule that any Critical or High finding is escalated immediately rather than waiting for periodic review.
- **high/M** `lifecycle-physocq-006` — Add a 'Site Context' question block covering: hosts critical/important DORA function (Y/N), trading or market-data infrastructure on-site, customer-facing footprint, presence of vulnerable people, and any regulator-mandated controls. Use the answers to gate sign-off.
- **informational/S** `tdora-physocq-002` — Add a Site Context question identifying whether the office supports a DORA critical or important function, and use the answer (alongside CMDB criticality) to drive questionnaire periodicity and sign-off escalation. This also makes the artefact reusable as DORA Art.5 record-keeping evidence.

## Red team lead / Risk & Compliance
_3 items_

- **critical/M** `tdora-rtmeth-004` — Add a 'TLPT actors' section defining White Team, Control Team, TI provider, RT provider, and the institution's interactions with the TCT / lead overseer for engagements positioned as TIBER-EU. Make 'WT Point of Contact' a downstream reference, not the only mention of the role.
- **high/M** `tdora-rtmeth-001` — Replace 'TIBER-Like' with one of two precise positions: (a) Exercises are run as TIBER-EU / DORA TLPT and follow the prescribed phases, actors, and artefacts (cross-reference per-NCA TIBER-XX guidance); or (b) Exercises are inspired by TIBER-EU but do not satisfy DORA Art.26 / TLPT — and remove any implication that they do. Verify against the live TIBER-EU v2 framework text and the relevant national TIBER-XX implementation.
- **high/M** `tdora-rtmeth-009` — Rewrite Scoping to reference Euronext's register of critical / important functions, describe how scope is derived from them, and confirm that production systems are in scope under controlled conditions. Verify the wording against DORA Art.26 and the RTS on TLPT.

## Red team lead / Risk-Compliance
_3 items_

- **high/M** `tdora-operations-002` — Either (a) introduce a separate Control Team role with the start/stop/approve authority and reduce White Team to the awareness/communication role per TIBER-EU, or (b) add a glossary note that this SOP uses 'White Team' as a combined CT+WT role for internal Operations and that for TLPT-aligned engagements the two roles are split. Verify TIBER-EU role definitions against the live framework.
- **medium/S** `tdora-operations-005` — Add to Scoping a requirement that each Operation's objectives reference one or more critical or important functions from the institution's register, so that Operations evidence is reusable for DORA reporting. Verify the precise DORA article references against the live regulation.
- **informational/S** `tdora-operations-001` — Add a one-paragraph 'Regulatory positioning' note clarifying that Operations are internal scenario-driven testing and are NOT TLPT, with a forward reference to the document that does govern TLPT-aligned engagements (likely the Exercises SOP or a dedicated TLPT procedure). Verify the exact DORA / TIBER-EU clauses cited against the live regulation text.

## Red team lead / White team
_3 items_

- **medium/S** `lifecycle-operations-009` — Add a Kill-Switch / Abort procedure: communication channel (out-of-band), safe-word, expected RT actions on abort (cease, preserve evidence, notify), and resumption protocol with WT sign-off.
- **medium/S** `lifecycle-operations-015` — Add a Leg-Up procedure: written request from RT to WT, criteria for approval, mandatory recording in OPLOG and final report (including which objective was reached only with a leg-up), and rules for when a scenario should instead be marked 'not concluded'.
- **low/S** `lifecycle-operations-013` — Replace the closing sentence with a Clean-Up checklist (per-artefact rows) that the RT operator and WT must jointly sign off; tie it to closure of the engagement ticket.

## Document author
_2 items_

- **low/S** `lifecycle-research-013` — Either embed Figure 1 in the docx or link the canonical .drawio path so prose-to-diagram coherence can be reviewed in one pass.
- **low/S** `lifecycle-research-014` — Add Status and Approver fields to the version table; mark v0.2 as Draft until reviewed by the red team lead.

## Red team lead / Legal & Risk
_2 items_

- **critical/M** `lifecycle-rtmeth-003` — Add a dedicated 'Authorization & Rules of Engagement' section that points to a mandatory RoE template covering: approving authority, legal/risk sign-off, safe-words, kill-switch, abort criteria, blue-team notification rules per engagement type, and indemnities. Make sign-off a hard pre-execution gate.
- **high/M** `tdora-rtmeth-007` — Add a 'Test risk management' subsection: kill-switch ownership, abort criteria, rollback expectations for persistence/registry artefacts, safe-harbour / indemnity language for testers. Reference the RoE template.

## Red team lead / Purple team
_2 items_

- **critical/M** `lifecycle-operations-003` — Add an explicit 'Purple-team close-out' subsection under Closure: a mandatory live workshop with the BT to replay the scenario, map BT detections (or absence) against each TTP, and capture defensive improvements. Make the workshop a gating step before the Operation can be marked complete.
- **high/S** `lifecycle-rtmeth-004` — Replace 'can happen' with explicit mandate: 'A purple-team close-out is required at the end of every Exercise, Operation and Threat Scenario. The Purple Teaming Process document defines the replay format, attendee list, alert/log correlation matrix, and improvement backlog.'

## Red team lead with Compliance
_2 items_

- **high/S** `tdora-threatscenarios-002` — Add a single 'Regulatory positioning' sentence in the Introduction: Threat Scenarios are internal control validation, not TLPT; TLPT-scoped activity follows the Exercise process. Cross-reference Exercises and Operations process documents.
- **informational/S** `tdora-threatscenarios-001` — Keep the current framing. Optionally add a one-line statement near the Introduction that this process is not TLPT and that TLPT-scoped engagements follow the Exercise process under TIBER-EU. Verify the framework references against the live DORA regulation text and RTS on TLPT.

## Red team lead with Threat intel
_2 items_

- **medium/S** `tdora-threatscenarios-003` — Either (a) keep operator-driven threat-actor selection but note explicitly that this differs from TIBER-EU's TI phase, or (b) when a Threat Scenario is intended to feed broader TLPT preparation, document the consumption of an existing TTI/GTL produced for an Exercise so the inputs are traceable.
- **low/S** `lifecycle-threatscenarios-015` — Update the Threat Actors guidance to include external-actor archetypes (compromised contractor, stolen-credential external attacker, supply-chain compromise) as candidates whenever the in-scope tool is reachable from outside the corporate perimeter or via a third party.

## Compliance + Red team lead
_1 items_

- **medium/M** `tdora-exercises-014` — Add an entity / jurisdiction applicability section: list in-scope Euronext entities, identify likely lead overseers, and link to per-entity TLPT addenda or NCA-specific guidance.

## Compliance + Red team lead + Legal
_1 items_

- **high/L** `tdora-exercises-006` — Add (in TLPT addendum) a section 'Authority coordination': identifying the lead overseer for each in-scope Euronext entity, the notification trigger and channel, the attestation deliverable, and the mutual-recognition workflow. Flag jurisdictional ambiguity where multiple NCAs could claim primacy.

## Compliance + Red team lead + Procurement
_1 items_

- **high/M** `tdora-exercises-007` — Add a 'Tester requirements' subsection citing DORA Art.27: criteria for external testers; conditions for using internal testers (rotation, independence); approval workflow when internal testers are used for a TLPT.

## Compliance with Red team lead
_1 items_

- **medium/S** `tdora-threatscenarios-006` — Add a one-line scope-of-applicability statement: which Euronext regulated entities and jurisdictions the Threat Scenario process applies to. If multiple entities, note which NCA's TIBER-XX guidance is the reference point should the outputs be cited as resilience-testing evidence.

## IR / SOC liaison
_1 items_

- **low/S** `lifecycle-physocq-010` — Cite the group-wide IR procedure by name and version, and specify the notification timing and reporting channel for stolen physical assets.

## Legal & Privacy / Red team lead
_1 items_

- **high/S** `tdora-rtmeth-008` — Replace the 'Privacy of Information Act (PIA)' reference with GDPR (and the applicable national data-protection law where engagements occur) and align the data categories with the lawful-basis and special-category framing. Where engagements are TIBER-EU framed, add a reference to the framework's data-handling expectations.

## Legal / DPO
_1 items_

- **high/M** `tdora-physoc-009` — Add a GDPR / data-protection section covering lawful basis, DPIA, retention, deletion and per-jurisdiction position on recording. Engage the DPO before next physical test.

## Legal/DPO + Compliance + Red team lead
_1 items_

- **medium/M** `tdora-exercises-010` — Rewrite Data Handling around: GDPR (lawful basis, special categories), MAR/MiFID inside-information and client-data confidentiality, DORA TLPT confidentiality requirements. Provide a decision tree: encountered-data type -> required action (halt, notify, delete, retain under controls).

## Legal/DPO + Red team lead
_1 items_

- **high/M** `lifecycle-physoc-009` — Add a 'Data handling and evidence custody' subsection prescribing encryption, access control, retention, secure destruction, and GDPR lawful-basis text for material captured during physical/social testing.

## Legal/Risk
_1 items_

- **medium/M** `lifecycle-physoc-007` — Update the Get-out-of-jail letter template and policy to reference an indemnification clause, evidence of liability insurance, a 24/7 legal contact for detained operators, and bail/counsel funding commitments.

## Legal/Risk + Data Protection Officer
_1 items_

- **high/M** `lifecycle-physocq-003` — Add a Data Handling section: state the lawful basis, require redaction of personal data in evidence (e.g. blur badge photos, mask names in access logs), mandate encrypted transit, define storage system + access control, and set a retention/destruction schedule consistent with the parent PhysicalSocial process.

## Legal/Risk + Red team lead + Compliance
_1 items_

- **high/M** `tdora-exercises-009` — Add a 'Risk management of the test' subsection (in the TLPT addendum and this SOP): kill-switch and abort authority; safe-harbour / indemnity clauses for internal and external testers; rollback procedure; crisis-comms plan if a test triggers a real incident response.

## Purple team + Red team lead
_1 items_

- **medium/S** `lifecycle-research-006` — Make purple-team close-out mandatory and define the structured artefacts it must produce that feed both the Research and Tool repositories (detection deltas, capability lifecycle changes, hunt hypotheses).

## Purple team / Red team lead
_1 items_

- **critical/M** `lifecycle-physoc-003` — Add a 'Purple-team close-out' section after Report that mandates a joint replay with blue team, SOC and physical security covering timeline, IoCs/physical indicators, detection gaps and agreed control improvements.

## Red team lead + AD/IAM owner
_1 items_

- **high/M** `lifecycle-bhe-006` — Define a remediation workflow: who receives findings, in which ticketing system, severity per Tier-0 reachability, SLA per severity, and an explicit re-test loop using the next scheduled BHE collection to verify closure.

## Red team lead + AD/IAM team
_1 items_

- **medium/S** `lifecycle-bhe-009` — State Euronext's stance on the optional Local-Admin-everywhere grant (default: NO) and on LDAP cleartext fallback (default: blocked); record exceptions with a named approver and review date.

## Red team lead + AET lead
_1 items_

- **medium/M** `coherence-bloodhound-013` — Add an 'Assessment & Exploitation Team (AET)' subsection to the methodology with charter, scope, and RACI vs the Red Team.

## Red team lead + Awareness team
_1 items_

- **medium/M** `lifecycle-physocq-009` — Add a Social Engineering and Tailgating block covering visitor-escort enforcement, anti-tailgating measures, awareness training cadence, and reception protocol for unsolicited contacts.

## Red team lead + Cloud security
_1 items_

- **medium/M** `lifecycle-bhe-012` — Add an 'Entra ID' subsection covering collection setup, cloud Tier-0 baseline, hybrid attack paths, and a current-state note on whether cloud collection is enabled at Euronext.

## Red team lead + IAM team
_1 items_

- **high/M** `lifecycle-bhe-004` — Track SAML/SSO + MFA enablement as a remediation item with an owner and date; in the meantime document compensating controls (named local accounts, password vaulting, enforced MFA at the app layer, quarterly access review) and a break-glass procedure.

## Red team lead + IR lead
_1 items_

- **high/M** `lifecycle-research-008` — Add a section describing the three adjacent-remit flows: research -> IR runbook updates, research / RT support during external assessments, research / RT support during live incidents - including triggers and owners.

## Red team lead + Legal/Risk + DPO
_1 items_

- **high/M** `lifecycle-bhe-003` — Add a 'Data Handling' section: classify BHE collection data, define retention (e.g. snapshots purged N days after engagement close), state where the SaaS tenant stores data and the GDPR basis, and require Legal/Risk sign-off for any external sharing of attack-path graphs.

## Red team lead + Legal/Risk + Facilities
_1 items_

- **high/S** `lifecycle-exercises-004` — Add an explicit 'Physical scope' subsection under Initiation/Requirements. Default to 'must be agreed in writing as in or out of scope per exercise' and list the additional authorizations required if in scope (facilities, HR, building security).

## Red team lead + Operational Resilience
_1 items_

- **medium/M** `tdora-physoc-011` — Reconcile the location-criticality model with the entity's DORA register of critical or important functions; add an override that any location hosting a critical function automatically requires Pentest-grade testing.

## Red team lead + Procurement + Legal/Compliance
_1 items_

- **medium/M** `tdora-bhe-003` — Reference the ICT third-party register entry for the BHE SaaS in this document (or in a linked Tooling Inventory), and ensure data-residency, exit-clause and sub-outsourcing items are tracked there. Verify the precise DORA articles cited against the live text.

## Red team lead + Purple team / Detection Engineering
_1 items_

- **high/S** `lifecycle-bhe-007` — Add a 'Purple-team Handover' subsection requiring a debrief with SOC/Detection Engineering after each BHE remediation cycle: review prioritised attack paths, verify detection coverage for SharpHound collection and the abused edges, and log detection gaps into the backlog.

## Red team lead + SOC lead + Legal/Risk
_1 items_

- **high/M** `lifecycle-bhe-002` — Reference (or include) an authorization template covering: which domains and OUs are in scope for SharpHound enumeration, the named approver, the formal SOC suppression/allowlisting agreement (not 'disregard alerts'), kill-switch / pause procedure, and reauthorization cadence.

## Red team lead + SOC manager
_1 items_

- **medium/M** `coherence-soc-rt-comms-diag-012` — Add an 'External actors and SOC interface' subsection (in the methodology and/or each SOP's Deconfliction section) describing the SOC structure (CSIRT, L1-L3, Pentest-Assessment) and the RT touchpoints during engagements and live IR support.

## Red team lead + TI lead
_1 items_

- **critical/L** `tdora-physoc-002` — Add a TLPT-mode addendum that maps each Physical Pentest stage to the TIBER-EU phases: TTI-derived pretexts and objectives, control-team-supervised execution, replay-and-attestation closure. Keep the internal Maturity flow as the non-TLPT path.

## Red team lead + Threat hunt
_1 items_

- **high/S** `lifecycle-research-007` — Add a 'Threat-hunt hypothesis output' artefact to Deep Dive and Capability Development; require it to be shared with the threat-hunt function on a defined cadence.

## Red team lead + Threat intelligence lead
_1 items_

- **high/M** `coherence-exercises-011` — Add a Threat Intelligence Team subsection to Operations_Process and ThreatScenarios_Process Teams & Responsibilities; align RACI to the Exercises SOP. Update the methodology to name the TI Team where it currently uses implicit references.

## Red team lead + White team lead
_1 items_

- **medium/S** `lifecycle-exercises-016` — Update Leg-Ups section to require: (1) entry in an engagement leg-up log, (2) WT countersignature, (3) explicit tagging of any downstream finding as 'leg-up assisted' in the Closure report.

## Red team lead / Legal & Privacy
_1 items_

- **medium/S** `lifecycle-rtmeth-012` — Replace 'PIA' with the relevant EU legal basis (GDPR Art.6/9, applicable national law) and add explicit personal-data and confidential-data categories. Define the White Team / Control Team in a dedicated section so the 'WT Point of Contact' reference is anchored.

## Red team lead / Legal / HR
_1 items_

- **critical/M** `lifecycle-physoc-005` — Add a 'Operator safety and check-ins' subsection to Planning specifying: control-point contact, mandatory check-in cadence, missed-check-in escalation, abort trigger words, in-country emergency contacts (medical / legal), permitted hours and clothing/identification.

## Red team lead / Legal-Risk
_1 items_

- **critical/M** `lifecycle-operations-007` — Add an explicit Authorization section before Research & Preparation listing: the engagement letter / RoE owner, required signatories (legal, risk, business owner), safe-word convention, kill-switch authority, abort criteria, and a pre-flight checklist that must be signed before any RT activity.

## Red team lead / Threat hunt
_1 items_

- **high/M** `lifecycle-operations-004` — Add a Threat-Hunt Handover step in Closure: a structured artefact (per-TTP hunt hypothesis, data sources, expected telemetry, time horizon) that is delivered to the hunt team and tracked to closure.

## Red team lead / Threat intel
_1 items_

- **medium/S** `tdora-operations-003` — Add a paragraph clarifying that Operations rely on opportunistic / internal CTI inputs and that any engagement intended to satisfy TLPT must additionally procure an independent TI provider producing a TTI report. Verify the TI-provider independence clause against the live RTS on TLPT.

## Red team lead with Legal/Risk
_1 items_

- **critical/M** `lifecycle-threatscenarios-002` — Add a 'Rules of Engagement / Authorization' section to the Planning phase. As a minimum: named approver(s) per scope (system owner + Head of Red Team / CISO), explicit Legal sign-off where personal or production data is in scope, kill-switch and abort criteria, safe-word, and the contacts on call to invoke them.

## Red team lead with Purple team
_1 items_

- **medium/M** `lifecycle-threatscenarios-012` — Reframe Execution to make the demonstrative nature explicit: keep Recon/Exploit/Escalation but add 'demonstration walk-through points' where the operator pauses to show the blue team the artefacts (logs, telemetry, alerts) that did or did not fire. Make clear this is not a stealth kill-chain.

## Red team lead with Purple team / SOC
_1 items_

- **critical/M** `lifecycle-threatscenarios-001` — Add an explicit 'Purple-team close-out' phase between Execution and Report. Specify required attendees (red team operators, SOC/blue team representative, target system owner), the agenda (per-scenario walk-through, detections observed vs missed, control recommendations) and the output (jointly-signed action list feeding the Report).

## Red team lead with SOC/Blue team
_1 items_

- **high/S** `lifecycle-threatscenarios-003` — Restructure Planning so that, after the red team's internal brainstorm, a mandatory joint planning workshop is held with the SOC / blue team and the system owner to agree scenarios, success criteria and the demonstration format. Document attendees and outputs.

## Red team lead with system owner
_1 items_

- **high/M** `lifecycle-threatscenarios-010` — Add a 'Safety controls' subsection in Execution listing: dedicated test accounts/projects where possible, agreed execution windows, the change-management coordination point, a rollback plan and a named on-call contact authorised to pause/abort.

## Red team lead, Purple team
_1 items_

- **critical/S** `lifecycle-rtdeck-003` — Add a Close-out phase slide making purple-teaming mandatory across Exercises, Operations and Threat Scenarios, and describe its inputs (red findings, telemetry gaps) and outputs (detection improvements, hunt hypotheses).

## Red team lead, Threat intel
_1 items_

- **medium/S** `tdora-rtdeck-003` — Add a note that internally-sourced TTI is acceptable for internal Exercises / Operations / Threat Scenarios but that TLPT runs require an independent TI provider; verify wording against the live RTS on TLPT.

## Red team lead, White team
_1 items_

- **medium/S** `lifecycle-rtdeck-010` — Add an approval-and-log requirement to the leg-up slide and require that each leg-up appear in the final report so coverage and detection findings remain defensible.

## Risk & Compliance / Red team lead
_1 items_

- **medium/S** `tdora-rtmeth-010` — Add a short jurisdictional clause stating that for any engagement positioned as TIBER-EU / TLPT, the applicable NCA and the corresponding TIBER-XX implementation must be identified per engagement, with the lead overseer recorded in the engagement letter.

## Threat intel + Red team lead
_1 items_

- **high/M** `tdora-physoc-004` — Add a step that, when running under TLPT, the physical scenarios and pretexts are derived from a TTI report from an independent TI provider and mapped to MITRE ATT&CK techniques.

## Threat intel / Red team lead
_1 items_

- **high/L** `tdora-rtmeth-003` — Add a Threat Intelligence phase that requires a Targeted Threat Intelligence report, names the provider/function (with independence criteria), and shows how TTI drives scenario selection. Replace or supplement the legacy threat profiles with Euronext-specific, FMI-sector-relevant TTPs.

## Threat intel lead
_1 items_

- **medium/M** `tdora-exercises-011` — Define a 'Targeted Threat Intelligence Report' deliverable in the TI phase, with template (threat actors, TTPs, attack hypotheses, scenario seeds, ATT&CK mapping), a named approver, and version control.

## Threat intel lead + Red team lead
_1 items_

- **medium/S** `lifecycle-exercises-009` — Add a paragraph in Targeted TI stating who can perform the TI (internal TI function, external provider) and confirming separation from the RT executors when feasible. Note that TLPT framing requires an independent TI provider.

## Threat intel lead + Red team lead + Compliance
_1 items_

- **high/M** `tdora-exercises-003` — State explicitly that for TLPT-framed Exercises the TI provider must be independent of the RT provider, with a named Targeted Threat Intelligence Report deliverable. For internal Exercises, document that internal TI is acceptable but separation of responsibilities is recommended.
