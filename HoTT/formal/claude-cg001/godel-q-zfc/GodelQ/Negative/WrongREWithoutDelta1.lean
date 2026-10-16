import GodelQ.ZFC.NeverRE
import Foundation.FirstOrder.SetTheory.Universe

/-!
# 负控制 NEG-DELTA1：可枚举性要用 Δ1 公理表示

`Universe` 中为真的全部句子构成的理论没有 Δ1 表示；内部可证性 `Provable` 所需的 `Theory.Δ₁`
实例找不到，`definability` 无从进行。预期：在 `Theory.Δ₁` 实例处被拒（细化阶段）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCNum

def trueInUniverse : SetTheory := {σ | Universe.{0}↓[ℒₛₑₜ] ⊧ σ}

example (Φ : SetTheorySemisentence 1) :
    𝚺ᴬ₁-Predicate fun b : ℕ ↦ Bootstrapping.Provable trueInUniverse
      (Bootstrapping.neg ℒₛₑₜ (^∃ (numCode b ^⋏ ↑(⌜Φ⌝ : ℕ)))) := by
  definability
