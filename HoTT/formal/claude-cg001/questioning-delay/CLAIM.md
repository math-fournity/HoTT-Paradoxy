# 过程 Q 写成带判定器的程序：宇宙上它等于 never（C-77 至 C-80）

> HUMAN_EDITED；2026-09-30；Claude，云端会话 01FJANnV。
>
> 起因：用户【原话】（2026-09-30，本会话）：
>
> > 把“追问永不停机”从元层推论写进内核，做法是把逐层追问写成带判定器的 Delay 程序，证明它永远停不下来。
>
> 候选登记：CN-045（【建议】）；根 `README/006 - 后续候选前缘.md` 第 2 节第 3 组。对齐检查与过程记录：`.claude/explore/20260930-追问Delay程序-工作台.md`。
>
> - proof id：
>   - 主包：`MP-CG001-QUESTIONING-DELAY-001`（`QuestioningDelay.agda`）；
>   - Agda 负控制：`MP-CG001-QUESTIONING-DELAY-NEG-001` 至 `-NEG-004`（下文“负控制”一节）；
>   - Lean：`MP-CG001-QUESTIONING-DELAY-LEAN-001`（`../questioning-delay-lean/QuestioningLean.lean`），其负控制 `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001`。
> - claim：`CG001-C-77`、`CG001-C-78`、`CG001-C-79`（Cubical Agda）；`CG001-C-80`（Lean 4）。
> - 工具链：
>   - Agda 2.8.0 + cubical 0.9（Linux 记录 `HoTT/formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`），`--safe --cubical --guardedness`，无公设；
>   - Lean 4.34.0（`HoTT/formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`），全部定理不依赖任何公理（`#print axioms`），另用 `leanchecker --fresh` 重放。
> - 依赖（全部导入，不重抄）：
>   - `../pedometer-semantics/PedometerSemantics.agda`（C-55：`Delay`、`never`、`runFor`、无界搜索 `StopProgram`）；
>   - `../pedometer-semantics/DelayMonad.agda`（C-59：`return`，以及“等于 never 当且仅当任何燃料都得不到结果”）；
>   - `../universe-questioning/UniverseHasNoLevel.agda`（C-75、C-76：`universeHasNoLevel`、`gatheringNeverSettled`）。
> - 标签：`FORMAL_QUESTIONING_PROGRAM_NEVER_HALTS_ON_UNIVERSE_WITH_SCOPE`。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §20（GOAL_LOCAL_INDEX_ONLY）。

## 任务

- **过程 Q**（社区稿 02 第 3.1 节的伪代码）：从第 1 问开始；第 k 问问“目录 C 的相同在第 k+1 层落定了吗？”（`isOfHLevel (k+1) C`）；得到“是”的证明，停止并交出 k；得到“否”的证明，走一步，问第 k+1 问。
- **判定器**：`Judge C = (k : ℕ) → Dec (isOfHLevel (suc k) C)`。每一问都交出“是”的证明或“否”的证明。判定器对每一问立即作答；程序里唯一的“走一步”在两问之间。
- **程序**：
  - `askFrom k .force = answer k (judge k)`；
  - `answer k (yes _) = now k`；
  - `answer k (no _) = later (askFrom (suc k))`；
  - `Q = askFrom 1`。
  写法与 C-55 的无界搜索相同，`Delay` 类型从 C-55 导入。区别只在停机条件可以住在任意宇宙层：C-55 的 `StopProgram` 要求停机条件在最低宇宙，而宇宙本身的停机条件 `isOfHLevel (k+1) (Type ℓ-zero)` 在下一层宇宙。
- **完成标准**：程序返回 `now k`，即交出落定的一层。运行语义沿用 C-55、C-59：`runFor n` 是给 n 步燃料的有限运行。
- **计数约定**：社区稿说的“第 1 步停”“第 2 步停”，指第 1 问、第 2 问答“是”；从第 1 问开始时，“第 k 问停”就是燃料 k−1 时返回 k。

## 命题全文

### C-77：程序本身（对任意目录 C、任意判定器）

- **(a) 燃料方程**：
  - `runYes`、`runNoZero`、`runNoSuc`：答“是”时返回 k（不论燃料多少）；答“否”且燃料为 0 时返回 `nothing`；答“否”且燃料为 n+1 时，等于从第 k+1 问起给燃料 n 的运行。三条都是 `refl`。
  - 用事实代替判定器的答案，得到同样的三条：`settledAt`、`notSettledAtZero`、`notSettledAt`。所以运行只取决于 C 在该层是否落定，与用哪个判定器无关。
