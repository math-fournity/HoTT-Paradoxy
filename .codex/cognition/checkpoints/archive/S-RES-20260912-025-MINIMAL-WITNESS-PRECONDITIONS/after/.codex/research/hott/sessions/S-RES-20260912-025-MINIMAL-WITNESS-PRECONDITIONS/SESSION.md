# S-RES-20260912-025-MINIMAL-WITNESS-PRECONDITIONS

- 触发：C4 最终复读发现 E₀ 使用 `(a,s₀),(a,s₁)` 却未显式假设 `a:A`，并把有限任务族过快写成可判定。
- 修正：给出 `a₀:A` 与 `s₀≠s₁:S`；一般 factorization 保持 proposition-level，只有额外有限类型/可判定相等等结构时才宣称可执行判定。
- 影响：C4/source+merge manifest/STATE source hashes/恢复入口更新；core generation-4/36 KC 和 ERCF 主方向不变。
- 数学状态：`PAPER_ONLY`；proof assistant 未运行。
- Git：未 commit、未 tag、未 push。
