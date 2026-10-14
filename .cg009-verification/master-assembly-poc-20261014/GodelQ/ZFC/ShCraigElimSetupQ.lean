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

/-! ## 三个**显式命名**的阻塞义务（2026-10-13）

`induction_setup_Q` 的 10 支里 7 支已证（`ShCraigElimBranches`）。
剩下三支**不是未证标记**，而是**三条显式命名的假设**——
这正是 GOAL.md 完成门 2 允许的「照实写明阻塞引理」的**机器可验证形态**：
`induction_setup_Q_of_blockers` 把三条义务作为**参数**，其证明**完整**。

| 支 | 义务 | 性质 |
|---|---|---|
| `hAll` | `AllBlocker` | `iT` 与 `free`/`subst` 的相容（§12.56：语言错配，需 `iVE-像`） |
| `hExs` | `ExsBlocker` | `iT` 与 `substs1` 的相容（§12.55：`substs1 t' domZero ≠ domZero`） |
| `hRoot` | `RootBlocker` | `p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`（D3 本身） |

**每条的精确形状**写在下面的 `def` 里，`induction_setup_Q_of_blockers`
的**证明是完整的**（无未证标记）。
本包因此**不再含任何未证标记**——
`ShCraigElim` 等价于「这三条 blocker 同时成立」。 -/

/-- **`hAll` 的阻塞义务**（精确形状，供舰队/后续会话直接引用）。

`allIntro` 支：`s` 是公式集、`^∀ p ∈ s`、子推导 `dd` 在
`insert (free ℒₒᵣ p) (setShift s)` 上、`ih : Q dd`。
要证 `Q (allIntro s p dd)`，即 `Derivable (translateSeq s)`。

**精确义务**：把 `ih`（在 `translateSeq (insert (free ℒₒᵣ p) (setShift s))` 上）
搬到 `Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s)))`。 -/
def AllBlocker : Prop :=
  ∀ {s p dd : V}, IsFormulaSet (L := ℒₒᵣ) s → IsSemiformula ℒₒᵣ (1:V) p →
    fstIdx dd = insert (free ℒₒᵣ p) (setShift (L := ℒₒᵣ) s) →
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx dd)) →
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq s)

/-- 同上，但结论写成 `Q` 的形状（`allIntro` 支的直接形式）。

⚠ **2026-10-13 更正**：此前这一条**只有 `Q dd` 假设，丢掉了 `Derivation Sh.craig dd`**，
于是它**过强**——`induction1` 的支里 `hd.2 : Derivation Sh.craig dd` 是现成的、
且携带实质信息。缺了它，取 `p = ⊤` 时 `free ⊤ = ⊤`，
`Q dd` 退化成「sequent 里有 `⊤`」，对**任意** `s` 无条件成立，
blocker 便蕴含 `∀ s, ^∀ ⊤ ∈ s → Derivable (translateSeq s)`。
机器证明见 `probes/W8-blockers-TOO-STRONG-20261013.lean`。
现补回 `Derivation Sh.craig dd`，与 `induction1` 支手里的一致。 -/
def AllBlockerQ : Prop :=
  ∀ {s p dd : V}, IsFormulaSet (L := ℒₒᵣ) s → ^∀ p ∈ (s : V) →
    fstIdx dd = insert (free ℒₒᵣ p) (setShift (L := ℒₒᵣ) s) →
    Derivation (V := V) (L := ℒₒᵣ) Sh.craig dd →
    Q (V := V) dd → Q (V := V) (allIntro s p dd)

/-- **`hExs` 的阻塞义务**（精确形状）。

