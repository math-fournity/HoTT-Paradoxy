# Coq-HoTT reflective subuniverse 的类型类证明搜索递归

> Evaluation：`COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001`
> 现象层：`TYPECLASS_PROOF_SEARCH`
> 候选范围：`COMMUNITY_HOTT_AUTOMATION_RECURSION_BOUNDARY`
> HoTT 现实相对结论：`NOT_ESTABLISHED`
> HoTT 理论问题结论：`NOT_ESTABLISHED`
> Gödel 结论：`NO_OBJECT_LANGUAGE_OR_PROVABILITY_PREDICATE`
> 日期：2026-09-14

## 1. 研究对象与问题

本评价研究 Coq-HoTT 社区库中一个由作者直接记录的 proof-search 设计边界。对 reflective subuniverse `O`，库提供：

```coq
Definition isequiv_O_inverts
  {A B : Type} `{In O A} `{In O B}
  (f : A -> B) `{O_inverts f}
  : IsEquiv f.
```

源码没有把该定理注册为自动实例，并解释：若如此登记，搜索可能不断生成更深的 `O_functor` 义务；紧邻的
`Hint Immediate` 形式也被注释掉。类似的说明还出现在 truncation、reflective subuniverses 的相等传递及 connectedness
实例周围。

研究问题是：在当前 Coq-HoTT 与 Rocq 版本上，这一作者记录的现象能否机械复现？它位于证明搜索、转换还是给定证明的
内核检查？当前库是否已经启用它？HoTT 结构是否为必要原因？它与 ASK、现实对应及 Gödel 不完备性有何关系？

## 2. 冻结分母与构建

### 2.1 社区源码

| 项目 | 固定值 |
|---|---|
| Official repository | `https://github.com/HoTT/Coq-HoTT` |
| Commit | `cc6184729bf8572a1d188c7a46f8d224f40bcceb` |
| Git tree | `1325fa48e5e57eb452fc4938e8ba116757d420ee` |
| Tracked entries | 675 |
| Tracked bytes | 5,188,476 |
| Tracked-tree SHA-256 | `9e6764b93b09a79bf627eae6746a07c4518e54f5bf5d498328e539f399fb7f7f` |
| Source state | clean |

`SCOPE.json` 固定 README、INSTALL、CI、opam、`ReflectiveSubuniverse.v`、`Basics/Trunc.v`、
`Truncations/Core.v` 和 `Truncations/Connectedness.v` 共 8 个来源文件、18 个文字锚点。18/18 在决定阶段全部找到。

### 2.2 原生构建

源码通过 `git archive HEAD` 进入此前不存在的目录，随后在网络关闭的容器中执行官方 `make -j2`：

| 项目 | 固定值 |
|---|---|
| Image | `rocq/rocq-prover:9.0` |
| Image/digest | `sha256:3ed9c46fa02e9fd7748a959abebb11b36f8818d10738dcc93edc67354c313ce2` |
| Platform | `linux/amd64` |
| Rocq | 9.0.1 |
| OCaml | 4.14.2 |
| Build interval | 2026-09-14 06:31:56Z–06:36:02Z |
| Exit | 0 |
| Build tree | 4,451 files / 74,553,091 bytes |
| Build-tree SHA-256 | `f54181b1db56dd67d28da8151a0a2417fdb35a9bee399ced6974f75d490cd2ee` |
| External build receipt | `Coq-HoTT-qualification-cc618472-20260914a/BUILD-RECEIPT.json` |

构建成功只使该实现获得实验资格，不证明本报告研究的语义结论。

## 3. 源码清点

在全部 675 个 tracked entries 中，对 `isequiv_O_inverts` 的活动自动登记数为 **0**。因此当前生产库没有启用本评价中导致
无界搜索的规则。

机器清点发现 5 条符合预先声明短语的递归搜索边界说明：

| 文件 | 行 | 作用 |
|---|---:|---|
| `theories/Basics/Trunc.v` | 391 | 某些 truncation rules 若自动参与会产生很长或不完成的搜索 |
| `theories/Modalities/ReflectiveSubuniverse.v` | 566 | `isequiv_O_inverts` 不作为 instance，避免持续增加 `O_functor` |
| 同上 | 575 | 被注释的 `Hint Immediate` 说明 |
| `theories/Truncations/Core.v` | 154 | 两个互逆结构不能同时作为 instances |
| 同上 | 168 | 把假设重新放入 typeclass search 可能形成循环 |

另一个已冻结锚点位于 `Truncations/Connectedness.v`，说明两个 connectedness 方向同时登记也会形成循环；它不在上述
inventory 的四个短语分母内，但由 18 个 source anchors 单独固定。

这些记录证明社区开发者已经识别并主动管理 HoTT 数学结构与自动搜索图之间的递归关系。它们没有声称 modality 或
truncation 的数学定义本身不一致。

