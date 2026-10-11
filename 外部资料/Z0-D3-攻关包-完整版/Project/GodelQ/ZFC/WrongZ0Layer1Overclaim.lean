/- Expected-rejection control: layer 1 alone must NOT give D3. -/
import GodelQ.ZFC.Z0Layer1

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.Z0Full

-- 尝试把层 1 的交换律当成 D3 。
-- 必须被驳：连词与量词的交换不含可证性谓词的任何信息。
theorem wrong_layer1_gives_D3 (σ : ArithmeticSentence) :
    𝗜𝚺₁ ⊢ ↑(zfcTr σ) 🡒 ↑(zfcTr (zfcTr σ)) :=
  GodelQ.Z0Layer1.map_all (φ := Semiformula.all ⊤)
