import GodelQ.ZFC.ShCraigElimPredicate
import GodelQ.ZFC.ShCraigElimNegLaw
import GodelQ.ZFC.SeqTranslateFormula
import GodelQ.ZFC.TranslateShiftCompat

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

## 2026-10-11 进展：2 支 → 6 支

`hAxL`、`hAnd`、`hOr`、`hCut` 已填（各自 `#print axioms` 只有三条标准公理）。
其中 **`hAxL`/`hCut` 正是本文档下面记为「所需相容律不存在」的两支**——
`ShCraigElimNegLaw.iT_neg`（一般 `iT`/`neg` 相容律）一旦证成，两支即通。

## 剩余三支的精确障碍（2026-10-11 本机核实）

`hAll`/`hExs`/`hShift` 要的是 `iT` 与 `shift`/`setShift`/`substs1` 的相容律。
本机读 Foundation 源码后确认：**这不是平凡的交换律**，原因在 `iVE` 与 `termShift`
对绑定变量的处理不同：

| 运算 | 对 `^#z`（bvar） | 对 `^&x`（fvar） |
|---|---|---|
| `iVE`（`InternalTranslate.lean:164`） | `eqAtom (^#(z + 1))` —— **码加一** | `eqAtom (^&x)` —— 不动 |
| `termShift`（Foundation `Term/Functions.lean:210`） | `^#z` —— **不动** | `^&(x + 1)` —— **码加一** |

`iVE` 加一是因为 `eqAtom` 引入一个绑定层（`iVE` 的输出在 `ℒₛₑₜ` 里多一层量词）；
`termShift` 加一是算术侧的自由变量移位。两者作用于**不同的变量类**。

**更准确地说（2026-10-11 探针核实）**：要证的不是
`iVE n (termShift t) = termShift (iVE n t)`（两边甚至不在同一个语言里——
`termShift` 是 `ℒₒᵣ` 的项层运算，`iVE n t` 已经是 `ℒₛₑₜ` 的公式），而是

```
iT 0 (shift ℒₒᵣ p)  与  shift ℒₛₑₜ (iT 0 p)   的关系
```

这是一条**跨语言相容律**：`shift ℒₒᵣ` 先改 `ℒₒᵣ` 侧的项（fvar 加一），
再经 `iVE` 到 `ℒₛₑₜ`；`shift ℒₛₑₜ` 则是先 `iT` 再改 `ℒₛₑₜ` 侧的公式。
在 `iTR` 里 `v.[i]` 走 `iVE`，两条路都要在 fvar 上加一，顺序要对上。

Foundation 在 `DerivabilityCondition/EquationalTheory.lean` 处理同类问题时
用的是 `Semiterm.shift_substs` / `Semiterm.substs_substs` 这类**已备的交换律**；
本包没有对应物，需要新写。

**这一步尚未做**；不要在没弄清之前假定它平凡。

## 未填，以及为什么（2026-10-11 前的记载，保留）

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
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

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

/-- **`translateSeq` 与 `setShift` 交换**（需要 `s` 是公式集，才拿到 `IsSemiformula`）。

