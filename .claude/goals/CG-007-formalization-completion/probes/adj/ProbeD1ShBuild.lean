import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 9（**不是收据**）：`Theory.Δ₁ Sh` 能不能建出来？

我判断它是多条线的共同缺口。`Theory.Δ₁` 的三个字段（Foundation `Syntax/Theory.lean:16`）：
```lean
class Δ₁ (T : Theory L) where
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁
```

Foundation 唯一的通用模板 `InductionScheme.delta1_of`（`Incompleteness/Definability.lean:203`）：
```lean
noncomputable abbrev InductionScheme.delta1_of
    {cond : 𝚫ᴬ₁.Semisentence 1} {S : ∀ V …, V → Prop}
    (hS : ∀ V …, 𝚫ᴬ₁-Predicate[V] S V via cond)
    (hC : ∀ γ, S ℕ ⌜γ⌝ ↔ C γ) : (InductionScheme ℒₒᵣ C).Δ₁
```
它给的是 `InductionScheme`（归纳原理的理论）的 Δ₁，不是任意理论。所以对 `Sh` 不直接适用。

**`Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}`**。它的成员谓词 = `iT` 图 + 𝗭𝗙𝗖 可证性。
Foundation 的 `𝚫ᴬ₁.Semisentence` 机制里没有 `iT` 这个构造子。

本探针逐条核：哪些部分是现成的 𝚫 层，哪些不是。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeD1Sh2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 现成件：trProv 是 𝚺ᴬ₁ 层（Z0Full.lean:40）
#check @trProv
#check @trProv_defined

-- 现成件：provability 的层级
#check @provable

-- Sh 的定义
#check @Sh
#check @Sh_provable_iff

-- Foundation 的 InductionScheme.delta1_of 模板（不能直接用，但可仿形）
#check @InductionScheme.delta1_of

-- 关键：`iT` 是不是 Foundation 意义上的 𝚫 层可定义谓词？
#check @iT
#check @iT_definable

end GodelQ.ProbeD1Sh2
