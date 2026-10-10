import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-!
# W8 · 第二层开工探针（临时文件，**不进收据源**）

记录 ← 方向（V 内部语法解释定理）开工时的实测结论。**没有证出任何新命题。**

## 已确认：第一层基本已完成

`arithTrln.translate` 是 `→ˡᶜ`（`LogicalConnective.Hom`），所以 ⊤/⊥/⋏/⋎/∼/🡒 的交换律自动具备
（见本文件 A 节，`rfl`/`simp` 通过）。而**内部化**版本 `iT`（项目自己的 `InternalTranslate.lean`）
已经给出全部公式级计算规则与正确性：

- `iT_rel` / `iT_nrel` / `iT_verum` / `iT_falsum` / `iT_and` / `iT_or` / `iT_all` / `iT_exs`
- `iT_quote : iT (n:V) ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（对每个 `φ : Semisentence ℒₒᵣ n`）

所以第二层要用的"翻译沿公式结构"的地基**已经有了**。

## 已确认：V 内部推导只有 10 条规则

来自 `Bootstrapping/Syntax/Proof/Basic.lean:412` 的 `blueprint`（`Derivation T d := (construction T).Fixpoint ![]`）：

| # | 规则图 | 形状 |
|---|---|---|
| 1 | `axLGraph` | `p ∈ s ∧ ∼p ∈ s` |
| 2 | `verumIntroGraph` | `⊤ ∈ s` |
| 3 | `andIntroGraph` | `⊢ p,s` 与 `⊢ q,s` ⟹ `⊢ p⋏q,s`（当 `p⋏q ∈ s`） |
| 4 | `orIntroGraph` | `⊢ p,q,s` ⟹ `⊢ p⋎q,s`（当 `p⋎q ∈ s`） |
| 5 | `allIntroGraph` | `⊢ free p, setShift s` ⟹ `⊢ s`（当 `^∀p ∈ s`） |
| 6 | `exsIntroGraph` | `⊢ p[t], s` ⟹ `⊢ ^∃p, s`（当 `^∃p ∈ s`，`t` 是项） |
| 7 | `wkRuleGraph` | `⊢ s'` ⟹ `⊢ s`（当 `s' ⊆ s`） |
| 8 | `shiftRuleGraph` | `⊢ s` ⟹ `⊢ s`（当 `setShift s = s`） |
| 9 | `cutRuleGraph` | `⊢ p,s` 与 `⊢ ∼p,s` ⟹ `⊢ s` |
| 10 | `axmGraph` | `p ∈ s ∧ p ∈ T`（理论公理） |

**结论：可以按 `Derivation Sh.craig` 的归纳做，不必显式构造一个"翻译推导"的函数。**
目标写成 `∀ s, Derivable Sh.craig s → Derivable 𝗭𝗙𝗖 (sᵗ)`，逐规则消。

## 已发现的障碍（此前未料到）

**sequent 不是树，是"码的指数和"**：`Sequent.quote Γ = ∑ φ ∈ Γ, Exp.exp ⌜φ⌝`
（`Syntax/Proof/Coding.lean:24`），`bitSubsetDef` 也印证了这是位集表示。
所以"把 sequent 里每个公式换成它的翻译"**不是**一个逐点操作，需要一个对 `s`（一个自然数）
做**强递归**的 V 可定义映射 `s ↦ sᵗ`，并证明它满足
`bitTest sᵗ ⌜φᵗ⌝ ↔ bitTest s ⌜φ⌝`（以及单元素情形 `{φ}ᵗ = {φᵗ}`，后者可计算）。

这是第二层的**第一个必做子任务**，也是 `axm`/`wk`/`shift`/`cut` 各支都要用到的公共前置。

**`axm` 支是唯一用到 𝗭𝗙𝗖 的地方**：`p` 是 `Sh.craig` 公理 ⟹ 由 `mem_craig_codes_iff` 得
`p = ρ.padding k` 且 `reWitness(k, ⌜ρ⌝)`；由 `reWitness_spec` + `Sh.reCh` 的语义得 `zfcTr ρ`，
即 V 手里**已有** `ρᵗ` 的一条 𝗭𝗙𝗖 推导；再用 `ρ.padding k = ρ ⋏ ⊤^k` 把它接回来。
（注意 `Sh.reCh.val` 展开为 `mkSigma (codeOfREPred (Encodable.encode '' Sh))`，与 `trProv` 只是
内容相同、不是同一公式，所以这里还要一条"`codeOfREPred` 的一般 V 表示引理"。）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCArith

namespace W8TranslateProbe

/-! ## A. 第一层：`translate` 的逻辑交换律（已有） -/

example {ξ : Type*} {n : ℕ} (φ ψ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (φ ⋏ ψ) = arithTrln.translate φ ⋏ arithTrln.translate ψ := rfl

example {ξ : Type*} {n : ℕ} (φ ψ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (φ ⋎ ψ) = arithTrln.translate φ ⋎ arithTrln.translate ψ := rfl

example {ξ : Type*} {n : ℕ} (φ : Semiformula ℒₒᵣ ξ n) :
    arithTrln.translate (∼φ) = ∼arithTrln.translate φ := by simp

/-! ## B. 第二层要用的 10 条规则图（名字核对） -/

#check @axLGraph
#check @verumIntroGraph
#check @andIntroGraph
#check @orIntroGraph
#check @allIntroGraph
#check @exsIntroGraph
#check @wkRuleGraph
#check @shiftRuleGraph
#check @cutRuleGraph
#check @axmGraph

/-! ## C. sequent 表示与"位测试"接口 -/

#check @insert
#check @insertDef
#check @bitSubsetDef
#check @fstIdx
#check @fstIdxDef
#check @setShift
#check @free

/-! ## D. 归纳入口（fixpoint 的归纳原理） -/

#check @Derivation
#check @Derivable
#check @derivation
#check @Fixpoint.Construction.Fixpoint
#check @Fixpoint.Construction.induction

end W8TranslateProbe
