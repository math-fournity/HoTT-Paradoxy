# B 的两个成因：A 与单价性一起让追问永不停，去掉任一条就停（C-430）

> HUMAN_EDITED；2026-10-15；Claude Code 桌面会话 95a1a81b（012-Opus），目标包 CG-010 的移交清单 H2；独立 worktree `claude/012-opus-w8`。
>
> **起因**：研究发起人 2026-10-15 的裁定 D4（与 GLM 会话逐站裁定；权威记录 `.claude/goals/CG-010-remaining-formalization-alignment/待你裁定-人话版/10-裁定结果-20261015.md`，逐字转录同目录 `11-会话GUI转录-20261015.md`）。研究发起人在界面问答里选的是：
> - D4-1“‘ZFC-1 导致 B’的‘导致’”：选“动作＋定理（推荐）”。选项原文：“定理层：‘A＋单价性⟹B，去任一条则停’合成一条可证定理；动作层：‘同一个 A 在两边’作为经你认可的读法写进叙事。”
> - D4-2“哪一条是非现实的抽象”：选“现成的收集（推荐）”。
> - D4-3“成因写 A＋单价性，被告仍为 A”：选“同意（推荐）”。
>
> 裁定记录的总口径：“ZFC-1 导致 B ＝ 同一个动作 A 在两边（读法，经认可）＋ 定理 A∧单价性⟹B（待合成）＋ 被告为 A、单价性入成因（裁定）。”本包合成的就是其中的定理。
>
> - proof id：主包 `MP-CG001-A-UNIVALENCE-B-001`（`AUnivalenceB.agda`）；负控制 `-NEG-001` 至 `-NEG-003`（见“负控制”一节）。
> - claim：`CG001-C-430`。
> - 工具链：Agda 2.8.0 + cubical 0.9，本机 macOS 记录 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`；`--safe --cubical --guardedness`，不假定任何东西。
> - 依赖（全部导入，不重抄）：
>   - `../pedometer-semantics/PedometerSemantics.agda`、`DelayMonad.agda`（C-55、C-59：`Delay`、`never`、`runFor`）；
>   - `../universe-questioning/UniverseHasNoLevel.agda`（C-75：`K`、`sec`、`secNontrivial` 与环路引理 `Ω^suc`、`hLevelΩ^`、`Πpt`、`ΩΠpt`、`Ω^Πpt`、`ΩEquiv≡ΩFun`）；
>   - `../questioning-delay/QuestioningDelay.agda`（C-77、C-79：追问程序 `question`、`Questioning`、`judgeℕ`、`Gathering`、`gatheringStopsAt`、`gatheringSilentBefore`、`gatheringJudge`）。
> - 标签：`FORMAL_B_NEEDS_A_AND_UNIVALENCE_FOR_EVERY_COLLECTION_WITH_FOUR_WITNESSES`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §61（GOAL_LOCAL_INDEX_ONLY）。

## 任务

把裁定里的那句话写成一条定理，对**每一个**收集都成立，并在一个检查单元里检查：

> 如果把所有高度一次交出的东西当成一个对象，并且相同是结构，那么对它的“是不是同一个”的追问永不停；去掉其中任何一条，追问就会停。

用到的词（都在 `AUnivalenceB.agda` 里定义）：

- **收集** `Collection`：一个编码的类型 `Code`，加上每个编码所指的成员 `El a`。宇宙是一个收集：编码就是类型，成员就是它自己。
- **相同是结构** `Univalent C`：两个编码以什么方式相同，恰好就是它们的成员之间的一一对应（把编码的路径送到成员的等价，这个映射是等价）。这就是单价性，写成对任意收集的条件。
- **相同是事实** `SamenessIsFact C`：编码组成一个集合。两个编码是不是同一个，只有“是”或“不是”，没有“以什么方式”。
- **所有高度一次交出（A）** `AllHeights C`：对每一个 n，收集里已经有一个成员，它的 (1+n) 层相同不平凡，而且在它的每一点上都一致地不平凡（一条不等于平凡截面的截面）。
- **高度有上限** `HeightsBoundedBy k C`：每个成员都在 h-层 k 落定。
- **追问程序**：C-77 的 `question (Code C) judge`。第 k 问问“编码在第 k+1 层落定了吗？”，答“是”就停，答“否”就问下一问。

## 命题全文：C-430（`AUnivalenceB.agda`）

- **(1) 两个成因都在：追问永不停。** 对任意收集 C，若 `Univalent C` 且 `AllHeights C`：
  - `UnivalentCollection.noFiniteLevel`：对一切 m，`Code C` 不在 h-层 m；
  - `UnivalentCollection.neverWithBoth`：对任意判定器，`question (Code C) judge ≡ never`。
  - 机制是一般化了的局部—整体环路原理 `UnivalentCollection.localGlobal`：`Ω^(2+n)(Code, a) ≃ Π (x : El a), Ω^(1+n)(El a, x)`。单价性把成员内部的相同提升一层，成为收集自身的相同。C-75 对宇宙证过同一个原理，这里只把“宇宙的单价性”换成“收集的单价性”这一条假设。
- **(2) 去掉 A（保留单价性，高度有上限）：追问停。** 若 `Univalent C` 且 `HeightsBoundedBy k C`：
  - `boundedSettles`：`Code C` 在 h-层 k+1 落定；
  - `haltsWithBound`：对任意判定器，追问停机（`Questioning.Halts`）。
- **(3) 去掉单价性（保留 A，相同换成事实）：第 1 问就停。** 若 `SamenessIsFact C`：
  - `factStopsAtOne`：对任意判定器，`runFor 0 (question (Code C) judge) ≡ just 1`，与成员是什么无关。
- **(4) 倒过来读：追问永不停，就两个成因都在。** 对任意判定器，若 `question (Code C) judge ≡ never`：
  - `neverNeedsUnbounded`：若 C 单价，则对一切 k，成员高度没有上限 k；
  - `neverNeedsStructure`：编码的相同不是事实。
- **(5) 三个见证：每一条都真的被满足，三个条款都不是空话。**
  - **(5a) 宇宙，两个成因都在。**
    - `universeUnivalent`（库里的单价性）；
    - `universeAllHeights`：成员 `K n = EM ℤ (1+n)`，截面 `sec n`（C-75）；
    - 于是 `universeNoLevel` 与 `universeNever` 经 (1) 重新得到 C-75、C-78；
    - 内核实跑：`universeKernel1000 : runFor 1000 (question (Type ℓ-zero) judgeViaB) ≡ nothing`（`refl`），判定器 `judgeViaB` 的每个“否”都来自 (1)。
  - **(5b) 1+n 层落定者的汇集，只有单价性、没有 A。**
    - `gatheringUnivalent`（经 `isEmbeddingFstΣProp` 与库里的单价性）、`gatheringBounded`；
    - 经 (2) 得 `gatheringSettles` 与 `gatheringHalts`；
    - 恰好第 1+n 问停（C-79 (b) 的 `gatheringStopsAt`、`gatheringSilentBefore`，导入）；
    - 内核实跑：`gatheringKernelSets : runFor 1 (question (Gathering 1) (gatheringJudge 1)) ≡ just 2`（`refl`）。
  - **(5c) 编号的 Eilenberg–MacLane 收集，只有 A、没有单价性。**
    - 编码是自然数 ℕ，第 n 个成员是 `K n = EM ℤ (1+n)`：
      - `numberedAllHeights`：成员与宇宙那一行完全相同，所有高度一次交出；
      - `numberedFact`：编码的相同是事实（ℕ 是集合）。
    - 经 (3) 得 `numberedStopsAtOne`：第 1 问就停。
    - 经 (1) 得 `numberedNotUnivalent`：它不单价；若单价，ℕ 就没有有限层，与 ℕ 是集合矛盾。
    - 内核实跑：`numberedKernel : runFor 0 (question ℕ judgeℕ) ≡ just 1`（`refl`）。
- **(6) 只是“不单价”不够，相同必须变成事实。** 成对收集 `paired`：编码是 `Type ℓ-zero × Bool`，成员取第一个分量。
  - `pairedAllHeights`：所有高度都在；
  - `pairedNotUnivalent`：它不单价——`(Unit , true)` 与 `(Unit , false)` 的成员相同，编码却不同；
  - `pairedNever`：它的追问照样永不停（`pairedNoLevel`：宇宙是它的收缩，宇宙没有有限层，它也没有）。
  - 原因是它的编码里仍带着宇宙那种“以什么方式相同”的结构。所以 (3) 的条件是“相同换成事实”，不是“单价性不成立”。
- **整体**：`qual-C430` 把 (1)–(6) 写成一个类型，并由一个项居留。

## 负控制

| proof id | 文件 | 断言 | 预期 |
|---|---|---|---|
| `MP-CG001-A-UNIVALENCE-B-NEG-001` | `WrongFactNever.agda` | 只有 A 也有 B：编号收集的追问在第 1 问仍沉默（`refl`） | 被拒：内核实跑，第 1 问答“是”，`just 1 != nothing` |
| `MP-CG001-A-UNIVALENCE-B-NEG-002` | `WrongBoundedNever.agda` | 只有单价性也有 B：集合的汇集在第 2 问之后仍沉默（`refl`） | 被拒：内核实跑，第 2 问答“是”，`just 2 != nothing` |
| `MP-CG001-A-UNIVALENCE-B-NEG-003` | `WrongBWithoutUnivalence.agda` | 拿恒等等价冒充单价性，把 (1) 用到编号收集上，得出“ℕ 没有有限层” | 被拒（类型检查）：恒等是 a ≡ b 到它自己的等价，不是单价性要的“编码路径到成员等价”的映射 |

## 这件事改变了什么（解释，非机器证明）

- 【判断】**裁定里的定理现在是一条，不是四块。**
  - 以前是四个包里分别证的个例：宇宙不停（C-75、C-78）；高度有上限的汇集在那一层停（C-79 (b)）；事实世界第 1 问停（C-80，Lean）；截断第 1 问停（C-83）。
  - 现在是对任意收集的一条定理，加四个见证（(5a)–(5c)、(6)），在一个 `--safe` 检查单元里过核。
- 【判断】**单价性第一次被单独隔离。**
  - CN-046 §3 的表说过：C-80（Lean 的事实世界）是粗粒度对照，“UIP 与单价性不相容，同时压平了所有高阶结构”，“不单独隔离单价性”。
  - (5c) 是细粒度对照：成员与宇宙那一行一模一样，所有高度都在；只把“编码以什么方式相同”从结构换成事实，追问就在第 1 问停。
  - 而且同一条定理 (1) 证明了这个收集不单价。这说明 A 单独不造成 B。
- 【判断】**另一侧也是单独隔离的。** (5b) 保留单价性、只给成员高度设上限，追问在第 1+n 问停（C-79 (b)）。这说明单价性单独不造成 B。
- 【裁定】**成因与被告是两回事。**
  - 定理只说两条都是成因，缺一不可，而且对两条是对称的。
  - 哪一条是非现实的抽象（被告），是研究发起人 2026-10-15 的裁定：现成的收集（A）；单价性入成因，保留。定理不替这个裁定作证，也不与它冲突。
- 【解释】**与研究发起人原话的关系。**
  - KC-000068：“设ZFC-1=ZFC+A，则ZFC-1=ZFC+P，而ZFC-1导致B”。
  - 裁定的读法是：同一个动作 A，在 ZFC-1 一侧给出芝诺的“解决”，在 HoTT 一侧（加上单价性）给出 B。
  - 本包证的是 HoTT 一侧的那一半：A 加单价性恰好造出 B，去掉任一条 B 就消失。“两边是同一个动作”仍是读法（经认可），不是本包的定理。

## 与已有结果的关系（不重复认领）

- (1) 用在宇宙上，重新得到 C-75、C-78。局部—整体环路原理的论证与 C-75 相同，只把“宇宙的单价性”抽成“收集的单价性”这一条假设。
- (2) 用在汇集上，与库里的 `isOfHLevelTypeOfHLevel` 一致。恰好停在哪一问，仍由 C-76 的 `gatheringNeverSettled` 与 C-79 (b) 给出（导入）。
- (3) 是 C-83 (a) 的同一个论证，推广到任意以集合为编码的收集。
- C-81 的无穷乘积是 A 的另一种形态（Π 一次交出所有高度的分量）。它不是“收集”，不是本定理的实例；它的单价性用在 Eilenberg–MacLane 空间的环路计算里，不在收集这一层。
- C-80 的事实世界在 Lean 里，跨内核，这里只引用。

## 元层还剩什么

与 C-77、C-78 相同。把内部定理读成“现实中照这个程序去跑，永远拿不到答案”，需要所用理论一致；对任意闭判定器，还需要典范性。立方类型论（含高阶归纳类型）有立方集合模型【来源转述：Cohen–Coquand–Huber–Mörtberg 2018；Coquand–Huber–Mörtberg 2018】；Agda 全部特性合在一起的一致性，本包不作断言。对 `judgeViaB`，照程序执行不停是语法事实，内核实跑了 1000 步。

## 禁止外推

- **不证明 ZFC-1 ⟹ B。** 本包只证 HoTT 一侧：A 加单价性造出 B，去掉任一条就停。“同一个动作 A 在 ZFC-1 一侧给出芝诺的解决”是另一侧，有自己的收据（C-423、C-428）。“两边是同一个动作”是经认可的读法，不是定理。
- **“被告是 A”是裁定，不是定理。** 定理对两个成因是对称的。
- **“去掉单价性”写成“编码的相同是事实”，不是“不单价”。**
  - 一个不单价、编码却另有高阶结构的收集，追问照样可以不停，(6) 机器证明了一个例子。
  - 所以 (3) 说的是“相同换成事实就停”，与 C-80、C-83 的写法一致，不是“只要不单价就停”。
- **“去掉 A”写成“成员高度有上限”。** `AllHeights` 要求每一层都有一条处处不平凡的截面，这是局部—整体原理需要的形状；只在一点处不平凡的成员，不在 (1) 的范围内（乘积那一形态见 C-81）。
- 不证明 HoTT 不一致，不证明宇宙或任何收集“不存在”。
- 用到高阶归纳类型（Eilenberg–MacLane 空间）。“现成的收集是非现实的”所需的解释桥与现实侧前提，由研究发起人的裁定承担，本包不改变它们的身份。
- 判定器立即作答；不停机来自问的层数没有顶，不来自某一问难答。`≡ never` 只经有限燃料的运行来读（C-59 (c)），不是墙钟时间、真实设备或证明助手运行时间的陈述。
- 数学内容标准：局部—整体环路原理与单价的 n-型宇宙是 (n+1)-型，都是 HoTT 的已知结果（Kraus–Sattler 2015 等），**不主张原创**。本仓库新增的是两件：
  - 把裁定里的定理对任意收集写成一条，在一个检查单元里检查；
  - 用编号收集把单价性单独隔离出来。
- 运行只在本机 macOS 上捕获与重放，没有在第二个平台重放。

## 运行

- 主包：`HoTT/verification/runs/20261015-CG001-A-UNIVALENCE-B-01`。
- 负控制：`20261015-CG001-A-UNIVALENCE-B-NEG-01` 至 `-NEG-03`（与上表 NEG-001 至 NEG-003 依次对应）。
- 捕获工具：`.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_macos_run.py`；核对：`verify_cg001_run.py --rerun`。
