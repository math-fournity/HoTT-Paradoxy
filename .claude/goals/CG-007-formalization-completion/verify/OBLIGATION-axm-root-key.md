# `axm` 支（`hRoot`）第 ii 步的精确义务陈述（2026-10-14，本线 CG-007 会话 d58e0c0d）

> **身份**：`OBLIGATION_STATEMENT / NOT_A_PROOF / NOT_A_RECEIPT`。
> 派工来自 Master（"把 ℕ 层 Craig 码与 V 层 `Δ₁Class` 的翻译关系钉成精确的义务陈述，不需要证明"）。
> 本文件**不证明**任何东西；它给出精确的义务、核过的 Foundation 接口、以及成立/不成立的判断依据。
> 探针：`probes/adj/ProbeAxmObligation.lean`（**exit 0、0 error**）。

## 0. 结论先说

**义务成立与否取决于方向。已证方向成立；一般方向是墙。**

| 方向 | 陈述 | 状态 |
|---|---|---|
| **A（已证）** | `(⌜σ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ σ ∈ Sh.craig` | ✅ **Foundation 现成** `Δ₁Class.mem_iff`（本线探针 3 与本次探针均 exit 0） |
| **B（义务 / 墙）** | `∀ x, x ∈ Sh.craig.Δ₁Class → ∃ σ, x = ⌜σ⌝` | ❌ **不成立**（V 非标准时 `x` 可以是非标准码），且这是 `RootKey` 从引号化版到一般版的**唯一缺口** |

**所以 Master 问的"若这条成立，`hAxm_quoted` → `RootKey` 就只差它"——答案是：
A 方向成立且现成，但它只覆盖引号化的 `x`；B 方向不成立，而 `RootKey` 要的正是 B。**
**`hRoot` 的墙比"只差一条引号化桥"更厚。**

## 1. `RootKey` 的精确形状（生产包已有）

`ShCraigElimSetupQ.lean`（`9276-cg007-w8-d3`）把它固化成命名 `def`：
```lean
RootKey : ∀ p, p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)
```
文件自注："**`RootKey` 就是 D3 本身**（`Sh.craig ⪯ Sh` 的内化）——本归约不解决 D3，
只是把义务搬到那一层、形状更小，且与另两条可对接。"

⟹ **`hRoot` 与 `zfcTr_D3_internalize` 是同一件事的两种形状**（与 Master 此前"四条线统一为命题 C"一致）。

## 2. 两条 ℕ 层 / V 层的 Foundation 接口（我逐条读过源码）

### (A) ℕ 层：Craig 码的成员关系

`CraigTrick.lean:270-275`：
```lean
lemma mem_craig_codes_iff (n : ℕ) :
    n ∈ Encodable.encode '' T.craig ↔
      ∃ s < n, ∃ m < n, (decode₂ (Sentence L) m).isSome ∧
        n = Nat.pair 4 (Nat.pair m (encode (Semiformula.weight s : Sentence L))) + 1 ∧
        ℕ ⊧/![s, m] T.reWitness.val
```
**关键**：`s : ℕ`，且**有界 `s < n`**；它是 `Semiformula.weight s` 的**层数**。

配套的可计算性（`:296-307`）：
```lean
lemma primrecPred_reWitness … : PrimrecPred fun a ↦ ℕ ⊧/![s a, m a] T.reWitness.val
lemma primrecPred_craig_codes : PrimrecPred (· ∈ Encodable.encode '' T.craig)
instance : T.craig.Primrec
```

### (B) V 层：`Δ₁Class` 与它的特征式

`Theory.lean:64`：
```lean
def Δ₁Class (T : Theory L) [T.Δ₁] : Set V := { φ : V | V ⊧/![φ] T.Δ₁ch.val }
```
`Sh.craig` 的 `Δ₁ch = Sh.craigCh`（`CraigTrick.lean:311`，实例里 **`T := Sh`**），
`craigCh` 的 body 引用 `Sh.reWitness`（`:210-216`）。展开成 `IsCraigAxiom`（`:207-208`）：
```lean
IsCraigAxiom x := ∃ s p : V, x = p ^⋏ qqVerums s ∧ V ⊧/![s, p] T.reWitness.val
```
**关键**：`s : V`，**无界**；它是 `qqVerums s` 的**长度参数**。

