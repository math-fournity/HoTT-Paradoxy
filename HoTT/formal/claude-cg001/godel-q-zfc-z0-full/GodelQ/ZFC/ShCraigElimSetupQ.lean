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

## ⚠ 本文件的完成度（2026-10-11 实测）

`induction_setup_Q` 里 **7/10 支已填**（`hAxL`/`hVerumIntro`/`hAnd`/`hOr`/`hWk`/`hShift`/`hCut`），
**`hAll`/`hExs`/`hRoot` 三支仍带未证标记**。
本文件的其余部分（`split_or`、`replace_of_imp`）**完全无未证标记、exit 0**。

**不要**把本文件当成「已完成的消去」——它给出的是**框架 + 7 支 + 剩余三支的精确缺口**：

* `hAll`：归约已定型（`Derivable.all` + `replace_of_imp` + 一条算术蕴含式 `⊢ A → B`）；
* `hExs`：同形（`Derivable.exs`）；
* `hRoot`：**就是 D3 本身**（`iT 0 p ∈ 𝗭𝗙𝗖.Δ₁Class`）。

细节见 `形式化追踪/11-Claude交接-第二次接手-20261011.md` §2。

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


/-! ## 公式替换（2026-10-11 新增） -/

/-! `replace_of_imp`：给定 `¬A ⋎ B` 可导与 `insert A S` 可导，得 `insert B S` 可导。

证法：`cut A`。
* (i) `insert A (insert B S)` ← `wk hd`；
* (ii) `insert (neg A) (insert B S)` ← 从 `¬A ⋎ B` 经 **`split_or`**
  得 `insert (neg A) (insert B ∅)`，再 `wk`。

`split_or` 正好把 `¬A ⋎ B` 拆成 `¬A` 与 `B`——这是本引理的关键。 -/

lemma replace_of_imp {A B S : V}
    (hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ A ^⋎ B) ∅))
    (hA : IsFormula ℒₛₑₜ A) (hB : IsFormula ℒₛₑₜ B)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert B S) := by
  refine Derivable.cut A ?_ ?_
  · -- insert A (insert B S) ← wk hd
    refine Derivable.wk (s := insert A (insert B S)) (s' := insert A S) ?_ ?_ hd
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact hB
        · exact hS y hy
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact mem_bitInsert_iff.mpr (Or.inl rfl)
      · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inr hy)))
  · -- insert (neg A) (insert B S) ← split_or hAB 再 wk
    have h1 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ A) (insert B ∅)) :=
      split_or hA.neg hB hAB
    refine Derivable.wk (s := insert (neg ℒₛₑₜ A) (insert B S))
      (s' := insert (neg ℒₛₑₜ A) (insert B ∅)) ?_ ?_ h1
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA.neg
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact hB
        · exact hS y hy
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact mem_bitInsert_iff.mpr (Or.inl rfl)
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact mem_bitInsert_iff.mpr (Or.inr (mem_bitInsert_iff.mpr (Or.inl rfl)))
        · exact absurd hy (by simp)

end GodelQ.ShCraigElimSetupQ
