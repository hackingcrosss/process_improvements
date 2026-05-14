# Quick-win review packets — run 2026-05-12-1520

Annotated copies of each affected source `.docx` with the quick-win edits flagged inline.

## How to use

1. Open each `*_REVIEW.docx` in Microsoft Word.
2. Each yellow-highlighted paragraph prefixed `[REVIEW]` or `[RENAME HEADING]` or `[ADD HERE]` describes one change to apply directly above it (or where indicated).
3. After making the edit, delete the yellow paragraph.
4. The companion `*_changelist.md` next to each doc lists every change so you can use it as a checklist or audit trail.
5. Annotations are sourced from `findings/_corpus/corpus-coherence.json` (curated mode) — each one cites the originating finding id (e.g. `Coherence finding -005`) so you can trace back if needed.

## Files

| # | Source doc | Annotated copy | Annotations | Checklist |
|---|---|---|---|---|
| 1 | `BloodhoundEnterprise_Process_v0.1.docx` | [`BloodhoundEnterprise_Process_v0.1_REVIEW.docx`](./BloodhoundEnterprise_Process_v0.1_REVIEW.docx) | 3 | [`BloodhoundEnterprise_Process_v0.1_REVIEW_changelist.md`](./BloodhoundEnterprise_Process_v0.1_REVIEW_changelist.md) |
| 2 | `Exercises_Process_v1.1.docx` | [`Exercises_Process_v1.1_REVIEW.docx`](./Exercises_Process_v1.1_REVIEW.docx) | 4 | [`Exercises_Process_v1.1_REVIEW_changelist.md`](./Exercises_Process_v1.1_REVIEW_changelist.md) |
| 3 | `Operations_Process_v1.0.docx` | [`Operations_Process_v1.0_REVIEW.docx`](./Operations_Process_v1.0_REVIEW.docx) | 9 | [`Operations_Process_v1.0_REVIEW_changelist.md`](./Operations_Process_v1.0_REVIEW_changelist.md) |
| 4 | `PhysicalSocial_Process_v1.0.docx` | [`PhysicalSocial_Process_v1.0_REVIEW.docx`](./PhysicalSocial_Process_v1.0_REVIEW.docx) | 1 | [`PhysicalSocial_Process_v1.0_REVIEW_changelist.md`](./PhysicalSocial_Process_v1.0_REVIEW_changelist.md) |
| 5 | `RedTeam_Methodology_v0.3.docx` | [`RedTeam_Methodology_v0.3_REVIEW.docx`](./RedTeam_Methodology_v0.3_REVIEW.docx) | 5 | [`RedTeam_Methodology_v0.3_REVIEW_changelist.md`](./RedTeam_Methodology_v0.3_REVIEW_changelist.md) |
| 6 | `Research_Methodology_v0.2.docx` | [`Research_Methodology_v0.2_REVIEW.docx`](./Research_Methodology_v0.2_REVIEW.docx) | 17 | [`Research_Methodology_v0.2_REVIEW_changelist.md`](./Research_Methodology_v0.2_REVIEW_changelist.md) |
| 7 | `ThreatScenarios_Process_v1.1.docx` | [`ThreatScenarios_Process_v1.1_REVIEW.docx`](./ThreatScenarios_Process_v1.1_REVIEW.docx) | 5 | [`ThreatScenarios_Process_v1.1_REVIEW_changelist.md`](./ThreatScenarios_Process_v1.1_REVIEW_changelist.md) |

## Notes

- Annotations are **inserted paragraphs**, not native Word comments — they show up in-line under the affected text, yellow-highlighted, with dark-red text. This makes them visible in any Word version and easy to delete after the change is applied.
- `Cyberark.Corp.Safeadmins` (literal AD object name in `BloodhoundEnterprise_Process`) is intentionally **not** rewritten — it is a real identifier in Active Directory, not prose.
- The `apts-apts-private.pptx` slide deck and `RedTeaming_v1.0.pptx` are not in this packet because the quick-win edits there are minor cosmetic (e.g. `Cobalt Strike` casing on the methodology slide deck) and the cost of round-tripping `.pptx` annotations is higher; suggest applying those directly when you re-export the decks.
- For "add subsection" / "add at end" annotations, the suggested text is in the yellow paragraph; copy-paste it into the doc, format to match the existing style, then delete the yellow paragraph.

_All seven annotated docs + checklists live in `reports/2026-05-12-1520/annotated-docs/`._