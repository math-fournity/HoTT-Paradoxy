import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeAcceptBlocker
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 验收台自检：把一个**真证明**填进去，看公理表是否变干净

`RootBlocker` 与已证的 `hRoot_core` 只差第三条假设：
`hRoot_core` 要 `Provable 𝗭𝗙𝗖 (iT 0 p)`，`RootBlocker` 给的是 `p ∈ Sh.craig.Δ₁Class`。

**所以 `RootBlocker` 可以精确地归约成一条更小的义务**：
`p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`（这正是 D3 那一层）。
把那条**当参数**传进来，`RootBlocker` 立刻成立——
这就是验收台要演示的「填一个真证明，exit 0，公理表干净」。 -/

-- 归约版：RootBlocker 由「更小的义务」推出（真证明，无未证标记）
theorem accept_root_via_reduction
    (h : ∀ (p : V), p ∈ Sh.craig.Δ₁Class → Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0:V) p)) :
    ShCraigElimSetupQ.RootBlocker (V := V) := by
  intro s p hs hps hd1
  exact ShCraigElimSetupQ.hRoot_core (V := V) hs hps (h p hd1)

-- 验收台：与上面同形，但**证明留空**（候选填这里）
theorem accept_root : ShCraigElimSetupQ.RootBlocker (V := V) := by
  sorry

-- 口径说明：`accept_root_via_reduction` 是**归约**不是证明——
-- 它把 RootBlocker 精确地搬到 D3 那一层，本身不解决 D3。
#print axioms accept_root_via_reduction
#print axioms accept_root

end GodelQ.ProbeAcceptBlocker
