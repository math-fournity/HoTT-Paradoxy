# HoTT AI 历史交接与综合研究工作区 — 从这里开始

> **当前顶层入口（2026-09-12）**：本目录已经是新的 Git repo，也是今后本项目的唯一综合工作根。历史交接包、三类 AI 来源、`ALL-Markdown` 的本地 GPT 研究材料、WebGPT 工作目录快照和 `理解章节` 均在这里按来源边界保存；后续工作必须先读取本文件、`AGENTS.md`、`MEMORY.md`、`核心认知.md` 和 `.codex/` 治理入口。

## 当前综合工作区

当前工作链路是：

```text
用户原始提问 → sources/prompts/ → 核心认知.md → 理解章节/ → HoTT/ 与审计/验证证据
       │                 │              │             │
       └──来源快照──→ sources/       └──会话后评估──→ .codex/cognition/
```

关键入口：

- `核心认知.md`：按时间顺序编号的、由三份历史 primary、Codex supplemental 和明确登记的用户治理原文组成的悖论/HoTT 悖论业务原文认知账本；当前为 `core-cognition-generation-2`、913 个 `KC-*`。每次工作开始全文加载，结束逐编号回评。它拥有用户原始研究意识，不拥有 AI 结果。
- `方向追踪.md`：跨 LocalGPT/WebGPT 的研究方向、候选、依赖、优先级和下一判别动作的当前投影；不替代 STATE 或 core。
- `全景视野.md`：跨 LocalGPT/WebGPT 的结果、正反例、失败、未知、产物、Git 和验证范围的当前投影；不替代数学主张矩阵。
- `理解章节/`：历史认知闭包及本次 transform 的主要成果；它是当前研究知识的 owner 候选，不以原始对话录替代。
- `sources/`：只读历史来源快照、提问原文、WebGPT 工作目录、本地 GPT `ALL-Markdown` 工作及 Gemini/WebGPT 导出。
- `audit/` 与 `scripts/audit/`：来源 manifest、覆盖矩阵、22,226 行跨源 reconciliation register、理解章节 merge receipt、fresh load receipt、提取重放与验证脚本；“完整”只以这里的可复现证据为准。
- `.codex/`：本 repo 的本地 Codex 治理框架；项目级规则补充全局规则，不替代全局规则。固定加载前三项为 `核心认知.md` → `方向追踪.md` → `全景视野.md`，然后才加载 HoTT 三问和其它动态依赖。
- `HoTT/`：从 `/Volumes/D/ALL-Markdown/HoTT/` 收录的研究工作副本；它保留本地 GPT 的工作记录，不自动等于当前数学真值。

`AI对话录/` 和 `workspace/` 仍保留在磁盘上作为原始嵌套 repo，但已由顶层 `.gitignore` 排除；顶层 `sources/` 是归档快照，后续修改不得直接把这两个嵌套工作树当作当前工作根。`/Volumes/D/ALL-Markdown/aistudio-docs/` 按用户要求不恢复；`HoTT_is_GONE_COMPLETE.md` 只作为有 provenance 的历史 AI 产物保存，是否覆盖原目录的事实仍标为未证明。

本轮框架对比和 core 内容边界见 [治理框架对比审计与核心认知增补评估-20260912.md](治理框架对比审计与核心认知增补评估-20260912.md)；三件套的实施/融合方案见 [实施方案-三件套研究连续性治理与理解章节融合-20260912.md](实施方案-三件套研究连续性治理与理解章节融合-20260912.md)。

**交给接手 AI 与用户。建立日期：2026-09-11。最后实际数学研究：R039。交接治理状态：顶层本地 STATE revision 12；R040/R041 只做 WebGPT 交接/治理工程，不是新的数学突破。**

本包原本是当前沙箱可取得的项目材料的完整、可验证交接，不只是一份摘要。现在它已被提升为顶层综合 repo：最新可工作目录、完整原治理框架、Git历史、当前挂载原件、逐轮研究/审计/失败记录、历史对话提取和未来增量交换工具均在同一个顶层目录。原 `workspace/` 仍是 WebGPT 交接时的嵌套工作副本，供历史核对和来源快照使用；不要把它误当作当前顶层工作根，也不要在其它历史副本中继续工作。

## 1. 最先了解的事实和边界

