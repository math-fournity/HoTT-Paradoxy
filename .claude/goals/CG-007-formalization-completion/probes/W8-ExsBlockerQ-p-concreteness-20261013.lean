import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 关键核验：`ExsBlockerQ` 里的 `p` 是否总是**具体构造子形**？（2026-10-13）

Master 提醒：若 `p` 是任意 `IsUFormula`，则「分类处理具体情形」**不覆盖全部**，
推广就没有意义。**本探针做这个 10 分钟核验。**

**`ExsBlockerQ` 的签名**（`ShCraigElimSetupQ.lean:101`）：
```
def ExsBlockerQ : Prop :=
  ∀ {s p t dd : V}, IsFormulaSet (L := ℒₒᵣ) s → ^∃ p ∈ (s : V) →
    IsTerm ℒₒᵣ t →
    fstIdx dd = insert (substs1 ℒₒᵣ t p) s →
    Derivation (V := V) (L := ℒₒᵣ) Sh.craig dd →
    Q (V := V) dd → Q (V := V) (exsIntro s p t dd)
```

**`p` 的约束只有 `^∃ p ∈ s`**（`s` 是公式集）——**没有具体形状约束**。

**故答案是：`p` 是任意的**——分类处理**不覆盖全部**。

## 结论（exit 0 核验）

`ExsBlockerQ` 与 `induction1` 的 `hExs` 支**都只给 `^∃ p ∈ s`**，
**没有任何具体形状约束**。`p` 是任意的 `V` 层元素（只要 `^∃ p` 合式）。

**故**：
* 「按 `p` 的具体构造子形分类处理」**不覆盖全部情形**；
* 语义路线（对具体 `p` 有效）**不能单独解决 `ExsBlockerQ`**；
* **一般 `p` 仍需语法路线**——与 Master 的边界判断一致。

**但这不是说语义路线无用**：它证明了「`complete` + 模型论证」这条链可用，
且对**具体的** `ExsBridge2` 实例（若未来出现）有效。
`ExsBridge2` 的一般情形仍须语法路线。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeExsBConcrete

-- 核验 `ExsBlockerQ` 的精确签名
#check @GodelQ.ShCraigElimSetupQ.ExsBlockerQ

-- 核验 `p` 的约束来源：`^∃ p ∈ s` 只经 `IsFormulaSet`
#check @IsFormulaSet

-- 对照 `induction1` 的 `hExs` 支：同样只有 `^∃ p ∈ s`
#check @Bootstrapping.Derivation.induction1

end ProbeExsBConcrete