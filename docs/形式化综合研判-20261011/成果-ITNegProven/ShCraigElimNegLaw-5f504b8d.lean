import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（九）：一般（V 内任意公式码）的 `iT` 与 `neg` 相容律

`hAxL` / `hCut` / `hShift` 三支需要

```
iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)          -- p 是 V 内任意公式码，可能非标准
```

`iT_quote_neg` 只对引号化（元层标准）公式给交换律，不能直接用在 `induction1` 的支里，
所以这里走 `semiformula_result_induction`（与 `isSemiformula_iT` 同形）在 V 内部证一般版本。

归纳谓词取 `P param n p q := param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q`，
结论用 `iT.construction.result ℒₒᵣ param p`（即 `iT param p` 的定义体），
使 8 个支的结论形状与原理给出的一致。**`param = n` 护罩是必需的**：`iT` 在
`all`/`exs` 支改层（`allChanges/exsChanges param 0 = param + 1`），而原理把输出层
`param` 与输入层 `n` 独立量化。

## 各支要点（照 `SeqTranslateFormula.lean` 的 `isSemiformula_iT` 骨架）

- 原理的支顺序是 `hP, hRel, hNRel, hverum, hfalsum, hand, hor, hall, hexs`
  （**九**个参数；`hP` 是 definability，放在最后一段给）。支内先 `rw [← h] at hp`
  把层数对齐到 `param`，因为后续 `neg_*`/`iT_*` 引理都在 `param` 层工作。
- `rel`/`nrel`：`neg_rel`/`neg_nrel` 要 `IsUTermVec`（不是 `IsSemitermVec`），
  由 `hv.isUTermVec` 转；`iT.construction` 的字段用 `simp only [iT.construction]` 展开。
- `verum`/`falsum`：`neg_verum`/`neg_falsum` **无参数**（`[simp]` 引理）。
- `and`/`or`：`neg_and`/`neg_or` 把外层 `neg` 推进去后，两侧用 `congrArg₂` 接归纳假设；
  右侧的 `neg (iT p ^⋏ iT q)` 用 `conv_rhs` + `neg_and` 反向归形。
- `all`/`exs`：先 `result_all`/`result_exs` 展开 `iT.construction.result`，再
  `nth_adjoin_zero` 把 `ys.[0]` 落回子结果，然后 `conv_rhs` 里用 `neg_all`/`neg_ex`
  （`ℒₛₑₜ` 侧，参数由 `(IsUFormula.imp …).2` / `(IsUFormula.and …).2` 合成，
  因为 `IsUFormula.imp`/`.and` 是 ↔ 形式）把右侧归到与左侧同一形状，
  最后正向 `ih 0 …` 收尾。

