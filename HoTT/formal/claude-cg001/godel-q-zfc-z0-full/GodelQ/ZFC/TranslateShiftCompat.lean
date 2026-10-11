import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（十一）：`iVE`/`shift` 跨语言的原子相容律

`hAll` / `hExs` / `hShift` 三支要 `iT` 与 `shift`/`setShift`/`substs1` 的相容律。
这不是平凡交换：`iVE`（`ℒₒᵣ` 项 → `ℒₛₑₜ` 公式）与 `termShift`（`ℒₒᵣ` 项移位）
对变量的处理不同——

| 运算 | 对 `^#z`（bvar） | 对 `^&x`（fvar） |
|---|---|---|
| `iVE` | `eqAtom (^#(z + 1))` —— 码加一（`eqAtom` 引入一个绑定层） | `eqAtom (^&x)` —— 不动 |
| `termShift` | `^#z` —— 不动 | `^&(x + 1)` —— 码加一 |

本文件给出**原子层**的两条相容律，即 `eqAtom` 与 `shift ℒₛₑₜ` 的交换：

* `shift_eqAtom_bvar`：`shift (eqAtom ^#z) = eqAtom ^#z`
* `shift_eqAtom_fvar`：`shift (eqAtom ^&x) = eqAtom ^&(x + 1)`

二者合起来说明：**`iVE` 送 bvar/fvar 到 `eqAtom`，而 `shift` 在两侧对
fvar 加一、对 bvar 不动——顺序恰好对上。** 这是拼出 `iT_shift` 的第一步。

## 证明要点

`eqAtom t = ^rel 2 cEqN (^#0 ∷ t ∷ 0)`，故 `shift` 走 `shift_rel`
（要 `(ℒₛₑₜ).IsRel 2 cEqN`，由 `codeIn_rel_quote` 给）配 `termShiftVec_cons₂`，
再把 `termShift_bvar` / `termShift_fvar` 代掉即可。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.TranslateShiftCompat

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `eqAtom t` 的向量（`^#0 ∷ t ∷ 0`）是 `ℒₛₑₜ` 的项向量，层数 2。 -/
lemma isUTermVec_eqAtom_vec (t : V) (ht : IsUTerm ℒₛₑₜ t) :
    IsUTermVec ℒₛₑₜ (2 : V) ((^#0 : V) ∷ (t ∷ (0 : V))) := by
  have hz : IsUTermVec ℒₛₑₜ (0 : V) (0 : V) := IsUTermVec.empty
  have hvec : IsUTermVec ℒₛₑₜ (1 : V) (t ∷ (0 : V)) := by
    simpa using (IsUTermVec.adjoin (L := ℒₛₑₜ) (n := (0 : V)) hz ht)
  have := IsUTermVec.adjoin (L := ℒₛₑₜ) (n := (1 : V)) hvec (IsUTerm.bvar (z := 0))
  rw [show (1 : V) + 1 = (2 : V) by norm_num] at this
  exact this

/-- **bvar 版**：`shift ℒₛₑₜ (eqAtom ^#z) = eqAtom ^#z`。

`termShift` 对 bvar 不动，而 `iVE` 的 bvar 支只把码加一（在 `eqAtom` 内部完成），
故 `shift` 作用后不变。 -/
lemma shift_eqAtom_bvar (z : V) :
    shift ℒₛₑₜ (eqAtom (^#z : V)) = eqAtom (^#z : V) := by
  show shift ℒₛₑₜ (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V))
  rw [shift_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^#z) (IsUTerm.bvar (z := z)))]
  congr 1
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := z))]
  rw [termShift_bvar, termShift_bvar]

/-- **fvar 版**：`shift ℒₛₑₜ (eqAtom ^&x) = eqAtom ^&(x + 1)`。

`termShift` 对 fvar 把码加一，与 `iVE` 的 fvar 支（不动）合起来，
正好给出「自由变量码加一」。 -/
lemma shift_eqAtom_fvar (x : V) :
    shift ℒₛₑₜ (eqAtom (^&x : V)) = eqAtom (^&(x + 1) : V) := by
  show shift ℒₛₑₜ (^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (^&(x + 1) : V) ∷ (0 : V))
  rw [shift_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^&x) (IsUTerm.fvar x))]
  congr 1
  rw [termShiftVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.fvar x)]
  rw [termShift_bvar, termShift_fvar]

/-! ## 与 `hAll`/`hExs`/`hShift` 的接口（2026-10-11 分析，尚未完成）

三支最终要的是 `translateSeq` 与 `setShift` 的交换：

```
hShift : s = setShift (fstIdx d)  ⟹  Derivable 𝗭𝗙𝗖 (translateSeq s)
ih     : Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))
```

由 `mem_translateSeq_iff`（`y ∈ translateSeq s ↔ ∃ x ∈ s, y = iT 0 x`）
逐元素看，这归结为

```
iT 0 (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT 0 p)          -- 记作 iT_shift
```

而 `iT_shift` 的原子支（`iT_rel` + `shift_rel`）归结为

```
iTR 0 k R (termShiftVec ℒₒᵣ k v) = shift ℒₛₑₜ (iTR 0 k R v)
```

`iTR` 只用 `v.[0]`、`v.[1]` 且经 `iVE`，所以再归结为**项层**的

```
iVE n (termShift t) = shift ℒₛₑₜ (iVE n t)        -- 记作 iVE_shift
```

本文件的 `shift_eqAtom_bvar`/`shift_eqAtom_fvar` 正是 `iVE_shift` 的
bvar/fvar 两支（`termShift_bvar`/`termShift_fvar` 分别对上
`iVE_bvar` 的加一与 `iVE_fvar` 的不动）。剩下的 `func` 支要用
`IsSemiterm.sigma1_induction`（`isSemiformula_iVE` 的先例），
并处理 `iVE.construction.resultVec` 与 `termShiftVec` 的相容。

**下一步顺序**：`iVE_shift`（用 sigma1_induction，func 支参照
`isSemiformula_iVE` 的 `nth_resultVec` 写法）→ `iT_shift` → `translateSeq_setShift`
→ `hShift` / `hAll` / `hExs`。`hExs` 另需 `iT_substs1`（同形）。
-/

end GodelQ.TranslateShiftCompat

#print axioms GodelQ.TranslateShiftCompat.isUTermVec_eqAtom_vec
#print axioms GodelQ.TranslateShiftCompat.shift_eqAtom_bvar
#print axioms GodelQ.TranslateShiftCompat.shift_eqAtom_fvar
