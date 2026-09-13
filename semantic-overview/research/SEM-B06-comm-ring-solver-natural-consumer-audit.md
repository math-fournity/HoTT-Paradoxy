# SEM-B06：交换环 solver 的真实下游消费者与交付阶段

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前判词：`NATURAL_LIBRARY_CONSUMER_FOUND / PROOF_TERM_GENERATION_ACCEPTED / FALSE_AND_MALFORMED_GOALS_REJECTED / TYPECHECKING_PROMISE_MET_WITH_SCOPE / NO_RUNTIME_DELIVERY_CLAIM`

## 1. 本轮问题与结论

B04 证明 `solve-Precategory!` 在测试范围内正常生成受检查的证明项，但固定树中 exact-name
使用只在其定义模块的五个示例；因此它没有闭合“真实自然消费者”这一项。B06 改用 Cubical
Agda v0.9 的 `CommRingSolver.solve!`，先要求候选同时满足：

1. solver 有明确的目标类别和类型检查阶段承诺；
2. 固定源码树中存在定义/示例模块之外的 production consumer；
3. consumer 实际把 solver 接入一个更大的数学构造，而不只是演示；
4. solver、consumer、正例和越界负例都能在固定工具链中重放。

四项全部满足。固定 Cubical 树中有 32 个导入该 solver 且含 `solve!` 的文件、229 次文本
调用；其中 29 个 production downstream modules 共 200 次。选定的
`Cubical.Algebra.CommRing.Localisation.Base` 调用 13 次，用于局部化关系传递、商运算良定义
和交换环结构证明。该 consumer 与 solver 都通过 `--ignore-interfaces` fresh 检查。

solver 在本地支持的交换环恒等式上成功；对任意 `x ≡ y`，归一形的 `refl` 类型检查失败；对
非等式 goal，reflection parser 直接拒绝。固定 solver 源码没有调用 `declarePostulate`。

这形成一个比 B04 更强的正控制：**自然消费者存在，且工具承诺在真实下游中被兑现；但承诺
本身就是类型检查期证明自动化。** 固定 Cubical 树没有该 solver 的 GHC/JS FFI 或
`main : IO` 入口，因此没有发生从数学等式证明资格到编译后/现实完成资格的提升。本轮不建立
`NATURAL_USAGE_MISMATCH`。

## 2. 固定来源与证据范围

| 输入 | 固定身份 |
|---|---|
| Agda | `2.8.0-3d04bac` |
| Agda binary | SHA-256 `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e` |
| Cubical library | v0.9 / tag commit `b150186d2544e7efeddd31e5d14a8b9ecbb100f7` |
| release archive | 1,555,852 bytes；SHA-256 `003f9c57c134e4a9401a4b339b3773be667aa169ff929ca3dfb9c8abefc225c5` |
| extracted tree | 1,111 files / 7,511,145 bytes；SHA-256 `73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81` |
| reflection source | SHA-256 `997e0cdd46c81e5e24f79c028e2e63cec7847ccaf3ad164e2aff34b01e971eb1` |
| solver theorem source | SHA-256 `b3d794a845531eb23fa34161480d713c40f4170b071349213ade4cf93a5f4601` |
| localisation consumer | SHA-256 `fbcf84b4dfffa6510a608db41dcf22e9d3b54a72993de4f97a23df5e3eb80d61` |

run `20260913-SEM-B06-COMMRING-NATURAL-CONSUMER-001-01` 固定 188 个唯一输入文件。
两个 fresh 步骤的实际 `Checking` 路径均逐项进入 manifest；这避免只列四个入口文件却遗漏
真实导入闭包。

本轮能支持的是固定版本源码与一次真实 Agda 执行。它没有穷举全部 200 个 production 调用，
也不证明每个有效交换环恒等式都在 solver 支持的语法片段内。

## 3. 承诺、实现与 proof term

### 3.1 对外承诺

`Cubical.Tactics.CommRingSolver` 的入口注释说明 boilerplate 由 Agda reflection 自动构造，并
把用户指向 Examples；Examples 以多项式恒等式、单位、交换、分配、负号和复杂项展示
`solve! R`。这个接口的交付发生在 Agda 检查源文件时：给目标洞产生一个 equality proof。

