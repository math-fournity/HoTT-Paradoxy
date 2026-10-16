-- CG-009: hAll — assembling the reduction with verified tools.
-- Route (9276's定型): Derivable.all + replace_of_imp + the arithmetic implication A → B.
import GodelQ.ZFC.SetupQTools
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.HAllProof
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- The remaining arithmetic implication: A → B where
--   A := iT 0 (free ℒₒᵣ p)        (the translated premise, no guard)
--   B := free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))    (the guarded premise all_m wants)
-- 9276 定型的归约：先 replace_of_imp 把 insert A S 换成 insert B S。
-- 因为 hAll 的 ih 给的是 Derivable (insert (free p) (setShift s))（ℒₒᵣ 侧），
-- 经 translateSeq_insert 后变成 insert (iT 0 (free p)) (setShift (translateSeq s))。
-- 而 all_m 需要 insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s))。

/-- The membership fact for `all_m`: `^∀ (imp domZero (iT 1 p)) ∈ translateSeq s`. -/
lemma all_mem {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (hp : (^∀ p : V) ∈ s)
    (hpU : IsUFormula ℒₒᵣ p) :
    (^∀ (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p)) : V) ∈ translateSeq (V := V) s := by
  rw [mem_translateSeq_iff]
  refine ⟨^∀ p, hp, ?_⟩
  rw [iT_all hpU]
  norm_num

/-- **`hAll`, unconditional** (modulo the arithmetic implication).

`all_m` needs the premise at `insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s))`,
while `ih` gives it at `insert (iT 0 (free ℒₒᵣ p)) (setShift (translateSeq s))`.
`replace_of_imp` bridges the two given the arithmetic implication `A → B` where
`A := iT 0 (free ℒₒᵣ p)`, `B := free ℒₛₑₜ (imp domZero (iT 1 p))` (via `free_imp_domZero`). -/
theorem hAll_uncond {s p d : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p : V) ∈ s)
    (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s)))
    (ih : Q d)
    -- the one remaining arithmetic implication (Σ1 completeness range)
    (hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0 : V) (free (L := ℒₒᵣ) p))
        ^⋎ free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p))) ∅)) :
    Q (allIntro s p d) := by
  simp only [Q, fstIdx_allIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.all.mp ((hs (^∀ p) hp).isUFormula))
  have hpS : IsSemiformula ℒₒᵣ 1 p := by
    -- IsSemiformula.all : IsSemiformula n (^∀ p) ↔ IsSemiformula (n+1) p
    have := (IsSemiformula.all (L := ℒₒᵣ) (n := 0)).mp (hs (^∀ p) hp)
    simpa using this
  -- ih at the translated premise
  have ih' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V)
      (insert (free (L := ℒₒᵣ) p) (setShift (L := ℒₒᵣ) s))) := by
    rw [← hd.1]; exact ih
  rw [translateSeq_insert] at ih'
  rw [GodelQ.TShiftFull.tshift s hs] at ih'
  -- ih' : Derivable (insert (iT 0 (free p)) (setShift (translateSeq s)))
  -- Apply replace_of_imp to swap A := iT 0 (free p) with B := free ℒₛₑₜ (imp domZero (iT 1 p))
  have hA : IsFormula ℒₛₑₜ (iT (0 : V) (free (L := ℒₒᵣ) p)) := by
    have := isSemiformula_iT (free (L := ℒₒᵣ) p) (IsSemiformula.free hpS)
    exact ⟨this.isUFormula, by simpa using this.bv_le⟩
  have hB : IsFormula ℒₛₑₜ (free ℒₛₑₜ (imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p))) := by
    apply IsSemiformula.free
    exact IsSemiformula.imp.mpr ⟨GodelQ.TranslateShiftCompat.isSemiformula_domZero',
      isSemiformula_iT p hpS⟩
  have hS : IsFormulaSet (L := ℒₛₑₜ) (setShift (L := ℒₛₑₜ) (translateSeq (V := V) s)) :=
    IsFormulaSet.setShift (isFormulaSet_translateSeq hs)
  have ih'' := GodelQ.SetupQTools.replace_of_imp hAB hA hB hS ih'
  -- Now apply all_m with p := imp domZero (iT 1 p) and s := setShift (translateSeq s)
  refine Derivable.all_m (T := 𝗭𝗙𝗖)
    (s := translateSeq (V := V) s)
    (p := imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p)) ?_ ?_
  · exact all_mem hs hp hpU
  · exact ih''

end GodelQ.HAllProof

#print axioms GodelQ.HAllProof.hAll_uncond
