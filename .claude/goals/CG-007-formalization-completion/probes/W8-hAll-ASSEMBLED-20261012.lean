import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeHAll
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma weaken_imp {A D X : V} (hA : IsFormula ℒₛₑₜ A) (hD : IsFormula ℒₛₑₜ D)
    (hX : IsFormulaSet (L := ℒₛₑₜ) X)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A X)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ D A) X) := by
  show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ D ^⋎ A) X)
  refine Derivable.or (T := 𝗭𝗙𝗖) (s := X) (p := neg ℒₛₑₜ D) (q := A) ?_
  refine Derivable.wk (T := 𝗭𝗙𝗖) (s := insert (neg ℒₛₑₜ D) (insert A X))
    (s' := insert A X) ?_ ?_ hd
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact hD.neg
    · rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA
      · exact hX y hy
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inl rfl)))
    · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inr hy)))

/-- `hAll` 支：`^∀ p ∈ s`，子推导在 `insert (free p) (setShift s)` 上。

**归约**：
* `iT 0 (^∀ p) = ^∀ (imp domZero (iT 1 p))`（`iT_all`），故 `translateSeq s` 含该全称；
* `Derivable.all` 需要 `Derivable (insert (free q) (setShift (translateSeq s)))`，`q := imp domZero (iT 1 p)`；
* ~~`free q = D → iT 0 (free p)`~~（`free_imp_domZero` + `iT_free`），
  `ih` 给 `Derivable (insert (iT 0 (free p)) (setShift (translateSeq s')))`，
  经 `weaken_imp` 得目标。 -/
lemma hAll {s p d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : (^∀ p) ∈ s)
    (hd : fstIdx d = insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))
    (ih : Q (V := V) d) :
    Q (V := V) (allIntro s p d) := by
  simp only [Q, fstIdx_allIntro]
  -- `q := imp domZero (iT 1 p)`
  set q : V := imp ℒₛₑₜ (domZero (V := V)) (iT (1 : V) p) with hq
  -- `^∀ q ∈ translateSeq s`
  have hpa : IsSemiformula ℒₒᵣ 1 p := by
    have h := IsSemiformula.all.mp (hs (^∀ p) hp)
    rw [show (0 : V) + 1 = 1 by norm_num] at h
    exact h
  have hfs : IsFormulaSet (L := ℒₒᵣ) (setShift ℒₒᵣ s) :=
    (IsFormulaSet.setShift_iff).mpr hs
  have hfp : IsFormula ℒₒᵣ (free ℒₒᵣ p) := hpa.free
  have hfs' : IsFormulaSet (L := ℒₒᵣ) (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s)) :=
    IsFormulaSet.insert_iff.mpr ⟨hfp, hfs⟩
  have hfs'' : IsFormulaSet (L := ℒₛₑₜ) (setShift ℒₛₑₜ (translateSeq s)) :=
    (IsFormulaSet.setShift_iff).mpr (isFormulaSet_translateSeq hs)
  -- `ih` 展开
  have ih' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (iT (0 : V) (free ℒₒᵣ p)) (setShift ℒₛₑₜ (translateSeq s))) := by
    have h := ih
    rw [Q, hd] at h
    rw [translateSeq_insert] at h
    rw [translateSeq_setShift hs] at h
    exact h
  -- `^∀ q ∈ translateSeq s`
  have hmem : (^∀ q) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∀ p), hp, by
      rw [hq]
      exact (iT_all (V := V) (n := (0 : V)) hpa.isUFormula).trans
        (congrArg (fun z => (^∀ (imp ℒₛₑₜ (domZero (V := V)) z) : V))
          (by rw [show (0 : V) + 1 = 1 by norm_num])) |>.symm⟩
  -- `Derivable.all` 之后再用 `all_m` 把 `^∀ q ∈ translateSeq s` 消掉
  refine Derivable.all_m (T := 𝗭𝗙𝗖) (s := translateSeq s) (p := q) hmem ?_
  -- `Derivable (insert (free q) (setShift (translateSeq s)))`
  rw [hq]
  -- `free (imp domZero X) = D → free X`（`free_imp_domZero`），`X := iT 1 p`
  rw [free_imp_domZero (V := V) (isSemiformula_iT (V := V) (n := (1 : V)) p hpa)]
  -- 目标：`Derivable (insert (D → free (iT 1 p)) (setShift (translateSeq s)))`
  -- `weaken_imp` 取 `A := free (iT 1 p)`、`D := subst ?[^&0] cDomN`、`X := setShift (translateSeq s)`
  refine weaken_imp (V := V) ?_ ?_ hfs'' ?_
  · -- `IsFormula A`：`free (iT 1 p)`
    exact (isSemiformula_iT (V := V) (n := (1 : V)) p hpa).free
  · -- `IsFormula D`：`D = subst ?[^&0] cDomN`（`free_imp_domZero` 的产物）
    refine IsSemiformula.subst (L := ℒₛₑₜ) ?_
      (IsSemitermVec.adjoin (IsSemitermVec.empty (L := ℒₛₑₜ) (V := V) (0 : V))
        (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := 0) 0))
    rw [domZero_eq_cDomN (V := V)]
    rw [show (0 : V) + 1 = 1 by norm_num]
    exact isSemiformula_cDomN (V := V)
  · -- **2026-10-12 修正版**：不用 `iT_free` 等式（已证伪）。
    -- 目标 `Derivable (insert (D → free (iT 1 p)) X)`。
    -- 思路：`weaken_imp` 反向走不通（要 A 的自由性），改用
    -- **两条公式的互相可导性**经 `Derivable.cut` 搬运：
    --   (A) Provable 𝗭𝗙𝗖 (imp (iT 0 (free p)) (free (iT 1 p)))
    --   (B) Provable 𝗭𝗙𝗖 (imp (free (iT 1 p)) (iT 0 (free p)))
    -- 先测 (A)/(B) 是否为**命题恒真式**（若是，可直接由 𝗭𝗙𝗖 的公理模式给出）。
    have hX := hfs''
    have hA : IsFormula ℒₛₑₜ (iT (0:V) (free ℒₒᵣ p)) :=
      (isSemiformula_iT (V := V) (n := (0:V)) (free ℒₒᵣ p) hpa.free.to_isSemiformula').free
    sorry

end GodelQ.ProbeHAll


/-! ## 2026-10-12 结论记录

上面这一处 `sorry` 的门槛被之前的判定高估了。现已知：

1. `iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (iT 1 p)` **作为等式为假**（机器归一化）。
2. 本文件其余 100 余行全部 exit 0，包括：
   * `weaken_imp`（`Derivable (A ⫽ X) → Derivable ((D→A) ⫽ X)`）✅
   * `ih'` 的三步搬运 ✅
   * `hmem`（`^∀ q ∈ translateSeq s`）✅
   * `Derivable.all_m` 的两次 refine ✅
   * `free_imp_domZero` 的改写 ✅
3. 所以 `hAll` 的实际剩余工作 = 把最后那一步从「等式」改成「互相可导」，
   而不是去证一条假等式。这一步的强度远低于原先的估计。 -/
