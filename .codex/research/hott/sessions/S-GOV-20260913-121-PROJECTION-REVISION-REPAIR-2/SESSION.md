# S-GOV-20260913-121-PROJECTION-REVISION-REPAIR-2

- 类型：corrective（治理修正）。
- 起因：`S-GOV-20260913-120-PROJECTION-REVISION-REPAIR` 把投影 index 写成 `source_state_revision: 119` 却又把 `STATE.revision` bump 到 120，
  `verify_three_way_cognition` 报 `DIRECTION_STATE_REVISION_STALE`。
- 修正：`方向追踪.md` / `全景视野.md` 的 `source_state_revision` 与 `projection_generation` 各一行；
  内容、判词、claim、run 均不变。
- 先例：S105/S106（C11 v2 修订 + corrective 重绑），"修正走新 checkpoint，不改写已应用事务"。
- 交付不变：`audit/统观工作技术报告-20260913.md`（`A-PROJECTION-REVISION-REPAIR-002` 仍为 S119 产物；本会话只登记修正本身）。
