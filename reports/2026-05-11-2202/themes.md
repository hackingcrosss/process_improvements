# Themes (run 2026-05-11-2202)

216 deduped findings across 9 artefacts cluster into the themes below. The new master deck (`RedTeaming_v1.0.pptx`) reinforces every existing theme rather than introducing new ones, with one additional internal-consistency cluster called out at the end.

Each theme heading notes whether the deck reinforces or contradicts the prose docs on that point.

## TIBER-EU / DORA TLPT misalignment (112 findings; 10 critical, 45 high, 34 medium, 10 low, 13 informational)

The dominant theme by volume. Across every prose document and the master deck the regulator-aligned vocabulary (TIBER-EU v2 phases — Preparation / TI / RTT / Closure — actor model with Control Team distinct from White Team, independent TI provider, TCT engagement, attestation, knowledge sharing, mutual recognition) is absent or implicit. Several findings continue to cite TIBER-EU v2 and DORA Art.26-27 'from memory' (confidence: low) and need verification against live text. **Deck status: reinforces.** The deck is silent on TIBER-EU / DORA TLPT entirely — no mention of 'TIBER', 'TLPT', 'lead overseer', 'attestation', 'mutual recognition' or 'control team' — while describing a full external-style kill-chain with C2 tooling. Risk: a leadership / audit audience may read the deck as a description of how Euronext does TLPT.

**Contributing finding ids:** lifecycle-threatscenarios-001, tdora-threatscenarios-001, tdora-threatscenarios-002, tdora-threatscenarios-003, tdora-threatscenarios-004, tdora-threatscenarios-005, tdora-threatscenarios-006, tdora-threatscenarios-007, lifecycle-operations-003, lifecycle-operations-004, lifecycle-operations-005, lifecycle-operations-007, lifecycle-operations-009, lifecycle-operations-010, lifecycle-operations-015, tdora-operations-001, tdora-operations-002, tdora-operations-003, tdora-operations-004, tdora-operations-005, tdora-operations-006, lifecycle-exercises-001, lifecycle-exercises-006, lifecycle-exercises-008, tdora-exercises-003, lifecycle-exercises-011, tdora-exercises-010, lifecycle-exercises-016, tdora-exercises-001, tdora-exercises-002, tdora-exercises-004, tdora-exercises-005, tdora-exercises-006, tdora-exercises-007, tdora-exercises-008, tdora-exercises-009, tdora-exercises-011, tdora-exercises-012, tdora-exercises-013, tdora-exercises-014, tdora-exercises-015, lifecycle-bhe-003, lifecycle-bhe-004, lifecycle-bhe-015, tdora-bhe-001, tdora-bhe-002, tdora-bhe-003, lifecycle-rtmeth-002, lifecycle-rtmeth-003, lifecycle-rtmeth-004, lifecycle-rtmeth-005, lifecycle-rtmeth-006, lifecycle-rtmeth-009, tdora-rtmeth-001, lifecycle-rtmeth-011, tdora-rtmeth-008, lifecycle-rtmeth-013, lifecycle-rtmeth-014, lifecycle-rtmeth-015, lifecycle-rtmeth-018, lifecycle-rtmeth-020, tdora-rtmeth-002, tdora-rtmeth-003, tdora-rtmeth-004, tdora-rtmeth-005, tdora-rtmeth-006, tdora-rtmeth-007, tdora-rtmeth-010, tdora-rtmeth-012, tdora-rtmeth-013, lifecycle-rtdeck-003, lifecycle-rtdeck-005, lifecycle-rtdeck-010, lifecycle-rtdeck-012, tdora-rtdeck-001, tdora-rtdeck-002, tdora-rtdeck-003, tdora-rtdeck-004, tdora-rtdeck-005, tdora-rtdeck-006, tdora-rtdeck-007, tdora-rtdeck-008, lifecycle-research-006, lifecycle-research-007, tdora-research-001, tdora-research-002, tdora-research-003, tdora-research-004, tdora-research-005, lifecycle-physoc-003, lifecycle-physoc-006, lifecycle-physoc-009, lifecycle-physoc-010, lifecycle-physoc-013, tdora-physoc-001, tdora-physoc-002, tdora-physoc-003, tdora-physoc-004, tdora-physoc-005, tdora-physoc-006, tdora-physoc-007, tdora-physoc-008, tdora-physoc-009, tdora-physoc-010, tdora-physoc-011, tdora-physoc-012, lifecycle-physocq-003, lifecycle-physocq-006, lifecycle-physocq-010, lifecycle-physocq-013, tdora-physocq-001, tdora-physocq-002

