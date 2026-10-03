# HMZ-001：首批原典的有界发现

> **证据级别：** `SOURCE_REPORTED + AI_INTERPRETATION + CONTROLLED_NO_CANDIDATE_SEED`。
>
> **不是：** ZFC 不一致证明、ZFC 总体缺陷判决、Power Set 的 Q、或 `H0→Z0` 已完成传输。

## 1. 来源真正共同说了什么

首批 HoTT／UF 原典确实反复提出四类动机：

1. **结构同一性：** 非正式数学常按同构使用结构，而 conventional foundations 的官方 equality 不直接给出这种识别；
2. **高阶对象的直接描述：** higher inductive types 与 univalence 把某些同伦对象／构造放入原生逻辑语言；
3. **更适于日常机器验证的基础：** 基础应成为可用于日常数学、可由 proof assistant 检查的工具；
4. **从 sets 到 homotopy types 的对象语言转向：** 作者主张 native axiomatization 的理论收益。

这是来源报告，不是对 ZFC 的定理性反驳。尤其，`directly`、`official`、`in practice` 等限定词不能删除。

## 2. 第一轮反投影的结果

### 2.1 最接近的入口是结构同一性，但第一位真实消费者是防线

Mumford 的实际 moduli 任务精确区分：按同构的 coarse classification、需要的 universal family、
automorphisms，以及必须指定的 maps。其正控制在 automorphism-free 情形，防线在一般情形保留映射数据。
因此它支持“这是一条真实的结构—代表边界”，却**不支持**“数学界把分类当作已经交付 family”。

本轮结论是：`HMZ-Q-001 = Q-R REJECTED_WITH_SCOPE`。这不是退回到“ZFC 没问题”，而是删掉了一个
偷换 Done 的假阳性路径。

### 2.2 ZFC 的 class/meta-language 边界是真正来源支持的，但被明示为语言支付

Shulman 给出了一条不只是 HoTT 宣传语的 ZFC-side fact：在纯 ZFC 的 class-as-formula 做法中，classes 不是
ZFC 可量化的对象；某些以“任意大范畴”为主体的语句不能在 ZFC 内部陈述，只能作为元定理表达。NBG 是来源
自己列出的支付：更换为带 classes 的语言，保留对 sets 的 conservative-extension 关系。

这确实把 `R-001/R-002/R-004` 的“语言／直接表达”动机推进到了一个精确 ZFC 理论层。但它没有产生罗素式
张力：ZFC 并没有把未形成 class 当作理论内对象交给操作，反而把它留在 metalevel；NBG 也明示改变语言。
因此 `HMZ-Q-005` 是 `REPRESENTATION_BOUNDARY / Q-R REJECTED_WITH_SCOPE_AS_P`。

### 2.3 Isabelle/ZF 使机器动机成为有力反控制

Isabelle 的官方 ZF 手册表明，ZF 作为 classical FOL 在 proof assistant 中有实际 formalization；Replacement
scheme 的确会给某些 theorem provers 增加实例化负担，但 Isabelle 明示提供派生规则、命名 constants 和实际
构造。它不允许把“UF 适合 proof assistant”简化成“ZFC 不能机器化”。这也没有排除未来某个 ZFC consumer 的
未支付交付，但把现有 `R-MACHINE` 的广义指控降为 `SOURCE_PAYMENT`。

### 2.4 Power Set 是清晰的形成承诺，却未由这批 HoTT 动机指向

Metamath 资料足以固定一份 Power Set 形成公式、rank guard 和 Foundation guard。它没有提供：

- HoTT 的 “direct higher description” 为什么恰好应被翻译成 `P(A)`；
- 一个将 `P(A)∈V` 当作完成某个可执行／可追溯任务的真实 consumer；
- 同一 subject、process、observation 与 Done；
- P2/P3 所需的再入、admission 或未支付完成性。

所以 `HMZ-Q-002` 不能成为“Power Set 已被 HoTT 动机重新定位”的结论。它保留为一个单独的、需要
`HMZ-MF-004` 支持的 station。

### 2.5 `H0→Z0` 没有被类比偷渡

初始 S001–S009 没有给出 ZFC 内的一等 `u_Z`，也没有形成一个保留 HoTT 高阶相同追问的 `F_Z/C_Z/Done`。
结构分类、Power Set、proof assistant 都会换掉原问题的一部分。因此目前正确的结论仍是：

```text
Z0 = UNKNOWN
Q0 = UNFORMED
H0 → Z0 = TRANSPORT_UNDER_SPECIFIED
```

### 2.6 机器验证动机仍是研究入口，不是即时攻击

Voevodsky 对既有基础、predicate logic、2-theories 与机器验证的说法，值得继续深挖。但源文本本身没有
指定一个 ZFC 使用者把存在／证明错误地升级为同一行动者的可执行交付。当前应研究的是这个 bridge，不能
从 proof assistant 运行或性能现象倒推 ZFC 的理论结论。

## 3. 冲突、未知与下一触发

| 项目 | 当前状态 | 下一来源／判别 |
|---|---|---|
| `R-STRUCT → ZFC` | 有真实 consumer，但当前 consumer 公开支付缺失数据。 | `HMZ-MF-002`：找相同 Done 被静默升级的 source，或更强地确认防线。 |
| predicate-logic / large-class 直接性 | Shulman 已给出 ZFC语言边界和NBG支付；2-theory同一对象仍未固定。 | `HMZ-MF-001` 的剩余：定位 2-theory / higher-object consumer。 |
| machine-formalization | Isabelle/ZF 已给出实践支付；层级间未支付交付仍无来源。 | `HMZ-MF-003` 的剩余：同一任务 consumer，不能用工具性能代替。 |
| Power Set | 有公理形式，R bridge 和 consumer 均缺。 | `HMZ-MF-004`；不能因为站位显眼而跳过。 |
| H0 transport | 仅有同词和不同任务；不保真。 | 先有 source-defined `u_Z/F_Z/C_Z/Done`，再填 T0–T5。 |

## 4. 研究发起人问题的当前回答

这份 run 已经把“HoTT 的创立者为何还要另建基础”从一个宽泛直觉，压缩为五张可复核 R 卡、五张
Z disposition、四张 Q/control 卡和四个明确的追踪义务。它证明了这条路线可做成来源严格的调查，而不是
把 HoTT 的口号直接转换为 ZFC 的罪名。

同时它也给出了一个富有约束力的现实结果：**最自然的结构同一性入口，第一份真实消费者反而说明数学实践
已经把非平凡 automorphism／map 数据当作任务的一部分显式支付。** 这使后续搜索更聚焦：我们不再找“任何
同构类不等于具体对象”的泛泛例子，而找是否存在某个 ZFC 侧消费者在同一 Done 下静默略过这份支付。

## 5. Stop / reopen

本轮已达到 `DENOMINATOR_COMPLETE_WITH_SCOPE`：十个冻结来源都有 `READ` 终态，四个 `HMZ-MF` 均已处理为
source payment、controlled no-hit 或 no bridge。它不应通过继续搜更多同类 HoTT 宣传文本来把“0 candidate”
改造成命中。

可以开启 successor 的触发是：新的作者原典、同一 Done 的未付 ZFC consumer、Power Set 的 R-source bridge，
或使 `H0→Z0` T0–T5 真实向前的来源。只有这些证据改变 `u/F/C/I/O/Done`、支付状态或 task identity 时，才重开
`HMZ-Q-001`、`HMZ-Q-002` 或 `HMZ-Q-005`。