它没有对运行时间上界、后端可执行程序、服务响应、现实资源或物理过程作承诺。

### 3.2 数学可靠性路径

`Solver.agda` 的 `isEqualToNormalform` 逐表达式证明解释值等于 Horner normal form 的解释值。
第 126–134 行附近的 `solve` 接收：

```text
p : eval (normalize e₁) xs ≡ eval (normalize e₂) xs
```

然后组合：

```text
sym (isEqualToNormalform e₁ xs) · p · isEqualToNormalform e₂ xs
```

得到两条原交换环表达式相等。宏不是只返回“归一成功”的布尔标志；它最终必须构造这个
定理的实例。

### 3.3 reflection 路径

`Reflection.agda` 的路径是：

1. `inferType`/`reduce` 读取 goal；
2. 只接受 equality goal，否则 `typeError`；
3. 检查用户给出的结构是 `CommRing`；
4. 把两端转为 algebra expressions 并收集变量；
5. `solverCallAsTerm` 构造 `ringSolve ... refl`；
6. `unify hole solution` 交给 Agda 核验。

`Reflection.agda` 与 `Solver.agda` 中 `declarePostulate` 直接调用数为 `0`。这与 B05 的控制宏
形成明确对照：两者都使用 reflection，但 B05 明确改变前提，本 solver 走 soundness theorem
加 `refl`。

## 4. 自然消费者清单

扫描条件不是在全树盲数 `solve!` 字符串，而是文件同时导入
`Cubical.Tactics.CommRingSolver*` 且含该标识符。结果：

| 分类 | 文件 | 调用文本次数 |
|---|---:|---:|
| production library downstream | 29 | 200 |
| experimental downstream | 1 | 3 |
| solver examples | 1 | 21 |
| reflection implementation | 1 | 5 |
| **合计** | **32** | **229** |

production consumers 分布在 BooleanRing、CommAlgebra、CommRing ideals/localisation、fields、
integer/matrix algebra、Zariski geometry 和 integer divisibility 等模块。它们不是 29 个同一
examples 文件的别名，而是独立的库证明模块。

### 4.1 选定 consumer：ring localisation

`Cubical.Algebra.CommRing.Localisation.Base` 定义把交换环按乘法闭子集局部化的集合商。其 13
次 `solve!` 至少承担三种真实职责：

- 在 `locTrans` 中重排乘法因子，把两个关系见证组合成传递性；
- 在加法/乘法的 `θ` 与负元良定义证明中，把代表元等式送入商构造所需的关系证明；
- 在 `+ₗ`、`·ₗ` 的单位、逆元、分配等结构证明中关闭交换环恒等式。

这条消费链不是“工具演示 → 工具自证”。solver 的输出进入 set quotient 上新交换环结构的
实际库证明。consumer 本身仍提供所有非纯环代数内容：商的消去器、关系见证、`cong`、
`ΣPathP`、子集命题性等。solver 只支付交换环表达式正规化那一段义务。

## 5. 六步机器运行

| 步骤 | 判据 | 实测 |
|---|---|---|
| `agda-version` | exit `0` | `EXPECTED` |
| `kernel-solver-fresh` | `--ignore-interfaces`、exit `0` | 176 个实际 checking sources；51.66 s |
| `kernel-natural-consumer-fresh` | localisation、`--ignore-interfaces`、exit `0` | 178 个 checking sources；53.05 s |
| `macro-positive` | 分配+交换正规化，exit `0` | `EXPECTED` |
| `macro-false-equality-negative` | exit `42`；三个 marker | `[UnequalTerms] x != y`；归一形 `refl` 类型不成立 |
| `macro-non-equality-negative` | exit `42`；两个 marker | `[GenericDocError]`；parser 拒绝 `.fst R` goal |

6/6 步符合冻结判据；run 总时长 112.30 s，`RUN.json.status` 为
`EXPECTED_BOUNDARY_OBSERVED`。

### 5.1 正例的范围

本地正例：

```agda
x · (y + z) ≡ z · x + x · y
```

它需要右分配、乘法交换和加法交换/结合的正规化，Agda 接受宏生成的证明项。更强的自然
正例是 localisation 模块的 13 个调用随整个文件一起通过 fresh 检查。