### ⟹ "两个 `s` 不是一个变量"确有 Foundation 出处

| | (A) ℕ 层 `mem_craig_codes_iff` | (B) V 层 `IsCraigAxiom` |
|---|---|---|
| 变量类型 | `s : ℕ` | `s : V` |
| 有界性 | `s < n`（有界） | 无界 |
| 角色 | `Semiformula.weight s` 的**层数** | `qqVerums s` 的**长度** |
| 配对物 | `m : ℕ`（`decode₂ (Sentence L) m`，有界 `< n`） | `p : V`（任意 V 元素） |

**二者在引号化时对上**，靠 Foundation `CraigTrick.lean:174-190`：
```lean
quote_weight (k : ℕ) : (⌜Semiformula.weight k⌝ : V) = qqVerums (k : V)
quote_padding (φ : Proposition L) (k : ℕ) : (⌜φ.padding k⌝ : V) = ⌜φ⌝ ^⋏ qqVerums (k : V)
Sentence.quote_padding (σ : Sentence L) (k : ℕ) : (⌜σ.padding k⌝ : V) = ⌜σ⌝ ^⋏ qqVerums (k : V)
```
即：把 ℕ 的 `k` 用 `(↑k : V)` 送进 `qqVerums`，就得到 V 层的那个 `s`。
**但这一步只在 `k` 是标准自然数时可用**——`↑k` 是 ℕ 到 V 的嵌入，非标准的 V 元素不在其像里。

## 3. 精确的义务陈述

**义务（B）**：
```lean
OBLIGATION_QUOTE_SURJECTIVE :
  ∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] (x : V),
    x ∈ Sh.craig.Δ₁Class → ∃ σ : Sentence ℒₒᵣ, x = ⌜σ⌝
```

**判断：不成立。** 依据（标身份：AI 分析，未证）：

1. `Δ₁Class` 的判定是 `V ⊧/![x] Sh.craigCh.val`，而 `V` 是**任意**满足 `V ⊧* 𝗜𝚺₁` 的结构，
   可以是**非标准**的。Foundation 的 `craigCh` 用**有界量词** `∃ s < x, ∃ p < x, ∃ v < x`
   （`:210-216`），所以 `x ∈ Δ₁Class` 只要求 `x` 足够大以容纳这些见证——
   **不要求 `x` 是标准编码**。
2. 若 `x` 是非标准码，则不存在标准 `σ` 使 `x = ⌜σ⌝`（`⌜·⌝ : Sentence L → V` 的像只含标准码）。
3. 反过来，**在标准模型 ℕ 中这条义务成立**（每个 `n ∈ ℕ` 若是 Craig 码则来自某个 `σ.padding s`，
   由 `mem_craig_codes_iff` 反向给出）——**这正是 `zfcTr_D3_standard`（`Z0Full.lean:108`）
   那种"正对照成立、一般模型不成立"的同一格局**。

**⟹ `hRoot`/`RootKey`/`zfcTr_D3_internalize` 是同一件事，而它的难点就是"非标准码"。**
这与 004-Step 刚机器证出的 `¬ IsTermFVFree ℒₒᵣ 0 ^&0`（`termShift ^&0 = ^&1`）
**同类**——Master 说得准确：**模型层的自由/非标准元素是这类桥的共同敌人**。

## 4. 那么 `hAxm_quoted` → `RootKey` 到底差什么

**差的不是一条引号化桥**（A 方向已现成）。差的是**在 `x` 非标准时怎么继续**。三条候选：

1. **收窄 `RootKey` 到引号化输入**：`RootKeyQuoted : ∀ σ, (⌜σ⌝ : V) ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗼 (iT 0 ⌜σ⌝)`。
   **这一条可能成立且可能足够**——因为 `hRoot` 的归纳支手里的 `p` 来自 `axm s p` 的构造子，
   而 `Derivation Sh.craig d` 的每个 `axm` 用的 `p` 是**推导里实际出现的公式码**。
   **关键问题**：推导编码 `d` 本身是否也可能是非标准的？
   ⟹ **这是最该先查的一条**（见 §5）。
2. **用 ℕ 层的 `mem_craig_codes_iff` 绕道**：把 `x ∈ Δ₁Class` 与"某个标准 `n` 的 Craig 码"
   关联。但 `x : V` 与 `n : ℕ` 之间没有桥梁，除非先有 §3 的义务（循环）。
