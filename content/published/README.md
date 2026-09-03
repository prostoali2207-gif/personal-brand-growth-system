# Published content registry

Record only content that is confirmed published.

Minimum record:

- `published_id`
- `brief_id`
- `channel_id`
- `platform_content_id / URL`
- `published_at`
- `exact_asset_or_copy_ref`
- `claim_refs`
- `experiment_id` if applicable
- `publication_evidence`
- `status`: `live | removed | edited | unknown`
- `last_verified_at`

A draft, scheduled item, upload attempt, or tool response without observable publication confirmation is not `published`.
