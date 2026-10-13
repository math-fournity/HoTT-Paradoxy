import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★★ 语义路线的**枢纽实测：动机不可定义**（2026-10-13）

### 背景

我（本线）提出的语义路线，其组装枢纽是这条**反向引理**：

```
IsSemiformula L n p → ∃ φ : Semiproposition L n, p = ⌜φ⌝
```

（Foundation 只有正向 `Semiformula.quote_isSemiformula`，反向不存在。）

两个未跟踪探针 `W8-IsFormula-to-quote` / `W8-reverse-quote` 都带 `sorry` 停在它上面。

### 本探针的机器判定（**负面**）

`definability` **失败**——且两种写法都失败：

* `∃ φ : Semiproposition ℒₛₑₜ 0, p = ⌜φ⌝` → `aesop failed`
* `∃ φ : Sentence ℒₛₑₜ, p = ⌜φ⌝`（ξ = Empty）→ `aesop failed`

（两条 `example` 见下，均 exit 1、错误为 `Tactic aesop failed`。）

### 为什么这不等于「引理为假」

`definability` 只说明**找不到 Σ1 定义**，不说明命题不成立。根因是**动机的形状**：

* `∃ φ : Sentence L` 量化的是 **Lean 类型**（`Semiformula L Empty 0`），
  不是 V 元素——V 层看不见它；
* 层参数在引号引理里是 **`ℕ`**（`quote_isSemiformula : ∀ {n : ℕ} (φ : Semiproposition L n), …`），
  而 `IsSemiformula` 的层是 **`V`**——两者不同型。

要证它得走 `IsSemiformula.sigma1_structural_induction` / `pi1_structural_induction`
（**注意**：`IsSemiformula.induction` 在 `Formula/Basic.lean:466-528` 是**整块注释掉的**，
`#check` 报 `unknown constant`），且 `hP` 必须**手工给**。

### 对语义路线的影响（**重要更正**）

`W8-quote-is-code-20261013.lean` 的结论「码与引号是同一件事，**卡点不存在**」
**过强**，应更正为：

* ✅ **已核**：`quote_and`/`quote_verum`/`quote_all` 等是 `rfl`
  —— 即**引号与构造子交换**：`⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝`；
* ❌ **未核**：`IsSemiformula` 的**每个**元素都是某个 `Semiproposition` 的引号。
  这正是枢纽，而它的动机**不可定义**。

`tprovable_tquote_iff_provable_quote_sentence` 要求 `⌜σ⌝` 形；
要把 `imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p))` 喂给它，
**必须**先说明该码是引号（分量各是引号，再由 `quote_imp` 拼）。
故**枢纽仍是语义路线的必经之路**，不是可绕的旁支。

### 给下游的两条路

1. **证枢纽**（手工给 `hP` 走 `pi1_structural_induction`）——
   谓词须改写成 V 可表达的形态（不能量化 Lean 类型）；
2. **绕枢纽**：不经 `SetTheory.complete`，直接用 `Derivable` 规则构造
   （即回到语法路线，见 `W8-ExsBridge2-corrected` 的 `ExsBridge2`，
   那条归约**已完整**，只剩 `ExsBridge2` 一条义务）。

**本探针只做判定，不声称引理为假。** -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeHubQuote
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ── 事实 1：`IsSemiformula.induction` 不存在（被注释掉）──────────
-- #check @IsSemiformula.induction          -- error: unknown constant
-- #check @Semiformula.induction            -- error: unknown constant
-- 存在的是：
#check @IsSemiformula.sigma1_structural_induction
#check @IsSemiformula.pi1_structural_induction

-- ── 事实 2：正向（引号 ⇒ IsSemiformula）存在 ──────────────────
#check @Semiformula.quote_isSemiformula

-- ── 事实 3：引号与构造子交换（`rfl`）──────────────────────────
example (φ ψ : Semiproposition ℒₛₑₜ 0) :
    (⌜φ ⋏ ψ⌝ : V) = (⌜φ⌝ : V) ^⋏ (⌜ψ⌝ : V) := rfl

-- ── 判定 A：Semiproposition 版动机不可定义（**exit 1**）────────
example : 𝚺ᴬ₁-Predicate fun p : V ↦
    ∃ φ : Semiproposition ℒₛₑₜ 0, p = (⌜φ⌝ : V) := by
  definability

-- ── 判定 B：Sentence 版（ξ = Empty）同样不可定义（**exit 1**）───
example : 𝚺ᴬ₁-Predicate fun p : V ↦
    ∃ φ : Sentence ℒₛₑₜ, p = (⌜φ⌝ : V) := by
  definability

end GodelQ.ProbeHubQuote
