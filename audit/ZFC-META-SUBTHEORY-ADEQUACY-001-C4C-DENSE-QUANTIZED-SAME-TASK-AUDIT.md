# C4C：稠密—量化模型的同一任务与完成合同审计

> **身份：** `C4_SAME_TASK_AUDIT / EXPLICIT_COMPLETION_CONTRACT_DIVERGENCE / NOT_A_CORE_VERDICT`。
>
> **TaskCard：** [C4C](ZFC-META-SUBTHEORY-ADEQUACY-001-C4C-TASKCARD.md)。
>
> **证据分母：** 用户 C2C 合同；IEP [*Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/)（2026-10-05读取，行 142–184）；C-361 与 C-370 的保存数学控制。
>
> **判词：** `SAMEQ_DENSE_QUANTIZED_REJECTED_WITH_SCOPE / EXPLICIT_COMPLETION_CONTRACT_DIVERGENCE_SOURCE_SUPPORTED / C4C_LOCAL_LEAF_CLOSED`。

## 1. 逐字段比较

| 字段 | 用户/C2C 的受控量化 Q | IEP Achilles/Dichotomy Standard Solution | 结论 |
|---|---|---|---|
| object | 规范化剩余距离；八个最小单位是离散控制。 | runner/course及由实数连续统组织的 path/time。 | `PARTIAL_ANALOGY_ONLY`：都有起点、终点和余量，但 source未把它们定义成同一状态空间。 |
| input | `remaining 0 = 1`；最小单位为 1/8。 | runner、course、constant finite positive speed、continuous path/time。 | `DIFFERENT`：IEP没有最小单位输入。 |
| operation | 每轮取余量的一半；最后一个最小单位被消除。 | continuous movement；IEP特别反对把过程理解成停下／重启的一系列离散 steps（行142–143）。 | `DIFFERENT`。 |
| observation | 对任意自然数阶段是否 `remaining = 0`。 | position/time、端点、几何级数和与实际无限子路径。 | `DIFFERENT`：C-361与C-370各自定义的观察不自动互译。 |
| `OriginDone` | 某有限自然数阶段到达零。 | 以有限正速度完成连续 course；Standard Solution认为要求最后一步／最后子路段是错误的（行166、184）。 | `EXPLICITLY_DIFFERENT`。 |

因此当前分母下无法支付 `SameQ_dense_quantized`。这不是说两个故事毫无关系：IEP 的 Dichotomy 正是 1/2、1/4、1/8 的半程结构，C2C选择该结构作为比较入口。但“共享半程叙述”没有保留同一个 `Done`。

## 2. `ExplicitTaskSwitch` 的精确范围

IEP 的 Standard Solution 仍明确以 physical motion 的语言称其为 resolution。与此同时，它把“需要 final step”归为错误的要求。相对于 C2C 所固定的 finite-stage `OriginDone`，这构成来源明示的 completion-contract difference：

```text
user/C2C Q:       Done means ∃ n : Nat, remaining n = 0.
IEP dense Q:      course completion does not require a final member of the
                  half-path sequence.
```

所以本卡可以支持：`EXPLICIT_COMPLETION_CONTRACT_DIVERGENCE_SOURCE_SUPPORTED`。它**不能**支持两个更强的句子：

- “IEP已经证明 user/C2C Q 不合理”；
- “bare ZFC 已经明确采纳并强制这种 revised contract”。

第一个需要用户现实前提与额外同一任务桥；第二个需要 M 的 actual adequacy policy，而 IEP 是应用层来源。

## 3. 强反控制已经发生

若 IEP 给出一个最小单位运动过程，并证明它的有限阶段到达等价于 continuous endpoint completion，本卡应被撤回。目前页面的内容反而更窄：它只说 Achilles 的论证在 discrete/atomistic assumptions 下不工作（行142–143），并没有定义这种过程或给出 equivalence。Arrow/Moving Rows 还表明离散条件本身不会统一消掉所有 Zeno 结构。

故本卡不会从“离散”一词推演出 `C-370`、物理量子化或普遍的 Zeno verdict。

## 4. 对 C4 的 machine-proof 义务

C-361和C-370各自已经检查 dense / quantized side。尚缺一个共同规范化的、可运行的形式命题，明确显示：在起点同为 1、终点同为 0 的两个固定 state/step rules中，`finiteStageDone` 不能被当作同一谓词。这个 formal control不会证明来源事实或 bare ZFC policy，却会防止本研究自己把两个 `Done` 偷换为同一个。

## 5. 后继

进入 **C4D：共同规范化的 dense—quantized completion divergence machine control**。该单元必须保留 C-361 的 continuous endpoint 正控制与 C-370 的 finite completion正控制，给出负控制，并明确标为 mathematical control。完成后才转 C5C 审计 M 对这种 explicit contract difference 的 adequacy responsibility。
