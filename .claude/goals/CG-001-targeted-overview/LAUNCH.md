你是我新开的 Claude Code 会话，在 /Volumes/D/HoTT_AI_HANDOFF_20260911 执行 Claude goal CG-001：有靶统观，从理论便利与现实过程出发寻找 HoTT 现实相对悖论。角色 RESEARCH_GENERATION，操作指令是《最高指示-Claude版》，目标、完成门与权限以 .claude/goals/CG-001-targeted-overview/GOAL.md 为准。

开工和每次压缩或恢复之后：先调用 goal-x Skill（resume CG-001），用 Read 重读回执列出的闭包文件（最高指示-Claude版、核心认知全文、扩展认知 003/008/009、本目标的 GOAL.md 和工作台），在对话里写出恢复说明，再从 STATE 的“下一步”继续。首次开工另按 GOAL.md §3 读完四件套其余分片和已走过的路。

做法：不做全书式覆盖。
1. 先画 HoTT 便利地图：整体层和机制层先行，添入与省去两面都看；每项写收益、被改条件、给外行的人话解释，以及从哪一句开始贴不上。
2. 再以现实中的完成方式为主通道生成种子句：理论为了 E 把 T 改成 T′，做 P，预计 O 会变。
3. 挑排名靠前、机制不同的种子追到判词。
先发现后核证；模型里没有靶前提就先补桥，不扩大枚举；落在已关闭机制上的种子，写明差量或判为重复。数学结论过 F-011，否则降格。

权限：我授权你写 .claude/goals/CG-001-targeted-overview/、HoTT/formal/claude-cg001/，以及 HoTT/verification/runs/ 下名字含 -CG001- 的新 run，并对这些自有路径做精确本地 Git 提交（git commit -m … -- <路径>，提交前核 index）。研究 STATE、MEMORY、方向追踪、全景视野、核心认知、CLAIM_EVIDENCE_MATRIX 和各 Session 目录由 Codex Session C 维护，你只读；需要登记的写进本目标的 relay.md。不 push、不 tag、不发布，不改他人未提交的文件，不调用 Agent 工具。

每个自然单元结束运行 python3 ~/.claude/skills/goal-x/goalx.py checkpoint CG-001 --phase … --next … --note …。

完成条件（二选一）：
- 对话中出现 CG-001 的完成门审计表，G-ALIGN、G-MAP、G-SEEDS、G-PURSUE、G-OMISSION、G-REPORT 六门都给出证据位置并判 PASS，随后出现 “goal-x close CG-001 status=COMPLETE” 的输出。
- 或者出现阻塞报告，并已执行 close --status BLOCKED 或 --status PAUSED。

是否命中（QUALIFIED_HIT / NO_QUALIFIED_HIT_WITHIN_SCOPE）单独报告，不影响完成判定。预算或上下文用尽不算完成。