`exsIntro` 支：`^∃ p ∈ s`、`IsTerm ℒₒᵣ t`、`fstIdx dd = insert (substs1 ℒₒᵣ t p) s`。
**精确义务**：把 `ih` 搬到 `Derivable (translateSeq s)`。 -/
def ExsBlocker : Prop :=
  ∀ {s p t dd : V}, IsFormulaSet (L := ℒₒᵣ) s → IsSemiformula ℒₒᵣ (1:V) p →
    IsTerm ℒₒᵣ t →
    fstIdx dd = insert (substs1 ℒₒᵣ t p) s →
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (fstIdx dd)) →
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq s)

/-- 同上，但结论写成 `Q` 的形状（`exsIntro` 支的直接形式）。

⚠ **2026-10-13 更正**：与 `AllBlockerQ` 同一缺陷——丢了 `Derivation Sh.craig dd`。
取 `p = ⊤` 时 `substs1 t ⊤ = ⊤`，`Q dd` 退化成「sequent 里有 `⊤`」，
blocker 便蕴含 `∀ s, ^∃ ⊤ ∈ s → Derivable (translateSeq s)`。
机器证明见 `probes/W8-blockers-TOO-STRONG-20261013.lean`。 -/
def ExsBlockerQ : Prop :=
  ∀ {s p t dd : V}, IsFormulaSet (L := ℒₒᵣ) s → ^∃ p ∈ (s : V) →
    IsTerm ℒₒᵣ t →
    fstIdx dd = insert (substs1 ℒₒᵣ t p) s →
    Derivation (V := V) (L := ℒₒᵣ) Sh.craig dd →
    Q (V := V) dd → Q (V := V) (exsIntro s p t dd)

/-- **`hRoot` 的阻塞义务**（`axm` 支，**就是 D3 本身**）。

`s` 是公式集、`p ∈ s`、`p ∈ Sh.craig.Δ₁Class`。
**精确义务**：`Derivable (translateSeq s)`。 -/
def RootBlocker : Prop :=
  ∀ {s p : V}, IsFormulaSet (L := ℒₒᵣ) s → p ∈ s → p ∈ Sh.craig.Δ₁Class →
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq s)

/-- 同上，但结论写成 `Q` 的形状（`axm` 支的直接形式）。 -/
def RootBlockerQ : Prop :=
  ∀ {s p : V}, IsFormulaSet (L := ℒₒᵣ) s → p ∈ s → p ∈ Sh.craig.Δ₁Class →
    Q (V := V) (axm s p)

/-- **`Q` 版的归纳设置**：`Derivation Sh.craig d → Q d` 的 10 个规则支。

**三条阻塞义务作为参数**（`hAll`/`hExs`/`hRoot`），
**证明本身完整**——本包因此不含任何未证标记。 -/
theorem induction_setup_Q_of_blockers (hAllB : AllBlockerQ (V := V))
    (hExsB : ExsBlockerQ (V := V)) (hRootB : RootBlockerQ (V := V))
    (d : V) (hd : Derivation (V := V) (L := ℒₒᵣ) Sh.craig d) :
    Q (V := V) d := by
  apply Derivation.induction1 (T := Sh.craig) 𝚺 (hP := q_defined.to_definable) hd
  · exact fun s hs p hp hn ↦ ShCraigElimBranches.hAxL hs hp hn
  · exact fun s hs hv ↦ ShCraigElimBranches.hVerumIntro hs hv
  · exact fun s hs p q dp dq hpq hdp hdq ihp ihq ↦
      ShCraigElimBranches.hAnd hs hpq hdp.1 hdq.1 ihp ihq
  · exact fun s hs p q dd hpq hd ih ↦ ShCraigElimBranches.hOr hs hpq hd.1 ih
  · -- allIntro：交给 AllBlocker（`fstIdx (allIntro s p dd) = s`）
    intro s hs p dd hp hd ih
    exact hAllB hs hp hd.1 hd.2 ih
  · -- exsIntro：交给 ExsBlocker（`fstIdx (exsIntro s p t dd) = s`）
    intro s hs p t dd hp ht hd ih
    exact hExsB hs hp ht hd.1 hd.2 ih
  · exact fun s hs dd h hd ih ↦ ShCraigElimBranches.hWk hs h ih
  · exact fun s hs dd h hd ih ↦ ShCraigElimBranches.hShift hs h ih
  · intro s hs p d₁ d₂ h₁ h₂ ih₁ ih₂
    have hp : IsSemiformula ℒₒᵣ 0 p := h₁.isFormulaSet p (by simp)
    exact ShCraigElimBranches.hCut hs hp h₁.1 h₂.1 ih₁ ih₂
  · -- axm：交给 RootBlocker（`fstIdx (axm s p) = s`）
    intro s hs p hps hpT
    exact hRootB hs hps hpT

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

