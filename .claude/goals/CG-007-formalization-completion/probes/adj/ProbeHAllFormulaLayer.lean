import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 8（**不是收据**）：`hAll` 的公式层能否直接用 ℒₛₜ 侧的 `Derivable.all_m`。

## 义务

IH：`Derivable 𝗭𝗙𝗖 (insert (iT 0 (free ℒₒᵣ p)) (translateSeq (setShift ℒₒᵣ s)))`
目标：`Derivable 𝗭𝗙𝗘 (translateSeq s)`，其中 `^∀ p ∈ s`。

## 想法

Foundation 的 `Derivable.all_m`（`Proof/Basic.lean:803`）：
```lean
lemma all_m {s p : V} (h : ^∀ p ∈ s)
    (hp : Derivable T (insert (free L p) (setShift L s))) : Derivable T s
```

若把它用在 `L := ℒₛₜ`、`s := translateSeq s`、`p := iT 1 p`（注意层 1→1），则要
  (h)  `^∀ (iT 1 p) ∈ translateSeq s`；
  (hp) `Derivable 𝗭𝗙𝗼 (insert (free ℒₛₜ (iT 1 p)) (setShift ℒₛₜ (translateSeq s)))`。

- (h) 由 `^∀ p ∈ s` 与 `iT_all`：`iT 0 (^∀ p) = ^∀ imp domZero (iT 1 p)`。**注意多一个 `imp domZero`**！
  所以 `^∀ (iT 1 p)` **不是** `iT 0 (^∀ p)`——差一个定义域限制。这是核心难点。
- (hp) 的 `free ℒₛₜ (iT 1 p)` 对不上 IH 的 `iT 0 (free ℒₒᵣ p)`。

本探针逐条核这三件的**形状**，确认难点在哪。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeHAll2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ℒₛₜ 侧的 ∀ 引言（现成）
#check @Derivable.all_m
#check @Derivable.all

-- 翻译后的 ^∀ 形状（本包 iT_all：升一层 + 定义域限制）
#check @iT_all

-- 难点 1：`iT 0 (^∀ p)` 的形状是 `^∀ imp ℒₛₜ domZero (iT 1 p)`（iT_all 直接给）
example (p : V) (hp : IsUFormula ℒₒᵣ p) : iT (0 : V) (^∀ p) = iT (0 : V) (^∀ p) :=
  rfl

-- 难点 2：free 的两侧
#check @free

-- 那么 all_m 的 h 需要 `^∀ (iT 1 p) ∈ translateSeq s`；
-- 而我们有的是 `^∀ imp domZero (iT 1 p) ∈ translateSeq s`。
-- 若 ℒₛₜ 侧能证「在 domZero 内取元素」给出 imp domZero (iT 1 p) 到 iT 1 p 的推论，
-- 那么 h 可由 wk + 一条 𝗭𝗙𝗖 定理给出。
-- 本探针记录这条通道，不断言可行。

end GodelQ.ProbeHAll2