## Purple-team close-out (22 findings; 6 critical, 6 high, 6 medium, 2 low, 2 informational)

Mandatory purple-team close-out (replay, 360 feedback, conversion of red findings into hunt hypotheses / detection improvements) is missing or weak across the methodology, deck, Exercises, Operations, Threat Scenarios, BloodhoundEnterprise, and the physical SOP. For Threat Scenarios this is the most striking gap — joint blue-team participation is the defining feature of that engagement type per the team's own taxonomy. **Deck status: reinforces.** The deck does not name purple-teaming or close-out anywhere; only 'present remediation plan' is mentioned.

**Contributing finding ids:** lifecycle-threatscenarios-001, lifecycle-threatscenarios-014, tdora-threatscenarios-005, lifecycle-operations-003, tdora-operations-004, lifecycle-exercises-001, tdora-exercises-005, lifecycle-bhe-007, lifecycle-rtmeth-001, lifecycle-rtmeth-004, lifecycle-rtmeth-018, tdora-rtmeth-006, lifecycle-rtdeck-003, tdora-rtdeck-005, lifecycle-research-001, lifecycle-research-006, lifecycle-research-012, tdora-research-002, lifecycle-physoc-003, tdora-physoc-002, tdora-physoc-005, lifecycle-physocq-014

## Authorization / RoE clarity (27 findings; 5 critical, 11 high, 9 medium, 1 low, 1 informational)

Authorization chain, legal sign-off, RoE templates, kill-switch / abort criteria, safe-words, and evidence-handling rules are missing or implicit across most SOPs. For physical engagements there is no operator check-in / emergency-contact protocol — this is a personal-safety gap, not just paperwork. **Deck status: reinforces.** The deck's RoE bullet on slide 6 lists prohibitions and scope items but does not name authorization chain, kill-switch, safe-words or data handling.

**Contributing finding ids:** lifecycle-threatscenarios-002, lifecycle-threatscenarios-015, lifecycle-operations-002, lifecycle-operations-007, lifecycle-operations-009, lifecycle-operations-015, lifecycle-exercises-004, lifecycle-exercises-005, lifecycle-exercises-008, tdora-exercises-009, lifecycle-bhe-002, lifecycle-rtmeth-003, lifecycle-rtmeth-017, tdora-rtmeth-007, lifecycle-rtdeck-007, tdora-rtdeck-006, lifecycle-research-002, tdora-research-004, lifecycle-physoc-005, lifecycle-physoc-006, lifecycle-physoc-007, lifecycle-physoc-010, lifecycle-physoc-011, lifecycle-physoc-018, tdora-physoc-008, lifecycle-physocq-007, lifecycle-physocq-014

## Codename + theme convention (13 findings; 5 high, 1 medium, 5 low, 2 informational)

Methodology docs and the deck do not codify the codename + fictional-character theme convention (theme applies to Exercises and Operations; Threat Scenarios receive a codename without the theme constraint). Individual SOPs reference codenames inconsistently. **Deck status: reinforces.** The deck does not mention codenames or themes at all, despite being a master explainer.

**Contributing finding ids:** lifecycle-threatscenarios-008, lifecycle-threatscenarios-009, lifecycle-operations-002, lifecycle-exercises-003, lifecycle-exercises-014, tdora-exercises-015, lifecycle-bhe-016, lifecycle-rtmeth-002, lifecycle-rtdeck-002, lifecycle-research-014, lifecycle-physoc-002, tdora-physoc-012, lifecycle-physocq-014

## Threat-hunt handover & IR support remit (14 findings; 10 high, 1 medium, 1 low, 2 informational)

The team's adjacent activities — post-engagement threat-hunt handover, hunt support during external red-team-against-Euronext exercises, threat-hunt and IR support during live incidents — are absent from the methodology, the deck, and most SOPs. This understates the team's value and creates a documentation gap with SOC / IR. **Deck status: reinforces.** The deck mentions Red Eye logs but not the wider hunt / IR remit.