项目叫 **ALL-Markdown / HoTT**。主要目标是 Z 哲学和 ASK 视角下的双向现实相对研究：某种明确的 Think in HoTT 如何使原可完成过程出现额外完成困难，或把数学上的存在/分类提升成未取得的有效交付能力。主要任务不等同于证明 HoTT 内部不一致，也不预设 HoTT 必错或永远正确。

最新认识严格区分：HoTT 已有的逻辑/同伦/计算能力；有效系统共有的可计算性与反射界限；特定理论化额外造成的失真。正确拒绝、正确报告未知和保全条件，是必须保留的正向结果。不能以普通程序也有的停机限制证明 HoTT “没考虑时间”，也不能因它有计算结构就断言它已处理所有悖论或完全对齐物理宇宙。

历史中不少结论只有纸笔推导和有限模型检查，原生证明助手未运行。R001原实验资料仍有缺件与版本冲突。**接手不能将 ZIP 完整性、Git提交、另一个AI的赞同或旧的PASS文字当成数学认证。**最后一轮的论文下载失败与读网页成功等边界仍在原记录里；本次交接没有重新认证它们。

本包不是平台完整聊天导出：保存了此前落盘的用户原话、公开回答、原始Gemini记录、信件、源码和结果。无法恢复未作为文件提供的旧沙箱状态、丢失的原始工具输出或完整平台会话数据库；不包含本模型隐藏推理。不要根据历史路径/链接自行补造不存在的附件。

## 2. 原始 handoff 包的数据地图（历史保留；当前入口以“当前综合工作区”为准）

`.codex` 是**项目根内的相对子目录**，不是与 `/mnt/data` 并列的绝对数据根。原环境中有：

| 原位置/类别 | 本次如何收录 |
|---|---|
| `/mnt/data/HoTT_silent_steps_rev39_with_git.zip` | 作为唯一最新完整基线解包为 `workspace/`；继承原Git，不重新初始化 |
| 原项目 `.codex/` | 全部保留：治理、Skills、状态、Session、研究正文、历史、事务、验证 |
| 原项目 `.git/` | 全部保留在 `workspace/.git/`；另有交接时的完整Git bundle |
| `HoTT/`、`认知闭包/`、根文档、`scripts/`、`artifacts/` | 直接在最新工作树中；代码、失败、来源与记录均不省略 |
| `/mnt/data` 中历次 ZIP、bundle、单独附件、早期 ALL-Markdown 目录、嵌套 user-… 挂载路径 | 全部进入无损原件存储 `archive/`，保留原文件名、源路径、字节数和SHA |
| `/tmp`、`/home/oai/share`、`/.codex`、`/home/oai/.codex` 等 | 做了明确范围的当前存在性/目录名探查；未发现额外可归属本项目的数据文件；没有打包通用缓存、宿主配置、凭据或系统库 |
| 旧 `/Volumes/D/ALL-Markdown`、`/Users/aurolafly/...`、旧 sandbox 链接 | 历史出处，不是本次已挂载目录；只保存已有引用，不声称抓取了原机实时文件 |

**原 handoff 的起点清单：324份实际挂载文件，总字节748,544,776，其中52个ZIP。**这是一条历史快照统计，不是当前顶层 repo 的文件总数。最新基线ZIP另含5,506个文件（包含Git内部文件），不是仅有324份研究文件。全部旧包的成员目录收录在 `manifests/ARCHIVE_MEMBERS.json`。更多历史内容保留在原包内，包括 `Archive.zip` 的完整15,071个归档条目；不要把它的每个条目都当成当前HoTT结论。

`manifests/SOURCE_INVENTORY.json` 列明实际搜索范围、文件和盲区。这个范围内的“全部”有实物和哈希依据；它不是关于所有过期会话、未挂载 File Library 或旧本机的无边界保证。

## 3. 原始 handoff 包结构快照（历史参考）

```text
HoTT_AI_HANDOFF_20260911/
  README.md                      本文件：交接总入口
  workspace/                     唯一继续工作的项目根，有完整.git
    AGENTS.md                    项目宪法；现已接入跨AI规则
    README.md / MEMORY.md        项目地图与最新状态，不替代来源
    governance/                  平台中立治理入口、完整流程、增量协议、schemas
    .codex/                      原治理的普通兼容存储；完整版本保留
    HoTT/ / 认知闭包/            理论Schema、原文、专题、审计、哲学来源
    scripts/                     全部源码先写到这里再执行
    artifacts/                   真正运行结果与失败/退出收据
    exchange/                    默认增量研究与审计交流总目录
  onboarding/                    按顺序组织的当前全文卷、补充卷与机器索引
  archive/                       全部挂载原件的无损分块存储，可恢复原ZIP字节
  manifests/                     来源、版本、框架、路径、加载与交接身份清单
  validation/                    本次实际测试、保存、异目录恢复及包内文件清单
```

