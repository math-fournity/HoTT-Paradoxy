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

**第七轮：向量长度不匹配是深层障碍（本机实测）**

`substs_rel` 的形状是 `subst L w (^rel k R v) = ^rel k R (termSubstVec L k w v)`——
它用**整个 `w`** 去替换 `v` 的每个分量。于是对 `eqAtom t = ^rel 2 cEqN ?[^#0, t]`：

```
subst ?[^#0, s] (eqAtom t) = ^rel 2 cEqN (termSubstVec 2 ?[^#0,s] ?[^#0,t])
                            = ^rel 2 cEqN (^#0 ∷ (subst ?[^#0,s] t) ∷ 0)
```

**而 `t` 拿到的向量是长度 2 的 `?[^#0, s]`，不是长度 1 的 `?[s]`**。
两者在 `t` 是 bvar 时给出**不同的结果**：

* `subst ?[^#0, s] ^#1 = (?[^#0,s]).[1] = s` ✅
* `subst ?[s] ^#1 = (?[s]).[1] = 0` ❌（越界）

即 `iT 0 (subst ℒₒᵣ ?[^&0] σ)` 与 `subst ℒₛₑₜ ?[^&0] (iT 1 σ)` 的向量长度
在**每一层绑定**上都会错位——`iT` 每遇到一个 `all`/`exs` 就插入一层，
但 `eqAtom`/`ve2` 自带 2 层。**这是 `hAll`/`hExs` 的真正难点**，
不是「缺一条交换律」那么简单。

**可能的出路（待核）**：

1. **不走 `subst` 交换，改走 `free` 的显式计算**：`hAll` 需要的其实只是
   `free ℒₛₑₜ (imp domZero (iT 1 p))` 这个**具体公式**的可导性，
   而不是它与 `iT 0 (free ℒₒᵣ p)` 的相等。可以试着直接从 `ih` 出发，
   用 `Derivable` 的规则（`all_m` 的反向、`wk`、`cut`）搭桥，
   完全避开 `subst` 交换律。
2. **给 `hAll` 的 `P` 谓词加一条「层数对齐」的护罩**（类似 `iT_shift` 的 `param = n`），
   让向量长度在归纳假设里就对齐。

**第八轮：`domZero` 的代入行为已完全算清（本机实测，两条引理 exit 0）**

```
termSubstVec ℒₛₑₜ 1 ?[^&0] ?[^#0] = ?[^&0]                        ✅ 已证
subst ℒₛₑₜ ?[^&0] domZero = subst ℒₛₑₜ ?[^&0] cDomN              ✅ 已证
```

**重要更正**：`domZero` **不是**代入不变的！`cDomN = ⌜arithTrln.domain⌝`
而 `arithTrln.domain : Semisentence ℒₛₑₜ 1` 层数是 **1**——它有一个**自由 bvar `#0`**
（就是 `x ∈ ω` 里的那个 `x`）。所以 `subst ?[^&0] cDomN` 会把那个 `#0` 换成 `^&0`，
与 `cDomN` 不同。

（`domZero_eq_cDomN` 仍然正确且有用：它说明 `domZero` 的**形状**是引号，
没有 `domZero` 自己的额外绑定层；但它不意味着 `domZero` 对代入免疫。）

**第九轮更正（重要）**：我上面那句「`free` 会把所有 `domZero` 的 `#0` 换成 `^&0`」
**是错的**。`substs_all` 的语义是**防捕获代入**：

```
substs_all : subst L w (^∀ p) = ^∀ subst L (qVec L w) p
qVec L w = ^#0 ∷ termBShiftVec L (len w) w
```

在绑定层下，向量首分量被换成 `^#0`——即**新绑定变量 `#0` 不被替换**。
所以 `subst ?[^&0]` 作用在 `^∀ (imp domZero Y)` 上时，`domZero` 里的 `#0`
是**被 `^∀` 绑定的**，**不会被改**。

只有**顶层**（不在任何绑定层下）的 `domZero`，其 `#0` 是自由的，才会被替换。
`free_imp_domZero`（本轮已证）正是这个顶层情形：
`free (imp domZero X) = imp (subst ?[^&0] domZero) (free X)`。

