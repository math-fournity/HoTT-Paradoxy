import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge2` 原子情形的**语义路线**（2026-10-13）

目标（原子情形）：
```
Provable 𝗭𝗙𝗖 (imp (iT 0 (^rel 2 cEqN ?[^&0,^&0]))
                  (^∃ (domZero ⋏ iT 1 (^rel 2 cEqN ?[^#0,^#0]))))
```

语义路线：`SetTheory.complete` 把目标化为「在每个 𝗭𝗙𝗖 模型里成立」。
但注意：`iT 0 (^rel ...)` 是 **V 里的码**，不是 `Semiformula`。
要接 `SetTheory.complete`（它要 `SetTheorySentence`），
须先说明这个码就是某个 `Semiformula` 的引号（`⌜·⌝`）。

**本探针核验这一步能否走通**（`iT` 码 ↔ `Semiformula` 引号）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeSemanticAtom

-- `iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（iT_quote，已核验可用）
-- 反向：`iT 0 p` 何时是某个 Semiformula 的引号？
#check @iT_quote
#check @Semiformula.quote
#check @Semiformula.quote_inj

-- 关键：`Provable` 吃的是 V 里的码，`SetTheory.complete` 产的是 `T ⊢ φ`（Semiformula 层）
-- 找两者的桥
#check @Provable.sound2
#check @Theory.Proof.complete_on_eq_models

end ProbeSemanticAtom