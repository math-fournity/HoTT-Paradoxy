# A1 延伸：序、距离、稠密放在哪里，运动放在哪里

> HUMAN_EDITED；2026-09-24；Claude（Opus 5.5），会话 6fd0312a（接手交接文档 `.claude/handoff/20260924-A1-三份表达碰撞与归因-交接.md`，用户指令“你来接手后续探索”）。
> proof id：`MP-CG001-MOTION-ORDER-SPLIT-001`（主包）、`MP-CG001-MOTION-ORDER-SPLIT-NEG-001`（负控制）；claims：`CG001-C-15`–`CG001-C-18`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §6（GOAL_LOCAL_INDEX_ONLY）；共享矩阵行只以草稿交 integrator。

## 这个包为什么存在

它服务于 A1 的归因讨论，具体是交接文档 §3 留给用户的第 1 问：A1 咬住的是“认同”（连通即相同），还是用户原先怀疑的“稠密、连续”（KC-000003、KC-000024 第一类）？

A1 已有的前提切换（C-05b，Ring4）说明：去掉稠密性，困难仍在。本包补上另一半：**HoTT 的合成运动里根本放不下稠密性。** 稠密性以严格序为前提（“任两点之间还有一点”）；本包证明，在任何类型里，被严格序隔开的两点之间没有运动，连通的类型上放不下任何严格序、任何非零的集合值距离。反过来，有理数线有严格序、有中点，却没有运动。所以在 HoTT 里，“有序、有稠密”的对象与“能运动”的对象是两个互不相通的对象；芝诺式的“穿过稠密点的运动”在合成层面无法提出。

数学内容都是恒等类型莱布尼茨律（路径归纳 / transport）的直接推论，**不主张原创**。“道路”“先后”“距离”“坐标”“时钟”是解释标签，本包不证明任何物理事实，不证明 HoTT 不一致。

## 命题全文

记号：`∥_∥₁` 为命题截断；`Connected A :≡ ∀ (x y : A) → ∥ x ≡ y ∥₁`；`Interval` 为 cubical 0.9 的区间 HIT（`start`、`finish`、`seg`）；`S¹` 为 cubical 0.9 的圆；`Q._<_` 为 cubical 0.9 `Cubical.Data.Rationals.Order` 的严格序；`q0 = [ pos 0 / 1+ 0 ]`、`q½ = [ pos 1 / 1+ 1 ]`、`q1 = [ pos 1 / 1+ 0 ]`。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-15**（有序则无运动） | (i) 对任意 `A : Type ℓ`、`R : A → A → Type ℓ'`：若 `∀ x → ¬ R x x`，则 `∀ x y → R x y → ¬ ∥ x ≡ y ∥₁`。(ii) 若 `Connected A`：对任意命题值关系 `R`（`∀ x y → isProp (R x y)`），`∀ x y x' y' → R x y → R x' y'`；对任意非自反关系 `R`，`∀ x y → ¬ R x y`；对任意集合 `P`、`d : A → A → P`、`o : P`，若 `∀ x → d x x ≡ o`，则 `∀ x y → d x y ≡ o`；对任意集合 `P` 与单射 `f : A → P`（`∀ x y → f x ≡ f y → x ≡ y`），`isProp A`。 | `orderExcludesMotion`、`Connected`、`OnConnected.{relationSpreads, noStrictOrder, noDistance, coordinatedIsPoint}` |
| **CG001-C-16**（道路与圆的实例） | `Connected Interval`；`Connected S¹`；对任意非自反 `R : Interval → Interval → Type ℓ'`，`¬ R start finish`；对任意 `d : Interval → Interval → ℚ`，若 `∀ x → d x x ≡ q0` 则 `d start finish ≡ q0`；对任意非自反 `R` 于 `S¹`，`∀ x y → ¬ R x y`；`¬ isProp S¹`；不存在单射 `f : S¹ → ℚ`。 | `connectedRoad`、`connectedCircle`、`noEarlierOnRoad`、`roadHasNoLength`、`noEarlierOnCircle`、`circleNotAPoint`、`noCoordinateOnCircle` |
| **CG001-C-17**（对照：数线有序无运动） | `(q0 Q.< q½) × (q½ Q.< q1)`（见证 `(0 , refl)`）；`∀ x → ¬ (x Q.< x)`；`¬ (q0 ≡ q1)`；`¬ ∥ q0 ≡ q1 ∥₁`（由 C-15(i) 与 `q0 Q.< q1` 得出）。 | `orderOnNumberLine`、`irreflexiveOnNumberLine`、`noMotionOnNumberLine`、`orderedHenceUnconnected` |
| **CG001-C-18**（一个全局状态） | 对类型族 `Counter : Interval → Type`（`Counter start = ℤ`、`Counter finish = ℤ`、`Counter (seg i) = sucPathℤ i`）：`Path (Σ Interval Counter) (start , pos 0) (finish , pos 1)`；对任意 `P` 与 `g : Σ Interval Counter → P`，`g (start , pos 0) ≡ g (finish , pos 1)`；`¬ (pos 0 ≡ pos 1)`；在 `ℕ × ℤ` 中 `¬ ((0 , pos 0) ≡ (1 , pos 1))`。负控制：把终点写成 `(finish , pos 0)` 的同一构造应被内核拒绝。 | `Counter`、`oneGlobalState`、`globalObservablesFrozen`、`conditionedReadingsDiffer`、`discreteMomentsDistinct`；负控制 `WrongGlobalState.agda` |

## 禁止外推

- C-15 只说非自反关系、命题值关系与集合值两点函数；不涉及取值于高阶类型的结构（例如取值于 `S¹` 的“距离”），也不说连通类型上没有任何结构（路径空间本身可以很丰富，例如 `ΩS¹ ≅ ℤ`，见 C-12）。
- C-16、C-17 只涉及 cubical 0.9 的 `Interval`、`S¹`、`ℚ`；Book 实数 ℝ_c 是集合由 Book 定理 11.3.9 给出（来源报告，本包未重放），故 C-15 同样适用于它，但本包没有在 ℝ_c 上实例化。
- C-17 只给出 0 < 1/2 < 1 这一具体中点，没有证明 ℚ 的一般稠密性。
- C-18 是 C-06 同一族的整体空间形态；它说的是 `Σ Interval Counter` 中的恒等，不说物理时钟或计数器的事实。“全局状态冻结、条件读数变化”与物理学中 Page–Wootters 机制的对应是 AI 解释，见 `.claude/explore/` 工作台，不是本包的命题。
- 本包不证明“HoTT 不能讨论稠密性”：稠密性可以放在集合（ℚ、ℝ_c）上讨论；本包证明的是，它不能与运动（路径）放在同一个对象的同一对点上。