逐元素用 `mem_translateSeq_iff` + `mem_setShift_iff`，公式性交给 `iT_shift`。 -/
lemma translateSeq_setShift {s : V} (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    translateSeq (setShift (L := ℒₒᵣ) s) = setShift (L := ℒₛₑₜ) (translateSeq s) := by
  apply Arithmetic.mem_ext; intro y
  simp only [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨iT 0 z, ⟨z, hz, rfl⟩, iT_shift (n := 0) z (hs z hz)⟩
  · rintro ⟨w, ⟨z, hz, rfl⟩, rfl⟩
    exact ⟨shift ℒₒᵣ z, ⟨z, hz, rfl⟩, (iT_shift (n := 0) z (hs z hz)).symm⟩

/-- **`hShift` 支**：`s = setShift (fstIdx d)`，子推导在 `fstIdx d` 上。

`Derivable.shift` 直接给 `Derivable 𝗭𝗙𝗖 (setShift (translateSeq (fstIdx d)))`，
再用 `translateSeq_setShift` 换回 `translateSeq s`。 -/
lemma hShift {s d : V} (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (h : s = setShift (L := ℒₒᵣ) (fstIdx d)) (ih : Q (V := V) d) :
    Q (V := V) (shiftRule s d) := by
  have hfs : IsFormulaSet (L := ℒₒᵣ) (fstIdx d) := by
    rw [h] at hs
    simpa using (IsFormulaSet.setShift_iff (L := ℒₒᵣ) (s := fstIdx d)).mp hs
  simp only [Q, fstIdx_shiftRule, h]
  rw [translateSeq_setShift hfs]
  exact Derivable.shift ih




#print axioms GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq
#print axioms GodelQ.ShCraigElimBranches.hWk
#print axioms GodelQ.ShCraigElimBranches.hVerumIntro
#print axioms GodelQ.ShCraigElimBranches.hAxL
#print axioms GodelQ.ShCraigElimBranches.hAnd
#print axioms GodelQ.ShCraigElimBranches.hOr
#print axioms GodelQ.ShCraigElimBranches.hCut
#print axioms GodelQ.ShCraigElimBranches.translateSeq_setShift
#print axioms GodelQ.ShCraigElimBranches.hShift

/-! ## 2026-10-11 进展（二）：`hShift` 已填，2 支 → 7 支

`iVE_shift`/`iT_shift`（`TranslateShiftCompat.lean`，全 0-sorry）一证，
`translateSeq_setShift` 与 **`hShift`** 立刻通。

**剩余两支的精确障碍**（本机核实）：`hAll`/`hExs` 要的不是 `iT`/`shift` 相容
（已有），而是 **`free`/`substs1` 的相容**：

* `hAll` 需要 `iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))`
  （因为 `iT 0 (^∀ p) = ^∀ imp domZero (iT 1 p)`，`all_m` 的 `q` 被强制成
  `imp domZero (iT 1 p)`）。展开 `free L p = substs1 L ^&0 (shift L p)` 后
  归结为一条**代入相容律**：`iT 0 (subst ℒₒᵣ ?[^&0] σ)` 与
  `subst ℒₛₑₜ ?[^&0] (imp ℒₛₑₜ domZero (iT 1 σ))` 的关系（`σ` 层数 1）。
* `hExs` 同形，用 `substs1 L t p`（`t` 是任意项），需 `iT` 与 `substs1` 的相容。

**注意**：这与 `shift` 的相容**不同类**。`shift` 是「自由变量整体加一」，
两条路都在 fvar 上加一，故能对上；`substs1` 是「把项塞进绑定位置」，
`ℒₒᵣ` 侧塞的是**项**、`ℒₛₑₜ` 侧塞的是**公式**（`domZero` 的引入正是为此），
所以 `iT` 必须把 `substs1` 的项论证翻译成公式论证——这是新的一类引理，
Foundation 的 `DerivabilityCondition/EquationalTheory.lean` 里
`Semiterm.shift_substs` 那套在这里不能照搬。

**建议的下一步**：先证 `iT_substs1` 的项层地基
（`iVE` 与 `subst` 在项上的相容，可能需要 `iVE_subst`），
再证公式层的 `iT_substs1`，最后 `free` 的版本。

## 2026-10-11 第三轮：`hAll` 的结构已实测打通，缺一条代入律

用探针（`probes/W8-hAll-guard-probe-20261011.lean`）实测确认了 `hAll` 的**完整归约结构**，
只剩一条代入相容律未证：

```
hAll 的目标：Derivable 𝗭𝗙𝗖 (translateSeq s)，其中 ^∀ p ∈ s
  all_m (s) (p := imp ℒₛₑₜ domZero (iT 1 p))       -- 注意 q 被 iT_all 强制成这个形状
    ├─ ^∀ (imp domZero (iT 1 p)) ∈ translateSeq s   ← mem_translateSeq_iff + iT_all
    └─ Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s)))
         ← 要先把 ih 从
             Derivable (insert (free ℒₒᵣ p) (setShift (fstIdx d)))   -- ih 给的
           搬到
             Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s)))
```

**两处不相容，都已定位**：

1. **`setShift` 那半**：`translateSeq_setShift`（本文件，已证）把它们对上。✅
2. **`insert` 那半**：`free ℒₛₑₜ (imp domZero (iT 1 p))` 与 `iT 0 (free ℒₒᵣ p)` 不同。
   展开 `free L p = substs1 L ^&0 (shift L p)`：
   * `free ℒₛₑₜ (imp domZero (iT 1 p))`
     `= subst ℒₛₑₜ ?[^&0] (shift ℒₛₑₜ (imp domZero (iT 1 p)))`
     `= subst ℒₛₑₜ ?[^&0] (imp (subst ?[^&0] cDomN) (iT 1 (shift ℒₒᵣ p)))`（用 `iT_shift`）
   * `iT 0 (free ℒₒᵣ p) = iT 0 (subst ℒₒᵣ ?[^&0] (shift ℒₒᵣ p))`

   两者要相等，需要**代入与 `iT` 的交换律**：
   `iT 0 (subst ℒₒᵣ ?[^&0] σ) = subst ℒₛₑₜ ?[^&0] (iT 1 σ)`（`σ` 层数 1）。
   这就是 `iT_substs1` 的核。

**为什么它不同于 `shift` 的相容**：`shift` 是自由变量整体加一，`ℒₒᵣ`/`ℒₛₑₜ` 两侧
对 fvar 都加一，故 `iT_shift` 能对上；`substs1` 是把**项**塞进绑定位置，
`ℒₒᵣ` 侧塞的是项 `^&0`、`ℒₛₑₜ` 侧塞的是 `iVE` 的像（`eqAtom`），
所以要先证一条**项层**的 `iVE_subst`（`iVE` 与 `termSubst` 的相容），
再抬到公式层。

**2026-10-11 第四轮更正（读 Foundation 源码后）**：`Bootstrapping.subst` 只作用于
**bvar**——`substs1 L t p = subst L ?[t] p` 是把 `t` 塞进 `p` 的 **bvar 0**，
fvar 完全不动（`subst_fvar` 类引理）。所以 `substs1 L ^&0 p` 是
「把**自由变量 0 这个项**塞进 bvar 0」，不是「塞进 fvar 0」。
这改变了 `iVE_subst` 的形状：

```
iVE n (termSubst ℒₒᵣ ?[^&0] t)     -- ℒₒᵣ 侧：把 ^&0 塞进 t 的 bvar 0
  vs.
subst ℒₛₑₜ ?[^&0] (iVE n t)        -- ℒₛₑₜ 侧：把 ^&0 塞进 iVE n t 的 bvar 0
```

`iVE n t` 的结构是 `eqAtom`/`ve0`/`ve2` 的复合，bvar 在里面是被 `eqAtom` 包着的
（`^#0` 是 `eqAtom` 自己的绑定变量，不是 `t` 的）。所以 `termSubst` 改的是 `t` 里
**原来的** bvar，而 `subst ℒₛₑₜ ?[^&0]` 会连 `eqAtom` 自己的 `#0` 一起改——
两者**不一致**。正确形状可能要先把 `subst` 的目标限制在 `iVE` 的「外层」
（即用 `substs1` 在**公式层**的对应物），或者改用 `free1` 那类同时处理
bvar 与 fvar 的代入。

**结论**：这一支需要先把 `free` 与 `iT` 的接口想清楚，不能直接照搬 `shift` 的证法。
`free1`（`subst L ?[^&0, ^#0] (shift L p)`）可能才是对的工具——
它同时提供 fvar 与 bvar 的替换位。**这是下一步要核的第一件事。**

## 2026-10-11 第四轮末：两个候选形状，需要一次决定性检验

读 Foundation 的**类型化**规则（`Proof/Typed.lean:271` 的 `all`）后确认：
`all` 的源 sequent 是 `insert φ.free Γ.shift`，其中 `φ.free` 是**公式层**的
`Semiformula.free`（`φ.shift.subst ![fvar 0]`），不是项层的。这说明
Foundation 自己的设计里，`free` 与 `iT` 的交互**本来就该在公式层解决**。

两个候选的代入相容律：

```
(A)  iT 0 (subst ℒₒᵣ ?[^&0] σ) = subst ℒₛₑₜ ?[^&0] (iT 1 σ)        -- 层数 0→1
(B)  iT m (subst ℒₒᵣ w p)      = subst ℒₛₑₜ w (iT m p)             -- 同层数 m
```

**(B) 更可疑也更可能是对的**：`iT` 只在 `all`/`exs` 支改层数，而 `subst` 不改层数，
所以「`iT` 与 `subst` 交换」应当是**同层数**的命题；`hAll` 里 `iT 1 σ` 的层数 1
来自 `all` 的绑定层，不是来自 `subst`。

但 (B) 有一个**直接的反例风险**：`iT m p` 的 `all` 支是 `^∀ (imp domZero (iT (m+1) p'))`，
`subst w` 作用在它上面时会同时改 `domZero` 里的 `#0`——若 `w.[0] ≠ ^#0`，
两侧就不一致。所以 (B) 需要 `w` 满足某种「首分量是 `^#0`」的条件，
而 `substs1 L ^&0` 的 `w = ?[^&0]` 恰恰**不满足**（首分量是 `^&0`）。

**这就是 `hAll` 的真正障碍**：`free` 用的是 `substs1 ^&0`（把 fvar 塞进 bvar），
而 `iT` 在每个绑定层插入 `domZero`，两者对「首分量」的要求冲突。

**下一步的决定性检验已执行（探针 `probes/W8-domZero-subst-probe-20261011.lean`）**，
结论：**检验未通过，但失败点是技术性的、不是数学性的**。

两个检验都归约到同一个待证式：

```
subst ℒₛₑₜ ?[^&0] (neg ℒₛₑₜ domZero) = neg ℒₛₑₜ domZero
```

即「`domZero` 的否定在 `subst ?[^&0]` 下不变」。证明卡在
`substs_substs` 的 `rw` 找不到模式——因为 `?[^#0]` 与 `?[^&0]` 是**同长度的
单元素向量**，`substs_substs` 的两侧形状在 `rw` 时不能自动对上
（`termSubstVec ℒₛₑₜ 1 ?[^&0] ?[^#0]` 需要先化简成 `?[^&0]`）。
这是 `rw` 的匹配问题，不是命题为假。

**所以 `hAll` 的路仍然可行，只是要先补两条小引理**：

1. `termSubstVec ℒₛₑₜ 1 ?[^&0] ?[^#0] = ?[^&0]`（`termSubstVec_cons` + `termSubst_bvar`
   + `nth_adjoin_zero`，本机已试到只差化简）；
2. `subst ℒₛₑₜ ?[^&0] domZero = domZero`（由上一条 + `substs_substs`）。

补完后 `hAll` 的护罩步（`or_m` + `wk`，已实测可证）配上
`free` 的相容律即可收尾。

**2026-10-11 第五轮：两条小引理一条已证、一条归约到 Foundation 的现成工具**

探针 `probes/W8-domZero-subst-partial-20261011.lean` 实测：

* ✅ `termSubstVec ℒₛₑₜ 1 ?[^&0] ?[^#0] = ?[^&0]`
  （`termSubstVec_cons` + `termSubst_bvar` + `simp`，**已 exit 0**）
* ⬜ `subst ℒₛₑₜ ?[^&0] domZero = domZero` 归约到
  `subst ℒₛₑₜ ?[^&0] cDomN = subst ℒₛₑₜ ?[^#0] cDomN`。
  **两条都是恒等**（`cDomN` 是引号化句子，无自由 bvar），
  工具在 Foundation：`typed_quote_substs`（`Formula/Coding.lean:109`）
  与 `Semiformula.quote_def`（`Coding.lean:216`）——
  把 `cDomN` 化到 `Semiproposition` 层再 `simp` 即可。
  同类的还有 `free_quote`（`Coding.lean:127`）——
  **它正是 `free` 与引号的交换律**，是 `hAll` 收尾要用的那类引理。

## 2026-10-11 第六轮：**朴素代入律被证伪**，机制已弄清

探针 `probes/W8-naive-subst-counterexample-20261011.lean` **实测出反例**：

```
subst ℒₛₑₜ ?[^&0] (iVE 1 ^#0)  = ^rel 2 cEqN (^&0 ∷ ^#1 ∷ 0)
iVE 0 (^&0)                    = ^rel 2 cEqN (^#0 ∷ ^&0 ∷ 0)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 不同
```

**机制**：`iVE n ^#z = eqAtom ^#(z+1)`，而 `eqAtom t = ^rel 2 cEqN (?[^#0, t])`——
`eqAtom` **自带一个 `#0` 绑定**（它编码的是 `#0 = t`）。所以

* `iVE 1 ^#0` 里的 `#0` 是 `eqAtom` 自己的绑定变量，`subst ?[^&0]` 会把它改成 `^&0`；
* 而 `iVE 0 ^&0` 的首分量仍是 `eqAtom` 自己的 `^#0`。

两者因此**必然不同**。任何「`iT`/`subst` 交换」的朴素形状都是**假的**。

**这对 `hAll` 的后果**：`hAll` 要证的目标
`Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) (setShift (translateSeq s)))`
里，`free ℒₛₑₜ X = substs1 ^&0 (shift X)` 作用在 `iT 1 p` 的**外**，
而 `iT 1 p` 内部每个 `eqAtom` 都有自带的 `#0`——代入会穿透进去。
所以**不能**走「先 `iT` 后 `subst`」的路。

**正确方向（待核）**：应当走「先 `subst` 后 `iT`」，即证明

```
iT 0 (subst ℒₒᵣ w p) = subst' ℒₛₑₜ (iVE-像的向量) (iT 0 p)
```

其中 `subst'` 的向量必须**逐分量对齐** `iVE` 的输出（因为 `iT` 的绑定层数变化）。
探针 `ProbeY` 已实测：正确的向量形状是 `^#0 ∷ termBShiftVec w`（即 `qVec` 的形状），
而不是 `w` 本身——这正是 `substs_all` 用 `qVec L w` 的原因。

**`domZero` 那一支已被 `domZero_eq_cDomN` 化解**（本轮已证）：
`domZero` 是引号化句子、无绑定结构，故 `subst` 不动它。

**下一步**：把 `iT`/`subst` 的正确形状用 `semiformula_result_induction` 试出来
（先在 `rel` 支上验证向量对齐），再回填 `hAll`。

**另记（对本包结构的观察）**：`iT m (subst ℒₒᵣ w p) = subst ℒₛₑₜ w (iT m p)`
这个「同层数」形状是**不成立的**——`iT` 的 `all` 支插入 `domZero`，
而 `domZero` 里的 `#0` 会被 `subst w` 改到。所以 `iT`/`subst` 的相容律
必须带「`w.[0] = ^#0`」之类的**护罩条件**（这正是 `free` 用 `substs1 ^&0`
时 `w = ?[^&0]` 不满足、需要单独处理的原因）。**这是 hAll 的真正难点所在。**

**`hAll` 的护罩步（已实测可证）**：从
`Derivable (insert A S)` 得 `Derivable (insert (imp B A) S)`——
用 `or_m` 在 `insert (imp B A) S` 上（因 `imp B A = neg B ^⋎ A` 是 `rfl`），
再把 `insert A S ⊆ insert (imp B A) S` 用 `wk` 弱化（需 `IsFormula` 的 `A`、`B`）。 -/

end GodelQ.ShCraigElimBranches
