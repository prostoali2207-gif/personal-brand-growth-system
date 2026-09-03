# Professional-core handoffs

Use one handoff record for each material transfer of responsibility between professional cores.

Recommended filename: `<date>-<from>-to-<to>-<topic>.md`.

## Required handoff fields

- `handoff_id`
- `created_at`
- `from_core` + exact version/status
- `to_core` + exact version/status
- `task`
- `authoritative_inputs`
- `verified_facts / approved_claims`
- `upstream_decision_refs`
- `locked_constraints`
- `unknowns / conflicts`
- `authority_boundary`
- `requested_output`
- `output_location`
- `evidence / provenance refs`
- `acceptance_status`: `pending | accepted | rejected | needs_clarification`

## Rule

The sender transfers evidence and constraints, not professional authority outside the receiving core's scope. The receiver must surface missing decision-critical information instead of filling it with assumptions.