### 5.2 假等式负例

目标 `x ≡ y` 只知道 `x`、`y` 是同一交换环的元素。solver 将它们作为不同变量，构造出的
两端 Horner normal forms 不同；`refl` 无法具有所需的 normal-form equality 类型，Agda 报
`[UnequalTerms]`。因此真实使用量大并没有让 solver 获得“同类型元素自动相等”的资格。

### 5.3 目标形状负例

目标 `fst R` 不是 equality。宏在重建多项式之前以
`The CommRingSolver failed to parse the goal` 拒绝。失败没有被转成一个无关 inhabitant。

## 6. E6 与交付层判断

| 子项 | 本轮状态 | 依据 |
|---|---|---|
| `E6a` 自然理论/工具消费者 | `YES_STRONG` | 29 production files / 200 uses；localisation 13-use consumer fresh 通过 |
| `E6b` 对应交付承诺 | `TYPECHECKING_PROMISE_MET_WITH_SCOPE` | 工具承诺是生成交换环等式 proof；正例、consumer 与负例边界一致 |
| `E6c` 同任务现实失配 | `NOT_ESTABLISHED` | 无编译后/资源/服务/现实任务承诺 |

固定 Cubical tree 中，`COMPILE GHC`/`COMPILE JS` 命中文件数为 `0`，正则
`main : IO` 命中文件数也为 `0`。这不是“Cubical 永远不能执行”的全称定理，只说明当前 solver
consumer corpus 的可见交付阶段止于 typechecking。

B06 因而修正一种容易发生的过度推断：**找到真实自然 consumer 是必要证据，但不是失配的
充分证据。** 还必须证明 consumer 把原资格升级成了更强承诺。在这里，production modules
确实依赖自动化，但依赖的是 kernel/type-checker 可复核的等式证明，未声称获得其它能力。

## 7. 对理论经济账本的含义

该 solver 带来真实经济收益：29 个 production modules 避免反复手写交换环重排，localisation
可以把注意力放在 quotient relation 与结构构造上。支付装置也能定位：

```text
reification + Horner normalization
  + isEqualToNormalform
  + normal-form refl
  + Agda unify/type checking
```

自动化节省“表达证明”的成本，没有删除 soundness obligation。对理论经济统观，这是一条
重要正例：应同时记收入、支付装置、承诺阶段和负例边界；不能因为工具很强或使用广泛就把
收入本身登记为资格越级。

## 8. 与机器统观线的边界

本轮没有新增 task grammar、case registry、自动 evaluator、跨层 verifier 或搜索调度。32/229
inventory 只是为这个人工语义判断固定自然使用分母；结论依赖对 solver theorem、reflection
term 和 localisation consumer 的逐段阅读。未来 machine-overview 可以选择该案例作为
`NATURAL_CONSUMER + DEFENSE_WORKS` 校准样本，但本分支没有实现其机器框架。

## 9. 剩余未知与停止条件

- 未逐一 fresh 检查其余 28 个 production files；
- 未证明 solver 语法片段的完备性；Examples 还明示某些定义展开/二元减法形状当前不支持；
- 未审计编译器内部 reflection 实现；
- 未搜索 v0.9 之外的 downstream repositories；
- 未建立 compiled runtime、现实资源、时间/运动或服务完成承诺。

B06 已满足本机制的停止条件：自然 consumer、实现/可靠性路径、完整实际导入闭包、一正两负、
固定来源与 E6 三分均已闭合。继续枚举同一 solver 的另外 28 个文件只会加深相同正控制。下一
单元应换到具有**明确更强交付声明**的版本化应用，或如实记录此类 consumer source gap。

## 10. 证据入口

- 形式探针：`semantic-overview/formal/sem-b06/`；
- runner：`semantic-overview/tools/run_sem_b06.py`；
- run：`semantic-overview/runs/20260913-SEM-B06-COMMRING-NATURAL-CONSUMER-001-01/`；
- 自然使用分母与源码命中：`source-audit.json`；
- 188 文件与两个 actual checking closures：`source-manifest.json`；
- 机器判词与六步状态：`RUN.json`。

这些是 semantic contributor 的研究候选，不新增 canonical math claim，也不修改
machine-overview lane。
