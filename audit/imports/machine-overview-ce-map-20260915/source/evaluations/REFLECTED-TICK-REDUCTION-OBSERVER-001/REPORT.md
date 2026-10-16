# 反射、forcing tick 与证明检查完成性：冻结实验报告

> Evaluation：`REFLECTED-TICK-REDUCTION-OBSERVER-001`  
> Evidence status：`FORMAL_EXECUTION_REPLAYED_WITH_SCOPE`  
> HoTT 非现实性结论：`NOT_ESTABLISHED`  
> Gödel 结论：`GENERIC_SELF_REDUCTION_CALIBRATION_ONLY`  
> 运行日期：2026-09-14  
> 工作树：`/Volumes/D/HoTT-machine-overview`  
> 分支：`feat/machine-overview-m1`  
> 运行基线 HEAD：`1aa1a6e32c0f59459f79ebc76f74e8f2b5be97a5`

## 1. 研究问题

这项评价把两个此前容易混在一起的问题放入同一组冻结对照中：

1. 精确历史 CCTT Agda 检查器的 Reflection 能否在宏调用位置观察普通 tick 与 forcing tick 的不同归约行为？这种调用位置的语法观察能否被提升为尊重对象层 Path 的统一观察函数？
2. 在同一检查器中，若一个自递归项被显式声明为可参与判断性归约，证明检查是否会因被迫求取不同规范形而在固定观察窗内不完成？这能否成为 HoTT 非现实性悖论或 Gödel 不完备性的实例？

评价预先冻结了 14 个问题、4 组来源、9 个源文件、5 棵源码树、23 个文字锚点、10 个原生探针、两个资格门和一组三因素因果模型。正式运行之前，未来探针路径均不存在；探针、来源与解释边界随后由 `FREEZE.json` 和 `DECISIONS.json` 绑定。

## 2. 直接结果

全部 10 个探针的首轮与重放均满足冻结预期，退出状态、标准输出和标准错误逐字节一致；2026-09-14 的独立 `verify --rerun` 又执行了全部 10 个探针，分类和逐字节输出再次一致。

| 探针 | 固定问题 | 结果 | 首轮 / 重放耗时 |
|---|---|---|---|
| `P01` | Reflection 在直接调用位置区分归约形 | 内核接受 | 2308 / 2209 ms |
| `P02` | 把该区分提升为同一路径两端的对象层结论 | 类型规则拒绝：`true` 与 `false` 不同 | 2148 / 2135 ms |
| `P03` | quotation/unquotation 重建普通 tick 与 forcing tick binder | 内核接受 | 1929 / 1972 ms |
| `P04` | 普通终止性审查面对直接自递归 | 有限拒绝 | 911 / 964 ms |
| `P05` | 受约束片段中手工声明递归项可终止 | 有限拒绝 | 907 / 901 ms |
| `P06` | 显式终止断言后的自递归项与自身比较 | 内核接受，没有被迫求取不同规范形 | 956 / 903 ms |
| `P07` | 同一递归项被迫与不同规范形比较 | 4 秒观察窗内未完成，退出 124 | 4640 / 4723 ms |
| `P08` | 保持递归定义对类型检查不透明，再比较不同规范形 | 有限类型拒绝，不展开循环 | 927 / 909 ms |
| `P09` | guarded 生产性无限流的 Reflection 规范化 | 在 delay 边界完成 | 1935 / 1916 ms |
| `P10` | Reflection `normalise` 显式可展开的自递归项 | 4 秒观察窗内未完成，退出 124 | 4604 / 4611 ms |

运行的确定性摘要为：

```text
FREEZE deterministic SHA-256:
d5ee4fe9470a3ad9c75833d35672bbc0bd746d50270d7f33ffd86f5c73baa1d4

DECISIONS deterministic SHA-256:
ccdbf2d18d899894fa98a42df9696bc68e4663c4625e8307739ad5bb06d9409f

RUN deterministic SHA-256:
ba808d367c2e19feb81215a72188832a82508c4d46e1db655567bf2e26cb8347
```

