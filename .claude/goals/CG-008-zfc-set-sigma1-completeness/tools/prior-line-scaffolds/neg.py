from pathlib import Path
text = r'''import GodelQ.ZFC.Z0UniBridge

/-!
# 负控制：`Z0UniBridge` 的归约不是空转

本文件试图把 `models_zfcTr_iff'` 的**假设侧**去掉：
断言 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 可由 `zfcTr σ` 在**任意**模型中的真值推出，
而不经过 `models_zfcTr_iff'` 的等价。

内核应拒绝：`zfcTr σ` 的真值只与 `trProv.val/[⌜σ⌝]` 的求值有关，
它是一个**模型事实**；而 `Provable 𝗭𝗙𝗖 ⌜translate σ⌝` 是一个**存在量词命题**。
两者由 `models_zfcTr_iff'` 连起来，但那条等价不是恒等式，
不能把 `V ⊧ zfcTr σ` 直接当成 `Provable`。

本文件带未证标记时不进收据源；这里它是**故意错**的，用来钉住归约的方向性。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.Z0UniBridgeWrong

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 错误断言：模型真值可以直接当作可证性，不需要 `models_zfcTr_iff'` 这条等价。 -/
example (σ : ArithmeticSentence) (h : V ↓[ℒₒᵣ] ⊧ zfcTr σ) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) :=
  h

end GodelQ.Z0UniBridgeWrong
'''
Path('GodelQ/ZFC/WrongZ0UniBridge.lean').write_text(text, encoding='utf-8')
print('written')
