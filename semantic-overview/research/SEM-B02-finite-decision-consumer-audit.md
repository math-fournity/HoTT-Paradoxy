# SEM-B02：仅仅有限、决定数据与自然分支消费者

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 基线：`a22f41ecf5c3becdd192383ff6cdbc846982813b`
>
> 当前判词：`NATURAL_THEORY_BRANCH_CONSUMER_FOUND / KERNEL_CHECKED_AND_RUNTIME_OBSERVED_WITH_SCOPE / EFFECTIVE_DELIVERY_LIFT_NOT_ESTABLISHED`

## 1. 本轮要区分的三件事

SEM-B01 证明“真实截断消费者”仍不等于 E6。SEM-B02 选择更强的候选：一个公开接口从命题级有限性产生 `A + ¬A` 决定数据，而且固定库内确实有下游对该决定数据做分支匹配。

本轮分别判断：

1. 是否存在自然的**理论内消费者**；
2. 是否存在对后端有限完成的**有效交付承诺**；
3. 是否已经构成同输入、同输出、同完成标准的**现实失配证据**。

只有三项都闭合，才可能把它提升为 `NATURAL_USAGE_MISMATCH`。本轮不把 `is-decidable` 这个名称或 JS 编译 exit 0 单独当作 Q4。

## 2. 源码中的资格链

### 2.1 `is-finite` 只保留 count 的命题截断

`univalent-combinatorics/finite-types.lagda.md:73-89` 定义：

```agda
is-finite-Prop X = trunc-Prop (count X)
is-finite X = type-Prop (is-finite-Prop X)
is-finite-count = unit-trunc-Prop
```

所以输入 `is-finite X` 是 `∥ count X ∥`，不是一个可直接投影的 `count X`。具体枚举、元素个数与等价映射都被放在命题截断内。

### 2.2 公开接口产出决定数据

`univalent-combinatorics/equality-finite-types.lagda.md:35-46` 声明：

```agda
has-decidable-equality-is-finite :
  is-finite X → has-decidable-equality X
```

其实现把 `is-finite-X` 消去到 `has-decidable-equality-Prop X`，并在具体 `count` 分支上运输 `Fin k` 的可判定相等性。另一方面，`foundation/decidable-types.lagda.md:42-59` 把决定性解释为 Curry–Howard 数据：

```agda
is-decidable A = A + (¬ A)
```

这比 SEM-B01 的“见证无关代数值”更接近执行分支：一个消费者可以对 `inl` / `inr` 模式匹配。

## 3. 自然消费者确实存在

固定 agda-unimath 源码中，`has-decidable-equality-is-finite` 出现在 16 个不同文件。至少两条链明确消费分支：

1. `foundation/exclusive-sum.lagda.md:129-155` 把由有限性取得的相等决定传给 `cases-is-prop-type-symmetric-exclusive-sum-Prop`，并分别处理 `inl p` 与 `inr np`。该链的最终输出是等式证明，属于命题层消费者。
2. `univalent-combinatorics/orientations-complete-undirected-graph.lagda.md:91-125,195-243` 用有限性导出的相等决定构造 `Decidable-Prop`，在 `cases-g` 中对两次决定作四分支匹配，随后构造有限差异子类型并把元素数模 2 映到 `Fin 2`。这里已经存在非命题数据结果，但它仍是库内数学函数。

因此，`NATURAL_THEORY_BRANCH_CONSUMER_FOUND` 成立。此前把 E6 简写成“有没有自然消费者”还不够精确；自然理论消费者与有效交付消费者必须分开。

## 4. 机器探针

探针源码位于 `semantic-overview/formal/sem-b02/`；收据位于 `semantic-overview/runs/20260913-SEM-B02-FINITE-DECISION-001-01/`。固定工具链为 Agda `2.8.0-3d04bac`、agda-unimath `7b81411d9f60afec359d29ed1e4edf43f4711c8a`、Node `v26.7.0`。

### 4.1 同一布尔等式任务

`SemB02Kernel.agda` 固定命题 `true ＝ false`，构造两条决定路径：

- `explicitDecision = inr neq-true-false-bool`：显式决定过程；
- `finiteDecision = has-decidable-equality-is-finite is-finite-bool true false`：从“Bool 仅仅有限”获得。

两者都经 `decisionTag` 映到 Bool；`inl` 映到 `true`，`inr` 映到 `false`。库内可证明两个 tag 都等于 `false`。

### 4.2 13 步正式运行

| 层 | 探针 | 实际结果 | 支持范围 |
|---|---|---|---|
| 外部源码 fresh kernel | `equality-finite-types` + 传递加载闭包 | exit 0；310 条 `Checking` | 固定定理与加载闭包被 kernel 接受 |
| 闭合 kernel 正例 | `SemB02Kernel.agda` | exit 0 | 显式决定与有限性决定在命题层都给出 `false` |
| 判断相等负例 | `SemB02DefinitionalNegative.agda` | exit 42；`[UnequalTerms]` | `finiteTag ＝ false` 不能由 `refl` 建立 |
| 显式决定 JS 正控 | `SemB02ExplicitRuntime.agda` | check 0；JS 生成 0；Node 0，输出 `FALSE` | 构造子消去式 FFI 能区分库 Bool；显式分支可运行 |
| 有限性定理 JS | `SemB02FiniteRuntime.agda` | check 0；JS 生成 0；Node 1 | 模块初始化时 `exports.unit-trunc is not a function`；没有产生 Bool 答案 |
| 优化后端复核 | 同一有限性探针 + `--js-optimize` | JS 生成 0；Node 1，同一错误 | 该版本的 JS 优化没有消去 postulate 依赖 |

