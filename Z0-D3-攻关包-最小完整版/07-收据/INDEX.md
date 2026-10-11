# 既有收据

- `RUN.json`：W8 主运行元数据（`20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01`）。
  `exit_code: 0`，`duration_seconds: 71.68`，112 条 `#print axioms` 全部只有
  `propext`、`Classical.choice`、`Quot.sound`。
  `non_goals` 明说 D3 未证（`Z0Blocked.lean` 带未证标记、不是该运行的编译源）。
- `AXIOM_REPORT.json`：112 条公理报告。
- `environment.txt`：运行环境。

**注意**：W8 收据的 `command_argv.source` 里**没有** `Z0Blocked.lean`（它带 `sorry`，被驱动拒绝）。
你的新运行应当把证完的 `Z0Blocked.lean`（或 `Z0D3Skeleton.lean`）加进 source 列表。
