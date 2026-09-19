{-# OPTIONS --safe --cubical --guardedness --two-level #-}

-- ReboundDisarm：第一弹反弹（极限理论式紧化）的「消毒」正面收据（2026-09-19）
-- claim id : CAND-F2-7-REBOUND-DISARM (candidate；registers_new_claim:false)
--
-- 背景（用户 2026-09-19 指令）：第一弹打出后的反弹 = 传统拓扑学处理圆环悖论的
-- 方法——加一个理想点、规定收敛、宣布「已处理」（023 片反弹机制的原始形态）。
-- 本模块机器见证该反弹的**构造性重建**在 cubical HoTT 中合法且免费：
--   1. 理想点是**显式构造子**（base : S¹），不是 postulate——本模块 --safe、
--      零公理通过编译即为其机器证词；
--   2. 经 HIT 的闭计算**可归约**（intLoop (pos zero) 定义性归约到 refl）——
--      canonicity 不被收费（对照 TA/TA-AC/TA-LEM 族：postulate 注入才收费）；
--   3. 端点同一化是**路径构造子**（loop : base ≡ base），不是收敛声明。
-- 结论（消毒叙事的精确形态）：极限理论本身在引擎中不死——死的只是它的
-- **免费用法**；真正的收费点在 Ω 塌缩层（CutRealLayer 的 SingleOmega，
-- B1a 已证「付费才有」），不在紧化。攻击面因此从「极限理论」移到
-- 「完成声明的免费化」。
--
-- 边界：本模块不声称紧化古典用法的非现实性已被形式化（那是论证层）；
-- 不声称 HoTT 不一致；对照收费演示件见 MissileFourChargeDemo.agda（故意
-- 不带 --safe，postulate 即收费注入点）。

module ReboundDisarm where

open import Cubical.Foundations.Prelude using (_≡_; refl)
open import Cubical.HITs.S1 using (S¹; base; loop; intLoop)
open import Cubical.Data.Int.Base using (ℤ; pos)

------------------------------------------------------------------------
-- 1. 理想点的显式性：紧化的「被加的点」就是构造子 base。
--    内核接受 base : S¹ 这个**闭构造子项**，即 canonicity 在对象层的见证。
------------------------------------------------------------------------

ideal-point-is-explicit : S¹
ideal-point-is-explicit = base

------------------------------------------------------------------------
-- 2. 端点同一化的构造性形态：两端收敛到同一点 = 一条路径构造子 loop。
--    古典紧化用「规定收敛」；cubical 用路径构造子——没有隐藏的声明。
------------------------------------------------------------------------

endpoint-identification-is-a-path : base ≡ base
endpoint-identification-is-a-path = loop

------------------------------------------------------------------------
-- 3. 经 HIT 的闭计算可归约：intLoop (pos zero) 定义性归约到 refl。
--    refl 被内核接受 = 该闭项经 HIT 递归原理后仍取得典范形——
--    「加理想点不收费」的计算证词（与 TA 族 postulate 卡住形态对照）。
------------------------------------------------------------------------

hit-computation-witness : intLoop (pos 0) ≡ refl
hit-computation-witness = refl
