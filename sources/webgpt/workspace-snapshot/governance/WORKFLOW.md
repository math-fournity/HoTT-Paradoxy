# 平台无关的日常工作与恢复

所有命令以 `workspace/` 为工作根；也可从任意目录调用脚本绝对路径并提供 `--root`。只需 Python 3.10+ 与 Git；不需外部 Python 包。无执行能力时可以读文件并形成交接文字，但必须标记命令 NOT_RUN，不能声称 checkpoint 成功。

## 1. 接手验收

运行包外层 README 中的完整包验证命令；核查 `git rev-parse HEAD` 与 `git status --short`，应匹配 `handoff-r040`。不要在旧宿主路径上运行。把 `governance/ENTRYPOINT.md` 显式纳入你的平台启动输入。

```bash
python3 -B scripts/handoff/govern.py plan --output exchange/outbox/start-plan.json
```

输出文件只保存清单，不代表内容已经读完。按其中 `documents` 的顺序逐份全文读取；长文件以返回的行范围接续。也可用已核对内容未过期的 onboarding 卷一次性注入，但必须检查当前快照与卷清单一致。例：

```bash
python3 -B scripts/handoff/govern.py read --snapshot <plan里的snapshot> --path <计划内相对路径> --start-line 1 --max-bytes 20000
python3 -B scripts/handoff/govern.py check --snapshot <同一snapshot>
```

根据 `total_lines` 与 `next_start_line`（以实际输出字段为准）完整继续。不能只读头部；最后由接手 AI 明确报告实际载入、缺件、冲突与理解，工具不代签。

## 2. 有界研究

以 STATE 中的最新前沿为依据，但允许独立选择更有价值、机制不同的方向。不要重做 R039 的同类自环测试冒充推进。保存问题版本、理论环境、公理、输入数据、实际代码与结果；论文来源和实例桥梁分别核查。不要批量运行 Archive 或另一 AI 写的任意代码。

建议同时建立本次 `exchange/rounds/<唯一ID>/`，即便用户尚未要求发送。它记录增量研究与审计接口，不替代正式研究记录。

## 3. 原治理 checkpoint（沿用完整引擎）

先保存研究正文、源码与实际证据，再重新读取当前计划作为**本次写回基线**。本轮新的 `sessions/<ID>/SESSION.md` 正文放在 checkpoint payload 中，由原子写入一次创建；不要先在目标路径创建同名 SESSION，再要求 checkpoint 覆盖它。其他不可覆盖来源/研究文件可先保存。如实构造 payload JSON（它是数据，不是 inline 可执行代码），格式完整模板在 `.codex/skills/hott-paradox-research/templates/session-checkpoint.md`。

写集合必须包含五份当前文档 MEMORY、FRONTIER、LESSONS、RESUME、STATE 与本次新 SESSION。STATE revision 递增1，latest_session 指向新的 Session，旧 records 的身份/未决项不丢失。改依赖必须说明真实重验证；不能为消除警告只换哈希。

```bash
python3 -B scripts/handoff/govern.py checkpoint --snapshot <当次基线> --payload <payload.json>
python3 -B scripts/handoff/govern.py checkpoint --snapshot <同一基线> --payload <payload.json> --apply
python3 -B scripts/handoff/govern.py plan --output exchange/outbox/after-plan.json
```

先 dry-run 再 apply；真正失败保留日志。回读新 Session、STATE/HEAD/MEMORY，并确认下次 plan 包含新证据。最后在用户已有授权下本地提交；Git不是数学证书。

## 4. 冲突与中断

旧基线、未完成事务、写锁必须停止相应写入，不擅自覆盖。只有确认原写者停止后，才可显式选择：

```bash
python3 -B scripts/handoff/govern.py recover --action finish --confirm-owner-stopped
```

或 `--action rollback`。该选择是操作者的真实责任，不可由一个超时自动代替。

新主机恢复的是文件而非原进程：不恢复后台作业，不借旧权限安装工具，不假设上次声称的编译器现在可用。旧历史绝对路径只是出处，当前脚本通过 `--root` 重新绑定。
