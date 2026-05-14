---
name: engagement-lifecycle-review
description: Evaluate a red team process artefact (already ingested into workdir/<slug>/) against the Euronext engagement lifecycle. Engagement-type-aware: applies the correct phase template for Exercise / Operation / Threat Scenario, checks codename + theme convention, mandatory purple-team close-out, threat-hunt and IR-support coverage, cyber + physical scope. Emits findings JSON files conforming to schemas/finding.schema.json.
---

# When to use

After `process-ingest` has run on an artefact. Read the ingested content from `workdir/<slug>/` and write findings to `findings/<slug>/engagement-lifecycle-review.json` as a JSON array.

# Required reading before evaluating

- `schemas/engagement-types.md` — the operational reference defining the three engagement types and cross-cutting expectations. **Always load this first** so you don't raise wrong-type findings (e.g. flagging stealth on a Threat Scenario).
- `schemas/finding.schema.json` — the output contract. Every finding you emit must validate against it.
- `workdir/<slug>/meta.json`, `content.md`, `diagram.json`, `captions.md` (whichever exist).

# Procedure

1. **Confirm engagement type.** Start from `meta.json.engagement_type_guess`. Read enough of `content.md` to either confirm or override it. If the doc covers multiple types, evaluate each section against its applicable template; if it's a methodology that spans all, treat it as `cross-cutting` and apply the union of expectations (with type tags on each finding).

2. **Apply the type-specific phase template.** For each phase below, decide one of: `present-and-clear`, `present-but-ambiguous`, `missing`, or `not-applicable`. Cite section refs from headings in `content.md`.

   **Spine (all types):**
   - Scoping
   - Authorization (legal sign-off, RoE, safe-words, data handling, blue-team notification rules where applicable)
   - Codename assignment (per convention — see step 3)
   - Execution (type-specific, see below)
   - Reporting (finding taxonomy, severity model, evidence requirements)
   - **Purple-teaming close-out** with the blue team (mandatory for all three types)
   - Threat-hunt handover (red findings → hunt hypotheses)
   - Remediation tracking
   - Lessons learned / capture into the team knowledge base

   **Type-specific execution phases:**
   - **Exercise:** OSINT → Targeted threat intelligence → APT simulation → Initial access → post-exploitation toward objective. Stealth is in scope; detection by blue team is itself a result to capture.
   - **Operation:** Assumed-breach setup → Scenario execution → Objective achievement → Detection observation. Stealth in scope.
   - **Threat Scenario:** Joint planning with blue team → Demonstration of internal-tool abuse paths (GitLab, Jenkins, CI/CD, internal SaaS, secret stores, ticketing) → Real-time discussion of detections and controls. **Stealth is NOT in scope — do not flag its absence.**

3. **Codename + theme convention check.**
   - Every engagement doc must require a codename.
   - For **Exercises and Operations**, the codename theme must be **known fictional characters** (movies / TV / books). Flag if absent or contradictory.
   - For Threat Scenarios, a codename is required but the fictional-character theme constraint does not apply.

4. **Cross-cutting completeness checks (raise findings if missing or ambiguous):**
   - Cyber **and** physical scope explicitly addressed (or explicitly out-of-scope with rationale).
   - Authorization chain: who signs off; what stops the engagement (kill-switch, abort criteria).
   - Safety / blast-radius controls (especially for Operations and Threat Scenarios that touch prod systems like GitLab/Jenkins).
   - Evidence-handling and data-protection rules (sensitive data encountered during pivots).
   - Provider/control-team roles if the engagement is run as TIBER-EU / DORA TLPT.
   - Threat-hunt handover described, not just promised.
   - Lessons learned capture mechanism (document, ticket, register — something concrete).

5. **Adjacent-remit completeness (only for methodology / framework / research docs):**
   - Threat hunting at engagement close.
   - Threat hunting / assistance during **external** red team exercises run against the institution.
   - Threat hunting / assistance during **live security incidents**.
   A methodology that ignores any of these understates the team's remit — flag as `completeness-gap`.

6. **Diagram coherence (if `diagram.json` or `captions.md` exists):**
   - Every actor/role mentioned in `content.md` should appear in the diagram and vice versa.
   - Every flow should have a label.
   - Trust boundaries / swimlanes should match what the prose claims.

# Emitting findings

Write `findings/<slug>/engagement-lifecycle-review.json` — a JSON array of objects matching `schemas/finding.schema.json`. For each finding:

- Set `evaluator: "engagement-lifecycle-review"`.
- Use `finding_id` of the form `lifecycle-<slug>-NNN` (zero-padded sequence).
- Set `artefact.engagement_type` to the type the finding applies to (or `cross-cutting`).
- Always include at least one `framework_refs` entry. Prefer the most specific anchor available:
  - PTES phase names for generic phase-completeness gaps.
  - TIBER-EU / DORA-TLPT for regulator-aligned gaps.
  - `EURONEXT-INTERNAL` once `references/euronext-internal-taxonomy.md` is populated.
- Quote the artefact text in `evidence.quote_or_observation` (use `<missing>` for absences) and write `evidence.expected` in one sentence.
- Severity guidance:
  - `critical`: missing authorization, missing kill-switch, no purple-team close-out, no evidence handling rules.
  - `high`: missing phase, no codename convention, methodology silent on physical scope or IR support.
  - `medium`: ambiguities, weak gates between phases, missing owners.
  - `low`: stylistic / naming issues.
  - `informational`: improvement opportunities.
- Include `recommendation.text`, `recommendation.effort` (S/M/L), and a sensible `recommendation.owner_hint`.

If the artefact is not an engagement / methodology / research doc at all (e.g. a policy stub), emit a single `informational` finding noting it's out of scope for this evaluator and exit.

# Anti-patterns to avoid

- Do **not** flag absence of stealth on a Threat Scenario.
- Do **not** assume every engagement must be TLPT — that's the `tiber-dora-alignment` evaluator's call.
- Do **not** invent internal control IDs. Use `EURONEXT-INTERNAL` refs only when `references/euronext-internal-taxonomy.md` contains the matching id.
- Do **not** rewrite the document. Findings reference sections, they don't replace them.
