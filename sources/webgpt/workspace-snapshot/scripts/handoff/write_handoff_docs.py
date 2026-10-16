#!/usr/bin/env python3
"""Write the explicitly requested cross-AI handoff contract; preserve legacy mathematical sources."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2];PKG=ROOT.parent
REQUEST='''我现在需要你把你的工作交接给另外一个AI，你需要把我们项目在你这里的所有东西，都打包。

你首先要想清楚我们这个项目在你那里都发生过哪些位置的数据存放？

我个人看到的目录包括：

```
`.codex`
/mnt/data

```

是否只有这些目录中有我们项目的数据呢？

如果要打包给另外一个AI，你不仅仅要把它们放入zip文件中，你必须写一份README.md文件，其中非常重要的是，你同时要解释和打包治理框架的完整版本。

因为那个AI接手之后，必须也要按照你的治理框架来构建一样的治理框架，才能够继续。

你甚至还要设计一套方案，让它未来的工作，能够每次都在我的指示下很方便地就能够以ZIP包的形式发送给你做审计，注意，只是每次的增量内容。

所以增量的内容，或许除了在治理框架的规定下需要存放在一定的位置，还需要为这种传递、交流，每次单独建立一个增量研究记录、交流用的目录。

请你为它设计好，放入它的治理框架中，默认增量的交流总目录就在它的工作目录中，是一个子目录。

另外，你不能假设它和你一样，都会使用`.codex`目录作为自己的项目内的治理框架所在的目录。

另外，另外一个AI，它具备100万上下文，远远超过你当前的上下文容量，所以你可以考虑如何让它一次性掌握全部信息，不怕加载的内容多，但是内容必须进行充分的说明，而且加载顺序要有条有理。

最终，全部整理好之后，放到一个单独的目录中，然后打包成zip，给我，其中包含那个关键的README.md。'''.replace('\x08','')

def write(p,text):
 p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise FileExistsError(p)
 p.write_text(text.rstrip()+'\n',encoding='utf-8')
def js(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2))

def main():
 write(ROOT/'governance/ENTRYPOINT.md','''# HoTT 跨 AI 治理入口 · portable handoff v1.0

本目录是平台中立的入口。接手者可以是任何 AI：不要求 Codex、插件、特殊消息接口或模型名称。把这些 Markdown 当作普通工作指令文档，按当前用户授权执行。`scripts/handoff/govern.py` 显式定位项目，不依赖 shell 当前目录，也不要求宿主自动识别 `.codex`。

## 唯一权威与完整版本

这不是一套缩水治理。完整原规则、两类 Skills、模板、运行器、测试、状态与旧事务全部在项目 `.codex/`，当前唯一位置见 `PATHS.json`；原 R039 完整版本还在包外层 `archive/originals/mnt_data/HoTT_silent_steps_rev39_with_git.zip`。为保留历史依赖和单一事务引擎，兼容存储路径没有改名。`.codex` 此时只是普通的数据目录，**不是要求另一 AI 采用的厂商治理入口**。

portable v1.0 只增加平台中立入口、完整加载导览与增量交换；不另建主张矩阵，不复制可变 STATE，不绕过原 checkpoint。原协议 1.3.0、原引擎 1.3.0、业务 Skill 1.3.4 的完整正文均须读。不要用本页摘要替代。

若宿主惯用 `.gemini`、`.claude` 或其他目录，可运行 `install-entry --directory <相对子目录>` 写一个指针入口。它不会覆盖原文件，不会复制状态；宿主是否自动加载，需要在该宿主实际确认。也可直接把本文件和根 AGENTS.md 加入新 AI 的项目启动指令。

## 每次开始／压缩后

先确认根、权限和 Git HEAD；完整读 AGENTS、两类 Skill、PROTOCOL 和 LOAD_SET。用 `govern.py plan` 解析当前固定及动态集合。依原计划先完整读第五闭包，再完整读三问；之后是用户原文、Schema、当前记忆、每个活动／待复核记录及其递归依赖。百万上下文的一次性导览在包外层 onboarding/，不是替代原政策。

每次新会话、再次执行研究 Skill 或压缩恢复，重新按当前字节加载。不能使用“上次读过”“哈希没变”“zip验证通过”作为免读理由。工具输出必须真实进入当前模型；有截断或容量不足就保留未加载范围，不伪造认知验收。治理也不要求在一次正常调用的每个内部步骤重新入门，避免治理互相递归。

## 工作与证据

共同目标、原话与证据纪律保持；思路与结论允许独立改进。区分 HoTT 已有能力、计算共同界限、特定理论化新增失真；双向现实相对目标不变。原生形式证明、纸笔论证、有限测试、第三方评语、未执行草稿分别记录。不要把旧失败重新包装成发现。最后的实际数学轮次为 R039，R040 仅交接工程。

新代码一律先保存 `scripts/`，再通过文件路径运行；失败和原始日志保存。不能直接运行历史脚本，它们可能固定旧路径；优先检查源码并写相对路径包装器。

## 每次结束

在授权范围内保存不可覆盖 Session、实际研究正文与所有输出。通过唯一旧引擎进行基线比较、dry-run、checkpoint、回读；同步 MEMORY/FRONTIER/LESSONS/RESUME/STATE。然后本地 Git 提交，记录真实 HEAD。见 `WORKFLOW.md`。

当用户要求交给 Astra 审计时，按 `EXCHANGE_PROTOCOL.md` 从明确基线导出增量。导出、收到审计、接受审计修改，是三个不同事件。审计不自动批准合并；不得伪造对方回复。禁止自动发送、push、模型切换或后台研究承诺。
''')
 js(ROOT/'governance/PATHS.json',{'schema_version':'hott.portable-paths.v1','project_id':'ALL-Markdown/HoTT','portable_version':'1.0.0','governance_protocol_version':'1.3.0','runtime_version':'1.3.0','business_skill_version':'1.3.4','entry':'governance/ENTRYPOINT.md','agent_policy':'AGENTS.md','runtime':'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py','governance_skill':'.codex/skills/hott-session-governance/SKILL.md','business_skill':'.codex/skills/hott-paradox-research/SKILL.md','load_set':'.codex/cognition/LOAD_SET.json','state':'.codex/research/hott/STATE.json','head':'.codex/cognition/HEAD.json','protocol':'.codex/cognition/PROTOCOL.md','memory':'MEMORY.md','frontier':'.codex/research/hott/FRONTIER.md','lessons':'.codex/research/hott/LESSONS.md','resume':'.codex/research/hott/RESUME.md','exchange_root':'exchange','scripts_root':'scripts','legacy_storage_is_ordinary_directory':True,'single_runtime':True})
 write(ROOT/'governance/WORKFLOW.md','''# 平台无关的日常工作与恢复

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

先保存不可覆盖 Session 及研究文件，再重新读取当前计划作为**本次写回基线**。如实构造 payload JSON（它是数据，不是 inline 可执行代码），格式完整模板在 `.codex/skills/hott-paradox-research/templates/session-checkpoint.md`。

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
''')
 write(ROOT/'governance/EXCHANGE_PROTOCOL.md','''# 增量研究与审计交换协议 · v1.0

## 目标、目录和单一权威

默认交流总目录是项目根下 **exchange/**，与任何厂商目录无关。每次单独目录：`exchange/rounds/<round_id>/`。正式数学正文仍保存在已有研究记录路径，程序在 scripts/，运行数据在 artifacts/。交流记录指向这些证据，不创建第二套结论真值。

- `rounds/`：用户原请求、增量研究记录、精确依赖、实际执行账本、审计问题；必须 Git 跟踪。
- `outbox/`：用户要求时导出的 ZIP 和导出收据；不入 Git，避免 ZIP 包含自己。
- `inbox/`：实际收到的原始审计包；不自动执行、不自动应用。重要审计原文经审查复制到 `audits/` 后入 Git。
- `audits/<audit_id>/`：实际审计原文、结果、目标包 SHA、base/head、逐条接受/拒绝理由和后续证据。未收到不得创建假回信。
- `templates/`：模板，不是执行成果。

## 每轮最小记录

`REQUEST.md` 保存原请求；`RESEARCH_DELTA.md` 说明旧状态、本轮实际动作、正反结果、数学/实现/现实桥梁分别到哪一步、失败与受影响结论；`AUDIT_REQUEST.md` 指定待审问题；`RUNS.json` 记录实际 argv/cwd/工具版本/源码输入哈希/stdout/stderr/退出码，未运行写 NOT_RUN；`ROUND.json` 绑定唯一 round_id 与 base_commit。

初始化：

```bash
python3 -B scripts/handoff/delta_tool.py round-init --id R041-EXAMPLE --request-file <用户原请求文件> --base handoff-r040
```

这里只创建模板，不启动研究、不自动生成证明。填写实际内容，完成原治理 checkpoint 和本地 Git commit 后，用户说“把本轮增量交给 Astra 审计”时执行：

```bash
python3 -B scripts/handoff/delta_tool.py export --round R041-EXAMPLE
```

生成 `exchange/outbox/R041-EXAMPLE.zip` 和 `.receipt.json`，将 ZIP 交给用户，**不通过任何账号自动发送**。

## 基线：不能把“已发送”当成“已确认”

首次基线是不可移动的标签 `handoff-r040`，实际 commit 在完整交接包的 manifests/HANDOFF_IDENTITY.json 中。后续优先使用双方真实确认的准确 commit SHA；接收方未保存中间增量时，继续从共同已知基线导出累计净增量。`--base` 可以显式指定已确认基线，但必须与 ROUND.json 一致，不得在导出时悄悄改掉。

一次增量必须满足 base 是 head 的祖先。发送成功、文件验收成功、数学审计认可和修改合并不同。审计员意见不是用户授权；不得为了通过审计重写旧日志、旧原话或事后伪造实验。

## ZIP 的精确定义

本协议只导出已提交、干净工作树的差量。未提交、新建未跟踪的研究资料会使导出失败。原工具忽略的缓存/虚拟环境不是研究证据，不能往那里藏运行成果。

ZIP 包含：

1. `MANIFEST.json`：协议、轮次、base/head commit和tree、每一包成员的 SHA-256/长度、审计状态 NOT_AUDITED。
2. `BASE_SNAPSHOT.json` 与 `HEAD_SNAPSHOT.json`：全量路径/模式/哈希目录，不携带全部旧内容。
3. `CHANGES.json`：新增/修改/删除及前后哈希；重命名按删除＋新增，避免含糊检测。
4. `payload/`：仅新增和修改后的文件字节；删除只有清单，不伪造空文件。
5. `changes.patch`：可读的完整差分（含二进制差分）；不是自动执行脚本。
6. `commits.bundle`：仅 base 之后的 Git 对象和历史，恢复时需要准确基线。
7. README：审计范围和安全入口。

同时携带 patch、payload和薄bundle用于交叉核对，不意味着包含全量旧项目。文件哈希不是签名，不能认证作者或数学真理。当前v1支持 Git SHA-1仓库、普通/可执行文件，拒绝symlink、submodule、跨平台大小写冲突、不安全路径、重复ZIP成员；这些情况需要显式迁移而非静默丢弃。单次解压总量上限512MiB，超过时拆分真实工作批次或明确建立新全量基线，不能任意删证据。

## Astra／其它审计员接收

必须用**已信任基线中的工具**验证新包，不先执行新包里的脚本：

```bash
python3 -B scripts/handoff/delta_tool.py verify /path/to/R041-EXAMPLE.zip --with-base
python3 -B scripts/handoff/delta_tool.py stage /path/to/R041-EXAMPLE.zip --destination /path/to/new_isolated_audit_workspace
```

`stage` 要求调用方根的 HEAD 精确等于 base；若当前工作已前进，先另建该 base 的独立检出。它只克隆到不存在的新目录，再验证bundle、完整前后清单与检出字节，**不覆盖活动研究目录**，不自动运行研究代码、钩子、测试或合并。

验收不等于审计。审计应先读当次原请求与差量，再沿依赖回到共享基线，分别判断数学主张、模型对应、程序行为和治理变化。若依赖的旧全量包缺失，报告 NEED_BASELINE，不猜补。

## 审计后采用

只存真实回信，记录其针对的 ZIP SHA、head commit、结论与限制。逐项接受或拒绝并给理由；需要改动时新建 Session/commit，保留失败版本。下一基线只有在用户和审计双方确实保存了同一版本时才更新；导出工具不自动推进基线。跨机器没有分布式锁，分支分歧不能靠“最后写者”覆盖。
''')
 write(ROOT/'exchange/README.md','''# HoTT 增量交流目录

完整合同：`../governance/EXCHANGE_PROTOCOL.md`。这里是默认交流总目录，与 .codex、Gemini 或 Claude 的平台无关。`rounds/` 和 `audits/` 是需版本管理的证据；`outbox/` 和 `inbox/` 是传输文件，不自动运行、不自动合并。

用户可以只说：“按增量交接协议，把自上次共同确认基线以来的工作打包给 Astra 审计。”AI负责先检查并填写本轮记录，再checkpoint、commit、export和提供ZIP链接。

初始共同基线：`handoff-r040`。最后实际数学轮次：R039。交接本身不改变任何数学证据等级。
''')
 js(ROOT/'exchange/BASELINE.json',{'schema_version':'hott.exchange-baseline.v1','baseline_ref':'handoff-r040','baseline_identity_file':'../manifests/HANDOFF_IDENTITY.json (relative to package root, not workspace)','last_mathematical_round':'R039','audit_status':'HANDOFF_BASELINE_NOT_EXTERNAL_MATH_AUDIT','update_rule':'Only explicit acknowledged common base; never advance on mere export'})
 for sub in ['outbox','inbox','audits','rounds','templates']:(ROOT/'exchange'/sub).mkdir(parents=True,exist_ok=True)
 write(ROOT/'exchange/templates/AUDIT_RESULT.template.json',json.dumps({'schema_version':'hott.audit-result.v1','audit_id':'REPLACE','round_id':'REPLACE','package_sha256':'REPLACE','base_commit':'REPLACE','head_commit':'REPLACE','received_at_utc':'REPLACE','reviewer_actual_identity':'REPLACE','status':'NOT_REVIEWED','claims':[],'files_reviewed':[],'executions':[],'unreviewed':[],'suggested_changes':[],'automatic_merge_authorized':False},ensure_ascii=False,indent=2))
 js(ROOT/'governance/schemas/AUDIT_ROUND.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','title':'hott.audit-round.v1','type':'object','required':['schema','round_id','base_commit','request_sha256','status'],'properties':{'schema':{'const':'hott.audit-round.v1'},'round_id':{'type':'string','pattern':'^[A-Za-z0-9][A-Za-z0-9_-]{0,95}$'},'base_commit':{'type':'string','pattern':'^[0-9a-f]{40}$'},'request_sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'},'status':{'type':'string'}},'additionalProperties':True})
 js(ROOT/'governance/schemas/DELTA_MANIFEST.schema.json',{'$schema':'https://json-schema.org/draft/2020-12/schema','title':'hott.audit-delta.v1','type':'object','required':['schema','round_id','base_commit','head_commit','base_tree','head_tree','members','review_status'],'properties':{'schema':{'const':'hott.audit-delta.v1'},'round_id':{'type':'string'},'base_commit':{'type':'string','pattern':'^[0-9a-f]{40}$'},'head_commit':{'type':'string','pattern':'^[0-9a-f]{40}$'},'members':{'type':'object'},'review_status':{'const':'NOT_AUDITED'}},'additionalProperties':True})
 write(ROOT/'governance/HANDOFF_RESEARCH_STATUS.md','''# 交接时的研究状态：只作路线图，不替代原文

最后实际数学轮次 R039；R040 是搬迁、说明、读取索引与增量审计工程，没有新数学结论。所有旧 records、原证据、失败版本及未决事项必须保留。

## 已对齐的目标

用户的 Z 哲学与 ASK 是研究起点，不能被改写成已经证明的物理或全称元定理。研究双向现实相对问题：A，原过程能够完成，某种明确理论化新增困难；B，数学分类或存在被提升为未取得的有效交付。主要目标不等同于证明 HoTT ⊢ ⊥；也不预设 HoTT 永远无错。

现在区分 HoTT 已有的逻辑/同伦/计算能力、有效形式系统共有的计算界限、某种具体理论化新增的失真。它不是“已解决所有悖论／已对齐物理宇宙”的结论。原生内核通过、纸笔论证、有限测试、来源恢复、同行看法分开。

## 最近结果与不可丢失的正反例

- R029—31：同域全反射的条件对角界限、分阶段解释和Löb型反射；共享的条件定理，不是HoTT内部矛盾。
- R032：受限解释及证明迁移；全部旧证明可迁移与旧公理在新环境中可证明对应；具体证书只需实际依赖，不能把迁移失败等同于目标不可证明。
- R033—34：依赖运输保留路径作用；具体迁移与只知道相等存在不同。统一 MereMove 被自同构反证排除；不是标准transport自己失效。
- R035—37：暂停后的认识纠偏已进入当前owner；R036具体有限过程两步完成，逐边存在性抽象会新增虚假无限路径；HoTT能够表达并识别它，不能冒称核心强制失真。
- R038：当前态路径提升支持Acc终止证据迁移；每个有限前缀可实现不保证单一无限相容执行。截断和无限相容极限不能一般交换。
- R039：普通发散不敏感弱互模拟本例保may、不保must；无限单边跳过的Bad关系不传递；正确Delay结果等价及有限跳过预算是正例。

## 下一候选（尚未研究）

保结果的确定性部分性等价上，顺序bind与竞争race/timeout是否有不同的下降条件。先固定真实操作、结果读取与商respect，不将两个操作共享“monad”或“等价”名字当成同一合同。不要再增加同类自环样本冒充进展。

RP-B01原生程序模型对应、R026规约/环境有效范围、资源兑现与自指分支仍开放。模型缺失不是删除问题的理由；新AI可独立调度，不能只被前沿最后一句锁死。

## 证据／恢复风险

近轮本机未有原生HoTT/Lean/Agda/Rocq验证，已有草稿需核源码和依赖；不要把普通Lean Eq当HoTT identity。R001原实验与报告版本仍有缺件/冲突；完整记录见 `.codex/research/hott/imports/R001/`。多轮全文认知未通过的状态保留，不能因为包完整或接手模型更大就追认此前已完整理解。新接手必须真正重读。

外部Gemini“找到悖论”的原文是审查对象，其多次撤回和错误模拟已另有评估；不要只读最新赞同，跳过审计。所有原信、回复、日志和修正都在 dialogue 及 session 链。
''')
 # User-visible request preserved in the current handoff record.
 sess=ROOT/'.codex/research/hott/sessions/S-HANDOFF-20260911-040-CROSS-AI'
 write(sess/'REQUEST.md',REQUEST)
 write(sess/'SESSION.md','''# S-HANDOFF-20260911-040-CROSS-AI

任务：完整跨AI交接和未来增量审计机制，不开展新数学。实际来源：当前挂载的 R039 完整Git包及本次 source inventory；另保存全部当前可取得的历史ZIP、bundle、单独文件与嵌套挂载附件。原电脑、过期沙箱、完整平台聊天导出并不因名称出现而实际可访问。

权限：读写当前沙箱工作副本，创建脚本、运行归档/传输测试、本地Git和ZIP；无远端push、其它AI、Work、模型切换、后台任务。接手AI不是已启动进程。

变化：增加 governance/ 平台中立入口与显式路径映射，仍沿用完整单一原治理引擎；默认 exchange/ 按轮保存增量研究、审计原请求、日志和回信。新增脚本先写 scripts/handoff/，再执行。原研究正文、源码、结果、闭包和Schema不改。

证据：artifacts/r040/DELTA_TEST_EXECUTION.json 为16项合成传输测试；完整源清单、包验证、实际Git身份位于外层 manifests/、validation/。哈希或工具通过不认证数学、作者真实性或AI理解。

认知：本轮完整读取交接有关的治理规则和当前记忆/前沿；没有声称451份动态材料已在当前上下文全文加载，也没有做新的全套业务Skill数学运行。为新AI生成同快照的完整原文卷和有序清单。

新AI第一动作：读根README及治理入口，验证包和Git，按全文计划恢复全部必要来源，报告仍缺与冲突。最后数学R039；后续从原前沿自主继续，不再等待Gemini。
''')
 # Root policy updated in place; history is in Git and the untouched source archive.
 p=ROOT/'AGENTS.md';text=p.read_text();insert='''## 跨AI移交与增量审计入口（2026-09-11，R040）

本次用户要求完整交给另一AI，使用平台中立入口 `governance/ENTRYPOINT.md`、路径映射 `governance/PATHS.json` 与 `scripts/handoff/govern.py`。不假设接手者识别 `.codex` 或具备Codex插件；原 `.codex` 作为普通兼容存储和完整历史保留，唯一原引擎不替换、不另建平行STATE。其他平台可在自选治理目录写指针入口，不能复制成两份可变状态。

默认交流总目录为根下 `exchange/`；每轮 `exchange/rounds/<ID>/` 完整记录用户请求、实际增量、证据与待审问题。只在用户指示时从准确共同Git基线导出增量ZIP；包含新增/修改/删除及基线清单、补丁和薄bundle。收到包后只在隔离副本验证和审计，不自动覆盖或合并，不自动将“已发送”当“已认可”。完整约定见 `governance/EXCHANGE_PROTOCOL.md`；它与原读写/checkpoint/证据政策同时适用。

百万上下文不免除全文输入确认。导览卷是当前原文的有序派生副本，清单和哈希不代表模型已读取；每次新Session/压缩仍按当前计划重读，不能为假装容纳而移走开放问题。当前任务为交接，最后实际数学为R039，原下一候选race/timeout保持未执行。

'''
 text=text.replace('## HoTT 每次会话／每次执行的治理入口',insert+'## HoTT 每次会话／每次执行的治理入口',1);p.write_text(text)
 p=ROOT/'README.md';text=p.read_text();start=text.index('## 当前状态与恢复入口');end=text.index('## 项目身份')
 text=text[:start]+'''## 当前状态与恢复入口（2026-09-11，revision40；最后实际研究R039）

**HANDOFF_READY**：用户要求移交给另一AI；本轮只做完整归档、治理平台中立入口、全文导览和增量审计协议。完整交接包先读外层 `README.md`；项目内先读 `AGENTS.md` 与 `governance/ENTRYPOINT.md`。原框架完整保留，不重置历史或数学状态。

最后数学结果与下一候选以当前 MEMORY、STATE、FRONTIER 为准。R039为停顿等价及完成量词，下一项race/timeout未执行。R035暂停、R036—37恢复和之前的当前描述均保留于历史，不替代本次交接状态。原生证明与完整认知验收不得因归档成功升级。

'''+text[end:];p.write_text(text)
 p=ROOT/'.gitignore';text=p.read_text()+'''\n# Transport artifacts are outputs, not research evidence. rounds/ and audits/ remain tracked.\nexchange/outbox/\nexchange/inbox/\nexchange/.work/\n''';p.write_text(text)
 p=ROOT/'.codex/cognition/LOAD_SET.json';obj=json.loads(p.read_text())
 obj['fixed_full_text']+=['governance/ENTRYPOINT.md','governance/PATHS.json','governance/WORKFLOW.md','governance/EXCHANGE_PROTOCOL.md','governance/HANDOFF_RESEARCH_STATUS.md','exchange/README.md']
 p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
 print('Wrote neutral governance, exchange protocol, schemas, source request and R040 session; original runtime and mathematical files unchanged.')
if __name__=='__main__':main()
