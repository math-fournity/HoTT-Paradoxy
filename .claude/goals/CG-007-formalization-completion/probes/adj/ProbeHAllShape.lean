import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 7（**不是收据**）：`hAll` 支义务的**精确定形状**与所需相容律的**精确陈述**。

## 义务

`Derivation.induction1` 的 `hAll`（Foundation `Proof/Basic.lean:652`）：
```
hAll : ∀ s, IsFormulaSet ℒₒᵣ s → ∀ p d, ^∀ p ∈ s →
  DerivationOf Sh.craig d (insert (free ℒₒᵣ p) (setShift ℒₒᵣ s)) →
  Provable 𝗭𝗙𝗖 (translateSeq (fstIdx d)) → Provable 𝗭𝗙𝗖 (translateSeq s)
```

## 化简链

1. `^∀ p ∈ s`（`hAll` 的假设 `hp`）。
2. IH：`Provable 𝗭𝗙𝗘 (translateSeq (insert (free p) (setShift s)))`
   `= Provable 𝗭𝗙𝗖 (insert (iT 0 (free p)) (translateSeq (setShift s)))`（`translateSeq_insert`）。
3. 目标：`Provable 𝗭𝗙𝗖 (translateSeq s)`。

**注意**：`translateSeq` 只翻译**闭公式**（层 0）。`free ℒₒᵣ p` 是 `Formula ℒₒᵣ`（层 0），
`setShift ℒₒᵣ s` 的成员也是层 0——所以 `iT 0` 适用，没有被翻译的量词在层数上炸开。
这与 `hShift` 不同（下面单独说）。

## 真正要的两条

**(A) 公式层**：`free ℒₒᵣ p` 与 `^∀ p` 的关系。Foundation `Formula/Typed.lean:261`：
```lean
noncomputable def free (φ : Semiformula V L 1) : Formula V L := φ.shift.subst ![Semiterm.fvar 0]
```
即 `free p` 是"把 `p` 的第 0 个约束变量换成第 0 个自由变量"。

**(B) 集合层**：`iT 0 (free p)` 与 `iT 0 p` 在 ℒₛₑ₧ 侧的关系。目标里 `^∀ p ∈ s`，翻译后是
`iT 0 (^∀ p)`，而 `iT_all` 说 `iT n (^∀ p) = ^∀ (imp domZero (iT (n+1) p))`——**层数升一**。
`free p` 是层 0 的公式，`iT 0 (free p)` 是层 0 的结果，不经过 `iT_all`。

所以 (B) 不是"`iT` 与 `free` 交换"，而是**两条独立的翻译**（`iT 0 (free p)` 与 `iT 0 p`）
在一个 ∀引言里对上。这正是层数错开的来源。

本探针只固定形状，不断言可证。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeHAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- setShift 的语义接口（Foundation，现成，本身就是 iff）
#check @mem_setShift_iff

-- translateSeq 的成员接口（本包）
#check @mem_translateSeq_iff

-- free 的定义（Foundation）
#check @free

-- iT_all：层数升一的形状（本包）
#check @iT_all
#check @iT_exs
#check @iT_and

-- 目标里实际出现的：translateSeq s 与 setShift s 的关系
example (s : V) (y : V) : (y ∈ translateSeq (setShift ℒₒᵣ s)) ↔
    ∃ x ∈ s, y = iT (0 : V) (shift ℒₒᵣ x) := by
  simp only [mem_translateSeq_iff, mem_setShift_iff]
  constructor
  · rintro ⟨x, ⟨x', hx', rfl⟩, rfl⟩
    exact ⟨x', hx', rfl⟩
  · rintro ⟨x', hx', rfl⟩
    exact ⟨_, ⟨x', hx', rfl⟩, rfl⟩

end GodelQ.ProbeHAll
