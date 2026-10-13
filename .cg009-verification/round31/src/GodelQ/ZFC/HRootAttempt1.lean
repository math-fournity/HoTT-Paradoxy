-- CG-009: 尝试 hRoot_uncond（= axmBridge 本身）。
--
-- HRoot.lean 的 docstring 给出 5 步路线，其中 1–4 标"proven or available"，
-- 只有第 5 步标为"pure API plumbing"（Provable.{u,0} vs Provable.{0,_}
-- 宇宙不匹配 + Sentence/Semiproposition 强制转换）。但 provable_iff_provable
-- 这个模式在 NeverRE / ShRE / TranslateRE / Z0Full 已四处跑通。
-- 本文件实地检验第 5 步到底是不是障碍。
import GodelQ.ZFC.HRoot

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.Translate

namespace GodelQ.HRootAttempt1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 第 5 步的实地检验：provable_iff_provable 能否跨宇宙用？

`Provable` 的定义来自 `Bootstrapping.ProvabilityAbstraction`，
`provable_iff_provable` 把元层的 `T ⊢ φ` 与 V 里的 `Provable T ⌜φ⌝` 联系起来。
先只做最小探针：确认这个 iff 在当前 variable 下的确切类型。 -/

-- 探针 A：provable_iff_provable 的类型
#check @provable_iff_provable

-- 探针 B：Padding 相关的可证性引理是否存在
#check @Entailment.padding_iff

end GodelQ.HRootAttempt1
