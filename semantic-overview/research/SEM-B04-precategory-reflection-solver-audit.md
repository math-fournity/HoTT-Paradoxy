# SEM-B04：precategory reflection solver 的证明生成与拒绝边界

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前判词：`REFLECTION_SOLVER_GENERATES_CHECKED_PROOF_TERM / FALSE_AND_MALFORMED_GOALS_REJECTED / DECLARE_POSTULATE_NOT_USED / DEFENSE_WORKS_WITH_SCOPE`

## 1. 本轮问题与结论

`SEM-B01`–`SEM-B03` 已把截断存在性、有限性决定和后端执行拆成不同层次。本轮切换到一个
真实的证明生成器消费者：agda-unimath 的 `solve-Precategory!`。需要回答的不是“Agda 有
reflection，所以是否危险”这种泛问题，而是四个可核问题：

1. 这个固定宏对用户承诺的工作是什么；
2. 它产生的成功是受 kernel/type checker 复核的证明项，还是绕过证明义务；
3. 一个不可由 precategory 公理推出的任意态射等式及一个非等式目标会怎样；
4. reflection API 虽然暴露 `declare-postulate`，这个固定 solver 是否调用它。

本次证据支持一个明确但有限的结论：`solve-Precategory!` 在类型检查阶段把可识别的
precategory 等式重建、归一化，构造一个以可靠性 lemma 和 `refl` 为核心的证明项，再让
Agda `unify` 该证明项与洞。结合律正例被接受；任意 `f ＝ g` 因归一形不能由 `refl` 证明而
被拒绝；非等式目标在 boundary 检查处被拒绝。固定 solver 源码没有调用
`declare-postulate`。

因此，在本次固定版本和三类探针范围内，理论层“由 precategory 公理可导出的方程”与工具
层“宏可完成的目标”没有出现资格越级。这里观察到的是一道正常工作的证明检查边界，当前
状态为 `DEFENSE_WORKS_WITH_SCOPE`。本轮没有发现自然外部 consumer，也没有现实交付承诺，
所以不能据此建立 B 方向的 `NATURAL_USAGE_MISMATCH`。

## 2. 固定来源、工具与适用范围

### 2.1 来源身份

| 输入 | 固定身份 |
|---|---|
| Agda | `2.8.0-3d04bac` |
| Agda binary SHA-256 | `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e` |
| agda-unimath commit | `7b81411d9f60afec359d29ed1e4edf43f4711c8a` |
| agda-unimath tree SHA-256 | `88460bc7d2e0ffd2bc85d60ca7fa0ea8e0b833bc12e1e6e9cd18ccd517db41c5` |
| `reflection/precategory-solver.lagda.md` | `4e34f147a01b4ffce9deb863c25521fd997dddc1a072e94e1b03f5cf444a7882` |
| `reflection/type-checking-monad.lagda.md` | `519f08b73ba6dd29cac3a41566a1b356147b9e27d96ba9970f1dd550c0b8a52e` |

run 的 `source-manifest.json` 固定 14 个文件，包括 runner、三个探针、六个外部源码文件、
library 配置、toolchain manifest 和 Agda 二进制。复核时 14 项均与记录哈希一致。

### 2.2 本轮能证明和不能证明什么

本轮核验的是固定源码在 Agda 类型检查/宏展开阶段的行为。它没有：

- 穷举 solver 支持的全部 precategory 方程；
- 审计 Agda 编译器内部实现或所有 reflection primitive；
- 证明所有未来版本或依赖组合都失败关闭；
- 证明 reflection primitive 可作为编译后运行函数使用；
- 建立 HoTT 内部不一致、自验证定理或现实有效交付承诺；
- 找到固定源码树外使用该宏的版本化自然 consumer。

## 3. 源码路径：成功为什么仍受证明检查

### 3.1 源码承诺

solver 文档第 34–35 行把宏描述为求解“由 precategory 公理推出”的方程。这个限定很关键：
承诺对象不是任意两个平行态射都相等，而是结合律、单位律等可由 precategory 公理归一化
得到的等式。

### 3.2 数学可靠性路径

