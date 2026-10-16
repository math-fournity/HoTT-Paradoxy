# S-GOV-20260914-145-R2-REGRESSION-SEMANTICS

- 类型：S144 后的语义 regression corrective。
- 触发：专项 test 仍固定旧的无条件 R2 no-decider 目标句，和当前 scoped 结论冲突。
- 修正：断言 R2 synthetic dual-kernel 状态、精确定义 `decidable P→enumerable(complement SBTM_HALT)` 与 C-214–C-218。
- 验证：`test_hott_programmatic_exploration_completeness.py` 5/5 PASS。
- 数学：C-208–C-218 源码、run、索引与判词均未改变。
- 下一步：继续 `goal.md` 三向薄切。
