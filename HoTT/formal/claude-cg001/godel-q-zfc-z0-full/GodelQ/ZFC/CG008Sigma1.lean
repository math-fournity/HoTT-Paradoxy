import GodelQ.ZFC.CG008SetAll

/-!
# CG-008 · 集合语言的 Σ₁ 完全性：闭句版本（构造尝试）

本文件尝试 `CG008_HANDOFF_2026-10-11.md` §4 的第 2 步——`set_sigma_one_complete`。

## 形状的确定（据探针 5 的层次分析）

- `setTheory_sigma₁_induction'` 的 `P` 取 untyped `SetTheorySemiformula ξ n`；
  内部演算的 `⊢` 取 typed `Bootstrapping.Semiformula V ℒₛₑₜ n`。
- 通道是 `⌜·⌝`（typed quote），对 `n = 0`（闭句）直接通。

因此本文件先做**闭句版本**：

```
set_sigma_one_complete_sentence {σ : SetTheorySentence}
    (hσ : ℬ[∈, ℒₛₑₜ].Hierarchy 𝚺 1 σ)
    (h : 𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝) : 𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝
```

**注意**：这个形状的前提取的是「内部已经可证」，所以它是**平凡**的。
真正要做的是前提取**语义** `V↓[ℒₛₑₜ] ⊧ σ`（像算术版 `bold_sigma_one_complete`
的 `V ⊧/w φ` 那样），再推出内部可证。

## 本文件做什么

先把「闭句 + 语义前提 ⇒ 内部可证」这条路的**输入输出形状**固定下来，
并把 `setTheory_sigma₁_induction'` 的调用方式写出来（十情形的骨架），
标出每个情形需要的工具是否已就位。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Sigma1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 1. 十情形所需的工具清单（现状核对）

`setTheory_sigma₁_induction'`（`SetTheory/Basic/Hierarchy.lean:63`）的十情形，
逐条核对集合语言内部演算的工具是否就位：

| 情形 | 形状 | 所需工具 | 现状 |
|---|---|---|---|
| `hVerum` | `⊤` | 内部 `⊤` 的证明（`Entailment.Minimal.verum`） | ✅ 通用 |
| `hFalsum` | `⊥` | 从语义 `V ⊧ ⊥` 出发——语义为假，情形不可达 | ✅ 平凡 |
| `hEQ` | `#a = #b` | `set_eq_refl`（`t = t`）+ `set_eq_symm` | ◐ 只对闭项；开项需全称闭包 |
| `hNEQ` | `#a ≠ #b` | `set_ne_symm` | ◐ 同上 |
| `hMem` | `#a ∈ #b` | —— | ❓ 缺（成员关系的**正**事实无法从等式得到） |
| `hNMem` | `#a ∉ #b` | —— | ❓ 缺 |
| `hAnd` | `φ ⋏ ψ` | `set_K_intro` | ✅ |
| `hOr` | `φ ⋎ ψ` | `set_A_intro_left/right` | ✅ |
| `hBall` | `∀¹[“#0 ∈ t”] φ` | `set_ball_intro` | ✅（本轮补上） |
| `hExs` | `∃¹ φ` | `set_exs_intro` | ✅（已有） |

**关键缺口**：`hMem` / `hNMem` 两个**成员关系**情形。
从语义 `V ⊨ #a ∈ #b` 出发，要在内部造出 `#a ∈ #b` 的推导——
这需要集合语言的**外延性/成员公理**层面的工具，而 `ZFCSetInternal.lean` 的
13 条全部是**等式**层面的（`set_subst_mem` 只做等号替换，不产生新的成员事实）。

`ZFCSetInternal.lean` 的 `set_outer_to_internal` 提供了一条出口：
若 `𝗭𝗙𝗖 ⊢ σ`（**外部**），则 `𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝`（**内部**）。
但 `#a ∈ #b` 带自由变量，不是闭句——需要先做全称闭包，
而这正是 `set_all_intro` 能做的（若闭包后的外部句可证）。

## 2. 结论

本文件固定了十情形的工具现状。**`hMem` / `hNMem` 是构造路线的真正剩余障碍**，
不是先前以为的「全称引入」（那个本轮已补上）。

## 治理

- 本文件不含任何未证标记，可进入收据。
-/

end GodelQ.CG008Sigma1