源码先定义 precategory expression 的解释与归一化。第 131–137 行的
`is-sound-normalize-Precategory-Expression` 给出归一结果与原表达式解释之间的等式；第
140–148 行的 `solve-Precategory-Expression` 接收两端归一形相等的证明，再通过左右两条
soundness 等式把它组合成原表达式相等。

宏所用的关键证明项因此不是裸的元级成功标志。它含有：

```text
inv(soundness lhs) · normalized-equality · soundness rhs
```

在当前实现里，`normalized-equality` 由 `refl` 提供。只有两端构造出来的归一表达式在类型
检查器看来相同，`refl` 才能具有要求的类型。

### 3.3 宏路径

第 240–249 行的宏依次：

1. `infer-type hole >>= reduce`，读取并归约目标；
2. `boundary-Type-Checker goal`，要求目标确实是等式；
3. `normalize lhs/rhs` 后用 `build-Precategory-Expression` 重建两端；
4. 构造 `solve-Precategory-Expression cat built-lhs built-rhs refl`；
5. `unify hole ...`，让 Agda 用该证明项填洞。

这条路径说明“宏自动完成”与“宏可绕过证明检查”不是同一件事。宏负责生成候选证明项，
而其类型仍须与目标统一。

## 4. 机器运行

run ID：`20260913-SEM-B04-PRECATEGORY-REFLECTION-001-01`。

| 步骤 | 判据 | 结果 | 证据 |
|---|---|---|---|
| `agda-version` | exit `0` | `EXPECTED` | `agda-version.stdout.txt` |
| `kernel-solver-fresh` | `--ignore-interfaces`，exit `0` | `EXPECTED`；273 行含 `Checking` 的实际加载诊断 | `kernel-solver-fresh.stdout.txt` |
| `macro-positive` | 结合律探针 exit `0` | `EXPECTED` | `macro-positive.stdout.txt` / `.stderr.txt` |
| `macro-false-equality-negative` | exit `42`，含三个冻结 marker | `EXPECTED` | `macro-false-equality-negative.stdout.txt` |
| `macro-non-equality-negative` | exit `42`，含两个冻结 marker | `EXPECTED` | `macro-non-equality-negative.stdout.txt` |

五步全部符合事先固定的退出码和错误 marker，`RUN.json.status` 为
`EXPECTED_BOUNDARY_OBSERVED`。

### 4.1 正例

正例目标是三个态射复合的结合律：

```agda
comp-hom-Precategory C h (comp-hom-Precategory C g f) ＝
comp-hom-Precategory C (comp-hom-Precategory C h g) f
```

定义体为 `solve-Precategory! C`，Agda exit `0`。这证明固定工具链接受宏生成的这个证明项，
也验证了从宏入口到 soundness lemma、`refl` 和 `unify` 的一条真实薄路径。它不是对文档中
“任何由公理可导出的方程”的全称覆盖。

### 4.2 任意态射等式负例

负例要求没有额外假设的两个平行态射 `f`、`g` 相等。Agda exit `42` 并报告
`[UnequalTerms]`：归一后的 `hom-Precategory-Expression f` 与
`hom-Precategory-Expression g` 不同，因此 `refl` 不能具有宏所构造的归一形等式类型。

该结果直接排除了这个受控输入上的一种误读：宏没有仅凭“二者都是同一 hom 类型中的
态射”就赋予相等证明。

### 4.3 非等式目标负例

负例把目标改成 `unit`。Agda exit `42`，报告 `[GenericDocError]` 和
`is not a ＝-type`。失败发生在宏的目标边界检查，而不是在之后伪造一个无关项。

## 5. `declare-postulate` 能力与这个 solver 的区别

固定 `type-checking-monad.lagda.md` 第 98–99 行确实暴露：

```agda
declare-postulate :
  Argument-Agda Name-Agda → Term-Agda → type-Type-Checker unit
```

第 197 行将它绑定为 `AGDATCMDECLAREPOSTULATE`。这说明 Agda reflection 的能力面中存在显式
声明 postulate 的操作，不能仅从“最终调用了 `unify`”推断整个 reflection API 没有公理引入
能力。

