# S-GOV-20260913-MACHINE-OVERVIEW-M1-AUDIT-FIX

- 目标：完整读取外部 M1 审计（`20260913-M1自动化统观实现审计` 索引 + 3 分片 + 复现包），独立复现 F1–F7，修复协调器缺陷，重跑验收，保留全部失败历史。
- 独立复现（修复前，本 worktree）：F1 源码哈希 FAIL 仍 `PROFILE_QUALIFIED`；F2a 记录 `77b04fc6…` 而实际文法 `2b9d1b0e…`（252 checks）；F2b 跨版本见证在 stub kernel 下仍得 `NATIVE_CHECKED_CALIBRATION_INSTANCE`；F3 删除内核 stdout 后 `validate=VALID`；F4 旧 review 把纯 race 值差异写成 continuation 发散；F5 `deadline_horizons=[2]` 下缩减产生 6 个越界见证；F6 `max_checks=1` 同时 `truncated=true` 与 `complete=true`；F7 缓存路径故障留下无 RUN.json 半成品、validate 仍 VALID、同 ID 重试失败。
- 修复：profile 判定纳入源码 FAIL 并锁 support 模块（profile v1）；`load_case_inputs` 统一重核 profile/task/grammar；verify 绑定 (case revision/hash, search run id+sha, witness AST sha, target freeze ledger)；`validate` 从产物与哈希重算有效性并识别 legacy/interrupted；缩减强制文法成员资格；完整性字段与预算/捕获截断分离；`ATTEMPT.json` 生命周期 + 内核超时/进程组终止 + 负控制诊断分类 + 重放分级（冷/暖缓存日志差异）。
- 审计前旧收据：7 个 run 加 `LEGACY.json` 保留并校验；3 个错误 review 移入 `reviews/.superseded/`（字节不变）。
- post-fix 验收：`selftest` 29/29；case rev-3 + search `20260913-SEARCH-L1-003`（4,788/4,788，50 见证，三族 14/28/8，complete=true）；三族 post-fix 原生核验 `...POSTFIX-DEADLINE/VALUE/COMPLETION-001` 全部 `NATIVE_CHECKED_CALIBRATION_INSTANCE`、0/0/42/0、重放 EXACT；`validate` VALID（11 runs，7 legacy，1 interrupted）；跨版本 verify、陈旧文法 search、postulate 证明、缺失内核输出、稀疏文法、预算截断、中断恢复、价值族解释共 8 类负向场景全部准确拒绝/标记。
- 诚实边界：仍无新数学 claim；现实桥梁 `UNRESOLVED`；M2–M5 未实现；内核超时路径用 `/usr/bin/yes` 受控测试（1 s）而非真实长证明；缓存状态未在 profile 声明。
