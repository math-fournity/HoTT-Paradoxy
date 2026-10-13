import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 找宇宙多态的桥（2026-10-13）

`Provable.sound` 硬接线宇宙 0，不可用。但 `Typed.lean` 有一条**多态**的桥：

  TProvable.iff_provable : T ⊢ σ ↔ Provable T.theory σ.val
  tprovable_tquote_iff_provable_quote_sentence :
    T.internalize V ⊢ ⌜σ⌝ ↔ Provable T (⌜σ⌝ : V)

这里 `V` 是**显式参数**（`InternalTheory V L`），故可能宇宙多态。
本探针核验它能否用在任意 V 上，作为 `Provable.sound` 的替代。

## ✅ 结论：可用——`V : Type u_3`，**宇宙多态**

```
@TProvable.iff_provable :
  ∀ {V : Type u_3} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {L : Language} [L.Encodable] [L.LORDefinable]
    {T : InternalTheory V L} {σ : Formula V L}, T ⊢ σ ↔ Provable T.theory σ.val

@tprovable_tquote_iff_provable_quote_sentence :
  ∀ {V : Type u_3} … {T : Theory L} [T.Δ₁] {σ : Sentence L},
    Theory.internalize V T ⊢ ⌜σ⌝ ↔ Provable T ⌜σ⌝
```

**这是 `Provable.sound`（`Provable.{0,0}`）的多态替代品**：
`V` 是显式参数 `Type u_3`，在任意 V 上可用。

**对语义路线的意义**：`tprovable_tquote_iff_provable_quote_sentence` 给出
`Provable 𝗭𝗙𝗖 ⌜σ⌝ ↔ Theory.internalize V 𝗭𝗙𝗖 ⊢ ⌜σ⌝`（对 `Sentence σ`），
即「V 里的可证码」↔「V 上的**内部**可导性」。
配合 `SetTheory.complete`（模型侧多态）与 `translate_iff`，语义路线的零件**齐了**。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeTypedBridge
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

#check @TProvable.iff_provable
#check @tprovable_tquote_iff_provable_quote_sentence
#check @InternalTheory

end ProbeTypedBridge