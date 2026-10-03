# H064 NodeCard：ZF 对幂集满射问题的实际 source consumer

> **身份：** `MASTER_PRIMARY_WEB_SOURCE / SAME_SOURCE_TRIGGERED_SUCCESSOR / CANDIDATE_NOT_CURRENT / NO_MATH_CLAIM`
> **Node ID：** `H064`。Master 单节点公开来源核对；不启动 worker，不访问其他 worktree 或凭据。

## 触发与问题

H063 在 Isabelle2025-2 的 `Univ` 源码中找到累积层级递归对 `Pow` 的实际使用，但 successor-stage 集合的存在由 ZF 的 `Pow` axiom/定义直接支付，源码没有暴露独立的运行任务或未完成 Q。H063 的范围外同页搜索摘要出现 `ZF_Base` 中的 `cantor` 定理标题；这是新的、同源可核的 Power Set 消费任务，故新增此串行节点，而不扩大 H063 的冻结卡。

本节点只核当前 Isabelle2025-2 `ZF_Base` 页面中的 `cantor` theorem：它是否以 `Pow(A)` 为对象域/值域，形成真实的同层任务；理论给出什么输入、操作、观察与 Done；对“能否枚举 Pow(A)”的提问，来源是新开一个未付 Q，还是已经直接给出答案。

## 冻结任务卡

```text
theory variant T: Isabelle2025-2 Session ZF / source ZF_Base.thy; 不外推到 ZFC 其他库、runtime 或现实程序。
subject u: Pow(A)（仅按 theorem source 的精确变量和类型）。
formation F: 当前 ZF_Base 对 Pow 与 Pow_iff 的 axiomatic declaration。
same-task source consumer C: 当前页面的 Cantor theorem 及其直接 proof text。
candidate Q: 对给定集合 A 与函数候选 b，b 是否可将 A surject onto Pow(A)；此问是否由 source 直接回答。
input / operation / observation / Done: source 未检查前全部 UNKNOWN。
layer: Isabelle/ZF object-language theorem statement + proof packet；proof tactic/runtime 行为分开记。
controls: Pow 的 membership rule/存在身份；有限/空集边界只在当前 theorem source 已给出时使用；不另造现实算法控制。
success: 精确定位 theorem statement、source proof、Q 的 direct-payment status 与禁止外推。
stop: 只读该 theorem 及定义它直接依赖的 Pow/集合形成源；不再寻找第二个 Cantor/choice/universe consumer。
```

## Frozen access/output policy

- `PRIMARY_WEB_SOURCE`，唯一资料根为 Isabelle2025-2 官方 ZF library：`https://isabelle.in.tum.de/library/FOL/ZF/ZF_Base.html`；可读取当前 `ZF` session index 已指向的该页面，不跟随非必要链接。
- 只读取 theorem 陈述、直接 proof block、`Pow` declaration/characterization 与定义 theorem type 所必需的 ZF source。禁止用数学教科书重述补齐源码中未出现的运行语义；不运行来源里的证明脚本。
- 返回 `Claims / Evidence / Conflicts / Unknowns / Mutations / Verification / Recommendation`；P1/P2/P3 字段缺证仍记 `UNKNOWN`。如果 Q 被 source 直接回答或 packet 直接支付，P2/P3不启动。
- 本节点只产生 source-inspected evidence；无 proof assistant run、无新数学结论、无 current-owner 或 STATE/Feature/MEMORY/rulings 修改。