**这对 `hAll` 的含义**：`all_m` 要的 `free ℒₛₑₜ q` 里 `q = imp domZero (iT 1 p)`
是**顶层**的 `imp`，故其 `domZero` 确实被替换。而 `iT` 内部各绑定层下的
`domZero` 不受影响。**这正是两边能对上的关键**——需要把
`iT 0 (subst ?[^&0] σ)` 与 `subst ?[^&0] (iT 1 σ)` 逐层对齐，
顶层的那一个 `domZero` 差异由 `free_imp_domZero` 显式携带。

## 2026-10-12 第十七轮：`ih` 搬运已机器验证；`iT_free` 等式**被机器判定为假**

**（a）`ih` 的搬运打通了**（`ShCraigElimSetupQ.lean` 的 `hAll` 支，已 exit 0 到
只剩一条 `sorry`）。

之前第十三/十四轮讨论的「`IsFormulaSet` 缺口」与「`translateSeq_setShift` 需要源公式集」
都已闭合，实际写法只有三步：

```lean
have hfd2 : fstIdx _dd = insert (free ℒₒᵣ p) (setShift ℒₒᵣ s) := _hd.1
have hs' := DerivationOf.isFormulaSet _hd
have hss : IsFormulaSet (L := ℒₒᵣ) s := _hs
have ih' : Derivable 𝗭𝗙𝗖 (insert (iT 0 (free ℒₒᵣ p)) (setShift ℒₜ (translateSeq s))) := by
  have h1 : translateSeq (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s))
      = insert (iT 0 (free ℒₒᵣ p)) (translateSeq (setShift ℒₒᵣ s)) := translateSeq_insert
  have h2 : translateSeq (setShift ℒₒᵣ s) = setShift ℒₜ (translateSeq s) :=
      translateSeq_setShift hss
  have hq : Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx _dd)) := _ih
  rw [hfd2, h1, h2] at hq
  exact hq
```

**两个 Lean 写法要点**（这轮才弄清）：
* `rw [← hfd2]` 方向错了——`hfd2` 的 LHS 是 `fstIdx _dd`，目标里没有它。
  正确做法是**正向**：先在 `have hq := _ih` 上 `rw [hfd2, h1, h2] at hq`，再 `exact hq`。
* `DerivationOf T d s` **不是**独立函数，`.1` 直接给 `fstIdx d = s`；
  `.isFormulaSet` 给 `IsFormulaSet L s`（不需要额外加强归纳不变量——第十四轮的结论正确）。

**（b）`iT_free` 等式被机器判定为假**（探针
`probes/W8-iT-free-NOT-equal-machine-verified-20261012.lean`）。

取 `p = ^rel 2 cEqN ?[^#0, ^#1]`（层 1），两侧 `simp only` 归一化后：

```
LHS = ^rel 2 cEqN (iVE 0 ^&0 ∷ iVE 0 ^&1 ∷ 0)
RHS = substs1 ℒₜ ^&0 (shift ℒₜ (imp ℒₜ domZero (^rel 2 cEqN (iVE 1 ^#0 ∷ iVE 1 ^#1 ∷ 0))))
```

**顶层构造子不同**（`^rel` vs `imp`），必然不相等。这比第十五轮的手算更强——
是机器归一化后的确定性结论。

**（c）但原子层的换名律是对的**（本轮同时验证，
`probes/W8-qVec2-atomic-rename-20261012.lean`，exit 0）：

```
subst ?[^#0, ^#1, ^&0] (^rel 2 cEqN ?[^#0, ^#2]) = ^rel 2 cEqN ?[^#0, ^&0]
```

即：**逐层交换确实不成立**（第十二/十五轮），但**单层的换名在 `qVec²` 向量下是对的**。
这两件事不矛盾——前者说整条交换律的形状不是 `iT m (subst w p) = subst w (iT m p)`，
后者说原子支的代入行为可以精确计算。

**（d）两处层数更正**（探针 `probes/W8-iVE-shape-level1-20261012.lean`）：

