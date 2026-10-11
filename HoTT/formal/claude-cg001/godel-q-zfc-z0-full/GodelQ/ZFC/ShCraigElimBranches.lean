import GodelQ.ZFC.ShCraigElimPredicate
import GodelQ.ZFC.SeqTranslateFormula
import GodelQ.ZFC.ShCraigElimNegLaw
import GodelQ.ZFC.TranslateSeqShift

/-!
# CG-007 · W8 第二层（五）：`induction1` 的规则支

`ShCraigElimSetup.induction_setup` 把 `Derivation.induction1` 的 10 个支固定成骨架。
本文件开始**填**这些支，每填一条就是一个无未证标记的定理。

（注意：收据驱动 `zfc_lean_check.py` 对源文件做**纯文本**扫描，注释里出现未证标记
的英文词也会被判为 `FORBIDDEN_SOURCE_MARKER`。本文件因此不在注释里写那个词。）

## 已填

* `isFormulaSet_translateSeq`：`translateSeq` 保持 `IsFormulaSet`
  （用 `isSemiformula_iT`，即 `SeqTranslateFormula.lean` 的主定理）。
* `hWk`：弱化支。用 `Derivable.wk` + `translateSeq_mono` + 上一条。
* `hVerumIntro`：`⊤ ∈ s` ⟹ `Derivable 𝗭𝗙𝗖 (translateSeq s)`。
  用 `Derivable.verum` + `iT_verum`。
* `hAxL`：`p ∈ s` 且 `neg p ∈ s` ⟹ `Derivable 𝗭𝗙𝗖 (translateSeq s)`。
  用 `Derivable.em`（`axL` 规则的 Derivable 版）+ **一般相容律**
  `ShCraigElimNegLaw.iT_neg`（CG001-C-398，2026-10-11 证出）把 `iT 0 (neg p)`
  换成 `neg (iT 0 p)`。

## 未填，以及为什么

其余 3 个支（`hAll`/`hExs`/`hShift`）与 `axm` 支。**2026-10-11 更新**：
`hAxL`/`hCut`/`hAnd`/`hOr` 已填（见上「已填」），下表随之更新。

| 支 | 需要什么 | 现状（2026-10-11 实测） |
|---|---|---|
| `hAll` | `iT` 与 `setShift` 的相容 | **不存在**。`shift` 的构造原子支用 `^rel k R (termShiftVec L k v)`（改**项向量**），`iT` 的原子支用 `iTR n k R v`，而 `iTR` 依赖 `iVE n v.[0]`/`v.[1]`——**两者不同构**。要证 `iT n (shift p) = shift (iT n p)` 需展开 `iTR` 定义 + 项层归纳，Foundation 无现成引理，比 `iT_neg` 实质性地难 |
| `hShift` | 同 `hAll` | 同上 |
| `hExs` | `iT` 与 `substs1` 的相容 | **不存在**，同上量级 |
| `axm` | 把 `p ∈ Sh.craig.Δ₁Class` 接到 `iT 0 p` 的 `𝗭𝗙𝗖`-可证性 | **路线已找到（2026-10-11 探针实测）**：`σ ∈ Sh.craig ⟹ 𝗭𝗙𝗖 ⊢ translate σ` 已证（三步：`Sh.craig ⪯ Sh`——Foundation `CraigTrick.lean:321` 已有实例 → `Sh_provable_iff` → `Entailment.by_axm`）。再接 Foundation 的 `Δ₁Class.mem_iff_s`（`(⌜φ⌝ : V) ∈ T.Δ₁Class ↔ ∃ σ ∈ T, φ = σ`）与 `iT_quote` 即可。**不需要** V 层 `codeOfREPred`（早先判定有误）。剩余：类型与命名空间对齐 |

**注意**：`iT_quote` 只对**引号化的**公式（`⌜φ⌝`，`φ` 是元层标准公式）给交换律；
`induction1` 的支拿到的是 **V 内的任意公式码**（可能非标准），
所以不能直接用 `iT_quote`。这是"V 内部"与"元层"的又一处分野。
**一般版本已由 `ShCraigElimNegLaw.iT_neg` 给出**（2026-10-11，C-398）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ShCraigElimBranches

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`translateSeq` 保持 `IsFormulaSet`**。

