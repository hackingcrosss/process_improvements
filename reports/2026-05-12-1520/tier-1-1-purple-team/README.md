# Tier 1.1 packet — Purple-team close-out

This packet implements the highest-leverage structural fix from the 2026-05-12-1520 review: closing the methodology-vs-SOP gap on purple teaming. **4 of the 12 critical findings collapse in a single coordinated change.**

## Files

- `Purple_Teaming_Process_v0.1.docx` — new process doc. Drop into `inputs/Methodology/`.
- `patch-instructions.md` — exact text to add to each engagement SOP + the methodology version-pin update.

## Quick start

1. Open `patch-instructions.md` and work through the 5 patches in order (the 6th is optional but recommended).
2. Drop the new `.docx` into `inputs/Methodology/`.
3. Re-run `/evaluate all` to confirm the severity drop.

## Why this first

- Methodology promises purple-team close-out for every engagement type; the three SOPs currently don't implement it (coherence findings -005, -009).
- Cross-reference to a `Purple Teaming Process document` is broken — no such doc exists (finding -006).
- Per-artefact evaluator flagged this as critical on all three SOPs and the methodology deck (findings `lifecycle-rtdeck-003`, `lifecycle-exercises-001`, `lifecycle-operations-003`, `lifecycle-threatscenarios-001`).
- The new doc itself uses curated vocabulary (Blue Team, Threat Intelligence Team, Red Team, TI, OFI, Tier 0/1/2 references...) so it doesn't introduce new drift.

## After this, Tier 1.2 (next)

Authorization chain / kill-switch / safe-words / abort criteria. Removes another 3 criticals across the SOPs and the methodology, and is the DORA Art. 26-27 defensibility ask.
