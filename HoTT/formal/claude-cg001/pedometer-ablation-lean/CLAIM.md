# 有向模型的计步器：Lean 4 独立内核重证（C-52）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：用户要求用其他机器证明系统与方法检验有向预测（原话见 `pedometer-ablation/CLAIM.md`）。本包用 Lean 4 作为**第二个独立内核**，重证 C-51 的有向模型，使这一侧不只依赖 Agda。
>
> - proof id：`MP-CG001-PEDOMETER-ABLATION-LEAN-001`（主包）；负控制 `MP-CG001-PEDOMETER-ABLATION-LEAN-NEG-001`。
> - claim：`CG001-C-52`。
> - 工具链：Lean 4.34.0（`LEAN_TOOLCHAIN.json` 固定启动器、共享库与 `Init` 的哈希），只用 Lean 核心，不用 Mathlib。运行由 `.claude/goals/CG-001-targeted-overview/tools/capture_lean_proof_run.py` 捕获，经 `tools/lean_check.py` 在最小环境中调用固定二进制，并以 `leanchecker --fresh` 在全新内核环境里重放全部常量。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §12（GOAL_LOCAL_INDEX_ONLY）。

## 适用范围

Lean 的相等满足证明唯一性（UIP），所以本包**不陈述任何关于 HoTT 路径的事**。图 `west —go→ east —back→ west` 上的自由范畴是集合层的对象；这里的每个命题都只关于这个模型。消融的 HoTT 一侧（C-49、C-50）在 Cubical Agda 中证明，C-49 的核心又在 Rzk 中证明（C-53）。

## 命题全文（`PedometerDirected.lean`，命名空间 `CG001.PedometerDirected`）

- **(a) 范畴律**：`Walk.append_stay`；`Walk.append_assoc`（`append stay w = w` 按定义成立）。
- **(b) 计步器是函子，提升唯一**：
  - `carry`：`carry stay n = n`，`carry (next s w) n = carry w (n + 1)`；
  - `carry_stay`；`carry_append : carry (append w v) n = carry v (carry w n)`；
  - `unique_lift : ∃ m, carry w n = m ∧ ∀ m', carry w n = m' → m' = m`。
- **(c) 只增、按步数增**：
  - `carry_length : carry w n = w.length + n`；
  - `never_lowers : n ≤ carry w n`；
  - `every_step_raises : n < carry (next s w) n`；
  - `roundTrip_adds_two : carry roundTrip n = n + 2`（`rfl`）。
- **(d) 停机**：`after_zero : after 0 = 0`、`after_one : after 1 = 2`、`halts : run 1 = some 1`（均为 `rfl`）。
- **(e) 没有逆**：
  - `go_has_no_inverse : ¬ ∃ w : Walk .east .west, next .go w = stay`；
  - `roundTrip_ne_stay : roundTrip ≠ stay`。
- **公理依赖**：源码末尾对 11 条主要定理执行 `#print axioms`，全部输出 “does not depend on any axioms”。它们不依赖 `propext`、`Quot.sound`、`Classical.choice`，也没有 `sorryAx`。
- **负控制**：`WrongDirectedStays.lean` 导入主模块，以 `rfl` 断言 `carry roundTrip 0 = 0`；内核拒绝（“Not a definitional equality”）。

## 与 C-51 的关系

C-52 与 C-51 是同一个数学模型，在两个互相独立的内核（Agda 与 Lean）中分别检查。C-51 另有 (f)，即与 HoTT 出路的对照，它需要高阶归纳类型，只在 Agda 中。

## 工具链事件（照实记录）

2026-09-25 10:09–10:12，第一次未隔离地调用 `leanchecker` 时，它经 PATH 上的 elan 代理找 `lean`。默认通道 `stable` 使 elan **自动下载并安装了 `leanprover/lean4:v4.34.1`**（约 2.7 GB），事先没有征得用户许可。

本包的任何运行都不使用该工具链。此后的全部调用改为按绝对路径调用固定版本，设 `LEAN_SYSROOT`，并使用最小环境。已向用户报告，是否保留由用户决定。

## 禁止外推

- 不涉及 HoTT、单价性或路径。
- 不是有向类型论内部的定理，也不是对 GWB 的重放。
- “步行”“计步器”“停下”是解释标签。
- 数学内容标准（自由范畴与其上的计数函子），**不主张原创**。
