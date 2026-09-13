# S-GOV-20260912-030-ERCF-DEPENDENCY-SEMANTICS-ALIGNMENT

- 触发：S029 后 research task plan 可生成，但 `review_required` 仍包含 `A-ERCF-FACTORIZATION-FORMAL-001`。
- 根因：该 proof record 把开放的 `A-HOTT-SELF-VALIDATION-ECONOMY-001` 放进 `depends_on`；runtime 会正确传播依赖的证据 stale/review。研究母题/动机不是 C-59–C-66 的证明有效性依赖。
- 修复：`depends_on=[A-MATH-PROOF-DELIVERY-GATE-001]`；新增非传播的 `research_parent=A-HOTT-SELF-VALIDATION-ECONOMY-001`；proof source/run/index/hash 全部不变。
- 预期验收：同一 task plan 成功，且 `review_required` 不包含 `A-ERCF-FACTORIZATION-FORMAL-001`；父研究记录仍保持开放/paper-only。
- 数学状态：`MP-ERCF-001` 不变；不是 HoTT 悖论。
- 三件套：无语义变化，只同步 revision 30/generation 014；core 不变。
- Git：未 commit、未 tag、未 push。
