# S-GOV-20260913-096-PROJECTION-SHARD-MIGRATION

- 用户审查分片现状后说“开始第二波”，授权见 `rulings.md` §18（合同 §7 要求的三件套迁移必须由用户明确发起）。
- 迁移：`方向追踪.md` → 5 片（28 条方向行按家族分配）；`全景视野.md` → 8 片（89 条结果行按家族分配，含 1 行跨块归位）。
- 关键规则：原文头部（marker/`source_state_revision`/`projection_generation`/`semantic_status`）留在索引；行分片自带表头两行，
  对账证明“每行恰好一次、表头重复数 = 行分片数 − 1”；工具 `migrate_projection_shards.py`，编辑 helper `projection_edit.py`。
- 消费端强化：`verify_three_way_cognition.py` 按逻辑文本解析 `DIR-*`/`OUT-*` 并新增 0/0 与缺片 fail-closed；`test_three_way_cognition.py` 新增分片用例。
- 不改任何 KC、数学判词、proof source/run/index；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 保持单文件。
- 本地 annotated `governance-v3.4.0` 指向本 checkpoint 后的 commit；不 push。
