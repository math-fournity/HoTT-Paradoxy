（本包现为 DRAFT。只有在研究发起人选定靶并说开工之后，才把下面两段粘贴给原生 /goal；《菲尔兹目标研究指导》002 片 D3 建议由研究发起人逐轮驱动，这时可以不用 /goal。）

在本仓库执行 Claude goal CG-004（菲尔兹第一靶：在研究发起人选定的菲尔兹奖工作里，做出一条有机器骨架的 UR 短链）。开工和每次压缩或恢复后：先调用 goal-x Skill（resume CG-004），按 `.claude/goals/CG-004-fields-first-target/GOAL.md` 用 Read 重读闭包文件（含《菲尔兹目标研究指导》索引与 6 个分片），写出恢复说明，再从 STATE 的“下一步”继续。研究发起人的选靶、UR 判定与归因讨论都要原话入工作台；没有选靶原话不得进入 P1。每完成一个自然单元运行 `python3 ~/.claude/skills/goal-x/goalx.py checkpoint CG-004 --next "…"`。只按 GOAL.md 的完成门判断完成，局部任务完成不算；不提交、不下载、不写共享 owner，除非研究发起人授权。

完成条件：对话中出现 CG-004 的完成门审计表（G0 至 G7），每一门都有证据位置且判 PASS，随后出现 `goal-x close CG-004 status=COMPLETE` 的输出；或者出现阻塞报告并已执行 `close --status BLOCKED` 或 `--status PAUSED`。