/-! ## `hAll` 支的组装（2026-10-12 新增）

`hAll` 的 `all_m` 有两条前提，本节的三个引理分别处理：

| 前提 | 引理 |
|---|---|
| `^∀ (imp domZero (iT 1 p)) ∈ translateSeq s` | `hAll_mem`（`iT_all` + `mem_translateSeq_iff`） |
| `Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) S)` | `all_m_premise`（`free_imp_domZero` + `imp_wk`） |

`hAll_reduce` 把两者拼起来，并把 `hAll` 的**全部**剩余压成一条形状干净的假设
`T = free ℒₛₑₜ (iT 1 p)`——即 `ih` 手里的 `iT 0 (free ℒₒᵣ p)` 要换成 `free ℒₛₑₜ (iT 1 p)`。
**注意**：那一步**不需要等式**，只需要在 sequent 层可换（见 §11 的说明）。 -/

/-- **`all_m` 的第二条前提的元素归属**：`^∀ (imp domZero (iT 1 p)) ∈ translateSeq s`。 -/
lemma hAll_mem {p s : V} (hp : IsUFormula ℒₒᵣ p) (hs : ^∀ p ∈ (s : V)) :
    (^∀ (imp ℒₛₑₜ (domZero (V := V)) (iT (1:V) p)) : V) ∈ translateSeq s :=
  mem_translateSeq_iff.mpr ⟨(^∀ p : V), hs,
    ((iT_all (n := (0:V)) hp).trans (by rw [show ((0:V) + 1) = (1:V) by norm_num])).symm⟩

/-- **`hAll` 支的归约**：`all_m` 的全部前提组装完毕，剩余压到一条 `hT`。

`ih` 给的是 `Derivable (insert T S)`，其中 `T` 应当是 `free ℒₛₑₜ (iT 1 p)`；
本引理把它送到 `all_m` 要的 `free ℒₛₑₜ (imp domZero (iT 1 p))`。 -/
lemma hAll_reduce {p S T : V}
    (hp : IsSemiformula ℒₒᵣ 1 p)
    (hS : IsFormulaSet (L := ℒₛₑₜ) S)
    (hT : T = free ℒₛₑₜ (iT (1:V) p))
    (ih : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert T S)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1:V) p))) S) := by
  subst hT
  exact all_m_premise (isSemiformula_iT (n := (1:V)) p hp) hS ih

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


/-! ## ★ `hAll` 的**精确剩余**：一条内部可证性 `AllKey`（2026-10-13）

`AllBlockerQ` 的 `ih` 给

```
Derivable (translateSeq (insert (free ℒₒᵣ p) (setShift s)))
  = Derivable (insert (iT 0 (free ℒₒᵣ p)) (setShift (translateSeq s)))
```

目标 `Derivable (translateSeq s)`。走 `Derivable.all_m`（`q := imp domZero (iT 1 p)`）：

| 前提 | 来源 |
|---|---|
| `^∀ q ∈ translateSeq s` | `hAll_mem`（已证） |
| `Derivable (insert (free q) (setShift (translateSeq s)))` | `hAll_reduce` → 只要 `free (iT 1 p)` 版 |

而 `free (iT 1 p)` 版由 `ih` 经 `replace_of_imp` 得到，**只要一条内部可证性**：

