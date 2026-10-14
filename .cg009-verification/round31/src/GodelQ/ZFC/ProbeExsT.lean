import GodelQ.ZFC.GateBranches
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.ProbeExsT
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- **探针结论：t 的「闭性」不可达；`termBV` 不记自由变量。**
--
-- 原想问：Craig 推导 d 的 sequent `insert (substs1 t p) s` 是否迫使 t 为闭项。
-- 结论：repo 里**没有**表达这个的谓词。`termBV` 只数绑定变量：
--   `termBV L ^#z = z + 1`（Basic.lean:705）、`termBV L ^&x = 0`（:708）
-- 自由变量对它完全不可见。`IsSemiterm.fvar (n x) : IsSemiterm L n ^&x` 无条件成立（:810），
-- 故 `IsTerm ℒₒᵣ t`（= `IsSemiterm ℒₒᵣ 0 t`，:773）允许 t = ^&x。
--
-- 附带障碍：`NumeralSemantics.eval_numeralF_iff` 要 `[SetStructure V] [V↓[ℒₛₑᵧ] ⊧* 𝗭]`，
-- 而 ExsBridge2 在 `[ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`——两套假设不可比。
example (s p t : V) (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (d : V)
  (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (substs1 (L := ℒₒᵣ) t p) s)) :
    -- t's free variables are all in ω (or: t is closed)
    True := by
  trivial

end GodelQ.ProbeExsT
