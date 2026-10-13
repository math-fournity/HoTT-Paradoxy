import GodelQ.ZFC.CG008AxmInt

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Bridge1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008AxmStep

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 桥的一半：`sigma ∈ Sh.craig → Provable 𝗭𝗙𝗖 (iT 0 ⌜sigma⌝)`

**链条**：

1. `sigma ∈ Sh.craig`
   →（`by_axm` + `Sh.craig ⪯ Sh`）→ `Sh ⊢ sigma`
   →（`Sh_provable_iff`）→ `𝗭𝗙𝗖 ⊢ translate sigma`      【`CG008AxmStep` 已证】
2. `𝗭𝗙𝗖 ⊢ translate sigma`
   →（`internalize_provability`，`D1.lean:27`）→ `Provable 𝗭𝗙𝗖 (⌜translate sigma⌝ : V)`
3. `⌜translate sigma⌝ = iT 0 ⌜sigma⌝`                                【`iT_quote`】

**合起来**：`sigma ∈ Sh.craig → TrProvable ⌜sigma⌝`。

**这就是 `provabilityPred Sh.craig sigma → zfcTr sigma` 的元层内容。** -/

set_option maxHeartbeats 800000 in
theorem craig_mem_to_TrProvable (sigma : ArithmeticSentence)
    (h : sigma ∈ Sh.craig) : TrProvable (⌜sigma⌝ : V) := by
  -- 第 1 步
  have h1 : Sh.craig ⊢ sigma := by_axm h
  have h2 : Sh ⊢ sigma := (inferInstance : Sh.craig ⪯ Sh).wk h1
  have h3 : 𝗭𝗙𝗖 ⊢ arithTrln.translate sigma := (Sh_provable_iff sigma).mp h2
  -- 第 2 步
  have h4 : Provable 𝗭𝗙𝗖 (⌜(arithTrln.translate sigma : Semisentence ℒₛₑₜ 0)⌝ : V) :=
    internalize_provability (T := 𝗭𝗙𝗖) (V := V) h3
  -- 第 3 步：把目标里的 `iT 0 ⌜sigma⌝` 换成 `⌜translate sigma⌝`
  have heq : iT (0 : V) (⌜sigma⌝ : V) =
      ⌜(arithTrln.translate sigma : Semisentence ℒₛₑₜ 0)⌝ := iT_quote (V := V) sigma
  rw [TrProvable, heq]
  exact h4

end GodelQ.CG008Bridge1

#print axioms GodelQ.CG008Bridge1.craig_mem_to_TrProvable