- **(b) 输出可靠**：`sound`：若 `runFor n (askFrom k) ≡ just j`，则 `isOfHLevel (suc j) C`。
- **(c) 停机恰好是“在某个有限层落定”**：
  - `haltsToLevel : Halts → HasLevel`，`levelToHalts : HasLevel → Halts`，其中 `Halts = Σ n Σ j (runFor n Q ≡ just j)`，`HasLevel = Σ m (isOfHLevel m C)`；
  - `noLevelToNever : ((m : ℕ) → ¬ isOfHLevel m C) → Q ≡ never`；
  - `neverToNoLevel : Q ≡ never → (m : ℕ) → ¬ isOfHLevel m C`。
- **(d) 精确停机时刻**：
  - `exactHalt`：若 C 在第 k+1 至 k+n 层都不落定、在第 k+n+1 层落定，则从第 k 问起、燃料 n 的运行返回 k+n；
  - `silentUpTo`：若 C 在第 k+1 至 k+n+1 层都不落定，则从第 k 问起、燃料 n 的运行返回 `nothing`。
- **(e) 与 C-55 是同一个搜索**：`SameAsC55.QIsSearchFromOne`：对最低宇宙里的目录，Q 等于 C-55 的 `StopProgram`（停机条件“在第 k+1 层落定”）从 1 开始的搜索（余归纳的路径）。

### C-78：宇宙

- **(a) 永远停不下来**：对任意判定器 `judge : Judge (Type ℓ-zero)`：
  - `universeQuestioningIsNever`：`question (Type ℓ-zero) judge ≡ never`；
  - `universeQuestioningRunsNothing`：对一切燃料 n，`runFor n (question (Type ℓ-zero) judge) ≡ nothing`；
  - `universeQuestioningNeverAnswers`：`¬ Halts`，即不存在燃料 n 与层 j 使运行返回 j。
- **(b) 判定器存在且唯一**：
  - `judgeU k = no (universeHasNoLevel (suc k))`：每一问都答“否”，每个“否”带着 C-75 的证明；
  - `judgesAreEqual`：判定器的类型是命题；`everyJudgeIsJudgeU`：任何判定器都等于 `judgeU`。
- **(c) 内核实跑**：`kernelRuns1000`：`runFor 1000 (question (Type ℓ-zero) judgeU) ≡ nothing`，由 `refl` 检查，也就是内核自己把程序展开了 1000 步。
- **(d) 对照：另一个问题**：`whetherSettled` 问“C 在某一层落定吗？”，一步不走就作答。对宇宙，不论这个问题怎样判定，它在燃料 0 答“否”（`universeWhetherAnswersNo`：`runFor 0 (whetherSettled (Type ℓ-zero) d) ≡ just false`）。

### C-79：同一个程序在“成员高度有上限”的目录上

- **(a) ℕ 与 Bool**：对任意判定器，Q 在第 1 问停下并返回 1（`naturalsStopAtOne`、`boolsStopAtOne`：燃料 0 即 `just 1`）。判定器存在（`judgeℕ`、`judgeBool`）。
- **(b) 落定层数有上限的目录**：`Gathering n = TypeOfHLevel ℓ-zero (1+n)`，即 h-层为 1+n 的类型的目录。
  - `gatheringStopsAt`：对任意判定器，燃料 n 的运行返回 1+n；
  - `gatheringSilentBefore`：燃料小于 n 的运行都返回 `nothing`；
  - 所以 Q 恰好在第 1+n 问停下。命题的目录第 1 问停（`propsStopAtOne`），集合的目录第 2 问停（`setsStopAtTwo`）。
  - 判定器存在（`gatheringJudge n`）。
  - 用到 C-76 的 `gatheringNeverSettled` 与库的 `isOfHLevelTypeOfHLevel`。

### C-80：事实世界（Lean 4，`QuestioningLean.lean`）