**Contributing finding ids:** lifecycle-threatscenarios-004, lifecycle-operations-004, lifecycle-exercises-002, lifecycle-bhe-008, lifecycle-bhe-018, lifecycle-rtmeth-005, lifecycle-rtmeth-006, lifecycle-rtdeck-004, lifecycle-research-007, lifecycle-research-008, lifecycle-physoc-004, lifecycle-physoc-016, lifecycle-physocq-010, lifecycle-physocq-014

## Physical scope completeness (34 findings; 2 critical, 19 high, 10 medium, 2 low, 1 informational)

Multiple SOPs are silent on whether physical attack paths are in or out of scope; the PhysicalSocial SOP itself lacks safety protocols, lacks TIBER-EU phase alignment for the physical leg, and has no purple-team close-out with physical security. **Deck status: reinforces.** The deck does not mention physical, social engineering, tailgating, badge cloning, or premises access anywhere.

**Contributing finding ids:** lifecycle-threatscenarios-007, lifecycle-operations-001, lifecycle-operations-008, lifecycle-exercises-004, lifecycle-bhe-013, lifecycle-rtmeth-007, lifecycle-rtdeck-005, lifecycle-research-009, lifecycle-physoc-001, lifecycle-physoc-003, lifecycle-physoc-004, lifecycle-physoc-006, lifecycle-physoc-007, lifecycle-physoc-008, lifecycle-physoc-009, lifecycle-physoc-011, lifecycle-physoc-016, lifecycle-physoc-018, tdora-physoc-001, tdora-physoc-002, tdora-physoc-003, tdora-physoc-004, tdora-physoc-005, tdora-physoc-006, tdora-physoc-007, tdora-physoc-009, tdora-physoc-011, lifecycle-physocq-001, lifecycle-physocq-002, lifecycle-physocq-003, lifecycle-physocq-008, lifecycle-physocq-009, lifecycle-physocq-011, tdora-physocq-001

## Engagement-type taxonomy clarity (12 findings; 4 high, 2 medium, 3 low, 3 informational)

The three-engagement taxonomy (Exercises / Operations / Threat Scenarios) is a strength when invoked, but several artefacts mix expectations across types. **Deck status: reinforces** (the deck does not enumerate the three types) **and contradicts** (slide 11 asserts 'Blue Team unaware' as a universal property — see the dedicated theme below).

**Contributing finding ids:** tdora-threatscenarios-001, lifecycle-exercises-014, lifecycle-bhe-001, lifecycle-rtmeth-001, lifecycle-rtmeth-004, tdora-rtmeth-013, lifecycle-rtdeck-001, lifecycle-rtdeck-006, lifecycle-research-001, lifecycle-research-012, tdora-research-002, lifecycle-physoc-001

## Reporting & remediation tracking (21 findings; 2 critical, 9 high, 7 medium, 2 low, 1 informational)

Reporting model (finding taxonomy, severity scale, evidence retention) and remediation tracking / lessons-learned capture are under-described. **Deck status: reinforces.** The deck names 'Report of activities' as an RT duty but does not describe the severity model or remediation tracker.

**Contributing finding ids:** lifecycle-threatscenarios-005, lifecycle-threatscenarios-006, lifecycle-threatscenarios-013, lifecycle-operations-005, lifecycle-operations-006, lifecycle-exercises-001, lifecycle-exercises-006, lifecycle-exercises-007, lifecycle-exercises-015, tdora-exercises-005, lifecycle-bhe-006, lifecycle-bhe-014, lifecycle-rtmeth-005, lifecycle-rtmeth-008, lifecycle-rtmeth-009, lifecycle-rtdeck-013, lifecycle-rtdeck-016, lifecycle-research-012, lifecycle-physoc-003, lifecycle-physoc-014, lifecycle-physocq-014

## Diagram & visual readability (15 findings; 4 high, 5 medium, 5 low, 1 informational)

Several prose SOPs reference figures the ingest pipeline could not render. The deck has the inverse problem: 15 of 27 slides are `[chart-or-smartart]` placeholders, with phase numbering (Phases 0-4) shown only inside visuals and no prose caption. This is both a content-readability concern and a documentation gap — the team's visual story is not captured in text.

**Contributing finding ids:** lifecycle-threatscenarios-011, lifecycle-operations-011, lifecycle-operations-012, lifecycle-operations-014, lifecycle-exercises-012, tdora-exercises-012, lifecycle-bhe-017, lifecycle-rtdeck-011, lifecycle-rtdeck-012, lifecycle-rtdeck-014, tdora-rtdeck-004, lifecycle-research-013, lifecycle-physoc-001, lifecycle-physocq-003, lifecycle-physocq-011

