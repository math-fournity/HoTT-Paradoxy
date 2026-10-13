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
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

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


/-! ## `imp` 弱化（2026-10-12 新增）

`imp_wk`：`insert X S` 可导 ⟹ `insert (D 🡒 X) S` 可导。

单边 LK 里 `D 🡒 X = ¬D ⋎ X`：先把 `¬D` 弱化进 sequent，再用 `Derivable.or`。

**为什么它是 `hAll` 的关键**：`hAll` 的 `all_m` 要 `free ℒₛₑₜ q`（`q = imp domZero (iT 1 p)`），
而 `ih` 给的是 `iT 0 (free ℒₒᵣ p)`。此前几轮一直想把这两者证成**相等**——
那需要 `iT` 与 `substs1` 的一般交换律，极难。但 `free_imp_domZero` 给出

```
free ℒₛₑₜ (imp domZero X) = imp (subst ?[^&0] domZero) (free ℒₛₑₜ X)
```

于是**只需**从 `free ℒₛₑₜ (iT 1 p)` 弱化到 `imp D (free ℒₛₑₜ (iT 1 p))`——
这正是本引理，一步 `or` 即得，**不需要任何等式桥接**。 -/

/-- **`imp` 弱化**：`insert X S` 可导 ⟹ `insert (D 🡒 X) S` 可导。 -/
lemma imp_wk {D X S : V} (hD : IsFormula ℒₛₑₜ D) (hX : IsFormula ℒₛₑₜ X)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert X S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (imp ℒₛₑₜ D X) S) := by
  show Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (neg ℒₛₑₜ D ^⋎ X) S)
  refine Derivable.or (s := S) (p := neg ℒₛₑₜ D) (q := X) ?_
  refine Derivable.wk (s := insert (neg ℒₛₑₜ D) (insert X S))
    (s' := insert X S) ?_ ?_ h
  · intro y hy
    rcases mem_bitInsert_iff.mp hy with rfl | hy
    · exact hD.neg
    · rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hX
      · exact hS y hy
  · intro y hy
    exact mem_bitInsert_iff.mpr (Or.inr hy)

/-- **`hAll` 的前提归约**：`all_m` 要的 `free ℒₛₑₜ (imp domZero Y)` 可由 `free ℒₛₑₜ Y` 得到。

`all_m` 的前提是 `Derivable (insert (free ℒₛₑₜ q) (setShift (translateSeq s)))`，
其中 `q = imp ℒₛₑₜ domZero (iT 1 p)`（由 `iT_all` 强制）。`free_imp_domZero` 把
`free (imp domZero Y)` 拆成 `imp (subst ?[^&0] domZero) (free Y)`，再由 `imp_wk`
从 `Derivable (insert (free Y) S)` 得到所要的 sequent。

**关键**：本引理**不需要** `iT 0 (free ℒₒᵣ p)` 与 `free ℒₛₑₜ (iT 1 p)` 之间的任何**等式**——
那正是此前几轮反复受阻之处（等式确实是假的）。所需的只是**一次 ∨ 弱化**。 -/
lemma all_m_premise {Y S : V} (hY : IsSemiformula ℒₛₑₜ 1 Y)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (h : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (free ℒₛₑₜ Y) S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (free ℒₛₑₜ (imp ℒₛₑₜ domZero Y)) S) := by
  rw [free_imp_domZero hY]
  have hD : IsFormula ℒₛₑₜ (subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))) :=
    IsSemiformula.subst (L := ℒₛₑₜ) (n := (1:V)) (m := (0:V)) isSemiformula_domZero'
      (IsSemitermVec.singleton.mpr (IsSemiterm.fvar (L := ℒₛₑₜ) (V := V) (n := (0:V)) 0))
  exact imp_wk hD hY.free hS h

/-! ## 可证公式入 sequent（2026-10-12 新增） -/

/-- **「可证公式可入 sequent」**：`Derivable (A ⫽ ∅)` ⟹ `Derivable (A ⫽ B)`。 -/
lemma provable_into_sequent {A B : V} (hB : IsFormulaSet (L := ℒₛₑₜ) B)
    (hd : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A ∅)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A B) := by
  have hA : IsFormula ℒₛₑₜ A := hd.isFormulaSet A (by simp)
  have hf : IsFormulaSet (L := ℒₛₑₜ) (insert A B) := by
    intro z hz
    rcases mem_bitInsert_iff.mp hz with rfl | hz
    · exact hA
    · exact hB z (by simpa using hz)
  refine Derivable.wk hf ?_ hd
  intro z hz
  rcases mem_bitInsert_iff.mp hz with rfl | hz
  · exact mem_bitInsert_iff.mpr (Or.inl rfl)
  · exact mem_bitInsert_iff.mpr (Or.inr (by simpa using hz))

/-! ## `hRoot` 的核心归约（2026-10-12 新增）

`hRoot` 手里的假设是 `p ∈ s` 与 `p ∈ Sh.craig.Δ₁Class`，目标 `Derivable 𝗭𝗙𝗖 (translateSeq s)`。

**关键简化**：走 `Derivable.by_axm` 需要 `iT 0 p ∈ 𝗭𝗙𝗖.Δ₁Class`，那是**错的方向**
（`iT 0 p` 一般不是 `⌜φ⌝` 形）。正确的路是：只要 `iT 0 p` 在 V 内部**可证**，
`insert (iT 0 p) ∅` 就可导，再由 `wk` 搬到 `translateSeq s` 上——**完全不需要 `𝗭𝗙𝗖.Δ₁Class`**。

于是 `hRoot` 的剩余内容精确地变成一条**内部可证性**命题：

```
p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)
```

即「Craig 公理的翻译在 𝗭𝗙𝗖 中可证」，这条正是 `Sh.craig ⪯ Sh` 的内部化。 -/

/-- **可证公式入 sequent**：`A` 在 V 内部可证，且 `A ∈ B`，则 `B` 可导。 -/
lemma derivable_of_mem_of_provable {A B : V} (hB : IsFormulaSet (L := ℒₛₑₜ) B)
    (hAB : A ∈ B) (hprov : Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 A) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 B := by
  have hder : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert A ∅) :=
    internal_provable_iff_internal_derivable.mp hprov
  refine Derivable.wk (s := B) (s' := insert A ∅) hB ?_ hder
  intro z hz
  rcases mem_bitInsert_iff.mp hz with rfl | hz
  · exact hAB
  · exact absurd hz (Arithmetic.not_mem_empty z)

/-- **`hRoot` 的核心**：`p ∈ s` 且 `iT 0 p` 内部可证 ⟹ `translateSeq s` 可导。

于是 `hRoot` 支的剩余义务只有一条：`p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`。 -/
lemma hRoot_core {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (hp : p ∈ s)
    (hprov : Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) p)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq s) :=
  derivable_of_mem_of_provable (ShCraigElimBranches.isFormulaSet_translateSeq hs)
    (mem_translateSeq_iff.mpr ⟨p, hp, rfl⟩) hprov

end GodelQ.ShCraigElimSetupQ
