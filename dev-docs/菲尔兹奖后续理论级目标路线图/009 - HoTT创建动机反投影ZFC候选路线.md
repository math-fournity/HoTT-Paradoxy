<!-- governance-shard:v2
logical_id: FIELDS-THEORY-TARGET-ROADMAP
shard_id: 009
index: ../菲尔兹奖后续理论级目标路线图.md
-->

# HoTT创建动机反投影ZFC候选路线

> **身份：** `DRAFT_PROPOSAL / MOTIVATION_BACKPROJECTION_SEED / NOT_A_ZFC_Q_OR_MATHEMATICAL_CLAIM`。
>
> **触发：** 研究发起人于 2026-10-03 提出：HoTT 的创建者所表述的、在已有 ZFC／集合论基础下仍有必要创建 HoTT 的理由 `R1,R2,…`，可否反向成为寻找 ZFC 候选 `Q1,Q2,…` 的来源；并提出将既有 HoTT 现象 `H0` 在 ZFC 中寻找对应物 `Z0`，进而考察 `Q0=H0(Z0)`。

## 1. 这条路线的准确形式

这不是“HoTT 被创造出来，所以 ZFC 必有缺陷”的推理。HoTT 作者的动机可能是：批评既有基础的一个限制、避免表示成本、追求新的对象语言、获得机器可实现性，或者仅仅选择不同的基础风格。它们的证据地位不同。

路线必须经过三个不能跳过的层次：

```text
R_i = HoTT 原典中可定位的动机、对比或能力目标
  → Z_i = 该动机在具体 ZFC / set-theoretic presentation 中对应的规则、表达代价、
          守卫或真实消费者；不是自动的“ZFC错误”
  → Q_i = 以模式 P 形成的同一任务候选：对象、formation、consumer、
          计算—存在—自指／完成追问、controls 与 Done 全部冻结。
```

`R_i → Z_i` 是**原典解释与来源映射**；`Z_i → Q_i` 才是**候选生成**。若没有一张通过 P1 的
`L0–L2`、同一任务、活跃义务／未支付检验的卡，结果只能停在 `MOTIVATION_ONLY` 或
`BACKPROJECTION_SEED`。

## 2. HoTT 原典提供的第一批动机种子

下列材料来自本仓库固定的 HoTT Book 源码，不把它们扩写成作者对 ZFC 不一致性的主张：

| ID | 原典动机 `R_i` | ZFC侧应重建的 `Z_i` | 当前身份 |
|---|---|---|---|
| `R-STRUCT` | 单价性使同构结构可被识别；书中称这与常规基础的“官方”立场不相容。 | set-theoretic equality、同构、具体代表、选择与自然性之间的表达／使用代价。 | `BACKPROJECTION_SEED`；已有 ETCS／规范选择控制必须先消费。 |
| `R-CONSTRUCT` | 类型的构造与消去原则让对象的形成、分解和计算可预测；书将它与集合论较自由的 formation principles 对照，并联系 proof assistant。 | ZFC 的 set existence、formula schema 或 proof witness 是否被某一实际消费者误当作同一行动者已取得的可操作对象。 | 与 ZFC-H8/H9、Power Set和P3-C相交；不是“ZFC无构造性”的结论。 |
| `R-HIGHER` | higher inductive types 与 univalence 给出某些同伦对象与构造的直接逻辑描述；书说它们不能被 classical set-theoretic foundations **直接**捕获。 | set-theoretic encoding、strict equality、coherence／transport或representative choice的直接性成本。 | `MOTIVATION_ONLY`；“不能直接捕获”不等于不能编码、更不等于已得到 Q。 |
| `R-MACHINE` | Univalent foundations 与可由 computer proof assistant 实现的数学基础相连。 | ZFC 使用者何时从形式存在／证明对象跨到可执行、可获得、可验证的交付。 | `BACKPROJECTION_SEED`；须排除外部 proof search 与纯实现层误配。 |
| `R-SET-CONTROL` | HoTT Book 亦尝试在 HoTT 内构造类似 ZF 的 cumulative hierarchy，并说明两种“set”有重要差异。 | 这说明互译／兼容本身是研究对象，而非一条反 ZFC 动机。 | `ANTI_ANALOGY_CONTROL`。 |

主要原典 locator：

- `HoTT/theory-schema/upstream/book-578b85cc/introduction.tex:15–24`：单价性、higher inductive types、常规基础与机器实现；
- `…/introduction.tex:36–51`：类型论、构造／消去、集合论形成原则与 proof assistants；
- `…/categories.tex:1443–1444`：在 set-theoretic foundations 中，唯一到同构不足以无 Choice 定义函数；
- `…/categories.tex:1716–1723`：集合论中的 category objects、同构不变性与 equality 的实际用途；
- `…/setmath.tex:7–27`：HoTT sets 与 ZF cumulative hierarchy 的差异和内部累计层级构造；
- `…/preface.tex:91–92`：机器可检查数学基础的实践目标。

## 3. `H0 → Z0 → Q0`：不是类比，而是传输门

