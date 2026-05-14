# Remediation backlog (run 2026-05-11-2202)

**216 deduped findings** grouped by recommended owner, sorted by severity x effort (S before L).

Severity ranking: critical > high > medium > low > informational. Effort ranking: S > M > L. Quick critical wins first.

## Red team lead with Purple team / SOC (1 items)

- **[CRITICAL / M]** `lifecycle-threatscenarios-001` (ThreatScenarios v1.1) — Add an explicit 'Purple-team close-out' phase between Execution and Report. Specify required attendees (red team operators, SOC/blue team representative, target system owner), the agenda (per-scenario walk-through, detections observed vs missed, control recommendations) and the output (jointly-signed action list feeding the Report).

## Red team lead with Legal/Risk (1 items)

- **[CRITICAL / M]** `lifecycle-threatscenarios-002` (ThreatScenarios v1.1) — Add a 'Rules of Engagement / Authorization' section to the Planning phase. As a minimum: named approver(s) per scope (system owner + Head of Red Team / CISO), explicit Legal sign-off where personal or production data is in scope, kill-switch and abort criteria, safe-word, and the contacts on call to invoke them.

## Red team lead / Purple team (3 items)

- **[CRITICAL / M]** `lifecycle-operations-003` (Operations v1.0) — Add an explicit 'Purple-team close-out' subsection under Closure: a mandatory live workshop with the BT to replay the scenario, map BT detections (or absence) against each TTP, and capture defensive improvements. Make the workshop a gating step before the Operation can be marked complete.
- **[HIGH / S]** `lifecycle-rtmeth-004` (RT-Methodology v0.3) — Replace 'can happen' with explicit mandate: 'A purple-team close-out is required at the end of every Exercise, Operation and Threat Scenario. The Purple Teaming Process document defines the replay format, attendee list, alert/log correlation matrix, and improvement backlog.'
- **[HIGH / M]** `tdora-rtmeth-006` (RT-Methodology v0.3) — Add a 'Closure' subsection that lists mandatory closure artefacts (replay record, 360° feedback notes, remediation plan, attestation, knowledge-sharing pack) and identifies which apply only to TLPT-framed Exercises versus all engagements.

## Red team lead / Legal-Risk (1 items)

- **[CRITICAL / M]** `lifecycle-operations-007` (Operations v1.0) — Add an explicit Authorization section before Research & Preparation listing: the engagement letter / RoE owner, required signatories (legal, risk, business owner), safe-word convention, kill-switch authority, abort criteria, and a pre-flight checklist that must be signed before any RT activity.

## Red team lead + Blue team lead (1 items)

- **[CRITICAL / M]** `lifecycle-exercises-001` (Exercises v1.1) — Add a mandatory 'Purple-team replay' step in Closure: a working session with the BT walking the kill chain step-by-step, mapping each TTP to detections/preventions in place, and agreeing concrete defensive improvements. Capture as a deliverable (report annex or separate replay note).

## Red team lead + Legal/Risk (7 items)

- **[CRITICAL / M]** `lifecycle-exercises-005` (Exercises v1.1) — Add an 'Authorization & Kill-switch' subsection: (1) named legal/risk sign-off prerequisite, (2) explicit abort criteria, (3) safe-word + 24/7 contact channel between RT lead and WT lead, (4) what 'stop' means operationally.
- **[HIGH / M]** `lifecycle-exercises-008` (Exercises v1.1) — Restructure Initiation around named deliverables: scoping document + engagement letter + signed RoE. Make 'all three signed' a hard gate before Targeted TI commences.
- **[MEDIUM / S]** `lifecycle-bhe-011` (BloodhoundEnterprise v0.1) — Specify the format and storage of the user written permission (e.g. ticket with manager approval), require IAM counter-signature for service or privileged accounts, and reference the engagement file where the artefact is stored.
- **[MEDIUM / M]** `lifecycle-research-004` (Research-Methodology v0.2) — Add an 'AI Enrichment governance' paragraph covering approved model/tenant, data-classification rules for inputs, prompt and version control, and how AI outputs are logged for audit.
- **[MEDIUM / M]** `tdora-research-004` (Research-Methodology v0.2) — Add a paragraph that escalates a reproduction to TLPT test-risk-management controls when the environment touched is shared with critical or important functions; require control-team authorisation and reference DORA Art.26 safety controls.
- **[LOW / S]** `lifecycle-research-011` (Research-Methodology v0.2) — Document classification, retention, and audited access patterns for the Research Repository and the REDS Jira project; cross-reference internal data-classification policy.
- **[INFORMATIONAL / S]** `tdora-physoc-010` (PhysicalSocial v1.0) — Add a per-jurisdiction reference list and review it on each cycle so authorization, attestation and competent-authority notifications use the current national TIBER-XX or DORA RTS text.

## Red team lead / Legal & Risk (2 items)

- **[CRITICAL / M]** `lifecycle-rtmeth-003` (RT-Methodology v0.3) — Add a dedicated 'Authorization & Rules of Engagement' section that points to a mandatory RoE template covering: approving authority, legal/risk sign-off, safe-words, kill-switch, abort criteria, blue-team notification rules per engagement type, and indemnities. Make sign-off a hard pre-execution gate.
- **[HIGH / M]** `tdora-rtmeth-007` (RT-Methodology v0.3) — Add a 'Test risk management' subsection: kill-switch ownership, abort criteria, rollback expectations for persistence/registry artefacts, safe-harbour / indemnity language for testers. Reference the RoE template.

## Red team lead / Risk & Compliance (4 items)

- **[CRITICAL / M]** `tdora-rtmeth-004` (RT-Methodology v0.3) — Add a 'TLPT actors' section defining White Team, Control Team, TI provider, RT provider, and the institution's interactions with the TCT / lead overseer for engagements positioned as TIBER-EU. Make 'WT Point of Contact' a downstream reference, not the only mention of the role.
- **[CRITICAL / L]** `tdora-rtmeth-002` (RT-Methodology v0.3) — Add a Preparation section to the methodology covering: GTL consumption, engagement letter template, critical/important-functions identification, and procurement criteria for independent TI and RT providers (or internal-tester arrangements). Verify each item against the live TIBER-EU v2 text and the DORA RTS on TLPT.
- **[HIGH / M]** `tdora-rtmeth-001` (RT-Methodology v0.3) — Replace 'TIBER-Like' with one of two precise positions: (a) Exercises are run as TIBER-EU / DORA TLPT and follow the prescribed phases, actors, and artefacts (cross-reference per-NCA TIBER-XX guidance); or (b) Exercises are inspired by TIBER-EU but do not satisfy DORA Art.26 / TLPT — and remove any implication that they do. Verify against the live TIBER-EU v2 framework text and the relevant national TIBER-XX implementation.
- **[HIGH / M]** `tdora-rtmeth-005` (RT-Methodology v0.3) — Add a 'Tester model' subsection that states whether Exercises are run internally, externally, or hybrid, and document how Art.27 qualification, independence and rotation requirements are met. Verify against DORA Art.27 and the RTS on TLPT.

## Red team lead, Purple team (1 items)

- **[CRITICAL / S]** `lifecycle-rtdeck-003` (RT-Deck v1.0) — Add a Close-out phase slide making purple-teaming mandatory across Exercises, Operations and Threat Scenarios, and describe its inputs (red findings, telemetry gaps) and outputs (detection improvements, hunt hypotheses).

## Purple team / Red team lead (1 items)

- **[CRITICAL / M]** `lifecycle-physoc-003` (PhysicalSocial v1.0) — Add a 'Purple-team close-out' section after Report that mandates a joint replay with blue team, SOC and physical security covering timeline, IoCs/physical indicators, detection gaps and agreed control improvements.

## Red team lead / Legal / HR (1 items)

- **[CRITICAL / M]** `lifecycle-physoc-005` (PhysicalSocial v1.0) — Add a 'Operator safety and check-ins' subsection to Planning specifying: control-point contact, mandatory check-in cadence, missed-check-in escalation, abort trigger words, in-country emergency contacts (medical / legal), permitted hours and clothing/identification.

## Red team lead + TI lead (1 items)

