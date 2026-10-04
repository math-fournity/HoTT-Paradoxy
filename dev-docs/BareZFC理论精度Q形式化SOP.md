# BARE-ZFC-Q-PRECISION-SOP：bare ZFC 的 Q 理论精度形式化 SOP

> **身份：** TASK_SCOPED_BARE_ZFC_PRECISION_CONTRACT / F049 / NOT_A_PREDECLARED_ZFC_INCONSISTENCY。
>
> **稳定引用名：** BARE-ZFC-Q-PRECISION-SOP。
>
> **状态：** EXECUTED_WITH_SCOPE / P0_LANGUAGE_FIXED / P1_APPLICATION_CONTRACT_FIXED / P2_C364_INTERFACE_CONTROL_MACHINE_PROVED / P3_EXPLICIT_TASK_SWITCH / BARE_SEMANTIC_INTERFACE_UNDERDETERMINED / NO_BARE_ZFC_PRECISION_THEOREM。

## 1. 研究对象

研究发起人的问题是：bare ZFC 的理论精度是否不足以承担 Q 所要求的完成观察。

这里的“精度不足”不等于下列任何一句：

- ZFC 不能编码自然数、时间、步骤、程序、状态或证明；
- ZFC 的对象语言能推出矛盾；
- 任意 ZFC 形式化的分析或物理模型都必然抹掉过程；
- 只要发现一个由研究者自造的 forgetful map，就已经证明 bare ZFC 不足。

本 SOP 所说的精度，是一个固定基础接口能否将下列责任作为自己的原生、必需判断：

~~~text
形式模型的 FormalDone
原过程的 OriginDone
FormalDone 到 OriginDone 的 bridge / payment
无 bridge 时拒绝 completion promotion
~~~

bare ZFC 的语言和公理可以容纳额外集合编码；问题是一个不带这项观察合同的基础接口，是否已经足以替某个过程任务作完成判词。

## 2. BareZFCPrecisionContract

每个实际实例必须冻结如下对象，不能用“ZFC”一词把它们混成一层：

~~~text
World W                 一个带过程、来源和完成合同的具体世界
Base B                  被称为 bare-ZFC-facing 的固定观察接口
project α : W → B       该接口实际保留的集合论／模型／判词数据
FormalDone : W → Prop   模型或子理论所给出的完成
OriginDone : W → Prop   原过程任务的完成
QNeed : W → Prop        Q 所要求的观察与 bridge 责任
Bridge                   FormalDone → OriginDone 的方向、域与 payment
SourceOwner              谁声明 B 足以作出什么完成判词
Controls                 富接口、显式 bridge、不同任务和连续端点控制
~~~

### 2.1 Q 精度的机器化判据

对一个固定投影 α，bare interface 具有 OriginDone 的观察精度，当且仅当存在一个仅依赖 B 的解码器：

~~~text
∃ decode : B → Prop,
  ∀ w : W, OriginDone(w) ↔ decode(α(w)).
~~~

相应地，Q 具有观察精度，当且仅当 QNeed 或等价的 bridge/payment 判定也能只通过 α 得到。

若能给出两个具体世界 w0、w1：

~~~text
α(w0) = α(w1)
OriginDone(w0) ≠ OriginDone(w1)
~~~

则任何仅看 α 的判定器都不能忠实决定 OriginDone。这是一个可由 kernel 证明的、接口相对的理论精度不足结论。

它的数学骨架已经存在于：

- HoTT/formal/ercf-factorization/ERCF.lean 的 FactorsThrough、ParadoxWitness 与 non-factorization 定理；
- HoTT/formal/self-contained/ZCore.agda 的 fiber-truth-invariant 与 no-free-enrichment。

这些既有定理只给出一般表示边界；本 SOP 的工作是让一个版本固定的 ZFC-facing interface 真实成为 α，而不把一般定理偷换成 bare ZFC 的结论。

## 3. 必须通过的四层

