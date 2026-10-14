import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（七）：`iT`/`neg` 相容律——正确的归纳谓词已找到

`hAxL`、`hCut`、`hShift` 三支需要

```
iT n (neg p) = neg ℒₛₑₜ (iT n p)          -- p 是 V 内任意公式码
```

本文件给出**能用的归纳谓词**，把这条律化归为 `semiformula_result_induction`
的 9 个支（与 `isSemiformula_iT` 同形）。

## 关键：谓词要把 `neg` 的递归结果对上 `iT` 的递归结果

上一轮记下的障碍是"`semiformula_result_induction` 的谓词第四参数被固定为
`result L c param p`，无法提及 `neg p` 的递归结果"。**换个写法就没有这个问题**：

```lean
P param n p q := iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q
```

原理把 `q` 固定成 `iT param p`，于是 `P param n p (result param p)` 展开正是
`iT param (neg p) = neg (iT param p)`——**就是所要的等式**。所以原理够用，
不需要新的同步归纳。（本机 `#check`/elaboration 已确认谓词被接受，
9 个支的归纳假设形状正确。）

## Foundation 已备好 `neg` 的逐构造子展开

| 引理 | 形状 |
|---|---|
| `neg_verum` / `neg_falsum` | `neg ⊤ = ⊥` / `neg ⊥ = ⊤` |
| `neg_rel` / `neg_nrel` | `neg (rel k R v) = nrel k R v` / 反之 |
| `neg_and` / `neg_or` | `neg (p ⋏ q) = neg p ⋎ neg q` / 反之 |
| `neg_all` / `neg_ex` | `neg (∀¹p) = ∃¹ neg p` / 反之 |

配 `iT_rel`/`iT_nrel`/`iT_verum`/`iT_falsum`/`iT_and`/`iT_or`/`iT_all`/`iT_exs`，
每个支都应当能关掉。**剩下的是 9 个支的机械填充。**

## 支的清单（本机已确认形状）

```
rel   : neg_rel + iT_nrel + iT_rel
nrel  : neg_nrel + iT_rel + iT_nrel + 码层面 neg 的对合
verum : neg_verum + iT_falsum + iT_verum + neg_verum（ℒₛₑₜ 侧）
falsum: 对偶
and   : neg_and + iT_or + iT_and + ihp + ihq
or    : neg_or + iT_and + iT_or + ihp + ihq
all   : neg_all + iT_exs + iT_all + ih（层数 +1，需 param 护罩）
exs   : neg_ex + iT_all + iT_exs + ih
```

## 一个真实的子障碍

`nrel` 支需要**码层面的 `neg` 对合律** `neg (neg x) = x`。
Foundation 只有元层的 `Semiformula.neg_neg`，码层面的没有现成引理；
`iTR param k R v` 是 `qqAlls` 的复合，不是 `^rel` 的形式，所以不能直接套 `neg_rel`。
这一条需要单独处理（很可能要沿 `iTR` 的结构或用 `neg` 自身的归纳）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNegGen

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **一般版本的 `iT`/`neg` 相容律的归纳设置**。

谓词 `P param n p q := iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q` 被
`semiformula_result_induction` 接受（本机确认），9 个支的归纳假设形状正确。
本文件**不填**这些支。 -/
theorem iT_neg_induction_setup {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p →
      iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param _n p q => iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q)
      (by definability)
      (by intro n param k R v hR hv; sorry)
      (by intro n param k R v hR hv; sorry)
      (by intro n param; sorry)
      (by intro n param; sorry)
      (by intro n param p q hp hq ihp ihq; sorry)
      (by intro n param p q hp hq ihp ihq; sorry)
      (by intro n param p hp ih; sorry)
      (by intro n param p hp ih; sorry)
  · intro p hp
    simpa [iT] using key hp

end GodelQ.ShCraigElimNegGen