- **[CRITICAL / L]** `tdora-physoc-002` (PhysicalSocial v1.0) — Add a TLPT-mode addendum that maps each Physical Pentest stage to the TIBER-EU phases: TTI-derived pretexts and objectives, control-team-supervised execution, replay-and-attestation closure. Keep the internal Maturity flow as the non-TLPT path.

## Red team lead with SOC/Blue team (1 items)

- **[HIGH / S]** `lifecycle-threatscenarios-003` (ThreatScenarios v1.1) — Restructure Planning so that, after the red team's internal brainstorm, a mandatory joint planning workshop is held with the SOC / blue team and the system owner to agree scenarios, success criteria and the demonstration format. Document attendees and outputs.

## Red team lead with Threat hunt (1 items)

- **[HIGH / M]** `lifecycle-threatscenarios-004` (ThreatScenarios v1.1) — Add a 'Threat-hunt handover' subsection (after Purple-team close-out) describing how scenario outcomes translate into hunt hypotheses, what data sources are required, who owns each hunt, and how completed hunts feed back into the engagement record.

## Red team lead with system owner (3 items)

- **[HIGH / M]** `lifecycle-threatscenarios-005` (ThreatScenarios v1.1) — Add a 'Remediation tracking' section: each reported vulnerability or scenario outcome gets logged in the issue/ticket tracker with owner, severity, due date and retest criteria; the red team holds a recurring review of open items.
- **[HIGH / M]** `lifecycle-threatscenarios-010` (ThreatScenarios v1.1) — Add a 'Safety controls' subsection in Execution listing: dedicated test accounts/projects where possible, agreed execution windows, the change-management coordination point, a rollback plan and a named on-call contact authorised to pause/abort.
- **[MEDIUM / M]** `tdora-threatscenarios-004` (ThreatScenarios v1.1) — Define a small Control role per Threat Scenario: a named institution-side owner (typically the system owner plus the Head of Red Team or delegate) responsible for the test mandate, escalation, communication and abort decision. Make clear this is internal and not the TIBER-EU Control Team in the regulatory sense.

## Red team lead (93 items)