```
AllKey : Provable 𝗭𝗙𝗖 (imp (iT 0 (free ℒₒᵣ p)) (free ℒₛₑₜ (iT 1 p)))
```

**这把 `hAll` 从「一条等式」压成「一条内部可证性」**：
* 与 `ExsBridge2` 同形（都是 `Provable (imp …)`）——**比等式弱**，故更可能为真；
* **不要求 `p` 是引号形**，故不受非标准码反例影响
  （见 `CLAIM-Z0-W8-HALL-BLOCKER.md` §4.6）。

此前的记录把 `hAll` 的剩余写成
`iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (iT 1 p)`——**那条等式已机器证伪**（`domZero` 计数不同）。
**`AllKey` 是它的弱化版**：不要求两侧相等，只要求左侧**蕴含**右侧。 -/

/-- **`hAll` 的精确剩余**：`iT 0 (free p)` → `free (iT 1 p)` 的内部可证性。

这是 `hAll` 支**唯一**未证的部分（其余全部由 `ShCraigElimSetupQ.hAll_mem`/`ShCraigElimSetupQ.hAll_reduce`/`ShCraigElimSetupQ.replace_of_imp` 给出）。
形状是 `Provable (imp …)`——**蕴含，不是等式**。 -/
def AllKey : Prop :=
  ∀ {p : V}, IsSemiformula ℒₒᵣ (1:V) p →
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (imp ℒₛₑₜ (iT (0:V) (free ℒₒᵣ p)) (free ℒₛₑₜ (iT (1:V) p)))

/-- **归约**：`AllKey` ⟹ `AllBlockerQ`（证明完整，exit 0，公理三条）。

证法：`Derivable.all_m` 在 `translateSeq s` 上（`q := imp domZero (iT 1 p)`），
两条前提分别由 `hAll_mem` 与（`hAll_reduce` ∘ `replace_of_imp`）给出。 -/
theorem allBlockerQ_of_key (hk : AllKey (V := V)) :
    AllBlockerQ (V := V) := by
  intro s p dd hs hps hfd hder ih
  unfold Q at ih ⊢
  rw [fstIdx_allIntro]
  rw [hfd, translateSeq_insert, ShCraigElimBranches.translateSeq_setShift hs] at ih
  have hp1 : IsSemiformula ℒₒᵣ (1:V) p := by
    have h0 : IsFormula ℒₒᵣ (^∀ p) := hs (^∀ p) hps
    simpa using (IsSemiformula.all (L := ℒₒᵣ) (n := (0:V)) (p := p)).mp h0
  have hpU : IsUFormula ℒₒᵣ p := hp1.isUFormula
  let S : V := setShift (L := ℒₛₑₜ) (translateSeq (V := V) s)
  have hS : IsFormulaSet (L := ℒₛₑₜ) S := by
    intro y hy
    rcases mem_setShift_iff.mp hy with ⟨z, hz, rfl⟩
    exact (ShCraigElimBranches.isFormulaSet_translateSeq hs z hz).shift
  have hmem : ((^∀ (imp ℒₛₑₜ (domZero (V := V)) (iT (1:V) p)) : V)) ∈ translateSeq s :=
    ShCraigElimSetupQ.hAll_mem hpU hps
  have hpre : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (free ℒₛₑₜ (iT (1:V) p)) S) := by
    have hAB : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
        (insert (imp ℒₛₑₜ (iT (0:V) (free ℒₒᵣ p)) (free ℒₛₑₜ (iT (1:V) p))) ∅) :=
      internal_provable_iff_internal_derivable.mp (hk hp1)
    exact ShCraigElimSetupQ.replace_of_imp hAB
      (isSemiformula_iT (n := (0:V)) (free ℒₒᵣ p) hp1.free)
      (isSemiformula_iT (n := (1:V)) p hp1).free
      hS ih
  have hpre' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1:V) p))) S) :=
    ShCraigElimSetupQ.hAll_reduce hp1 hS rfl hpre
  exact Derivable.all_m hmem hpre'

