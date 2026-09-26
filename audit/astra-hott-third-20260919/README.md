# GLM 第二次回复与修复的第三次审计证据

本目录保存三份已有Agda命令的重复执行、十份代表性收据的当前静态校验、六个合成选项控制与逻辑审计的来源身份。报告入口：[第三次审计](../../Astra对击落HoTT工作的第三次审计.md)。控制是验证器正确性测试，不是HoTT矛盾证明。

脚本为 `HUMAN_EDITED`；生成JSON与原输出为 `DERIVED_VERIFICATION_RECEIPT`。本目录不是新的canonical数学账本。所有实物保留实际失败，重复捕获不得覆盖原目录。

| 入口 | 用途 |
|---|---|
| [SUMMARY.json](SUMMARY.json) / [REPLAYS.json](REPLAYS.json) | 三新命令一致：一个接受、两个预期拒绝 |
| [VERIFIER-RESULTS.json](VERIFIER-RESULTS.json) | 当前十个收据5 PASS、5 FAIL的具体原因 |
| [NEGATIVE-RUN-INTEGRITY.json](NEGATIVE-RUN-INTEGRITY.json) | 两个负向run的artifact/source/external pins核验范围 |
| [OPTION-CONTROLS.json](OPTION-CONTROLS.json) | 五个已修控制与一个字符串误接受，另有强制safe对照 |
| [synthetic-option-controls/](synthetic-option-controls/) | 独占合成源及测试RUN/index，不属于项目主张矩阵 |
| [checks/](checks/) | 各次argv、cwd、exit、stdout/stderr与hash |
| [INPUT-BEFORE.json](INPUT-BEFORE.json) / [INPUT-AFTER.json](INPUT-AFTER.json) | 受审文件身份与运行期间无漂移记录 |
| [CONTEXT-SOURCES.json](CONTEXT-SOURCES.json) / [EXTERNAL-SOURCES.md](EXTERNAL-SOURCES.md) | 首审、数学危机工程、原典与术语来源 |
| [COGNITION-REATTESTATION.json](COGNITION-REATTESTATION.json) | 四件套25文件收据复认；不认证模型理解 |
| [audit_current.py](audit_current.py) / [option_controls.py](option_controls.py) / [capture_context.py](capture_context.py) | 此次证据的实际产生脚本 |

受审源码未修改；工具链沿原run指定位置执行，可能产生正常接口缓存。没有独立环境部署、网络目标测试、正式数学claim注册或canonical状态更新。
