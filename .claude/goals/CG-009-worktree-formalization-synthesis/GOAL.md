# CG-009：跨 worktree 形式化资产审查与当前未来形势研判

<!-- goal-x:essentials-begin -->
## 1. 父目标

研究发起人 2026-10-11：首先记录本会话的分析与审计结果；查看三个正在运行的 AI worktree 及其他曾工作过的 worktree 有无新增方向、资产值得吸收；最后写一份综合的形式化与机器证明当前与未来工作形势研判。

用户点名：WorkBuddy dev-ef7e5239、dev-f65ca154；Codex 9276-w9b-residue-snapshot-20261011。工作tree的活跃是用户提供的信息，不以git dirty或没有可发现的session来推断进程活跃与否。

## 2. 完成门

1. 先前Z0-D3审计分析、运行方法、失败和范围在本worktree报告中存档，另有共享索引/追踪可集成登记。
2. 所有 git worktree 登记项获得HEAD、branch、dirty、与dev差异的初筛清单；无法访问或不适用项明说，不静默截断。
3. 三个活跃工位及其他有增量的工位按相关源码、日志、方案原文深读；识别资产而非照抄完成声称。
4. 值得吸收的候选列出来源工位、路径/源身份、已有与新增部分、是否过核、解决哪个缺口、集成依赖与边界；重点可用源码在私有副本复核，不能复核的如实降格。
5. 综合报告落盘：当前真实版图、路线比较、下一单元建议、完成门、未决项、资产清单与覆盖边界；交付用户。

## 3. 角色与权限

只读审查、资产比较、数学路线研判。禁止改其他AI文件、启动代理、提交推送、发布、删除、改Foundation缓存。所有命令cwd保持本worktree，不cd原检出。仅报告、目标包、私有核验副本/日志写本worktree。共享记录先给可集成草稿，不覆盖活跃canonical文件。goal编号避让canonical CG001..007及WorkBuddy自称CG008，使用本会话CG009。

## 4. 恢复闭包

```goal-x-closure
/Volumes/D/HoTT_AI_HANDOFF_20260911/CLAUDE.md | 实用主义与证据边界、形式化追踪SOP
/Volumes/D/HoTT_AI_HANDOFF_20260911/形式化追踪/README.md | 已有版图，不将覆盖当完成
/Volumes/D/HoTT_AI_HANDOFF_20260911/形式化追踪/05-分支上的形式包/README.md | 历史八方向已吸收分母
/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/docs/Z0-D3审查-工作记录.md | 本会话已完成审计全文及局部D3建议
docs/形式化综合研判-20261011/审查工作台.md | 当前已读资产、未知、下一步
docs/形式化综合研判-20261011/worktree-inventory.json | 所有工位初筛快照与采集时间
```

恢复：bind后Read本文件、STATE、LOG、闭包；重新git worktree list与canonical log；若HEAD/关键文件变化，重读受影响原件，不用哈希代替阅读。工位进展本次快照为准，后续变化不追认成先前已核事实。

## 5. 阶段

A 审计存档与工位初筛 → B 活跃/有新增工位深读 → C 有价值资产独立复核 → D 当前未来综合研判与可集成登记 → E 完成门核对交付。

每个自然单元后goalx checkpoint；数学诊断、未证路线、实际kernel结果分别标注。失败探针不证明目标不可证；没有文件变化不证明工位没在工作。
<!-- goal-x:essentials-end -->