/-! ## ★ `hRoot` 的**精确剩余**：一条内部可证性 `RootKey`（2026-10-14）

与 `AllKey` 同形地，把 `RootBlockerQ` 压成一条 `Provable`：

```
RootKey : ∀ p, p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)
```

此前这一步只写在交接文档与探针里（`accept_root_via_reduction`，
`probes/W8-blocker-acceptance-bench-20261013.lean`）——**没有进生产包**。
这里把它固化成命名 `def` 并给出归约定理，使三条 blocker 的剩余**形状统一**：

| 支 | 剩余 | 形状 |
|---|---|---|
| `hAll` | `AllKey` | `Provable (imp (iT 0 (free p)) (free (iT 1 p)))` |
| `hExs` | `ExsBridge2`（003/004 线） | `Provable (imp (iT 0 (p[t])) (^∃ (domZero ⋏ iT 1 p)))` |
| `hRoot` | `RootKey` | `p ∈ Sh.craig.Δ₁Class → Provable (iT 0 p)` |

**`RootKey` 就是 D3 本身**（`Sh.craig ⪯ Sh` 的内化）——本归约**不解决 D3**，
只是把义务搬到那一层、形状更小，且与另两条**可对接**。 -/

/-- **`hRoot` 的精确剩余**：Craig 公理的翻译在 𝗭𝗙𝗖 中可证（= D3 的内化）。 -/
def RootKey : Prop :=
  ∀ {p : V}, p ∈ Sh.craig.Δ₁Class →
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) p)

/-- **归约**：`RootKey` ⟹ `RootBlockerQ`（证明完整，exit 0，公理三条）。

证法一行：`hRoot_core hs hps (hk hpT)`。 -/
theorem rootBlockerQ_of_key (hk : RootKey (V := V)) :
    RootBlockerQ (V := V) := by
  intro s p hs hps hpT
  unfold Q
  rw [fstIdx_axm]
  exact hRoot_core hs hps (hk hpT)

/-! ## ★ `hExs` 的**精确剩余**：`ExsBridge2`（2026-10-13，004-Step 证；本提交移入生产包）

与 `AllKey`/`RootKey` 同形，`ExsBlockerQ` 压成一条 `Provable`：

```
ExsBridge2 : ∀ p t, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
    Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 ℒₒᵣ t p)) (^∃ (domZero ⋏ iT 1 p)))
```

即「`p[t] → ∃x(x ∈ ω ∧ p(x))`」。

**旧形状 `ExsBridge`（`∀ T'` 量化）为假**：取 `T' = ^&0` 需 `⊢ ∀x (x ∈ ω)`——
带自由变量的 `Provable φ` 在 LK 里等价于 `⊢ ∀x φ`。反例 `p = #0 = #0`、`t = ^&0`。
**`ExsBridge2` 不要求单个见证项**，只要与 sequent 里的 ∃ 公式**同形**的蕴含。

**归约**（`exsBlockerQ_of_bridge2`，证明完整）：
桥给 `¬A ⋎ ∃` → `split_or` 拆成 `{¬A, ∃}` → `wk` 得 `Derivable (insert (¬A) S)`
（**`∃ ∈ S` 是关键**）→ `cut A`。

**出处**：`probes/W8-ExsBridge2-corrected-20261013.lean`（004-Step）。
本提交把它移入生产包，使**三条 blocker 的剩余齐聚一处**（各一条 `Provable`）。 -/

/-- **`hExs` 的精确剩余**：`p[t] → ∃x (x ∈ ω ∧ p(x))`。 -/
def ExsBridge2 : Prop :=
  ∀ {p t : V}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (imp ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V))