* `iVE 1 ^#0 = ^rel 2 cEqN ?[^#0, ^#1]` —— **层 1，不是 3**。
  先前把 `eqAtom` 的参数位 `#1` 误当成公式层数，导致所有 `IsSemitermVec` 的
  `< 3` 界类型错误。正确说法是 `isSemiformula_iVE : IsSemiterm ℒₒᵣ n t → IsSemiformula ℒₜ (n+1) (iVE n t)`。
* `conjunct 2 i 0 (iVE k t)` 的第二分量是 `subst (^#0 ∷ shiftVec 2 i) (iVE k t)`，
  不是裸的 `iVE k t`。

**下一步的岔路（需要研究发起人定）**：
1. **不走等式**，从 `ih'` 出发用 `Derivable` 规则（`wk`/`cut`/`em`）直接构造目标；
2. **改 `iT` 的 `all` 支语义**——这是接口级改动，`iT` 已被 C-390/C-391 等收据引用。


**第十轮：对齐所需的向量形状已实测确认**

```
qVec ℒₛₑₜ ?[^&0] = ^#0 ∷ ?[^&0]        ✅ 已证（exit 0）
```

（因 `termBShiftVec` 对 fvar 不动，`termBShiftVec 1 ?[^&0] = ?[^&0]`。）

**手算验证了 bvar 支的一致性**：

```
iVE 0 (subst ?[^&0] ^#0)  = iVE 0 ^&0 = eqAtom ^&0 = ^rel 2 cEqN (?[^#0, ^&0])
subst (qVec ?[^&0]) (iVE 1 ^#0) = subst (^#0 ∷ ^&0 ∷ 0) (eqAtom ^#1)
                                = ^rel 2 cEqN (?[^#0, ^&0])          ✓ 相同
```

**关键点**：`qVec` 的首分量 `^#0` 恰好保护了 `eqAtom` 自己的绑定变量，
而第二分量 `^&0` 替换掉 `eqAtom` 的参数 `^#1`——**这正是 `substs_all`
用 `qVec` 而不是 `w` 的原因**，也是 `iT`/`subst` 相容律的**正确形状**：

```
iT m (subst ℒₒᵣ w p) = subst ℒₛₑₜ (qVec ℒₛₑₜ (iVE-像 w)) (iT (m+1) p)
```

（层数 `m → m+1` 因为 `iT` 的 `all`/`exs` 支插入绑定层；
向量的每个分量要经 `iVE` 翻译成公式层的项。）

**第十一轮：`subst_eqAtom_qVec` 的精确条件已定，只差一条项层引理**

探针 `probes/W8-termSubst-prefix-need-20261011.lean` 实测确认：
`subst (^#0 ∷ s ∷ 0) (eqAtom t) = eqAtom (subst ?[s] t)` **不是无条件成立的**——
`subst` 会把整个向量 `^#0 ∷ s ∷ 0` 交给 `t`，而 `?[s]` 只给一个分量。
两者只在 **`t` 不含 bvar ≥ 2** 时一致（此时两边 `[0]=^#0`、`[1]=s` 都对得上）。

**精确条件**：`termBV ℒₛₑₜ t ≤ 1`（等价于 `IsSemiterm ℒₛₑₜ 1 t`）。

**缺的引理**（一条，项层）：

```
termSubst L w t 只依赖 w 的前 (termBV t + 1) 个分量
```

即 `(∀ i ≤ termBV t, w₁.[i] = w₂.[i]) → termSubst L w₁ t = termSubst L w₂ t`。
这是 `termSubst` 的**有限依赖性**，沿 `t` 的结构归纳即可
（`termSubst_bvar` 只取 `w.[z]`，`z < termBV t`；`func` 支交给向量归纳假设）。

**证完后**：`subst_eqAtom_qVec`（条件版）→ `iVE_subst` 的 bvar 支
→ 整个 `iT_subst` 相容律 → `hAll`/`hExs`。

**第十二轮：向量首分量不匹配 —— 精确障碍（本机实测反例）**

探针 `probes/W8-vector-first-component-20261011.lean` 直接算出：

```
termSubst ?[^&0] ^#0              = (?[^&0]).[0] = ^&0
termSubst (^#0 ∷ ^&0 ∷ 0) ^#0     = (^#0 ∷ ^&0 ∷ 0).[0] = ^#0
                                 ^^^^ 不同！
```

