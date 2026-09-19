<!-- governance-shard-index:v2
logical_id: MATH-FOURNITY-PUBLIC-RELEASE-PLAN
mode: topical
shard_root: MATH-FOURNITY-公开仓库规划-20260919
last_shard: MATH-FOURNITY-公开仓库规划-20260919/006 - 逐阶段可执行验收清单.md
append_target: -
soft_line_target: 300
-->

# MATH-FOURNITY 公开结果包规划 — 索引

> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 5 个分片；缺一片即未完成，按表顺序读取；300 行只是软目标，不是上限。
> 当前状态：`DESIGN_REPAIRED_WITH_EXECUTABLE_CHECKLIST_NOT_IMPLEMENTED`。本规划定义公开结果包的边界、构建合同和逐阶段验收；不等于已经向 `/Users/aurolafly/MATH-FOURNITY` 导出资产、形成可公开 README、完成 CI、外部审计或 push。

本规划执行用户的公开交付裁定：读者得到的是最终结果、精确命题、可复现机器证据、明确边界与开放问题；不必消费用户—AI 对话、四件套、dev-notes、治理过程或调试失败史。

<!-- governance-shard-table:start -->
| Shard | 文件 | 语义范围 | 状态 |
|---|---|---|---|
| 001 | [目标、受众与结果边界](<MATH-FOURNITY-公开仓库规划-20260919/001 - 目标、受众与结果边界.md>) | 公开包目的、读者路径、结果定义、排除边界与当前现场 | current |
| 002 | [发布清单与证据单位合同](<MATH-FOURNITY-公开仓库规划-20260919/002 - 发布清单与证据单位合同.md>) | manifest-first、10 个候选公开证据单位、范围枚举、证据/许可证字段与排除规则 | current |
| 003 | [可移植重放与 CI 合同](<MATH-FOURNITY-公开仓库规划-20260919/003 - 可移植重放与 CI 合同.md>) | 相对路径 replay runner、输出比较、CI、故障语义与安全边界 | current |
| 004 | [公开文档、语言与读者路径](<MATH-FOURNITY-公开仓库规划-20260919/004 - 公开文档、语言与读者路径.md>) | 三语入口、结果优先文档、术语/来源/身份与最小治理入口 | current |
| 005 | [阶段、验收与发布闸门](<MATH-FOURNITY-公开仓库规划-20260919/005 - 阶段、验收与发布闸门.md>) | 阶段顺序、验收矩阵、身份/许可对齐、外部审计与 push 边界 | current |
| 006 | [逐阶段可执行验收清单](<MATH-FOURNITY-公开仓库规划-20260919/006 - 逐阶段可执行验收清单.md>) | P0–P4 的 check ID、输入、行动、oracle、证据、失败状态、恢复和越阶禁止 | current |
<!-- governance-shard-table:end -->

## 本索引的即时结论

- 旧计划的“10 个核心 run”改为 **10 个公开证据单位候选**；一个单位可包含主证明和必要的最终负向控制，不能用模糊的文件计数替代清单。
- 旧 `RUN.json.command_argv` 和 `compile.sh` 含本机绝对路径，不能原样承诺 GitHub Actions 重放；公开包必须先实现并验证独立的可移植 replay runner。
- 公开仓库当前只有占位 README 与 MIT LICENSE；其本地 Git 身份已是 `Math Fournity <math-fournity@proton.me>`，但对外文本、LICENSE 与 CITATION 尚未同步，不能宣称发布准备完成。
- P0 的规划与逐阶段 checklist 已完成；P1–P4 的每一个 check 仍是 `NOT_STARTED`，不能因本清单存在而提升公开包、CI、同行评审或发布状态。
- 本轮只更新本规划及项目级发现入口；未修改 `/Users/aurolafly/MATH-FOURNITY`、未导出源码、未 commit、未 push。
