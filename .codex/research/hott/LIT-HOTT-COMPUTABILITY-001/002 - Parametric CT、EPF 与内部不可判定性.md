<!-- governance-shard:v2
logical_id: LIT-HOTT-COMPUTABILITY-001
shard_id: 002
index: ../LIT-HOTT-COMPUTABILITY-001.md
-->

# Parametric CT、EPF 与内部不可判定性

## 三种前提不能混写

固定 Coq 源码把相关原则分为：

1. `CT ϕ`：一个 monotone step-indexed interpreter `ϕ` 能为每个 total `nat → nat` 函数找到 code；
2. `SCT`：同一类解释器还支持带参数的 uniform coding；
3. `EPF`／`EPF_bool`：存在 universal enumeration of partial functions／Boolean partial functions。

`bestaxioms.v` 机器实现 `SCT → EPF`、`EPF → SCT`、`EPF → Σ ϕ, CT ϕ ∧ SMN_for ϕ` 等桥。它们说明 s-m-n、universal partial function 与 parametric CT 可以在所选 constructive metalanguage 中互相组织；不能因此把任何一个原则当作裸 HoTT 的定理。

## 当前机器提升

此前 C-208/C-218 只有 synthetic implication：若 target 可判定，则一个固定 hard complement 可枚举。新包 `MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` 在 Coq 8.13.2 中重放：

```text
EPF_bool + SCT
  → 存在 K：K 可半判定，compl K 不可半判定，K 与 compl K 均不可判定
  → ¬ decidable (compl K_nat_bool)
  → ¬ decidable (∀ n, f n = 0)
```

三个定理的 `Print Assumptions` 均为 `Closed under the global context`。这里没有隐藏全局 axiom，但 `EPF_bool + SCT` 明写在 theorem type 中。它关闭的是 `R2_CONDITIONAL_INTERNAL_NOT_DECIDABLE`，不是 `R2_AMBIENT_HOTT_UNCONDITIONAL_NOT_DECIDABLE`。

## 对机器统观的直接影响

- Oracle 应把 `synthetic implication`、`conditional internal negation`、`unconditional internal negation` 分成三类；
- GNR-4 的 universal computation 生成器必须声明 CT/SCT/EPF/SMN 哪项进入输入；
- OP-11 跨模型移植必须检查这一原则只在 reflective/modality universe 还是 ambient universe 成立；
- consumer 若把“在选定计算宇宙中有 universal enumeration”提升成“任意 univalent universe 的全局 total solver”，才形成 `B-ModelToUniverse` 候选；
- 当前尚无这条 natural consumer，也没有 ProgramCode 的无条件内部不可判定 theorem。

## 版本边界

作者 README 指定 Coq 8.13.2、Equations 1.2.3+8.13、stdpp 1.5.0。Coq 8.15.2/stdpp 1.7.0 的目标构建在 `Shared/ListAutomation.v:142` 失败；精确旧环境则成功。该差异只说明 proof script/toolchain compatibility，不能解释成数学定理反例。