研究发起人所称 `H0` 指本项目已经记录的 HoTT 侧“相同／宇宙／高阶结构”的完成困难读法；它的正式命题、
来源与用户判定仍由现有 HoTT evidence owners 拥有。这里不把 `H0` 重新表述为 ZFC 命题。

`Z0`目前是 **UNKNOWN**。下列条件必须同时满足，才允许把一个 ZFC 侧位置称为 `H0` 的传输对应：

| 传输条件 | 必须保住的内容 | 不足的替代物 |
|---|---|---|
| `T0` 理论内对象 | ZFC 侧有对象语言的一等对象／接口 `u_Z`，而非 `V`、外部模型或叙事性的“全部结构”。 | proper class、编码说明、元语言总体。 |
| `T1` 形成与交接 | 有明确 formation `F_Z`，且同一对象被 ZFC 内规则或来源定义的 consumer 使用。 | “存在一个 set”或 theorem name。 |
| `T2` 同一任务 | HoTT 的 subject、过程、观察与 Done 经映射后仍是同一类追问。 | 将“高阶相同何时落定”换成“能否任意选代表”或其它新任务。 |
| `T3` 未支付完成性 | `Q0?` 不被定义、公理、给定 witness 或标准 guard 直接回答；必须有 active positive obligation 或 formation-origin 的未付追问。 | 一般的同构不等于、不可枚举或已知独立性。 |
| `T4` P2/P3形状 | 来源支持 same-object reentry／上升式依赖，或构造／准入／完成状态中的真实张力。 | 外部 proof search、rank 序列、静态编码或实现超时。 |
| `T5` 控制 | 有有限／截断／标签保留或来源支付的对照，能说明什么改变了结论。 | 只凭 HoTT 与 ZFC 都谈“同一”就宣称同形。 |

因此当前最诚实的记法是：

```text
H0 → Z0 = TRANSPORT QUESTION
Z0       = UNKNOWN
Q0       = UNFORMED
```

这条传输可能得到两种都有价值的结果：找到保留同一任务的 ZFC 候选，或证明 ZFC 的 extensional equality／
分层使用在关键处**切断**了 HoTT 的机制。后者是 `ANTI_ANALOGY_CONTROL`，不能被写成发现失败或 ZFC 已无问题。

## 4. 首批反投影卡与既有控制的关系

### 4.1 结构同一性：最接近 `H0→Z0`，也最容易换题

HoTT Book 的结构主义动机自然指向 ZFC 中“同构结构、具体代表、选择与自然性”的界面。它与
`FND-STRUCT-005` 重叠，故不得另起一条未经控制的新“同构悖论”。已有控制表明：

1. 把“能任选某个代表”加强为“对一切自同构自然的代表”改变了 Done；
2. Mumford 的 universal-family 例子公开保留了所需对象／映射，不能把 coarse classification 当已支付的 family；
3. Mathlib 的唯一 inverse 和 skeleton 都显式支付 noncomputability、isomorphism 或 natural-isomorphism 数据。

所以 `R-STRUCT` 的下一问不是“ZFC 没有 univalence”，而是：**是否存在一个版本固定的 ZFC／集合论消费者，
它把仅按同构给出的结构 classification 当作已经足以交付一个具体、自然且可用的对象，而又没有明示所需的
选择／标记／相干数据？** 在这样的 consumer 出现以前，本卡仍是来源种子。

### 4.2 构造与机器实现：与现有罗素线相交，但不能以“ZFC不计算”代替 Q

`R-CONSTRUCT` 与 `R-MACHINE` 指向的不是“ZFC 没有算法”，而是更窄的使用问题：某个来源是否把对象的
存在、一个 schema instance、或 proof-theoretic witness，升级为同一行动者已经获得的可操作交付。

这应继续消费现有 H8/H9、P3-C、source-layer和ConstructionBridge controls：

```text
set existence ≠ effective decision
fixed formula schema ≠ internal universal evaluator
finite Finset completion ≠ arbitrary ZF Power Set construction
external proof search ≠ ZFC-internal admission process
```

这些不是反对反投影路线，而是它的最低资格。

## 5. 未启动的后续规格

若研究发起人以后选择启动本路线，第一张卡应按下列模板冻结，而不是直接让 R1/R2/R3 成为 Q1/Q2/Q3：

```text
Motivation source R_i and exact locator:
ZFC variant / source layer / precise Z_i:
Candidate u_Z / F_Z / C_Z / I/O/Done:
Target-Q / Candidate-Q / Control-Q:
H0 transport status: T0–T5 pass / fail / unknown (when applicable)
P1/P2/P3 expected roles:
same-task X_i / Op / O / Done:
standard defense and nearest control:
reopen / stop condition:
```

本路线不改变当前 Power Set 的 `Q-0 UNFORMED` 身份，不替代 P-first 的明显承诺原则，不启动 worker、网络、
Goal、STATE candidate或数学证明。它只是增加一组由 HoTT 原典动机提供的、可逐项证伪的 ZFC 来源入口。
