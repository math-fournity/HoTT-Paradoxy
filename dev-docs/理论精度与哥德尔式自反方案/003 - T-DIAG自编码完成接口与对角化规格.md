<!-- governance-shard:v2
logical_id: T_PRECISION_DIAGONAL_PLAN
shard_id: 003
index: ../理论精度与哥德尔式自反方案.md
-->

# T-DIAG自编码完成接口与对角化规格

> **状态：** CANDIDATE_PROOF_THEORETIC_PROGRAM / NO_DIAGONAL_THEOREM_YET。
>
> **功能：** 将 T-OBS 的静态观察边界升级为可比较哥德尔不完备性的自反问题，但只在编码、替换、验证和 bridge 前提都被支付时启动。

## 1. 哥德尔可借的机制

Gödel式机制不是“任意自指”。它至少要求：

~~~text
Code              对象、公式、过程或任务的有效编码
Verify_T          有限验证关系，例如 Proof_T
Accept_T          T 的实际证明／完成／接受接口
quote / substitute 可实行的 quotation 与替换
diag              固定点或对角化构造
reflection        接口输出与目标判词之间的明确反射原则
~~~

### 1.1 与 GODEL-Q-REFLECTION-SOP 的模块边界

[GODEL-Q-REFLECTION-SOP](../哥德尔式ZFC完成观察反射方案SOP.md) 已经拥有实际 completion interface 的 GodelizationCard、G0--G5、正反控制和其独立闭包。T-DIAG 不复制这些卡；它把该模块放在两个更高的门之后：

1. T-OBS 必须先固定这个接口究竟压平了哪一个会改变 D 的过程差异；
2. T-Meta 必须审计其 Code、OriginDone 和 RealityMap ρ 是否仍是原任务，而不只是可进行对角化的替代任务。

所以，GODEL-Q-REFLECTION-SOP 的 G0 仍是实际 interface 的最小来源行动；T-DIAG 的新增义务是把 G0--G5 的输出接回 T 的观察精度和同一任务合同。

原始哥德尔路线以 Proof_T／Prov_T 为资格接口。T-DIAG 不假定目标一定是可证明性；它可研究完成接受接口 Accept_T。但若缺少有效编码、替换或真实 consumer，不能把一个手写递归、一次 timeout 或自然语言悖论称为 Gödel式实例。

## 2. 候选接口与对角目标

固定：

~~~text
Accept_L(e)       理论或来源指定的“e 已被接受为完成”接口
FormalDone(e)     形式模型完成
OriginDone(e)     原过程完成
Bridge_L(e)       Accept_L(e) → OriginDone(e)
~~~

候选对角任务族的形状为：

~~~text
OriginDone(D(e)) ↔ ¬ Accept_L(e)
~~~

若存在可实行 fixed point d = D(⌜d⌝)，并且 L 声称一条覆盖该任务族的完成反射：

~~~text
Accept_L(d) → OriginDone(d)
~~~

则可在明确前提下推得：

~~~text
Accept_L(d) → ¬ Accept_L(d).
~~~

这个结果的首要读法是接口不能接受 d；只有再加入一个来源支付的 completeness／total-acceptance 原则，才可能形成矛盾。它可能显示不完备、拒绝接受、反射失败或需要额外强度；不自动显示理论不一致。

## 3. 与罗素模式 P 的关系

| 层 | 罗素模式 P | T-DIAG 的加强 |
|---|---|---|
| 形成／资格 | 对象是否已形成或可用 | 编码与有限验证关系是否可表示 |
| 再入 | 对象进入自身成员判定 | code 进入 Accept_T / Prov_T 并经 diag 回返 |
| 时间 | 形成追问是否可完成 | 有限 proof / acceptance search 的全称边界 |
| 结论 | ASK 拒绝非法提问或暴露 UR | 接口必须拒绝、失去反射或暴露不完备 |

T-DIAG 不替代 P1/P2/P3；它是 P 在满足严格可表示性条件时可能出现的证明论分支。

## 4. 元层与元元层的分工

**元层**：验证 Code、Verify_T、Accept_T、substitution、diag 与对象层／元理论的导出条件。

**元元层**：验证编码是否仍是原任务；OriginDone 是否被偷偷重定义；Accept_T 是否是真实来源或实际理论接口；Bridge_L 是否已被支付。

因此，任何 T-DIAG proof package 必须附带：

1. 一个 syntax/coding source；
2. 一个 actual consumer source；
3. 一个 task-preservation card；
4. 一个 DifferentTask 反控制；
5. 一个 BridgePaid 正控制；
6. 机器证明只覆盖它实际拥有的层。

## 5. 停止条件

- CODE_OR_DIAG_NOT_REPRESENTABLE_WITHIN_FIXED_T：在明确理论/版本内编码或对角化前提失败；
- ACCEPT_INTERFACE_NOT_SOURCE_PAID：只有研究者定义的接口，没有真实来源消费者；
- TASK_BRIDGE_UNPAID：对角任务不能证明保留原过程；
- DIAGONAL_BOUNDARY_MACHINE_PROVED_WITH_SCOPE：前提成立，机器验证其不完备／反射边界；
- NO_GODEL_CLAIM：任何缺项均禁止使用哥德尔式结论。
