---
name: tiber-dora-alignment
description: Evaluate a red team process artefact (already ingested) against TIBER-EU v2 and DORA TLPT (Regulation (EU) 2022/2554, Articles 26-27, plus the related RTS on TLPT). Identifies whether the doc claims TLPT alignment, whether the required TIBER-EU phases / actors / artefacts are present, and where the doc is silent on regulator-mandated elements. Emits findings JSON files conforming to schemas/finding.schema.json.
---

# When to use

After `process-ingest`. Read from `workdir/<slug>/` and write findings to `findings/<slug>/tiber-dora-alignment.json`.

# Required reading first

- `schemas/engagement-types.md` — to understand which engagement types are TLPT-eligible at all.
- `schemas/finding.schema.json` — output contract.
- `workdir/<slug>/meta.json`, `content.md`, `diagram.json` (whichever exist).

# Authoritative anchors (cite these in `framework_refs`)

- **TIBER-EU Framework v2** (ECB, 2018, current): four phases — Preparation (Generic Threat Landscape, scoping), Threat Intelligence (Targeted Threat Intelligence), Red Team Test (RTT), and Closure (replay, 360° feedback, remediation planning, attestation). Core actors: TIBER Cyber Team (TCT), Control Team (CT), Threat Intelligence (TI) provider, Red Team (RT) provider, White Team (WT).
- **DORA — Regulation (EU) 2022/2554** Articles 26 (advanced testing of ICT tools, systems and processes based on TLPT) and 27 (requirements for testers). Reference the relevant **RTS on TLPT** clauses (scope, internal vs external testers, threat intel provider, mutual recognition, control team, communication with authorities, attestation/closure).
- For NCA-specific guidance (AFM, AMF, FSMA, CSSF, CONSOB, etc.) flag as `OTHER` with a note pointing the user to the relevant national TIBER-XX implementation.

If you cannot recall a clause precisely, do **not** invent it — set `confidence: "low"` and write the framework ref as `TIBER-EU v2 (general)` or `DORA Art.26 (general)` and ask in the recommendation that the user verify against the live text.

# Procedure

1. **Determine TLPT relevance.**
   - Does the doc explicitly claim TLPT / TIBER alignment? Search for `TIBER`, `TLPT`, `DORA`, `threat intelligence provider`, `control team`, `white team`, `attestation`, `mutual recognition`, `lead overseer`, `competent authority`.
   - If yes → run all checks below.
   - If no but the engagement type is `exercise` → flag at `informational` that the doc may be a candidate for TLPT framing, and run the checks anyway as a gap analysis.
   - If no and the engagement type is `operation` or `threat-scenario` → run a reduced check focused on whether the doc inadvertently implies TLPT applicability without the supporting actors/artefacts (a real risk for audit conversations).

2. **TIBER-EU phase coverage.** For each phase, mark `present`, `partial`, or `missing` and quote section refs:
   - **Preparation:** Generic Threat Landscape (GTL) consumption, scoping document, engagement letter, identification of critical functions, procurement of providers (TI + RT), establishment of WT/CT.
   - **Threat Intelligence:** Targeted Threat Intelligence (TTI) report; identification of credible threat actors and TTPs; alignment of test scenarios with TTI.
   - **Red Team Test:** Execution per TTI-derived scenarios; controlled escalation; legs/flags/objectives; safe harbours.
   - **Closure:** Replay with blue team, 360° feedback, remediation plan, attestation, knowledge sharing with TCT/regulator.

3. **DORA TLPT requirements check.** Raise findings for any of these that are missing or ambiguous when TLPT is claimed or implied:
   - **Scope:** critical or important functions identified per DORA's "critical functions" notion; production systems are in scope (TLPT requires live-prod testing under controls).
   - **Tester requirements (Art. 27):** internal vs external testers; if internal, the rotation/independence requirements; if external, the procurement and qualification criteria.
   - **Threat intelligence provider:** an independent TI provider feeding TTI; not the same entity as the RT provider unless explicitly justified.
   - **Control team:** a small named CT inside the institution that owns the test, distinct from blue team; communication and escalation paths defined.
   - **Coordination with authorities:** lead overseer / competent authority notification; attestation to the authority post-test; mutual recognition pathway.
   - **Risk management of the test itself:** safety controls, kill-switch, rollback, safe harbours for testers, indemnities.
   - **Data protection:** handling of personal data and confidential information encountered during the test; legal basis under GDPR.
   - **Closure artefacts:** test summary report, remediation plan, attestation, knowledge sharing.

4. **Anti-misalignment check.** If the doc treats TIBER-EU phases as optional or describes "stealth-free walk-through" as TLPT, flag as `regulatory-misalignment` (severity `high`) — Threat Scenarios are useful but are not TLPT.

5. **Cross-checks against engagement-lifecycle-review.** The two evaluators overlap intentionally on RoE/authorization. Do **not** silence findings here that overlap; the synthesizer will dedupe. But anchor every finding here to a TIBER/DORA reference so the audit trail is clear.

# Emitting findings

Write `findings/<slug>/tiber-dora-alignment.json` — JSON array conforming to `schemas/finding.schema.json`.

- `evaluator: "tiber-dora-alignment"`.
- `finding_id`: `tdora-<slug>-NNN`.
- Every finding **must** include at least one `framework_refs` entry with `framework: "TIBER-EU"` or `framework: "DORA-TLPT"` (or both).
- Severity guidance:
  - `critical`: claims TLPT alignment but is missing a regulator-mandated element (e.g. control team, attestation, TI provider independence).
  - `high`: ambiguity that could be read as TLPT non-compliance under examination.
  - `medium`: phase present but evidence-light.
  - `low`: terminology drift (e.g. uses "white cell" when TIBER-EU says "White Team").
  - `informational`: candidate-for-TLPT framing for an Exercise that is not currently positioned as one.
- Always set `confidence`. Use `low` whenever you cite a clause from memory rather than from a source you have in this workspace.

# Anti-patterns to avoid

- Do **not** assume DORA TLPT applies to every Euronext entity equally — Euronext operates several regulated entities across multiple jurisdictions; flag jurisdictional ambiguity rather than choose one.
- Do **not** quote precise regulation text you are not certain of. A general ref + a `verify against live text` recommendation is safer than a fabricated quote.
- Do **not** raise stealth/no-stealth findings here — that's lifecycle's job.
