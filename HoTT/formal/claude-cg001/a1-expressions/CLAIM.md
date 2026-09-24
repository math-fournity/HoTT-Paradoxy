# CG-001 延伸：A1 的第二、第三份 HoTT 表达与二者的碰撞

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），会话 bb204ea1（CG-001 关闭后，按用户“第三份可以做”“把该做的，都做了”继续）。
> proof id：`MP-CG001-A1-EXPRESSIONS-001`；claims：`CG001-C-10`–`CG001-C-14`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §5（GOAL_LOCAL_INDEX_ONLY）；共享矩阵行只以草稿交 integrator。

## 这个包证明什么、不证明什么

A1 的第一份表达（包 `motion-measurement`，C-01–C-07）用的是恒等路径、ap 与几个 HIT：把运动读成恒等路径时，任何取值于集合的读数沿运动不变。本包用 HoTT 的另外几块给出第二、第三份表达，再证明几条把它们放在一起时才显出来的命题（碰撞）。

数学内容都是已知结果或其直接推论：
- 截断中路径的刻画（Book 定理 7.3.12）；
- 圆的泛性质（Book §6.2，库 `IsoFunSpaceS¹`）与单价性；
- ΩS¹ ≃ ℤ（Book 推论 8.1.10）；
- 万有覆叠可缩（Book reals L29–33 的来源报告；本包给出原生证明）。

本包**不主张原创**。“仪表”“跑者”“刻度”“到达”是解释标签；这些标签对应的现实任务与解释桥见交接文档。本包不证明 HoTT 内部矛盾。

## 命题全文

记号：`isSet P` 即 P 是 0-type；`∥_∥₁`、`∥_∥₂` 为命题截断与集合截断；`helix : S¹ → Type` 为 cubical 0.9 的圈数覆叠（`helix base = ℤ`，沿 `loop` 为 `sucPathℤ`）；`ΩS¹ = (base ≡ base)`。

| claim | 命题 | 源码符号 |
|---|---|---|
| **CG001-C-10**（II-a 归因定理） | 对任意 `Pos : Type ℓ`、`Step : Pos → Pos → Type ℓ'`，记 `Invisible :≡ ∀ (P : Type ℓ) → isSet P → ∀ (f : Pos → P) x y → Step x y → f x ≡ f y`，`Identified :≡ ∀ x y → Step x y → ∥ x ≡ y ∥₁`，则 `Identified → Invisible` 且 `Invisible → Identified`；若某个集合值读数在某一步两端不同，则 `¬ Identified`。实例：`Step = _≡_`（S¹ 上把运动读成路径）时 `Identified` 与 `Invisible` 成立；对四个地点与 `next` 函数（`Step x y = (next x ≡ y)`），`¬ Identified`。 | `Attribution.{Invisible, Identified, identified→invisible, invisible→identified, visibleStep→notIdentified}`、`MotionAsIdentity.*`、`MotionAsSteps.stepsAreNotIdentified` |
| **CG001-C-11**（II-b 改名定理） | 对任意 `ℓ`，`Iso (S¹ → Type ℓ) (Σ[ A ∈ Type ℓ ] (A ≃ A))`；`helix` 对应的改名在每个 `z` 上等于 `sucℤ z`。 | `readingSpacesOverLoop`、`lapCounterIsRelabeling` |
| **CG001-C-12**（II-c 圈数去处） | 任意 `h : S¹ → ℤ` 满足 `∀ x, h x ≡ h base`；`Iso ΩS¹ ℤ`；二者合为一个积。 | `noLapCountFromPosition`、`lapsAreTheMannerOfSameness`、`contrast` |
| **CG001-C-13**（III 无原点的刻度） | `¬ ((x : S¹) → helix x)`；对任意 `p : ΩS¹`，`transport (λ i → helix (p i)) (pos 0) ≡ winding p`（由 `refl`）。辅助：`∀ z → ¬ (sucℤ z ≡ z)`（奇偶性）。 | `noAbsoluteOrigin`、`shiftIsWinding`、`sucℤ≢`、`parityFlips` |
| **CG001-C-14**（碰撞） | (i) `isContr (Σ S¹ helix)`；(ii) `(base , pos 0) ≡ (base , pos 1)`（在 `Σ S¹ helix` 中）；(iii) 对任意 `g : Σ S¹ helix → ℤ` 与 `w w'`，`g w ≡ g w'`；(iv) 对任意 `A`、`P : A → Type`、截面 `s t`、路径 `p : a ≡ b`：`s b ≡ transport (λ i → P (p i)) (s a)`，且 `s a ≡ t a → s b ≡ t b`。辅助：`∀ x → isSet (helix x)`，`∀ x c → encode x (decode x c) ≡ c`，`∀ x → Iso (base ≡ x) (helix x)`。 | `runnerHasOneState`、`zeroLapsIsOneLap`、`counterUnreadable`、`NoNewInformation.{destinationPredicted, agreeOnceAgreeAlong}`、`isSetHelix`、`encodeDecode`、`pathsToCounter` |

## 禁止外推

- C-10 只说集合值读数与 merely 恒等；不涉及高阶读数的全部结构。
- C-11 至 C-14 都在 cubical 0.9 的 S¹、helix、ℤ 上；不说所有 HIT 都如此，也不说任何物理跑道、计数器或温度计的事实。
- C-14(i)–(iii) 是万有覆叠可缩的推论；它说的是 `Σ S¹ helix` 中的恒等，不说依赖投影 `snd` 不存在。“计数器读不出数字”只针对取值于 ℤ 的非依赖读数。
- 本包不证明 HoTT 不一致，也不证明 HoTT 不能表示变化：C-11 与 C-06 表明，变化可以作为事先写进类型族的改名来表示。