- **[HIGH / S]** `lifecycle-exercises-003` (Exercises v1.1) — Update the CODENAME section to require codenames drawn from known fictional characters (movies, TV, books), and to be logged in the engagement register. Provide one or two illustrative examples.
- **[HIGH / S]** `lifecycle-operations-002` (Operations v1.0) — Update the CODENAME section to state that Operation codenames must be drawn from known fictional characters (movies / TV / books), with examples and a register of used names to avoid collisions.
- **[HIGH / S]** `lifecycle-operations-008` (Operations v1.0) — Add a Scope subsection that explicitly addresses cyber + physical: state default in/out of scope, link to the Physical/Social process and questionnaire, and require the RoE to record physical scope per engagement.
- **[HIGH / S]** `lifecycle-physoc-002` (PhysicalSocial v1.0) — Add a 'Codename' subsection to Planning requiring assignment of a unique codename per the team's theme convention and recording it on the Get-out-of-jail letter and the engagement register.
- **[HIGH / S]** `lifecycle-physocq-002` (PhysicalSocial-Questionnaire v1.0) — Add an 'Ownership and Custody' section naming the questionnaire owner, the office-side respondent role, the central reviewer, the storage repository (with access controls), and the response SLA.
- **[HIGH / S]** `lifecycle-rtdeck-002` (RT-Deck v1.0) — Add a slide describing the codename convention (fictional-character theme for Exercises/Operations, codename-required-but-theme-flexible for Threat Scenarios) and link it to the corresponding sections of the per-type process docs.
- **[HIGH / S]** `lifecycle-rtdeck-004` (RT-Deck v1.0) — Add a slide enumerating the three adjacent activities (close-out hunt, external-RT hunt support, live-IR support) so leadership and auditors see the full team remit rather than only offensive operations.
- **[HIGH / S]** `lifecycle-rtdeck-005` (RT-Deck v1.0) — Add a slide on cyber + physical scope, referencing the existing PhysicalSocial process docs so the deck does not give the impression the team is cyber-only.
- **[HIGH / S]** `lifecycle-rtdeck-006` (RT-Deck v1.0) — Re-word Slide 11 so blue-team awareness rules are conditional on engagement type, and add a clarifying line that Threat Scenarios are explicitly collaborative.
- **[HIGH / S]** `lifecycle-rtmeth-002` (RT-Methodology v0.3) — Add a 'Codename Assignment' section to the methodology stating: every engagement (Exercise/Operation/Threat Scenario) is assigned a codename before authorization; Exercises and Operations follow the fictional-character theme; Threat Scenarios follow the team's alternative convention. Reference the codename register.
- **[HIGH / S]** `lifecycle-rtmeth-007` (RT-Methodology v0.3) — Add a 'Physical scope' subsection that confirms physical assessments are in scope, identifies the additional sign-offs required (site/facility owner, Legal), and references the PhysicalSocial Process document and questionnaire.
- **[HIGH / S]** `lifecycle-threatscenarios-006` (ThreatScenarios v1.1) — Add a 'Lessons learned' step at the end of every Threat Scenario: a short retrospective populated by the red team (and ideally co-signed by blue), captured in a named register/wiki page, used as input to the next Planning brainstorm.
- **[HIGH / S]** `lifecycle-threatscenarios-007` (ThreatScenarios v1.1) — In the Scope subsection, add a one-line statement on physical scope: by default out-of-scope for tool-focused Threat Scenarios, but explicitly in-scope when the scenario subject is a physical control (e.g. badge system, datacentre access, visitor flow).
- **[HIGH / S]** `tdora-rtdeck-004` (RT-Deck v1.0) — Add a mapping slide showing internal Phase 0–4 alongside the four TIBER-EU phases; even if the team does not run TLPT routinely, this gives auditors a shared vocabulary.
- **[HIGH / M]** `lifecycle-operations-001` (Operations v1.0) — Add an explicit 'Assumed-Breach Setup' phase before Initial Foothold (or replace Initial Foothold) that describes how the WT provisions the foothold, how scenarios are defined up front, and how scenario-driven execution differs from full kill-chain emulation.
- **[HIGH / M]** `lifecycle-physoc-001` (PhysicalSocial v1.0) — Add a 'Relationship to engagement types' section that maps Physical Pentest / Audit / Questionnaire to Exercise, Operation and Threat Scenario, clarifies the stealth posture in each, and removes or relabels the 'Figure 1 - Threat Scenarios Phases' caption so it does not imply a Threat Scenario when the section describes a stealthy Pentest.
- **[HIGH / M]** `lifecycle-physoc-014` (PhysicalSocial v1.0) — Add explicit remediation tracking (register, owner, due date, verification) and a lessons-learned capture step to the Report phase.
- **[HIGH / M]** `lifecycle-research-002` (Research-Methodology v0.2) — Add a 'Lab & Authorization' subsection requiring techniques be first reproduced in a named isolated lab, with documented authorization (and a stricter gate for any reproduction that needs prod-like or production data).
- **[HIGH / M]** `lifecycle-research-005` (Research-Methodology v0.2) — Define promotion criteria from Experimental -> Operational and require a 'tradecraft release note' that updates Exercise / Operation / Threat-Scenario playbooks and the ATT&CK technique map when a new capability lands.
- **[HIGH / M]** `lifecycle-rtdeck-001` (RT-Deck v1.0) — Add a dedicated section near the front of the deck describing Exercises, Operations and Threat Scenarios side by side (shape, stealth posture, blue-team awareness, typical regulator overlap) so internal audiences cannot confuse one for another.
- **[HIGH / M]** `lifecycle-rtdeck-011` (RT-Deck v1.0) — Add prose captions to each chart/SmartArt slide that summarise the diagram in two or three sentences so the deck conveys methodology even when the visual is illegible or stripped during conversion to other formats.
- **[HIGH / M]** `lifecycle-rtmeth-006` (RT-Methodology v0.3) — Add a 'Adjacent responsibilities' section covering: (i) post-engagement threat hunt at close-out; (ii) hunt and attacker-perspective support during external red-team-against-Euronext; (iii) red-team support to IR during live incidents. Define triggers, owners, and deliverables for each.
- **[HIGH / M]** `lifecycle-rtmeth-008` (RT-Methodology v0.3) — Add a 'Reporting' section defining mandatory report structure (exec summary, attack narrative, ATT&CK mapping, findings with severity), severity rubric, evidence retention requirements, and review/QA gate before issue.
- **[HIGH / M]** `lifecycle-rtmeth-014` (RT-Methodology v0.3) — Rewrite the Scoping section to describe how scope is determined and recorded: identification of critical/important functions, in-scope and explicitly out-of-scope assets, identities and networks, time windows, blue-team-awareness rule per engagement type, and scoping document template. The current 'capability checklist' content should be moved to a separate 'Engagement feasibility' subsection.
- **[HIGH / M]** `tdora-physoc-001` (PhysicalSocial v1.0) — Add a 'TIBER-EU / DORA TLPT alignment' section that (a) confirms physical and social vectors are eligible legs of a TLPT, (b) specifies that when run under TLPT the TI-derived scenarios drive the physical pretexts and objectives, and (c) routes the physical leg through the same control-team / white-team and attestation pathway as the cyber leg. Verify the exact framework text before publication.
- **[MEDIUM / S]** `lifecycle-bhe-010` (BloodhoundEnterprise v0.1) — Require peer-reviewed cleanup verification: a second team member checks the OPLOG against environment state and signs off; record the sign-off in the engagement file.
- **[MEDIUM / S]** `lifecycle-bhe-017` (BloodhoundEnterprise v0.1) — Replace the generic 'reduce alerts and evade detections' wording with engagement-type-aware guidance: stealth in scope for Exercises/Operations, demonstration-mode for Threat Scenarios; reference the relevant engagement process.
- **[MEDIUM / S]** `lifecycle-exercises-007` (Exercises v1.1) — Add a Closure step 'Lessons learned': structured retro covering RT, WT and (where appropriate) BT input, captured in the team knowledge base using a fixed template; include explicit follow-up actions and owners.
- **[MEDIUM / S]** `lifecycle-exercises-012` (Exercises v1.1) — Either re-ingest the document with diagram extraction enabled, or add prose descriptions / captions next to each figure reference (Phase ownership matrix, timeline, deconfliction flow, kill chain). Critical for the diagram-consistency evaluator to be meaningful.
- **[MEDIUM / S]** `lifecycle-operations-006` (Operations v1.0) — Define a single durable lessons-learned artefact (e.g. team wiki register or Confluence page) and a short retro template that the RT lead must complete after every Operation.
- **[MEDIUM / S]** `lifecycle-physoc-011` (PhysicalSocial v1.0) — Define a tester-identity kit (visible ID, cover story, safe-word for phone verification) and require it as part of the Planning checklist.
- **[MEDIUM / S]** `lifecycle-physoc-013` (PhysicalSocial v1.0) — Add a 'Notification matrix' to Planning specifying for each assessment type who is in the know (white team) and who is blind (blue team / SOC), and when and how disclosure happens after the test.
- **[MEDIUM / S]** `lifecycle-physoc-015` (PhysicalSocial v1.0) — Add a hardware-implant inventory, chain-of-custody log, and explicit 'recovery and decommissioning' close-out step.
- **[MEDIUM / S]** `lifecycle-physoc-016` (PhysicalSocial v1.0) — Add an 'Adjacent responsibilities' subsection covering IR support and assistance to externally-run red team exercises that include physical or social vectors.
- **[MEDIUM / S]** `lifecycle-physocq-001` (PhysicalSocial-Questionnaire v1.0) — Rewrite the Introduction to state that this is a periodic Physical Security Questionnaire issued to Euronext office locations (per CMDB criticality), referencing the parent PhysicalSocial process for the engagement-led testing flow.
- **[MEDIUM / S]** `lifecycle-physocq-004` (PhysicalSocial-Questionnaire v1.0) — Re-render the three formulas as in-line text (Vulnerability Score, Controls Coverage, Maturity), add the frequency lookup table, and include one worked example. Verify the Word source so the equations survive ingestion.
- **[MEDIUM / S]** `lifecycle-physocq-005` (PhysicalSocial-Questionnaire v1.0) — Add a Maturity-to-Periodicity table (e.g. Maturity ≥0.9 → 36 months, 0.7-0.9 → 24, 0.5-0.7 → 12, <0.5 → 6) and codify the override rule for sites with open critical findings.
- **[MEDIUM / S]** `lifecycle-physocq-008` (PhysicalSocial-Questionnaire v1.0) — Add a cross-reference to PhysicalSocial_Process_v1.0 explaining how questionnaire results feed engagement scoping (target site selection, blast-radius judgement, prerequisites for a physical leg).
- **[MEDIUM / S]** `lifecycle-research-009` (Research-Methodology v0.2) — Add an explicit line clarifying scope of physical / social-engineering tradecraft research; align with the physical-social process docs.
- **[MEDIUM / S]** `lifecycle-research-010` (Research-Methodology v0.2) — Add tool ownership, review cadence, and explicit transition criteria between Experimental / Operational / Deprecated / Retired states.
- **[MEDIUM / S]** `lifecycle-research-015` (Research-Methodology v0.2) — Introduce a small handling tier on OPSEC / detection notes (e.g. RT-only, share-with-purple, releasable) so capability documentation is shared safely.
- **[MEDIUM / S]** `lifecycle-rtdeck-009` (RT-Deck v1.0) — Replace named individuals with the team role ('Offensive Engineering & Research / Red Team'); list named operators only in per-engagement authorisation documents that are versioned and access-controlled.
- **[MEDIUM / S]** `lifecycle-rtdeck-012` (RT-Deck v1.0) — Add a one-line label per phase on Slides 12–14 and a master 'Phases at a glance' slide that maps the internal phase numbers to PTES and to TIBER-EU phases.
- **[MEDIUM / S]** `lifecycle-rtdeck-013` (RT-Deck v1.0) — Add a Reporting slide naming the severity model, evidence-retention rules and report consumers; cross-reference any report template used by the team.
- **[MEDIUM / S]** `lifecycle-rtdeck-016` (RT-Deck v1.0) — Add a slide naming the remediation tracker and the lessons-learned capture point; link to per-type process docs for the specifics.
- **[MEDIUM / S]** `lifecycle-rtmeth-001` (RT-Methodology v0.3) — Rewrite the introduction to list the three engagement types and describe Purple Teaming separately as a mandatory close-out across all three. Align with the team's published engagement taxonomy.
- **[MEDIUM / S]** `lifecycle-rtmeth-016` (RT-Methodology v0.3) — Update the Threat Scenario paragraph to describe the assumed-breach, demonstrative, joint-planning structure and call out the typical internal-tool targets (GitLab, Jenkins, CI/CD, internal SaaS, secret stores, ticketing). State explicitly that stealth is not in scope.
- **[MEDIUM / S]** `lifecycle-rtmeth-017` (RT-Methodology v0.3) — Rewrite the Operations paragraph: 'Operations are assumed-breach, scenario-scoped engagements with formal authorization, codename, and a small set of pre-defined objectives. They are typically used to test specific hypotheses or prove risks, and follow the Operations Process document.' Drop the 'outside the context of a formalized engagement' wording.
- **[MEDIUM / S]** `lifecycle-threatscenarios-008` (ThreatScenarios v1.1) — Move 'CODENAME' to be the first subsection of Planning and add a sentence on where the codename register lives (which document, who has access).
- **[MEDIUM / S]** `lifecycle-threatscenarios-013` (ThreatScenarios v1.1) — Reference the team's reporting template explicitly and document the severity scale used. Specify the minimum evidence required per finding (screenshot, OPLOG line(s), artefact path).
- **[MEDIUM / S]** `lifecycle-threatscenarios-014` (ThreatScenarios v1.1) — Promote clean-up to its own gated step at the end of Execution, with a checklist (accounts, files, persistence, scheduled jobs, config changes) and an explicit sign-off recorded in the engagement record.
- **[MEDIUM / S]** `tdora-exercises-012` (Exercises v1.1) — Add a paragraph in RT Test mapping Unified Kill Chain phases to TIBER-EU 'legs / flags / objectives'. Require ATT&CK technique IDs at each step. Provide a sample mapping table.
- **[MEDIUM / S]** `tdora-research-002` (Research-Methodology v0.2) — Require engagement deliverables (RTT report, closure report, attestation pack) to cite the Research Repository and Tool Repository IDs of the techniques and capabilities used, so research provenance is auditable for TLPT.
- **[MEDIUM / M]** `lifecycle-exercises-010` (Exercises v1.1) — Add an 'OPSEC and detection capture' note to the RT Test phase: stealth is in scope; the RT records every BT detection event (or absence thereof) per TTP; produce time-to-detect / time-to-contain metrics as a Closure deliverable.
- **[MEDIUM / M]** `lifecycle-exercises-015` (Exercises v1.1) — Define the reporting taxonomy: severity rubric, mandatory evidence fields, ATT&CK technique ID per finding, and scenario-to-finding linkage. Provide a report template.
- **[MEDIUM / M]** `lifecycle-operations-010` (Operations v1.0) — Introduce a named Scoping step with a scoping document template (in-scope, out-of-scope, objectives, success criteria, constraints, third-party dependencies) and require WT sign-off before the RT Test begins. Replace 'anything is in scope' with explicit boundaries.
- **[MEDIUM / M]** `lifecycle-physoc-018` (PhysicalSocial v1.0) — Document the physical-to-cyber and cyber-to-physical handover including authorization re-confirmation, network segmentation/kill-switch and termination criteria.
- **[MEDIUM / M]** `lifecycle-rtmeth-011` (RT-Methodology v0.3) — Expand the Forbidden Attacks section into a 'Safety & blast-radius controls' section: lab-first testing requirement (already present), explicit rollback/cleanup expectations for persistence and registry artefacts, change-window communication with WT, and pre-action notification triggers for high-impact actions.
- **[MEDIUM / M]** `lifecycle-rtmeth-020` (RT-Methodology v0.3) — Add a 'Roles & responsibilities' section defining: engagement lead, operators, threat intel, White Team, Control Team (where applicable), and their handoff responsibilities at each lifecycle phase.
- **[MEDIUM / M]** `lifecycle-threatscenarios-011` (ThreatScenarios v1.1) — Mandate a single OPLOG storage location (or a small approved set), specify access controls, retention period and a standard export schema (CSV/JSON) so logs are usable by IR. Personal note-taking apps remain acceptable as scratch but the canonical OPLOG must live in the approved location.
- **[MEDIUM / M]** `tdora-operations-004` (Operations v1.0) — Restructure Closure to deliver: (1) test summary report, (2) replay workshop with BT, (3) remediation plan owned by control owners, (4) internal attestation/sign-off that the Operation completed within RoE, (5) knowledge-sharing artefact (lessons-learned register entry). Verify which DORA articles cover non-TLPT testing evidence.
- **[LOW / S]** `lifecycle-bhe-005` (BloodhoundEnterprise v0.1) — Expand AET on first use and link to the team charter / RACI; add a glossary if more in-house acronyms are introduced.
- **[LOW / S]** `lifecycle-bhe-013` (BloodhoundEnterprise v0.1) — Add a single 'Scope' line: 'Cyber/identity only; physical scope is not applicable to this methodology.'
- **[LOW / S]** `lifecycle-bhe-014` (BloodhoundEnterprise v0.1) — Add a quarterly trend-review step: extract recurring BHE finding patterns into the team knowledge base and feed them into AD hardening guidance and detection backlog.
- **[LOW / S]** `lifecycle-bhe-015` (BloodhoundEnterprise v0.1) — Promote the document out of Draft, add owner / approver / next-review-date in a control block, and schedule an annual review.
- **[LOW / S]** `lifecycle-exercises-014` (Exercises v1.1) — Search/replace 'operation' with 'exercise' everywhere except where a deliberate cross-reference is intended; align with the Exercise / Operation / Threat Scenario taxonomy.
- **[LOW / S]** `lifecycle-exercises-018` (Exercises v1.1) — Add document-control front-matter: owner, approver, review cadence, classification, applicability scope. Move the Versioning table into the front-matter.
- **[LOW / S]** `lifecycle-operations-011` (Operations v1.0) — Either map the three named subphases to the Unified Kill Chain stages explicitly (table) or pick one model (UKC vs 3-stage) and use it consistently. Map each subphase to the corresponding ATT&CK tactics for OPLOG tagging.
- **[LOW / S]** `lifecycle-operations-012` (Operations v1.0) — Mandate a central OPLOG repository with access control and audit trail; permit individual note-taking only as a working copy that is mirrored daily into the central store.
- **[LOW / S]** `lifecycle-physoc-017` (PhysicalSocial v1.0) — Render the formulae (LaTeX or image with alt-text) inline and provide a worked example so the Maturity calculation is reproducible.
- **[LOW / S]** `lifecycle-physocq-011` (PhysicalSocial-Questionnaire v1.0) — Re-export the document with figures embedded, or maintain an Annex (PDF) with worked examples; verify ingestion captures them.
- **[LOW / S]** `lifecycle-physocq-012` (PhysicalSocial-Questionnaire v1.0) — Spell-check pass; fix 'wether' to 'whether' and review for similar typos.
- **[LOW / S]** `lifecycle-research-012` (Research-Methodology v0.2) — Explicitly designate the Research Repository (or a sibling wiki) as the lessons-learned register, with an owner and a cadence for review.
- **[LOW / S]** `lifecycle-rtdeck-008` (RT-Deck v1.0) — Correct the typo and, while there, name the severity / scoring framework actually used (e.g. CVSS, internal severity model) so 'framework to assess results' is concrete rather than aspirational.
- **[LOW / S]** `lifecycle-rtdeck-014` (RT-Deck v1.0) — Confirm whether Slides 25–27 are intentionally blank; if so add titles, if not investigate ingest fidelity.
- **[LOW / S]** `lifecycle-rtmeth-015` (RT-Methodology v0.3) — Define a central OPLOG location (shared, access-controlled), a minimum retention period, chain-of-custody / read-only export expectations, and a rule that personal OneNotes are working copies that must be transferred to the central log at engagement close.
- **[LOW / S]** `lifecycle-rtmeth-018` (RT-Methodology v0.3) — Promote the methodology to v1.0 once the gaps in this review are closed, add an approval/signoff line and an explicit review cadence (e.g. annual), and name a document owner.
- **[LOW / S]** `lifecycle-rtmeth-019` (RT-Methodology v0.3) — Replace the embedded matrix with either a properly captioned figure that survives DOCX export, or a small text table that places Threat Scenario / Operation / Exercise along the stealth and adversary-emulation axes explicitly.
- **[LOW / S]** `lifecycle-threatscenarios-009` (ThreatScenarios v1.1) — Document the Threat-Scenario codename convention explicitly (theme or 'no theme', allowed character set, register location). Cross-reference the Exercises and Operations conventions so the difference is intentional, not accidental.
- **[LOW / S]** `lifecycle-threatscenarios-016` (ThreatScenarios v1.1) — Add a short paragraph to Scenarios Description on approved LLM use: which tools are approved, what may not be shared (codenames, real internal tool names, credentials), and that LLM output must be peer-reviewed before adoption.
- **[LOW / S]** `tdora-physoc-012` (PhysicalSocial v1.0) — When publishing the TLPT addendum, adopt TIBER-EU role names and provide a mapping from the existing 'Local CISO / Local Facilities Manager' wording to White Team / Control Team membership.
- **[LOW / S]** `tdora-rtmeth-012` (RT-Methodology v0.3) — Add a glossary entry for White Team (WT) and align 'white cards / leg ups' wording with TIBER-EU 'leg-ups' so reviewers and auditors can map the terminology.
- **[LOW / S]** `tdora-rtmeth-013` (RT-Methodology v0.3) — Add a single sentence to each of the Operations and Threat Scenarios paragraphs stating these engagements are internal control validation and do not constitute DORA TLPT / TIBER-EU exercises.
- **[INFORMATIONAL / S]** `lifecycle-bhe-001` (BloodhoundEnterprise v0.1) — Add a 'Use in Engagements' section explicitly mapping BHE output into Exercise (recon, post-exploitation pathing), Operation (assumed-breach pathing) and Threat Scenario (joint walk-through of AD abuse paths) lifecycles, and state that BHE is a tooling methodology, not an engagement type itself.
- **[INFORMATIONAL / S]** `lifecycle-bhe-016` (BloodhoundEnterprise v0.1) — Add a one-line cross-reference to the Exercises / Operations / Threat Scenarios processes for engagement codename rules.
- **[INFORMATIONAL / S]** `lifecycle-operations-014` (Operations v1.0) — Add an explicit cross-reference to the deconfliction diagram (resources/diagrams/deconfliction.drawio) in the Deconfliction section, including a one-line summary of the workflow it depicts.
- **[INFORMATIONAL / S]** `lifecycle-operations-016` (Operations v1.0) — Cross-reference the Attack Paths management file from this SOP, name its owner and review cadence, and ensure each Operation's chosen paths are pulled from it (rather than ad-hoc) for traceability.
- **[INFORMATIONAL / S]** `lifecycle-physocq-014` (PhysicalSocial-Questionnaire v1.0) — Confirm in the Introduction that the questionnaire is a scoping input artefact only and that engagement lifecycle phases live in the parent process and engagement SOPs.
- **[INFORMATIONAL / S]** `lifecycle-research-001` (Research-Methodology v0.2) — Keep the cross-cutting positioning; ensure engagement-specific SOPs reference this document so research provenance is auditable from any engagement deliverable.
- **[INFORMATIONAL / S]** `tdora-bhe-001` (BloodhoundEnterprise v0.1) — Confirm that no further TIBER/DORA action is required of this document beyond a one-line cross-reference into the engagement / TLPT framework document; verify the framing against the live TIBER-EU v2 and DORA RTS on TLPT text.
- **[INFORMATIONAL / S]** `tdora-research-001` (Research-Methodology v0.2) — No TLPT alignment is claimed and none is required for this doc. Confirm by adding a one-line note that this methodology is engagement-type agnostic and is referenced (not itself governed) by any TIBER-EU / DORA TLPT engagement.
- **[INFORMATIONAL / S]** `tdora-research-003` (Research-Methodology v0.2) — Add one sentence clarifying that for TIBER-EU / DORA TLPT engagements the regulator-mandated independent TI provider and TTI report are still required; this internal research process is supplementary input, not a substitute.
- **[INFORMATIONAL / S]** `tdora-research-005` (Research-Methodology v0.2) — Add a one-line jurisdictional note: this methodology is jurisdiction-agnostic; specific TIBER-XX / NCA / DORA TLPT obligations are inherited from the engagement scoping document.

