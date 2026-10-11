import GodelQ.ZFC.Z0Full
import Foundation.FirstOrder.Incompleteness.StandardProvability

/-! 探针 2：寻找绕开语义解释定理的 V 内部工具（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCZ0 GodelQ.Z0Full

namespace Probe2

-- A. V 内部的推导弱化
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.Derivation.of_ss
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.Derivable.of_ss
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.Provable
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.Theory.Δ₁Class

-- B. Theory.RE 给什么
#check @FFL.FirstOrder.Theory.RE
#check @FFL.FirstOrder.Theory.RE.reCh
#check @FFL.FirstOrder.Theory.reCh
#check @FFL.FirstOrder.Theory.craigCh

-- C. 内部化的 WeakerThan（若存在）
#check @FFL.FirstOrder.Arithmetic.provable_standardProvability_imp_of_Δ₁Class_subset

-- D. Sh 的 RE 见证公式形状
#print GodelQ.ZFCZ0.Sh_RE
#check @GodelQ.ZFCZ0.zfc_provable_re
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.REPred

-- E. 关键：Sh.craig 的 Δ1 类与 Sh 的 reCh 的关系
#check @FFL.FirstOrder.Theory.IsCraigAxiom
#check @FFL.FirstOrder.Theory.mem_craig_codes_iff

-- F. Provable 与 Derivable 的关系
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.TProvable.iff_provable
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Arithmetic.tprovable_iff_provable

end Probe2
