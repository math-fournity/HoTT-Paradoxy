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


## R017：所有代码先保存，再执行；局部证书与全域总性

根AGENTS已明确禁止inline代码，包括临时诊断、数据和文档操作；先保存到scripts再按路径调用。仅用于写文件的heredoc不是执行，解释器stdin/c/e和临时shell算法不再使用。

| 路径 | 本轮实际用途 |
|---|---|
| `tools/restore_rev16.py` | 安全恢复带.git的rev16 ZIP到新可写目录，继承原4个commit |
| `session/register_scripts_only_policy.py` | 原位修订AGENTS并保存改前字节、diff和完整指令 |
| `session/r017_cognition.py` | 解析真实加载集合、连续发出正文、记录缺块；不伪造认识通过 |
| `research/r017_local_execution.py` | 有限寄存器语法、有界模拟、当前执行证书及显式自环；不是全域停机判定器 |
| `tests/test_r017_local_execution.py` | 42项实际测试，含错误证书、fuel边界与源先行政策 |
| `session/prepare_r017_record.py` | 保存初稿、直接规则摘录、来源hash和有限结果 |
| `session/finalize_r017_record.py` | 保存初稿后真实压缩这一事实，更新交付索引，不改强制加载政策 |
| `session/finish_r017_checkpoint.py` | 使用既有事务API保存revision17，核新加载集合与旧快照拒绝 |
| `tools/audit_r017.py` | 对比继承Git基线、校验脚本和结果、检查新代码仅在scripts |
| `tools/package_workspace.py` | 复用已保存的打包工具，输出.git ZIP与bundle并实际恢复验证 |

实际运行记录在`artifacts/r017/execution/`；当前推导见R017 Session；初稿及后续修订版本在Git中，不删除失败/变更历史。

```bash
python3 -B scripts/tests/test_r017_local_execution.py
python3 -B scripts/research/r017_local_execution.py --output /tmp/hott-r017-new-result.json
```

输出使用新路径，拒绝覆盖原实验。实际9216次包装运行仅为声明有限模型；全域批准器不可能性是另写的带有效通用性/语义可靠性前提的纸笔证明，未运行HoTT内核。


## R018 · 外部HoTT.json核验

- session/r018_prepare_audit.py：恢复rev17、原JSON保全和公开文本/代码精确提取。
- recovered/HoTT_json/：外部AI的原Python与两段Lean，带原始hash，不伪称可编译。
- research/r018_test_transcript_simulator.py：复现原Python及10个边界诊断测试。
- research/r018_lean_eq_audit.lean：普通Lean proof-irrelevance反证候选，NOT_COMPILED。
- tools/r018_get_lean.py、r018_get_lean_zip.py：失败工具链获取尝试，真实错误保留。
- session/r018_finish_audit.py：有界审计回写，原owner不变。
- tools/r018_package_audit.py：Git与完整交付包验证。

实际结果见artifacts/r018，不把代码存在或Python PASS称为HoTT机器证明。


## R019 · HoTT-2完整增量审计

- session/r019_prepare.py：恢复rev18真实Git包，保全原JSON，去parts重复，提取公开文字/代码/原结果。
- tests/r019_simulator_audit.py：原样运行三版模拟器及32项诊断；结果artifacts/r019。
- session/r019_metadata_audit.py：全源码AST/内嵌脚本/治理故障探针；不对当前目录执行源治理。
- session/r019_decode_attachments.py：解码两份真实Python附件并比较字节，不执行附带更新器。
- session/r019_finish_audit.py：文档、原规则摘录、分项裁决和受控checkpoint。
- tools/r019_package_audit.py：原字节保护、本地Git提交和包/bundle恢复验证。
- recovered/HoTT2_json/：全部原始代码、内嵌脚本和附件。**不要批量执行；其中治理脚本会写绝对路径，原Lean文本未完成。**

Python诊断PASS是核查实现缺陷，不是HoTT证明PASS。原输入是599415字节、73chunk新问答；原始签名/草稿仅保全，不作结论证据。


## R020 · Gemini意见与首封论辩

- session/r020_restore.py：安全恢复revision19 Git包，不伪造rev24。
- session/r020_prepare.py：原文及五个角色块逐字切片、固定来源回查。
- session/r020_finish.py：首次记录准备与15项文件检查；dry-run未通过，错误保留。
- session/r020_resume_checkpoint.py：保全未提交稿并换用新Session身份；依赖门禁拒绝，错误保留。
- session/r020_commit_final.py：明确待复核依赖状态后完成事务，原记录与治理器不改。
- tools/r020_package.py：本地Git与完整/转发ZIP、bundle读回恢复检查。

没有新的数学实验或原生内核证明。所有新增代码先保存再调用；首封信未发送，没有模拟对方回复。


## R021 · Gemini两轮综合与研究计划保全

新增脚本在 `scripts/session/r021_*.py` 与 `scripts/tools/r021_*.py`，均先落盘再调用。
`restore`恢复真实rev20仓库；`prepare`原文切片/来源指纹；`sources`记录远端快照尝试（DNS失败如实保留）；`integrate`维护来源裁决与当前目标；`checkpoint`经既有manager同步状态；`verify`只查文件/路由/边界；`package`实际提交、Git/ZIP/bundle恢复验证。
本轮没有运行HoTT数学模拟器或证明助手。机械检查不是数学定理证明。旧回收源码和历史脚本不被改写。

## R022 · 第二封论辩回信与交接

新增工具均先落盘再调用：`scripts/session/r022_restore.py` 安全恢复原包；`r022_prepare.py` 整理真实文稿与台账；`r022_checkpoint.py` 经原治理器交接；`scripts/tools/r022_verify_package.py` 校验、Git提交与打包。它们不调用Gemini，不运行数学模拟器，不把文件检查当内核证明。

R022补充工具：`scripts/session/r022_checkpoint_retry.py` 修正被拒载荷的kind与待复核状态，保留失败日志；`r022_plan_check.py` 在新进程只读验证当前路由。

R022交付修复：`scripts/tools/r022_finish_delivery.py` 保留首次快照比较失败，先完成文档修改再冻结并核对源目录／异目录状态；不改数学或治理引擎。
