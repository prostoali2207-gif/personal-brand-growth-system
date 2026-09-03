# Experiments

Experiment records preserve design locks and prevent retrospective rewriting.

Minimum record:

- `experiment_id`
- `owning_core`
- `decision_question`
- `hypothesis_refs`
- `units / population`
- `variants / intervention`
- `primary_metric / estimand`
- `guardrails`
- `attribution / measurement assumptions`
- `start / stop rules`
- `locked_fields`
- `status`: `draft | preregistered | running | stopped | completed | invalidated`
- `data_refs`
- `analysis_ref`
- `decision_ref`

Use the current Growth Experimentation & Measurement core for material experiment/measurement judgment. Do not change locked design fields after outcome visibility without recording the deviation.