## Red team lead with Compliance (2 items)

- **[HIGH / S]** `tdora-threatscenarios-002` (ThreatScenarios v1.1) — Add a single 'Regulatory positioning' sentence in the Introduction: Threat Scenarios are internal control validation, not TLPT; TLPT-scoped activity follows the Exercise process. Cross-reference Exercises and Operations process documents.
- **[INFORMATIONAL / S]** `tdora-threatscenarios-001` (ThreatScenarios v1.1) — Keep the current framing. Optionally add a one-line statement near the Introduction that this process is not TLPT and that TLPT-scoped engagements follow the Exercise process under TIBER-EU. Verify the framework references against the live DORA regulation text and RTS on TLPT.

## Red team lead / Threat hunt (1 items)

- **[HIGH / M]** `lifecycle-operations-004` (Operations v1.0) — Add a Threat-Hunt Handover step in Closure: a structured artefact (per-TTP hunt hypothesis, data sources, expected telemetry, time horizon) that is delivered to the hunt team and tracked to closure.

## Red team lead / Risk (2 items)

- **[HIGH / M]** `lifecycle-operations-005` (Operations v1.0) — Add a Remediation Tracking subsection: where findings are logged (ticketing tool), how owners are assigned, SLAs by severity, retest expectations, and a register the red team can reference for trend analysis.
- **[MEDIUM / S]** `lifecycle-rtmeth-009` (RT-Methodology v0.3) — Add a 'Remediation tracking & lessons learned' subsection that specifies: where remediation actions are tracked, who chases them to closure, cadence of follow-up, and where lessons learned are captured (separate from the offensive Bag of Tricks).

