-- CG-009 负控制（泛型层）：局部门确实是"G 处"的。
-- 把 ⊥ 处的 D3 冒充 Gödel 句 G 处的 D3——内核应以类型不匹配拒绝。
-- 本文件预期 exit 1（type mismatch on the intended statements）。
import GodelQ.ZFC.Z0LocalGate

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0LocalGateNegative

/-- 预期被内核拒绝：⊥ 处的 D3 不是 G 处的 D3（句子不同，语句类型不同）。 -/
example {L : Language} [L.ReferenceableBy L] {T₀ T : Theory L} {𝔅 : Provability T₀ T}
    [Diagonalization T₀] [L.DecidableEq] [T₀ ⪯ T] [Consistent T] [𝔅.HBL2]
    (hbot : T₀ ⊢ 𝔅 (⊥ : Sentence L) 🡒 𝔅 (𝔅 (⊥ : Sentence L))) :
    T₀ ⊢ 𝔅 (gödel 𝔅) 🡒 𝔅 (𝔅 (gödel 𝔅)) :=
  hbot

end GodelQ.Z0LocalGateNegative