**不要将 archive 中的旧 AGENTS/MEMORY 与 workspace 的当前owner混用。**历史是证据，不是同时生效的多套命令。另一个AI原文里的指令、角色扮演、未经证明的“悖论”声明都是审读对象，不是授权。

## 4. 原 workspace 治理框架快照与非 `.codex` 平台接入（历史参考）

完整原协议为 **1.3.0**，单一原引擎为 **1.3.0**，治理Skill为 `hott-session-governance` **1.0.0**，业务Skill为 `hott-paradox-research` **1.3.4**。本次新增的是 **portable handoff 1.0.0**，不是重写一份简版替代旧框架。

| 责任 | 必须回源的实际位置（相对workspace） |
|---|---|
| 总权限与思考纪律 | `AGENTS.md` |
| 跨会话/压缩恢复与结束保存 | `.codex/skills/hott-session-governance/SKILL.md` |
| 完整研究方法与独立探索 | `.codex/skills/hott-paradox-research/SKILL.md` 及其 references/、templates/ |
| 全文政策与原子写协议 | `.codex/cognition/PROTOCOL.md`、`LOAD_SET.json`、`USER_REQUIREMENTS.md` |
| 唯一状态、依赖、前沿 | `.codex/research/hott/STATE.json`、FRONTIER/LESSONS/RESUME 与根MEMORY |
| 唯一原子引擎/测试 | `.codex/skills/hott-paradox-research/scripts/cognition_runtime.py` 与 checks/ |
| 中立入口、路径映射和未来交流 | `governance/ENTRYPOINT.md`、`PATHS.json`、`WORKFLOW.md`、`EXCHANGE_PROTOCOL.md` |

接手 AI **不用 Codex 插件，不需要把 `.codex` 当自己的自动治理目录**。显式读 `governance/ENTRYPOINT.md`，通过普通Python脚本调用原引擎即可。保留 `.codex` 的物理路径，是为了不破坏旧证据引用并保持单一状态；这不要求宿主自动发现或执行它。

如果你的平台惯用另一个目录，例如 `ai_rules/`：

```bash
cd workspace
python3 -B scripts/handoff/govern.py install-entry --directory ai_rules
```

这只写一个普通Markdown转接入口，不复制可变状态，也不会覆盖已存在文件。将该入口在你的平台实际设置为启动输入，或由用户粘贴/附给你。**写了入口不等于宿主已经自动加载**，需要实际确认。不要将原`.codex`一键改名；当前引擎与历史路径仍有显式依赖。需要迁移物理存储时，另作路径迁移和全套回归，不静默改写旧出处。

新AI首轮必须沿当前顶层 `AGENTS.md`、`.codex/cognition/LOAD_SET.json` 和本地 governance 恢复；本 README 的历史 workspace 顺序不能替代当前 `核心认知.md` 全文。没有全部读入，不得声称认知验收已通过。出现文件变动、跨Session、压缩或截断时重建读取计划；同一次研究→保存的正常内部调用不用无限重入。

## 5. 原 handoff 包给大上下文 AI 的加载方案（当前顶层覆盖规则优先）

目标不是喂给你全部重复ZIP、Git对象和opaque签名，而是先一次性提供**当前真正需要的全部正文**，再按来源补齐历史或专项语料。全部原件仍保留，不为节省上下文删掉开放问题。

### 推荐阅读顺序

1. 当前顶层先读本README、`AGENTS.md`、`MEMORY.md`、`核心认知.md` 和 `.codex/` 本地治理；下面原 `workspace/AGENTS.md`、中立入口与原治理/业务Skills 只作为历史快照参考。
2. 按 `onboarding/READING_PLAN.json` 的核心顺序，完整读第五认知闭包，再完整读已对齐三问。这是理念和问题源头，不可用摘要替代。
3. 完整读用户原话、当前Z/时间owner、主张矩阵、Theory Schema；Schema只作规则地图，使用具体规则时继续读固定版原始源码。
4. 完整读当前MEMORY、STATE、FRONTIER、LESSONS、RESUME与所有活动/待复核记录的正文、来源和递归依赖。旧原话/旧结论/新修正必须分开。
5. 按补充索引读当前未在核心集合中的历史主文、Schema全文、代码/测试、结果和通信；关注实际依赖，不把摘要和相同标题算成同证据。
6. 原始大语料、旧ZIP、重复checkpoint和完整Git对象属全量保全层；初次可按索引定位，追溯具体来源时再展开。它们不都是治理每次要求加载的材料。

