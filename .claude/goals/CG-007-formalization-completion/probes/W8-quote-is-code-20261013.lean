import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 卡点解除：码**就是**引号（`rfl`）（2026-10-13）

上一轮定位的卡点是「零件要求引号形 `⌜σ⌝`，而目标是具体码」。
**这个卡点不存在**——Foundation 的 `quote_and`/`quote_verum` 等是 **`rfl`**：

```
@[simp] lemma quote_and (φ ψ : Semiproposition L n) : (⌜φ ⋏ ψ⌝ : V) = ⌜φ⌝ ^⋏ ⌜ψ⌝ := rfl
@[simp] lemma quote_verum : (⌜(⊤ : Semiproposition L n)⌝ : V) = ^⊤ := rfl
```

即 **V 层的构造子（`^⋏`、`^⊤`、`^∃` …）作用在引号上，结果字面上就是那个引号**。
故「码 = 某 Sentence 的引号」不需要证明，是 `rfl`。

本探针机器核验这一点（exit 0）：

```
@Semiformula.quote_and  (φ ψ : Semiproposition L n) : ⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝
@Semiformula.quote_verum : ⌜⊤⌝ = ^⊤
@Semiformula.quote_all  (φ : Semiproposition L (n+1)) : ⌜∀¹ φ⌝ = ^∀ ⌜φ⌝
@Semiformula.quote_inj_iff : ⌜φ₁⌝ = ⌜φ₂⌝ ↔ φ₁ = φ₂
@Semiformula.quote_isSemiformula (φ : Semiproposition L n) : IsSemiformula L ↑n (⌜φ⌝ : V)
```

**两个 `rfl` 实例直接通过**（`⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝`、`⌜⊤⌝ = ^⊤`）。

**故上一轮定位的卡点不存在**：码与引号是**同一件事**，不是两件需要桥接的东西。
语义路线的组装障碍因此**解除**——剩下的是把 `iT` 的输出识别成引号
（用 `iT_quote` 正向：`iT ↑n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeQuoteIsCode

-- 具体核验：`^∃ (domZero ⋏ iT 1 p)` 形式的码，其分量若都是引号，则整体是引号
#check @Semiformula.quote_and
#check @Semiformula.quote_verum
#check @Semiformula.quote_all
#check @Semiformula.quote_inj_iff

-- 最小实例：`⌜φ ⋏ ψ⌝ = ⌜φ⌝ ^⋏ ⌜ψ⌝` 是 rfl
example (φ ψ : Semiproposition ℒₛₑₜ 0) :
    ((⌜φ ⋏ ψ⌝ : V)) = (⌜φ⌝ : V) ^⋏ (⌜ψ⌝ : V) := rfl

example : ((⌜(⊤ : Semiproposition ℒₛₑₜ 0)⌝ : V)) = (^⊤ : V) := rfl

end ProbeQuoteIsCode