这些摘要只绑定确定性内容；墙钟耗时和生成时间保留在非确定性字段中。

## 3. 反射观察的边界

### 3.1 调用位置确实存在语法/归约差异

宏在具体调用位置对其收到的语法执行 `normalise` 时，可以把 forcing family 的应用判为 `zero`，而普通 tick 下的 `dfix` 项仍未归约到同一形态。直接宏调用因此能生成不同的 Bool 结果。

这个观察属于主机侧对调用位置语法及其规范形的观察。它说明当前 Reflection 接口能够接触到一部分归约差异。

### 3.2 统一对象函数没有保留该差异

把同一宏包装成普通对象层函数时，宏在函数定义处面对的是变量，而不是未来调用位置的具体项；展开后的对象函数成为固定结果。它仍尊重 `force-delay` Path，两端都得到相同 Bool，却不再保留直接调用位置的真假区分。

当探针尝试把直接调用位置得到的 `true` 与 `false` 放入一个所要求的 Path 时，类型规则有限拒绝。由此得到的准确结论是：

```text
HOST_SYNTAX_OBSERVATION_WITH_OBJECT_LEVEL_CONGRUENCE_FENCE
```

即，主机反射能够观察调用位置的语法/归约差异，但本次构造没有把它提升为违反对象层 Path 同余性的统一观察器。

### 3.3 binder 重建是正控制

历史源码的 quotation 路径留有 annotation 相关注释，而 unquotation 使用默认 annotation。尽管如此，`Tick k` 与 `FTick k` 的反射类型信息足以让宏通过 `getType`、`getDefinition`、`declareDef` 和 `defineFun` 重建普通 tick 与 forcing tick binder 的行为；两个克隆定义均通过内核检查。

因此，“annotation 字段没有完全按同一方式往返”本身没有在本评价中形成 binder 行为丢失。它是一个已通过的重建正控制，不能写成缺陷实例。

## 4. 证明检查非完成的三因素因果模型

正式探针支持以下最小三因素组合：

1. `SELF_RECURSIVE_TERM`：存在直接自递归项；
2. `TERM_DECLARED_AVAILABLE_TO_JUDGEMENTAL_REDUCTION`：该项被显式声明为可参与判断性归约；
3. `PROOF_CHECK_FORCES_A_DISTINCT_NORMAL_FORM`：证明目标迫使它与一个不同规范形比较。

三者共同出现时，`P07` 和通过 Reflection 求规范形的 `P10` 都达到 4 秒观察边界。三项消融给出不同的有限结果：

- 移除自递归项，换成 guarded 生产性无限对象，规范化在 delay 边界完成（`P09`）；
- 不让递归定义参与类型检查归约，比较在有限时间内被拒绝（`P08`）；
- 不要求不同规范形，只检查递归项的自等式，检查在有限时间内完成（`P06`）。

普通终止性审查先于这些探针拒绝直接循环（`P04`）；受约束片段也拒绝手工终止断言（`P05`）。所以当前因果结论不是“该社区框架通常会接受循环项”，而是：

```text
EXPLICIT_TERMINATION_ASSERTION_CAN_MAKE_PROOF_CHECKING_NOT_COMPLETE
```

这正好给方向 B 提供一个控制样本：如果跳过“这个定义是否有终止性依据”的询问，并把它交给判断性归约，后续证明检查可以不完成。但当前框架的通常审查已经阻止了这一步，所以样本尚未展示 HoTT 自身绕过了这一询问。

## 5. 为什么这还不是数学上的“永不终止”结论

两次正式运行和一次独立重跑都只观察到：精确命令在每次 4 秒的边界内没有返回，容器内 `timeout` 以 124 结束进程。这是稳定的运行事实，但不是对所有时间的证明。

若要提升为数学上的非终止性，需要对具体归约关系证明：从目标状态开始，每一步只能继续产生包含同一递归 redex 的状态，且不存在抵达所需规范形的有限序列；或者把该实例归约到已经形式化的发散关系。该证明尚未进入本 repo 的机器证明门禁。因此本报告坚持使用“观察窗内未完成”，而不把 4 秒运行写成永不终止定理。

