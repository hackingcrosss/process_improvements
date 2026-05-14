---
purpose: Operational reference loaded by evaluator skills. Defines how the three Euronext red team engagement types differ so evaluators apply the correct phase template and don't raise wrong-type findings (e.g. flagging "no stealth" on a Threat Scenario).
---

# Euronext red team engagement types

All three types share a core spine: **scoping → authorization (RoE, legal) → codename → execution → reporting → purple-team close-out → remediation tracking → lessons learned**, and all three may include physical components.

## 1. Exercise

- **Shape:** Full external kill-chain.
- **Phases (type-specific):** OSINT → Targeted threat intelligence → APT simulation → Initial access → (typically) post-exploitation toward an objective.
- **Stealth:** Critical. Detection by blue team is itself a finding.
- **Codename theme:** Known fictional characters (movies / TV / books).
- **Typical regulator overlap:** May be run as TIBER-EU / DORA TLPT (with a control team and threat intel provider) or as an internal exercise. Evaluators must check whether the doc claims TLPT alignment and, if so, whether the TIBER-EU phases (GTL, TTI, RTT, Closure) are present.

## 2. Operation

- **Shape:** Usually **assumed breach**, scoped to a small set of pre-defined scenarios / objectives.
- **Phases (type-specific):** Assumed-breach setup (foothold provisioning) → Scenario execution → Objective achievement → Detection observation.
- **Stealth:** Critical (smaller blast radius than an exercise but still adversarial).
- **Codename theme:** Known fictional characters (movies / TV / books).
- **Typical regulator overlap:** Internal; may be cited as evidence of resilience under DORA but is not itself a TLPT.

## 3. Threat Scenario

- **Shape:** **Assumed breach with blue team in the room.** Walk-through / demonstrative.
- **Phases (type-specific):** Joint planning with blue team → Demonstration of tool-abuse paths (e.g., GitLab, Jenkins, CI/CD, internal SaaS, ticketing, secret stores) → Real-time discussion of detections and controls.
- **Stealth:** **Not expected.** Do **not** raise stealth findings against a Threat Scenario doc.
- **Codename:** Yes (always), but the fictional-character theme is specific to Exercises and Operations — Threat Scenarios may use a different convention.
- **Typical regulator overlap:** Internal control validation; useful evidence for DORA operational resilience testing but not TLPT.

# Cross-cutting expectations every engagement doc must cover

- Codename assigned per the convention above.
- Authorization / Rules of Engagement: legal sign-off, scope boundaries, safe-words, data-handling, blue-team notification rules (where applicable per type).
- Physical scope explicitly addressed or explicitly out-of-scope.
- **Purple-teaming close-out** with the blue team to define defensive improvements — mandatory for all three types.
- Threat-hunt handover: how red findings turn into hunt hypotheses for blue.
- Remediation tracking and lessons-learned capture.

# Adjacent team responsibilities (in scope when reviewing methodology / research docs)

- Threat hunting at engagement close-out.
- Threat hunting / assistance during **external** red team exercises the institution undergoes.
- Threat hunting / assistance during **live security incidents**.

A methodology doc that ignores these understates the team's actual remit and should be flagged.
