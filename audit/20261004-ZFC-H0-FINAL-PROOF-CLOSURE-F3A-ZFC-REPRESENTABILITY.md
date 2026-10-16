# ZFC-H0 总证明闭环：F3-A ZFC 过程可表示性的开源正控制

> **身份：** `RESEARCH_COGNITION_CLOSURE / M3_BARE_ZFC_INTERFACE / EXTERNAL_SOURCE_AND_KERNEL_POSITIVE_CONTROL`。
>
> **问题：** bare ZFC 是否因为缺少“时间维度”而不能表示 H0/A 所需的步骤、序列和过程合同？还是 Q 的候选缺口发生在已有表示被用来作基础验收时的观察/提升政策？

## 1. 本项目自己的先验判断

在读取外部 formalization 前，F3 的必要区分是：

```text
语言/模型可表示 Process、Trace、OriginDone
≠
某个 foundation-facing acceptance policy 必然检查 FormalDone → OriginDone
```

若 ZFC formalization 能定义 `ω`、函数和序列，则“ZFC 没有过程表示能力”应当被排除；剩余的 Q 问题只能是对同一过程的观察、bridge payment 与充分性提升。反过来，单有 sequence encoding 也不证明任何数学共同体或 ZFC policy 已支付 completion bridge。

## 2. 学术与开源代码调查

冻结外部来源：

```text
FormalizedFormalLogic/Foundation
commit f3972f4204fc61e1b736ed843415894c83f35508
Lean toolchain leanprover/lean4:v4.34.0
```

已直接审读的源码给出以下可定位事实：

| 文件 | 源码事实 | 对 F3 的作用 |
|---|---|---|
| `ZF/Basic.lean` | `𝗭𝗙` 与 `𝗭𝗙𝗖` 是明确的 first-order set-theory theories。 | 固定实际 object-language target，不用“ZFC”作泛称。 |
| `ZF/ZF.lean` | 对任意可定义函数/关系给 Replacement image 的存在与可定义 construction。 | 表明模型层可用函数图/Replacement 构造集合对象。 |
| `FunctionSet.lean` | 定义函数集合、domain/range、function graph 与可定义性。 | 函数图并非只能在元语言口头描述。 |
| `Recursion/Seq.lean` | `Seq` 是函数且 domain 为 ordinal；给 length、entry、append 和相关 definability。 | 有版本固定的集合论 sequence/process carrier。 |
| `Universe.lean` | 构造一个 set-theoretic universe model，并定义 `ω`。 | 给 model-level positive-control route；它不是 bare ZFC object-language theorem 的替代。 |

Metamath 的 `set.mm` 同样把 ZFC 作为 first-order axioms，并公开 Replacement、Power Set、Infinity 等公理的形式化。这是独立的架构正控制，不是本项目对 Metamath 运行的证明。

## 3. 先实际编译，再作范围判断

在来源阅读之后，先对自己的判断作了可失败的实现尝试：如果 Foundation 的 `Seq` 只是
文档中的名字、不能在它声明的 Zermelo model interface 下通过 Lean，或者阶段值不具唯一性，
则“可表示性正控制”不能成立。为避免把依赖安装成功误作证明，我执行了两层实际检查：

1. 外部 checkout 在原 commit 的 `lake-manifest.json` 恢复为 Git 原字节后，
   `lake build Foundation.FirstOrder.SetTheory.Recursion.Seq` 成功完成 1,071 个 build jobs；
2. 项目内的 `H0ProcessRepresentation.lean` 用该 checkout 的 `leanprover/lean4:v4.34.0`
   实际检查 `Seq` 的 ordinal domain、in-domain stage 的唯一值、`nth` graph membership、
   `Seq` predicate 与 `lh` function 的定义性。主运行打印五个声明均依赖
   `propext`、`Classical.choice` 与 `Quot.sound`，且每个定理都以
   `[V↓[ℒₛₑₜ] ⊧* 𝗭]` 为**参数**；它没有在运行中构造 Zermelo model。

反控制 `WrongH0ProcessRepresentation.lean` 保持相同的模型假设和同一 in-domain stage，
却要求两个不同 stage value。Lean 在 `value ≠ value` 的义务处拒绝该构造。这个拒绝只核验
函数图的唯一值属性；它不能被读成关于运动、连续时间、H0 语义或 ZFC 一致性的命题。

首个 capture 误经用户默认 elan launcher 选择 Lean 4.34.1；它保留为历史运行 `-01`，不作主证据。
随后 capture 固定 project-local 4.34.0，又把 external Lake project 通过 `lake --dir` 调用，令
实际命令以 canonical project-relative source path 记录。主运行 `-04` 和负控制 `-04` 因而同时通过
kernel check、external-tree hash、matrix-row freeze 与 selected proof-evidence verifier。

## 4. 当前结论与边界

```text
ZERMELO_MODEL_PROCESS_REPRESENTABILITY_POSITIVE_CONTROL_MACHINE_PROVED_WITH_SCOPE
M3_LANGUAGE_ABSENCE_ROUTE_REJECTED_WITH_SCOPE
M3_ACCEPTANCE_POLICY_STILL_UNPAID
```

C-366 的具体 carrier 是 Foundation 的 **Zermelo** model interface `𝗭`，不是本项目在对象语言内
新证明的 ZFC theorem。这个范围反而足以排除一个更强的反表示说法：若较弱的 Zermelo interface
已经能表示 ordinal-indexed sequence graph，则不能用“bare ZFC 没有原生时间符号”推出它不能表示
离散阶段、轨迹或阶段值。

这不是“ZFC 已经有足够 Q”。它只排除了一个过强读法：不能再由“没有原生时间符号”推出“不能在集合论中表示 `runFor`、序列、函数或过程合同”。要提出 bare-ZFC precision conclusion，仍须固定一个 `C_accept` 或 formal acceptance interface，说明它面对这些已可表示对象时究竟观察、忽略还是支付 `FormalDone → OriginDone`。

## 5. 可复核证据与下一最小动作

主包与控制：

- `HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation.lean`；
- `HoTT/formal/zfc-h0-final-closure/WrongH0ProcessRepresentation.lean`；
- `HoTT/formal/zfc-h0-final-closure/H0ProcessRepresentation-CLAIM.md`；
- 主运行 `HoTT/verification/runs/20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-04/`；
- 负控制 `HoTT/verification/runs/20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001-04/`；
- `MP-ZFC-H0-PROCESS-REPRESENTATION-001 / C-366` 的 claim matrix 与 proof-version registry 行。

下一动作不再是继续寻找 sequence encoding。M3 的余项是找出一个**版本固定、bare-ZFC-facing 的
acceptance interface**，或在冻结的语义来源分母内给出该接口未被定义的有界结论；它必须明确
`Represent / FormalDone / OriginDone / Observe / Reject / BridgePaid / AdequacyLift`，并证明或拒绝
其与实际来源 owner 的关系。单凭 C-366 不得继续制造新的过程编码 fixture。

## 6. 入口

- [Foundation repository](https://github.com/FormalizedFormalLogic/Foundation)
- [Foundation ZF source tree at the frozen commit](https://github.com/FormalizedFormalLogic/Foundation/tree/f3972f4204fc61e1b736ed843415894c83f35508/Foundation/FirstOrder/SetTheory)
- [Metamath ZFC formalization overview](https://us.metamath.org/mpeuni/mmset.html)
