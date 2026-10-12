import GodelQ.ZFC.CG008VeLevel

/-!
# CG-008 · `ve2` 的零件
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Ve2
open GodelQ.ZFCArith GodelQ.Translate GodelQ.CG008VeParts
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `cFunc k f` 在 `k ≠ 0` 时是层 3 的公式（add/mul）。 -/
lemma cFunc_isSemiformula_three {k f : V} (hk : k ≠ 0) :
    Bootstrapping.IsSemiformula ℒₛₑₜ 3 (Translate.cFunc k f) := by
  rw [Translate.cFunc]
  by_cases hf : f = 0 <;>
    simp only [hk, hf, ↓reduceIte, Translate.cFuncN, ite_true, ite_false]
  all_goals try norm_num
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
      (arithTrln.func Language.ORing.Func.add)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 3) _
  · rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 3)
      (arithTrln.func Language.ORing.Func.mul)]
    simpa [Nat.cast_ofNat] using
      FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 3) _

/-- 三元替换向量 `^#2 ∷ ?[^#0, ^#1]` 在层 3 是项向量。

用 `IsSemitermVec.cons_iff` + `doubleton` 拆，避免直接处理 `V` 上的界。 -/
lemma isSemitermVec_ve2vec : Bootstrapping.IsSemitermVec ℒₛₑₜ 3 3 (^#2 ∷ (?[^#0, ^#1] : V)) := by
  rw [show (3 : V) = 2 + 1 by norm_num]
  rw [Bootstrapping.IsSemitermVec.cons_iff]
  refine ⟨?_, ?_⟩
  · simp [Bootstrapping.IsSemiterm.bvar]
  · rw [Bootstrapping.IsSemitermVec.doubleton]
    exact ⟨by simp [Bootstrapping.IsSemiterm.bvar], by simp [Bootstrapping.IsSemiterm.bvar]⟩

/-- **`cDomN` 是公式的码**（层 1 的 `IsSemiformula`）。 -/
lemma cDomN_isSemiformula :
    Bootstrapping.IsSemiformula ℒₛₑₜ 1 ((Translate.cDomN : ℕ) : V) := by
  rw [Translate.cDomN]
  rw [FFL.FirstOrder.Sentence.coe_quote_eq_quote (V := V) (L := ℒₛₑₜ) (n := 1)]
  simpa [Nat.cast_one] using
    FFL.FirstOrder.Sentence.quote_isSemiformula (V := V) (L := ℒₛₑₜ) (n := 1) _

-- **`ve2_isUFormula` 未证**。`ve2 n k f w = qqAlls (imp (conjunct 3 n 0 w.[0] ⋏ (conjunct 3 n 1 w.[1] ⋏ ⊤))
-- (subst (^#2 ∷ ?[^#0, ^#1]) (cFunc k f))) 2`。要证它是公式，需要：
-- 1. `qqAlls`（`isUFormula_qqAlls`）✅、`imp`（`IsUFormula.imp`）✅、`⋏`（`IsUFormula.and`）✅、`⊤` ✅；
-- 2. **`conjunct 3 n i w.[i]` 是公式**——第一块已证（`CG008Conj.conjunct_fst_isUFormula`），
--    **第二块未证**（见 `CG008Conj` 的说明）；
-- 3. **`subst (^#2 ∷ ?[^#0, ^#1]) (cFunc k f)`**：`cFunc` 在 `k ≠ 0` 时是层 3 的公式
--    （`cFunc_isSemiformula_three` ✅），但替换向量的分量界是**算术界**——
--    与 `conjunct` 第二块同一类障碍（`V` 的 `LT` 是裸的）。
-- **所以 `ve2_isUFormula` 归结为两处**：`conjunct` 第二块 + 替换向量的算术界。

-- `conjunct` 的公式性未证。`conjunct b n i y = (subst ?[#i] cDomN) ⋏ (subst (#i ∷ shiftVec b n) y)`。
-- 本轮查清一处**层数事实**：`subst L w q` 要 `IsSemitermVec L n m w`，即 `len w = n`，
-- 而 `?[^#i]` 的 `len` 是 **1**（一个分量），与 `i` 无关。所以第一块在层 1 可直接用
-- `subst_singleton_isUFormula`；但该引理把替换向量的**下标**写死为 `^#0`，而这里要 `^#i`。
-- 把下标参数化的尝试（层取 `z + 1`）因 `len ?[^#z] = 1 ≠ z + 1` 未过——
-- **下一步**：`?[#i]` 的层数实为 `i + 1` 而非 `len`，需要用 `IsUTermVec` 的定义直接构造。

end GodelQ.CG008Ve2

#print axioms GodelQ.CG008Ve2.cFunc_isSemiformula_three
#print axioms GodelQ.CG008Ve2.isSemitermVec_ve2vec