## 6. 自然消费者扫描

固定源码树中的终止性控制声明清点如下：

| 源码树 | 角色 | 匹配数 | 涉及文件数 |
|---|---|---:|---:|
| Cubical v0.9 | 社区生产源码 | 0 | 0 |
| 历史 guarded/CCTT 源码 | 社区生产源码 | 0 | 0 |
| 当前项目 `HoTT/formal` | 项目证明源码 | 0 | 0 |
| 精确 Agda 检查器测试树 | 检查器测试 | 76 | 53 |
| 精确 Agda examples 树 | 示例 | 3 | 1 |

测试树中的 76 项分为 39 个显式可展开断言、35 个不透明递归声明和 2 个历史声明；examples 树有 3 个显式可展开断言。这个清点证明相关控制在检查器测试与示例中真实存在，但在三个冻结的生产源码树中没有找到自然使用。

因此本评价的 `natural_usage_mismatches` 为空。它不能支持“社区 HoTT 库的正常定理会自然触发同一非完成”的陈述。

## 7. 与两类非现实性方向的关系

### 7.1 方向 A

本评价没有固定一个现实运动或有限活动，再证明 HoTT 表示为它新增了无限完成义务。tick 与 forcing tick 的归约差异属于表示和反射边界；它没有建立“现实过程完成、同任务理论过程不完成”的配对。因此方向 A 在本评价中仍是 `NOT_TESTED_TO_CORRESPONDENCE`。

### 7.2 方向 B

三因素探针具体显示：一旦把未经终止性论证的自递归方程作为可计算定义交给判断性归约，某些证明目标会使检查过程达到观察边界。它清楚说明为什么 ASK——在引入对象时询问其计算合法性、终止性或生产性依据——是决定性的。

但这项见证来自研究者显式改变通常审查结论，不是 HoTT 规则或社区自然消费者自行省略 ASK。方向 B 因此获得的是 `CONTROLLED_MECHANISM_CALIBRATION`，没有获得 `HOTT_INSTANCE`。

## 8. 为什么这不是 Gödel 不完备性实例

一个自递归定义只给出程序层的循环形态。Gödel 不完备性实例还需要至少具备：

1. 固定的对象理论及其递归呈现；
2. 对象语言的语法编码；
3. 可计算替换和对角操作；
4. 对该理论证明关系的表示；
5. 明示的一致性、可靠性或 Hilbert–Bernays–Löb 导出条件；
6. 一个由上述结构得到的对象层定点句；
7. 从精确前提推出不可证性、不完备性或内部一致性限制的机器证明；
8. HoTT/立方结构在构造中不可删除的证据。

当前评价没有定义对象语言、Gödel 编码、证明谓词或对角引理。因而其唯一允许的 Gödel 相关描述是：

```text
GENERIC_SELF_REDUCTION_CALIBRATION_ONLY
```

下一步应借鉴已经机器化的 Coq 与 Isabelle 不完备性工程，先建立对象化义务，而不是继续增加更多手写循环。

## 9. 资格审查

| 等级 | 本评价状态 | 理由 |
|---|---|---|
| `N0 OBSERVATION_LIMIT` | `PASS` | 两个探针在冻结的 4 秒窗内三次一致不完成 |
| `N1 CAUSAL_CONTROLS` | `PASS` | 正常终止审查、受约束片段、不透明递归、自等式、guarded 生产性对象形成对照与消融 |
| `N2 ORDINARY_CONFIGURATION` | `FAIL` | 核心探针依赖显式终止断言 |
| `N3 HOTT_ESSENTIALITY` | `FAIL` | 同类自递归机制不依赖 Path、univalence 或 HIT；没有证明 HoTT 构造不可删除 |
| `N4 NATURAL_CONSUMER` | `FAIL` | 三棵冻结生产源码树中未找到相关自然声明或消费者 |
| `N5 REALITY_CORRESPONDENCE` | `FAIL` | 没有固定同任务的现实活动和观察量 |
| `N6 MACHINE_PROVED_CLAIM` | `FAIL` | 有原生执行证据，没有“永不终止”或 HoTT 非现实性的机器证明 |