## Red team lead / Risk-Compliance (4 items)

- **[HIGH / M]** `tdora-operations-002` (Operations v1.0) — Either (a) introduce a separate Control Team role with the start/stop/approve authority and reduce White Team to the awareness/communication role per TIBER-EU, or (b) add a glossary note that this SOP uses 'White Team' as a combined CT+WT role for internal Operations and that for TLPT-aligned engagements the two roles are split. Verify TIBER-EU role definitions against the live framework.
- **[MEDIUM / S]** `tdora-operations-005` (Operations v1.0) — Add to Scoping a requirement that each Operation's objectives reference one or more critical or important functions from the institution's register, so that Operations evidence is reusable for DORA reporting. Verify the precise DORA article references against the live regulation.
- **[INFORMATIONAL / S]** `tdora-operations-001` (Operations v1.0) — Add a one-paragraph 'Regulatory positioning' note clarifying that Operations are internal scenario-driven testing and are NOT TLPT, with a forward reference to the document that does govern TLPT-aligned engagements (likely the Exercises SOP or a dedicated TLPT procedure). Verify the exact DORA / TIBER-EU clauses cited against the live regulation text.
- **[INFORMATIONAL / S]** `tdora-operations-006` (Operations v1.0) — Add a one-line note in Scoping that the engagement RoE must record which Euronext regulated entities are in scope and the corresponding competent authority / TIBER-XX implementation, so that any escalation to TLPT framing is traceable.

## Red team lead + Threat hunt lead (1 items)

- **[HIGH / M]** `lifecycle-exercises-002` (Exercises v1.1) — Add a 'Threat-hunt handover' subsection in Closure: for each successful scenario, produce a hunt hypothesis (data sources, query logic stub, expected indicators) and route it to SOC/threat-hunt with an owner and due date.

## Red team lead + Legal/Risk + Facilities (1 items)

- **[HIGH / S]** `lifecycle-exercises-004` (Exercises v1.1) — Add an explicit 'Physical scope' subsection under Initiation/Requirements. Default to 'must be agreed in writing as in or out of scope per exercise' and list the additional authorizations required if in scope (facilities, HR, building security).

## Red team lead + Risk / IT-Sec governance (1 items)

- **[HIGH / S]** `lifecycle-exercises-006` (Exercises v1.1) — Add a 'Remediation tracking' subsection in Closure: each recommendation becomes a register/ticket entry with owner and due date; define retest criteria for high/critical findings and an SLA for status updates.

## Threat intel lead + Red team lead + Compliance (1 items)

- **[HIGH / M]** `tdora-exercises-003` (Exercises v1.1) — State explicitly that for TLPT-framed Exercises the TI provider must be independent of the RT provider, with a named Targeted Threat Intelligence Report deliverable. For internal Exercises, document that internal TI is acceptable but separation of responsibilities is recommended.

## Red team lead + Compliance (6 items)

- **[HIGH / M]** `tdora-exercises-002` (Exercises v1.1) — Add explicit Preparation deliverables to the Initiation phase (or to the TLPT addendum): GTL ingestion, engagement letter, critical-or-important-functions list, provider procurement / qualification record. Cite DORA Art.26 and TIBER-EU Preparation when used.
- **[HIGH / M]** `tdora-exercises-004` (Exercises v1.1) — Add (in the TLPT addendum or this SOP): Control Team identification distinct from WT where the framework requires it; named interface to the TCT / lead overseer; explicit naming of the institution-side test owner.
- **[HIGH / M]** `tdora-exercises-005` (Exercises v1.1) — Add to Closure (or the TLPT addendum) the five artefacts: replay, 360 feedback, remediation plan, attestation, and TCT/authority knowledge-sharing. For non-TLPT Exercises, at minimum require replay + remediation plan.
- **[LOW / S]** `tdora-exercises-015` (Exercises v1.1) — Clarify WT/CT split for TLPT-framed Exercises (or document the deliberate combination). Keep current single-WT model for non-TLPT Exercises.
- **[INFORMATIONAL / S]** `lifecycle-exercises-011` (Exercises v1.1) — Add an Introduction paragraph noting that the Exercise may be performed as a TIBER-EU / DORA TLPT and that, when so framed, the addendum 'Exercise as TLPT' applies (control team, TI provider independence, attestation, etc.).
- **[INFORMATIONAL / S]** `tdora-exercises-001` (Exercises v1.1) — Add an Introduction paragraph stating: (a) most Exercises are internal; (b) where an Exercise is run as a TIBER-EU / DORA TLPT, the TLPT addendum applies and overrides this SOP where they conflict; (c) the trigger criteria (entity in scope of DORA TLPT, designation by lead overseer).

