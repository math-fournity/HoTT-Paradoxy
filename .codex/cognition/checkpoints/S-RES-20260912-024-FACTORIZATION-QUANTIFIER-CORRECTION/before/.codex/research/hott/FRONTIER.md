# HoTT 研究前沿（S022 自反真理验证与理论经济）

本文件是当前注意力槽，不是数学结论数据库。C4 已回答用户问题但证据等级为 `PAPER_ONLY`；本轮没有 proof-assistant 或具体发散运行。

| 槽位 | 当前对象 | 状态 | 下一判别动作 |
|---|---|---|---|
| 当前用户主方向 | ERCF：理论经济化抽象与反射性自我认证何时迫使部分性、不完备或元层上升 | active-user-direction / paper-only | 明确区分 V1 proof checking、V2 normalization、V3 proof search、V4 truth/soundness、V5 internal total self-verifier |
| 第一最小可验结果 | ERCF-1/2：`α:R→A` 的任务相对 factorization、平凡任务正例与观察敏感反例 | ready-for-formalization | 选定 Lean/Agda/HoTT 片段，证明 `ParadoxWitness(α,J) → ¬FactorsThrough(α,J)`，保存源码与真实运行 |
| 战略自反深化 | ERCF-3 × W51/RP-B01：Code/quote/eval/provability/ASK 与验证器自身 | blocked-on-walking-skeleton-and-calculus | 只在 exact calculus、宇宙和 derivability 条件固定后构造 diagonal；不以一般 Gödel 口号冒充 HoTT 特有结论 |
| 最小覆盖边界 | 一致、操作语义清楚、观察规格明确而 HoTT 无法保真解释的最小理论 | open / no-witness | 区分语法可写、内部模型、保真解释和正确拒绝；非法 `U:U`/非正递归只计 `DEFENSE_WORKS` |
| 对照与历史支线 | cubical normalization 正控制、R041 bind/race、R034 native、guard/online causality | retained / not-current-first | 用于反驳过强结论和比较局部不变性；不覆盖当前用户主方向 |

判词保持：`DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。新增 ERCF 结论也必须区分实际 divergence、无总判定器和元理论不可闭合。
