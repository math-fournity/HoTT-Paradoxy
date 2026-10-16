# MP-COST-FACTORIZATION-001：同函数异时的第一机器构造

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`

本包把《HoTT 研究三问》的第一候选（"同函数异时"）做成原生机器实例：**外延相同的两个程序，其成本不能从裸函数恢复；而成本细化表示可以恢复。** 这是方向 A（现实可完成/理论额外困难）与"资格保持"主线的第一个 cost 实例。

## 固定构造

- 源演算：极小程序语法 `Prog = fast | slow k`，语法导向步数成本 `cost`（`fast` 1 步、`slow k` 2+k 步），`run` 恒返回 0；
- 裸表示：`fun : Prog → (ℕ → ℕ)`（只保留外延函数）；
- 细化表示：`refine : Prog → ((ℕ → ℕ) × ℕ)`（函数 + 输入 0 处成本）。

## 冻结命题

- `C-96`：对任意 `k`，`fun fast ≡ fun (slow k)`（funext）而 `¬ (cost fast 0 ≡ cost (slow k) 0)`（同函数、异成本）。
- `C-97`：不存在能区分两个外延相等程序的裸函数谓词：`¬ Σ[ P ∈ ((ℕ→ℕ) → Type) ] (P (fun fast) × ¬ P (fun (slow 0)))`（funext 路径 + transport）。
- `C-98`：推论——不存在从裸函数恢复成本的 consumer：`¬ Σ[ r ∈ ((ℕ→ℕ) → ℕ) ] (∀ p → r (fun p) ≡ cost p 0)`。
- `C-99`：正控制——细化表示可恢复成本（`snd (refine p) ≡ cost p 0`）并区分两个程序（`refine fast ≢ refine (slow k)`）。

## 解释边界（判词）

判词：`NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL`（表示限制 + 正控制）：

- 不可区分性来自 HoTT 自身的原则（funext 是原生 Path），所以"从裸函数取成本"不是被任意规则禁止，而是被等式本身排除；
- 正控制说明损失是**表示**造成的，补回成本分量即可恢复——不是"cost 不可表达"的过强结论；
- 不是 HoTT 悖论；不证明现实物理时间或编译实现主张。

## 不证明（非目标）

- 不证明真实编译器/硬件的成本模型；`cost` 是明示的语法导向计数示例；
- 不证明原创性（三问文档已标明 cost/extensionality 张力有文献讨论，如 cost-aware type theory）；
- 不构造"自然 consumer"（该问题保留为方向表的 Gate）。

## 证明身份

- proof ID：`MP-COST-FACTORIZATION-001`
- claim IDs：`C-96`–`C-99`
- final run：`20260912-MP-COST-FACTORIZATION-001-01`
- source：`CostFactorization.agda`
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件见 `../../verification/runs/20260912-MP-COST-FACTORIZATION-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
