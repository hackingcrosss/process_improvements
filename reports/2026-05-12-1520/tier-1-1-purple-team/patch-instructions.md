# Tier 1.1 — Purple-team close-out: integration instructions

This packet adds the **mandatory Purple-team close-out phase** to every engagement SOP and replaces the broken `Purple Teaming Process document` cross-reference in the methodology. It closes coherence findings `-005`, `-006`, `-009`, `lifecycle-rtdeck-003`, `lifecycle-exercises-001`, `lifecycle-operations-003`, `lifecycle-physoc-003`, `lifecycle-threatscenarios-001` — **4 of the 12 critical findings**.

## What's in this packet

| File | Purpose |
|---|---|
| `Purple_Teaming_Process_v0.1.docx` | Drop-in new process doc. Place it at `inputs/Methodology/Purple_Teaming_Process_v0.1.docx` and the cross-reference from the methodology resolves. |
| `patch-instructions.md` (this file) | The exact paragraph to add to each engagement SOP + the methodology version-pin update. |

## How to apply

The new doc is ready to drop in. For each engagement SOP, you have two near-identical patches: one to add the **Purple-team close-out subsection** at the end of the Closure (or Report) section, and one to add the **OFI block** alongside it. Both reference the new Purple Teaming Process doc instead of duplicating its content.

---

### 1. Drop-in: place the new doc

Copy `Purple_Teaming_Process_v0.1.docx` to:

```
inputs/Methodology/Purple_Teaming_Process_v0.1.docx
```

That alone resolves the broken cross-reference (coherence finding `-006`).

---

### 2. `inputs/Engagements/0. Threat Scenarios/ThreatScenarios_Process_v1.1.docx`

**Location:** at the end of the existing `## Report` section (which you already plan to rename to `## Closure` per the earlier quick-win annotation).

**Add this subsection as the last subsection of `## Closure`:**

> ### Purple-team close-out
>
> Every Threat Scenario concludes with a mandatory purple-teaming close-out workshop with the Blue Team. The workshop walks through the scenario phase-by-phase, correlates Red Team actions against Blue Team detections and produces a detection-vs-action map, a hunt-hypothesis list for the SOC, OFIs for both teams, and a prioritised remediation backlog with named owners. Because Threat Scenarios are blue-team-collaborative during execution, the close-out emphasises detection-gap analysis and tool-specific hunt hypotheses rather than phase-by-phase replay.
>
> For the full procedure, attendees, inputs, outputs and engagement-type-specific guidance, see `Purple_Teaming_Process_v0.1.docx`.

---

### 3. `inputs/Engagements/1. Operations/Operations_Process_v1.0.docx`

**Location:** at the end of the existing `## Closure` section, after the current closure paragraphs.

**Add this subsection:**

> ### Purple-team close-out
>
> Every Operation concludes with a mandatory purple-teaming close-out workshop with the Blue Team. The workshop is the Blue Team's first detailed exposure to the engagement (Operations are assumed-breach and the Blue Team is typically unaware during execution); pace the walkthrough accordingly. Outputs: detection-vs-action map per kill-chain phase, gap register, hunt-hypothesis list for the SOC, OFIs for both teams, and a prioritised remediation backlog with named owners.
>
> For the full procedure, attendees, inputs, outputs and engagement-type-specific guidance, see `Purple_Teaming_Process_v0.1.docx`.

---

### 4. `inputs/Engagements/2. Exercises/Exercises_Process_v1.1.docx`

**Location:** at the end of the existing `### Closure` subsection within `## Phases Description`.

**Add this subsection (as `#### Purple-team close-out` since Closure is already an `###`):**

> #### Purple-team close-out
>
> Every Exercise concludes with a mandatory purple-teaming close-out workshop with the Blue Team. For Exercises run as TLPT under DORA (Regulation (EU) 2022/2554, Articles 26–27) or under TIBER-EU, this corresponds to the regulator-mandated 360-degree feedback session, and additional attestation artefacts are required (replay walkthrough, test report with MITRE ATT&CK coverage, joint attestation signed by RT Provider, TI Provider, Control Team and the financial entity).
>
> For the full procedure, attendees, inputs, outputs, the RACI and TLPT-specific requirements, see `Purple_Teaming_Process_v0.1.docx`.

---

### 5. `inputs/Methodology/RedTeam_Methodology_v0.3.docx`

The methodology already references "the Purple Teaming Process document". Now that the doc exists, **pin the version**:

**Find:** "These engagements should follow the Purple Teaming Process document."

**Replace with:** "These engagements should follow `Purple_Teaming_Process_v0.1.docx`."

This closes the broken-xref finding `-006` and resolves the methodology-vs-SOP coherence on purple teaming.

---

### 6. (Optional but recommended) `inputs/Physical & Social/PhysicalSocial_Process_v1.0.docx`

The Physical Pentest sub-process currently ends at `## Report`. Adding the same close-out closes `lifecycle-physoc-003`.

**Add a new section after `## Report` (or rename `## Report` to `## Closure` and add the subsection):**

> ### Purple-team close-out
>
> Every Physical Pentest concludes with a mandatory purple-teaming close-out workshop with the Blue Team, broadened to include Physical Security and Facilities. The walkthrough covers the physical kill-chain (reconnaissance, access controls, social engineering, hardware implants, escalation) and produces a detection-vs-action map against badge logs, CCTV recordings, intruder-detection alarms and security-guard reports.
>
> For the full procedure, attendees, inputs, outputs and physical-specific guidance, see `Purple_Teaming_Process_v0.1.docx`.

---

## Impact

Applying patches 1–5 closes the following findings from the 2026-05-12-1520 register:

- `coherence-rt-meth-009` (high) — methodology mandates purple-team close-out absent from SOPs
- `coherence-rt-meth-010` (medium) — broken cross-reference `Purple Teaming Process document`
- `lifecycle-rtdeck-003` (critical) — methodology silent on purple-team close-out, remediation tracking, hunt-hypothesis handover
- `lifecycle-exercises-001` (critical) — Closure missing TIBER-EU mandated artefacts
- `lifecycle-operations-003` (critical) — no purple-teaming close-out with Blue Team
- `lifecycle-threatscenarios-001` (critical) — no purple-team close-out described

Plus partial impact on `lifecycle-physoc-003` (critical) if patch 6 is applied.

That is **4 of 12 criticals + 2 of 63 highs + 1 of 62 mediums** removed in a single coordinated change.

## After applying

Re-run `/evaluate all` to confirm severity drop. The next coherence run will also flag any new drift introduced by the patches (none expected — the new doc uses the curated canonical names).
