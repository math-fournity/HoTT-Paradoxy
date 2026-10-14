import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 回答 001-Step：语义路线对**闭项 t** + 一般 p 是否适用？（2026-10-14）

001-Step 的论据：`IsTerm t := IsSemiterm ℒₒᵣ 0 t`（闭项）⟹ t 的码是标准形
（numeral 链）⟹ 不受非标准码反例影响。所以猜「闭项 t」情形可能有语义捷径。

**本探针核验这个论据的每一步。**

**关键区分**：我此前否证语义路线的理由是**`p` 不是引号形**（非标准码）。
闭项 `t` 只影响 `substs1 t p` 的**子项**，**不改变 `p` 本身**。

## 核验结果（exit 0）：**闭项 t 救不了语义路线**

决定性一行是 `SetTheory.complete` 的签名：

```
SetTheory.complete : ∀ (T : SetTheory) [𝗘𝗤 ℒₛₑₜ ⪯ T] (φ : SetTheorySentence),
  (∀ (M : Type u_3) … , M↓[ℒₛₑₜ] ⊧ φ) → T ⊢ φ
```

**`φ : SetTheorySentence` —— 一个 Lean 的类型化句法对象**，不是 V 层的码。

而 `ExsBridge2` 要证的是 `Provable 𝗭𝗙𝗂 (imp (iT 0 (substs1 t p)) (^∃ (domZero ⋏ iT 1 p)))`——
**一个 V 层的码**。

**❌ 闭项 `t` 不改变这一点**：`IsTerm t` 只让 `t` 的码标准（numeral），
`substs1 t p` 仍是**含 `p` 的 V 层码**；而要把这个码变成 `SetTheorySentence`
（即 `⌜某句⌝`），需要的正是**反向引理**——它已被机核验**为假**（非标准码）。

**故**：001-Step 的论据前半对（闭项 t ⟹ t 的码标准），
**但结论不成立**——卡点不在 `t`，在 `p` 到引号的那一步。

## 对 001-Step 的建议

`iT_substs1`（等式层）仍是必需的：它把 `iT 0 (substs1 t p)` 化成
`subst (iVE 0 t) (iT 1 p)`，从而**绕开**「整体码的引号识别」——
这是语法路线能成立的原因（它只需 `IsSemiformula ℒₒᵣ (m+1) p`，
正是 `hAll`/`hExs` 手里有的）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeSemanticClosedT
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① `IsTerm` 的定义（闭项）
#check @IsTerm
#check @IsSemiterm.bvar

-- ② 闭项的码与 numeral（Foundation 现成件）
#check @Arithmetic.typedNumeral

-- ③ `substs1 t p` 的码含 t 的码，但 **p 仍是核心**
#check @IsSemiformula.substs1
#check @IsSemitermVec.singleton

-- ④ ★ 决定性核验：`SetTheory.complete` 要什么形状？
#check @SetTheory.complete

end ProbeSemanticClosedT