所以 `?[^&0]` 与 `^#0 ∷ ^&0 ∷ 0` 在 **bvar 0** 上给出不同结果——
即 `subst ?[^&0]`（`free` 用的）与 `subst (qVec ?[^&0])`（`substs_all` 用的）
**不是同一个运算**。前者替换 `#0`，后者保护 `#0`。

**这对 `hAll` 是决定性的**：`free L p = substs1 L ^&0 (shift L p) = subst L ?[^&0] (shift L p)`
用的是**替换** `#0` 的语义；而 `iT` 在 `all` 支内部用的是 `substs_all` 的
**保护** `#0` 的语义。**两者在语义上就是不同的**，
不是「缺一条交换律」能弥补的。

**结论（对本支的重新评估）**：`hAll` 需要的等式
`iT 0 (free ℒₒᵣ p) = free ℒₛₑₜ (imp domZero (iT 1 p))` **很可能是假的**——
或至少不能由「`iT` 与 `free` 交换」得到。正确的做法可能是：

* **不用 `all_m`**，改用 `Derivable` 的其他规则（`wk`/`cut`/`em`）直接构造
  `Derivable (translateSeq s)`；
* 或**改 `iT` 的定义**，让 `all` 支用「替换」语义而非「保护」语义——
  但这会改变整个包的接口，代价大；
* 或**承认这一支需要新的数学**，把它作为独立的开放问题记录下来。

**第十三轮：直接攻 `hAll` 的目标，发现 `IsFormulaSet` 缺口（本机实测）**

探针 `probes/W8-hAll-formula-set-gap-20261011.lean` 实测：把 `ih` 的 sequent
按 `hd` 展开成

```
translateSeq (fstIdx d) = insert (iT 0 (free ℒₒᵣ p)) (setShift ℒₛₑₜ (translateSeq (fstIdx dd)))
```

**这一步本身是通的**（`translateSeq_insert` + `translateSeq_setShift`），
但 `translateSeq_setShift` 要求**源**是公式集：

```
translateSeq_setShift : IsFormulaSet ℒₒᵣ s → translateSeq (setShift ℒₒᵣ s) = setShift ℒₛₑₜ (translateSeq s)
```

而 `hAll` 支给我们的假设里**只有**
`Derivable (translateSeq (fstIdx d))`——由 `Derivable.isFormulaSet` 得
`IsFormulaSet ℒₛₑₜ (translateSeq (fstIdx d))`，即**像**是公式集；
`IsFormulaSet ℒₒᵣ (fstIdx dd)`（**源**是公式集）**拿不到**。

**这是一个独立的、更基本的缺口**：`induction1` 的 `hAll` 支的假设
（`DerivationOf T dp (insert (free L p) (setShift L s))`）里
**没有** `IsFormulaSet L s` 这一项，而 `translateSeq_setShift` 需要它。

**可能的修法**：
1. 给 `P`/`Q` 谓词**加强**：把 `IsFormulaSet ℒₒᵣ (fstIdx d)` 作为归纳不变量的一部分
   （`induction1` 的 `P : V → Prop` 只作用在推导编码上，但可以改成
   `fun d ↦ IsFormulaSet ℒₒᵣ (fstIdx d) ∧ Derivable ...`，只要保持 Σ1）；
2. 或证明 `IsFormulaSet ℒₛₑₜ (translateSeq s) → IsFormulaSet ℒₒᵣ s`
   （需要 `iT` 的单射性，可能比 1 更难）。

**修法 1 更可行**：`IsFormulaSet` 是 Π1（`∀ p ∈ s, IsSemiformula ...`），
与 `Derivable`（Σ1）合取后仍是 **Σ1**（`∃` 后可跟 Π1 有界量词），
`induction1` 的 `hP` 应当仍能接受。**这是下一步该做的第一件事。**

**第十四轮：`IsFormulaSet` 缺口已闭合（本机实测）**

探针 `probes/W8-derivationOf-formulaSet-20261011.lean` 实测确认：

