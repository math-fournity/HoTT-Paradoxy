# MP-COST-FACTORIZATION-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。

本文件记录《HoTT 研究三问》第一候选（同函数异时）的首个原生机器实例。

## 1. 触发与依据

- 触发：S038 后 `方向追踪.md` §6 第 4 项（同函数异时 cost 第一机器构造）。
- 依据：三问文档 §二.5 的"快/慢程序"示例与不可恢复论证；一般因子化的 Lean 骨架 `MP-ERCF-001`（本包是其 HoTT 原生实例 + 正控制）。

## 2. 本轮构造

- 小程序语法 `Prog = fast | slow k`，语法导向成本 `cost`（1 步 / 2+k 步），`run` 恒 0；
- 裸表示 `fun`（外延函数）与细化表示 `refine`（函数 + 成本分量）；
- 不可区分性用 funext 路径 + transport 证明；成本恢复 no-go 作为其谓词实例；细化正控制给出恢复与区分。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-96` | `fun fast ≡ fun (slow k)` 且 `¬ (cost fast 0 ≡ cost (slow k) 0)` | `same-function-different-cost` |
| `C-97` | 不存在区分两个外延相等程序的裸函数谓词 | `no-distinguishing-predicate` |
| `C-98` | 不存在 `r : (ℕ→ℕ) → ℕ` 从裸函数恢复成本值 | `no-cost-value-recovery` |
| `C-99` | 细化表示可恢复成本且区分两程序 | `refined-cost-recovery`、`refined-separates` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-COST-FACTORIZATION-001-01/`；
- 同一 Agda 2.8.0 + Cubical v0.9 工具链；exit 0，stderr 0 字节；
- 独立重放：`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`；
- 矩阵第六次增长后重放七个旧包，全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。

## 5. 失败与修订谱系

本包一处机械修正：`¬` 需本地定义（未导入 partiality 模块）。命题未削弱。

## 6. 判词与边界

判词：`NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`。

- 不可区分性由 HoTT 自身等式原则（funext）产生，故"从裸函数取成本"被等式排除而非被额外规则禁止；
- 正控制说明补回成本分量即可恢复——不是"成本不可表达"的过强结论；
- 不是 HoTT 悖论；不证明真实编译器/硬件成本或原创性；自然 consumer 仍为开放 Gate。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
