# scripts：研究代码与操作工具

本目录收回当前附件中可取得的脚本/形式化源码，并保存本轮全部可复现操作代码。原路径未删除、原字节未改；回收副本默认仅归档，不自动执行。

## 可运行的本轮工具

- `tools/restore_checkpoint.py`：从明确检查点安全恢复新目录。
- `tools/recover_code.py`：扫描附件/嵌套包，按内容哈希去重，保留每个来源路径。
- `session/run_logged.py`：保存实际命令、输出、返回码与时间。
- `session/establish_git.sh`：只创建新的本地Git基线，不设置remote/push。

## 已恢复的直接历史实验

| 原Session路径 | scripts回收路径 | SHA-256 |
|---|---|---|
| `.codex/research/hott/sessions/S-ANS-20260910-007-CAUSAL-EQUIVALENCES/FINITE_CHECKS.py` | `scripts/recovered/4c4f5da5b30bf5df9a00/FINITE_CHECKS.py` | `4c4f5da5b30bf5df9a0036f3683a1a12a5cd4038cbb73e860a10e463007b598c` |
| `.codex/research/hott/sessions/S-ANS-20260910-008-RELATIONAL-SIP/FINITE_CHECKS.py` | `scripts/recovered/eef4c0466d30012b2cee/FINITE_CHECKS.py` | `eef4c0466d30012b2ceed594a3e8f7971f424449d1c092e4288f9258ccf09d7d` |
| `.codex/research/hott/sessions/S-ANS-20260910-010-LABEL-STREAM/FINITE_CHECKS.py` | `scripts/recovered/0c7e076a9749fd347a01/FINITE_CHECKS.py` | `0c7e076a9749fd347a013aee7f963d0425b43f5dfdacf05b063b4530d35a9e00` |
| `.codex/research/hott/sessions/S-ANS-20260910-011-COMPLETION-CERTIFICATE/FINITE_CHECKS.py` | `scripts/recovered/09366972dd1aac586555/FINITE_CHECKS.py` | `09366972dd1aac58655501ccb2e498c6b70afcdb5939b64b8610589c458748a9` |
| `.codex/research/hott/sessions/S-ANS-20260910-014-DONE-OBSERVABILITY/FINITE_CHECKS.py` | `scripts/recovered/10a55b3d59d5d96c6f0d/FINITE_CHECKS.py` | `10a55b3d59d5d96c6f0d9739dc88c06f29272fc13e90b4d535690d3b1c38f113` |
| `.codex/research/hott/sessions/S-ANS-20260910-015-QUOTIENT-DESCENT/FINITE_CHECKS.py` | `scripts/recovered/ecbdcd2f4c4d9e34c02b/FINITE_CHECKS.py` | `ecbdcd2f4c4d9e34c02b0f2880ed11a145a2add3ac743a3082e8bd8d132ac6a6` |

## 回收边界

扫描 14 个顶层ZIP、10 个嵌套ZIP及挂载源码，登记 300 次源码出现，保存 68 份不同内容/语言扩展的副本。逐项路径、来源、哈希见 `RECOVERY_MANIFEST.json`。

没有从聊天摘要伪造缺失脚本。原始R001代码仍不能确认完整恢复；代码片段/伪代码保留在原Markdown/会话里，不自动改装成已运行脚本。此前临时命令若未作为文件或日志进入附件，不能声称已找回。

历史所有恢复代码未经逐份语义/安全审查，不要批量运行。具体复现前先读源码、确认依赖与写入目标。

## R016：本轮新执行源码与复现

| 路径 | 作用 |
|---|---|
| `research/r016_axiomatic_transport.py` | 有类型的Bool/函数/opaque-ua片段；区分VALUE、NORMAL_NONCANONICAL、ILL_TYPED、FUEL_EXHAUSTED；并非HoTT kernel |
| `tests/test_r016_axiomatic_transport.py` | 36项单元测试，包含捕获规避替换和正反对照 |
| `session/replay_r015.py` | 只复放已审阅的R015纯脚本，拒绝源码SHA变化，逐字段比较历史结果 |
| `session/read_required_pages.py` / `read_source.py` | 按文件范围发出正文并留记录；不证明模型保留或理解 |
| `session/prepare_r016_evidence.py` | 保存真实来源区间、输入身份、结果和加载边界 |
| `session/finish_checkpoint.py` | 通过既有runtime API更新revision15→16，含dry run与STALE_BASE实测 |
| `tools/audit_workspace.py` | 回收源码hash、新Python语法、指定敏感标记和原文件保护检查；不执行回收码 |
| `tools/package_workspace.py` | 干净Git＋fsck＋bundle＋带.git的ZIP，实际解压与clone复核，不访问remote |

实际命令输出见`artifacts/execution/`，新实验结果见`artifacts/r016/`，推导与裁决见最新Session。Git保留每次执行时的源版本；源码改变后旧receipt不可当新运行。

无需依赖安装：`python3 -B scripts/tests/test_r016_axiomatic_transport.py`。
实验新输出示例：`python3 -B scripts/research/r016_axiomatic_transport.py --out /tmp/hott-r016-new.json`。
所有输出选择新路径；不要通过覆盖历史结果消除失败证据。回收工具最初的目录全扫描不应不加审查地对已经生成新交付包的同一input-dir反复执行；首次作用域和字节映射以现有清单/Git版本为准。
