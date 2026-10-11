import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（六）：`iT` 与 `neg` 的相容律（引号化版本）

`induction1` 的 `hAxL`、`hCut` 两支需要

```
iT 0 (neg p) = neg ℒₛₑₜ (iT 0 p)
```

其中 `p` 是 **V 内的任意公式码**。本文件给出**引号化版本**（`p = ⌜φ⌝`，
`φ` 是元层标准公式），并说明为什么一般版本需要新的工作。

## 引号化版本为什么不够

`induction1` 的支拿到的是 V 内的公式码，可能对应**非标准**公式；
`iT_quote` 只对 `⌜φ⌝`（φ 标准）给出 `iT` 与 `translate` 的一致性，
所以引号化版本不能直接用在支里。这与本 repo 反复出现的
"元层 vs V 内部"分界线是同一处。

## 一般版本：结构分析已经完成，但归纳原理不够用（本机实测）

### 逐例分析：结论是对的

`neg`（`Bootstrapping.neg`，即 `Negation.construction.result L 0 p`）
与 `iT` 是**两个结构同构的递归**：

| 构造子 | `neg` 的支 | `iT` 的支 | 相容性 |
|---|---|---|---|
| `rel k R v` | `^nrel k R v` | `iTR n k R v` | `iT n (^nrel …) = neg (iT n (^rel …))` ✓（`iT_nrel`/`iT_rel`） |
| `nrel k R v` | `^rel k R v` | `neg (iTR …)` | 同上 ✓ |
| `⊤` / `⊥` | 互换 | 不动 | ✓（`iT_verum`/`iT_falsum`） |
| `p ⋏ q` | `neg p ⋎ neg q` | `iT p ⋏ iT q` | ✓（De Morgan + 归纳假设） |
| `p ⋎ q` | `neg p ⋏ neg q` | `iT p ⋎ iT q` | ✓ |
| `∀¹ p` | `∃¹ (neg p)` | `∀(dom → iT p)` | ✓（量词对偶 + `dom` 不变） |
| `∃¹ p` | `∀¹ (neg p)` | `∃(dom ⋏ iT p)` | ✓ |

**每一个构造子都对得上。** 所以这条相容律在数学上成立。

### 障碍：归纳原理的谓词不够宽

`iT` 是 `UformulaRec1` 的 `blueprint.result`，其归纳原理
`UformulaRec1.Construction.semiformula_result_induction` 的谓词形如

```lean
P param n p q     -- 其中 q 被固定为 result L c param p
```

**第四个参数只能是 `iT param p` 本身**，不能提及 `neg p` 的递归结果。
而相容律需要同时说 `iT param p` 与 `iT param (neg p)` 两件事，
所以不能直接套这个原理。`UformulaRec1.Construction` 下**没有**更宽的归纳原理
（本机 `#check` 确认只有 `semiformula_result_induction` 一个）。

### 两条可行路线

1. **在元层归纳，用 `Semiformula.rec'`**：先证引号化版本（本文件的
   `iT_quote_neg` 已完成），再用 `Semiformula.rec'` 沿标准公式结构推广。
   问题是 `induction1` 的支拿到的是 V 内任意码，不是 `⌜φ⌝`。
2. **加强谓词，一次跟踪两条链**：把 `P` 取成
   `fun param n p q => q = iT param p ∧ iT param (neg ℒₒᵣ p) = neg ℒₛₑₜ q`，
   但第四个参数被原理固定，需要在 `all`/`exs` 支里把
   `neg` 的递归调用也纳入——这要求原理允许 `P` 提及 `neg p` 的 `result`，
   而当前原理不允许。**需要自定义一条同步归纳**，工作量与
   `isSemiformula_iT` 同量级（后者用同一个原理，9 个支）。

**结论**：这条相容律不是"读一读就能补上"的，需要一条**新的同步归纳原理**
或对 `UformulaRec1` 机制的扩展。它同时阻塞 `hAxL`、`hCut`、`hShift` 三支。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ShCraigElimNeg

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **引号化版本的 `iT`/`neg` 相容律**：对元层标准公式 `φ` 成立。

`iT_quote` 把两边都送到 `arithTrln.translate` 的引号，
`LogicalConnective.Hom.map_neg'` 给出 `translate` 与 `neg` 的交换。 -/
lemma iT_quote_neg {n : ℕ} (φ : Semisentence ℒₒᵣ n) :
    iT (n : V) (⌜∼φ⌝ : V) = neg ℒₛₑₜ (iT (n : V) (⌜φ⌝ : V)) := by
  rw [iT_quote, iT_quote]
  rw [show neg ℒₛₑₜ (⌜arithTrln.translate φ⌝ : V) =
      (⌜∼(arithTrln.translate φ)⌝ : V) from (quote_neg' _).symm]
  congr 1
  exact LogicalConnective.Hom.map_neg' arithTrln.translate φ

end GodelQ.ShCraigElimNeg

#print axioms GodelQ.ShCraigElimNeg.iT_quote_neg
