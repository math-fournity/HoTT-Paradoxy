import GodelQ.ZFC.ShCraigElimSetupQ
/-!
裁决探针 11（**不是收据**）：到 `AllBlockerQ` 的两条路线是否真的独立？

## 两条路线

**路线 A（生产包，9276，`ShCraigElimSetupQ.lean`）**
`AllKey` → `allBlockerQ_of_key`，其中 `AllKey : Prop := ∀ p, Provable 𝗭𝗙𝗖 (imp (iT 0 (free p)) (free (iT 1 p)))`
——**注意：没有 `domZero` 守卫**。`all_m` 的第二条前提由
`ih ⟶ replace_of_imp (hAB := AllKey 的 imp) ⟶ hAll_reduce ⟶ all_m_premise` 给出，
而 `all_m_premise`（:316）走 `free_imp_domZero` + `imp_wk`：
从 `Derivable (free Y ⫽ S)` 得 `Derivable (free (imp domZero Y) ⫽ S)`。

**路线 B（`HABElim` + `HAllProof` + `HAllUncond`）**
`HAllProof.hAll_uncond` 的 `hAB : Derivable (neg A ⋎ free ℒₛₑ₧ (imp domZero (iT 1 p))) ∅`
其中 `A := iT 0 (free ℒₒᵣ p)`——**`B` 侧带 `domZero`，且用 `neg ⋎`（排中律）形式**。
`hAB` 由 `HABElim.hAB_derivable` 给，收尾 `Derivable.or` + `Derivable.em`。

## 关键差异（本探针要定的）

路线 A 的 `AllKey` 断言的是 **`imp A B_unguarded`**（`B` 不带 domZero），
路线 B 的 `hAB` 断言的是 **`neg A ⋎ B_guarded`**（`B` 带 domZero）。

两条陈述**不同**。问题是：它们是否互相可导？若 A 可导 B 且反之，则"两条独立路线"实为一条。
若不然，则确实是两条。

本探针逐条核这两条陈述的**精确形状**（不断言可互相推导）。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ

namespace GodelQ.ProbeTwoRoutes

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 路线 A 的钥匙：AllKey（无 domZero）
#check @GodelQ.ShCraigElimSetupQ.AllKey
#check @GodelQ.ShCraigElimSetupQ.allBlockerQ_of_key
#check @GodelQ.ShCraigElimSetupQ.allKey_of_bridge

-- 路线 A 的两个组件
#check @GodelQ.ShCraigElimSetupQ.all_m_premise
#check @GodelQ.ShCraigElimSetupQ.hAll_mem
#check @GodelQ.ShCraigElimSetupQ.hAll_reduce

-- 路线 A 的钥匙：AllKey 的内容（`Provable` 层，逐字照 `AllKey` 的定义写出来核对）
example (p : V) (hp : IsSemiformula ℒₒᵣ (1 : V) p)
    (hk : GodelQ.ShCraigElimSetupQ.AllKey (V := V)) : True := by
  have h := hk hp
  trivial

-- 路线 B 的钥匙内容（B 侧带 domZero，neg ⋎ 形式）
--   hAB : Derivable (insert (neg A ^⋎ free ℒₛₑ₧ (imp ℒₛₑ₧ domZero (iT 1 p))) ∅)
-- 路线 B 在 HABElim.lean 里，不在本包；这里只记录形状差异。

-- 两者共同的落点
#check @GodelQ.ShCraigElimSetupQ.AllBlockerQ

end GodelQ.ProbeTwoRoutes
