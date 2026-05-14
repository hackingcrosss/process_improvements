# Themes — run 2026-05-12-1914

**Total findings (deduped):** 54. **Themes (≥2 findings):** 10.

## Purple-team close-out follow-ups (version pinning, Euronext role mapping)

_10 findings (medium:7, low:2, informational:1)_

-  **medium** — Cross-reference 'Purple Teaming Process document' (unversioned) — doc now exists but reference is not version-pinned  *(methodology-docs-redteam-methodology-v0-6-docx)*
-  **medium** — New Purple Teaming Process doc uses 'vX.docx' placeholders in References  *(engagements-3-purple-teaming-docs-purple-teaming-process-v0-1-docx)*
-  **medium** — Purple Team Close-Out cross-reference unversioned  *(Exercises_Process_v1.4.docx)*
-  **medium** — Purple Team Close-Out cross-reference unversioned  *(Operations_Process_v1.3.docx)*
-  **medium** — Purple Team Close-Out cross-reference unversioned (same pattern as cyber SOPs)  *(PhysicalSocial_Process_v1.1.docx)*
-  **medium** — Purple Teaming Process cross-reference still unversioned  *(RedTeam_Methodology_v0.6.docx)*
-  **medium** — Purple-team close-out subsection added but cross-reference 'Purple Teaming Process documentation' is unversioned  *(ThreatScenarios_Process_v1.4.docx)*
-  **low** — Typo: 'Feeback' should be 'Feedback' (subsection heading)  *(Research_Methodology_v0.4.docx)*
-  **low** — Stakeholder deck does not reflect v0.6 methodology updates (Codename theme, Purple-team mandatory phase, OFI glossary)  *(methodology-redteaming-v1-0-pptx)*
-  **informational** — v0.3 -> v0.6 closed multiple Tier 1 findings (Codename theme, Bag of Tricks, Tools repository naming, OFI glossary, Purple Team reference)  *(RedTeam_Methodology_v0.6.docx)*

## Other / general process-quality findings

_9 findings (high:2, medium:3, low:3, informational:1)_

-  **high** — Section opens 'two main teams' but describes three (RT, BT, WT)  *(Operations_Process_v1.3.docx)*
-  **high** — No Teams & Responsibilities section: WT, BT and TI roles not defined for Threat Scenarios  *(ThreatScenarios_Process_v1.4.docx)*
-  **medium** — Codename register location not specified  *(RedTeam_Methodology_v0.6.docx)*
-  **medium** — Strong skeleton; lacks Euronext-specific role mapping (named owners / tracking forum URL)  *(Purple_Teaming_Process_v0.1.docx)*
-  **medium** — Stakeholder deck (RedTeaming v1.0.pptx) does not reflect v0.6 methodology updates  *(RedTeaming_v1.0.pptx)*
-  **low** — 'SOC team should be warned' but no formal notification mechanism  *(BloodhoundEnterprise_Process_v0.3.docx)*
-  **low** — References use 'vX.docx' placeholders  *(Purple_Teaming_Process_v0.1.docx)*
-  **low** — Useful Links list repository names but no live URLs / paths  *(Research_Methodology_v0.4.docx)*
-  **informational** — Tracking forum left generic in v0.1  *(Purple_Teaming_Process_v0.1.docx)*

## TIBER-EU / DORA TLPT regulatory mapping

_8 findings (high:3, medium:2, low:1, informational:2)_

-  **high** — TIBER-EU role mapping (TLPT Authority, Control Team, TI Provider, RT Provider) not made explicit in Initiation  *(Exercises_Process_v1.4.docx)*
-  **high** — TIBER-EU role taxonomy not explicitly mapped to internal roles  *(Exercises_Process_v1.4.docx)*
-  **high** — Methodology does not expand TLPT / TIBER-EU / CBEST or map engagement types to regulator-mandated tests  *(RedTeam_Methodology_v0.6.docx)*
-  **medium** — TIBER-EU artefact checklist incomplete despite improvements  *(Exercises_Process_v1.4.docx)*
-  **medium** — TIBER-EU role taxonomy referenced at attestation only; not expanded with internal mapping  *(Purple_Teaming_Process_v0.1.docx)*
-  **low** — Methodology v0.6 still uses 'TIBER-Like' rather than expanding TLPT / TIBER-EU  *(methodology-docs-redteam-methodology-v0-6-docx)*
-  **informational** — Operations correctly out of TIBER-EU / DORA TLPT scope (opportunistic assumed-breach)  *(Operations_Process_v1.3.docx)*
-  **informational** — Threat Scenarios correctly out of TIBER-EU / DORA TLPT scope (objective-oriented, BT-collaborative, internal-tool focus)  *(ThreatScenarios_Process_v1.4.docx)*

## Cross-doc naming drift (One Note, Bloodhound, PoC, Sharphound)

_7 findings (high:1, medium:3, low:3)_

