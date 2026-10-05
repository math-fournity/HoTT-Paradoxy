# T-DIAG-001：自编码接受与完成 bridge 的最小逻辑铰链

> **状态：** `T_DIAG_LOGICAL_KERNEL_MACHINE_PROVED_WITH_SCOPE / ACTUAL_PARENT_BRIDGE_UNPAID_WITH_SCOPE`。
>
> **上位方案：** `T-PRECISION-DIAGONAL-SOP` 的 T2/T3/T4 接合单元。
>
> **目的：** 形式化哥德尔式路线中最小但不可省略的逻辑核；它不是 bare ZFC、`set.mm`、芝诺、圆环或 HoTT H0 的实例化。

## 1. 为什么选这个单元

T-OBS-001 已经给出“指定观察投影不能决定指定判词”的抽象因子化边界。G0 又已经冻结一个真实 `set.mm` proof-acceptance interface，并重放了 Foundation 的 generic Gödel技术基线；但其 current verdict 是：proof acceptance 尚未是研究发起人关心的 `OriginDone`，且 `ρ`、internal-provability adequacy、actual diagonal 和 completion bridge 均未支付。

下一步若继续寻找更多 checker，只会重复 G0 已经关闭的来源路由。应先把以下问题机器化：**如果一个真实接口未来确实支付了这些条件，它究竟会被什么逻辑后果约束？**

## 2. 冻结的候选结构

固定一个代码域 `Code`、变换 `D : Code → Code`、自编码实例 `d : Code`、接受谓词 `Accept : Code → Prop` 与原过程完成谓词 `OriginDone : Code → Prop`。

候选前提为：

```text
fixed              D d = d
diagonalContract   OriginDone (D d) ↔ ¬ Accept d
bridge             Accept d → OriginDone (D d)
```

候选结论为：

```text
¬ Accept d
```

这不是“理论推出 False”。它只说：在一个已经拥有上述三项前提的接口里，`d` 不能被该接口接受。若另有来源支付的 total-acceptance 或 completeness 原则，才会产生进一步的反射失败／不完备性问题。

## 3. 必须被反驳或防止的偷换

| 风险 | 反控制或失败判词 |
|---|---|
| 只有自然语言“自指”，没有可实行的 `D` 和 `d` | `NO_ACTUAL_DIAGONAL_CONTRACT`；不得叫哥德尔式实例。 |
| `Accept` 只是 proof checker 的接受，却被称作原过程完成 | `TASK_BRIDGE_UNPAID`；不得推广至芝诺、圆环或 H0。 |
| `diagonalContract` 没有来源或保真编码支持 | 它只能是 abstract formal control。 |
| `bridge` 不存在 | 必须有一个正控制表明 `Accept d` 与 `¬ OriginDone (D d)` 可以相容；不得误报矛盾。 |
| 由抽象结论跳到 ZFC | `NO_BARE_ZFC_INCONSISTENCY_CLAIM` 保持。 |

## 4. 计划中的正负控制

1. **bridge 已支付的正面模型：** `Accept d` 为假、`OriginDone (D d)` 为真；对角合同和 bridge 均成立，结论只是“不能接受 d”。
2. **bridge 缺失的反控制：** `Accept d` 为真、`OriginDone (D d)` 为假；对角合同与 fixed point 可成立，但 bridge 不能被构造。它证明自编码本身不推出冲突。
3. **错误 bridge 负控制：** 在第 2 个模型中强行声称 `Accept d → OriginDone (D d)`；Lean 应拒绝该文件。

## 5. 本单元的来源与机器证明义务

候选冻结后，才允许读取并比较：

- Foundation `First.lean`/`Second.lean` 的 code、quotation、substitution 与对角化技术基线；
- G0 的 `set.mm` proof-acceptance interface 及其 internalization/adequacy gap；
- 现有 C-359、C-362、C-363、C-364 的 completion bridge controls。

机器资产使用 Lean core，并已保存 source、toolchain、正向运行、负控制、source manifest、claim matrix 与 proof-version registry。`MP-T-PRECISION-TDIAG-001` / C-368 的 primary run 是 `20261004-MP-T-PRECISION-TDIAG-001-02`；错误 bridge control `20261004-MP-T-PRECISION-TDIAG-NEG-001-01` 被预期拒绝。`-01` 保留为 capture-before-final-claim-status 的历史收据，`-02` 将 final claim/source 状态绑定到 matrix row。来源仍未把 fixed process 的 `OriginDone` 与 `Accept` 接到同一任务，故当前只能给出 `T_DIAG_LOGICAL_KERNEL_MACHINE_PROVED_WITH_SCOPE / ACTUAL_PARENT_BRIDGE_UNPAID_WITH_SCOPE`。

## 6. 禁止外推

本卡不预设也不证明：

- `set.mm` 或 bare ZFC 有一个 actual completion bridge；
- ZFC 的对象语言矛盾或一般不完备性；
- 固定 HoTT H0、芝诺或圆环是该 `d`；
- 用户的想法 T 已经整体得证；
- 任何真实系统必须接受所有代码。