生成的 `SemB02Kernel.js` 明确连接 `finiteDecision` 与 `finiteTag`。但实际 Node 错误更早发生：传递依赖 `foundation.set-truncations` 在模块初始化时构造 `equiv-unit-trunc-unit-Set`，调用被生成为 `undefined` 的 `unit-trunc`。所以本轮观察到的是**整个自然定理模块不可加载执行**，不是 `finiteDecision` 运行后返回了错误分支。

### 4.3 正控与输入差异

显式正控提供了一个实际可运行的相等决定，但它直接保留 `inr neq-true-false-bool`；有限性路径只输入 `is-finite-bool = ∥ count bool ∥`。两条路径的理论命题相同，提供给程序的输入资格不同。因此该对照证明“预先保留决定过程可运行”，不证明同输入的现实侧已经完成而理论侧失败。

## 5. 承诺搜索与词汇反例

对根 README、决定性定义、有限性定义、有限相等定理、exclusive-sum 消费者与 orientation 消费者做固定范围搜索：

- `executable/execution/runtime/compile/compiler/backend/program/algorithm/termination/complexity/extract/real-world` 没有命中；
- `resource` 唯一词汇命中是 README 的 “informative resources for mathematicians”，指资料；
- `effective` 两处命中是 `eq-effective-quotient'`，指商的数学有效性。

根 README 把项目定位为单价数学形式化和面向数学家的信息资源。固定源码没有把 `has-decidable-equality-is-finite` 声明成 JS/GHC 可运行算法，也没有给 postulated truncation 提供 `COMPILE` 实现。

这个负结论只覆盖固定提交、上述 16 个 exact-name 使用文件和本轮选择的自然调用链；外部应用、文章和未来版本仍未知。

## 6. 过程失败与纠偏

1. 初版 kernel 探针漏导入依赖对构造子，报 `NotInScope ,`；补精确 import 后通过，命题未改。
2. 初版“count 正控”仍导入高层有限性模块，Node 在 eager postulate 初始化处失败；它不能作为无截断正控，因而被显式决定探针替换。
3. 初版 Bool FFI 用 JavaScript truthiness 解码 Scott 编码构造子，导致 `false` 被打印为 `TRUE`；生成代码显示两个构造子都是函数。最终 FFI 改为构造子消去，正式 run 输出 `FALSE`。
4. 一个降低高层依赖的隔离尝试仍通过 counting/standard-finite 依赖引入同一 set-truncation 初始化，未能把运行失败推迟到 `finiteDecision`；正式证据据此只声称模块加载边界。

这些探索失败没有被静默抹掉：它们在本节登记；正式判词只按纠偏后的 13 步收据给出。B01 的旧 `TRUE` 正控也已在其当前报告中降窄适用范围。

## 7. E6 的候选细分

本轮建议把后续 E6 检查临时拆成三个独立问题：

| 子项 | 含义 | SEM-B02 |
|---|---|---|
| `E6a` | 有真实、可回查的理论内下游消费较弱资格所得数据 | `YES`：16 文件使用；至少两条显式分支链 |
| `E6b` | 下游或工具接口明确承诺 Q4/Q7 有效交付 | `NOT_FOUND_IN_SCOPE` |
| `E6c` | 同输入、同输出、同完成标准下，承诺与真实运行形成失配 | `NOT_ESTABLISHED` |

这只是本分支的方法候选，不改主线 C3/C11。它的作用是防止两种相反错误：把纯数学调用者一律说成“没有消费者”，或看到一次模式匹配就直接宣布现实相对悖论。

## 8. 判词与下一步

当前综合判词：

- `NATURAL_THEORY_BRANCH_CONSUMER_FOUND`；
- `KERNEL_CHECKED_AND_RUNTIME_OBSERVED_WITH_SCOPE`；
- `FINITE_THEOREM_MODULE_RUNTIME_BLOCKED_BY_POSTULATE_DEPENDENCY`；
- `EFFECTIVE_DELIVERY_LIFT_NOT_ESTABLISHED`；
- `NATURAL_USAGE_MISMATCH_NOT_ESTABLISHED`。

SEM-B02 到此停止继续制作同型内部探针。下一步应寻找 `E6b`：固定版本的外部应用、教程、插件或下游包，是否把这一类 `is-decidable` / finite decision 明确接到编译 main、服务接口或资源内完成承诺。若没有可回查外部消费者，应登记 `CONSUMER_SOURCE_GAP`，不再用库内更多数学调用点代替。

## 9. 给 canonical integrator 的候选建议

未来 integrator 若接受本单元，可以考虑：

1. 把 E6 从单一“自然消费者”字段细分为理论消费、交付承诺、同任务失配三个检查项；
2. 登记 `has-decidable-equality-is-finite` 的自然理论消费者已找到，不再把该类队列说成只有命名假阳性；
3. 保留判词在 `EFFECTIVE_DELIVERY_LIFT_NOT_ESTABLISHED`，不得因 `is-decidable = A + ¬A` 或 JS compile exit 0 自动升级；
4. 将 JS 模块 eager postulate 初始化作为固定工具链运行边界，重开条件为后端/模块生成策略或截断实现变化。

这些都是 `CANDIDATE_NOT_CURRENT`，不更新主线 claim matrix、STATE 或方向/全景投影。
