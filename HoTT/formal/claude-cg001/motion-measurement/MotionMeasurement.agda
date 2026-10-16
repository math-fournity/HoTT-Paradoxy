{-# OPTIONS --safe --cubical --guardedness #-}
{-
  CG-001 / A1「沿运动测量」原生证明
  工具链：Agda 2.8.0-3d04bac，cubical 0.9（HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json）
  proof id：MP-CG001-MOTION-MEASUREMENT-001
  claims  ：CG001-C-01 … CG001-C-07（命题全文、量词与禁止外推见同目录 CLAIM.md）

  身份：有范围的机器证明。仪表、旅程、跑道等现实解释属于解释桥，
  由 CLAIM.md 与工作台候选卡承担，本文件不证明任何物理事实。
-}
module MotionMeasurement where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Equiv
open import Cubical.Foundations.Univalence using (ua)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Data.Sigma
open import Cubical.Data.Empty using (⊥; isProp⊥)
open import Cubical.Data.Bool using (Bool; true; false; true≢false; isSetBool)
open import Cubical.Data.Nat using (ℕ; zero; suc; znots; snotz)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucℤ; injPos; sucPathℤ)
open import Cubical.Data.NatPlusOne using (1+_)
open import Cubical.Data.Rationals.Base using (ℚ; isSetℚ; [_/_]; eq/⁻¹)
open import Cubical.HITs.S1 using (S¹; base; loop; helix)
open import Cubical.HITs.S1.Properties using (isConnectedS¹)
open import Cubical.HITs.Interval using (Interval; seg)
  renaming (zero to start; one to finish)
open import Cubical.HITs.PropositionalTruncation using (∥_∥₁; ∣_∣₁; squash₁; rec)
open import Cubical.Relation.Nullary using (¬_)

private
  variable
    ℓ ℓ' : Level

------------------------------------------------------------------------
-- CG001-C-01（T1）：函数沿路径保持读数。
-- 书 引理 2.2.1（basics.tex L686–700）：ap 同时被读作“函数尊重相等”与“函数连续”。
-- 这里对任意类型 A、任意读数类型 P、任意“仪表” f、任意“旅程” p 成立。