3. **接受一般义务，攻 D3**：即现状，`RootKey = D3`。

**我的建议：先查第 1 条。** 它是唯一可能**绕开** D3 的选项，而且答案很可能就在
`Derivation` 的定义里（推导是否强制标准长度/标准码）。

## 5. 给 003-Step / 004-Step 的一个具体可查问题

`Derivation Sh.craig d` 的 `d : V` 是否**必然**是标准编码？

- 若**是**（例如 `Derivation` 的构造子强制某种标准性），则 `axm s p` 支里的 `p` 就是标准码，
  §4 第 1 条成立，**`hRoot` 可能不必攻 D3**——那会是重大收窄。
- 若**否**（`d` 可以非标准），则 §4 第 1 条不成立，`hRoot = D3` 的现状判断确认。

**这条查询很便宜**（读 `Derivation` 的定义与 `induction1` 的构造子即可），
但**判别力很高**：它决定 `hRoot` 是"还要攻 D3"还是"可能已经足够"。
**我建议把它列为 `hRoot` 方向的第一个动作**，在任何人去攻 D3 之前。

### §5 的答案（同日已查，结论：**选项 1 关闭**）

我读了 Foundation 的定义，答案是**否**——`d` 不必然标准，`p` 更是显式的任意 V 元素：

```lean
-- Proof/Basic.lean:533
def Derivation : V → Prop := (construction T).Fixpoint ![]
-- :535
def DerivationOf (d s : V) : Prop := fstIdx d = s ∧ Derivation T d
```

`Derivation` 是 `Fixpoint`——**无界归纳定义**，在 𝗜𝚺₁ 里由 `derivation`（`:543`，
`𝚫ᴬ₁.Semisentence 1`，来自 `fixpointDefΔ₁`）刻画。无界 Fixpoint **允许非标准元素**
（"有限但非标准长度的推导"在 𝗜𝚺₁ 的非标准模型里存在）。所以 `d` 可以非标准。

更直接的是 `induction1` 的 `hRoot`（`Proof/Basic.lean:664`）：
```lean
(hRoot : ∀ s, IsFormulaSet L s → ∀ p, p ∈ s → p ∈ T.Δ₁Class → P (axm s p))
```
**`p` 是量词任取的 `V` 元素**，唯一约束是 `p ∈ T.Δ₁Class`（而 `Δ₁Class` 的判定
`V ⊧/![p] T.Δ₁ch.val` 用有界量词，**不强制 `p` 标准**，见 §3）。
配套的 `Derivation.axm`（`:749-752`）也只要求 `p ∈ T.Δ₁Class`。

⟹ **§4 第 1 条（收窄到引号化输入）不成立。** `hRoot` 支手里的 `p` 就是一般的 `V` 元素，
**必须处理非标准码**。

**于是 `hRoot = D3 = 命题 C` 的现状判断得到确认**，且这次是从 Foundation 定义推出来的，
不是从"攻不动"推出来的。三条候选里第 2 条循环、第 1 条已排除，**只剩第 3 条（攻 D3）**。

这条确认有实际价值：它说明**在 `hRoot` 方向找"绕开 D3 的巧径"是没有希望的**，
该方向的人力应当全部投向 D3 本身（即 `zfcTr_D3_internalize` / `Theory.Δ₁ Sh` 那一族），
不要再去试各种收窄。

## 6. 边界

- 本文件**不证明**任何东西。§3 的"不成立"是我的判断（AI 分析，未证），
  依据是 `⌜·⌝` 的像只含标准码 + `craigCh` 的有界量词不强制标准性。
- 已核过的 Foundation 接口（探针 exit 0 确认可访问且签名如我所述）：
  `Δ₁Class.mem_iff`、`Sentence.quote_padding`、`quote_padding`、`quote_weight`、`RootKey`（def）、
  `FFL.FirstOrder.Theory.mem_craig_codes_iff`、`FFL.FirstOrder.Theory.primrecPred_craig_codes`。
- 未核：`hAxm_quoted`（003-Step 的件）的精确陈述；`Derivation` 是否强制标准码（§5，留给下一动）。
- 本文件不涉及 `hExs`（那是 `substs1 t` 任意闭项，001-Step 在做）。
