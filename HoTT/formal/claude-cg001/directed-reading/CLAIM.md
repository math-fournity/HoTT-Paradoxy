# 有向读数：先升后降要读数目标提供什么箭头

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。起因：Terra 复审 003 的 O-010（C-24 的目标循环）。回应正文：`Terra对Opus的审计/Opus给GPT的回应/004 - Opus 对 Terra 003 的回复：CG-001.md`；思考笔记：`.claude/思考与发现/CN-022 - Terra 复审 003 的自查与对辩：补丁理论的附录与有向读数.md`。
> proof id：`MP-CG001-DIRECTED-READING-001`（主包）、`MP-CG001-DIRECTED-READING-NEG-001`（负控制）；claims：`CG001-C-34`–`CG001-C-38`。
> 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；源码选项 `--safe --cubical --guardedness`，无公设，不加公理；零警告。
> 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §8（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`。

## 这个包为什么存在

上一轮 Claude 写道：“在合成的有向时间上，要让读数先升后降，需要一个带非可逆回路的读数类型。” Terra 指出这句过强：读数 a、b、a 只要求目标里有箭头 a → b 与 b → a；回路可逆与否取决于目标。本包把这件事按目标的箭头结构分成四类，各给一个机器检查的陈述，并加一个抽象引理，说明为什么“普通数值”读数在有向理论里沿箭头根本不动。

沿有向旅程 0 → 1 → 2 的读数 a、b、a，把旅程的两支箭头送到目标中的箭头 a → b 与 b → a。于是：
- 箭头都塌缩（离散）或目标反对称（偏序）：这样的读数不存在（C-34）；
- 目标中互逆的一对箭头会迫使两端相等（Rezk 条件“同构即相等”蕴含此性质）：回路必须不可逆（C-35）；
- 不满足此性质的目标（两个对象之间只有一对互逆箭头，余离散）：可逆回路即可（C-36）；
- 满足此性质、又有先升后降的目标存在：行走的收缩（C-37）；
- 抽象冻结：读数类型若对“旅程形状” J 是零化的（常值映射 R → (J → R) 为等价），读数沿每段旅程两端相等（C-38）。

数学内容都是标准事实，**不主张原创**。

## 命题全文

记号：`Target` 记录含 `Ob : Type`、`Hom : Ob → Ob → Type`、`idA`、`_⋆_`（按“先…后…”的顺序复合）。在 `Readings T` 中：
`UpThenDown = Σ[ a ∈ Ob ] Σ[ b ∈ Ob ] (¬ (a ≡ b)) × Hom a b × Hom b a`；
`InversePair f g = ((f ⋆ g) ≡ idA a) × ((g ⋆ f) ≡ idA b)`；
`ArrowsCollapse = ∀ a b → Hom a b → a ≡ b`；`Antisymmetric = ∀ a b → Hom a b → Hom b a → a ≡ b`；
`InversePairsCollapse = ∀ a b (f : Hom a b) (g : Hom b a) → InversePair f g → a ≡ b`。

| claim | 命题（量词与假设照实写） | 源码符号 |
|---|---|---|
| **CG001-C-34**（离散或反对称的目标冻结先升后降） | 对任意 `T : Target`：`ArrowsCollapse → ¬ UpThenDown`；`Antisymmetric → ¬ UpThenDown`。 | `Readings.collapseFreezes`、`Readings.antisymmetryFreezes` |
| **CG001-C-35**（互逆对塌缩时回路必不可逆） | 对任意 `T`：`InversePairsCollapse → ∀ a b → ¬ (a ≡ b) → ∀ (f : Hom a b) (g : Hom b a) → ¬ InversePair f g`。 | `Readings.cycleNotInvertible` |
| **CG001-C-36**（余离散目标：可逆回路） | `codiscrete`（`Ob = Bool`，`Hom _ _ = Unit`）：`UpThenDown`（取 `true , false`）；该对箭头 `InversePair`；`¬ InversePairsCollapse`。 | `codiscrete`、`codiscreteUpThenDown`、`codiscreteCycleInvertible`、`codiscreteDoesNotCollapse` |
| **CG001-C-37**（行走的收缩：互逆对塌缩，仍能先升后降） | `walkingRetraction`（对象 `true`=A、`false`=B；`Hom A A = {idAA, idem}`，其余 `Hom` 为 `Unit`，即 f : A → B、g : B → A、id_B；“f 后 g”为 `idem`，“g 后 f”为 id_B）满足单位律 `wIdL`、`wIdR` 与结合律 `wAssoc`（是一个范畴）；`InversePairsCollapse`；`UpThenDown`（取 `true , false , f , g`）；`¬ InversePair f g`。负控制：以 `refl` 证明“f 后 g”等于 `idAA`，内核拒绝（`idem != idAA`）。 | `EndA`、`WHom`、`wid`、`wcomp`、`wIdL`、`wIdR`、`wAssoc`、`walkingRetraction`、`retractionCollapsesInversePairs`、`retractionUpThenDown`、`retractionCycleNotInvertible`；负控制 `WrongInversePair.agda` |
| **CG001-C-38**（抽象冻结） | 对任意类型 `J`、点 `j0 j1 : J`、类型 `X`、`R`：若 `constMap : R → (J → R)`（`constMap r _ = r`）是等价，则对任意 `T : X → R` 与 `γ : J → X`，`T (γ j0) ≡ T (γ j1)`。 | `Freeze.constMap`、`Freeze.frozenAlongJourney` |

## 与有向类型论的桥（来源陈述，本项目未重放）

- Gratzer、Weinberger、Buchholtz，*Directed univalence in simplicial homotopy type theory*（arXiv:2407.09146）：
  - 定义 2.2 hom 类型；定义 2.5 Segal；定义 2.7 同构；定义 2.8 Rezk（IdToIso 为等价）；定义 2.10 与引理 2.11：群胚（𝕀-零化）等价于“每个箭头都可逆的范畴”；
  - 公理 6（𝕀 检测离散性）、公理 7（𝕀 的全局点只有 0、1 且 0 ≠ 1）；
  - 推论 3.20：在其 triangulated type theory（TT_□）中，Nat 与 Bool 是 𝕀-零化的，即群胚；
  - 引理 3.7（Phoa 原理）：𝕀 → 𝕀 的映射由端点对 (a ≤ b) 决定，因此 𝕀 值读数沿箭头单调；
  - 推论 3.13：Δⁿ 是范畴，作者称这是该系统中第一个显式构造的非离散范畴；摘要称构造了单纯类型论中第一批有非平凡同态的类型（离散类型的宇宙 S，且 S 满足有向单价：hom_S(A,B) ≃ (A → B)）。
- Riehl、Shulman，*A type theory for synthetic ∞-categories*（arXiv:1705.07442）：Segal 类型与 Rezk 类型的定义；Segal 类型之间的函数自动保持复合与恒等（经 GWB §2.1 转述）；离散类型（idtoarr 为等价）是 Segal 类型（命题 7.3），离散当且仅当 Rezk 且所有箭头可逆（命题 10.10），两处编号经 Bardomiano Martínez（MSCS 2025）转引，未直接读 RS17 原文。

对应（解释）：`ArrowsCollapse` 对应离散类型（如 TT_□ 中的 Nat、Bool）；`Antisymmetric` 对应偏序式目标（如 𝕀）；`InversePairsCollapse` 对应 Rezk 类型（如 S、Δⁿ）；余离散对应不完备的 Segal 结构（其在 sHoTT 或 TT_□ 内部能否构造为类型：未核）；行走的收缩对应 S 中 Bool → Unit → Bool 这样的回路（A = Bool、B = Unit：“g 后 f”是 Unit 上的恒等，“f 后 g”是 Bool 上的常值幂等映射，不是恒等）。C-38 取 J 为有向区间、R 为 Nat 时，结论要借 GWB 推论 3.20（TT_□，来源报告）。

## 禁止外推

- 这是对象、箭头、复合层面的模型（加一条抽象引理），不是单纯类型论或 TT_□ 的原生证明；与它们的对应是解释，依赖上面的来源陈述。
- C-38 对任意 J 成立；把它用到 sHoTT 的有向区间与 Nat 上，依赖 GWB 推论 3.20（只在 TT_□ 中陈述）。在 RS17 的 sHoTT 中 Nat 是否可证离散：未核（在其预期模型中离散类型解释为常值单纯空间）。
- 不说有向理论不能表示先升后降：C-36、C-37 给出了能表示的目标；也不说温度计的读数“应当”取哪一类目标，那是建模选择。
- 行走的收缩只验证了单位律与结合律；没有另证 hom 为集合，也没有证完整的 Rezk 条件（只证 `InversePairsCollapse`，它是 Rezk 条件的推论）。
