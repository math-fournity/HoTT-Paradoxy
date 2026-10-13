import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★★ 语义路线的**枢纽**：动机不可定义 + **类型障碍**（2026-10-13，本线）

### 背景

语义路线（本线 2026-10-13 提出）要把 `Provable 𝗭𝗙𝗖 φ` 对**具体 V 层码** `φ` 喂给
`SetTheory.complete` / `tprovable_tquote_iff_provable_quote_sentence`。
那两条零件都要求 `φ = ⌜σ⌝`（`σ : Sentence`，**Lean 对象**）。
故整条路线压在一条**反向引理**上：

```
IsSemiformula L n p → ∃ φ : Semiproposition L n, p = ⌜φ⌝
```

Foundation 只有**正向**（`Semiformula.quote_isSemiformula`），反向不存在。

### 本探针的机器判定（两条，均为**负面**）

**判定 A**：`definability` 在动机上**失败**（`aesop failed`，exit 1）：

```
example : 𝚺ᴬ₁-Predicate fun p : V ↦ ∃ φ : Semiproposition ℒₛₑₜ 0, p = (⌜φ⌝ : V)
```

**判定 B**：换成 `Sentence ℒₛₑₜ`（`ξ = Empty`）**同样失败**（exit 1）。

### ★ 根因：不是「不够聪明」，是**类型障碍**

`IsSemiformula.pi1_structural_induction` / `sigma1_structural_induction` 的动机是

```
{P : V → V → Prop} (hP : 𝚷ᴬ₁-Relation P) … : IsSemiformula L n p → P n p
```

——**`P` 的第一分量是 `n : V`**。而 `Semiproposition L k` 要 **`k : ℕ`**。
故「`p` 是某层 `n` 公式的引号」**根本无法写成 `P n p`**（`n : V` 上写不出 `Semiproposition L n`）。

这不是 definability 技巧问题：**动机在类型上就不可陈述**。
（`Semiproposition L k := Semiformula L ℕ k`，`k : ℕ`；见
`Foundation/FirstOrder/Syntax/Classical/Formula.lean:44`。）

### ⚠ 对 `W8-quote-is-code-20261013` 的更正（**该探针结论过强**）

它写「**卡点不存在**」「语义路线的组装障碍因此**解除**」——**过强**。它实际只核验了：

* ✅ **引号与构造子交换**（`rfl`）：`⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝`、`⌜⊤⌝ = ^⊤`；
* ❌ **未核**：`IsSemiformula` 的每个元素**都是**某个 `Semiproposition` 的引号
  （即引号的**满射性**）。

前者是「引号是好的」，后者是「码都能倒回引号」——**两件事**。
`imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p))` 这种码要喂给零件，
**必须**先有后者。故**枢纽仍在**，不是可绕的旁支。

### 事实清单（本探针已核）

* `IsSemiformula.induction` / `Semiformula.induction`：**不存在**
  ——`Formula/Basic.lean:466-528` 是**整块注释掉的**，`#check` 报 `unknown constant`；
  可用的是 `sigma1_structural_induction`（:1484）与 `pi1_structural_induction`（:1516）。
* 正向 `Semiformula.quote_isSemiformula` 存在（层参数是 `ℕ`）。
* `ℒₛₑₜ.Func := fun _ ↦ Empty`——集合论语言**无函数符号**
  （`Foundation/FirstOrder/SetTheory/Basic/Misc.lean:24`）。

### 给下游的两条路

1. **改陈述**：不用 `P n p`，改成对**具体 `m : ℕ`** 逐层证
   （`IsSemiformula L ↑m p → ∃ φ : Semiproposition L m, p = ⌜φ⌝`），
   再用**码的结构递归**——但 `and`/`or` 同层递归，对 `m` 的强归纳不够
   （须对码本身递归，而码可以是非标准元）；
2. **绕枢纽**：不经 `complete`，直接用 `Derivable` 规则构造
   （回到语法路线，见 `W8-ExsBridge2-corrected` 的 `ExsBridge2`，
   那条归约**已完整**，只剩 `ExsBridge2` 一条义务）。

**本探针只做判定，不声称枢纽为假。** -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeHubQuote
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ── 事实 1：`IsSemiformula.induction` 不存在（整块被注释掉）────────
-- #check @IsSemiformula.induction        -- error: unknown constant
-- #check @Semiformula.induction          -- error: unknown constant
#check @IsSemiformula.sigma1_structural_induction
#check @IsSemiformula.pi1_structural_induction

-- ── 事实 2：正向（引号 ⇒ IsSemiformula）存在 ────────────────────
#check @Semiformula.quote_isSemiformula

-- ── 事实 3：引号与构造子交换（`rfl`）——注意这只是**一半** ───────
example (φ ψ : Semiproposition ℒₛₑₜ 0) :
    (⌜φ ⋏ ψ⌝ : V) = (⌜φ⌝ : V) ^⋏ (⌜ψ⌝ : V) := rfl

-- ── 判定 A：Semiproposition 版动机不可定义（**exit 1**）─────────
example : 𝚺ᴬ₁-Predicate fun p : V ↦
    ∃ φ : Semiproposition ℒₛₑₜ 0, p = (⌜φ⌝ : V) := by
  definability

-- ── 判定 B：Sentence 版（ξ = Empty）同样不可定义（**exit 1**）────
example : 𝚺ᴬ₁-Predicate fun p : V ↦
    ∃ φ : Sentence ℒₛₑₜ, p = (⌜φ⌝ : V) := by
  definability

end GodelQ.ProbeHubQuote