- Lean 的内核没有余归纳类型，所以同一个过程直接写成它的有限燃料运行 `runFrom`，定义就是 C-77 (a) 的三条燃料方程（`runYes`、`runNoZero`、`runNoSucc` 把它们作为定理重述）；判定器的形状相同：每一问都是对“在第 k+1 层落定”的判定。
- h-层沿用 cubical 库 `isOfHLevel` 的三条子句。Lean 的相等是命题，恒等类型的层数在 `IsOfHLevelProp` 中继续；第 0 层用存在量词，即 `isContr` 的命题形式。Q 从第 1 问开始，不会用到第 0 层。
- **结论**：`higherLevels`：每个类型在第 2 层及以上都落定，宇宙 `Type` 也不例外（与 C-72 同源）。所以：
  - `universeStopsAtOne`：对任意判定器与任意燃料，`question Type judge fuel = some 1`；
  - `everyTypeStopsAtOne`：对任何类型都一样。
- 判定器存在（`judgeType`：第 0 问答“否”，因为 `Unit` 与 `Empty` 是不同的类型；第 1 问起答“是”）；`kernelComputesOne`：`question Type judgeType 0 = some 1` 由 `rfl` 检查。

## 负控制

| proof id | 文件 | 断言 | 预期 |
|---|---|---|---|
| `MP-CG001-QUESTIONING-DELAY-NEG-001` | `WrongUniverseAnswersEarly.agda` | 宇宙的追问用 `judgeU`、燃料 1 就返回 1（`refl`） | 被拒：内核实跑，得 `nothing != just 1` |
| `MP-CG001-QUESTIONING-DELAY-NEG-002` | `WrongNaturalsSilent.agda` | 同一程序在 ℕ 上、燃料 0 沉默（`refl`） | 被拒：`just 1 != nothing` |
| `MP-CG001-QUESTIONING-DELAY-NEG-003` | `WrongSetsStopAtOne.agda` | 集合的目录第 1 问就停（`gatheringJudge 1`，`refl`） | 被拒：`nothing != just 1` |
| `MP-CG001-QUESTIONING-DELAY-NEG-004` | `WrongNeverByRefl.agda` | 宇宙的追问等于 `never`，用 `refl` 证 | 被拒：`askFrom … 1 != never`。计算本身看不出程序不停（余归纳记录没有 eta），C-78 (a) 必须用余归纳的证明 |
| `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001` | `../questioning-delay-lean/WrongLeanUniverseSilent.lean` | 在 Lean 里，宇宙的追问在燃料 0 沉默（`rfl`） | 被拒：`question Type judgeType 0` 与 `none` 不定义相等（它归约为 `some 1`） |

## 这件事改变了什么（解释，非机器证明）

- 【判断】**“永不停机”从元层推论变成内部定理。** 之前，社区稿 02 第 5 节的推理是：C-75（每一层都否）加上 Q 的定义（写在理论外面的伪代码），再加上一致性，推出 Q 不停。现在：
  - Q 是理论里的一个对象（C-77）；
  - “Q 在宇宙上等于 `never`”由内核检查（C-78 (a)）；
  - 按 C-59 (c)，这恰好等于“任何有限步的运行都得不到结果”。
- 【判断】**程序忠实于 Q，不是只会不停的程序。** 停机恰好刻画为“在某个有限层落定”（C-77 (c)），而且同一个程序该停处都停：
  - ℕ、Bool 第 1 问停（C-79 (a)）；
  - 集合的目录第 2 问停，h-层 1+n 的目录第 1+n 问停（C-79 (b)）；
  - Lean 里的宇宙第 1 问停（C-80）。
  所以宇宙上的 `never` 来自宇宙本身，不来自程序的写法。
- 【判断】**停机时刻跟着成员高度的上限走。** 成员的相同层数以 1+n 为上限的目录，Q 在第 1+n 问停；宇宙的成员没有上限，Q 不停。社区稿 02 第 4 节说“最干净的一级是第二级和第三级之间：只差成员的高度有没有上限”，现在它是同一个程序的一族实例，另加一个极限情形。
- 【判断】**两个问题，两种完成标准。** “哪一层落定？”（Q）在宇宙上永远交不出答案；“有没有一层落定？”（`whetherSettled`）一步不走就答“没有”（C-78 (d)）。后者给出的是 Q 永不停的证书，不是 Q 的完成。这把社区稿 02 第 5 节“必须正面回答的反驳”写成了两个程序的对照。
- 【解释】**与用户原意的关系**（KC-000016：“如果你把S的构造过程写成程序，那么S的构造是无法完成的”；KC-000050、KC-000051）：程序的视角现在进入了 HoTT 内部。HoTT 里同时有两样东西：
  - 一条形成规则，一次交出 `Type ℓ-zero : Type (ℓ-suc ℓ-zero)`；
  - 一条内核检查过的定理：追问宇宙落定于哪一层的程序等于 `never`。
  两者并存，不是矛盾，也不是不一致。把它读作“绕过 ASK，当作已经完成”（B 方向），要经过解释桥（P1）与现实侧前提（P2），这两道门本包不改变。

