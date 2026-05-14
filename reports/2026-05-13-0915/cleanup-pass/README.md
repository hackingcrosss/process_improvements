# Cleanup-pass review packet — run 2026-05-13-0915

Annotated copies of every doc with S-effort residuals from the `2026-05-12-1914` corpus-coherence run. Each annotation is a single concrete edit you can apply directly in Microsoft Word.

## How to use

1. Open each `*_REVIEW.docx` in Microsoft Word.
2. Each yellow-highlighted paragraph prefixed `[REVIEW]`, `[RENAME HEADING]`, or `[ADD HERE]` describes one change to apply directly above it (or where indicated).
3. After making the edit, delete the yellow paragraph.
4. The companion `*_changelist.md` next to each doc lists every change so you can use it as a checklist or audit trail.
5. Annotations cite the originating coherence finding id (e.g. `Coherence finding -005`) so you can trace back to `findings/_corpus/corpus-coherence.json`.

## Files

| # | Source doc | Annotated copy | Annotations | Checklist |
|---|---|---|---|---|
| 1 | `BloodhoundEnterprise_Process_v0.3.docx` | [`BloodhoundEnterprise_Process_v0.3_REVIEW.docx`](./BloodhoundEnterprise_Process_v0.3_REVIEW.docx) | 1 | [`BloodhoundEnterprise_Process_v0.3_REVIEW_changelist.md`](./BloodhoundEnterprise_Process_v0.3_REVIEW_changelist.md) |
| 2 | `Research_Methodology_v0.4.docx` | [`Research_Methodology_v0.4_REVIEW.docx`](./Research_Methodology_v0.4_REVIEW.docx) | 1 | [`Research_Methodology_v0.4_REVIEW_changelist.md`](./Research_Methodology_v0.4_REVIEW_changelist.md) |
| 3 | `RedTeam_Methodology_v0.6.docx` | [`RedTeam_Methodology_v0.6_REVIEW.docx`](./RedTeam_Methodology_v0.6_REVIEW.docx) | 5 | [`RedTeam_Methodology_v0.6_REVIEW_changelist.md`](./RedTeam_Methodology_v0.6_REVIEW_changelist.md) |
| 4 | `Operations_Process_v1.3.docx` | [`Operations_Process_v1.3_REVIEW.docx`](./Operations_Process_v1.3_REVIEW.docx) | 3 | [`Operations_Process_v1.3_REVIEW_changelist.md`](./Operations_Process_v1.3_REVIEW_changelist.md) |
| 5 | `Exercises_Process_v1.4.docx` | [`Exercises_Process_v1.4_REVIEW.docx`](./Exercises_Process_v1.4_REVIEW.docx) | 2 | [`Exercises_Process_v1.4_REVIEW_changelist.md`](./Exercises_Process_v1.4_REVIEW_changelist.md) |
| 6 | `ThreatScenarios_Process_v1.4.docx` | [`ThreatScenarios_Process_v1.4_REVIEW.docx`](./ThreatScenarios_Process_v1.4_REVIEW.docx) | 1 | [`ThreatScenarios_Process_v1.4_REVIEW_changelist.md`](./ThreatScenarios_Process_v1.4_REVIEW_changelist.md) |
| 7 | `PhysicalSocial_Process_v1.1.docx` | [`PhysicalSocial_Process_v1.1_REVIEW.docx`](./PhysicalSocial_Process_v1.1_REVIEW.docx) | 2 | [`PhysicalSocial_Process_v1.1_REVIEW_changelist.md`](./PhysicalSocial_Process_v1.1_REVIEW_changelist.md) |
| 8 | `PhysicalSocial_Questionnaire_Process_v1.0.docx` | [`PhysicalSocial_Questionnaire_Process_v1.0_REVIEW.docx`](./PhysicalSocial_Questionnaire_Process_v1.0_REVIEW.docx) | 1 | [`PhysicalSocial_Questionnaire_Process_v1.0_REVIEW_changelist.md`](./PhysicalSocial_Questionnaire_Process_v1.0_REVIEW_changelist.md) |
| 9 | `Purple_Teaming_Process_v0.1.docx` | [`Purple_Teaming_Process_v0.1_REVIEW.docx`](./Purple_Teaming_Process_v0.1_REVIEW.docx) | 2 | [`Purple_Teaming_Process_v0.1_REVIEW_changelist.md`](./Purple_Teaming_Process_v0.1_REVIEW_changelist.md) |

**Total: 18 annotations across 9 documents.**

## Source findings

All annotations trace back to `findings/_corpus/corpus-coherence.json` (12 findings, curated mode, 2026-05-12-1914 run). Mapping:

- `coherence-001` → `One Note` → `OneNote` (RedTeam_Methodology v0.6)
- `coherence-002` → `Bloodhound` → `BloodHound` (Operations v1.3)
- `coherence-003` → `WT PoC` / `RT PoC` → spelled out (Exercises v1.4)
- `coherence-004` → `Sharphound` → `SharpHound` (BloodHound v0.3)
- `coherence-005` → pin `Purple_Teaming_Process_v0.1.docx` cross-references (5 docs)
- `coherence-006` → fix `vX.docx` placeholders (Purple Teaming v0.1)
- `coherence-007` → add 'Index of process documents' subsection (RedTeam_Methodology v0.6)
- `coherence-008` → mention Physical & Social as fourth modality (RedTeam_Methodology v0.6)
- `coherence-012` → expand `TIBER-Like` → `TLPT / TIBER-EU` (RedTeam_Methodology v0.6)

Plus two cleanup-pass items not in the coherence findings:
- `Feeback` typo in Research_Methodology v0.4 heading
- `VRC` / `CMDB` first-use expansion in PhysSoc docs
- "two main teams" → "three main teams" contradiction in Operations v1.3

## Notes

- Annotations are **inserted paragraphs**, not native Word comments — yellow-highlighted, dark-red bold text, indented. Same convention as the `2026-05-12-1520` packet. They render the same in every Word version and are trivial to delete after the change is applied.
- Out of scope for this packet (carried over to next tier):
  - `coherence-009` (AET acronym — needs charter doc, Tier 3)
  - `coherence-010` (stakeholder pptx refresh, Tier 2)
  - `coherence-011` (drawio orphan actors, Tier 3)
- After applying all edits, bump versions: BloodHound v0.3 → v0.4, Research v0.4 → v0.5, Methodology v0.6 → v0.7, Operations v1.3 → v1.4, Exercises v1.4 → v1.5, ThreatScenarios v1.4 → v1.5, PhysSoc v1.1 → v1.2, PhysSoc Questionnaire v1.0 → v1.1, Purple Teaming v0.1 → v0.2. Then re-run `/evaluate all` — expect remaining critical/high count to drop further.

_All nine annotated docs + checklists live in `reports/2026-05-13-0915/cleanup-pass/`._
