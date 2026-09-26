# 同一个演算，只换一步的种类：路径还是箭头（C-57，Rzk，带显式有向单价接口）

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> **起因**：Terra 复审 009 的 §6、T-021 与 O-029：
> - 010 的有向对照“同时更换了恒等路径演算、有向区间、协变性、宇宙 S、模态公理与具体模型”，因此还不是严格的核心理论层面消融；
> - 最低充分的下一步是：在可复现的 TT_□/GWB 形式化中，或在**具有明示该公理接口的证明环境**中，固定 `Nat ∈ S`、`Gl(Nat, Nat, suc)`、其协变运输、两步复合与精确的停机合同。
>
> 本包按后一种方式做。讨论见 CN-030 与回信 012。
>
> - proof id：`MP-CG001-DIRECTED-INTERFACE-001`（主包）、`MP-CG001-DIRECTED-INTERFACE-NEG-001`（负控制）。
> - claim：`CG001-C-57`。
> - 工具链：Rzk 0.11.3（`HoTT/formal/claude-cg001/directed-native/RZK_TOOLCHAIN.json`），sHoTT，无公设，不加公理，不用模态。运行由 `.claude/goals/CG-001-targeted-overview/tools/capture_rzk_proof_run.py` 捕获。
> - 标签：`RZK_TYPECHECKED_RELATIVE_TO_EXPLICIT_DIRECTED_UNIVALENCE_INTERFACE`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §13（GOAL_LOCAL_INDEX_ONLY）。

## 接口（只作为定理的假设出现，不是公设）

| 假设 | 对应的来源（GWB，arXiv:2407.09146，经 sciverse 全文；未重放） |
|---|---|
| `S : U`、`El : S → U` | S 是离散类型的宇宙（摘要、§6） |
| `is-cov : is-covariant S El`（RS17 定义 8.2） | 引理 5.11：宇宙上的族是协变的 |
| `du : is-directed-univalent S El is-cov`：对一切 `A B`，把箭头送到其协变运输的映射 `hom S A B → (El A → El B)` 是等价 | 定理 6.13（有向单价性）：`mor2fun` 是等价，这里取端点固定的形式 |
| `Gl` 取该等价的截面，`coe-Gl` 由截面律推出 | 定义 6.14、引理 6.15（`coe` 为 `f`） |
| 纤维 `El A` 扮演自然数：`s` 为后继，`z` 为零，只用两条事实：`z-not-hit`（`s x = z` 不可能）、`no-fixed`（`z = s (s z)` 不可能） | ℕ 属于 S（TT_□ 中 ℕ 离散，推论 3.20） |
| (c) 中的复合 `comp` 与 `coe-comp`（复合的协变运输是运输的复合） | 引理 6.16（S 是 Segal 的，证明梗概）与 RS17 的函子性 |

## 命题全文（`SameCalculusSwitch.rzk`）

- **(a) 一步写成 S 中的路径**：
  - `no-path-acts-as-step`：没有路径 `p : A = A` 使 `El` 沿它的运输作用为 `s`（依据 `z-not-hit`）；
  - `path-round-trip-never-stops`：沿路径 `p` 再沿其逆走一个来回，随身之物回到 `z`，所以停机条件“值为 `s (s z)`”不成立（依据 `no-fixed`）。
- **(b) 一步写成 S 中的箭头**：
  - `arrow-step-acts`：箭头 `Gl A A s` 使 `El` 沿它的协变运输作用为 `s`；
  - `arrow-walk-stops`：两步箭头行走到达 `s (s z)`，停机条件在两步后成立。
- **(c) 复合的来回箭头**：`composite-round-trip-stops`：在 `comp`、`coe-comp` 的假设下，复合箭头 `comp step step` 也把 `z` 带到 `s (s z)`。
- **负控制**：`WrongDefinitionalCoe.rzk` 不借助接口，以 `refl` 断言沿任意箭头的协变运输就是给定函数，被拒：`cannot unify term π₁ (π₁ (is-cov A B f u)) with term φ u`。

## 解读【解释】

- 这是 Terra 要的“同一演算”对照：
  - (a) 与 (b) 用同一个演算（sHoTT）、同一个宇宙 `S`、同一个族 `El`、同一个纤维、同一个停机合同；
  - 唯一的区别是一步的种类：路径还是箭头。路径一侧，群胚律照旧（运输是等价，来回复原）；箭头一侧，有向单价性让不可逆的 `s` 成为一步。
- **对 010 的一处修正**：TT_□ 并没有去掉 P9（恒等路径可逆）。在同一演算里路径仍然可逆，这是 C-53 与本包 (a)。它做的是另加一种不必可逆的态射。所以这个对照的准确名字是**过程原语的切换**（用恒等路径还是用箭头表示一步），不是“去掉群胚律”。
- 接口的一致性，即这样的 `S` 与 `El` 确实存在，是 GWB 的定理（来源，未重放），不是本包的结论。

## 禁止外推

- 不构造 S，也不重放 GWB 的公理与证明；定理对任何满足接口的 `S`、`El` 成立。
- (c) 的复合假设代替了 GWB 引理 6.16 与 RS17 函子性，本包没有证明它们。
- 不涉及现实行走；“一步”“停机”是解释标签。
- 数学内容标准，**不主张原创**。
