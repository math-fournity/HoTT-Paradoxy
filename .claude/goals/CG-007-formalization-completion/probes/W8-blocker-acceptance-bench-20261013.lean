import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeAcceptBlocker
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 三条 Blocker 的**验收台**（2026-10-13）

## 用途

别的线证出桥之后，把证明填进对应 `theorem accept_*` 的 `sorry`，跑 build：

* 输出只剩 `[propext, Classical.choice, Quot.sound]` = **接线成功**；
* 出现 `sorryAx` = 那条 blocker 还没真证出来。

## 递证明前先核对形状

六条 `#check` 打出 blocker 的精确形状（Q 版三条 + 非 Q 版三条）。
有些证明天然是 `Derivable` 形状（非 Q 版），有些是 `Q` 形状，先 check 再递，
形状差一点就白费一轮。

## 自检证据（本台自己验过，判据不是摆设）

```
accept_root_via_reduction  depends on axioms: [propext, Classical.choice, Quot.sound]           ← 真证明
accept_root                depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]  ← 占位
```

同一台机器、同一形状，一个干净一个带 `sorryAx`。 -/

-- ── 形状快照（供递证明前核对）─────────────────────────────
#check (ShCraigElimSetupQ.AllBlockerQ : Prop)
#check (ShCraigElimSetupQ.ExsBlockerQ : Prop)
#check (ShCraigElimSetupQ.RootBlockerQ : Prop)
#check (ShCraigElimSetupQ.AllBlocker : Prop)
#check (ShCraigElimSetupQ.ExsBlocker : Prop)
#check (ShCraigElimSetupQ.RootBlocker : Prop)

-- ── 验收位 1：AllBlockerQ（iT 与 free/subst 相容）─────────
theorem accept_all : ShCraigElimSetupQ.AllBlockerQ (V := V) := by
  sorry

-- ── 验收位 2：ExsBlockerQ（iT 与 substs1 相容；等式路线已判死，改走可证蕴含）─
theorem accept_exs : ShCraigElimSetupQ.ExsBlockerQ (V := V) := by
  sorry

-- ── 验收位 3：RootBlockerQ（= 命题 C / D3 的可证性内化）───
theorem accept_root : ShCraigElimSetupQ.RootBlockerQ (V := V) := by
  sorry

-- ── 附带：RootBlocker（非 Q 版）的一步归约，**已证** ──────
-- RootBlocker 与已证的 hRoot_core 只差第三条假设：
--   hRoot_core 要 `Provable 𝗭𝗙𝗖 (iT 0 p)`，RootBlocker 给 `p ∈ Sh.craig.Δ₁Class`。
-- 所以 RootBlocker 可精确归约成 `p ∈ Sh.craig.Δ₁Class → Provable 𝗭𝗙𝗖 (iT 0 p)`（= D3 那层）。
-- **它不解决 D3**，只是把义务搬到那一层、形状更小。
theorem accept_root_via_reduction
    (h : ∀ (p : V), p ∈ Sh.craig.Δ₁Class →
      Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (iT (0:V) p)) :
    ShCraigElimSetupQ.RootBlocker (V := V) := by
  intro s p hs hps hd1
  exact ShCraigElimSetupQ.hRoot_core (V := V) hs hps (h p hd1)

-- ── 验收口令 ────────────────────────────────────────────
-- 填完三个 `sorry` 后跑 build，看下面三条：
--   只剩 [propext, Classical.choice, Quot.sound] = 接线成功
--   出现 sorryAx = 那条还没真证出来
#print axioms accept_all
#print axioms accept_exs
#print axioms accept_root
#print axioms accept_root_via_reduction

end GodelQ.ProbeAcceptBlocker