-  **high** — Naming drift: 'One Note' in methodology v0.6 OPLOGS section; three SOPs already fixed to 'OneNote'  *(methodology-docs-redteam-methodology-v0-6-docx)*
-  **medium** — Naming drift: 'Bloodhound' (lowercase 'h') in Ops v1.3; BH v0.3 already uses 'BloodHound' canonical  *(engagements-1-operations-docs-operations-process-v1-3-docx)*
-  **medium** — 'Bloodhound' (lowercase 'h') in prose; canonical is 'BloodHound'  *(Operations_Process_v1.3.docx)*
-  **medium** — 'One Note' still in OPLOGS section (line 129); canonical is 'OneNote'  *(RedTeam_Methodology_v0.6.docx)*
-  **low** — Naming drift: 'Sharphound' (lowercase 'h') one occurrence in BH v0.3 line 7  *(methodology-docs-bloodhoundenterprise-process-v0-3-docx)*
-  **low** — 'Sharphound' (lowercase 'h') used in line 7; vendor canonical is 'SharpHound'  *(BloodhoundEnterprise_Process_v0.3.docx)*
-  **low** — Versioning table credits 'Generated draft' as author  *(Purple_Teaming_Process_v0.1.docx)*

## Authorization, RoE and kill-switch (Tier 1.2 — DORA defensibility)

_5 findings (critical:4, high:1)_

-  **critical** — Authorization phase still implicit: no named legal sign-off, no kill-switch / abort criteria, no safe-words  *(Exercises_Process_v1.4.docx)*
-  **critical** — Authorization phase implicit: no legal sign-off, no RoE artefact, no safe-words, no kill-switch / abort criteria  *(Operations_Process_v1.3.docx)*
-  **critical** — Authorization phase still absent: no legal sign-off, no RoE artefact, no kill-switch, no safe-words, no abort criteria  *(ThreatScenarios_Process_v1.4.docx)*
-  **critical** — Authorization chain, kill-switch and safe-words still not defined in the methodology  *(RedTeam_Methodology_v0.6.docx)*
-  **high** — Authorization chain not described at engagement level  *(PhysicalSocial_Process_v1.1.docx)*

## Acronym disambiguation and undefined acronyms (PoC, VRC, CMDB, AET, IST, CTI)

_4 findings (high:2, medium:2)_

-  **high** — Acronym conflict: 'WT PoC' / 'RT PoC' in Exercises v1.4 Deconfliction; Operations v1.3 was rewritten to full form  *(engagements-2-exercises-docs-exercises-process-v1-4-docx)*
-  **high** — 'VRC' acronym used in Questionnaire section without expansion  *(PhysicalSocial_Process_v1.1.docx)*
-  **medium** — 'WT PoC' / 'RT PoC' still used in Exercises Deconfliction — Operations was rewritten, Exercises missed  *(Exercises_Process_v1.4.docx)*
-  **medium** — 'CMDB' used as load-bearing input without definition  *(PhysicalSocial_Questionnaire_Process_v1.0.docx)*

## Operator safety (physical engagements)

_3 findings (critical:1, medium:2)_

-  **critical** — Operator safety protocol still absent: no scheduled check-ins, no abort/kill-switch wording, no emergency contacts  *(PhysicalSocial_Process_v1.1.docx)*
-  **medium** — LLM-assisted scenario generation mentioned but no data-handling rules / vendor restrictions  *(ThreatScenarios_Process_v1.4.docx)*
-  **medium** — AI Enrichment layer described but no rule about what may be submitted to public LLMs  *(Research_Methodology_v0.4.docx)*

## External actor / SOC interface (orphan actors)

_3 findings (medium:3)_

-  **medium** — AET acronym in curated vocab but still no charter doc  *(methodology-docs-bloodhoundenterprise-process-v0-3-docx)*
-  **medium** — Orphan actors still present: CSIRT, L1/L2/L3, Pentest/Assessment in SOC-RT comms diagram  *(resources-diagrams-soc-rt-communications-drawio)*
-  **medium** — AET expansion now in curated vocab but no charter doc defines AET's responsibilities or relationship to RT  *(BloodhoundEnterprise_Process_v0.3.docx)*

## Lessons-learned / knowledge-base capture

_3 findings (low:3)_

-  **low** — Lessons-learned capture step still absent  *(Exercises_Process_v1.4.docx)*
-  **low** — Lessons-learned capture mechanism still not described separately  *(Operations_Process_v1.3.docx)*
-  **low** — Threat-hunt handover and lessons-learned capture mechanism not described separately  *(ThreatScenarios_Process_v1.4.docx)*

## Methodology coverage gaps (Tier model, Ancillary remit, Modality index)

_2 findings (medium:2)_

-  **medium** — Methodology index incomplete: does not reference PhysSoc, Research Methodology, or BloodHound process docs  *(methodology-docs-redteam-methodology-v0-6-docx)*
-  **medium** — Methodology does not cover Physical & Social engagements as a fourth modality  *(RedTeam_Methodology_v0.6.docx)*
