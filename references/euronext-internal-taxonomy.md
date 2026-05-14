---
purpose: Placeholder for the Euronext internal risk/audit/control taxonomy. Replace this content with the actual taxonomy so the tiber-dora-alignment and other evaluators can tag findings with internal control IDs in addition to external framework refs.
status: PLACEHOLDER — populate before relying on EURONEXT-INTERNAL framework_refs
---

# Internal taxonomy (TO POPULATE)

When you fill this in, evaluators will use it to add `framework_refs` entries with `framework: EURONEXT-INTERNAL` and `ref: <your control id>`. Suggested structure:

## Control families
- (e.g.) `RT-METH-*` — Red team methodology controls
- (e.g.) `RT-OPS-*` — Engagement execution controls
- (e.g.) `RT-RPT-*` — Reporting and remediation tracking
- (e.g.) `RT-RND-*` — Research / tradecraft / tooling
- (e.g.) `RT-PHY-*` — Physical security engagement controls
- (e.g.) `RT-IRSUP-*` — Incident response and threat-hunt support

## Per-control entry shape
```
- id: RT-METH-007
  title: Engagement codename assignment
  description: Every engagement is assigned a unique codename per the team theme convention prior to authorization.
  owner: Red team lead
  evidence_expected: Codename register entry, RoE document header
```
