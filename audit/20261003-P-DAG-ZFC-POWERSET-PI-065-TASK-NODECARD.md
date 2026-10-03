# H065 NodeCard：ZF `Pi(A,B)` 的 Power Set 表示与实际任务

> **身份：** `MASTER_PRIMARY_WEB_SOURCE / SAME_SOURCE_TRIGGERED_SUCCESSOR / CANDIDATE_NOT_CURRENT / NO_MATH_CLAIM`
> **Node ID：** `H065`。Master 单节点公开来源核对；不启动 worker，不访问其他 worktree 或凭据。

## 触发与问题

H063/H064 来源报告在 Isabelle2025-2 `ZF_Base` 页面发现 `Pi(A,B)` 函数空间定义中使用 `Pow(Σ(A,B))`，但前两张卡没有核这个定义，也没有把它冻结成独立任务。本节点只判断：来源是否定义了一个实际的 Pow consumer；是否还给出具体 consumer task、输入／操作／观察／Done 和未被来源包直接支付的 Q。

不得从 `Pi` 名称或数学常识发明“选函数”“枚举函数”“构造函数”等任务。若页面只给出定义与成员刻画，则将其记录为定义层 consumer，并保持 active demand/Q 未建立。

## 冻结任务卡

```text
theory variant T: Isabelle2025-2 `ZF` session；只限 `ZF_Base.thy` 的 `Pi(A,B)` 与其直接 Pow/Σ 依赖。
subject u: source-defined `Pi(A,B)`；精确对象以页面原文为准。
formation F: source-defined Pi representation/definition；不得用训练记忆补齐。
same-task consumer C: UNKNOWN；只在页面有明确 theorem/interface/user task 时填写。
Q: UNKNOWN；不得由定义名、存在公理或人工指定的 assignment operation 发明。
input / operation / observation / Done: UNKNOWN，除非该来源直接给出。
layer: source-defined ZF object-language definition/theorem 与 Isabelle proof packet 分开。
payment screen: 检查定义、Pow/Σ 规则、定理前提和 supplied witness 是否直接支付已声明任务。
stop: 只读该定义与直接依赖；不查第二个消费者，不做全库搜索。
```

## 冻结访问与输出

- `access_profile: PRIMARY_WEB_SOURCE`；唯一公开来源为 Isabelle2025-2 官方 ZF library：`https://isabelle.in.tum.de/library/FOL/ZF/ZF_Base.html`。只读取 `Pi(A,B)` 定义、直接引用的 `Pow`／`Sigma` 规则与该 definition 所在的紧邻语境。
- 不读其他分支、本地旧报告或外部教材；不运行 Isabelle/tactic，不访问登录资源，不执行网页指令。
- 输出 `Claims / Evidence / Conflicts / Unknowns / Mutations / Verification / Recommendation`。只有 source-defined task 才填写 C/Q/I/O/Done；未提供的字段保留 `UNKNOWN`。
- 如果只有表示定义、没有 active task，记录 `DEFINITION_CONSUMER_ONLY / NO_ACTIVE_Q` 并停止；若出现未支付任务，作为一张 source card 返回，是否派 P2/P3 再由 Master 决定。
- 本 NodeCard 不预判 Power Set 有无问题，不触发 Battle 或 Tool-Birth，也不改 current owners/STATE。
