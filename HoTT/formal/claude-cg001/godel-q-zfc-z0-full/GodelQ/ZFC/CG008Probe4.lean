import GodelQ.ZFC.CG008Reduce

/-!
# CG-008 探针 4（非收据）：归约后的目标到底需要什么

归约（`CG008Reduce.lean`）把缺口化成：

```
∀ V ⊨ 𝗜𝚺₁, ∀ τ, 𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ⌝ → 𝗭𝗙𝗖.internalize V ⊢ ⌜translate (zfcTr τ)⌝
```

本探针查实**这个内部形状离 D3 有多远**。

## 关键观察

内部演算里有一条**现成**的路子：`TProof.modusPonens`（`Typed.lean`）。
若能证出内部蕴含句 `𝗭𝗙𝗖.internalize V ⊢ ⌜translate τ 🡒 translate (zfcTr τ)⌝`，
则 modus ponens 一步给出目标。

而这条蕴含句**恰好就是** `Z0Blocked.lean` 文档里第 16-18 行说的
「`zfcTr_D3_syntactic`」——文件里明确记着它**不是 ZFC 定理**：

> `zfcTr_D3_syntactic : 𝗭𝗙𝗖 ⊢ translate τ 🡒 translate (zfcTr τ)` 本身不是 ZFC 定理。
> 它是“τ → ZFC 证明了 τ 的翻译”的反射原理，对任意 τ ZFC 不能证明。

所以这条路被已知的反射原理障碍挡住（那正是哥德尔第二定理的内容）。

## 那么归约后的目标要什么？

要在**内部**从 `⌜translate τ⌝` 的推导造出 `⌜translate (zfcTr τ)⌝` 的推导，
而**不**经过那条反射蕴含。这需要：

1. 内部演算里对 `provable 𝗭𝗙𝗖` 的 Σ₁ 完全性（即「V 内部的推导码存在 ⟹ V 内部
   `provable 𝗭𝗙𝗖` 那个码成立」），
2. 再把这个 Σ₁ 事实沿 `iT`/`iTDef` 翻译成 `⌜translate (zfcTr τ)⌝`。

第 1 条是 Foundation **已有**的（`D3.lean` 的 `sigma_one_complete`），但它服务的是
`ArithmeticTheory` 的 `Provable T`，而这里要的是集合论 `𝗭𝗙𝗖`。
第 2 条需要把「算术 Σ₁ 完全性的结论」与「集合语言的翻译」在 V 内部对上。

本探针只查实第 1 条在集合语言侧**是否可直接调用**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe4

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：内部演算的蕴含消去对集合语言可用（`Entailment` 的 `ModusPonens` 实例）。
若那条蕴含句能证出，目标一步可达。 -/
example (φ ψ : Formula V ℒₛₑₜ)
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ 🡒 ψ) (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) :
    𝗭𝗙𝗖.internalize V ⊢ ψ :=
  h ⨀ hφ

/-- **查实 2**：集合语言侧的「Σ₁ 完全性」**不能**直接调 Foundation 的算术版。
`Bootstrapping.Arithmetic.sigma_one_complete` 要求 `T : ArithmeticTheory`，
而 `𝗭𝗙𝗖` 是 `Theory ℒₛₑₜ`。这一行预期**编不过**（保留为注释形式的事实记录）。

```lean
-- 预期失败：
-- example {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
--     V↓[ℒₒᵣ] ⊧ σ → Provable 𝗭𝗙𝗖 (⌜σ⌝ : V) :=
--   Bootstrapping.Arithmetic.sigma_one_complete (T := 𝗭𝗙𝗖) hσ
-- 错误：`𝗭𝗙𝗖` 是 `Theory ℒₛₑₜ`，不是 `ArithmeticTheory`
```

对**算术**理论它可用——这正是缺口不能靠算术 D3 直接闭合的原因。 -/
example {σ : ArithmeticSentence} (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    V↓[ℒₒᵣ] ⊧ σ → Provable 𝗜𝚺₁ (⌜σ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := 𝗜𝚺₁) hσ

end GodelQ.CG008Probe4