但固定 `precategory-solver.lagda.md` 中 `declare-postulate` 的直接命中数是 `0`；宏实际构造
的是 `solve-Precategory-Expression ... refl`，再调用 `unify`。因此“TCM API 有
`declare-postulate`”和“这个 solver 使用了 `declare-postulate`”必须分开记账。当前证据只
支持后者为否。

这也给出下一轮的精确控制实验：可以另写一个明确调用 `declare-postulate` 的最小宏，观察
普通模式与 safe 模式如何处理它。该实验若成功，只能说明显式公理引入能力和 safe-mode
边界；不能倒推本 solver 使用了该能力，也不能写成 kernel 内部矛盾。

## 6. 自然 consumer 与 E6 判别

对固定 agda-unimath 树做 exact-name 扫描，含 `solve-Precategory!` 的文件只有
`reflection/precategory-solver.lagda.md` 自身；命中是宏定义及同文件内的五个示例。没有在
该固定树中找到独立的库模块、服务、插件或应用入口把它接到另一项交付承诺。

对本轮对象，E6 可拆为：

| 子项 | 本轮状态 | 理由 |
|---|---|---|
| `E6a` 理论/工具内自然消费 | `YES_WITHIN_DEFINING_MODULE` | solver 自带五个示例，正例入口真实通过 |
| `E6b` 有效交付承诺 | `TYPECHECKING_PROMISE_MET_FOR_TESTED_SCOPE` | 实际承诺就是完成可归一化的 precategory 等式目标；正例通过、两类越界目标失败 |
| `E6c` 同任务现实失配 | `NOT_ESTABLISHED` | 没有现实任务基线，也没有固定外部 consumer |

这里与 B01/B02 不同：B01/B02 的关键裂缝出现在 postulate 的后端运行含义；B04 的工具承诺
本来就在 Agda 类型检查阶段，且本次观察到的 proof term 仍被类型检查。因此不能把“没有
编译后服务”当作该 solver 的交付失败。

## 7. 对“统观”方法的增量

本轮给第一次统观路线补上一种重要的正控制。资格审计不能只寻找理论收益后的缺口，也必须
识别支付装置真实工作、错误输入被拒绝的场景。否则方法会把任何自动化都预设为理论越级，
失去区分力。

可复用的审计顺序是：

1. 固定工具对外承诺所在的阶段；
2. 找到生成项与可靠性 lemma 的实际路径；
3. 检查更强能力是否只是同一 API 暴露，还是目标工具真实调用；
4. 同时运行承诺内正例、语义错误负例与目标形状错误负例；
5. 最后才判断是否存在自然 consumer 和现实交付升级。

这种顺序能把三种情况分开：证明自动化正常工作、显式公理能力被有意使用、以及理论资格被
外推成未经支付的完成承诺。

## 8. 剩余未知与停止条件

- 文档的全称承诺没有被穷举，只验证了一条结合律薄路径；
- 没有审计 solver 的全部间接依赖或 Agda 实现源码；
- exact-name 搜索不覆盖别名封装、未索引外部仓库或私有 consumer；
- 未测试 `declare-postulate` 在普通模式与 safe 模式的差异；
- 未建立现实任务、资源边界或时间/运动结构。

`SEM-B04` 已满足停止条件：固定源码、一个承诺内正例、两个边界负例、完整原始输出和源码
哈希均已保存。本线下一项最小可验结果是 `SEM-B05`：明确标注为受控公理引入实验，分别
核普通模式和 safe 模式，不修改 B04 的 solver，也不把能力面结果回写成该 solver 的事实。

## 9. 证据入口

- 形式探针：`semantic-overview/formal/sem-b04/`；
- runner：`semantic-overview/tools/run_sem_b04.py`；
- run：`semantic-overview/runs/20260913-SEM-B04-PRECATEGORY-REFLECTION-001-01/`；
- 机器摘要：`RUN.json`；
- 源码命中：`source-audit.json`；
- 文件哈希：`source-manifest.json`。

这些都是 contributor 分支候选实物，不是 canonical claim matrix 行、STATE revision 或项目
current truth。
