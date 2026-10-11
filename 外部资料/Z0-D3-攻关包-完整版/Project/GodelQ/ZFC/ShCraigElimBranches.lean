import GodelQ.ZFC.ShCraigElimPredicate
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

end GodelQ.ShCraigElimBranches

#print axioms GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq
#print axioms GodelQ.ShCraigElimBranches.hWk
#print axioms GodelQ.ShCraigElimBranches.hVerumIntro