## 内化之后，元层还剩什么

- 【判断】内部定理说的是：对这个程序，任何有限燃料的运行都返回 `nothing`。把它读成“现实中照这个程序去跑，永远拿不到答案”，还需要元层的两件事：
  - **所用理论一致**：否则它也能证明相反的命题。立方类型论（含高阶归纳类型）有立方集合模型【来源转述：Cohen–Coquand–Huber–Mörtberg 2018；Coquand–Huber–Mörtberg 2018】；Agda 全部特性合在一起的一致性，本包不作断言。
  - **对任意的闭判定器，还需要闭项算到典范形**（典范性）：核心立方类型论已有证明【来源转述：Huber 2019】；含高阶归纳类型的 Cubical Agda 全部特性是否有，本包不断言。
- 【判断】对本包的判定器 `judgeU`，照程序执行不停是语法事实：它每一问都给出“否”，每一步都是定义展开，内核实跑检查了 1000 步（C-78 (c)）。需要一致性的，是“这些‘否’都是对的”，即不存在正确的“是”。
- 所以 CN-045 预期的“剩下的元层部分只是‘所用理论一致’”基本成立，精确地说是一致性，外加对任意判定器的典范性。解释桥与现实侧前提不在此列，它们从来不是机器能回答的问题。

## 禁止外推

- 不证明 HoTT 不一致，也不证明“宇宙不存在”。本包证明的是：追问宇宙落定于哪一层的程序等于 `never`。
- “存在性追问 = 这个过程”是解释桥（社区稿 02 第 12 节 P1）；“一个总体要算存在，它的相同必须在某一层落定”是现实侧前提（P2）。两者待研究发起人裁定，也交社区判断；本包不改变它们的身份。
- `≡ never` 说的是这个程序在这个运行语义下的性质。`never` 是一个整体给出的余归纳对象，本包只经有限燃料的运行来读它（C-59 (c)）。它不是墙钟时间、真实设备或证明助手运行时间的陈述。
- 判定器立即作答。不停机来自问的层数没有顶，不来自某一问难答。耗时的判定器（`ℕ → Delay (Dec …)`）没有建模：C-55 的 `Delay` 只接受最低宇宙里的值，而宇宙的判定结果在下一层宇宙。
- 宇宙上的结论经 C-75 用到高阶归纳类型（Eilenberg–MacLane 空间）。没有高阶归纳类型时，落不定的主语是宇宙塔（Kraus–Sattler 定理 5.9，运行 `20260927-COPUS-KS-UNIVERSE-TOWER-01`），本包没有为它写程序。
- C-80 是有限燃料语义的转写：两个系统里的程序由同一组方程定义，但本包不证明它们是跨系统的同一个对象。Lean 一侧只陈述集合层面的事实。
- 数学内容标准：Capretta 风格的无界搜索，加上 C-75、C-76 的 h-层事实，技术上**不主张原创**。本仓库新增的是：把过程 Q 做成理论内部的对象，以及把三级阶梯写成同一个程序的实例。

## 运行

- 主包：`HoTT/verification/runs/20260930-CG001-QUESTIONING-DELAY-01`。
- Agda 负控制：`20260930-CG001-QUESTIONING-DELAY-NEG-01` 至 `-NEG-04`（与上表 NEG-001 至 NEG-004 依次对应）。
- Lean：`20260930-CG001-QUESTIONING-DELAY-LEAN-01`；负控制 `20260930-CG001-QUESTIONING-DELAY-LEAN-NEG-01`。
- 捕获工具：`.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_linux_run.py` 与 `capture_cg001_lean_linux_run.py`（由 Cloud-Opus 的捕获工具派生，差异写在文件头）；核对：`verify_cg001_run.py --rerun`。
