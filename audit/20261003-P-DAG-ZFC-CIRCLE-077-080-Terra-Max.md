# P-DAG H077–H080：极限、完成定义与圆环 Q0 的来源 Battle

> **身份：** `SOURCE_TASK_CONTRACT_BATTLE / EXPLICIT_DONE_SUBSTITUTION_CONTROL / USER_DONE_ADJUDICATION_REQUIRED / NOT_A_ZFC_INCONSISTENCY_OR_Q_CONVERGENCE`。
>
> **结论范围：** 这组来源证明一个真实的哲学／解释分歧已经被定位：标准连续统回应可以显式改写完成条件；批评来源可以把极限的静态定义与“是否到达”分开。它不证明哪一方的完成准则正确，不证明 ZFC 有矛盾，也不证明原圆环过程已被任一来源完整回答。

## 1. DAG 与输入失败的完整谱系

| 节点 | 角色 | 终态 | 对本卡的作用 |
|---|---|---|---|
| H077 | Norton source-match | `PASS` | 得到一个实际 C/I/O/Done source contract；其支付方式是**显式删除**最后动作条件。 |
| H078 | Bathfield + Sierpińska source-match | `PASS` | 将两位批评者限定为哲学／教育诊断；它们不提供 ZFC 矛盾或普遍连续模型否定。 |
| H079 | Battle 首次 prelaunch | `INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT` | prompt少了 runner要求的精确 profile marker；未借认证、未启动App Server、未采样。 |
| H080 | H079 的唯一功能修复重跑 | `PASS` | 独立仲裁：争点是 Done 的定义／解释桥，不是数学事实冲突。 |

H079保留而不覆盖，避免把一次采样前输入合同失败伪装成理论或模型结论。H080的唯一变化是 prompt 第一行加入精确 `P-VALIDATION` marker；source pack、TaskCard、non-goals与问题保持不变。

## 2. 三组来源事实

### A. Norton：一个实际的完成合同，但它显式改变 Done

[John D. Norton 的大学课程文本](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html) 将 runner 的困难表述为无限多个 passing actions。它先写有限情形的 `Done_strict`：所有动作，包括最后一个动作；再以无限序列无最后项为理由，把它替换成 `Done_revised`：做完所有动作，不再要求最后动作。它还给连续时间模型中各半程通过时刻赋值 (1/2,3/4,7/8,ldots)。

H077的关键不是“它证明了用户的圆环完成”，而是它使 contract 差异显式可见：

```text
Done_strict  = all actions, including a last terminating action
Done_revised = all actions, with no last-action requirement
```

H077确认Norton提供了真实来源中的 `C/I/O/Done`，但该来源以改写完成准则支付自己的解答；它没有声称此改写等于用户原圆环的来源保持／实际复原 Done。

### B. Bathfield 与 Sierpińska：极限公式与“达到”问题分层

