# C5A：数学基础的 faithful-representation 准则与芝诺过程完成桥

> **身份：** `CORE_ADEQUACY_TASK_CARD / C5_FOUNDATION_SOURCE_AUDIT / MATHEMATICAL_ADEQUACY_SOURCE_FOUND / PHYSICAL_PROCESS_BRIDGE_UNPAID`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)。
>
> **前序：** [C3A promotion/bridge card](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C3A-FOTG-GEOMETRIC-PROMOTION-BRIDGE-CARD.md)。
>
> **冻结来源：** [C5A snapshot manifest](../sources/external/zfc-meta-subtheory-c5a-20261005/README.md)。

## 1. C5A 的精确问题

前卡已固定下列来源事实：IEP 的 Standard Solution 有实际 promotion，Mizar/FOTG 只支付几何级数成分，Norton 所对应的 strict last-action reading 则遭遇显式 task switch。尚缺的不是又一条极限 theorem，而是：

```text
M 作为数学基础，为什么应当要求 P 对 Q 支付
FormalDone → OriginDone 的 bridge？
```

本卡只检验来源是否明确给出这种责任。它不把“基础理应更精确”的研究直觉写成 ZFC 已有公理。

| CoreAdequacy 字段 | C5A 固定内容 |
|---|---|
| `M` | bare ZFC，或将 ZFC 用作集合论数学基础的明确哲学／方法论角色；两者必须分开。 |
| `S` | IEP 所称 standard real analysis / classical mechanics；Mizar/FOTG `SERIES_1` 只作已知的 geometric-series 成分控制。 |
| `Q` | IEP Achilles/Dichotomy 的 runner、physical path、time、speed 与到达任务；strict OriginDone 仍由 Norton reading 标识。 |
| `FormalDone` | 完整连续统模型中的有限时间到达语言，及其几何级数数学成分。 |
| `P` | `physical-continuum/path/time/speed model ∧ geometric calculation ⇒ resolution/arrival` 的 IEP composite promotion。 |
| `Bridge` | 输入、操作、观察、Done 是否都由 S 的 formal result 保留；前卡结论为 strict bridge 未支付。 |
| `Adequacy` | 下面分成 `Adequacy_math` 和 `Adequacy_process`，不得混为一项。 |

## 2. 真正找到的来源支付：`Adequacy_math`

Penelope Maddy 的 *Set-theoretic Foundations* 开篇把 ZFC（可加大基数）作为 classical mathematics 的标准 foundation 角色来讨论。它引用 Moschovakis 的表述：在 sets universe 中寻找所需 mathematical objects 的 faithful representations，并说具体个案中的“delicate problem”是**明确 faithful representation 的条件并证明存在一份**。Maddy 随即把这一工作解释为数学对象的 surrogate，且明确说这种 reduction 并不声称揭示对象的深层 metaphysical identity。

同一组内容由 IEP *Foundations of Mathematics* 复述：基础的一个重要角色是用 surrogate 表征 original mathematical object 的 mathematically relevant features；具体代表关系本身才是此处有基础意义的对象。SEP *Set Theory* 则把 ZFC 的常规基础角色界定为：数学对象可作为 sets 被构造、数学陈述与论证可在集合论语言中形式化；其 Dedekind-cut presentation 的重点是具备 complete ordered field 的结构公理，而不是某个实现就是实数的形而上身份。

因此 C5A 支付下列**数学表征准则**：

```text
Adequacy_math(O_math, R_math) requires:
  (a) 明确 O_math 的 mathematically relevant features；
  (b) 明确 R_math 的 representation 条件；
  (c) 证明 R_math 保存这些被固定的特征。
```

这不是从 ZFC syntax 推出的定理；它是一个版本固定、来源明确的 set-theoretic-foundational criterion。它已足以拒绝一种偷换：不能仅因 `R_math` 是某个 set-theoretic real / series object，就跳过“哪些特征要保存”的说明。

## 3. 它没有支付什么：`Adequacy_process`

本研究所需的强 bridge 是：

```text
Adequacy_process(Q, S) requires:
  若 P 声称 S 的 FormalDone 已解决同一个过程任务 Q，
  则 Q.input / Q.operation / Q.observation / Q.OriginDone
  必须被列为要保留的特征，或来源必须明确承认任务已切换。
```

这里有一个实质边界，不能略过。

1. IEP Zeno 明说 Standard Solution 把 runner’s path 当作 **physical continuum**，以 positive finite speed 运行，并把 physical processes 处理成 point-events；它因此不是一条只谈抽象级数的来源。
2. 同一来源也明说 no-final-step intuition 被拒绝，且在“physical process”与“set-theoretic composition of the continuum”的关系上保留批评、替代方案和争议。
3. IEP Foundations 在说明 mathematical surrogacy 时反而提醒：物理科学当然也用现象模型，但这种实践比数学 surrogate relation 更直接；该来源没有把物理模型完成条件的所有语义责任归给集合论基础。
4. Maddy 的一手论文本身谈的是 mathematical objects 的 representation，并否认这一 reduction 自动提供 metaphysical insight；它没有把“真实 runner 的 strict completion”列为 every set-theoretic representation 必须验证的特征。

