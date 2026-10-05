# CoreAdequacyTaskCard — C0R1：冻结候选宇宙的全家族 reconciliation

> **状态：** `LEAF_ACTIVE / CANDIDATE_UNIVERSE_RECONCILIATION / NOT_A_TOTAL_VERDICT`。

## 1. 任务

对 F-A–F-E 逐一回读其当前 owner、direct source、control、reopen condition，判断当前冻结分母是否真正没有未处理候选。不可把“已写很多卡”或“某个C6通过”当作 C0 完成。

## 2. 输出

一张 family table：每族的 exact denominator、paid fields、unpaid fields、live/remainder和reopen_if。若所有固定分母已处理，则写 `C0_DENOMINATOR_EXHAUSTED_WITH_SCOPE`，但仍须执行 SOP 004 的其它总门和最终 conclusion classification。
