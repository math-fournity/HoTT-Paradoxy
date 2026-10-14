import GodelQ.ZFC.ShCraigElimSetupQ
/-!
裁决探针 13（**不是收据**）：`axm` 支第 ii 步的精确义务——ℕ 层的 Craig 码与 V 层的 `Δ₁Class` 之间到底是什么关系。

## 背景

`hRoot`（`axm` 支）的义务是
```
RootKey : ∀ p, p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)
```
而 `hAxm_quoted`（003-Step 已证）只处理**引号化**的 `⌜σ⌝`。要接上一般情形，需要一条
"V 层成员 → 引号化成员"的桥。Master 派工把这条桥钉成精确义务陈述（不要证明）。

## Foundation 给的两侧（我已逐条读源码）

**(A) ℕ 层的 Craig 码**（`CraigTrick.lean:270-275` `mem_craig_codes_iff`）：
```lean
n ∈ Encodable.encode '' T.craig ↔
  ∃ s < n, ∃ m < n, (decode₂ (Sentence L) m).isSome ∧
    n = Nat.pair 4 (Nat.pair m (encode (Semiformula.weight s : Sentence L))) + 1 ∧
    ℕ ⊧/![s, m] T.reWitness.val
```
**变量 `s : ℕ`**（有界 `< n`），是 `Semiformula.weight s` 的**层数**。

**(B) V 层的 Δ₁ 类**（`Theory.lean:64`）：
```lean
def Δ₁Class (T : Theory L) [T.Δ₁] : Set V := { φ | V ⊧/![φ] T.Δ₁ch.val }
```
而 `Sh.craig` 的 `Δ₁ch = Sh.craigCh`（`CraigTrick.lean:311`，`T := Sh`），
`craigCh` 的 body 引用 `Sh.reWitness`。展开成 `IsCraigAxiom`：
**变量 `s : V`**（无界），与 `p' : V` 一起满足 `x = p' ^⋏ qqVerums s`。

**⟹ Master 说的"两个 `s` 不是一个变量"确有 Foundation 出处**：(A) 的 `s` 是 ℕ（层数、有界），
(B) 的 `s` 是 V（`qqVerums` 的长度参数、无界）。二者靠 `quote_weight`/`quote_padding`
（`CraigTrick.lean:174-190`）在**引号化**时对上：`⌜Semiformula.weight s⌝ = qqVerums (s : V)`。

## 本探针要钉的三条（只 `#check` + 显式 `example`，不断言主义务可证）

1. **已证方向**：`(⌜σ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ σ ∈ Sh.craig`（`Δ₁Class.mem_iff`，本线探针 3 已 exit 0）。
2. **一般方向（这就是义务）**：任给 `x : V` 与 `x ∈ Sh.craig.Δ₁Class`，
   能否得到某个 `σ` 使 `x = ⌜σ⌝`？——**V 非标准，`x` 可能是非标准码，这一步是真墙**。
3. **引号化时的形状对齐**：`⌜σ.padding s⌝ = ⌜σ⌝ ^⋏ qqVerums (s : V)`（Foundation `Sentence.quote_padding`）。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ

namespace GodelQ.ProbeAxmObligation

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- (1) 已证方向：引号化成员 ↔ 理论成员
#check @Δ₁Class.mem_iff

example (σ : Sentence ℒₒᵣ) : ((⌜σ⌝ : V) ∈ Sh.craig.Δ₁Class) ↔ (σ ∈ Sh.craig) :=
  Δ₁Class.mem_iff

-- (2) 一般方向：V 层任意成员 → 它是某个 σ 的引号？
-- 这就是 RootKey 从"引号化版"到"一般版"要的桥。**未证**。
-- (2) 一般方向：V 层任意成员 → 它是某个 σ 的引号？**这就是义务本身，未证。**
-- 下面这条故意**留空目标**（用 `True` 承载），只为了记录义务的形状不进编译错误。
example (x : V) (hx : x ∈ Sh.craig.Δ₁Class) : True := trivial

-- 义务的精确陈述（供人读，不作为 Lean 目标）：
--   OBLIGATION : ∀ x, x ∈ Sh.craig.Δ₁Class → ∃ σ : Sentence ℒₒᵣ, x = ⌜σ⌝
-- V 非标准时 x 可能是非标准码，这一步是 RootKey 从引号化版到一般版的墙。

-- (3) 引号化时的形状对齐（Foundation 现成）
#check @Sentence.quote_padding
#check @quote_padding
#check @quote_weight

-- (4) RootKey 的精确形状（生产包已有 def）
#check @GodelQ.ShCraigElimSetupQ.RootKey

-- (5) ℕ 层 Craig 码的成员关系（Foundation 现成）
#check @FFL.FirstOrder.Theory.mem_craig_codes_iff
#check @FFL.FirstOrder.Theory.primrecPred_craig_codes

end GodelQ.ProbeAxmObligation
