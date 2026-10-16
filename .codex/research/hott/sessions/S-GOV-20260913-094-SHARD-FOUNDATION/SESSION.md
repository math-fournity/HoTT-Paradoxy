# S-GOV-20260913-094-SHARD-FOUNDATION

- 用户要求：全局治理框架更新"长治理文档软分片与索引"后，本项目完成拆解改造且不影响未来工作；已确认边界见 `rulings.md` §17。
- 本轮动作（CP-1）：只建能力与合同，不迁移既有正文。runtime 3.3.0 解析 `governance-shard-index:v2`，把逻辑文档展开为
  "索引 + 按 table 顺序全部分片"，`check` 必须覆盖每一片，结构错误 fail closed；`MUTABLE` 文档分片进入 `HEAD.json.tracked`。
- 新增：`docs/quality/长治理文档分片与索引合同.md`、pin 的 v2 校验器副本与包装器、一次性迁移工具、5 条 runtime 负向测试。
- 保留：三件套、`HoTT/CLAIM_EVIDENCE_MATRIX.md`（行级 proof 收据耦合）、`AGENTS.md`、来源快照与历史交付分卷；触发条件写入合同 §7。
- 不改任何 KC、mathematical status、proof source/run/index；`AGENTS.md` 的 hash 仅因新增路由章节而 re-pin（带 revalidation）。
- 迁移（CP-2，revision 95）与本地 annotated `governance-v3.3.0` 待执行；不 push。
