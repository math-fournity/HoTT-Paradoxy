# S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT

- 触发：S031 后原生 proof task plan 成功，但 `review_required` 包含 result 与 F-011 Gate。
- 根因：全量 source-hash 审计只发现 `HoTT/formal/README.md`、`HoTT/verification/runs/README.md` 仍是 S030 值；二者已由 S031 合法更新。
- 修复：只同步这两个 hash，并修正 S031 preparer；proof source/run/matrix/toolchain 不改。
- 预期验收：`A-ERCF-TRUNCATION-DEFENSE-001` plan 成功且 `review_required=[]`；旧 Lean/native exact replay 均通过。
- 数学状态：C-67–C-70 仍为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS`；不是悖论。
- 三件套：无语义变化，只同步 revision 32/generation 016；core 不变。
- Git：未 commit、未 tag、未 push。
