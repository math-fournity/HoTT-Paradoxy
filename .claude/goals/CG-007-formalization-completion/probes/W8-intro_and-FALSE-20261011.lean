import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat GodelQ.ShCraigElimBranches

set_option maxHeartbeats 800000

namespace GodelQ.ProbeBM
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 关键认识：h : Derivable (insert p (insert q s))
-- 用 Derivable.and (s := insert (p⋏q) s) 需要
--   Derivable (insert p (insert (p⋏q) s))   ← 从 h 弱化需要 insert p (insert q s) ⊆ 它
-- 但 insert p (insert q s) ⊄ insert p (insert (p⋏q) s)（y = q 不在右边）！
--
-- **wk 的方向根本不对**。正确做法：
-- h 给的是「p 与 q 都在 sequent 里」。
-- 要得 Derivable (insert p (insert (p⋏q) s))：
--   从 h 出发，把 q 换成 p⋏q —— 这需要 **q 蕴含 p⋏q**，而 q 单独推不出 p⋏q。
--
-- 所以「用 Derivable.and」这条路也是错的！
-- 正确的路：h 的 sequent 含 p 与 q，用 andIntro 规则需要 sequent 含 p⋏q。
-- 在 sequent 演算里，「含 p 与含 q ⟹ 含 p⋏q」是 **∧R**，需要两条子推导。
--
-- 即：Derivable (insert (p⋏q) s) 需要
--   Derivable (insert p (insert (p⋏q) s))  与  Derivable (insert q (insert (p⋏q) s))
-- 而这两个**不能**从 h 弱化得到（h 的 sequent 不含 p⋏q）。
--
-- 实际上 h : insert p (insert q s)，而 insert p (insert (p⋏q) s) 更大吗？
-- 元素集：{p, q} ∪ s vs {p, p⋏q} ∪ s。**不是包含关系**！
-- 所以 wk 不行，Derivable.and 也不行。
--
-- **正确的证法**：用 **cut**。
-- 目标 Derivable (insert (p⋏q) s)
-- cut p：需要 Derivable (insert p (insert (p⋏q) s)) 与 Derivable (insert (neg p) (insert (p⋏q) s))
--   第一条：含 p，从 h 弱化？h 的 sequent 是 {p,q}∪s，目标是 {p,p⋏q}∪s。
--   两者都有 p，但目标多了 p⋏q、少了 q。**仍然不是包含关系**。
--
-- 结论：intro_and 在 sequent 演算里**不能从 insert p (insert q s) 推出**！
-- 因为 sequent 语义是「析取」，而 {p, q} 与 {p, p⋏q} 的析取不等价。
-- 实际上：¬p ∨ ¬q ∨ ⋁¬s vs ¬p ∨ ¬(p⋏q) ∨ ⋁¬s = ¬p ∨ ¬p ∨ ¬q ∨ ⋁¬s
-- 后者更强（多了 ¬p）。
-- 所以 **intro_and 是假命题**（除非 p 有额外性质）。

end GodelQ.ProbeBM