## 4. 八个原生探针

所有探针使用冻结源码和构建。每个探针先执行一次，再在全新工作目录重放；独立 `verify --rerun` 又执行第三次。
三轮的分类、退出状态、stdout 和 stderr 逐字节一致。

| 探针 | 唯一变化 | 冻结结果 | 首轮 / 重放 |
|---|---|---|---:|
| `P01` | 不登记 `isequiv_O_inverts` | 搜索有限失败 | 1866 / 1517 ms |
| `P02` | 使用源码注释中的 `Hint Immediate` | 当前 Rocq 上搜索有限失败 | 1622 / 1360 ms |
| `P03` | `Existing Instance isequiv_O_inverts` | 5 秒观察窗内未完成，exit 124 | 5992 / 5816 ms |
| `P04` | `Hint Resolve isequiv_O_inverts` | 5 秒观察窗内未完成，exit 124 | 5869 / 5616 ms |
| `P05` | 与 P03 相同，但 `typeclasses eauto 5` | 有限停止：达到深度界 | 1103 / 1102 ms |
| `P06` | P03 环境中询问已知恒等等价 | 内核接受 | 1024 / 1018 ms |
| `P07` | 无 HoTT import 的一般递归类型类规则 | 5 秒观察窗内未完成，exit 124 | 5677 / 5659 ms |
| `P08` | P03 环境，深度 4 且开启 trace | 有限停止；保留 206 行搜索轨迹 | 1163 / 1151 ms |

正式运行摘要：

```text
FREEZE deterministic SHA-256:
733e062a5fd121fa0b80af351cff013a0147ad311e968517a2b8406b6e23d4fc

DECISIONS deterministic SHA-256:
7e7c84a8bae938cf2e451627b59ff320e713124c237a90a3eefbc33baefd62ef

RUN deterministic SHA-256:
c42ddc1b878c64d9cd926e56daba1cfa338da2e723e5f32d548ea7c794ee5bd2
```

## 5. 递归机制的直接轨迹

`P08` 的有限深度 trace 包含：

- 8 次 `isequiv_O_inverts` 搜索步骤；
- 34 次 `O_functor` 出现；
- 义务 `O_inverts O (O_functor O f)`；
- 更深义务 `O_inverts O (O_functor O (O_functor O f))`。

因此，观察边界不是只由墙钟相关性猜测出来；有限 trace 直接展示了社区源码注释所描述的递进结构。其搜索图可概括为：

```mermaid
flowchart LR
  A[IsEquiv f] -->|isequiv_O_inverts| B[O_inverts O f]
  B -->|isequiv_O_functor / recursive instance| C[O_inverts O (O_functor O f)]
  C --> D[O_inverts O (O_functor O (O_functor O f))]
  D --> E[...]
```

这是一条自动证明搜索路径。它没有产生一个被内核接受的无限证明项，也没有表明给定一个已完成证明后内核检查会不完成。

## 6. 对照与版本差异

### 6.1 当前库主动保留边界

`P01` 与源码 inventory 共同表明：默认配置没有活动登记，搜索有限失败。社区代码通过不把该定理注册为 instance 来保持
自动搜索图的有限行为。因此，本评价不是当前生产库正常使用时自然出现的 non-completion。

### 6.2 历史注释的精确形式在当前版本上没有复现

源码说“even this” `Hint Immediate` 也似乎形成循环；`P02` 在 current commit + Rocq 9.0.1 上却有限失败。可能原因包括
Rocq 搜索器代际变化、`Hint Immediate` 与普通 resolve/instance 的语义差异或历史触发目标不同。本评价只给出版本固定的
负结果，不据此否定作者历史观察。

### 6.3 普通实例登记复现源码解释

`P03/P04` 进入观察边界，而 `P05` 以有限深度终止并保留递进 trace。这支持一项受限因果解释：在本固定目标和当前搜索
语义下，无界 instance/resolve 使用使 `O_functor` 义务递进；搜索深度上界将其转换为明确的有限拒绝。

### 6.4 已知证明与一般机制

`P06` 说明递归规则存在并不会使所有目标都不完成；已有直接 instance 的恒等等价能够快速解决。`P07` 用无 HoTT 构造的
类 `P n` 与规则 `P (s n) -> P n` 得到同一观察边界。这一消融否定了“递归搜索形态只能由 HoTT 产生”的假说。

## 7. 与 ASK 和两类非现实性方向的关系

这项结果与方向 B 有明确但反向的关系：它展示为什么自动登记一条数学上正确的推理规则之前，还需要询问其搜索行为是否
良基。社区库恰好已经作出了这个询问，并选择不登记。当前状态是：

```text
ASK_LIKE_DESIGN_GUARD_PRESENT_NOT_BYPASSED
```

