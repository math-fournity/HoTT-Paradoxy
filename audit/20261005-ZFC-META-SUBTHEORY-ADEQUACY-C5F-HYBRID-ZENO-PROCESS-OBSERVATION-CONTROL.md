# C5F：混合系统的 Zeno execution 作为过程观察正控制

> **身份：** `CORE_ADEQUACY_TASK_CARD / C5_POSITIVE_COMPARISON_CONTROL / PROCESS_OBSERVATION_FORMAL_THEORY_SOURCE / NOT_A_ZFC_FAILURE_WITNESS`。
>
> **父方案：** [ZFC-META-SUBTHEORY-ADEQUACY-SOP](../dev-docs/ZFC元理论子理论充分性最终闭环SOP.md)。
>
> **冻结来源：** [C5F snapshot manifest](../sources/external/zfc-meta-subtheory-c5f-20261005/README.md)。

## 1. 为什么需要这个正控制

用户关于 ZFC 的问题不是“任何理论都必须拒绝无限”。更精确地说，是一个基础／模型是否有能力并有责任在某个过程语义中区分：

```text
formal or limit-level result
versus
an actually admissible / complete process with a specified observation contract.
```

若没有一个真实理论会把这种区分当正式对象，`ProcessCompletionAudit` 就可能只是本项目自造偏好。C5F 检验这一点。

## 2. Zheng 技术报告的实际模型责任

Zheng 的 Berkeley EECS 技术报告将 Zeno hybrid execution 定义为：在有限时间区间发生无限个离散 transitions。它进一步说：

1. physical systems 的宏观动力学通常连续，但 hybrid abstractions可能产生 Zeno models；
2. 某些 classical Zeno models 对被建模系统的 dynamics 描述不完整；Zeno behavior 是这种 model incompleteness 的信号；
3. 因此通过引入 post-Zeno states、guards、resets 和 post-Zeno dynamics 来**补全**模型；
4. simulation 在 Zeno point 附近必然 halt，因为 discrete event handling takes non-zero finite computation time；完整模型再允许近似模拟越过 Zeno point。

这给出一个来源固定的 `ProcessCompletionAudit` 实例：

```text
HybridModel H
  + infinite discrete transitions in finite time
  + implementation / simulation observation
  ⇒ H is potentially incomplete,
     not merely a formally valid finished description.
```

模型的补全不是重新命名 “resolved”，而是添加 post-Zeno states 与 transition data；报告还明确承认某些 post-Zeno dynamics 需要 model designer 的额外分析，且可能不唯一。

## 3. 它对 bare-ZFC 研究的精确作用

| 比较项 | hybrid-system source | ZFC-supported Standard Solution source | 允许的结论 |
|---|---|---|---|
| 被观察的过程 | discrete transitions / Zeno time / simulation behavior | continuous path / point-events / calculus / revised completion | 两种过程语义不同，不能直接当作同一 Q。 |
| 异常判词 | Zeno behavior may reveal model incompleteness | no-last-action intuition is revised away | `ProcessCompletionAudit` 是真实理论职责的例子。 |
| 修复 | explicit post-Zeno states、guards、resets、dynamics | revised completion contract / continuous model | 都需要说明新增或改变了什么；不能以相同词“completion”合并。 |
| 对 ZFC 的作用 | 不依赖 ZFC source role | ZFC is foundation for math resources | 证明可有过程敏感 formal theory；不证明 bare ZFC 有矛盾。 |

因而 C5F 支持用户方向中的一个受限、重要结论：**理论可以把“过程是否真完成／模型是否遗漏 post-limit dynamics”做成正规形式语义问题；这不是不可形式化的感性直觉。**

它不支持：

```text
Hybrid Zeno = IEP runner task
Hybrid-model incompleteness = bare ZFC inconsistency
Discrete transitions finite time = all continuum motion impossible
```

## 4. C5F 判词

```text
PROCESS_COMPLETION_AUDIT_HAS_REAL_FORMAL_THEORY_PRECEDENT
ZEN0_BEHAVIOR_CAN_BE_MODELED_AS_ABSTRACTION_INDUCED_INCOMPLETENESS
EXPLICIT_POST_ZENO_COMPLETION_IS_A_POSITIVE_REPAIR_PATTERN
NOT_SAME_Q_AS_STANDARD_ANALYSIS_RUNNER
NOT_A_BARE_ZFC_FAILURE_WITNESS
```

## 5. 对最终形式化的作用

C5F 给 C6 留下一项强 `Control+` 规格：若主张一个模型／基础具有过程完成观察力，不能只存一个 Boolean `resolved`；至少应能区分 Zeno-style transition accumulation、Zeno point、pre/post state以及 model-completion data。它不要求把 hybrid automata 偷换成 ZFC 或 HoTT，而是要求未来的 source-to-spec table 明确哪一层被保留。

## 6. successor

当前 [C0 successor reselection 002](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-002-TASKCARD.md) 保持不变：找同一 actual M/S/Q/P/Adequacy source chain。C5F 是正控制和比较语义，不是这条 chain 的替代；它防止我们今后把 `ProcessCompletionAudit` 误报为无法理论化的要求。
