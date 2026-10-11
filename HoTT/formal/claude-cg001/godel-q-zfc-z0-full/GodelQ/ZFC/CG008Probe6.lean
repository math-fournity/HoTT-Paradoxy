import GodelQ.ZFC.CG008SetAll

/-!
# CG-008 探针 6（非收据）：`Derivable` 的原始层规则 API 对集合语言是否可用

## 背景

上一轮把缺口归约到内部演算形状（`CG008Reduce.lean`）：

```
∀ V ⊨ 𝗜𝚺₁, ∀ τ, 𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ⌝ → 𝗭𝗙𝗖.internalize V ⊢ ⌜translate (zfcTr τ)⌝
```

而 `CG008MemCase.lean` 指出障碍：算术版靠 `toNumVec` 把自由变量的值命名成**数字项**，
`ℒₛₑₜ` 没有常项，这一步无对偶。

## 本探针要查的

读 `Syntax/Proof/Basic.lean:935` 发现一条**此前未用过的通道**：

```lean
lemma internal_provable_iff_internal_derivable {φ : V} :
    Provable T φ ↔ Derivable T (insert φ ∅ : V)
```

`Derivable`（`Basic.lean:537`）是**原始层**的推导谓词：`∃ d : V, DerivationOf T d s`，
其中 `s : V` 是一个**编码的序列**（不是 typed `Formula`）。
它的规则 API（`Basic.lean:786-937`）——`em`、`and_m`、`all_m`、`ex_m`、`wk`、`cut`、
`by_axm`、`and`、`or`、`all`、`exs`、`conj`、`disj`——**只要求 `T.Δ₁Class`**，
不要求算术、不要求 typed 层。

**若这些规则对 `𝗭𝗙𝗖` 可用**，那么在 V 内部构造推导就不必走 typed 层，
「自由变量命名」的障碍可能被绕开：`Derivable` 的规则直接作用在**编码**上。

本探针逐条查实。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe6

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`Provable` ↔ `Derivable` 的通道对 `𝗭𝗙𝗖` 可用。
这是通用引理（`Basic.lean:939`），只要 `T : Theory L`。 -/
example (φ : V) : Provable 𝗭𝗙𝗖 φ ↔ Derivable 𝗭𝗙𝗖 (insert φ ∅ : V) :=
  internal_provable_iff_internal_derivable

/-- **查实 2**：`Derivable` 的 `by_axm` 规则对 `𝗭𝗙𝗖` 可用——
即「公理集里的句子可证」，只用 `T.Δ₁Class`。
这正是上一轮 `ZFCSetInternal.set_outer_to_internal` 想做的事，但走的是**编码层**而非 typed 层。 -/
example {s p : V} (hs : IsFormulaSet ℒₛₑₜ s) (hp : p ∈ s) (hT : p ∈ 𝗭𝗙𝗖.Δ₁Class) :
    Derivable 𝗭𝗙𝗖 s :=
  Derivable.by_axm hs p hp hT

/-- **查实 3**：合取引入规则 `Derivable.and` 对 `𝗭𝗙𝗖` 可用。 -/
example {s p q : V} (hp : Derivable 𝗭𝗙𝗖 (insert p s)) (hq : Derivable 𝗭𝗙𝗖 (insert q s)) :
    Derivable 𝗭𝗙𝗖 (insert (p ^⋏ q) s) :=
  Derivable.and hp hq

/-- **查实 4**：全称引入规则 `Derivable.all` 对 `𝗭𝗙𝗖` 可用（编码层，不需要 typed `Formula`）。 -/
example {p s : V} (hp : IsSemiformula ℒₛₑₜ 1 p)
    (h : Derivable 𝗭𝗙𝗖 (insert (free ℒₛₑₜ p) (setShift ℒₛₑₜ s))) :
    Derivable 𝗭𝗙𝗖 (insert (^∀ p) s) :=
  Derivable.all hp h

/-- **查实 5**：存在引入规则 `Derivable.exs` 对 `𝗭𝗙𝗖` 可用。 -/
example {p t s : V} (hp : IsSemiformula ℒₛₑₜ 1 p) (ht : IsTerm ℒₛₑₜ t)
    (h : Derivable 𝗭𝗙𝗖 (insert (substs1 ℒₛₑₜ t p) s)) :
    Derivable 𝗭𝗙𝗖 (insert (^∃ p) s) :=
  Derivable.exs hp ht h

/-- **查实 6**：切规则 `Derivable.cut` 对 `𝗭𝗙𝗖` 可用。 -/
example {s : V} (p : V) (hd₁ : Derivable 𝗭𝗙𝗖 (insert p s))
    (hd₂ : Derivable 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ p) s)) :
    Derivable 𝗭𝗙𝗖 s :=
  Derivable.cut p hd₁ hd₂

end GodelQ.CG008Probe6
