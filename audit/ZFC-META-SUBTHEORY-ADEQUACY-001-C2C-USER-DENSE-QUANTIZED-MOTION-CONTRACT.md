# C2C：用户稠密—量化运动合同与 source-to-spec 表

> **身份：** `C2_USER_ORIGIN_Q_CONTRACT / A_DIRECTION / PHYSICS_PREMISE_USER_OWNED`。
>
> **TaskCard：** [C2C](ZFC-META-SUBTHEORY-ADEQUACY-001-C2C-USER-DENSE-QUANTIZED-MOTION-TASKCARD.md)。

## 1. 两个固定的数学控制模型

| 字段 | dense control | quantized control |
|---|---|---|
| 起点 | normalized remaining distance `1` | eight minimum units `8`，同样规范化为总距离 `1`。 |
| operation | 每步剩余距离乘 `1/2`。 | 每步剩余 unit count取 floor half；最后一个 unit 以最小可移动单位消除。 |
| state | positive rational/real remainder `2⁻ⁿ`。 | natural number of minimum units。 |
| observation | 对每个 `n : ℕ` remainder仍正。 | explicit recurrence `8 → 4 → 2 → 1 → 0`。 |
| Done | finite stage remaining distance exactly zero。 | remaining unit count exactly zero。 |

这是一对**数学控制**，不是物理时空的测量。用户关于运动/时空量子化、普朗克尺度和现实可完成性的说法是本任务的 `USER_REALITY_PREMISE`；项目必须保留其身份，不能把这对有限模型说成已经证实那项物理前提。

## 2. 原文到规格

| 用户原文 | formal field | 保真边界 |
|---|---|---|
| “每次只走剩下路程的一半，永远走不完” | dense `remaining n = 2⁻ⁿ`；`∀n, remaining n > 0`。 | 表达每个自然数编号阶段未到达，不否定连续时间 endpoint。 |
| “现实不是稠密的，是离散的／量子化的” | explicit finite lattice with minimum unit。 | 只是受控的离散 counterpart，不是关于物理世界的 theorem。 |
| “在稠密性的空间中，无法完成现实可以完成事情” | contrast: dense no finite stage zero；quantized control reaches zero。 | 需保留相同起点/终点/half-rule的规范化比较；只能说明该 control family。 |
| ZFC问题／极限声称解决 | later `P_dense` audit。 | 当前不把模型 contrast直接归为 bare ZFC defect。 |

## 3. 已有和新增机器义务

- 已有 C-361：固定 dense partial-sum model在任何有限自然数阶段都未到 endpoint，同时闭连续时间 endpoint有正控制。
- 新 C-370：用 Lean core固定 quantized half recurrence，证明 `8 → 4 → 2 → 1 → 0` 和四步 completion，作为离散正控制。
- 二者的关系由本合同说明；它们不在同一个 proof assistant theorem中被伪装成物理结论。

## 4. C2C 判定边界

完成 C2C 后允许说：用户提出的 dense-vs-quantized motion contrast已有一组同起点／终点的受控数学模型和机器检查。仍不允许说：真实时空已被本项目证明离散、ZFC不能形式化离散运动、或极限理论的数学定理失效。