故当前来源只支持下面的条件句：

```text
若 IEP 的 physical runner completion 被固定为 O_math 的一个
mathematically relevant feature，并且 P 声称自己的 S-model 是该同一对象的
faithful representation，那么 Adequacy_math 要求该 feature 的 preservation/payment。
```

而 `若` 的前件尚未被同一来源支付。IEP 的 Standard Solution 给出了 composite promotion，却没有把这个 promotion 连接到“ZFC 基础的 faithful-representation audit”；Maddy/IEP Foundations 给了表征责任，却没有指定 IEP runner’s strict OriginDone 是该表征中必须保留的 mathematical feature。

## 4. source-to-spec fidelity table

| 来源字段 | 形式规格字段 | 已支付 | 尚未支付 |
|---|---|---|---|
| Maddy / Moschovakis：在 sets universe 发现 faithful representations；具体情形须定条件并证明 representation 存在。 | `RelevantFeatureSet O_math`、`Faithful(R_math,O_math)` | 数学对象的 feature-sensitive representation criterion。 | physical process completion 必是 `RelevantFeature`。 |
| SEP：set-theoretic real satisfies complete-ordered-field categorical axioms；对象可以有不同实现。 | `SubtheoryStructure S` | real model 的结构性，而非形而上同一性。 | runner 的 operation / observation / Done。 |
| IEP Zeno：physical continuum, point-events, positive finite speed, calculus; Standard Solution resolves. | `ActualPromotion P` | 有实际连续统 application promotion，而不只是 theorem name。 | P 与 M 的 faithful-representation obligation 在同一文本中相连。 |
| IEP Zeno / Norton：no final step intuition rejected / strict Done 任务切换。 | `BridgeStrict` | strict bridge 并非由 Standard Solution 自动给出。 | revised Done 与 strict OriginDone 的等价。 |
| `Adequacy_process` | `AdequacyRequiresBridge M S Q P` | 无。 | 一个实际来源将 ZFC / set-theoretic foundation 的职能明确扩展为对该 physical-process bridge 的审查。 |

## 5. C5A 判词

```text
MATHEMATICAL_FAITHFUL_REPRESENTATION_ADEQUACY_SOURCE_ESTABLISHED
PHYSICAL_PROCESS_COMPLETION_EXTENSION_UNPAID
BARE_ZFC_ENFORCEMENT_OF_PROCESS_BRIDGE_UNPAID
STRICT_BRIDGE_REMAINS_UNPAID_FOR_FIXED_Q
NOT_CORE_MACHINE_PROVED
```

这不是 `Adequacy` 已完全失败，也不是 ZFC 已被证明有对象语言矛盾。它使原先的 `ADEQUACY_UNSOURCED` 变为更精确的双层状态：**数学表征责任已有来源，而把它提升到 IEP 的 physical process completion 上仍无 actual payment。**

## 6. 控制与最强反证

- **Bridge-paid control：** 若一份同源的标准解法证明 `FormalDone ↔ strict OriginDone`，则本卡的 process bridge gap 收回。
- **Process-as-relevant-feature control：** 若一份集合论基础或其明确应用来源把 runner completion 的 input/operation/observation/Done 列作 faithful representation 的必要条件，并证明其保留，则 `Adequacy_process` 可被实际支付。
- **Different-task control：** 若来源公开把 revised completion 设为另一个任务，则它保护 Standard Solution 免于 strict-Q 指控；不能被反写成 bare ZFC failure。
- **Scope control：** SEP/Maddy 的 set-theoretic representation 说法不等于 ZFC 理论本身带有物理语义；将其当作 `Adequacy_process` 已支付是 `SURROGATE_INTERFACE_DRIFT`。

## 7. successor scan

`C5A` 已完成其最小来源动作：找到了真正的 foundational representation criterion，也定位了它没有越过的边界。它不结束 C5，更不结束总 Goal。

下一项唯一最小行动是：

```text
C5B-APPLIED-MODEL-BRIDGE-RESPONSIBILITY-SOURCE

在固定的 IEP Standard Solution / ZFC-founded-continuum source denominator 内，
寻找是否有一个版本固定的一手或权威来源同时：
  (1) 把 continuous model 表为 runner 的同一 physical process；
  (2) 指明该表示应保留哪些过程完成特征；
  (3) 将这项保真责任明确连接到 set-theoretic / foundational semantics，
      或明确拒绝这样的连接。

若它只给物理模型或只给集合论 surrogate，分别登记 partial source，
不得合取为 AdequacyRequiresBridge。
```

`reopen_if`：出现一个同源、版本固定的 source payment，将 IEP 的 physical runner task、ZFC/set-theoretic representation、strict/revised Done 的关系逐字段固定。