| 层 | 任务 | 可接受产物 | 不能声称 |
|---|---|---|---|
| P0：语言与来源 | 固定 bare ZFC 的语言／公理或实际基础接口，以及实际使用它的来源 | 版本、定位、接口字段、来源分层 | “没有时间 primitive”自动等于不可表示 |
| P1：过程合同 | 固定 W、OriginDone、FormalDone、bridge 和现实任务 | ActualQCard 或等价的过程规格 | 任意故事都可代表圆环／芝诺 |
| P2：投影与反控制 | 给出 α，说明它为何是该接口实际保留的数据；构造同投影、异 Q 的 witness，或证明不存在 | 明确 factorization 或 non-factorization 证明 | 自造投影代表全部 ZFC |
| P3：归因 | 证明或拒绝 SourceOwner 将 B 的完成判词当作原过程完成 | 来源级 policy card 与机器 consequence | 把来源未观察写成 ZFC 已失败 |

P0–P3 必须全部通过，才允许使用“该固定 bare-ZFC-facing interface 对 Q 的观察精度不足”。任何一层失败都形成同样有价值的范围结论。

## 4. 机器证明路线

### M1：通用定理复核

复核现有 ERCF/ZCore 的 fiber-constancy 定理和它们的 run/source 边界。它们应当被引用，不能重命名为 bare ZFC 定理。

### M2：接口相对的精确定理

新增 proof package 时，定理必须具有如下形状：

~~~text
precision_failure :
  α w0 = α w1 →
  OriginDone w0 ≠ OriginDone w1 →
  ¬ (∃ decode : B → Prop,
      ∀ w, OriginDone w ↔ decode (α w)).
~~~

这个定理只能证明固定 α 的不足。它不证明 bare ZFC 无法定义别的、更富的编码。

### M3：富接口正控制

给 α 加入过程标签、bridge certificate 或明确的 OriginDone invariant 后，证明对应的观察可以恢复或原先的反例不再成立。此控制防止把“需要更多信息”误报为“不可能处理过程”。

### M4：来源绑定

只有实际来源确实将 α 作为完成判词的充分输入，M2 才可参与 bare-ZFC 精度归因。来源若已经要求 bridge、明确改变任务、或使用富接口，应形成防御结论。

## 5. 固定反控制

1. **可编码性正控制：** 一份带过程轨迹、bridge 或标签的集合编码可以让 ZFC 中的额外定义使用这些数据。它反驳“ZFC完全不能表达时间”的过强说法。
2. **连续端点正控制：** 自然数阶段没有末项，不能推出连续时间模型没有端点到达。
3. **显式 bridge 正控制：** bridge 被给出并被验证时，不能继续称该接口遗漏 Q。
4. **不同任务控制：** FormalDone 与 OriginDone 本来服务不同任务时，不能要求二者相等。
5. **来源 owner 控制：** 研究者定义的投影不能代替实际 ZFC-facing source 的完成接口。

## 6. 完成、停止与重开

| 结果 | 条件 | 允许结论 |
|---|---|---|
| INTERFACE_Q_PRECISION_FAILURE_WITH_SCOPE | P0–P3闭合，固定 α 的同投影异 Q witness 和 source owner 均成立 | 该接口不足以单独作 Q 的完成判词 |
| INTERFACE_Q_PRECISION_DEFENSE_WITH_SCOPE | 富接口或来源已携带并消费 bridge／过程 invariant | 该接口在该任务上已经支付 Q |
| SOURCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE | 无法从来源冻结 α 或 SourceOwner | 不将 generic theorem归因给 bare ZFC |
| USER_PROCESS_CONTRACT_REQUIRED | OriginDone 未能稳定冻结 | 不继续制造 witness |
| FORMALIZATION_BLOCKED_WITH_SCOPE | 合同已固定而 proof assistant 无法保真表达 | 寻找原生演算或已证明的翻译 |

重开条件是新的一手来源、研究发起人对过程合同的明确裁定，或一个能改变 P0–P3 任一层结论的保真模型。不得通过不断增加 toy fixture 重开。

## 7. 直接调用

~~~text
按照SOP=BARE-ZFC-Q-PRECISION-SOP，继续推进，直至无法推进。
~~~

本轮已完成上述首项及 M2/M3：来源卡、H095、C-364、正负控制、主 run、精确重放和索引已进入本仓库。当前结果由 [P0/P1/P3 来源卡](../audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md) 与 [C-364 claim](../HoTT/formal/bare-zfc-q-precision/CLAIM.md) 拥有。它没有令 generic factorization 定理变成 bare ZFC 结论，也没有形成 bare ZFC 的 semantic interface theorem；按第 6 节停为 `SOURCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE`，直到出现能够改变 P0–P3 的新一手来源或用户固定新的 OriginDone 合同。