若另一个库、插件或用户环境在没有终止性分析的情况下把该规则加入无界自动搜索，便会形成一个具体的方向 B 候选；但这项
冻结语料没有找到这种自然启用的 consumer。

方向 A 没有在本评价中建立。这里没有现实中已完成的运动或活动，也没有证明理论表示为同一任务新增了无限义务。类型类搜索
目标是一个元层证明自动化任务，不能代替用户所要求的时间、运动或现实计算对应。

## 8. 为什么它不是 Gödel 不完备性

本评价没有：对象语言、有效编码、substitution、proof-code checker、provability predicate、diagonal lemma、
Hilbert–Bernays–Löb 条件或独立句。它只给出一个搜索规则的递归运行形态。因此：

```text
NO_OBJECT_LANGUAGE_OR_PROVABILITY_PREDICATE
```

类型类引擎的无界深度和 Gödel 的“任何满足精确前提的理论都有不可判定句”属于不同层级。前者可以用搜索深度上界转换为有限
失败；后者不能通过给自动化工具设置深度而消除。

## 9. 资格结论

| 等级 | 状态 | 直接理由 |
|---|---|---|
| `N0 OBSERVATION_LIMIT` | `PASS` | 普通 instance、resolve 与一般递归对照三轮均达到 5 秒边界 |
| `N1 CAUSAL_CONTROLS` | `PASS` | 默认/Immediate/深度界/已知等价/一般递归/有限 trace 构成控制与消融 |
| `N2 ORDINARY_CONFIGURATION` | `FAIL` | current source 的活动登记数为 0；探针主动登记规则 |
| `N3 HOTT_ESSENTIALITY` | `FAIL` | 无 HoTT 的一般类型类规则复现同一形态 |
| `N4 NATURAL_CONSUMER` | `PARTIAL` | 社区作者记录真实设计边界，但冻结生产配置中没有启用 consumer |
| `N5 REALITY_CORRESPONDENCE` | `FAIL` | 没有固定同任务现实对应 |
| `N6 MACHINE_PROVED_CLAIM` | `FAIL` | 有原生执行和 trace，没有数学上的永不终止证明 |

综合结论：这是目前机器统观找到的第一个**来自当前社区 HoTT 代码、由作者明确记录、可以原生复现其邻近机制的证明搜索递归边界**。
它提高了机器统观的真实性，却同时通过对照阻止了不恰当的理论归因。

## 10. 对总方案的影响

本评价回答了“在社区 HoTT 代码中制造一个不完成的证明过程是否困难”：并不困难，而且社区源码本身已经记载相应候选。
但它也证明继续增加元层循环的边际价值很低，因为 `N2/N3/N5` 没有因此提高。

依据用户指定的外部方案，下一条主线转为对象层机器：

1. 在 Cubical Agda v0.9 / Agda 2.8.0 的标准检查片段中定义确定性两计数器机器；
2. 定义 `Halts` 为命题截断后的有限步见证，定义 `Diverges` 为每个有限步均非 final；
3. 机器证明一个 halt 程序和一个 loop 程序；证明项自身必须完成；
4. 之后才构造 universal evaluator 与 diagonal/reduction，证明不存在统一 `Dec Halts`；
5. 独立推进 Coq-HoTT/MetaRocq 的 syntax、substitution、proof checker、provability predicate 与 diagonal 义务。

这将把研究从 `R0 operational observation` 提升到 `R1 certified divergence`，再尝试 `R2 certified undecidability`；当前
Coq-HoTT 结果保持 R0。

## 11. 复核入口

- `SCOPE.json`：分母、来源、构建、18 anchors、15 questions、8 probes 和资格门；
- `FREEZE.json`：探针创建前的 evaluator/scope/toolchain/source/build 绑定；
- `DECISIONS.json`：source anchors、活动登记清点、作者记录边界与 probe source pins；
- `probes/*.v`：八个原生 Rocq 探针；
- `runs/20260914-COQ-HOTT-TYPECLASS-RECURSION-001/RUN.json`：首轮、重放、trace 与语义结论；
- `machine-overview/coq_hott_typeclass_recursion.py`：冻结、执行和独立复核器；
- `machine-overview/HOTT-NONTERMINATION-MACHINE-OVERVIEW-PLAN.md`：总方案、文献与下一阶段；
- `machine-overview/literature/README.md`：用户指定外部方案的稳定快照索引。

复核命令：

```bash
python3 machine-overview/coq_hott_typeclass_recursion.py verify \
  --run machine-overview/evaluations/COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001/runs/20260914-COQ-HOTT-TYPECLASS-RECURSION-001/RUN.json \
  --rerun
```

本评价仍位于尚未提交的研究工作树中，属于 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；没有写入项目主分支或数学 claim matrix。
