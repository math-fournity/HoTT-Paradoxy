import GodelQ.ZFC.ShCraigElimPredicate
import GodelQ.ZFC.ShCraigElimNegLaw
import GodelQ.ZFC.SeqTranslateFormula

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

## 未填，以及为什么

其余 9 个支。它们分成两类：

**（甲）需要 `iT` 与某个运算的相容律**（本机实测：这些相容律**尚不存在**）：

| 支 | 需要的相容律 | 现状 |
|---|---|---|
| `hAxL` | `iT 0 (neg p) = neg ℒₛₑₜ (iT 0 p)`（**一般公式**，非引号化） | 不存在。`InternalTranslate.lean` 只有 `iT_nrel`（原子级 `^nrel k R v`），一般公式的否定要递归展开 blueprint |
| `hCut` | 同上（`ih₂` 里出现 `iT 0 (neg p)`） | 同 `hAxL` |
| `hAll` | `iT` 与 `setShift` 的相容 | 不存在 |
| `hExs` | `iT` 与 `substs1` 的相容 | 不存在 |
| `hShift` | 同 `hAll` | 不存在 |

**（乙）只需已有零件**（应当可以直接填）：

| 支 | 思路 |
|---|---|
| `hAnd` | 两条子推导 + `iT_and` |
| `hOr` | 两条子推导 + `iT_or` |

**注意**：`iT_quote` 只对**引号化的**公式（`⌜φ⌝`，`φ` 是元层标准公式）给交换律；
`induction1` 的支拿到的是 **V 内的任意公式码**（可能非标准），
所以不能直接用 `iT_quote`。这是"V 内部"与"元层"的又一处分野。
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

/-- **`hAxL` 支**：`p ∈ s` 且 `neg p ∈ s`。

翻译后 `translateSeq s` 同时含 `iT 0 p` 与其否定：
`iT 0 (neg p) = neg (iT 0 p)` 由 `ShCraigElimNegLaw.iT_neg` 给出
（本机已证，exit 0）。于是 `Derivable.em` 直接给出结论。

`iT_neg` 需要 `p` 是 `ℒₒᵣ` 的公式（层数 0）；`IsFormulaSet s` 提供它。 -/
lemma hAxL {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : p ∈ s) (hn : neg ℒₒᵣ p ∈ s) :
    Q (V := V) (axL s p) := by
  simp only [Q, fstIdx_axL]
  refine Derivable.em (isFormulaSet_translateSeq hs)
    (iT 0 p) (mem_translateSeq_iff.mpr ⟨p, hp, rfl⟩) ?_
  exact mem_translateSeq_iff.mpr
    ⟨neg ℒₒᵣ p, hn, (ShCraigElimNegLaw.iT_neg p (hs p hp)).symm⟩

/-- **`hAnd` 支**：`p ^⋏ q ∈ s`，两条子推导分别在 `insert p s`、`insert q s` 上。

`iT 0 (p ⋏ q) = iT 0 p ⋏ iT 0 q`（`iT_and`），故 `translateSeq s` 里含该合取，
用 `Derivable.and_m`。子推导的归纳假设给的是 `insert` 后的可导性，
要先把 `translateSeq (insert p s)` 与 `insert (iT 0 p) (translateSeq s)` 对上
（`translateSeq_insert`）。 -/
lemma hAnd {s p q dp dq : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : (p ^⋏ q) ∈ s)
    (hdp : fstIdx dp = insert p s) (hdq : fstIdx dq = insert q s)
    (ihp : Q (V := V) dp) (ihq : Q (V := V) dq) :
    Q (V := V) (andIntro s p q dp dq) := by
  have hf : IsUFormula ℒₒᵣ (p ^⋏ q) := (hs (p ^⋏ q) hpq).isUFormula
  have hfp : IsUFormula ℒₒᵣ p := IsUFormula.and.mp hf |>.1
  have hfq : IsUFormula ℒₒᵣ q := IsUFormula.and.mp hf |>.2
  simp only [Q, fstIdx_andIntro]
  refine Derivable.and_m (mem_translateSeq_iff.mpr
    ⟨p ^⋏ q, hpq, (iT_and hfp hfq).symm⟩) ?_ ?_
  · simpa only [Q, hdp, translateSeq_insert] using ihp
  · simpa only [Q, hdq, translateSeq_insert] using ihq

/-- **`hOr` 支**：`p ^⋎ q ∈ s`，子推导在 `insert p (insert q s)` 上。

`iT_or` 给 `iT 0 (p ⋎ q) = iT 0 p ⋎ iT 0 q`；`Derivable.or_m` 收尾。 -/
lemma hOr {s p q d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : (p ^⋎ q) ∈ s) (hd : fstIdx d = insert p (insert q s))
    (ih : Q (V := V) d) :
    Q (V := V) (orIntro s p q d) := by
  have hf : IsUFormula ℒₒᵣ (p ^⋎ q) := (hs (p ^⋎ q) hpq).isUFormula
  have hfp : IsUFormula ℒₒᵣ p := IsUFormula.or.mp hf |>.1
  have hfq : IsUFormula ℒₒᵣ q := IsUFormula.or.mp hf |>.2
  simp only [Q, fstIdx_orIntro]
  refine Derivable.or_m (mem_translateSeq_iff.mpr
    ⟨p ^⋎ q, hpq, (iT_or hfp hfq).symm⟩) ?_
  simpa only [Q, hd, translateSeq_insert] using ih

/-- **`hCut` 支**：两条子推导分别在 `insert p s`、`insert (neg p) s` 上。

`Derivable.cut` 直接给 `Derivable (translateSeq s)`——但它要的是
`Derivable (insert (iT 0 p) (translateSeq s))` 与
`Derivable (insert (neg (iT 0 p)) (translateSeq s))`。
第二条的 `neg (iT 0 p)` 要换回 `iT 0 (neg p)`，仍用 `iT_neg`。 -/
lemma hCut {s p d₁ d₂ : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : IsSemiformula ℒₒᵣ 0 p)
    (hd₁ : fstIdx d₁ = insert p s) (hd₂ : fstIdx d₂ = insert (neg ℒₒᵣ p) s)
    (ih₁ : Q (V := V) d₁) (ih₂ : Q (V := V) d₂) :
    Q (V := V) (cutRule s p d₁ d₂) := by
  simp only [Q, fstIdx_cutRule]
  refine Derivable.cut (iT 0 p) ?_ ?_
  · simpa only [Q, hd₁, translateSeq_insert] using ih₁
  · rw [show neg ℒₛₑₜ (iT 0 p) = iT 0 (neg ℒₒᵣ p) from
        (ShCraigElimNegLaw.iT_neg p hp).symm]
    simpa only [Q, hd₂, translateSeq_insert] using ih₂

end GodelQ.ShCraigElimBranches

#print axioms GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq
#print axioms GodelQ.ShCraigElimBranches.hWk
#print axioms GodelQ.ShCraigElimBranches.hVerumIntro
#print axioms GodelQ.ShCraigElimBranches.hAxL
#print axioms GodelQ.ShCraigElimBranches.hAnd
#print axioms GodelQ.ShCraigElimBranches.hOr
#print axioms GodelQ.ShCraigElimBranches.hCut