综合资格：

```text
REPRESENTATION_BOUNDARY_AND_TERMINATION_CALIBRATION
```

## 10. 对“为什么过去没有找到 HoTT 的问题”的新解释

这项实验提供了一个比“模型没有充分思考”更具体的诊断：过去的搜索经常把三类目标放在一起——制造一个不完成的程序、找到一个证明器实现边界、证明 HoTT 的现实相对非现实性。第一件事很容易；第二件事需要固定版本和因果对照；第三件事还要额外满足 HoTT 必要性、自然消费者和同任务现实对应。

若搜索只优化“让进程不返回”，它会迅速找到人为自递归，却不会提高 HoTT 结论的证据等级。若搜索只在强规范化核心中寻找普通定义的直接循环，终止性与 canonicity/normalization 元理论又会系统性阻止它。真正窄而困难的位置是：

- 核心理论与反射、重写、宏、外部求值或部分性表示的连接处；
- HoTT 构造确实增加计算义务、且该义务由自然消费者触发的位置；
- 对象理论能够表示足够语法与证明关系、但不能把外部元理论结论直接当作内部能力的位置。

这解释了为何“不可停机”是有效搜索轴，却不是一个只靠写循环即可完成的答案。

## 11. 下一轮最小可验证工作

依照总方案，下一轮按以下顺序推进：

1. 以 Agda Cubical v0.9 为第一分母，搜索通常配置中的定义相等、Reflection、HIT eliminator、quotient/partiality 和高阶相干消费者；明确禁止显式撤销终止性审查。
2. 固定一个真实 HoTT 消费者并做任务保持缩减，判断非完成是否仍需 Path/HIT/univalence；若移除这些构造后仍存在，登记为通用类型论或实现现象。
3. 资格化 MetaRocq 与 Coq-HoTT，复用现有 Gödel 机器化工程的语法编码、primitive recursive 表示和证明谓词结构，建立 `G1` 对象化路线。
4. 在 Agda Cubical 内定义一个极小、可递归检查的对象语言，先机器证明 substitution 和 derivation checking 的基本性质，再考虑 diagonal construction。
5. 对“所有两类悖论最终都导致计算不完成”的总假说建立反例集，至少包含生产性无限、不可判定但具体实例完成、非现实性差异表现为错误值而非非完成三类候选。

本评价至此完成其校准职责。后续结果必须使用新的 evaluation ID 或 revision；不得修改本次冻结的 evaluator、scope、probe 或运行收据来改变结论。

## 12. 可复核入口

- `SCOPE.json`：问题、来源、探针与资格门；
- `FREEZE.json`：预先冻结的 evaluator、scope、源码树、工具链与解释；
- `DECISIONS.json`：23 个来源锚点、终止性声明清点与探针源码绑定；
- `runs/20260914-REFLECTED-TICK-REDUCTION-OBSERVER-001/RUN.json`：正式运行、逐字节重放和语义结果；
- `probes/*.agda`：10 个原生探针；
- `machine-overview/reflected_tick_termination.py`：协调器与独立复核入口；
- `machine-overview/tests/test_reflected_tick_termination.py`：冻结绑定、来源清点、因果模型与结论边界回归测试；
- `machine-overview/HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md`：不可停机机器统观总方案与文献索引。

复核命令：

```bash
python3 machine-overview/reflected_tick_termination.py verify \
  --run machine-overview/evaluations/REFLECTED-TICK-REDUCTION-OBSERVER-001/runs/20260914-REFLECTED-TICK-REDUCTION-OBSERVER-001/RUN.json \
  --rerun

python3 -m unittest machine-overview/tests/test_reflected_tick_termination.py -v
```

本评价运行时工作树含本研究线尚未提交的既有变更；`RUN.json` 已记录 exact worktree、branch、HEAD 与 dirty 计数。当前证据属于本地未提交状态，尚未形成 Git 版本闭合。
