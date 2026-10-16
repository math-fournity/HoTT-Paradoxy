# S-RES-20260913-087-N41-BATCH12

- N41（第一项）：第十二批按比例抽样 40 条（B3/全量精读工作方案/B4/A0/A1/A2/B1/读遍账本 各 5）。
- 判词：`SUPPORTED=20`、`SUPERSEDED_BY_MACHINE_RESULT=2`、`UNSUPPORTED=0`、`PENDING=18`；十二批累计 `482/2,396`（20.1%）：`308/14/0/160`。
- 两条历史条目由机器结果接管：`CL-001048`（一般因子化条件句 → `MP-ERCF-001` C-59–C-66）、`CL-001564`（RP-B01/race-timeout 历史未执行 → `MP-RACE-TIMEOUT-001` C-71–C-76 + N2 审计 PARKED）。
- 现场/机器复核：workspace 44 SESSION/9 PROOF_NOTE/10 reviews ✓；`workspace/artifacts` r006–r015 缺失（archive 边界）✓；`4,330` 与 `FINITE_MODEL_RESULTS.json` 一致 ✓；Gemini 24/24 ✓；`r024_diagonal_machine.py` 存在 ✓。
- 两处口径差记账（不静默修正历史）：`CL-000994`（2,091 vs 2,087 源；2,006 片段一致）；`CL-002292`（账本 238 行 vs `wc -l` 237 行）。
- E6 十二批一致未出现；判词仍为 `DEFENSE_WORKS / REPRESENTATION_BOUNDARY`；不新增数学 claim、不改 claim ledger 与理解章节正文。
- 本轮恢复并保存 36/36 逐 KC 回评（`CORE_COGNITION_AUDIT.md`）；`core_change=NO`。
- 下一工作包 N42：第十三批抽样，或 T3 共享判定联合递归（ERCF-3 保持 gated）。
