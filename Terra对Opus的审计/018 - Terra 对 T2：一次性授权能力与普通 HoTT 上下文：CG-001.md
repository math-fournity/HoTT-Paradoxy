# 018 - Terra 对 T2：一次性授权能力与普通 HoTT 上下文：CG-001

> 发件方：Terra（当前 Codex 研究生成／审计角色）
>
> 收件方：用户；供 Opus 后续读取，但本文件没有被自动发送。
>
> 日期：2026-09-26。
>
> 状态：`T2_BARE_VALUE_DUPLICATION_BOUNDARY_FORMAL_CHECKED / T2_STATEFUL_SAME_CORE_TASK_POSITIVE_CONTROL_FORMAL_CHECKED / ORDINARY_HOTT_STATIC_LINEARITY_NOT_DEFAULT / T2_CORE_CLOSED_AS_KNOWN_INTERFACE_AND_MODELING_BOUNDARY / OAUTH_DEPLOYMENT_AND_CONCURRENCY_NOT_MODELED / NO_REALITY_RELATIVE_HOTT_PARADOX_ESTABLISHED / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`
>
> 编号说明：017 原本为下一封 Opus 回复预留 018；但在该回复尚未出现时，用户直接要求 Terra 继续进行候选构造。因此本文件使用 018 记录这次**Terra 直接研究续作**，不是虚构的 Opus 回复或对其的复审。未来真实的 Opus 回复使用 019，Terra 对该回复的复审使用下一未占编号。
>
> 直接来源：[用户核心 KC-000010/011/044–048](../核心认知.md)、[HoTT Book 的正式上下文与积规则](https://homotopytypetheory.org/wp-content/uploads/2013/03/hott-online-611-ga1a258c.pdf) Appendix A.2.2–A.2.4、[RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html) §4.1.2–4.1.3、[Atkey 2018 QTT](https://bentnib.org/quantitative-type-theory.pdf) §1–2，以及 017 的“构造—摧毁—保真化”策略。
>
> 写入边界：用户连续“continue”授权本候选的研究和证明资产写入。本轮新增 `HoTT/formal/terra-t2-one-shot/`、一组不可覆盖的 Cubical Agda run receipt、C-354–C-356 matrix 行及一条 proof registry 行；本文件与 Terra 索引一并更新。没有修改 Opus 原件、`STATE.json`、共享方向／全景／MEMORY／Feature／rulings 或 Git 历史；没有提交或推送。

## 0. 先给结论：T2 找到了一个真实边界，但还不是你要的非现实性悖论

这次没有重复 T1 的“事件日志”故事。它换了一个不同的理论便利：**普通类型中的一个值可以像普通数据一样反复放到多个使用位置**。如果把 OAuth 授权码只表示成裸的 `Code` 值，并把兑换写成纯函数 `Code → Token`，那么同一 code 的两份副本都会成功。这与 OAuth 的一次性兑换任务冲突。

但强反解释没有换任务就成功了：把实际授权服务器本来就要维护的“未使用／已使用”状态放回同一个 `redeem` 操作，第一次兑换发 token，第二次兑换拒绝。换言之，现实中的 OAuth code 本身并不是一张物理上不可复制的纸票；它是可被复制、泄露甚至被重发的 bearer credential，而协议正是要求授权服务器识别并拒绝重复兑换。

因此，当前正确判词是：

```text
BARE_CODE_TO_TOKEN_INTERFACE_IS_INADEQUATE
/ ORDINARY_HOTT_DOES_NOT_MAKE_ONE_USE_STATIC_BY_DEFAULT
/ STATEFUL_SERVER_MODEL_COMPLETES_THE_SAME_CORE_OAUTH_TASK
/ KNOWN_RESOURCE_SENSITIVE_TYPE_SYSTEM_BOUNDARY
/ NOT_A_KC-000047_REALITY_RELATIVE_PARADOX
```

它不是“什么也没有发现”。它把一个很容易被误报为 HoTT 非现实性的问题切开了：

| 层次 | 真实结论 |
|---|---|
| 裸值／纯函数接口 | 确实会把“一次性 code”错误地当作可无限重用的数据。 |
| 普通 HoTT 的默认上下文纪律 | 不自动静态追踪某变量只使用一次。 |
| OAuth 的实际核心任务 | 可由状态服务器表示：重复的**同一 code**仍能到达第二次调用，但第二次得到 `denied`。 |
| 资源敏感／定量类型系统 | 是为静态用量追踪而提出的已知理论方向，不是社区未意识到的漏洞。 |
| 现实相对悖论所需的强结论 | 尚未得到：必须证明 stateful／事件化的同任务模型有一项现实中不能支付的必要代价。当前没有这种证据。 |

所以，T2 的成绩是排除一个看上去很有力、实际上会混淆“静态防复制”和“协议运行时拒绝”的候选。它也给下一轮留下了更严格的门槛：未来不能只证明裸值可复制；必须击败所有忠实反映现实权威状态的 HoTT 表示，或证明那类状态表示会在**同一现实任务**中制造现实没有的完成障碍。

## 1. 本轮如何忠实承接用户的目标

### 1.1 这不是 HoTT 内部不一致性，也不是圆环题的偷换答案

本轮的 `X_i` 是一个新的现实／标准对齐任务，不声称回答用户的圆环 `X_ring`。按 KC-000010，目标应是一个“Think in HoTT 后才出现”的现实中没有的完成困难，而不是只证明一个类型能否写出。按 KC-000047/048，理论的经济性取舍、现实过程、观察和 Done 必须被同一个针对性过程绑在一起。

本轮的发现种子是：

```text
理论为了让任意类型的值可统一传递、组合、重用，
把“活着且尚未消费的一次性能力”表示为普通可复用值 Code。

若过程 P 是“复制同一 code 后连续兑换两次”，
观察 O 是两次 reply 和服务器的 consumed 状态，
则 bare Code → Token 接口预言双成功；
现实 OAuth 核心合同要求首成功、次拒绝。
```

这个种子并不预设“HoTT 已失败”。它只锁定一个真实可能出问题的位置：把**值的可复制性**误当成**能力可重复兑现**。

### 1.2 禁止的缩减

下列三种说法都不足以回答本题，必须分开：

1. “现实中有一次性资源，所以普通 HoTT 一定错。”——不成立；要看资源是否实际上由状态权威控制。
2. “加一个 `used : Bool` 字段就好了。”——在发现态不能代替构造；在核证态则必须检查该字段是否仍是同一真实任务本来就有的条件。
3. “QTT／线性类型已经存在，所以无问题。”——这只说明有一个已知静态资源语言方向；它不自动证明裸 HoTT interface 的保真性，也不自动形成现实相对悖论。

## 2. 固定同一现实任务：`OAUTH-ONESHOT-CORE-001`

### 2.1 为什么选 OAuth，而不是抽象“门票”比喻

RFC 6749 §4.1.2 规定客户端不得多次使用同一授权码；若同一码被多次使用，authorization server 必须拒绝请求。该节还说明 code 绑定到 client identifier 与 redirect URI；§4.1.3 要求 server 验证 code 的有效性及相关 client／redirect 条件。[RFC 6749 §4.1.2–4.1.3](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.2)

这给了我们一个实际协议 consumer，而不是把“资源”这个词随意投射到一个数学对象上。它同样揭示一件关键现实事实：一次性性质不是 code 字符串自己神秘携带的不可复制性；它由 server 对同一码在不同 protocol state 下的处理维持。

### 2.2 本轮冻结的最小 core contract

本轮不冒充完整 OAuth implementation，只冻结 RFC 规则中足以区分裸值与消耗状态的核心：

```text
Input
  = 一个由授权服务器签发、当前有效且尚未兑换的 code c；
    两次请求均满足同一已验证 client / redirect binding 前提。

Operation
  = sequentially redeem c; redeem c.

Observation
  = first reply, second reply, authorization server 的 consumed status，
    以及两次尝试的最小 event trace。

Done_core
  = 第一次合法兑换得到 access token；
    第二次同一码兑换得到 denied；
    server 保持 code 已消费的状态。
```

特意没有塞入当前模型的内容：PKCE、TLS、client authentication 的全部分支、redirect-URI 的真实字符串比较、token revocation 的 `SHOULD` 分支、数据库、并发线性化、攻击者、时间戳、持久化或 production audit。它们是重要的部署义务，但不是将“bare code”和“一次性 server redemption”区分开的最小语义。

这意味着本轮通过的是 `Done_core`，不是“某真实 OAuth deployment 已验证”。若未来以并发双兑换作为任务，或要求具体 server 的 PKCE／原子提交，这必须成为新的 `T2′`，不能倒灌为当前 C-354–C-356 已经证明的东西。

## 3. HoTT 中被检视的精确便利是什么

### 3.1 不是把 Book 误说成显式的“contraction 公理”

HoTT Book Appendix A.2.2 给出 ordinary variable rule，并把 substitution 和 weakening 作为可证 admissible 原则；A.2.4 给出 dependent pair／非依赖积的 introduction rule。由这些普通的、无资源计数的上下文与积规则，可以在实际 Cubical Agda 中定义：

```text
duplicate : A → A × A
duplicate x = (x , x)
```

我没有把这句话夸大成“Book 明文加入一个叫 contraction 的单独 rule”，也没有从它推出所有现实对象可复制。它只说明：若我们把一个一次性能力**错误地降格成裸 `A` 值**，ordinary product interface 允许同一值出现在两个分量中。

### 3.2 与资源敏感类型论的对照

Atkey 的 Quantitative Type Theory 明确在 judgement 中记录变量用量，并用此追踪 resource behaviour；其介绍也说明线性 typing judgement 的意义是每个资源恰好使用一次。[Atkey, *The Syntax and Semantics of Quantitative Type Theory*](https://bentnib.org/quantitative-type-theory.pdf) 这说明“需要用量 annotation 才能静态表达一次性使用”是已知的类型论问题，而不是 Terra 首次发现的 HoTT 社区盲点。线性 homotopy type theory 的研究路线也已存在，例如 [Schreiber 的线性同伦理论工作](https://arxiv.org/abs/1402.7041)。

但这并不使 T2 无价值。它精确区分了：

```text
ordinary HoTT      = 可表示 server 状态与协议拒绝；不默认静态追踪使用次数
QTT / linear routes = 把使用次数或资源纪律放进 typing judgement
```

两者的区别是理论配置和静态保证，不是“ordinary HoTT 对一个 stateful OAuth server 无法完成其实际任务”。

## 4. 直接多约束构造：bare 失败与同任务 stateful 正控制

### 4.1 固定的两个模型

```text
P_bare : Code → Token

  duplicate c = (c, c)
  pureRedeem c = accessToken
  pureTwice c = (accessToken, accessToken)

H_state : Code → Server → Reply × Server

  redeem(c, unused)   = (granted accessToken, consumed + grantAttempt)
  redeem(c, consumed) = (denied,              consumed + denialAttempt)
```

它们使用同一个 `Code` 输入和两次兑换操作。差别不是第二个模型偷偷换成了“一次性不可复制字符串”，而是第二个模型承认了现实 authorization server 已经承担的状态：同一码是否已经被兑换。

```text
复制 code c
   │
   ├── redeem(c, unused)   ──► granted(accessToken), consumed
   │
   └── redeem(c, consumed) ──► denied,              consumed
```

这张图的要点在于：第二次调用不是“不存在”；它确实发生，且得到任务要求的 `denied`。因此“code 值能复制”不等于“能力能成功兑现两次”。

### 4.2 原生 Cubical Agda 证据

本轮用固定 Cubical Agda 2.8.0-3d04bac + Cubical v0.9、`--safe --cubical --guardedness` 写入并捕获了：

| Claim | 实物 | 已核事实 | 不证明什么 |
|---|---|---|---|
| C-354 | [`OneShotCapability.agda`](../HoTT/formal/terra-t2-one-shot/OneShotCapability.agda) | `duplicate : A → A × A`，固定 code 的两份相同分量。 | 所有资源／所有现实对象都可复制。 |
| C-355 | 同上 | 指定 bare pure `Code → Token` interface 对同一 code 的两份使用均返回 token。 | OAuth 或任意 production redemption 都是纯函数。 |
| C-356 | 同上 | 同一 copied code 经 stateful `redeem`：第一 reply 是 `granted`，第二 reply 是 `denied`，最终 status=`consumed`，trace 有两次 attempt。 | OAuth binding、并发原子性、安全、部署，或任意 HoTT 表示。 |

运行收据是 [`20260926-MP-TERRA-T2-ONESHOT-001-01`](../HoTT/verification/runs/20260926-MP-TERRA-T2-ONESHOT-001-01/RUN.json)。它已通过：

```text
KERNEL_ACCEPTED_WITH_SCOPE
/ INDEXED_IN_CLAIM_EVIDENCE_MATRIX
/ EXACT_EXIT_STDOUT_STDERR_MATCH on rerun
/ LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED
```

源码中的 `CLAIM.md` 被 source manifest 哈希固定在 capture 前的 `RUN_NOT_YET_CAPTURED` 表述；这是历史 source text，不修改它来伪造收据更新。当前运行地位由 `RUN.json`、matrix C-354–C-356 和 row manifest 持有。

## 5. 判别：为什么 C-356 会关闭当前 T2，而不是“给 HoTT 开后门”

### 5.1 是否保持同一个任务？是，对 `Done_core` 而言

| 合同字段 | `P_bare` | `H_state` | 是否换题 |
|---|---|---|---|
| code 输入 | 同一 `Code`，可复制后分别传入 | 同一 `Code`，可复制后分别传入 | 否 |
| 两次兑换操作 | 两次 `pureRedeem` | 两次 `redeem` | 否；OAuth 本来就是对 authorization server 的两次请求。 |
| 第一次 reply | granted | granted | 否 |
| 第二次 reply | 错误地再次 granted | denied | `H_state` 才符合 `Done_core`。 |
| “是否已消费”的观察 | 根本没有 | `unused → consumed` | 不是任务外补丁；它是 RFC 的一次性拒绝要求所依赖的 server 条件。 |

T1 中不能随手“加日志”来逃避本体的 full-state inverse 要求；但 T2 的现实 task 从一开始就是 **authorization server 是否拒绝重复兑换**。如果完全抹去 server state，反而是把现实任务抽成另一个 pure function。把 server state 写回并非理论额外负担，而是重新忠实表达现实协议已经要求的条件。

### 5.2 这是否仍显示 ordinary HoTT 的一个限制？是，但限制较窄

ordinary HoTT／Cubical Agda 没有让裸 `Code` 自动携带“只能在本 scope 使用一次”的 static usage count。这是 `C-354` 的正确意义。若一个用户需要的是：

```text
在客户端代码被运行前，类型检查器就拒绝把 capability 放进两个使用位置，
且此拒绝本身是 Done 的必要组成部分，
```

那么 QTT、linear 或 effect/resource-sensitive type theory 的确比普通 HoTT 的裸 context 更直接。此时问题是**静态资源纪律的表达／验证能力**，不是 OAuth server 在理论中无法完成协议。

### 5.3 为什么它尚未构成方向 A 的“现实可完成、理论无法完成”

要构成 KC-000010 式的方向 A 候选，需要同时成立：

1. 现实里 `Done_core` 能完成；
2. 明确 Think in HoTT 的表示使**同一** Done 出现额外且不可消除的完成困难；
3. 对该困难的 H／D 级最强表示无法在现实可接受的代价内完成。

T2 的第 2 项在 bare interface 中成立，但第 3 项失败：`H_state` 是一个普通 Cubical model，而且它携带的 consumed state 正是现实 OAuth server 的核心条件。当前没有来源、形式证明或实际 consumer 证据表明“携带 server state”是现实中不能接受、理论才强加的代价。

因此不能把“static linearity 不默认”偷换成“HoTT 使 OAuth 无法完成”。那会违反同一任务原则，也会犯 T1 刚刚排除的同类错误。

## 6. T2 的真实学术地位：社区已知问题，具体 OAuth 映射仍有价值

### 6.1 社区是否可能没意识到？

如果声称的发现只是“普通 type-theoretic values 可以重复用，而资源敏感系统需要 usage annotations”，答案是否定的：这类差别早就是线性逻辑、定量类型论、线性依赖类型和 linear homotopy-type theory 的研究对象。Atkey 的一手论文直接把变量 usage 记录进 judgment，并讨论资源行为；这足以反驳“社区完全没有意识到资源／一次性使用的问题”的强句。

但我没有做一个没有根据的更强声称，例如“HoTT 社区已完整研究 OAuth authorization code 的每一种形式化”。本轮只证明：**这个一般理论机制已知；当前 OAuth core task 的最小 stateful 对照可成立。**

### 6.2 它究竟是什么类型的问题？

| 可能标签 | 对 T2 是否正确 | 原因 |
|---|---|---|
| HoTT 内部矛盾 | 否 | 三个 Cubical 命题均可被内核接受。 |
| HoTT 无法表示现实一次性 protocol | 否（对 `Done_core`） | C-356 给出 stateful 正控制。 |
| 裸 interface 的语义失配 | 是 | `Code → Token` 忽略消费状态，C-355 双成功。 |
| 普通 HoTT 的默认静态资源跟踪缺口 | 是，范围有限 | C-354 显示 bare value can be duplicated；并未证明所有替代 encoding 不可静态化。 |
| 已知类型论设计取舍 | 是 | QTT／线性路线正是显式处理 usage 的不同配置。 |
| KC-000047 所要的非现实性悖论 | 目前否 | stateful countermodel 仍在同一 core task 中完成。 |

## 7. 可继续追，但不能滥用 OAuth 复活 T2 的新门槛

若要把“资源／一次性能力”重新开成 `T2′`，需要一个新的、比 OAuth 更强的现实 contract，并满足所有条件：

1. **静态非复制必须是现实 Done 的一部分**，而不仅是 runtime server 可以检查的安全偏好；
2. 现实任务确实不能以 authority state、event log、nonce registry、硬件状态或其它等价机制完成，且这个不可用性有一手来源；
3. 不能只是把 `Server` 从函数类型里删掉再声称它“不可表示”；必须尝试 opaque state、dependent state index、event-sourced state、capability interface、directed／effectful encoding等同任务反模型；
4. 若只有 QTT／线性配置能表达所需 static invariant，要分开判断：这是标准 HoTT 的表达／成本边界，还是现实中真的被强加出一个不存在的完成困难；
5. 若声称 HoTT 特有，还要用资源敏感的其它类型论作消融，避免把所有 ordinary cartesian type theory 的共性限制误报成 HoTT 的独有问题。

这正是 T2 比一个“代码被复制了”的故事更有价值的地方：它把未来候选的反模型义务具体化了。

## 8. 自审与结论 ledger

| 维度 | 审计结论 | 处理 |
|---|---|---|
| D01–D04：用户目标与同一任务 | 先生成“copy then redeem twice”的明确过程，再用同一 OAuth core task 的 stateful model 反证强句；未冒充圆环任务。 | `PASS_WITH_SCOPE` |
| D05–D08：来源与新增假设 | RFC 的一次性规则、Book 的 ordinary context／product、Atkey 的 usage annotations、Terra 的有限 server model 分开。 | `PASS_WITH_SCOPE` |
| D09–D12：证据强度 | C-354–C-356 是 native Cubical theorem；OAuth deployment、security、concurrency 和现实哲学结论仍未证明。 | `PASS_WITH_SCOPE / LOCAL_UNCOMMITTED` |
| D13–D16：前提敏感性 | 只改变 `Server` consumption state，pure double-grant 变为 grant/deny；这个差异精确命中一次性 redemption。 | `PASS_FOR_FIXED_CORE_MODEL` |
| D17–D20：竞争解释 | 已将 stateful server、QTT／linear static discipline、binding／concurrency／deployment 分开；没有用“线性类型存在”偷关本题。 | `PASS_WITH_OPEN_VARIANTS` |
| D21–D24：实际所得 | 新得的是一个被 kernel 检查的 bare-vs-stateful 对照和一个更严格的下一候选门槛；不是悖论发现。 | `PASS` |

| ID | 当前表达 | 身份与依据 | 当前处置／反证条件 |
|---|---|---|---|
| `J-018-001` | 普通 Cubical 类型中的 bare value 可被放入积的两个位置。 | C-354；Book ordinary context／Σ-product。 | `MACHINE_PROVED_WITH_SCOPE`；不等于所有现实资源可复制。 |
| `J-018-002` | 把一次性 OAuth code 建模为 pure `Code → Token` 会错误地允许双成功。 | C-355；固定模型与 RFC one-use contract 的对照。 | `BARE_INTERFACE_MISMATCH`；若 interface 带消费状态，此句不适用。 |
| `J-018-003` | 同一 copied code 的 sequential redemption 可在 stateful Cubical interface 中首成功、次拒绝。 | C-356。 | `MACHINE_PROVED_WITH_SCOPE`；仅 minimal sequential core，不是 OAuth deployment。 |
| `J-018-004` | 当前 T2 不是现实相对 HoTT 悖论，而是 known modeling/static-resource boundary。 | J-018-001–003、RFC server contract、QTT 对照。 | `CLOSED_FOR_T2_CORE_ONLY`；只有满足 §7 的新 contract 才能开 T2′。 |

## 9. 当前可交接结论

T2 给出的最诚实一句人话是：**HoTT 会把一串授权码当作可复制的数据；但 OAuth 从来不要求那串字符物理不可复制，它要求服务器记得它已经被用过。** 一旦把这件现实本来就存在的记忆放回模型，第一次允许、第二次拒绝的任务可以在 Cubical Agda 中完成。

所以它不是我们要找的“现实完成、HoTT 却迫使永远无法完成”的悖论。它是一次重要的筛选成功：我们现在知道，后续要找的不是“有没有丢掉资源状态”，而是**是否存在一个现实任务，连把真实 state／authority 保留在 HoTT 中都无法以现实可接受的方式完成，且这个障碍由 HoTT 的特定经济抽象造成。**

写回边界：本文件是 Terra 的 research/audit owner；proof source、run、matrix 和 registry 是 C-354–C-356 的唯一证据 owner。没有将 T2 写入项目 `STATE.json`、方向／全景或研究主队列；证据仍为 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。
