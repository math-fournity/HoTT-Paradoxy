import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.ShCraigElimNegLaw

/-!
# CG-007 · W8 第二层（十一）：`induction1` 的规则支——四个新支

`ShCraigElimSetup.induction_setup` 把 `Derivation.induction1` 的 10 个支固定成骨架。
本文件再填四个（`ShCraigElimBranches.lean` 已有 `hWk`、`hVerumIntro`）：

| 支 | 用到的引理 |
|---|---|
| `hAnd` | `iT_and` + `Derivable.and_m` + `translateSeq_insert` |
| `hOr` | `iT_or` + `Derivable.or_m` |
| `hAxL` | **`iT_neg`（C-399，一般相容律）** + `Derivable.em` |
| `hCut` | **`iT_neg`（C-399）** + `Derivable.cut` |

`hAxL`/`hCut` 正是 `ShCraigElimBranches.lean` 记为"未填"的两支：它们需要一般（V 内任意
公式码）的 `iT`/`neg` 相容律，而不是引号化的 `iT_quote_neg`。这条律在 C-399 中证出。

## 还没填的三支，以及为什么

| 支 | 需要的东西 |
|---|---|
| `hAll` | `iT` 与 `free`/`setShift` 的相容律 |
| `hExs` | `iT` 与 `substs1` 的相容律 |
| `hShift` | 同 `hAll` |

这三条相容律是翻译与去 Bruijn 操作之间的交换：翻译在每个量词下多引一个约束变量
（`domZero` 的 `#0`），所以层数会错开一位，不是平凡的交换。它们未证。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches
open GodelQ.ShCraigElimNegLaw

namespace GodelQ.ShCraigElimFilled

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hAnd` 支**：两条子推导给出 `iT 0 p` 与 `iT 0 q` 可导，
结论 sequent 里有 `p ⋏ q`，翻译后是 `iT 0 p ⋏ iT 0 q`（`iT_and`），用 `Derivable.and_m`。 -/
lemma hAnd {s p q dp dq : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋏ q ∈ s)
    (hdp : DerivationOf Sh.craig dp (p ⫽ s)) (hdq : DerivationOf Sh.craig dq (q ⫽ s))
    (ihp : Q (V := V) dp) (ihq : Q (V := V) dq) :
    Q (V := V) (andIntro s p q dp dq) := by
  simp only [Q, fstIdx_andIntro]
  have hp : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) p ⫽ translateSeq s) := by
    simpa only [Q, hdp.1, translateSeq_insert] using ihp
  have hq : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) q ⫽ translateSeq s) := by
    simpa only [Q, hdq.1, translateSeq_insert] using ihq
  have hconj : IsSemiformula ℒₒᵣ 0 (p ^⋏ q) := hs (p ^⋏ q) hpq
  have hconj' := IsSemiformula.and.mp hconj
  have hsp : IsUFormula ℒₒᵣ p := hconj'.1.isUFormula
  have hsq : IsUFormula ℒₒᵣ q := hconj'.2.isUFormula
  refine Derivable.and_m (p := iT (0 : V) p) (q := iT (0 : V) q) ?_ ?_ ?_
  · rw [← iT_and (V := V) hsp hsq]
    exact mem_translateSeq_iff.mpr ⟨p ^⋏ q, hpq, rfl⟩
  · exact hp
  · exact hq

/-- **`hOr` 支**：一条子推导（`p ⫽ q ⫽ s`），结论 sequent 里有 `p ⋎ q`。 -/
lemma hOr {s p q d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋎ q ∈ s)
    (hd : DerivationOf Sh.craig d (p ⫽ q ⫽ s)) (ih : Q (V := V) d) :
    Q (V := V) (orIntro s p q d) := by
  simp only [Q, fstIdx_orIntro]
  have hd' : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (iT (0 : V) p ⫽ iT (0 : V) q ⫽ translateSeq s) := by
    simpa only [Q, hd.1, translateSeq_insert] using ih
  have hconj : IsSemiformula ℒₒᵣ 0 (p ^⋎ q) := hs (p ^⋎ q) hpq
  have hconj' := IsSemiformula.or.mp hconj
  have hsp : IsUFormula ℒₒᵣ p := hconj'.1.isUFormula
  have hsq : IsUFormula ℒₒᵣ q := hconj'.2.isUFormula
  refine Derivable.or_m (p := iT (0 : V) p) (q := iT (0 : V) q) ?_ ?_
  · rw [← iT_or (V := V) hsp hsq]
    exact mem_translateSeq_iff.mpr ⟨p ^⋎ q, hpq, rfl⟩
  · exact hd'

/-- **`hAxL` 支**：`p ∈ s` 且 `∼p ∈ s`。翻译后是 `iT 0 p` 与 `iT 0 (neg p)`；
后者由 C-399 变成 `neg (iT 0 p)`，于是 `Derivable.em` 直接给结论。 -/
lemma hAxL {s p : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hp : p ∈ s) (hn : neg ℒₒᵣ p ∈ s) :
    Q (V := V) (axL s p) := by
  simp only [Q, fstIdx_axL]
  have hsp : IsSemiformula ℒₒᵣ 0 p := hs p hp
  refine Derivable.em (isFormulaSet_translateSeq hs) (iT (0 : V) p) ?_ ?_
  · exact mem_translateSeq_iff.mpr ⟨p, hp, rfl⟩
  · rw [← iT_neg (V := V) hsp]
    exact mem_translateSeq_iff.mpr ⟨neg ℒₒᵣ p, hn, rfl⟩

/-- **`hCut` 支**：两条子推导（`p` 与 `∼p`），枢轴取 `iT 0 p`（C-399 把第二支的
`iT 0 (neg p)` 搬成 `neg (iT 0 p)`）。 -/
lemma hCut {s p d₁ d₂ : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) (hp : p ∈ s)
    (hd₁ : DerivationOf Sh.craig d₁ (p ⫽ s)) (hd₂ : DerivationOf Sh.craig d₂ (neg ℒₒᵣ p ⫽ s))
    (ih₁ : Q (V := V) d₁) (ih₂ : Q (V := V) d₂) :
    Q (V := V) (cutRule s p d₁ d₂) := by
  simp only [Q, fstIdx_cutRule]
  have h1 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) p ⫽ translateSeq s) := by
    simpa only [Q, hd₁.1, translateSeq_insert] using ih₁
  have h2 : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0 : V) (neg ℒₒᵣ p) ⫽ translateSeq s) := by
    simpa only [Q, hd₂.1, translateSeq_insert] using ih₂
  have hsp : IsSemiformula ℒₒᵣ 0 p := hs p hp
  refine Derivable.cut (iT (0 : V) p) ?_ ?_
  · exact h1
  · rw [← iT_neg (V := V) hsp]
    exact h2

end GodelQ.ShCraigElimFilled

#print axioms GodelQ.ShCraigElimFilled.hAnd
#print axioms GodelQ.ShCraigElimFilled.hOr
#print axioms GodelQ.ShCraigElimFilled.hAxL
#print axioms GodelQ.ShCraigElimFilled.hCut