## Compliance + Red team lead + Legal (1 items)

- **[HIGH / L]** `tdora-exercises-006` (Exercises v1.1) — Add (in TLPT addendum) a section 'Authority coordination': identifying the lead overseer for each in-scope Euronext entity, the notification trigger and channel, the attestation deliverable, and the mutual-recognition workflow. Flag jurisdictional ambiguity where multiple NCAs could claim primacy.

## Compliance + Red team lead + Procurement (1 items)

- **[HIGH / M]** `tdora-exercises-007` (Exercises v1.1) — Add a 'Tester requirements' subsection citing DORA Art.27: criteria for external testers; conditions for using internal testers (rotation, independence); approval workflow when internal testers are used for a TLPT.

## Compliance + Red team lead (2 items)

- **[HIGH / S]** `tdora-exercises-008` (Exercises v1.1) — Replace 'Critical Assets/Function' with 'critical or important functions' (DORA terminology) in the TLPT addendum, and explicitly state that for TLPT-framed Exercises live-production systems supporting those functions are in scope under defined controls.
- **[MEDIUM / M]** `tdora-exercises-014` (Exercises v1.1) — Add an entity / jurisdiction applicability section: list in-scope Euronext entities, identify likely lead overseers, and link to per-entity TLPT addenda or NCA-specific guidance.

## Legal/Risk + Red team lead + Compliance (1 items)

- **[HIGH / M]** `tdora-exercises-009` (Exercises v1.1) — Add a 'Risk management of the test' subsection (in the TLPT addendum and this SOP): kill-switch and abort authority; safe-harbour / indemnity clauses for internal and external testers; rollback procedure; crisis-comms plan if a test triggers a real incident response.

## Red team lead + SOC lead + Legal/Risk (1 items)

- **[HIGH / M]** `lifecycle-bhe-002` (BloodhoundEnterprise v0.1) — Reference (or include) an authorization template covering: which domains and OUs are in scope for SharpHound enumeration, the named approver, the formal SOC suppression/allowlisting agreement (not 'disregard alerts'), kill-switch / pause procedure, and reauthorization cadence.

## Red team lead + Legal/Risk + DPO (1 items)

- **[HIGH / M]** `lifecycle-bhe-003` (BloodhoundEnterprise v0.1) — Add a 'Data Handling' section: classify BHE collection data, define retention (e.g. snapshots purged N days after engagement close), state where the SaaS tenant stores data and the GDPR basis, and require Legal/Risk sign-off for any external sharing of attack-path graphs.

## Red team lead + IAM team (1 items)

- **[HIGH / M]** `lifecycle-bhe-004` (BloodhoundEnterprise v0.1) — Track SAML/SSO + MFA enablement as a remediation item with an owner and date; in the meantime document compensating controls (named local accounts, password vaulting, enforced MFA at the app layer, quarterly access review) and a break-glass procedure.

## Red team lead + AD/IAM owner (1 items)

- **[HIGH / M]** `lifecycle-bhe-006` (BloodhoundEnterprise v0.1) — Define a remediation workflow: who receives findings, in which ticketing system, severity per Tier-0 reachability, SLA per severity, and an explicit re-test loop using the next scheduled BHE collection to verify closure.

## Red team lead + Purple team / Detection Engineering (1 items)

- **[HIGH / S]** `lifecycle-bhe-007` (BloodhoundEnterprise v0.1) — Add a 'Purple-team Handover' subsection requiring a debrief with SOC/Detection Engineering after each BHE remediation cycle: review prioritised attack paths, verify detection coverage for SharpHound collection and the abused edges, and log detection gaps into the backlog.

## Red team lead + Threat hunt (2 items)

- **[HIGH / S]** `lifecycle-bhe-008` (BloodhoundEnterprise v0.1) — Add a 'Threat-Hunt Handover' step: every Tier-0-reachable path identified by BHE generates a hunt hypothesis (look-back search for the abuse in logs); results recorded alongside the remediation ticket.
- **[HIGH / S]** `lifecycle-research-007` (Research-Methodology v0.2) — Add a 'Threat-hunt hypothesis output' artefact to Deep Dive and Capability Development; require it to be shared with the threat-hunt function on a defined cadence.

## Red team lead / Threat hunt lead (1 items)

- **[HIGH / M]** `lifecycle-rtmeth-005` (RT-Methodology v0.3) — Add a 'Threat-hunt handover' subsection: define the handover artefact (e.g. ATT&CK-mapped hypothesis pack derived from OPLOGS + report), the recipient (threat hunt / SOC), timing (within X days of close-out), and ownership.

## Legal & Privacy / Red team lead (1 items)

- **[HIGH / S]** `tdora-rtmeth-008` (RT-Methodology v0.3) — Replace the 'Privacy of Information Act (PIA)' reference with GDPR (and the applicable national data-protection law where engagements occur) and align the data categories with the lawful-basis and special-category framing. Where engagements are TIBER-EU framed, add a reference to the framework's data-handling expectations.

## Threat intel / Red team lead (2 items)

- **[HIGH / L]** `tdora-rtmeth-003` (RT-Methodology v0.3) — Add a Threat Intelligence phase that requires a Targeted Threat Intelligence report, names the provider/function (with independence criteria), and shows how TTI drives scenario selection. Replace or supplement the legacy threat profiles with Euronext-specific, FMI-sector-relevant TTPs.
- **[MEDIUM / M]** `lifecycle-rtmeth-013` (RT-Methodology v0.3) — Update Threat Planning to require: (i) ATT&CK technique mapping for each Threat Profile, (ii) source list for the threat intel that informs profile selection, (iii) explicit alignment to financial-market-infrastructure sector threats.

## Red team lead, Legal/Risk (8 items)

- **[HIGH / S]** `tdora-rtdeck-005` (RT-Deck v1.0) — Add a Closure slide enumerating the four artefacts (summary report, remediation plan, attestation, replay/knowledge-sharing) and flag which apply to internal engagements vs TLPT runs.
- **[HIGH / M]** `tdora-rtdeck-001` (RT-Deck v1.0) — Add a slide positioning the team's three engagement types against TIBER-EU v2 and DORA TLPT: which (Exercises) may be run under TIBER-EU with a Control Team / TI provider; which (Operations, Threat Scenarios) are internal-only and can be cited as DORA operational-resilience evidence but are not themselves TLPT.
- **[HIGH / M]** `tdora-rtdeck-002` (RT-Deck v1.0) — If any engagement is to be positioned as TIBER-EU / TLPT, explicitly add Control Team and independent Threat Intelligence provider to the actor model and explain how internal-RT TTI is handled (separation of duties or external TI for TLPT runs). Otherwise state that the deck describes the internal, non-TLPT operating model only.
- **[MEDIUM / S]** `lifecycle-rtdeck-007` (RT-Deck v1.0) — Expand the RoE slide to enumerate authorisation chain, kill-switch / abort, safe-words, evidence handling and data-protection, and cross-reference the per-type process docs for full templates.
- **[MEDIUM / S]** `tdora-rtdeck-006` (RT-Deck v1.0) — Add a safety-controls slide naming kill-switch, rollback, safe-harbours / indemnities, and data-protection treatment; cross-reference per-type process docs for full procedures.
- **[MEDIUM / M]** `tdora-rtdeck-007` (RT-Deck v1.0) — Add a slide noting that critical-function identification follows DORA's definition and that TLPT eligibility and lead-overseer routing depend on the specific Euronext regulated entity in scope; point readers to Legal/Risk for the per-entity mapping.
- **[LOW / S]** `lifecycle-rtdeck-015` (RT-Deck v1.0) — Apply a classification footer / cover-page marking, and decide whether C2 implementation detail belongs in the master explainer deck or in a separate tooling deck with tighter access controls.
- **[LOW / S]** `tdora-rtdeck-008` (RT-Deck v1.0) — Add a positioning statement that the deck describes the internal red-teaming methodology only and that TLPT runs require additional actors (Control Team, independent TI provider), additional artefacts (TTI, attestation) and authority coordination — with a pointer to the document or owner that governs TLPT engagement.