[Bathfield 2018 的 PhilSci-Archive 记录](https://philsci-archive.pitt.edu/16355/)讨论常见“收敛几何级数解决芝诺”的说法，并把“有极限”与顺序 supertask 的终止操作分开；[Sierpińska 1990](https://flm-journal.org/Articles/43489F40454C8B2E06F334CC13CCA8.pdf)把 Weierstrass 的 ε–N 定义与“一个序列是否达到极限”的问题分开，指出形式化可能把后一问从数学问题中移走。

H078的范围判词是：二者提供的是**对解释桥的批评**，不是一条 ZFC 内部定理、不是对所有连续路径的反例，也不是物理离散性的证明。

### C. 连续端点模型是必须保留的第三项控制

既有项目 C-269/C-272 的来源记录给出一个在闭时间区间上有明确末时刻的连续几何控制；它禁止将这场 Battle 写成“只要使用连续统就必然没有末态”。该记录本轮未重跑，仍只按其既有范围作为 `SOURCE_REPORTED_CONTROL`。

## 3. H080 的裁决：不是数学冲突，是完成合同的分叉

H080将A、B与控制卡对照后得到四个可被直接复核的结论：

1. Norton、Bathfield与Sierpińska没有在冻结材料中对同一数学事实相互矛盾。
2. Norton没有悄悄把 `Done_strict` 说成 `Done_revised`；删除最后动作条件是显式的。
3. Bathfield与Sierpińska没有证明极限数学错误；它们质疑的是从 `Done_formal`（极限／级数）到 reaching／sequential completion 的解释升级。
4. 一个有明确终点的连续路径是额外的、被声明的 contract，不能由任一方自动与每一种 action-sequence Done 等同。

因此，Battle 的 Master verdict 是：

```text
SOURCE_TASK_CONTRACT_SPLIT
Done_strict / Done_revised / Done_formal are not source-established as the same task.
The completion-condition change is explicit in the standard-response source.
USER_DONE_ADJUDICATION_REQUIRED before any same-task UR or ZFC claim.
```

这不是把决定推回研究发起人以逃避工作。相反，三种 Done、它们的来源、何处发生替换、以及什么事实能推翻当前判词都已冻结。剩下的是一个确实属于原任务的哲学／现实契约裁决：原圆环／芝诺过程究竟要求哪一种 Done，或者是否需要一个额外的连续端点桥来把它们接回同一任务。

## 4. P1/P2/P3 与 QConvergenceLink

| 刀 | H077–H080 给出的结果 | 不能写成什么 |
|---|---|---|
| P1 | Norton提供一个实际 completion consumer contract；它的输入、观察与两种Done可冻结。 | `Done_revised`自动等于用户原Done，或一个source已经给出ZFC Q。 |
| P2 | 三个来源均无同一对象的 formation–reentry；`NOT_APPLICABLE`是正确结果。 | 因为有无限动作或极限就有罗素式自指。 |
| P3-C | 解释桥是明确的考察对象：Norton改写Done，批评来源指出形式化避开reaching，连续端点模型需额外contract。 | 静态极限定义、某次证明或外部时间自动构成理论内生命周期。 |

```text
ZFC-CIRCLE-Q0 global state = Q-1_SEED (retained)
H077 control              = C_LANE_TASK_SWITCH_CONTROL
H078 control              = CRITICAL_BRIDGE_DIAGNOSIS / NO_FORMAL_CONSUMER
H080 effect               = Q_NARROW
Q-2/Q-3/Q-4               = not reached
Power Set station          = unchanged; S3 competition check remains incomplete
P calibration              = unchanged; source-match/Battle is not blind CAL promotion
```

H077使“一个实际来源正在说 completion”变得可定位；但它同时显式付款为另一个Done，因此没有留下 P1 的未支付正义务。H078的批评也不能独自形成C-lane。全局Q1保留，是因为尚可检索其他来源／解释桥；但当前两边都不足以使卡跨入共同Q。

## 5. 运行与 trajectory 收据

| 节点 | 实际 actor / permission | public final SHA-256 | private wire terminal | L1–L5摘要 |
|---|---|---|---|---|
| H077 | `gpt-5.6-terra / max`；readOnly、never、network false、0 tool/file/approval | `b78454bc79d908e27403109eb9715af072fa5b00942495d5e991e6b17621f453` | `wire.jsonl:998` | L1完整AGENTS body未从wire认证；L2预期为零；L3回显source card；L4由Master复核；L5仅node范围PASS。 |
| H078 | `gpt-5.6-terra / max`；readOnly、never、network false、0 tool/file/approval | `7e7b61ed71b42021e0d64f84ab4138d336a33e2c4bd070d406196910453c3ce9` | `wire.jsonl:1093` | 同上；输出只支撑冻结批评来源的范围。 |
| H080 | `gpt-5.6-terra / max`；readOnly、never、network false、0 tool/file/approval | `85c756adf5c72df63a35ba1fdbdc2c705ad50728be7f70ed4b2b1332f183535a` | `wire.jsonl:957` | 同上；仲裁只在sealed pack上作公开contract comparison。 |

每个direct App Server wire都通过 catalog→tree→tail / final inspection的轨迹审计。private raw、prompt、AGENTS与reasoning summary留在0600隔离目录；本报告不复制隐藏reasoning，也不从final反推其内容。

## 6. 下一项最小行动与停止条件

下一动作不是继续扩大“所有极限理论”的控诉，而是二选一的可证伪来源行动：

1. **同一任务路径：**固定一个圆环／连续运动来源，要求它同时给出原 $M$、允许操作、连续端点或离散端点、观察和Done，再检查它是否将`Done_formal`与此Done直接同一化；
2. **有界负路径：**若后续来源都像Norton一样显式改写Done，或像SEP一样公开保留物理桥，则把它们收为`SOURCE_BRIDGE_DEFENSE / TASK_SWITCH_EXPLICIT`分母，不再称为ZFC的问题。

无论哪条发生，原用户的圆环原文、C-269/C-272控制和本报告的三种Done都必须保持；不能删去其中一项以制造命中。

## 7. Delta SelfAuditCard

```text
source units
  = user circle/Q0 primary; Norton; Bathfield; Sierpińska; C-269/C-272 control;
    H077/H078 public MatchTraces; H079 preflight receipt; H080 Battle.
original requirement
  = use the circle to examine whether continuum completion is being treated as
    the original completion, while preserving the task and not calling a theory
    contradictory from a slogan.
actual action
  = separate standard response, criticism, endpoint control, and three Done
    contracts; run two source-match nodes and a bounded source Battle.
alignment verdict
  = ALIGNED. A real source disagreement was narrowed to its actual contract
    difference; P2 was not forced; the continuous positive control remained active.
deviation
  = H079 INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT: profile marker was not exact.
repair
  = H080 changed only the marker and retained the frozen source pack; terminal
    run then passed. No theory/source verdict is derived from H079.
pattern-universe / Tool-BirthCard
  = OLD_TOOL_FIELD_GAP = NO. P1 and P3-C already express the source/bridge
    distinction; P2's non-applicability is a control, not an uncontained pattern.
QConvergenceLink
  = global Q-1 retained; source subcards Q_NARROW; no Q-2/Q-3/Q-4;
    C_LANE_TASK_SWITCH_CONTROL is not Candidate-Q.
station / calibration
  = no Power Set station change; no CAL upgrade; S3 remains incomplete.
falsifier / next trigger
  = a fixed source with the original M, allowed operation, O and Done that
    treats formal completion as the same task without an explicit bridge/payment.
```
