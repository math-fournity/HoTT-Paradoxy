# G0：哥德尔式 ZFC 完成观察路线的实际接口分母

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **阶段：** `G0` — 冻结真实、版本固定的 ZFC-facing completion acceptance interface。
>
> **日期：** 2026-10-04。
>
> **结论身份：** `SOURCE_INTERFACE_DENOMINATOR / G0_PARTIAL_PASS / NOT_A_GODEL_THEOREM / NOT_A_BARE_ZFC_INCONSISTENCY_CLAIM`。
>
> **本轮判词：** `ACTUAL_PROOF_ACCEPTANCE_INTERFACE_FROZEN_WITH_SCOPE`，但对研究发起人关心的芝诺／圆环／H0 原过程，仍为 `PARENT_COMPLETION_ACCEPTANCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE`。因此不释放 G1–G6 的实际过程链。

## 1. 本轮要回答的窄问题

G0 不问“ZFC 能否表示时间”或“ZFC 是否不完备”。C-366 已经在冻结的 Zermelo 模型中给出过程图可表示性的正控制；它排除了“没有时间 primitive，所以不能表示过程”的过强路线。

本轮只问：能否在一份**真实、版本固定的来源**中同时冻结下列对象？

```text
T              精确的 ZFC-facing 对象理论或正式系统
Accept_T       该来源实际使用的接受接口
FormalDone     接口说完成时究竟完成了什么
OriginDone     原过程说完成时究竟完成了什么
Bridge         来源是否把 FormalDone 提升为 OriginDone
Code / Check   是否已有可用于哥德尔化的编码与有限检查入口
```

这里“同时”是关键。一个证明数据库能机械接受有限证明，不等于它已经接受一段运动、一个连续统解答或 fixed HoTT H0 的原过程已经完成；一个哲学或数学来源说“问题已解”，也不等于它已经给出可对角化的对象语言 proof predicate。

## 2. 先验判断：为什么先分成三类候选

在读取本轮来源之前，工作判断是：哥德尔的技术核心一定需要一个能处理有限编码和有限检查的真实接口；而研究发起人关心的 Q 又一定需要一个对**原过程完成**负责的真实消费者。因此最可能遇到的结构不是“没有 ZFC 接口”，而是三种接口被分散在不同层：

1. 形式证明系统提供 `Code / Check / Accept_T`；
2. 数学实践或哲学来源提供“此过程已经解决”的 `FormalDone`；
3. 语义模型提供过程的可表示性。

若来源确实这样分裂，则它不支持“ZFC 已被击中”，而是为 G0 精确指出缺哪一个同一任务接头。下面的来源读取用于检验这一判断。

## 3. 冻结的来源分母

