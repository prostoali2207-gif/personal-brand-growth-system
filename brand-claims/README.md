# Brand claim ledger

This ledger controls what may be asserted publicly about the person, work, projects, capabilities and results.

Recommended one record per claim or tightly coupled claim family.

## Minimum claim record

- `claim_id`
- `claim_text`
- `claim_type`: `identity | role | capability | project | result | metric | process | other`
- `scope`
- `evidence_refs`
- `evidence_strength`: `direct | corroborated | limited`
- `status`: `candidate | approved | rejected | superseded | expired`
- `approved_public_wording`: optional; must not exceed the evidence
- `limitations`
- `approved_by`
- `approved_at`
- `review_by`: when freshness matters

Only `approved` claims may be treated as reusable public brand facts. `candidate` means plausible/under review, not publishable truth.