## Safety, OPSEC & data protection (28 findings; 5 critical, 9 high, 13 medium, 1 low)

Cross-cutting OPSEC and safety gaps: PIA (US 'Privacy of Information Act') referenced in two methodology docs instead of GDPR / DORA; classification labels missing on the master deck despite C2-tooling detail; operators named by individual on the deck despite it being a persistent explainer; no operator check-in protocol for physical engagements.

**Contributing finding ids:** lifecycle-threatscenarios-002, lifecycle-threatscenarios-010, tdora-threatscenarios-007, lifecycle-operations-009, lifecycle-exercises-005, lifecycle-exercises-010, tdora-exercises-010, tdora-exercises-009, lifecycle-bhe-003, lifecycle-bhe-009, lifecycle-bhe-017, lifecycle-rtmeth-003, lifecycle-rtmeth-011, tdora-rtmeth-008, lifecycle-rtmeth-020, tdora-rtmeth-004, tdora-rtmeth-007, tdora-rtmeth-012, lifecycle-rtdeck-007, tdora-rtdeck-006, lifecycle-research-003, lifecycle-research-015, tdora-research-004, lifecycle-physoc-005, lifecycle-physoc-012, tdora-physoc-008, tdora-physoc-009, lifecycle-physocq-003

## Document governance (owner/version/classification) (17 findings; 7 high, 5 medium, 4 low, 1 informational)

Several artefacts lack an owner, review cadence, or classification label. The deck in particular carries no visible classification marking yet documents operator names and Cobalt Strike infrastructure.

**Contributing finding ids:** lifecycle-threatscenarios-005, tdora-threatscenarios-004, lifecycle-exercises-006, lifecycle-exercises-007, lifecycle-exercises-017, lifecycle-exercises-018, lifecycle-bhe-003, lifecycle-bhe-006, lifecycle-bhe-015, lifecycle-rtmeth-009, lifecycle-rtdeck-015, lifecycle-research-010, lifecycle-research-011, lifecycle-physoc-014, tdora-physoc-005, lifecycle-physocq-002, tdora-physocq-002

## Other / long-tail (20 findings; 2 high, 10 medium, 7 low, 1 informational)

Single findings not clustering with the above (e.g. trailing blank slides on the deck, tool-specific operational detail in BloodhoundEnterprise). Captured in the register; not material at the theme level.

**Contributing finding ids:** lifecycle-threatscenarios-003, lifecycle-threatscenarios-012, lifecycle-threatscenarios-016, lifecycle-operations-013, lifecycle-operations-016, lifecycle-bhe-005, lifecycle-bhe-010, lifecycle-bhe-011, lifecycle-bhe-012, lifecycle-rtmeth-016, lifecycle-rtmeth-019, lifecycle-rtdeck-008, lifecycle-rtdeck-009, lifecycle-research-004, lifecycle-research-005, lifecycle-physoc-015, lifecycle-physoc-017, lifecycle-physocq-004, lifecycle-physocq-005, lifecycle-physocq-012

## Deck contradicts engagement-type taxonomy (new for this run)

The master deck (`RedTeaming_v1.0.pptx`) describes red teaming as if the team only ran one engagement shape: full external-style kill-chain with the blue team unaware. Slide 11 states `'Blue Team (BT): TBD — Unaware of the exercise, must carry-on with normal activities.'` as a general property. This is inconsistent with the team's own taxonomy as captured in the prose SOPs:

- **Threat Scenarios** are by design **collaborative walk-throughs** with the blue team in the room (per `ThreatScenarios_Process_v1.1.docx`).
- **Operations** are partially-stealth assumed-breach engagements with deconfliction mechanics (per `Operations_Process_v1.0.docx`).
- **Exercises** are the only engagement type for which 'blue team unaware' is a defining property.

The deck additionally names specific operators ('Renato Cruz and José Barbosa') on slide 11 — appropriate for a per-engagement RoE artefact, not for a persistent master explainer that fronts the team to internal and audit audiences. Together these slides risk codifying the wrong picture of what the team does.

**Contributing finding ids:** lifecycle-threatscenarios-001, lifecycle-threatscenarios-003, lifecycle-threatscenarios-012, tdora-threatscenarios-005, lifecycle-rtdeck-001, lifecycle-rtdeck-006, lifecycle-rtdeck-010
