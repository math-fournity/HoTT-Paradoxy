# S-RES-20260912-059-EVIDENCE-QUEUE-BATCH2

- 触发：S058 路由的第一工作包 N13（按 owner 文档分层抽样）。
- 抽样规则（`scripts/audit/sample_understanding_claims_batch2.py`）：按 owner 文档分层（C 10 / meta 10 / A 15 / B 15，层内先剔除第一批样本再等距取样）→ 50 条。
- 判词分布：`SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15`；两批累计 90/2,396（3.76%）：43/12/0/35。
- 新发现：`CL-001835`/`CL-001876`（C0）账本文本仍为 generation-2 口径（903 KC），而 owner 文档已更新——claim 账本缺 owner-doc hash，行锚/文本漂移。已开 `A-CLAIM-LEDGER-DRIFT-001`（OPEN_ISSUE / REVIEW_REQUIRED），并有界记录不影响机器闭合结果。
- E6 检查：第二批仍未出现 natural-use chain。
- 边界：样本只覆盖固定分层规则；PENDING 不当作支持或否证；不新增 claim matrix 行。
- 三件套：direction/panorama revision 59/generation 043；core 不变；无 理解章节 变更。
- Git：未 commit、未 tag、未 push。