| ID | 角色 | 版本锚点与直接来源 | 它真正承担什么 | 它不能承担什么 |
|---|---|---|---|---|
| `G0-A-METAMATH-SETMM` | 真实形式证明接受接口 | `metamath/set.mm` 的 `develop` 为 `160ebb63ec17ff00a809520a420c92914a424622`（2026-10-04 `git ls-remote --symref`）；[README](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/README.md)、[verifiers.md](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/verifiers.md)、[workflow](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/.github/workflows/verifiers.yml) | `set.mm` 被其 own README 说明为使用 classical logic 和 ZFC 的数据库；repository 明确把数据库变更的 proof re-verification 作为接受前动作，并列出五个独立 verifier。 | 不把 proof acceptance 定义成芝诺、圆环或 H0 的原过程完成；不提供本项目 `OriginDone`、`ρ` 或 `Bridge`。 |
| `G0-B-IEP-NORTON` | 实际连续统／芝诺 completion consumer | 已冻结的 [A2 来源合同卡](20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md)：IEP、Norton、SEP，采集 2026-10-04 | IEP 把 ZF with Choice 支撑的标准实分析放在标准芝诺解答语境；Norton 明示严格“有最后动作”的完成条件被删去，而解答采用较弱的完成合同。 | 没有一个版本固定的 ZFC proof checker、对象层 `Prov_T` 或可实行的 diagonal interface。 |
| `G0-C-C366-ZERMELO` | 过程可表示性正控制 | [C-366 claim](../HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation-CLAIM.md)；Foundation `f3972f4204fc61e1b736ed843415894c83f35508`、Lean 4.34.0 | ordinal-indexed sequence graph、唯一 stage value、`Seq`/`lh` 的一阶可定义性在冻结模型接口中有 kernel proof。 | 它是模型层表示性控制，不是实际 source consumer，也不接受“原过程已经完成”。 |
| `G0-D-MMLEAN4` | Metamath verifier 的 Lean 实现控制 | `digama0/mm-lean4@58123caf246f4d7afc903d8a749512449bef75c1`；[README](https://github.com/digama0/mm-lean4/blob/58123caf246f4d7afc903d8a749512449bef75c1/README.md)、`Metamath/Verify.lean` | README 给出 `lake exe mm-lean4 path/to/set.mm` 的实际 checker 入口；源码给出 parser/verification program。 | 它是 Lean 中写出的 M 层 program，不是已经证明 checker sound/total 的 theorem，也不是 `set.mm`/ZFC 内部 provability predicate。 |
| `G0-E-FLYPITCH` | ZFC proof-relation 深嵌入来源 | `flypitch/flypitch@d72904c17fbb874f01ffe168667ba12663a7b853`；[README](https://github.com/flypitch/flypitch/tree/d72904c17fbb874f01ffe168667ba12663a7b853)、`src/fol.lean`、`src/ZFC.lean`、`src/summary.lean` | `ZFC : Theory L`、proof tree、`T ⊢' f`、proof substitution，以及 source-reported CH independence theorem 可定位。 | 这是 Lean 3 M 层的 ZFC proof relation；没有 Nat Gödel numbering、T 内 provability/fixed point、parent `OriginDone` 或 bridge。 |
| `G0-F-FOUNDATION-GODEL` | 通用哥德尔技术的 kernel replay | `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508`；`First.lean`、`Second.lean`、`StandardProvability.lean` | exact Lean 4.34 source replay 实际检查 code/quote/substitution、standard provability、第一／第二不完备性 theorem。 | 适用于带 `ArithmeticTheory`、可定义性／可枚举性、算术强度、soundness／consistency假设的 generic T；不实例化 bare ZFC、set.mm、parent `OriginDone` 或 bridge。 |

### 3.1 远端 source snapshot

本轮仅下载了小型 source documents 到临时只读检查目录，未把外部 `set.mm` 的 49.1 MiB 数据库复制进本 repo：

| 文件 | 固定 revision | 本轮 SHA-256 | 作用 |
|---|---|---|---|
| `README.md` | `160ebb63…` | `33c057d3c5fcf9c20f836030a20b05cb7578231af0bc90c521c560e629b3baa9` | 确认 `set.mm` 使用 ZFC、数据库与 proof 角色。 |
| `verifiers.md` | `160ebb63…` | `362dfba67ca6dbfc3aca7fc0b356563edf20410e91f90044f38d01b7be47bbf6` | 确认接受前的多 verifier re-check policy。 |
| `.github/workflows/verifiers.yml` | `160ebb63…` | `6dccde49f13affdc33fbeebd06d60dc92ce940b2290e5f41bc19811df9561403` | 确认 workflow 对 `set.mm` 实际调用 verifier 的脚本形态。 |

`set.mm` 在上述 immutable revision 的 HTTP HEAD 结果为 `200 OK`、`Content-Length: 51,466,065`；这证明该 pinned object 可取得，不是该数据库已在本机重跑的证据。

`mm-lean4` 的本轮 checkout SHA-256 为：README `45544f6675ed117a4386eaeaa797608c46de7dc0085367fed199e0e73ebeee50`、`lean-toolchain` `12b3414dafc4575fab9eb37bb265165c5a637af839af2d300f7e931b78765706`、`Metamath/Verify.lean` `dce8d9be2bf74d003b812cae68c245d9e2ee80d27a0d1a424135adc6f04dd731`。其 pinned toolchain 是 `leanprover/lean4:v4.26.0-rc2`；本机已有 `v4.26.0` 正式版而没有该 RC。一次 `lake build` 观察到 elan 开始请求 RC2，但未得到 build binary；因此不把该尝试计作 source run。

随后用本机已有 `v4.26.0` 完成的非 canonical positive/negative control 已保存为 [run receipt](20261004-GODEL-Q-REFLECTION-G0-MMLEAN4-META-CHECKER/RUN.json) 和 [范围报告](20261004-GODEL-Q-REFLECTION-G0-MMLEAN4-META-CHECKER-CONTROL.md)。该补充不改变前一句关于 exact RC2 replay 未完成的结论。

## 4. GodelizationCard A：Metamath `set.mm` 的 proof-acceptance interface

| 字段 | 冻结值 | 证据状态 | 范围与限制 |
|---|---|---|---|
| `T` | Metamath language 中的 `set.mm` database，revision `160ebb63…`；README 说明其采用 classical logic + ZFC。 | `SOURCE_CERTIFIED` | 这是一个 **ZFC-facing formal database**，不是 bare ZFC 的唯一标准语法，也不是所有集合论模型。 |
| `M` | 五个独立 verifier（C、C++、Rust、Java、Python）以及 repository 的 GitHub Actions workflow。 | `SOURCE_CERTIFIED` | 本轮没有本地重跑任一 verifier；不把远端来源陈述写成当前本机 kernel receipt。 |
| `Code` | Metamath database 中的公式、proof steps 与其压缩 proof representation。 | `SOURCE_CERTIFIED` | 这支持“有真实有限 proof artifact”；尚未给出 ZFC 内对该编码的 arithmetization 或证明谓词。 |
| `Check` | workflow 对数据库调用 verifier；来源说明每个 `set.mm`/`iset.mm` change 在接受前被 re-verified。 | `SOURCE_CERTIFIED_FOR_PINNED_DATABASE_WORKFLOW` | 不是 `T` 内关于 checker totality 的 theorem；那是 G2 义务。 |
| `Accept_T` | 一个数据库 revision 的所有声明 proofs 通过指定 verifier checks，且 change 才可被接受。 | `SOURCE_CERTIFIED` | acceptance object 是 proof/database validity，不是“任意数学或物理任务已经完成”。 |
| `FormalDone` | 该数据库内给出的 proofs 已被机器逐步验证。 | `SOURCE_CERTIFIED` | 只在 formal proof validity 的消费者语境中成立。 |
| `OriginDone`（native control） | 对“有限 proof checking 是否完成”的原任务，来源的描述与 `FormalDone` 对齐。 | `SOURCE_CERTIFIED_WITH_SCOPE` | 这是一个 source-defined positive control；没有把它外推到运动、连续时间或 HoTT Q。 |
| `OriginDone`（parent target） | 芝诺／圆环的原动作完成，或 fixed H0 的原追问完成。 | `OPEN / NOT_SOURCE_SUPPLIED` | `set.mm` source 没有为这些任务承诺一个完成谓词。 |
| `Bridge`（native control） | proof accepted → proof check completed，属于该 source 自己的任务定义。 | `SOURCE_DEFINED_TASK_ALIGNMENT` | 此处不是“formal theorem truth → 现实过程完成”的桥。 |
| `Bridge`（parent target） | `Accept_set.mm(e) → OriginDone_Zeno/H0(e)`。 | `ABSENT_BY_SCOPE / NOT_A_SOURCE_SILENCE_CLAIM` | 不是从“文档未提到”推出不可能，只是当前 card 没有这个接口。 |
| `Diag` | 对 `Accept_set.mm` 的 quotation/substitution/fixed-point 及其在 T 内可表示性。 | `OPEN` | 历史 R3/R4 或主机上的任何编码不能替代。 |
| `QObservation` | 对 proof-validation task，未见 `FormalDone ∧ ¬ OriginDone`；对 parent target，尚未定义同一输入域。 | `NATIVE_CONTROL_NORMAL / PARENT_UNFORMED` | 不能从这个正常控制推得 ZFC 没有 Q。 |
| `RealityMap ρ` | proof artifact → verification task可由来源角色解释；proof artifact → Zeno/H0 process 尚未给出。 | `NATIVE_SCOPE_ONLY` | 不能以“数学可以编码一切”补上保真映射。 |

### 4.1 两个必需控制

**原任务正控制。** 若任务就是“这个 Metamath proof/database 是否通过规定验证”，`Accept_set.mm` 的输入、操作、观察和 Done 都由该形式系统来源定义。此时没有未支付的 `FormalDone → OriginDone` 提升。这说明一个真正的 proof acceptance interface 本身不自动制造 Q。

**DifferentTask 反控制。** 将 `Accept_set.mm` 的 input（proof/database）、operation（verification）和 Done（valid proof accepted）替换成 runner 的动作序列或 fixed H0 的逐层追问，已经改变了对象、输入、操作、观察与完成标准。当前没有 source-supplied `ρ` 将这两类任务相连。因此不得把“Metamath 接受一个 ZFC proof”写成“ZFC 已接受芝诺或 HoTT 原过程完成”。

### 4.2 `mm-lean4`：G2 的 M 层 implementation control，而非 G2 支付

`digama0/mm-lean4` 的 README 是一个有用的真实实现入口：它是用 Lean 4 写成的 Metamath verifier，并说明可以构建命令行程序来检查 `set.mm`。但直接阅读当前 `Metamath/Verify.lean` 有两个决定性边界：

1. 主入口是 `partial def check (fname : String) : IO DB`；这不是一个给所有有限输入提供 Lean termination theorem 的 total definition。
2. 源码被 Lean typecheck 也不自动证明 verifier 的 semantic soundness，更不构造 `set.mm`/ZFC 内的 `Proof_T`、`Prov_T`、quotation 或 diagonal theorem。

因此本卡只登记：

```text
META_ONLY_CHECKER_IMPLEMENTATION_SOURCE_IDENTIFIED
EXACT_TOOLCHAIN_BUILD_NOT_COMPLETED_WITH_SCOPE
NONCANONICAL_POSITIVE_AND_NEGATIVE_RUNTIME_CONTROL
NO_G2_TOTALITY_OR_T_INTERNAL_REPRESENTABILITY_PAYMENT
```

它提高了后续 G2 的可操作性，但不能释放 G2，更不能改变 parent `OriginDone`/bridge 的缺口。

### 4.3 Foundation：已机器重放的通用 Gödel技术基线

冻结 `Foundation@f3972f…` 的 `First.lean` 和 `Second.lean` 已在 exact Lean 4.34.0 source closure 中实际重放。它们不是笼统地写“会有自指”，而是给出 `codeOfREPred`、quote、substitution、standard provability、first incompleteness 和 consistency-unprovability 的明确类型和依赖。

这正是 GODEL-Q 需要借鉴的技术骨架，但 theorem 的量词仍是带明确假设的 `ArithmeticTheory`。当前没有 map 将 `set.mm`／bare ZFC 的 actual interface 证明为满足这些假设，也没有将对角 sentence 解释为 parent completion task。完整运行与范围在 [Foundation 基线报告](20261004-GODEL-Q-REFLECTION-G2-FOUNDATION-GENERIC-GODEL-BASELINE.md) 中固定。

这一缺口现已有一个精确的类型控制，而不是只靠“没有看到 map”的叙述：Foundation 同时暴露 `ZermeloFraenkelChoice : SetTheory` 和通用 `ArithmeticTheory` theorem，但把前者直接作为后者的 `T` 会被 Lean 以 `SetTheory`／`ArithmeticTheory` 类型不匹配拒绝。正、负控制及其 run receipt 见 [Foundation ZFC 映射缺口](20261004-GODEL-Q-REFLECTION-G2-FOUNDATION-ZFC-GODEL-MAPPING-GAP.md)。这个结果只阻断**直接**实例化；它不证明不存在可另行构造、并经完整前提验证的算术化或解释。

## 5. GodelizationCard B/C：为何不能把另外两类来源补成同一个接口

| 字段 | `G0-B-IEP-NORTON` | `G0-C-C366-ZERMELO` | G0 结论 |
|---|---|---|---|
| 实际 completion consumer | 有：来源把标准连续统解法称为 resolution，同时明示 strict/revised completion 的任务切换。 | 无：C-366 只是模型中 trace 表示的 theorem。 | B 给过程合同，C 给表示性；都不替代 A 的 proof acceptance。 |
| 版本固定 `T` | 有 ZFC-supported application language；没有一套被该来源指定的 proof calculus/database。 | 有冻结 Lean model interface；不是 bare-ZFC source consumer。 | 两者均不能充当 `T = actual ZFC completion checker`。 |
| `Code / Check / Diag` | 无来源给出的 finite proof checker 或 diagonal mechanism。 | 有部分集合论 definability；无 actual acceptance checker 或 fixed point consumer。 | 不能借它们启动 G2/G3。 |
| `FormalDone / OriginDone` | 这正是强项：Norton 的 card 区分 revised 和 strict Done，并拒绝把前者当作后者的 bridge。 | 不定义二者。 | B 反而构成 SourceSwitch control，而非未支付桥。 |
| 与 H0 的关系 | 没有 fixed H0 map 或 adequacy policy。 | 可表示 trace 但未给 H0Map/AdequacyLift。 | 无法支付 F-050 所需的共同 acceptance contract。 |

## 6. G0 判词与对路线的影响

本轮冻结了一个真实、版本固定的 **formal proof acceptance** interface；因此不再把“也许根本没有可哥德尔化接口”当作无区别的空白。

但 G0 的 parent target 不是“能不能检查一份 proof”，而是一个 ZFC-facing interface 是否把形式完成提升为芝诺／圆环／H0 原过程完成。当前分母显示：

```text
Metamath:       Code + Check + Accept_T，缺 parent OriginDone / ρ / bridge
IEP/Norton:     completion contract + task-switch control，缺 Code + Check + Diag
C-366:          process representation control，缺 actual consumer + acceptance policy
mm-lean4:        M-layer checker implementation，缺 checker totality/soundness theorem 与 T-internal representation
Flypitch:          M-layer ZFC proof relation/substitution，缺 Gödel coding/fixed point 与 parent completion bridge
Foundation:        generic code/quote/substitution/provability/fixed-point baseline，缺 target-specific ZFC/process map
```

所以本轮支持的最大结论是：

```text
G0_ACTUAL_PROOF_ACCEPTANCE_INTERFACE_FROZEN_WITH_SCOPE
PARENT_COMPLETION_ACCEPTANCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE
G1_TO_G6_NOT_RELEASED_FOR_THE_PARENT_Q_CHAIN
```

它**不**支持：bare ZFC 有形式矛盾；Metamath、IEP 或 Norton 已承认 Q；不存在任何可把这三类责任连接起来的未来来源；或者 C-359 的条件 consequence 已被实际实例化。

## 7. 下一最小判别行动与重开条件

### 7.1 受限来源筛选的负结果

本轮还对公开网页进行了两个窄搜索批次：

| 批次 | 冻结查询 | 可用命中 | 对 G0 的作用 |
|---|---|---|---|
| Metamath 与 Zeno | `site:us.metamath.org/mpeuni Zeno set.mm`、`site:github.com/metamath/set.mm "Zeno"`、`"Zeno's Paradox" "Metamath" formal proof`、`"Zeno's paradoxes" formalization "ZFC" proof` | Metamath 的数据库、ZFC/实分析目录与 verifier 来源；没有一条返回结果同时给出 Zeno 原过程的 completion contract。 | 不把 `set.mm` 的 proof acceptance 假装成 Zeno resolution。 |
| 其他 proof assistant | `"Zeno's paradox" formalized theorem prover`、`"Zeno's dichotomy" formalized proof assistant`、`"Zeno" "Isabelle" formalization`、`"Zeno" "Lean" formalization calculus` | 返回的 Zeno 名称多指向无关 prover、一般哲学讨论或非 ZFC 形式化；没有出现同一来源将 ZFC formal acceptance、原过程 Done 与 bridge 接在一起。 | 只支持继续保持当前分母的 `UNDERDETERMINED_WITH_SCOPE`。 |

这是一份按查询和日期固定的筛选记录，**不**是“世界上不存在这种来源”的结论；新的版本固定来源、不同原过程合同或更精确的 source owner 都会重新打开 G0。

当前工作不能通过再造一个 Bool fixture 或把 host checker 当 `T` 内 checker 来继续。下一项只有一个足够小、能改变结论的来源动作：

> 寻找一个版本固定的 actual source，令同一 source owner 同时给出 `(i)` 明确的 ZFC-facing formal acceptance、`(ii)` 一个特定过程类别的 `OriginDone`、以及 `(iii)` 从前者到后者的 bridge、task switch 或明确拒绝。

若找到了，才能用该 source 重建 GodelizationCard 并重新决定是否释放 G1。若该 source 明确说 `Done` 已被改写，结果应登记为 `SOURCE_INTERFACE_DEFENSE_WITH_SCOPE`；若保持来源分裂，结果是本 card 的有界 underdetermination，不是 bare-ZFC 结论。

## 8. 可复查动作

```bash
# 外部 revision 身份（动态网络事实；需要当前复核）
git ls-remote --symref https://github.com/metamath/set.mm.git HEAD

# 本项目的既有 source-contract 对照
sed -n '1,260p' audit/20261004-ZFC-ACTUAL-Q-A2-标准解法来源完成合同.md
sed -n '1,240p' HoTT/formal/bare-zfc-q-precision/CLAIM.md
sed -n '1,220p' HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation-CLAIM.md
```

外部网页在本轮的直接支撑包括 [set.mm README](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/README.md)、[verifier policy](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/verifiers.md)、[GitHub Actions workflow](https://github.com/metamath/set.mm/blob/160ebb63ec17ff00a809520a420c92914a424622/.github/workflows/verifiers.yml) 与 [IEP 的芝诺标准解答条目](https://iep.utm.edu/zenos-paradoxes/)。这些来源证明各自的系统或叙述边界；它们不证明本项目的哲学归因。
