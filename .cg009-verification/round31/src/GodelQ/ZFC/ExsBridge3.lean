-- ⛔ **撤回：本条等式为假，勿再攻。2026-10-14，001-Step 自查发现 + 001-Flash 独立复核。**
--
-- 假在**类型层**：`subst L w p` 的 `w` 语义上是**项向量**，而 `iVE n t` 的输出
-- 永远是**公式**（`eqAtom` 或 `ve0`/`ve2`）。把公式码当项向量用，结果是乱码。
--
-- 本 repo 已机器证伪同型命题（`ITSubstCounter.navy_law_is_false_shape`，公理干净）：
-- ```lean
-- subst ℒₛₑₜ ?[^&0] (iVE 1 ^&x) = ^rel 2 ↑cEqN [^&0, ^&x]     -- 不是 eqAtom ^&x
-- ```
-- 真因：`eqAtom t = ^rel 2 cEqN [#0, t]` 自己带 bvar 0，`subst` 撞的是它。
--
-- **hExs 的剩余义务是蕴含式（Σ1 范围），不是等式。**
-- 正路：`ExsBridge2`（`iT 0 (p[t]) ⟹ ^∃ (domZero ⋏ iT 1 p)`），
-- 由 001-Step 攻，走 `Derivable.exsIntro` + 见证项，不碰本文件。
--
-- 保留本文件仅为：statement 的机器类型检查记录 + 这一段撤回诊断。
--
-- CG-009: `iT_substs1_term`（已撤回） —— **任意项代换**的 iT 相容律（hExs 支的中间引理）。
--
--      iT 0 (substs1 ℒₒᵣ t p) = subst ℒₛₑₜ (iVE 0 t) (iT 1 p)
--
-- `p` 层 1，`t` 是任意的**项**（不必是闭项，层 0 即可）。
--
-- ## 与本树既有结果的差别（为什么不能直接从 QvecV 推广）
--
-- `substs1 t p = subst ?[t] p`（把 bvar 0 换成**项 t**）；
-- 而 `HABKey.iT_free_eq`（已证）处理的是 `free p = substs1 ^&0 (shift p)`
-- （把 bvar 0 换成**自由变量** `^&0`）。两者代入向量不同，且
-- `iVE` 对项与变量的处理不同：
--   * `iVE n (^#z) = eqAtom ^#(z+1)`  （iVE_bvar）
--   * `iVE n (^&x) = eqAtom ^&x`      （iVE_fvar）
--   * `iVE n (^func k f v) = if k = 0 then ve0 k f else ve2 n k f …`  （iVE_func）
-- 第三支需要 `ve2` 的开口律（`IVEOpenFunc15/16/17` + `IVEOpenFull`，本树已证）。
--
-- ## 归属
--
-- 与 001-Step 分工（2026-10-14）：001-Flash 攻本引理，001-Step 攻见证引理
-- （`subst (iVE 0 t) (iT 1 p) ⟹ ^∃ (domZero ⋏ iT 1 p)`）。
import GodelQ.ZFC.ITSubstOpen9

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFunc15 GodelQ.IVEOpenFunc16
open GodelQ.IVEOpenFunc17 GodelQ.IVEOpenFull

namespace GodelQ.ExsBridge3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 目标（statement 已钉住）

`p` 层 1（`IsSemiformula ℒₒᵣ 1 p`），`t` 层 0（`IsTerm ℒₒᵣ t` 即 `IsTerm ℒₒᵣ 0 t`）。 -/

/-- （撤回段见文件头。）真值探针：取 `t := ^&0`。此时
`substs1 ^&0 p = subst ?[^&0] p`（自由变量），而 `iVE 0 ^&0 = eqAtom ^&0`。
左边 `iT 0 (subst ?[^&0] p)`，右边 `subst (eqAtom ^&0) (iT 1 p)`。
**它退化不成** `HABKey.iT_free_eq`（那条右端是 `subst ?[^&0] (iT 1 (shift p))`，
向量不同：`?[^&0]` 是一个自由变量，`[eqAtom ^&0]` 是一个**公式**）。
所以这条探针只验证「statement 不荒谬」。 -/
example (p : V) (hp : IsSemiformula ℒₒᵣ 1 p) :
    iT (0 : V) (substs1 ℒₒᵣ (^&0) p) = subst ℒₛₑₜ (iVE (0 : V) (^&0)) (iT (1 : V) p) := by
  show iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) p) = _
  sorry

/-- **`iT_substs1_term`**：任意项代换与 `iT` 交换。

     iT 0 (substs1 t p) = subst (iVE 0 t) (iT 1 p)

语义：`p[t]` 的翻译 = 「在 `iT 1 p` 里把 `iVE` 描述的变量等式代入」——
`iVE 0 t` 编码「t 的值 = #0」，即 p 里那个新绑定变量的约束。 -/
theorem iT_substs1_term (p t : V) (hp : IsSemiformula ℒₒᵣ 1 p) (ht : IsTerm ℒₒᵣ t) :
    iT (0 : V) (substs1 ℒₒᵣ t p) = subst ℒₛₑₜ (iVE (0 : V) t) (iT (1 : V) p) := by
  -- 首先把 substs1 展开成 subst ?[t]（definitional）
  show iT (0 : V) (subst ℒₒᵣ (?[t] : V) p) = subst ℒₛₑₜ (iVE (0 : V) t) (iT (1 : V) p)
  sorry

end GodelQ.ExsBridge3

#print axioms GodelQ.ExsBridge3.iT_substs1_term
