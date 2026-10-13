import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★★ 枢纽**为假**：非标准码（2026-10-13，本线）

上一探针（`W8-hub-quote-motive-NOT-definable`）报「动机不可定义」。
本探针给出**更强的判定：命题本身为假**（对任意 `V`）。

### 命题

```
IsSemiformula L n p → ∃ F : Semiproposition L n, p = ⌜F⌝
```

### 为什么为假

三条源码事实：

1. **`IsSemiformula` 是 Fixpoint**（`Formula/Basic.lean:284`）：
   `def IsUFormula : V → Prop := (FormalizedFormula.construction L).Fixpoint ![]`，
   而 `Fixpoint v x := ∃ s, x ∈ c.limSeq v s`（`HFS/Fixpoint.lean:205`）。
2. **`limSeq` 的迭代指标是 `V`**（`HFS/Fixpoint.lean:131`）：
   `def limSeq (s : V) : V := c.prConstruction.result v s` —— **`s : V`，不是 `ℕ`**。
   故在非标准模型里 `s` 可以**非标准**，`IsSemiformula` 因此含**非标准层高的公式码**。
3. **`⌜F⌝`（`F : Semiproposition L n`，Lean 对象）永远是标准码**：
   Lean 对象由**有限多**个构造子搭成，其码是标准自然数。

⟹ 取非标准模型中的非标准公式码 `p`：`IsSemiformula L 0 p` 成立，
但**不存在** Lean 对象 `F` 使 `p = ⌜F⌝`。**命题为假。**

### 与同行发现的关系

* **同行**（commit `00de1fa1`）发现 Foundation 在 **ℕ 层**有
  `IsSemiformula.sound {n φ : ℕ} : IsSemiformula L n φ → ∃ F, ⌜F⌝ = φ`
  （`Formula/Coding.lean:478`）。**ℕ 上没有非标准元**，故 ℕ 层为真、V 层为假——
  这不是「搬不过来」，是**真值不同**。
* 这解释了同行遇到的「V 层没有 `Nat.strongRec`」：**不是缺工具，是没有真命题可证**。

### 对语义路线的影响（**决定性**）

语义路线（本线 2026-10-13 提出）的组装**必须**把 V 层具体码识别成 `⌜σ⌝`。
本探针说明**这一步在非标准模型里根本不可能**——故**语义路线按原形状不可行**，
不是「难」，是**目标为假**。

**出路**（都不经 `complete`）：
1. 语法路线：直接用 `Derivable` 规则构造
   （`W8-ExsBridge2-corrected` 的 `ExsBridge2`，归约**已完整**，只剩它一条义务）；
2. 若仍要语义，须**加强假设**：只用**标准**码（但 `ExsBlockerQ` 里的 `p`
   来自 `IsFormulaSet`，在非标准模型里含非标准元，加强不了）。

### 与舰队判断的交叉印证

002-Flash 把 C 靶心窄到「**非标准码**」一条——与本探针**同一堵墙**：
非标准公式码既是 C 的障碍，也是语义路线枢纽的**反例来源**。

**本探针只给结构性论证**（未在 Lean 里构造非标准模型——那需要模型论设施）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeHubFalse
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 事实 1：`IsSemiformula` 是 Fixpoint（V 谓词）
#check @IsUFormula
#check @FormalizedFormula.construction

-- 事实 2：`Fixpoint` 的见证 `s` 是 `V`
#check @Fixpoint.Construction.Fixpoint

-- 事实 3：Foundation 的 ℕ 层反向引理（**标准码**，与 V 层不同真值）
#check @IsSemiformula.sound

end GodelQ.ProbeHubFalse