## Legal/Risk + Red team lead (5 items)

- **[HIGH / M]** `lifecycle-physoc-006` (PhysicalSocial v1.0) — Expand authorization to require: Legal counter-signature, HR acknowledgement, Group Security awareness, landlord/building-security notification where premises are shared, and a documented decision on local law-enforcement pre-notification per jurisdiction.
- **[HIGH / M]** `lifecycle-physoc-008` (PhysicalSocial v1.0) — Add a Social-engineering rules subsection covering target carve-outs, pretext approval, audio/video recording legality per jurisdiction, sock-puppet account governance and post-engagement decommissioning.
- **[HIGH / M]** `lifecycle-research-003` (Research-Methodology v0.2) — Add a Legal/IP review gate to Capability Development covering third-party-code licensing, customer/vendor disclosure obligations, and a documented decision to publish, embargo, or keep internal.
- **[HIGH / M]** `tdora-physoc-007` (PhysicalSocial v1.0) — Add a jurisdictional coordination subsection naming, for each Euronext regulated entity, the relevant competent authority, the home/host relationship and the mutual-recognition route. Verify against current published TIBER-EU and DORA TLPT cross-border guidance.
- **[HIGH / M]** `tdora-physoc-008` (PhysicalSocial v1.0) — Add a 'Risk management of the test' subsection covering kill-switch, rollback, safe harbour and indemnification, applicable whether or not the test is run under TLPT.

## Red team lead + IR lead (1 items)

- **[HIGH / M]** `lifecycle-research-008` (Research-Methodology v0.2) — Add a section describing the three adjacent-remit flows: research -> IR runbook updates, research / RT support during external assessments, research / RT support during live incidents - including triggers and owners.

## Threat hunt / SOC liaison (1 items)

- **[HIGH / S]** `lifecycle-physoc-004` (PhysicalSocial v1.0) — Add a Threat-hunt handover step listing the physical-attack TTPs to be hunted post-engagement (badge anomalies, after-hours access, rogue device MACs on edge ports, suspicious sock-puppet contacts).

## Legal/Risk (2 items)

- **[HIGH / L]** `lifecycle-physoc-010` (PhysicalSocial v1.0) — Add a per-jurisdiction annex covering at least NL/FR/BE/PT/IT/IE with local legal counsel sign-off on authorization wording, recording legality, ID acceptable in the Get-out-of-jail letter and works-council notification.
- **[MEDIUM / M]** `lifecycle-physoc-007` (PhysicalSocial v1.0) — Update the Get-out-of-jail letter template and policy to reference an indemnification clause, evidence of liability insurance, a 24/7 legal contact for detained operators, and bail/counsel funding commitments.

## Legal/DPO + Red team lead (1 items)

- **[HIGH / M]** `lifecycle-physoc-009` (PhysicalSocial v1.0) — Add a 'Data handling and evidence custody' subsection prescribing encryption, access control, retention, secure destruction, and GDPR lawful-basis text for material captured during physical/social testing.

## Red team lead + Group CISO (2 items)

- **[HIGH / M]** `tdora-physoc-003` (PhysicalSocial v1.0) — Define and document White Team / Control Team membership for any physical leg run under TLPT, including escalation to Group level and to the relevant lead overseer / competent authority.
- **[HIGH / M]** `tdora-physoc-005` (PhysicalSocial v1.0) — Add Closure artefacts to the Physical Pentest pipeline: replay workshop, 360 feedback, remediation plan with owners and dates, and an attestation template aligned with TIBER-EU.

## Threat intel + Red team lead (1 items)

- **[HIGH / M]** `tdora-physoc-004` (PhysicalSocial v1.0) — Add a step that, when running under TLPT, the physical scenarios and pretexts are derived from a TTI report from an independent TI provider and mapped to MITRE ATT&CK techniques.

## Legal / DPO (1 items)

- **[HIGH / M]** `tdora-physoc-009` (PhysicalSocial v1.0) — Add a GDPR / data-protection section covering lawful basis, DPIA, retention, deletion and per-jurisdiction position on recording. Engage the DPO before next physical test.

## Legal/Risk + Data Protection Officer (1 items)

- **[HIGH / M]** `lifecycle-physocq-003` (PhysicalSocial-Questionnaire v1.0) — Add a Data Handling section: state the lawful basis, require redaction of personal data in evidence (e.g. blur badge photos, mask names in access logs), mandate encrypted transit, define storage system + access control, and set a retention/destruction schedule consistent with the parent PhysicalSocial process.

## Red team lead + Risk (4 items)

- **[HIGH / S]** `lifecycle-physocq-007` (PhysicalSocial-Questionnaire v1.0) — Add an 'Approvals and Escalation' section with a sign-off matrix (site, security, red team, risk) and a rule that any Critical or High finding is escalated immediately rather than waiting for periodic review.
- **[HIGH / M]** `lifecycle-physocq-006` (PhysicalSocial-Questionnaire v1.0) — Add a 'Site Context' question block covering: hosts critical/important DORA function (Y/N), trading or market-data infrastructure on-site, customer-facing footprint, presence of vulnerable people, and any regulator-mandated controls. Use the answers to gate sign-off.
- **[INFORMATIONAL / S]** `tdora-physocq-001` (PhysicalSocial-Questionnaire v1.0) — No action required for TLPT alignment. If, however, the questionnaire's Vulnerability/Maturity score is ever cited as evidence of resilience under DORA Art.24-26, add a footnote making clear that the questionnaire is a periodic baseline assessment, not a TLPT, and that physical sites supporting DORA-critical functions remain in scope for engagement-led testing under the parent PhysicalSocial process.
- **[INFORMATIONAL / S]** `tdora-physocq-002` (PhysicalSocial-Questionnaire v1.0) — Add a Site Context question identifying whether the office supports a DORA critical or important function, and use the answer (alongside CMDB criticality) to drive questionnaire periodicity and sign-off escalation. This also makes the artefact reusable as DORA Art.5 record-keeping evidence.

## Red team lead with Purple team (2 items)

- **[MEDIUM / M]** `lifecycle-threatscenarios-012` (ThreatScenarios v1.1) — Reframe Execution to make the demonstrative nature explicit: keep Recon/Exploit/Escalation but add 'demonstration walk-through points' where the operator pauses to show the blue team the artefacts (logs, telemetry, alerts) that did or did not fire. Make clear this is not a stealth kill-chain.
- **[MEDIUM / M]** `tdora-threatscenarios-005` (ThreatScenarios v1.1) — Extend the Report phase into a 'Closure' phase with three artefacts: a joint replay session, a remediation plan (owner / due date / retest), and an internal sign-off by the Control owner confirming completion and clean-up. This dovetails with the lifecycle review's purple-team and remediation-tracking findings.

## Red team lead with Threat intel (2 items)

- **[MEDIUM / S]** `tdora-threatscenarios-003` (ThreatScenarios v1.1) — Either (a) keep operator-driven threat-actor selection but note explicitly that this differs from TIBER-EU's TI phase, or (b) when a Threat Scenario is intended to feed broader TLPT preparation, document the consumption of an existing TTI/GTL produced for an Exercise so the inputs are traceable.
- **[LOW / S]** `lifecycle-threatscenarios-015` (ThreatScenarios v1.1) — Update the Threat Actors guidance to include external-actor archetypes (compromised contractor, stolen-credential external attacker, supply-chain compromise) as candidates whenever the in-scope tool is reachable from outside the corporate perimeter or via a third party.

## Compliance with Red team lead (1 items)

- **[MEDIUM / S]** `tdora-threatscenarios-006` (ThreatScenarios v1.1) — Add a one-line scope-of-applicability statement: which Euronext regulated entities and jurisdictions the Threat Scenario process applies to. If multiple entities, note which NCA's TIBER-XX guidance is the reference point should the outputs be cited as resilience-testing evidence.

## Legal/Risk / DPO with Red team lead (1 items)