```lean
DerivationOf T d s → IsFormulaSet L s     -- 即 `DerivationOf.isFormulaSet`，直接可得 ✅
IsFormulaSet L (insert (free L p) (setShift L s)) → IsFormulaSet L (setShift L s)   ✅
IsFormulaSet L (setShift L s) → IsFormulaSet L s    -- `IsFormulaSet.setShift_iff`  ✅
```

**所以 `IsFormulaSet ℒₒᵣ (fstIdx d)` 根本不用加强归纳不变量**——
`hAll` 支的假设里就有 `DerivationOf T d (insert (free L p) (setShift L s))`，
`DerivationOf.isFormulaSet` 直接给出 `IsFormulaSet L (fstIdx d)`，
再两步拆出 `IsFormulaSet L s`。**我第十三轮的「缺口」判断是错的**——
`IsFormulaSet` 一直在手边，只是我没看 `DerivationOf` 的假设。

**修正后的 `hAll` 归约链**（全部零件已就位）：

```
hAll：目标 Derivable (translateSeq s)
  all_m 需要 ^∀ q ∈ translateSeq s，其中 q := imp domZero (iT 1 p)
    ← mem_translateSeq_iff + iT_all ✅
  all_m 需要 Derivable (insert (free ℒₛₑₜ q) (setShift (translateSeq s)))
    ← ih : Derivable (translateSeq (fstIdx d))
         = Derivable (insert (iT 0 (free ℒₒᵣ p)) (setShift (translateSeq s)))
           [translateSeq_insert + translateSeq_setShift，**公式集由 DerivationOf.isFormulaSet 给**]
    ← 需把 iT 0 (free ℒₒᵣ p) 换成 free ℒₛₑₜ (imp domZero (iT 1 p))
       **这一条仍未证**（第十三/十二轮已证明朴素形状为假）
```

**所以 `hAll` 现在只剩一条待证等式**（其余全部已就位）：
`iT 0 (free ℒₒᵣ p) ≡ free ℒₛₑₜ (imp domZero (iT 1 p))`（等价或互相可导）。

**第十二轮的反例说明这条等式不能靠「`iT` 与 `free` 交换」得到**
（`free` 用替换语义、`iT` 的绑定层用保护语义）。
但**未必为假**——反例只说明「逐层交换」不对，两边**整体**可能仍相等
（因为 `free` 只作用于顶层，而 `iT` 的 `domZero` 插入正好补偿）。

**第十五轮：等式为假（domZero 计数不同），且发现 Q/P 接口不一致**

**(a) 等式为假**。对 `p = ^∀ (^rel 2 R ?[^#0, ^#1])`（层数 1、含一个 `all`）手算：

```
左边 iT 0 (free ℒₒᵣ p)：
  free p 把自由 #0 换成 ^&0，p 的 all 还在
  → ^∀ (imp domZero (iT 1 (free 的体)))            —— **一层** imp domZero
右边 free ℒₛₑₜ (imp domZero (iT 1 p))：
  iT 1 p = ^∀ (imp domZero (iT 2 体))
  顶层再包一层 imp domZero
  → 展开后                                        —— **两层** imp domZero
```

层数不同 ⟹ **两边不相等**。这解释了为什么 `hAll` 走「等式」的路不通。

**(b) 更重要的发现：`Q`/`P` 接口不一致**。

* `ShCraigElimSetup.induction_setup` 的目标谓词是 **`P d := Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`**
  （`ShCraigElimPredicate.lean:40`），其 `hP` 由 `p_defined` 提供；
* 而本轮填的 `hAxL`/`hAnd`/…/`hShift` **全部证的是 `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`**
  （`ShCraigElimPredicate.lean:65`）。

两者由 `Provable.toDerivable` / `Derivable.toProvable`
（`Basic.lean:947`，即 `internal_provable_iff_internal_derivable`）互转，
**但它们对 sequent 的形状要求不同**：`Provable T φ` 是单公式，
`Derivable T s` 是 sequent。`Derivable.toProvable` 要求 `s = φ ⫽ ∅`。

**所以接进 `induction_setup` 时**，每个支的结论 sequent
（如 `translateSeq s`）**不一定是单公式形**——需要先处理这一层。
这是接装时必须先解决的一步，**比 `hAll`/`hExs` 更靠前**。

