# SEM-B05：显式 reflection 公理引入与 Agda safe-mode 边界

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前判词：`EXPLICIT_REFLECTION_POSTULATE_EXTENDS_THEORY_IN_DEFAULT_MODE / SAFE_MODE_REJECTS_THE_POSTULATE / SAFE_ORDINARY_REFLECTION_ACCEPTED / CONTROLLED_CAPABILITY_BOUNDARY_OBSERVED`

## 1. 为什么做这项控制实验

B04 已确认固定的 `solve-Precategory!` 通过 soundness lemma、`refl` 和 `unify` 生成受检查的
证明项，同时也发现其导入的 reflection TCM API 暴露 `declare-postulate`。仅凭 API 中存在
更强能力，不能指控 solver 使用了该能力；仅凭 solver 没有使用，也不能假装能力不存在。

B05 因而只回答一个机制问题：如果一个宏**明确调用** `declarePostulate` 在当前目标类型上
增加公理，Agda 2.8 默认模式和 safe 模式分别如何处理？实验还需要两个控制，避免把 safe
mode 的行为误读成“禁止全部 reflection”，或把 `true ≡ false` 的默认成功误读成无公理
证明。

本轮结果形成一个清楚的四段判别：

1. 默认模式允许宏显式声明 `true ≡ false` 的新 postulate，随后文件 exit `0`；
2. 把同一份源码加上命令行 `--safe` 后，Agda 以 `[SafeFlagPostulate]` 拒绝；
3. 将同一宏体放进源码级 `OPTIONS --safe` 文件也得到相同拒绝；
4. safe 模式接受只提交普通 `refl` 项的 reflection 宏，而无新公理时直接用 `refl` 证明
   `true ≡ false` 被 `[UnequalTerms]` 拒绝。

默认模式的成功是**显式扩展理论后的成功**。它不是 kernel 从空前提证明了错误等式，也不是
Agda 内部不一致。safe 模式的拒绝是本固定版本对这项源级能力的有效边界；它不等于对 kernel
可靠性的内部证明或跨版本全称保证。

## 2. 固定身份与源码能力

### 2.1 工具和来源

| 输入 | 身份 |
|---|---|
| Agda | `2.8.0-3d04bac` |
| Agda binary | SHA-256 `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e` |
| `Agda/Builtin/Reflection.agda` | SHA-256 `ef851b831795fea34125c6cd17fb81675ed9eb62c871addb5951082cb1732b13` |
| agda-unimath TCM wrapper | commit `7b81411d9f60afec359d29ed1e4edf43f4711c8a`；SHA-256 `519f08b73ba6dd29cac3a41566a1b356147b9e27d96ba9970f1dd550c0b8a52e` |
| B04 solver | 同一 commit；SHA-256 `4e34f147a01b4ffce9deb863c25521fd997dddc1a072e94e1b03f5cf444a7882` |

22 项 source manifest 固定四个 probe、Agda primitive 源码集合、对照源码、runner、toolchain
manifest 与二进制。run 完成后逐项复核 bytes 和 SHA-256。

### 2.2 primitive 与 wrapper

固定 `Agda/Builtin/Reflection.agda` 第 297 行给出：

```agda
declarePostulate : Arg Name → Type → TC ⊤
```

第 377 行以 `AGDATCMDECLAREPOSTULATE` 绑定该 primitive。agda-unimath 的
`reflection/type-checking-monad.lagda.md` 第 98–99 行暴露同型的 `declare-postulate`，第 197
行绑定同一 builtin。B05 直接使用 Agda builtin 层，避免 safe 测试先被未标记 safe 的第三方
wrapper import 阻断。

primitive 文件第 426 行把 JS 后端的 `declarePostulate` 编译实现留为 `undefined`。这与本轮
实验边界一致：所观察的是类型检查期 TCM 操作，不是编译后程序调用。

## 3. 控制宏与唯一变化

`SemB05Unsafe.agda` 和 `SemB05Safe.agda` 的核心宏都执行：

```agda
bindTC (inferType hole) λ goal →
bindTC (freshName "sem-b05-declared-axiom") λ axiom-name →
bindTC (declarePostulate (visible-name axiom-name) goal) λ _ →
unify hole (def axiom-name [])
```

两个文件的差异限于 module 名、safe option 和解释注释。runner 去除这些项目后重算的主体
SHA-256 都是
`1bb92b865b1bff62ad359d7d40e647a83bf2068aa7d86629af2286c13dc8b1b1`，机器字段
`unsafe_safe_normalized_body_equal=true`。

另外，runner 对 `SemB05Unsafe.agda` 的原字节直接加命令行 `--safe` 重跑。源码级 safe 与
命令行 safe 都失败，因此 safe 结论不依赖人工维持两份近似文件。

## 4. 六步机器运行

run ID：`20260913-SEM-B05-REFLECTION-POSTULATE-SAFE-001-01`。

| 步骤 | 固定判据 | 结果 |
|---|---|---|
| `agda-version` | exit `0` | `EXPECTED` |
| `explicit-postulate-default` | 显式公理宏，默认模式 exit `0` | `EXPECTED` |
| `same-source-cli-safe-negative` | 同一 unsafe 源字节 + `--safe`；exit `42`；两项 marker | `EXPECTED` |
| `source-safe-postulate-negative` | 源级 `OPTIONS --safe`；exit `42`；两项 marker | `EXPECTED` |
| `safe-reflection-positive` | safe 宏只用 `refl`/`unify`；exit `0` | `EXPECTED` |
| `no-axiom-false-equality-negative` | 无公理直接 `refl`；exit `42`；三项 marker | `EXPECTED` |

6/6 步符合判据，`RUN.json.status=EXPECTED_BOUNDARY_OBSERVED`。

### 4.1 默认模式：显式扩展理论