`onboarding/volumes/core-*.md` 是从当前计划中的文件按原行序生成的**全文**，不是摘要；每段有项目相对路径、原SHA、行范围及EOF信息。分卷只是绕开单次工具输出限额。补充卷 `supplement-*.md` 与清单标明范围。**若卷生成之后工作树变化，应重生成或直接读新文件，不拿旧卷当当前状态。**

记录有确切的文件数、行数和UTF-8字节数；只有本机能离线取得的tokenizer才给相应计数。另一模型的分词器和系统预留未知，不能仅凭“100万”保证所有材料一批放得下。优先完整加载核心；留出推演/回复空间；如宿主仍截断，明确未加载并重建，不用旧收据冒充全部进入上下文。原433/451等历史数字不是永久上限，执行前重新plan。

加载后请写一份你自己的 `RECEIVER_ACK.md`：实际HEAD、读过的卷/文件/快照、未读和缺失、当前目标、最近正反结果、原生工具状态、你理解的下一动作。它是一份真实接手记录，不由本包预先代填PASS。

## 6. 先验证，再开始工作

从本顶层目录运行（无网络、不会运行旧研究脚本）：

```bash
python3 -B workspace/scripts/handoff/verify_package.py --package-root .
git -C workspace rev-parse HEAD
git -C workspace status --short
git -C workspace fsck --full
```

真实基线、标签和SHA在 `manifests/HANDOFF_IDENTITY.json`。完整ZIP自身SHA在同名 `.sha256` 文件中；ZIP不能把自己的最终哈希放进自己而造成自引用。校验是完整性，不是认证作者、数学证明或宿主认知。

日常命令（已进入workspace）：

```bash
python3 -B scripts/handoff/govern.py plan --output exchange/outbox/receiver-plan.json
python3 -B scripts/handoff/govern.py read --snapshot <plan.snapshot> --path <计划中的路径> --start-line 1 --max-bytes 20000
python3 -B scripts/handoff/govern.py check --snapshot <同一snapshot>
```

原子checkpoint格式、dry-run/apply、并发拒绝、中断恢复见 `governance/WORKFLOW.md`。运行器只认证字节和事务。每个里程碑保存新的不可覆盖研究Session和实际证据，更新五个current owner，之后本地commit。

不要批量运行旧 `scripts/session/r0xx_*.py`：不少历史脚本用于固定旧revision或旧路径，作用是证据而不是通用恢复命令。新中立入口按相对路径解析根。研究代码由接手者审查后显式运行，缺少工具时留NOT_RUN。

## 7. 未来只发增量：exchange/目录与一键导出