`IsFormulaSet ℒₒᵣ s` 展开为 `∀ p ∈ s, IsSemiformula ℒₒᵣ 0 p`；
`translateSeq s` 的元素是 `iT 0 x`（`x ∈ s`），
而 `isSemiformula_iT` 给出 `IsSemiformula ℒₛₑₜ 0 (iT 0 x)`。 -/
lemma isFormulaSet_translateSeq {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    IsFormulaSet (L := ℒₛₑₜ) (translateSeq (V := V) s) := by
  intro p hp
  rcases mem_translateSeq_iff.mp hp with ⟨x, hx, rfl⟩
  exact isSemiformula_iT x (hs x hx)

/-- **`hWk` 支**：弱化。

规则是 `s' ⊆ s ⊢ s'` ⟹ `⊢ s`。翻译后要证
`Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d)) → Derivable 𝗭𝗙𝗖 (translateSeq s)`，
用 `Derivable.wk`（弱化）配 `translateSeq_mono`。

`Derivable.wk` 的三条义务：目标 sequent 是公式集、包含关系、源推导。 -/
lemma hWk {s d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : fstIdx d ⊆ s) (ih : Q (V := V) d) : Q (V := V) (wkRule s d) := by
  simp only [Q, fstIdx_wkRule]
  exact Derivable.wk (isFormulaSet_translateSeq hs) (translateSeq_mono h) ih


/-- **`hVerumIntro` 支**：`⊤ ∈ s`。

`iT 0 ⊤ = ⊤`（`iT_verum`），所以 `translateSeq s` 里含 `⊤`，
由 `Derivable.verum` 得结论。 -/
lemma hVerumIntro {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (hv : (^⊤ : V) ∈ s) :
    Q (V := V) (verumIntro s) := by
  simp only [Q, fstIdx_verumIntro]
  apply Derivable.verum
  · exact isFormulaSet_translateSeq hs
  · exact mem_translateSeq_iff.mpr ⟨^⊤, hv, (iT_verum 0).symm⟩

/-- **`hAxL` 支**：`p ∈ s` 且 `neg p ∈ s` ⟹ `Q (axL s p)`。

`Q (axL s p)` 经 `fstIdx_axL` 化为 `Derivable 𝗭𝗙𝗖 (translateSeq s)`。
`translateSeq s` 含 `iT 0 p`（由 `hp`）与 `iT 0 (neg p) = neg (iT 0 p)`
（由 `hn` 与一般相容律 `iT_neg`），正是 `Derivable.em` 需要的两条。 -/
lemma hAxL {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : p ∈ s) (hn : neg ℒₒᵣ p ∈ s) : Q (V := V) (axL s p) := by
  simp only [Q, fstIdx_axL]
  apply Derivable.em (isFormulaSet_translateSeq hs)
  · exact mem_translateSeq_iff.mpr ⟨p, hp, rfl⟩
  · refine mem_translateSeq_iff.mpr ⟨neg ℒₒᵣ p, hn, ?_⟩
    exact (GodelQ.ShCraigElimNegLaw.iT_neg (n := 0) p (hs p hp)).symm

/-- **`hAnd` 支**：`p ⋏ q ∈ s`，两条子推导分别给出 `insert p s` 与 `insert q s`。

`translateSeq_insert` 把 `insert` 推进翻译，于是子推导的结论正好是
`Derivable 𝗭𝗙𝗖 (insert (iT 0 p) (translateSeq s))` 的形状；
结论 sequent 侧的 `p ⋏ q ∈ s` 经 `iT_and` 送到 `iT 0 p ^⋏ iT 0 q ∈ translateSeq s`。 -/
lemma hAnd {s p q dp dq : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (h : p ^⋏ q ∈ s)
    (ihp : Q (V := V) dp) (ihq : Q (V := V) dq)
    (hdp : fstIdx dp = insert p s) (hdq : fstIdx dq = insert q s) :
    Q (V := V) (andIntro s p q dp dq) := by
  have hu : IsUFormula ℒₒᵣ (p ^⋏ q) := (hs (p ^⋏ q) h).isUFormula
  have hp : IsUFormula ℒₒᵣ p := ((IsUFormula.and).mp hu).1
  have hq : IsUFormula ℒₒᵣ q := ((IsUFormula.and).mp hu).2
  simp only [Q, fstIdx_andIntro]
  simp only [Q] at ihp ihq
  rw [hdp] at ihp
  rw [hdq] at ihq
  simp only [translateSeq_insert] at ihp ihq
  exact Derivable.and_m (mem_translateSeq_iff.mpr ⟨p ^⋏ q, h, (iT_and hp hq).symm⟩) ihp ihq

/-- **`hOr` 支**：`p ⋎ q ∈ s`，子推导给出 `insert p (insert q s)`。 -/
lemma hOr {s p q dpq : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (h : p ^⋎ q ∈ s)
    (ih : Q (V := V) dpq) (hd : fstIdx dpq = insert p (insert q s)) :
    Q (V := V) (orIntro s p q dpq) := by
  have hu : IsUFormula ℒₒᵣ (p ^⋎ q) := (hs (p ^⋎ q) h).isUFormula
  have hp : IsUFormula ℒₒᵣ p := ((IsUFormula.or).mp hu).1
  have hq : IsUFormula ℒₒᵣ q := ((IsUFormula.or).mp hu).2
  simp only [Q, fstIdx_orIntro]
  simp only [Q] at ih
  rw [hd] at ih
  simp only [translateSeq_insert] at ih
  exact Derivable.or_m (mem_translateSeq_iff.mpr ⟨p ^⋎ q, h, (iT_or hp hq).symm⟩) ih

/-- **`hCut` 支**：`cutRule s p d₁ d₂`，两条子推导分别给出 `insert p s` 与 `insert (neg p) s`。

第二条子推导翻译后含 `iT 0 (neg p)`，用一般相容律 `iT_neg` 换成 `neg (iT 0 p)`，
正是 `Derivable.cut` 需要的形状。`p` 的公式性由调用方给出（来自子推导的 sequent 是公式集）。 -/
lemma hCut {s p d₁ d₂ : V} (_hs : IsFormulaSet (L := ℒₒᵣ) s) (hp : IsSemiformula ℒₒᵣ 0 p)
    (ih₁ : Q (V := V) d₁) (ih₂ : Q (V := V) d₂)
    (h₁ : fstIdx d₁ = insert p s) (h₂ : fstIdx d₂ = insert (neg ℒₒᵣ p) s) :
    Q (V := V) (cutRule s p d₁ d₂) := by
  simp only [Q, fstIdx_cutRule]
  simp only [Q] at ih₁ ih₂
  rw [h₁] at ih₁
  rw [h₂] at ih₂
  simp only [translateSeq_insert] at ih₁ ih₂
  rw [GodelQ.ShCraigElimNegLaw.iT_neg (n := 0) p hp] at ih₂
  exact Derivable.cut (iT (0 : V) p) ih₁ ih₂

/-- **`hShift` 支**：`shiftRule`。

规则是：从 `d` 的结论 sequent `s'` 出发，结论 sequent 是 `setShift s'`。
翻译后要证 `Derivable 𝗭𝗙𝗖 (translateSeq (setShift (fstIdx d)))`；
用 `Derivable.shift`（它给 `setShift` 下的可证性）配 `translateSeq_setShift`
（把 `translateSeq` 推进 `setShift`）。

`translateSeq_setShift` 要求 `s'` 是公式集——由子推导给出
（`Derivable.isFormulaSet` 取子推导的 `h.1`）。 -/
lemma hShift {s d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : s = setShift ℒₒᵣ (fstIdx d)) (ih : Q (V := V) d) :
    Q (V := V) (shiftRule s d) := by
  have hs' : IsFormulaSet (L := ℒₒᵣ) (fstIdx d) := by
    rw [h, IsFormulaSet.setShift_iff] at hs
    exact hs
  simp only [Q, fstIdx_shiftRule, h]
  rw [GodelQ.TranslateSeqShift.translateSeq_setShift hs']
  exact Derivable.shift ih

end GodelQ.ShCraigElimBranches

#print axioms GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq
#print axioms GodelQ.ShCraigElimBranches.hWk
#print axioms GodelQ.ShCraigElimBranches.hVerumIntro
#print axioms GodelQ.ShCraigElimBranches.hAxL
#print axioms GodelQ.ShCraigElimBranches.hAnd
#print axioms GodelQ.ShCraigElimBranches.hOr
#print axioms GodelQ.ShCraigElimBranches.hCut
#print axioms GodelQ.ShCraigElimBranches.hShift
