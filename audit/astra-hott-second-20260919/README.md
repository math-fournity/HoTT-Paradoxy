# GLM 修复的第二次独立审计证据

本目录固定 HoTT/Cubical Agda 三项修复的重复执行、依赖检查及外层收据校验器的有限正反控制。它不注册新数学主张，不将合成控制视为证明，不修改正式证明源、历史收据或 canonical 状态。

报告入口：[Astra对击落HoTT工作的第二次审计](../../Astra对击落HoTT工作的第二次审计.md)。本目录脚本为 `HUMAN_EDITED`；JSON/原始输出为脚本产生的 `DERIVED_VERIFICATION_RECEIPT`，不构成新的 MACHINE_MANAGED_CANONICAL 数据库。重新捕获使用新的输出位置；不手工把 FAIL 改为 PASS。

| 文件 | 用途 |
|---|---|
| [audit_repairs.py](audit_repairs.py) | 原 argv 重放三新证明，校验三新十旧收据，快照与显式 import 闭包检查 |
| [SUMMARY.json](SUMMARY.json) / [REPLAYS.json](REPLAYS.json) | 3/3 精确重放、运行时长、依赖范围 |
| [VERIFIER-RESULTS.json](VERIFIER-RESULTS.json) | 当前十三次静态校验；旧十份 7 PASS / 3 FAIL |
| [INPUT-BEFORE.json](INPUT-BEFORE.json) / [INPUT-AFTER.json](INPUT-AFTER.json) | 受审代码/报告/run 的基线与哈希；重放中未变 |
| [COGNITION-REATTESTATION.json](COGNITION-REATTESTATION.json) | 四件套 25 文件同档位复认；哈希不认证理解 |
| [check_pragma_controls.py](check_pragma_controls.py) | 隔离合成控制，真实调用当前 verifier 与 Agda |
| [PRAGMA-CONTROLS-v2.json](PRAGMA-CONTROLS-v2.json) | 有效三控制和强制 safe 对照；确认注释 pragma 误接受 |
| [PRAGMA-CONTROLS.json](PRAGMA-CONTROLS.json) / [synthetic-verifier-controls/](synthetic-verifier-controls/) | 首次 setup 因使用保留字失败；保留原件，不作为所审计缺陷证据 |
| [synthetic-verifier-controls-v2/](synthetic-verifier-controls-v2/) | 修正标识符后的最小 Agda 文件、合成 RUN/index；不是正式主张索引 |
| [collect_context.py](collect_context.py) / [CONTEXT-SOURCES.json](CONTEXT-SOURCES.json) | 补充文档/原典/代码身份与 scoped 检查 |
| [CONTEXT-CHECKS.json](CONTEXT-CHECKS.json) / [BASELINE-MATRIX-EXCERPTS.json](BASELINE-MATRIX-EXCERPTS.json) | Git 差异、原矩阵登记、版本与治理检查 |
| [checks/](checks/) | 每次独立执行的命令、exit、stdout、stderr 与 digest |

执行工具链沿用受审 run 固定的 Agda 2.8.0-3d04bac / Cubical v0.9。新验证器控制输入只有合成类型声明，无账号、网络服务或他人系统操作。该控制显示 Python 审核规则的误识别；Agda 强制 safe 对照正确拒绝公设。
