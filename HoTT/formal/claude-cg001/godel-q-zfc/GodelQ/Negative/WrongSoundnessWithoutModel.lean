import GodelQ.ZFC.Soundness

/-!
# 负控制 NEG-SOUNDNESS：数字句的可靠性要用模型

给 𝗭𝗙𝗖 加上一句 `haltsS ΦH a` 之后，`Universe` 不再必然是这个理论的模型；`models_of_provable` 需要的
`Universe ⊧* insert (haltsS ΦH a) 𝗭𝗙𝗖` 找不到。预期：在模型实例处被拒（细化阶段）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound

example {a : ℕ} (h : (insert (haltsS ΦH a) 𝗭𝗙𝗖 : SetTheory) ⊢ haltsS ΦH a) :
    Universe.{0}↓[ℒₛₑₜ] ⊧ haltsS ΦH a :=
  models_of_provable inferInstance h