- **[MEDIUM / M]** `tdora-threatscenarios-007` (ThreatScenarios v1.1) — Add a 'Data handling' subsection to Execution: what to do if personal or confidential data is encountered, minimisation rules, evidence retention/redaction, and the contact (DPO / Legal) for escalations. Pair with the lifecycle review's OPLOG storage finding.

## Red team lead / White team (3 items)

- **[MEDIUM / S]** `lifecycle-operations-009` (Operations v1.0) — Add a Kill-Switch / Abort procedure: communication channel (out-of-band), safe-word, expected RT actions on abort (cease, preserve evidence, notify), and resumption protocol with WT sign-off.
- **[MEDIUM / S]** `lifecycle-operations-015` (Operations v1.0) — Add a Leg-Up procedure: written request from RT to WT, criteria for approval, mandatory recording in OPLOG and final report (including which objective was reached only with a leg-up), and rules for when a scenario should instead be marked 'not concluded'.
- **[LOW / S]** `lifecycle-operations-013` (Operations v1.0) — Replace the closing sentence with a Clean-Up checklist (per-artefact rows) that the RT operator and WT must jointly sign off; tie it to closure of the engagement ticket.

## Red team lead / Threat intel (1 items)

- **[MEDIUM / S]** `tdora-operations-003` (Operations v1.0) — Add a paragraph clarifying that Operations rely on opportunistic / internal CTI inputs and that any engagement intended to satisfy TLPT must additionally procure an independent TI provider producing a TTI report. Verify the TI-provider independence clause against the live RTS on TLPT.

## Legal/DPO + Compliance + Red team lead (1 items)

- **[MEDIUM / M]** `tdora-exercises-010` (Exercises v1.1) — Rewrite Data Handling around: GDPR (lawful basis, special categories), MAR/MiFID inside-information and client-data confidentiality, DORA TLPT confidentiality requirements. Provide a decision tree: encountered-data type -> required action (halt, notify, delete, retain under controls).

## Red team lead + White team lead (2 items)

- **[MEDIUM / S]** `lifecycle-exercises-016` (Exercises v1.1) — Update Leg-Ups section to require: (1) entry in an engagement leg-up log, (2) WT countersignature, (3) explicit tagging of any downstream finding as 'leg-up assisted' in the Closure report.
- **[LOW / S]** `tdora-exercises-013` (Exercises v1.1) — Update Leg-Ups: each leg-up logged with WT countersignature, and tagged in the closure report; for TLPT-framed Exercises, called out in the closure / attestation pack.

## Red team lead + IT operations (1 items)

- **[MEDIUM / S]** `lifecycle-exercises-017` (Exercises v1.1) — Add a 'Clean-up & restoration' subsection in Closure with a fixed checklist, an owner (RT lead), and BT/IT verification as a gate to formal engagement closure.

## Threat intel lead (1 items)

- **[MEDIUM / M]** `tdora-exercises-011` (Exercises v1.1) — Define a 'Targeted Threat Intelligence Report' deliverable in the TI phase, with template (threat actors, TTPs, attack hypotheses, scenario seeds, ATT&CK mapping), a named approver, and version control.

## Red team lead + AD/IAM team (1 items)

- **[MEDIUM / S]** `lifecycle-bhe-009` (BloodhoundEnterprise v0.1) — State Euronext's stance on the optional Local-Admin-everywhere grant (default: NO) and on LDAP cleartext fallback (default: blocked); record exceptions with a named approver and review date.

## Red team lead + Cloud security (1 items)

- **[MEDIUM / M]** `lifecycle-bhe-012` (BloodhoundEnterprise v0.1) — Add an 'Entra ID' subsection covering collection setup, cloud Tier-0 baseline, hybrid attack paths, and a current-state note on whether cloud collection is enabled at Euronext.

## Red team lead + Procurement + Legal/Compliance (1 items)

- **[MEDIUM / M]** `tdora-bhe-003` (BloodhoundEnterprise v0.1) — Reference the ICT third-party register entry for the BHE SaaS in this document (or in a linked Tooling Inventory), and ensure data-residency, exit-clause and sub-outsourcing items are tracked there. Verify the precise DORA articles cited against the live text.

## Risk & Compliance / Red team lead (1 items)

- **[MEDIUM / S]** `tdora-rtmeth-010` (RT-Methodology v0.3) — Add a short jurisdictional clause stating that for any engagement positioned as TIBER-EU / TLPT, the applicable NCA and the corresponding TIBER-XX implementation must be identified per engagement, with the lead overseer recorded in the engagement letter.

## Red team lead, White team (1 items)

- **[MEDIUM / S]** `lifecycle-rtdeck-010` (RT-Deck v1.0) — Add an approval-and-log requirement to the leg-up slide and require that each leg-up appear in the final report so coverage and detection findings remain defensible.

## Red team lead, Threat intel (1 items)

- **[MEDIUM / S]** `tdora-rtdeck-003` (RT-Deck v1.0) — Add a note that internally-sourced TTI is acceptable for internal Exercises / Operations / Threat Scenarios but that TLPT runs require an independent TI provider; verify wording against the live RTS on TLPT.

## Purple team + Red team lead (1 items)

- **[MEDIUM / S]** `lifecycle-research-006` (Research-Methodology v0.2) — Make purple-team close-out mandatory and define the structured artefacts it must produce that feed both the Research and Tool repositories (detection deltas, capability lifecycle changes, hunt hypotheses).

## Red team lead + Local Facilities Manager (1 items)

- **[MEDIUM / S]** `lifecycle-physoc-012` (PhysicalSocial v1.0) — Add explicit no-go zones, timing exclusions and an evacuation-compliance clause to the Scope subsection.

## Red team lead + Procurement (1 items)

- **[MEDIUM / S]** `tdora-physoc-006` (PhysicalSocial v1.0) — Add a 'Tester requirements' subsection covering internal-vs-external posture, rotation/independence rules, and external-provider qualification criteria, citing DORA Art.27 and the RTS on TLPT.

## Red team lead + Operational Resilience (1 items)

- **[MEDIUM / M]** `tdora-physoc-011` (PhysicalSocial v1.0) — Reconcile the location-criticality model with the entity's DORA register of critical or important functions; add an override that any location hosting a critical function automatically requires Pentest-grade testing.

## Red team lead + Awareness team (1 items)

- **[MEDIUM / M]** `lifecycle-physocq-009` (PhysicalSocial-Questionnaire v1.0) — Add a Social Engineering and Tailgating block covering visitor-escort enforcement, anti-tailgating measures, awareness training cadence, and reception protocol for unsolicited contacts.

## Red team lead + Records management (1 items)

- **[MEDIUM / S]** `lifecycle-physocq-013` (PhysicalSocial-Questionnaire v1.0) — Add a 'Response Retention' clause stating retention period, archive location, and re-versioning rule when a site is re-questioned.

## Document author (2 items)

- **[LOW / S]** `lifecycle-research-013` (Research-Methodology v0.2) — Either embed Figure 1 in the docx or link the canonical .drawio path so prose-to-diagram coherence can be reviewed in one pass.
- **[LOW / S]** `lifecycle-research-014` (Research-Methodology v0.2) — Add Status and Approver fields to the version table; mark v0.2 as Draft until reviewed by the red team lead.

## IR / SOC liaison (1 items)

- **[LOW / S]** `lifecycle-physocq-010` (PhysicalSocial-Questionnaire v1.0) — Cite the group-wide IR procedure by name and version, and specify the notification timing and reporting channel for stolen physical assets.

## Red team lead + Threat hunt + IR (1 items)

- **[INFORMATIONAL / S]** `lifecycle-bhe-018` (BloodhoundEnterprise v0.1) — Add an 'Adjacent uses' subsection covering BHE support to threat hunt during external red team tests of Euronext and during live IR, with the caveat that collection cadence/permissions may need adjustment in those modes.

## Red team lead + Compliance/Legal (1 items)

- **[INFORMATIONAL / S]** `tdora-bhe-002` (BloodhoundEnterprise v0.1) — Add a one-line cross-reference: 'When BHE is used inside a TIBER-EU / DORA TLPT Exercise, the Control Team must be informed of collection windows and BHE outputs are part of the test evidence governed by the Closure / attestation steps of the testing framework.' Verify wording against the live TIBER-EU v2 and DORA RTS on TLPT.
