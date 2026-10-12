import GodelQ.ZFC.CG008Bv2

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BvZ
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 第 1 步：`bv_rel` 之后是 `listMax (termBVVec 2 ?[^#0,t])`
example (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.bv ℒₛₑₜ (Translate.eqAtom t)
      = Arithmetic.listMax (Bootstrapping.termBVVec ℒₛₑₜ 2 (?[^#0, t] : V)) := by
  have hv : Bootstrapping.IsUTermVec ℒₛₑₜ 2 (?[^#0, t] : V) :=
    Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
      ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0), ht⟩
  have hR : (ℒₛₑₜ).IsRel 2 (Translate.cEqN : V) := by
    rw [Translate.cEqN]
    exact (Bootstrapping.isRel_quote_quote (V := V) (L := ℒₛₑₜ) (k := 2)
      (x := Encodable.encode (Language.Eq.eq : (ℒₛₑₜ).Rel 2))).mpr
      ⟨Language.Eq.eq, rfl⟩
  rw [Translate.eqAtom, Bootstrapping.bv_rel hR hv]

-- 第 2 步：`termBVVec_cons` 两次——**只剩最后一条 `termBVVec_nil` 的宇宙/实例对齐**。
-- `termBVVec_cons` 两次都过了（目标已化到 `termBV ^#0 ∷ termBV t ∷ termBVVec L 0 0`），
-- 但 `termBVVec_nil`（`Term/Basic.lean:721`）在本上下文里宇宙不匹配
-- （报 `Eq.{1}` vs `Eq.{u_1+1}`），其来源 `resultVec_nil`（`:613`）是多元的，
-- 但要用它需给出 `termBV.construction`（`termBV` 是 `Function`，无 `.construction` 字段）。
-- **下一步**：查 `termBV` 的 `Construction` 实例名（它由 `IsUTerm.BV` 段的 blueprint 给出），
-- 或直接用 `len_zero_iff_eq_nil`（`resultVec_nil` 的证明正是用它）。

end GodelQ.CG008BvZ
