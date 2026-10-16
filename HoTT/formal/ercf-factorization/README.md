# MP-ERCF-001：任务相对因子化基础

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED`

本目录形式化 C4/ERCF-1/2 的通用表示论骨架：因子化的必要条件、明确 witness 对因子化的否定、带 section 时的一个充分条件、E₀ 正反控制、subsingleton 余域反控制、分离观察族和 identity 观察控制。

## 证明范围

- 系统：Lean 4 的普通依值类型论与 equality；
- 公理：源码中不声明额外 axiom；
- 结论：只关于 `FactorsThrough`、`FiberConstant`、`ParadoxWitness` 等本文件定义；
- 不使用：univalence、cubical Path、HIT、propositional truncation、higher coherence；
- 因此：这些机器证明是进入 HoTT 特定研究前的通用 walking skeleton，**不是 HoTT 悖论，也不证明任何 HoTT 核心缺陷或现实物理桥梁**。

## 身份

- proof ID：`MP-ERCF-001`
- claim IDs：`C-59`–`C-66`
- source：`ERCF.lean`
- final indexed run：`20260912-MP-ERCF-001-02`
- pre-index run：`20260912-MP-ERCF-001-01`（kernel accepted，但 README 随后补充最终状态，因此不作为当前索引 run）
- run root：`../../verification/runs/`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Lean 4.33.1 已对本目录当前源码实际运行；final run 的 stdout/stderr、环境和 source manifest 在 `20260912-MP-ERCF-001-02/`，C-59–C-66 由 claim matrix 索引。当前工作树未提交，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
