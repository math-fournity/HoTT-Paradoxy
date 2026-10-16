{-# OPTIONS --safe --cubical --guardedness #-}
{-
  CG-001 / A1 负控制（预期被内核拒绝）
  proof id：MP-CG001-MOTION-MEASUREMENT-NEG-001
  目的：直接写出“路上的温度计从 0 读到 1”，检查 Cubical Agda 是否拒绝。
  预期：seg 分支在 i = i1 处给 0，而 finish 分支给 1，边界不一致，类型检查失败。
  这证明 CG001-C-03 不是空洞地成立：内核确实执行“沿路径读数不变”的约束。
-}
module WrongVaryingReading where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Nat using (ℕ)
open import Cubical.HITs.Interval using (Interval; seg)
  renaming (zero to start; one to finish)

thermometer : Interval → ℕ
thermometer start = 0
thermometer finish = 1
thermometer (seg i) = 0