`SemB05Unsafe.agda` 的目标是 `true ≡ false`。宏读取这个目标，声明名为
`sem-b05-declared-axiom` 的 fresh postulate，再以该名字对应的 definition term 填洞。Agda
exit `0`。

这个结果的准确语义是：默认模式允许程序通过 reflection 做一件普通 Agda 源码也能显式做的
事情——增加一条无定义的公理。成功项依赖该公理；如果消费者声称产物是无公理计算或构造性
证明，必须把这条依赖纳入审计。

### 4.2 safe 模式：针对 postulate 的明确拒绝

同一源文件加 `--safe` 时，Agda exit `42`：

```text
[SafeFlagPostulate]
Cannot postulate SemB05Unsafe.sem-b05-declared-axiom with safe flag
```

源码级 safe 版本对对应名字给出同类错误。失败发生在 `declarePostulate`，错误指向宏为
`true ≡ false` 填洞的 `unquote`。这直接核验了本固定版本 safe flag 对该能力的边界。

### 4.3 safe reflection 正例

`SemB05SafeReflectionPositive.agda` 也声明 `OPTIONS --safe`，但宏只构造 `refl` 并调用
`unify` 完成 `true ≡ true`。它 exit `0`。因此上述失败不能归因为 safe mode 一概禁止宏、
quotation 或 `unify`；本次可见差异是显式 postulate 声明。

### 4.4 无公理负例

`SemB05NoAxiomNegative.agda` 不用 reflection，直接让 `refl` 居留 `true ≡ false`。Agda exit
`42` 并报告 `[UnequalTerms] true != false`。这确认默认宏正例的关键新增输入正是显式声明的
公理，而不是 Bool 或 equality 在当前工具链中意外退化。

## 5. 与 B04 solver 的隔离

B04 的固定源码 audit 对 `precategory-solver.lagda.md` 得到
`solver_declare_postulate_call_count=0`；B05 runner 独立重算仍为 `0`。B04 宏构造的是
`solve-Precategory-Expression ... refl`，随后 `unify`；B05 控制宏明确调用
`declarePostulate`。

所以这两条结论必须同时保留：

- reflection 能力面允许默认模式下的显式公理引入；
- 已审计的 `solve-Precategory!` 没有使用这项能力。

按模块邻近、共同 import 或共同使用 `unify` 将两者混同，会重演“一个函数的性质被交付成
另一个函数的性质”这种命题忠实性错误。

## 6. 对理论经济与 B 方向的含义

本控制实验展示一种清楚的支付关系：宏可以瞬间取得任意目标的 inhabitant，但它付出的代价
是把目标本身登记为新公理。这个“收益”没有消除证明义务，而是改变了理论前提。safe mode
选择拒绝这种支付方式，同时允许普通 proof-term reflection。

因此 B05 不是自然使用失配案例：

| 判别项 | 状态 | 说明 |
|---|---|---|
| 机制能力 | `OBSERVED` | 默认模式允许显式 `declarePostulate` |
| 能力使用 | `CONTROLLED_ONLY` | 使用发生在本轮明确编写的探针 |
| safe 防线 | `OBSERVED_WITH_SCOPE` | CLI 与源码级 safe 都拒绝；普通 safe reflection 通过 |
| B04 归因 | `NEGATIVE` | 固定 solver 直接调用数为零 |
| 自然 consumer | `NOT_SEARCHED_THIS_UNIT` | 本轮不是外部 consumer 搜索 |
| 现实交付失配 | `NOT_ESTABLISHED` | 没有现实任务、承诺或同任务基线 |

对后续人工语义审计，可复用的规则是：看到 proof assistant 接受文件时，应同时检查
`OPTIONS`/CLI 模式、postulate/axiom 声明、reflection declaration primitives 和最终 claim 的
公理说明；看到 API 提供某项 primitive 时，又必须回到目标模块的实际调用路径，不能由能力
存在推定具体使用。

## 7. “统观”路线中的位置

B04 是 defense-working 正控制，B05 是 explicit-assumption boundary 控制。两者组合后，人工
语义路线能区分四类状态：

1. 宏生成可复核证明项，边界内成功；
2. 宏对错误目标失败；
3. 宏明确增加公理后成功，公理依赖是结果的一部分；
4. safe profile 拒绝该公理引入，但保留普通 reflection。

这项工作不建设 machine-overview 的 task grammar、registry、case evaluator 或 verifier。
它产出的是一个窄、可复核的语义判例，未来 integrator 可以选择把它作为机器统观系统的测试
输入，也可以只保留为人工审计证据。

## 8. 剩余未知与停止条件

- 未审计其它 reflection declaration primitive；
- 未检查 Agda compiler 内部 safe-mode 实现；
- 未对其它 Agda 版本作全称保证；
- 未搜索第三方宏是否隐式使用 `declarePostulate`；
- 未建立 compiled runtime、资源、时间、运动或现实任务承诺。

B05 已达到停止条件：能力正例、同源 safe 负例、源码 safe 负例、safe reflection 正控和无公理
负控全部保留，且 22 项输入哈希固定。继续扩展 reflection primitive 枚举的边际收益低于回到
真实自然 consumer 与交付承诺的主线，因此本分支在这里停止该机制深挖。

## 9. 证据入口

- 形式探针：`semantic-overview/formal/sem-b05/`；
- runner：`semantic-overview/tools/run_sem_b05.py`；
- run：`semantic-overview/runs/20260913-SEM-B05-REFLECTION-POSTULATE-SAFE-001-01/`；
- 机器摘要：`RUN.json`；
- 源码对照：`source-audit.json`；
- 逐文件身份：`source-manifest.json`。

以上都是 contributor candidate，不是 canonical claim matrix、STATE revision 或项目 current
truth。