/-- **归约**：`ExsBridge2` ⟹ `ExsBlockerQ`（证明完整，exit 0，公理三条）。 -/
theorem exsBlockerQ_of_bridge2 (hBr : ExsBridge2 (V := V)) :
    ExsBlockerQ (V := V) := by
  intro s p t dd hs hps ht hfd hder ih
  unfold Q at ih ⊢
  rw [fstIdx_exsIntro]
  rw [hfd, translateSeq_insert] at ih
  have hpex : IsSemiformula ℒₒᵣ (1:V) p := by
    have h0 : IsFormula ℒₒᵣ (^∃ p) := hs (^∃ p) hps
    simpa using (IsSemiformula.exs (L := ℒₒᵣ) (n := (0:V)) (p := p)).mp h0
  have hp : IsUFormula ℒₒᵣ p := hpex.isUFormula
  have hS : IsFormulaSet (L := ℒₛₑₜ) (translateSeq s) :=
    ShCraigElimBranches.isFormulaSet_translateSeq hs
  have hmem : ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∃ p : V), hps, (iT_exs (V := V) (n := (0:V)) hp).symm⟩
  have hA : IsFormula ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)) :=
    isSemiformula_iT (n := (0:V)) (substs1 ℒₒᵣ t p)
      (IsSemiformula.substs1 (L := ℒₒᵣ) (n := (0:V)) ht hpex)
  have hE : IsFormula ℒₛₑₜ ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) :=
    (IsSemiformula.exs (L := ℒₛₑₜ) (n := (0:V))
      (p := ((domZero (V := V)) ^⋏ iT (0+1:V) p))).mpr
      (IsSemiformula.and.mpr
        ⟨isSemiformula_domZero (V := V) (n := (0:V)),
         isSemiformula_iT (n := (0+1:V)) p (by simpa using hpex)⟩)
  have hW : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (imp ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V)) ∅) :=
    internal_provable_iff_internal_derivable.mp (hBr hp ht)
  have hsplit : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)))
        (insert ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∅)) :=
    split_or hA.neg hE hW
  have hnegA : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))) (translateSeq s)) := by
    refine Derivable.wk
      (s := insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))) (translateSeq s))
      (s' := insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)))
        (insert ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∅)) ?_ ?_ hsplit
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA.neg
      · exact hS y hy
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact mem_bitInsert_iff.mpr (Or.inl rfl)
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact mem_bitInsert_iff.mpr (Or.inr hmem)
        · exact absurd hy (Arithmetic.not_mem_empty y)
  exact Derivable.cut (iT (0:V) (substs1 ℒₒᵣ t p)) ih hnegA

/-! ## ★ `AllKey` 由「`iT` 与 `subst` 的桥」推出（2026-10-14）

`AllKey` 只要**蕴含**，但它可以由一条**等式**推出（`imp A A` 永真）：

```
iT 0 (free ℒₒᵣ p) = subst ?[^&0] (iT 1 (shift ℒₒᵣ p))    -- 桥 B(q := shift ℒₒᵣ p)
                  = subst ?[^&0] (shift ℒₛₑₜ (iT 1 p))    -- iT_shift（已证）
                  = free ℒₛₑₜ (iT 1 p)                    -- free 的定义
```

**桥 `B`** 正是 003 线的 `iT_substs1'`（层 1 版）：
`subst ?[^&0] (iT 1 q) = iT 0 (subst ?[^&0] q)`，取 `q = shift ℒₒᵣ p`。

**意义**：`hAll` 的 `AllKey` 与 003 线的桥**接上了**——
桥一通，`AllKey` 即得（不必另证）。
这也说明此前把 `hAll` 剩余记成
`iT 0 (free p) = free (iT 1 p)` **并不荒谬**——
那条等式**就是**由桥 + `iT_shift` 得到的；
它「被证伪」指的是**不带桥的朴素版本**（`domZero` 计数不同）。 -/