**下一步（优先级调整）**：
1. 先解决 `Q`/`P` 的接装（把已填的 7 支从 `Q` 转成 `P` 可用的形式）；
2. 再攻 `hAll`/`hExs`——**不能再走等式**，需要考虑
   「用 `Derivable` 规则直接从 `ih` 构造」或「改 `iT` 的 `all` 支定义」。

**注意**：第 2 条若确认需要改 `iT` 定义，那是接口级改动，
应先与研究发起人确认（本分支的 `iT` 已被 C-390/C-391 等收据引用）。

**第十六轮：`P` 谓词的语义问题已确认（本机实测）**

`Provable T φ` 的签名是 `(T : Theory L) → V → Prop`——**它接受任意 `V`**，
所以 `P d := Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d))` **能通过类型检查**，
但语义上把 `translateSeq s`（一个**集合**）当成了**单个公式**。

**这不是编译错误，是语义错误**：`Provable` 的定义（`Basic.lean:539` 附近）
是 `∃ d, Proof d φ`，而 `Proof d φ := DerivationOf T d {φ}`——
它要求推导的结论 sequent **恰好是单元素集 `{φ}`**。
`translateSeq s` 一般不是单元素集，故 `P d` 在 `s ≠ {φ}` 时**几乎必然为假**。

**后果**：`induction_setup` 的 `P` 谓词**用错了**——
正确的归纳不变量应当是 `Q d := Derivable 𝗭𝗙𝗖 (translateSeq (fstIdx d))`
（sequent 层），而这正是本轮填的 7 支所用的。

**所以接装方案很明确**：
1. 把 `induction_setup` 的 `hP` 从 `p_defined` 换成 **`q_defined`**
   （`ShCraigElimPredicate.lean:72` 已经就位，`Q` 也是 Σ1 谓词）；
2. 目标从 `P d` 改成 `Q d`；
3. 各支直接用本轮已填的 `hAxL`/…/`hShift`（它们证的就是 `Q`）。

**`ShCraigElim` 本身的结论**仍是「`Provable Sh.craig ⌜σ⌝ → Provable 𝗭𝗙𝗖 ⌜translate σ⌝」，
其中两侧都是**单公式** `Provable`——这没问题，因为那一步不走 `induction1`。
`induction1` 只用在**中间的**「`Derivable Sh.craig s → Derivable 𝗭𝗙𝗖 (translateSeq s)`」
这一步，那一步用 `Q` 是对的。

**下一步（优先级最高，比 hAll 靠前）**：把 `induction_setup` 改用 `Q`。

---

## 第十七轮：`Q` 版 `induction_setup` 已完成（`ShCraigElimSetupQ.lean`）

**本机实测 exit 0**：新增 `ShCraigElimSetupQ.induction_setup_Q`，
`hP := q_defined.to_definable`（`Q` 是 Σ1 谓词），
**7 支已接入**（`hAxL`/`hVerumIntro`/`hAnd`/`hOr`/`hWk`/`hShift`/`hCut`），
剩 `hAll`/`hExs`/`hRoot` 三支。

接装时解决的两处细节（都是 `DerivationOf` 的用法）：
* `hAnd`/`hOr`/`hCut` 要 `fstIdx dp = …`，从 `DerivationOf` 用 `.1` 取；
* `hCut` 要 `IsSemiformula ℒₒᵣ 0 p`，从 `h₁.isFormulaSet p (by simp)` 拿
  （`h₁` 的 `DerivationOf` 给 `IsFormulaSet (insert p s)`）。

---

## 第十八轮：`hAll` 的**最终诊断**——本支需要新的数学，不是缺引理

把 `hAll` 的所有可能路线逐一实测后，结论如下。

**目标**：`Derivable (translateSeq s)`，其中 `^∀ p ∈ s`。
**`ih`**：`Derivable (insert (iT 0 (free ℒₒᵣ p)) (setShift (translateSeq (fstIdx d))))`。

**`all_m` 要求的前提**：`Derivable (insert (free ℒₛₑₜ q) (setShift (translateSeq s)))`，
其中 `q := imp ℒₛₑₜ domZero (iT 1 p)`（由 `iT_all` 强制）。

**中间缺的那一步**是：把 `iT 0 (free ℒₒᵣ p)` 换成 `free ℒₛₑₜ q`。
三轮实测证明这条路**走不通**：

| 轮次 | 检验 | 结果 |
|---|---|---|
| 第十二 | `termSubst ?[^&0] ^#0` vs `termSubst (^#0 ∷ ^&0 ∷ 0) ^#0` | `^&0` vs `^#0`——**不同** |
| 第十五(a) | `p` 含 `all` 时两边的 `imp domZero` 层数 | 一层 vs 两层——**不等** |
| 第十八 | `iVE 1 ^#0` 经 `subst ?[^&0]` | `^&0 ∷ 0 ∷ 0` vs `^#0 ∷ ^&0 ∷ 0`——**不同** |

