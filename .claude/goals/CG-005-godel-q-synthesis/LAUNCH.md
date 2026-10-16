# CG-005 启动说明

状态：2026-10-07 本机会话 d58e0c0d 一轮做完（P0–P8），完成门 1–7 的证据见 `GOAL.md` §1 与会话中的完成门审计表。本包不需要原生 `/goal` 续跑。

若要在新会话里恢复或复核：

```text
/goal-x resume CG-005
```

恢复后按 `GOAL.md` §3 的闭包重读原文，再读 `综合报告.md`、`审计报告.md`、`设计.md` 与 `HoTT/formal/claude-cg001/godel-q/CLAIM.md`。

独立复核（交给没有共享历史的审计者）可粘贴：

```text
请独立复核 Claude 线目标包 CG-005（.claude/goals/CG-005-godel-q-synthesis/）。先只读 GOAL.md 与 原话摘录.md，自己复述研究发起人的原问与验收标准；再读 HoTT/formal/claude-cg001/godel-q/CLAIM.md，逐条核对 GodelQ/Qualification.lean 中 qual_C84 至 qual_C94 的类型是否与 CLAIM 一致；用 .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --rerun 重放 HoTT/verification/runs/20261007-CG001-GODEL-Q-01（负控制加 --expect-rejected）；最后判断：形式命题是否忠实于研究发起人的论证，ZFC 实例化所依赖的标准元定理是否写全，禁止外推是否守住。不要修改任何执行者产物；执行完成、业务命中、审计结论分开报告。
```

仍需研究发起人决定的事：见 `综合报告.md` §9 与总索引 002 §2 第 26 条。