`iTR`/`domZero`/`iT (…)` 都是 `IsUFormula`，故码层对合律用 `IsUFormula.neg_neg` 即可。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegLaw

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般版本的 `iT`/`neg` 相容律**：`iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p)`，
对 V 内任意公式码 `p`（层数 `n`）成立。 -/
theorem iT_neg {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_
  · intro p hp
    simpa [iT] using key hp (rfl : n = n)
  · definability
  · intro n param k R v hR hv h
    rw [← h] at hv
    have hu : IsUTermVec ℒₒᵣ k v := hv.isUTermVec
    simp only [iT.construction]
    rw [neg_rel (L := ℒₒᵣ) hR hu, iT_nrel hR hu]
  · intro n param k R v hR hv h
    rw [← h] at hv
    have hu : IsUTermVec ℒₒᵣ k v := hv.isUTermVec
    simp only [iT.construction]
    rw [neg_nrel (L := ℒₒᵣ) hR hu, iT_rel hR hu,
      IsUFormula.neg_neg (isSemiformula_iTR hR hv).isUFormula]
  · intro n param h
    simp only [iT.construction]
    rw [neg_verum (L := ℒₒᵣ), iT_falsum, neg_verum (L := ℒₛₑₜ)]
  · intro n param h
    simp only [iT.construction]
    rw [neg_falsum (L := ℒₒᵣ), iT_verum, neg_falsum (L := ℒₛₑₜ)]
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    show iT param (neg ℒₒᵣ (p ^⋏ q)) =
      neg ℒₛₑₜ (iT param p ^⋏ iT param q)
    rw [neg_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    show iT param (neg ℒₒᵣ p ^⋎ neg ℒₒᵣ q) =
      neg ℒₛₑₜ (iT param p ^⋏ iT param q)
    rw [iT_or (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula)]
    show iT param (neg ℒₒᵣ p) ^⋎ iT param (neg ℒₒᵣ q) =
      neg ℒₛₑₜ (iT param p ^⋏ iT param q)
    conv_rhs => rw [neg_and (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋎ ·) (ihp h) (ihq h)
  · intro n param p q hp hq ihp ihq h
    rw [← h] at hp hq
    show iT param (neg ℒₒᵣ (p ^⋎ q)) =
      neg ℒₛₑₜ (iT param p ^⋎ iT param q)
    rw [neg_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    show iT param (neg ℒₒᵣ p ^⋏ neg ℒₒᵣ q) =
      neg ℒₛₑₜ (iT param p ^⋎ iT param q)
    rw [iT_and (IsUFormula.neg hp.isUFormula) (IsUFormula.neg hq.isUFormula)]
    show iT param (neg ℒₒᵣ p) ^⋏ iT param (neg ℒₒᵣ q) =
      neg ℒₛₑₜ (iT param p ^⋎ iT param q)
    conv_rhs => rw [neg_or (L := ℒₛₑₜ) (isSemiformula_iT p hp).isUFormula
      (isSemiformula_iT q hq).isUFormula]
    exact congrArg₂ (· ^⋏ ·) (ihp h) (ihq h)
  · intro n param p hp ih h
    rw [← h] at hp
    show iT param (neg ℒₒᵣ (^∀ p)) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [neg_all (L := ℒₒᵣ) hp.isUFormula]
    show iT param (^∃ (neg ℒₒᵣ p)) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [iT_exs (IsUFormula.neg hp.isUFormula)]
    show (^∃ (domZero ^⋏ iT (param + 1) (neg ℒₒᵣ p)) : V) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∀ p))
    rw [UformulaRec1.Construction.result_all (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.allSize param p = 1)]
    change (^∃ (domZero ^⋏ iT (param + 1) (neg ℒₒᵣ p)) : V) =
      neg ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.allChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∃ (domZero ^⋏ iT (iT.construction.allChanges param 0) (neg ℒₒᵣ p)) : V) =
      neg ℒₛₑₜ (^∀ (imp ℒₛₑₜ domZero (iT (iT.construction.allChanges param 0) p)))
    conv_rhs =>
      rw [neg_all (L := ℒₛₑₜ)
        ((IsUFormula.imp (L := ℒₛₑₜ)).2
          ⟨(isSemiformula_domZero (n := param)).isUFormula,
           (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩)]
      rw [imp, neg_or (L := ℒₛₑₜ) (IsUFormula.neg (isSemiformula_domZero (n := param)).isUFormula)
        ((isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula)]
      rw [IsUFormula.neg_neg (isSemiformula_domZero (n := param)).isUFormula]
    rw [ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    rfl
  · intro n param p hp ih h
    rw [← h] at hp
    show iT param (neg ℒₒᵣ (^∃ p)) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [neg_ex (L := ℒₒᵣ) hp.isUFormula]
    show iT param (^∀ (neg ℒₒᵣ p)) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [iT_all (IsUFormula.neg hp.isUFormula)]
    show (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p))) : V) =
      neg ℒₛₑₜ (UformulaRec1.Construction.result ℒₒᵣ iT.construction param (^∃ p))
    rw [UformulaRec1.Construction.result_exs (c := iT.construction) (L := ℒₒᵣ)
      hp.isUFormula (rfl : iT.construction.exsSize param p = 1)]
    change (^∀ (imp ℒₛₑₜ domZero (iT (param + 1) (neg ℒₒᵣ p))) : V) =
      neg ℒₛₑₜ (^∃ (domZero ^⋏
        ((UformulaRec1.Construction.result ℒₒᵣ iT.construction
          (iT.construction.exsChanges param 0) p ∷ (0 : V)) : V).[0]))
    rw [nth_adjoin_zero]
    change (^∀ (imp ℒₛₑₜ domZero (iT (iT.construction.exsChanges param 0) (neg ℒₒᵣ p))) : V) =
      neg ℒₛₑₜ (^∃ (domZero ^⋏ iT (iT.construction.exsChanges param 0) p))
    conv_rhs =>
      rw [neg_ex (L := ℒₛₑₜ) ((IsUFormula.and (L := ℒₛₑₜ)).2
        ⟨(isSemiformula_domZero (n := param)).isUFormula,
         (isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula⟩)]
      rw [neg_and (L := ℒₛₑₜ) (isSemiformula_domZero (n := param)).isUFormula
        ((isSemiformula_iT p (by simpa [iT.construction] using hp)).isUFormula)]
    rw [ih 0 (by simp [iT.construction]) (by simp [iT.construction, h])]
    rfl

end GodelQ.ShCraigElimNegLaw

#print axioms GodelQ.ShCraigElimNegLaw.iT_neg