**根因**：`iVE` 引入的 `eqAtom` **自带一个绑定变量 `#0`**
（它编码的是 `#0 = t`）。外层的 `subst`（无论用哪个向量）
都会穿透进去改那个 `#0`，而 `iT` 在绑定层下用的是 `substs_all` 的
**保护**语义（`qVec` 首分量换成 `^#0`）。**两种语义不可调和。**

**这不是「缺一条引理」**：三轮反例覆盖了朴素形状、层数对齐形状、
`qVec` 对齐形状——都不成立。`hAll`（与同形的 `hExs`）需要的是
**结构性的新想法**，可能是：

1. **改 `iT` 的 `all`/`exs` 支定义**：让它们用「替换」而非「保护」语义
   （代价：`iT` 已被 C-390/C-391 等收据引用，属接口级改动，**需研究发起人裁定**）；
2. **绕开 `induction1` 的 `hAll` 支**：直接对 `Sh.craig` 推导的结构做别的归纳
   （可能更贴合「Craig 技巧的公理都是封闭句」这一事实）；
3. **换 `translateSeq` 的定义**：让它对 `setShift`/`free` 的交互更友好。

## 第十九轮：`hRoot` 的诊断——它就是 D3 本身

`hRoot` 支：`s` 是公式集，`p ∈ s`，`p ∈ Sh.craig.Δ₁Class`，
目标 `Derivable (translateSeq s)`。走 `Derivable.by_axm` 需要：

```
IsFormulaSet ℒₛₑₜ (translateSeq s)   ✅ isFormulaSet_translateSeq
iT 0 p ∈ translateSeq s              ✅ mem_translateSeq_iff
iT 0 p ∈ 𝗭𝗙𝗖.Δ₁Class                 ⬜ ← 全部困难所在
```

最后一条**正是 D3 的实质**：`Sh.craig` 的公理（`σ.padding s` 形）
经 `iT` 翻译后要落在 `𝗭𝗙𝗖.Δ₁Class`（或至少 𝗭𝗙𝗖 可证）。
这就是 `Z0UniBridge.ShCraigElim` 的另一面——`hRoot` 支不是「填一个洞」，
而是**把整条消去的实质集中在这一点上**。

**这也解释了为什么 `hAll`/`hExs` 难**：三条支（`hAll`/`hExs`/`hRoot`）
分别对应「∀ 翻译的绑定层」「∃ 翻译的绑定层」「Craig 公理的翻译」，
都是**跨语言翻译**的实质困难，不是技术细节。

---

## 本轮（2026-10-11 后半）总结

**新增可交付物**：
* `ShCraigElimSetupQ.lean`——`Q` 版 `induction_setup`，7 支已接入（exit 0）；
* `TranslateShiftCompat.lean` 扩到 ~900 行，新增 `domZero_eq_cDomN`、
  `free_imp_domZero` 等引理；
* 探针 20+ 份归档进 `probes/`，覆盖 `hAll` 的所有路线。

**精确刻画的三条剩余支**：

| 支 | 障碍 | 性质 |
|---|---|---|
| `hAll` | `iVE` 的 `eqAtom` 自带 `#0`，与外层 `subst` 的语义冲突 | 需新想法 |
| `hExs` | 同 `hAll`（`substs1` 版） | 需新想法 |
| `hRoot` | 就是 D3：`iT 0 p ∈ 𝗭𝗙𝗖.Δ₁Class` | 需新数学 |