/-- **`AllKey` 由层 1 的桥推出**（证明完整，exit 0，公理三条）。 -/
theorem allKey_of_bridge
    (hB : ∀ {q : V}, IsSemiformula ℒₒᵣ (1:V) q →
      subst ℒₛₑₜ (?[^&0] : V) (iT (1:V) q) =
        iT (0:V) (subst ℒₒᵣ (?[^&0] : V) q)) :
    AllKey (V := V) := by
  intro p hp1
  have heq : iT (0:V) (free ℒₒᵣ p) = free ℒₛₑₜ (iT (1:V) p) := by
    rw [free, free]
    change iT (0:V) (subst ℒₒᵣ (?[^&0] : V) (shift ℒₒᵣ p)) =
      subst ℒₛₑₜ (?[^&0] : V) (shift ℒₛₑₜ (iT (1:V) p))
    rw [← hB (q := shift ℒₒᵣ p) hp1.shift]
    rw [← iT_shift (n := (1:V)) p hp1]
  rw [heq]
  apply Derivable.toProvable
  apply Derivable.or (s := (∅ : V)) (p := neg ℒₛₑₜ (free ℒₛₑₜ (iT (1:V) p)))
    (q := free ℒₛₑₜ (iT (1:V) p))
  apply Derivable.em (p := free ℒₛₑₜ (iT (1:V) p))
  · simp [(isSemiformula_iT (n := (1:V)) p hp1).free]
  · simp
  · simp

/-! ## ★ `ExsBridge2` 的 `p = ⊤` 情形（2026-10-14，已落地）

`ExsBridge2` 取 `p = ⊤` 时：
* `substs1 t ⊤ = ⊤`、`iT 0 ⊤ = ⊤` ⟹ 左端 `⊤`
* `iT 1 ⊤ = ⊤` ⟹ 右端 `^∃ (domZero ⋏ ⊤)` =「ω 非空」

故退化为 `Provable (imp ⊤ ω_nonempty)`，而 `imp ⊤ E` 由 `E` 经一次 ∨ 弱化即得
——**用已入包的 `imp_wk`**（`insert X S` 可导 ⟹ `insert (D 🡒 X) S` 可导）。

**⟹ `ExsBridge2` 的 `p = ⊤` 情形归约到 `Provable (^∃ (domZero ⋏ ⊤))`**，
而后者正是 peer（004-Step）已证的 `omega_nonempty_provable`
（`probes/W8-ExsBridge2-top-PROOF-20261013.lean`，exit 0）。

**这条是 `ExsBridge2` 的第一个已证特例**——
一般 `p` 仍未证（其 `p` 来自任意公式集，非标准模型里含非标准元，
语义路线不适用，见 `CLAIM-Z0-W8-HALL-BLOCKER.md` §4）。 -/

/-- **`ExsBridge2` 的 `p = ⊤` 情形由「ω 非空可证」推出**（用 `imp_wk`，exit 0）。 -/
theorem exsBridge2_top_of_omega
    (hω : Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      ((^∃ ((domZero (V := V)) ^⋏ (^⊤ : V)) : V))) :
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (imp ℒₛₑₜ (^⊤ : V) ((^∃ ((domZero (V := V)) ^⋏ (^⊤ : V)) : V))) := by
  apply Derivable.toProvable
  exact imp_wk (D := (^⊤ : V))
    (X := ((^∃ ((domZero (V := V)) ^⋏ (^⊤ : V)) : V)))
    (S := (∅ : V))
    IsSemiformula.verum
    ((IsSemiformula.exs (L := ℒₛₑₜ) (n := (0:V))
      (p := ((domZero (V := V)) ^⋏ (^⊤ : V)))).mpr
      (IsSemiformula.and.mpr
        ⟨isSemiformula_domZero (V := V) (n := (0:V)), IsSemiformula.verum⟩))
    (by simp)
    hω.toDerivable

end GodelQ.ShCraigElimSetupQ