travelKeepsReading : {A : Type ℓ} {P : Type ℓ'} (f : A → P) {a b : A}
  → a ≡ b → f a ≡ f b
travelKeepsReading f p = cong f p

-- Cubical 逐刻形态：旅程中任一时刻 i 的读数都等于出发时的读数。
readingAtEveryMoment : {A : Type ℓ} {P : Type ℓ'} (f : A → P) {a b : A}
  (p : a ≡ b) (i : I) → f (p i) ≡ f a
readingAtEveryMoment f p i = cong f (λ j → p (i ∧ ~ j))

-- 任意两刻的读数相同。
anyTwoMoments : {A : Type ℓ} {P : Type ℓ'} (f : A → P) {a b : A}
  (p : a ≡ b) (i j : I) → f (p i) ≡ f (p j)
anyTwoMoments f p i j = readingAtEveryMoment f p i ∙ sym (readingAtEveryMoment f p j)

-- 读数取值于集合时，绕回原处的整条读数记录就是常路径。
loopRecordIsFlat : {A : Type ℓ} {P : Type ℓ'} → isSet P → (f : A → P) {a : A}
  (p : a ≡ a) → cong f p ≡ refl
loopRecordIsFlat setP f p = setP _ _ (cong f p) refl

-- “加一个非依赖字段”无济于事：不存在一条旅程，使某个仪表在两端读数不同。
-- 对一切类型 A、一切读数类型 P、一切 f 成立。
noTripWithChangedReading : {A : Type ℓ} {P : Type ℓ'} (f : A → P)
  → ¬ (Σ[ a ∈ A ] Σ[ b ∈ A ] (a ≡ b) × (¬ (f a ≡ f b)))
noTripWithChangedReading f (a , b , p , changed) = changed (cong f p)

------------------------------------------------------------------------
-- CG001-C-02：环形跑道 S¹（书 §6.1：由一个点 base 与一条路径 loop 生成）。
-- 任何取值于集合的仪表处处读数相同（书 推论 7.5.9 在 S¹ 上的实例）。

circleReadingConstant : {P : Type ℓ} → isSet P → (h : S¹ → P) → (x : S¹) → h x ≡ h base
circleReadingConstant setP h base = refl
circleReadingConstant setP h (loop i) =
  isProp→PathP (λ j → setP (h (loop j)) (h base)) refl refl i

-- 不存在“只在车站响”的探测器：在 base 为 true、在某处为 false 的 d 不存在。
noStationDetector : ¬ (Σ[ d ∈ (S¹ → Bool) ] (d base ≡ true) × (Σ[ x ∈ S¹ ] d x ≡ false))
noStationDetector (d , atStation , x , elsewhere) =
  true≢false (sym atStation ∙ sym (circleReadingConstant isSetBool d x) ∙ elsewhere)

-- 有理数值温度计在环上处处读数相同。
ringThermometerConstant : (h : S¹ → ℚ) (x : S¹) → h x ≡ h base
ringThermometerConstant = circleReadingConstant isSetℚ

-- B 向孪生：环上任一处都（merely）“已到站”（书 hlevels.tex L1260）。
alwaysArrived : (x : S¹) → ∥ base ≡ x ∥₁
alwaysArrived = isConnectedS¹

-- 对照：随路径扭转的圈数计数器（helix）绕一圈确实 +1。
-- HoTT 能数圈；读数属于随位置扭转的纤维，而非固定刻度。
lapCounterAdvances : transport (λ i → helix (loop i)) (pos 0) ≡ pos 1
lapCounterAdvances = refl

------------------------------------------------------------------------
-- CG001-C-03：一条路（区间 HIT，书 §6.3）。两端是“同一个地方”（seg），
-- 路上任何仪表两端读数相同；不存在两端读数不同的温度计。

roadEndsSamePlace : start ≡ finish
roadEndsSamePlace = seg

roadEndsSameReading : {P : Type ℓ} (T : Interval → P) → T start ≡ T finish
roadEndsSameReading T = cong T seg

noThermometerGradient : {P : Type ℓ} → ¬ (Σ[ T ∈ (Interval → P) ] ¬ (T start ≡ T finish))
noThermometerGradient (T , differ) = differ (cong T seg)

------------------------------------------------------------------------
-- CG001-C-04：有理数线（稠密、是集合）上，0 与 1 之间没有路径：“有数的线不能动”。

q0 q1 : ℚ
q0 = [ pos 0 / 1+ 0 ]
q1 = [ pos 1 / 1+ 0 ]

noMotionOnRationalLine : ¬ (q0 ≡ q1)
noMotionOnRationalLine p = znots (injPos (eq/⁻¹ _ _ p))

rationalLoopsTrivial : (x : ℚ) (p : x ≡ x) → p ≡ refl
rationalLoopsTrivial x p = isSetℚ x x p refl

------------------------------------------------------------------------
-- CG001-C-05（正控制与前提切换）。
-- (a) 量子化的环：4 个位置，运动当作离散时间的函数（不是路径）。
--     读数记录 0,1,2,1,0 会变；车站可以被识别、被关闭，关闭后其余位置仍在。

data Pos : Type where
  p0 p1 p2 p3 : Pos

step : Pos → Pos
step p0 = p1
step p1 = p2
step p2 = p3
step p3 = p0

trip : ℕ → Pos
trip zero = p0
trip (suc k) = step (trip k)

height : Pos → ℕ
height p0 = 0
height p1 = 1
height p2 = 2
height p3 = 1

tripReturns : trip 4 ≡ p0
tripReturns = refl

recordAt0 : height (trip 0) ≡ 0
recordAt0 = refl

recordAt1 : height (trip 1) ≡ 1
recordAt1 = refl

recordAt2 : height (trip 2) ≡ 2
recordAt2 = refl

recordAt3 : height (trip 3) ≡ 1
recordAt3 = refl

recordAt4 : height (trip 4) ≡ 0
recordAt4 = refl

recordVaries : ¬ (height (trip 1) ≡ height (trip 0))
recordVaries = snotz

stationDetector : Pos → Bool
stationDetector p0 = true
stationDetector p1 = false
stationDetector p2 = false
stationDetector p3 = false

stationClosedLeavesTrack : Σ[ x ∈ Pos ] ¬ (x ≡ p0)
stationClosedLeavesTrack = p1 , λ q → true≢false (cong stationDetector (sym q))

-- (b) 同样四个位置，把“走一步”换成路径（HoTT 的运动）：前提切换。

data Ring4 : Type where
  r0 r1 r2 r3 : Ring4
  e0 : r0 ≡ r1
  e1 : r1 ≡ r2
  e2 : r2 ≡ r3
  e3 : r3 ≡ r0

-- 不再存在读数 0、1 的高度计。
noHeightProfileOnRing4 : ¬ (Σ[ h ∈ (Ring4 → ℕ) ] (h r0 ≡ 0) × (h r1 ≡ 1))
noHeightProfileOnRing4 (h , h0 , h1) = znots (sym h0 ∙ cong h e0 ∙ h1)

-- 不再存在车站探测器。
noDetectorOnRing4 : ¬ (Σ[ d ∈ (Ring4 → Bool) ] (d r0 ≡ true) × (d r1 ≡ false))
noDetectorOnRing4 (d , at , off) = true≢false (sym at ∙ cong d e0 ∙ off)

-- Ring4 连通：任一位置都（merely）与车站相等。
ring4Connected : (x : Ring4) → ∥ r0 ≡ x ∥₁
ring4Connected r0 = ∣ refl ∣₁
ring4Connected r1 = ∣ e0 ∣₁
ring4Connected r2 = ∣ e0 ∙ e1 ∣₁
ring4Connected r3 = ∣ e0 ∙ e1 ∙ e2 ∣₁
ring4Connected (e0 i) = isProp→PathP (λ j → squash₁ {A = r0 ≡ e0 j}) ∣ refl ∣₁ ∣ e0 ∣₁ i
ring4Connected (e1 i) = isProp→PathP (λ j → squash₁ {A = r0 ≡ e1 j}) ∣ e0 ∣₁ ∣ e0 ∙ e1 ∣₁ i
ring4Connected (e2 i) = isProp→PathP (λ j → squash₁ {A = r0 ≡ e2 j}) ∣ e0 ∙ e1 ∣₁ ∣ e0 ∙ e1 ∙ e2 ∣₁ i
ring4Connected (e3 i) = isProp→PathP (λ j → squash₁ {A = r0 ≡ e3 j}) ∣ e0 ∙ e1 ∙ e2 ∣₁ ∣ refl ∣₁ i

-- 关闭车站（只能用 ¬(r0 ≡ x) 表达，书 §1.12）后，什么都不剩。
closedStationLeavesNothing : ¬ (Σ[ x ∈ Ring4 ] ¬ (r0 ≡ x))
closedStationLeavesNothing (x , away) = rec isProp⊥ away (ring4Connected x)

------------------------------------------------------------------------
-- CG001-C-06（依赖读数的出路及其限度）。
-- 把“变化”写进类型族：沿路用 sucPathℤ 粘合纤维，两端的原始读数便可以不同；
-- 但这个差恰好是类型族里预先写好的平移：沿路运输把起点读数送到终点读数。

Counter : Interval → Type
Counter start = ℤ
Counter finish = ℤ
Counter (seg i) = sucPathℤ i

counterReading : (x : Interval) → Counter x
counterReading start = pos 0
counterReading finish = pos 1
counterReading (seg i) = toPathP {A = λ j → sucPathℤ j} {x = pos 0} {y = pos 1} refl i

rawReadingsDiffer : ¬ (counterReading start ≡ counterReading finish)
rawReadingsDiffer p = znots (injPos p)

roadShiftIsBuiltIn : (z : ℤ) → transport (λ i → Counter (seg i)) z ≡ sucℤ z
roadShiftIsBuiltIn z = transportRefl (sucℤ z)

transportedReadingAgrees :
  transport (λ i → Counter (seg i)) (counterReading start) ≡ counterReading finish
transportedReadingAgrees = fromPathP (cong counterReading seg)

-- 一般形式：任何类型族的任何截面，沿任何路径运输后都与终点读数一致（书 引理 2.3.4 apd）。
sectionAgreesAfterTransport : {A : Type ℓ} (F : A → Type ℓ') (s : (x : A) → F x)
  {a b : A} (p : a ≡ b) → transport (λ i → F (p i)) (s a) ≡ s b
sectionAgreesAfterTransport F s p = fromPathP (cong s p)

------------------------------------------------------------------------
-- CG001-C-07：换比喻检查。

-- 钟（ℕ 值）沿任何旅程读数不变。
clockStandsStill : {A : Type ℓ} (clock : A → ℕ) {a b : A} → a ≡ b → clock a ≡ clock b
clockStandsStill clock = cong clock

-- 往返等于没出门（书 引理 2.1.4）。
roundTripIsNoTrip : {A : Type ℓ} {a b : A} (p : a ≡ b) → p ∙ sym p ≡ refl
roundTripIsNoTrip = rCancel

-- 宇宙层：沿等价（ua）移动的“集合”，任何量都不变（人数不变）。
headcountInvariant : {P : Type ℓ'} (count : Type ℓ → P) {A B : Type ℓ}
  → A ≃ B → count A ≡ count B
headcountInvariant count e = cong count (ua e)
