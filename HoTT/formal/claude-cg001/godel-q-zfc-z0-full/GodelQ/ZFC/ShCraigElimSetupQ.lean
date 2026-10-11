import GodelQ.ZFC.ShCraigElimBranches

/-!
# CG-007 · W8 第二层（十六）：`induction_setup` 的 `Q` 版（2026-10-11）

`ShCraigElimSetup.induction_setup` 的归纳不变量用的是

```
P d := Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d))
```

**这有语义问题**：`Provable T φ` 内部是 `∃ d, Proof d φ`，
而 `Proof d φ := DerivationOf T d {φ}`——它要求结论 sequent **恰好是单元素集**。
`translateSeq s` 一般不是单元素集，故 `P d` 在 `s ≠ {φ}` 时几乎必然为假。

正确的归纳不变量是 **`Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`**
（sequent 层），本文件给出 `Q` 版的 `induction_setup`。
`ShCraigElimBranches` 已填的 7 支证的就是 `Q`，可直接接入。

## 与 `P` 版的关系

`P` 版仍然有价值（它是 `Provable` 层的陈述，`Z0Blocked.lean` 那边可能需要），
但**归纳本身**必须在 `Q` 层做。若最终需要 `P` 层结论，再由
`Derivable.toProvable`（要求 `s = φ ⫽ ∅`）或 `Derivable.conj` 转换。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ShCraigElimSetupQ

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`Q` 版的归纳设置**：`Derivation Sh.craig d → Q d` 的 10 个规则支。

7 支已由 `ShCraigElimBranches` 给出；`hAll`/`hExs`/`hRoot` 仍空。 -/
theorem induction_setup_Q (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    Q (V := V) d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺 (hP := q_defined.to_definable) hd
  · exact fun s hs p hp hn ↦ ShCraigElimBranches.hAxL hs hp hn
  · exact fun s hs hv ↦ ShCraigElimBranches.hVerumIntro hs hv
  · exact fun s hs p q dp dq hpq hdp hdq ihp ihq ↦
      ShCraigElimBranches.hAnd hs hpq hdp.1 hdq.1 ihp ihq
  · exact fun s hs p q dd hpq hd ih ↦ ShCraigElimBranches.hOr hs hpq hd.1 ih
  · -- allIntro
    intro s _hs p _dd _hp _hd _ih
    simp only [Q, fstIdx_allIntro]
    sorry
  · -- exsIntro
    intro s _hs p t _dd _hp _ht _hd _ih
    simp only [Q, fstIdx_exsIntro]
    sorry
  · exact fun s hs dd h hd ih ↦ ShCraigElimBranches.hWk hs h ih
  · exact fun s hs dd h hd ih ↦ ShCraigElimBranches.hShift hs h ih
  · -- cutRule：hCut 需要 IsSemiformula ℒₒᵣ 0 p，从 p ∈ insert p s 与 hs 拿
    intro s hs p d₁ d₂ h₁ h₂ ih₁ ih₂
    -- p 的公式性：h₁ 的 DerivationOf 给 IsFormulaSet (insert p s)
    have hp : IsSemiformula ℒₒᵣ 0 p := h₁.isFormulaSet p (by simp)
    exact ShCraigElimBranches.hCut hs hp h₁.1 h₂.1 ih₁ ih₂
  · -- axm
    intro s _hs p _hps _hpT
    simp only [Q, fstIdx_axm]
    sorry


/-! ## 单边 LK 的析取引理（2026-10-11 新增）

`split_or`：`Derivable (insert (p ⋎ q) s) → Derivable (insert p (insert q s))`。
这是单边 LK 的 ∨R 可逆性，用 `cut (p⋎q)` + `neg_or`（De Morgan）+ `and_m` + `em`。
它是 `hAll` 收尾所需的 `replace_of_iff` 的零件之一。 -/

/-- **析取分裂**。 -/
lemma split_or {p q s : V} (hp : IsFormula ℒₛₑₜ p) (hq : IsFormula ℒₛₑₜ q)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (p ^⋎ q) s)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert p (insert q s)) := by
  have hfs : IsFormulaSet (L := ℒₛₑₜ) (insert p (insert q s)) := by
    intro y hy
    simp only [mem_bitInsert_iff] at hy
    rcases hy with rfl | rfl | hy
    · exact hp
    · exact hq
    · exact h.isFormulaSet y (by simp [hy])
  refine Derivable.cut (p ^⋎ q) ?_ ?_
  · refine Derivable.wk (s := insert (p ^⋎ q) (insert p (insert q s)))
      (s' := insert (p ^⋎ q) s) ?_ ?_ h
    · intro y hy
      simp only [mem_bitInsert_iff] at hy
      rcases hy with rfl | hy
      · exact IsSemiformula.or.mpr ⟨hp, hq⟩
      · exact hfs y (by simp only [mem_bitInsert_iff] at hy ⊢; tauto)
    · intro y hy
      simp only [mem_bitInsert_iff] at hy ⊢
      tauto
  · have hneg : neg ℒₛₑₜ (p ^⋎ q) = neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q :=
      neg_or hp.isUFormula hq.isUFormula
    rw [hneg]
    refine Derivable.and_m (s := insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q) (insert p (insert q s)))
      (p := neg ℒₛₑₜ p) (q := neg ℒₛₑₜ q) (by simp) ?_ ?_
    · refine Derivable.em (s := insert (neg ℒₛₑₜ p) (insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q)
          (insert p (insert q s)))) ?_ p ?_ ?_
      · intro y hy
        simp only [mem_bitInsert_iff] at hy
        rcases hy with rfl | rfl | rfl | rfl | hy
        · exact hp.neg
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact hp
        · exact hq
        · exact h.isFormulaSet y (by simp [hy])
      · simp [mem_bitInsert_iff]
      · simp [mem_bitInsert_iff]
    · refine Derivable.em (s := insert (neg ℒₛₑₜ q) (insert (neg ℒₛₑₜ p ^⋏ neg ℒₛₑₜ q)
          (insert p (insert q s)))) ?_ q ?_ ?_
      · intro y hy
        simp only [mem_bitInsert_iff] at hy
        rcases hy with rfl | rfl | rfl | rfl | hy
        · exact hq.neg
        · exact IsSemiformula.and.mpr ⟨hp.neg, hq.neg⟩
        · exact hp
        · exact hq
        · exact h.isFormulaSet y (by simp [hy])
      · simp [mem_bitInsert_iff]
      · simp [mem_bitInsert_iff]

end GodelQ.ShCraigElimSetupQ