**已排除的路线**（三轮反例，不再重复尝试）：
* 「`iT` 与 `free`/`subst` 逐层交换」——第十二、十五、十八轮已证伪；
* 「`iT` 与 `free` 整体相等」——第十五轮已证伪（`domZero` 层数不同）。

**结论**：`induction1` 这条路线在本轮已推进到**它的自然边界**——
7/10 支 + 完整框架 + 3 支的精确障碍刻画。
继续需要的是**结构性决策**（改 `iT` 定义 / 换路线 / 承认这是开放问题），
超出「继续填支」的范围。

**结论**：`hAll` 不能靠「`iT` 与 `free`/`subst` 交换」来证——
两者的语义本就不同。出路只有出路 1：
**直接从 `ih` 用 `Derivable` 规则搭桥**，把
`Derivable (insert (iT 0 (free ℒₒᵣ p)) S')` 变成
`Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) S')`，
中间用 `cut` + 两条公式的**互相可导性**（而不是相等）。

**另记（对本包结构的观察）**：`iT m (subst ℒₒᵣ w p) = subst ℒₛₑₜ w (iT m p)`
这个「同层数」形状是**不成立的**——`iT` 的 `all` 支插入 `domZero`，
而 `domZero` 里的 `#0` 会被 `subst w` 改到。所以 `iT`/`subst` 的相容律
必须带「`w.[0] = ^#0`」之类的**护罩条件**（这正是 `free` 用 `substs1 ^&0`
时 `w = ?[^&0]` 不满足、需要单独处理的原因）。**这是 hAll 的真正难点所在。**


**2026-10-12 第十八轮更正（重要，推翻上一段）**：上一轮说「出路只有出路 1（互相可导）」，
**这是错的**。同文件第十七轮末已经写下正确的下一步：

> 用 `cut` + 两条公式的**互相可导性**（而不是相等）

也就是说：不需要 `iT 0 (free ℒₒᵣ p) ≡ free ℒₛₑₜ (imp domZero (iT 1 p))`，
只需要这两条公式在 𝗭𝗙𝗖 里**互相可导**（弱得多）。第十七轮的机器归一化只否证了**相等**，
**没有否证互相可导**——这两件事强度差很远，我当时混淆了。

`ih'` 已经给出了 `Derivable (insert (iT 0 (free ℒₒᵣ p)) S')`；
要把它变成 `Derivable (insert (free ℒₛₑₜ (imp domZero (iT 1 p))) S')`，
走 `Derivable.cut` 配上两条方向的蕴含式即可，
这两条蕴含式都可以是 `Provable 𝗭𝗙𝗖` 层的命题恒真式
（`hRoot_core` 已给出「可证公式入 sequent」的搬运）。

**所以 `hAll` 的剩余缺口精确地是两条内部可证性命题**：

```
(A) Provable 𝗭𝗙𝗖 (imp (iT 0 (free ℒₒᵣ p)) (free ℒₜ (imp domZero (iT 1 p))))
(B) Provable 𝗭𝗙𝗖 (imp (free ℒₜ (imp domZero (iT 1 p))) (iT 0 (free ℒₒᵣ p)))
```

这两条是**语义命题**（翻译后的公式在 𝗭𝗙𝗖 中可导），不再是纯语法等式。
已确认的护罩步（同文件上文）说明 `insert A S → insert (imp B A) S` 方向可证；
`insert (imp B A) S → insert A S` 是 modus ponens 的 sequent 版
（`replace_of_imp`，`ShCraigElimSetupQ.lean` 已证）。

**`hAll` 的护罩步（已实测可证）**：从
`Derivable (insert A S)` 得 `Derivable (insert (imp B A) S)`——
用 `or_m` 在 `insert (imp B A) S` 上（因 `imp B A = neg B ^⋎ A` 是 `rfl`），
再把 `insert A S ⊆ insert (imp B A) S` 用 `wk` 弱化（需 `IsFormula` 的 `A`、`B`）。 -/

end GodelQ.ShCraigElimBranches
