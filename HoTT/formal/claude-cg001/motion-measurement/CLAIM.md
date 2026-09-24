# CG-001 / A1「沿运动测量」证明包

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），CG-001 执行会话 bb204ea1。
> proof id：`MP-CG001-MOTION-MEASUREMENT-001`（主包）、`MP-CG001-MOTION-MEASUREMENT-NEG-001`（负控制）。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设、无额外公理。
> 索引：本目标的 `.claude/goals/CG-001-targeted-overview/证据索引.md`（GOAL_LOCAL_INDEX_ONLY）。共享矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的行只以草稿写在该目标的 `relay.md`，由 integrator 决定是否登记。

## 这个包证明什么、不证明什么

本包的数学内容都是 HoTT 中早已知道的基本事实：书 引理 2.2.1（ap）、引理 2.3.4（apd）、引理 6.3.1（区间可缩）、推论 7.5.9（连通类型到集合的映射为常值）等。本包只在固定工具链上原生重证它们，并把它们接到 CG-001 候选 A1 的现实任务上，**不主张原创**。

现实解释（“仪表”“旅程”“跑道”“车站”“钟”）是解释桥上的标签，由工作台 A1 候选卡承担；本包不证明任何物理事实，也不证明 HoTT 内部矛盾。

## 命题全文

记号：`ℓ ℓ'` 为任意宇宙层级；`≡` 为 Cubical Path；`I` 为区间；`isSet P` 即 P 是 0-type。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-01** | 对任意 `A : Type ℓ`、`P : Type ℓ'`、`f : A → P`、`a b : A`、`p : a ≡ b`：(i) `f a ≡ f b`；(ii) 对任意 `i : I`，`f (p i) ≡ f a`；(iii) 对任意 `i j : I`，`f (p i) ≡ f (p j)`；(iv) 若 `isSet P`，对任意回路 `p : a ≡ a`，`cong f p ≡ refl`；(v) 不存在 `a b`、`p : a ≡ b` 使 `¬ (f a ≡ f b)`。 | `travelKeepsReading`、`readingAtEveryMoment`、`anyTwoMoments`、`loopRecordIsFlat`、`noTripWithChangedReading` |
| **CG001-C-02** | 在 cubical 0.9 的 `S¹`（`base`、`loop`）上：(i) 对任意集合 `P` 与 `h : S¹ → P`，`∀ x, h x ≡ h base`；(ii) 不存在 `d : S¹ → Bool` 使 `d base ≡ true` 且某 `x` 有 `d x ≡ false`；(iii) 任意 `h : S¹ → ℚ` 为常值；(iv) `∀ x, ∥ base ≡ x ∥₁`（库 `isConnectedS¹` 的重述）；(v) 对照：`transport (λ i → helix (loop i)) (pos 0) ≡ pos 1`，由 `refl` 成立。 | `circleReadingConstant`、`noStationDetector`、`ringThermometerConstant`、`alwaysArrived`、`lapCounterAdvances` |
| **CG001-C-03** | 在区间 HIT（`start`、`finish`、`seg`）上：(i) `start ≡ finish`；(ii) 对任意 `P` 与 `T : Interval → P`，`T start ≡ T finish`；(iii) 不存在 `T` 使 `¬ (T start ≡ T finish)`。负控制：定义 `thermometer start = 0`、`finish = 1`、`seg i = 0` 被内核拒绝（`UnequalTerms 1 != 0`）。 | `roadEndsSamePlace`、`roadEndsSameReading`、`noThermometerGradient`；`WrongVaryingReading.agda` |
| **CG001-C-04** | 在 cubical 0.9 的 `ℚ = (ℤ × ℕ₊₁) // ∼` 上：(i) `¬ ([ pos 0 / 1+ 0 ] ≡ [ pos 1 / 1+ 0 ])`；(ii) 对任意 `x : ℚ` 与 `p : x ≡ x`，`p ≡ refl`。 | `noMotionOnRationalLine`、`rationalLoopsTrivial` |
| **CG001-C-05** | (a) 对归纳类型 `Pos`（`p0`–`p3`）与 `step`、`trip : ℕ → Pos`、`height : Pos → ℕ`：`trip 4 ≡ p0`；`height (trip k)` 在 k = 0,1,2,3,4 依次为 0,1,2,1,0（均由 `refl` 成立）；`¬ (height (trip 1) ≡ height (trip 0))`；存在 `x : Pos` 使 `¬ (x ≡ p0)`。(b) 对 HIT `Ring4`（点 `r0`–`r3`，路径 `e0 : r0 ≡ r1`、`e1`、`e2`、`e3 : r3 ≡ r0`）：不存在 `h : Ring4 → ℕ` 使 `h r0 ≡ 0` 且 `h r1 ≡ 1`；不存在 `d : Ring4 → Bool` 使 `d r0 ≡ true` 且 `d r1 ≡ false`；`∀ x, ∥ r0 ≡ x ∥₁`；不存在 `x` 使 `¬ (r0 ≡ x)`。 | `Pos`、`step`、`trip`、`height`、`tripReturns`、`recordAt0`–`recordAt4`、`recordVaries`、`stationDetector`、`stationClosedLeavesTrack`；`Ring4`、`noHeightProfileOnRing4`、`noDetectorOnRing4`、`ring4Connected`、`closedStationLeavesNothing` |
| **CG001-C-06** | 对类型族 `Counter : Interval → Type`（`Counter start = ℤ`、`Counter finish = ℤ`、`Counter (seg i) = sucPathℤ i`）：存在截面 `counterReading`，其 `start` 值为 `pos 0`、`finish` 值为 `pos 1`；`¬ (counterReading start ≡ counterReading finish)`（二者同为 ℤ 的元素）；`∀ z, transport (λ i → Counter (seg i)) z ≡ sucℤ z`；`transport (λ i → Counter (seg i)) (counterReading start) ≡ counterReading finish`。一般形式：对任意 `F : A → Type ℓ'`、截面 `s`、路径 `p : a ≡ b`，`transport (λ i → F (p i)) (s a) ≡ s b`。 | `Counter`、`counterReading`、`rawReadingsDiffer`、`roadShiftIsBuiltIn`、`transportedReadingAgrees`、`sectionAgreesAfterTransport` |
| **CG001-C-07** | 对任意 `A`、`clock : A → ℕ`、`p : a ≡ b`：`clock a ≡ clock b`；`p ∙ sym p ≡ refl`；对任意 `count : Type ℓ → P` 与 `e : A ≃ B`：`count A ≡ count B`（经 `ua e`）。 | `clockStandsStill`、`roundTripIsNoTrip`、`headcountInvariant` |

## 禁止外推

- 不证明任何“实数参数化轨迹”“解析曲线”或“离散时间函数”上的读数不变；C-05(a) 恰好是这类表示下读数会变的正控制。
- 不证明 HoTT 不能表示随位置变化的量：C-06 表明，把变化写进类型族（依赖纤维）时，两端原始读数可以不同，但差正是类型族里预先写好的平移。
- 不证明 Book HoTT 或 Cubical Agda 不一致，不证明任何现实系统有误，不证明物理时空的结构。
- C-02(iii)、C-04 只涉及 cubical 0.9 的 `ℚ`；Book 实数是集合由书 定理 11.3.9 给出（来源报告，未在本包重放）。
- “仪表”“旅程”“车站”只是解释标签；这些词对应的现实任务与桥梁见工作台 §4 A1 候选卡。