默认交流总目录就是 **workspace/exchange/**。每轮独立目录 `rounds/<ID>/`，包含REQUEST、RESEARCH_DELTA、AUDIT_REQUEST、RUNS及ROUND身份。它们应跟踪于Git；正式研究结论仍落在原治理指定路径。

### 开始本轮

```bash
python3 -B scripts/handoff/delta_tool.py round-init --id R041-EXAMPLE --request-file <用户原请求.md> --base handoff-r040
```

研究完成：填实增量记录，保存代码/原始运行日志与所有失败，按原框架checkpoint，检查Git差异并commit。再在用户要求时：

```bash
python3 -B scripts/handoff/delta_tool.py export --round R041-EXAMPLE
```

得到 `exchange/outbox/R041-EXAMPLE.zip` 与导出收据。包内只有base之后的新增/修改文件、删除清单、完整前后哈希目录、差分和薄Git bundle；不会再次塞入全部历史语料。二进制也可以传递。工作树脏、记录缺失、base错误、路径不安全会拒绝；没有自动发信或网络操作。

**用户以后可以只说：**“按增量交接协议，把自上次双方确认的基线以来的工作，打包给 Astra 审计。”不需要每次重新设计目录。

初始基线是标签 `handoff-r040`；之后用实际共同确认的commit。已发送不等于已收到，已收到不等于审计通过，审计通过不等于用户授权合并。未收到审计时可继续从相同共同基线导出累计净增量；不得为了缩小ZIP擅自换成接收者没有的中间提交。

### Astra或另一审计员接收

用可信基线里的工具，而不是直接执行新ZIP中的代码：

```bash
python3 -B scripts/handoff/delta_tool.py verify /path/to/R041-EXAMPLE.zip --with-base
python3 -B scripts/handoff/delta_tool.py stage /path/to/R041-EXAMPLE.zip --destination /path/to/new_isolated_audit_workspace
```

`stage` 只创建新的隔离副本，验证bundle与实际文件后停止；不覆盖原工作树，不运行新代码，不自动合并。它要求当前根HEAD精确匹配base，否则应先建立那个base的独立检出。审计报告落 `exchange/audits/<ID>/` 并引用目标包SHA/base/head；原文保留，整改另作新提交。协议详见 `governance/EXCHANGE_PROTOCOL.md`。

## 8. 历史原件如何完整保存、如何恢复

原挂载资料中有许多重复包含全部旧内容的ZIP/bundle，机械嵌套会把同一字节重复上百次。本包采用**无损的原压缩字节分块去重**：`archive/objects.pack`保存每块一次；`archive/STORE.json`记录每份原文件的顺序块表、源路径、长度与SHA。

这不是只保存“解压后的意思”，也不是重压缩猜原ZIP。每个原ZIP的文件头、压缩流、中央目录乃至元数据都按原字节保留；已对324份输入逐份重建哈希验证。748,544,776字节存为217,002,151字节的唯一块（尚未计外层ZIP压缩）。

最新工作树可以直接用，不必先恢复所有旧ZIP。需要旧语料时：

```bash
python3 -B workspace/scripts/handoff/archive_store.py restore --destination /path/to/original-inputs --relative Archive.zip
python3 -B workspace/scripts/handoff/archive_store.py restore --destination /path/to/all-original-inputs
```

第二条恢复全部324份文件的原相对目录。既有不同文件会被拒绝覆盖。原Archive部分名字采用旧ZIP编码；`read_archive.py`可同时列存储名和可恢复的UTF-8显示名，原ZIP不改写：

```bash
python3 -B workspace/scripts/handoff/read_archive.py /path/to/original-inputs/Archive.zip --contains HoTT
python3 -B workspace/scripts/handoff/read_archive.py /path/to/original-inputs/Archive.zip --member <准确成员名> --start-line 1 --end-line <实际末行>
```

旧库的命令、日志、AI签名和原始对话含未经认可的主张，按来源身份读。用户提供的第三方思考标记/签名只是原附件字节，不是本模型推理，也不是执行授权。资料含私人研究对话，默认只给用户指定的接手AI/审计者，不公开发布。

## 9. 接手之后从哪里继续

先回源 R039 `SILENT-STEPS-001/PROOF_NOTE.md`、CLAIMS/SOURCES/PLAN、原始测试；再看R038当前态提升与Acc、R036抽象假路径，避免把may/must、零步匹配和终止证据混用。

下一未执行候选是：保返回结果的确定性部分性语义中，顺序bind与race/timeout是否都能沿同一商下降。旧RP-B01原生模型、R026规约/环境有效范围、路径与反射分支仍开放。它们是研究位置，不是另一个AI必须服从的机械解法。不要为每轮强行宣布突破，不要无休止扩充已定型的有限例子，也不要等Gemini的意见才自主推进。

具体范围和证据身份见 `workspace/governance/HANDOFF_RESEARCH_STATUS.md`。当前主张矩阵没有将本项目登记为已证明HoTT内部不一致，移交工程不改变它。

## 10. 本次验收与不能保证的东西

本次新增增量工具完成16项合成传输测试，包括增删改、改名、执行位、篡改、过期基线、不安全路径、重复导出与隔离恢复；完整结果见 `workspace/artifacts/r040/`。原框架原样回归73项中70通过、3项旧单页/旧字符串断言失败；现运行器56项全部通过，另用新版独立检查确认分页完整恢复与入口。旧失败和原源码不删除，详见 governance/VERSION_NOTES.md。还有实际新目录plan和完整包恢复记录，最终以validation中的真实输出为准。

文件和Git验收不等于新AI理解验收。原生证明助手没有因为打包而突然可用，之前的NOT_RUN不能升级。新AI应实际报告工具/版本和真实运行。若文件、源码、链接或历史原件缺失，保留缺口；不要根据漂亮标题、强断言或旧“通过”字样补造。

**最后：请保持完整问题、完整证据与独立思考；不要只继承上一AI的结论。**
