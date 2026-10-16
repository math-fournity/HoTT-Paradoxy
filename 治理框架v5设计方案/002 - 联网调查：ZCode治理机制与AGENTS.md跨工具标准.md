# 联网调查：ZCode 治理机制与 AGENTS.md 跨工具标准

（2026-09-18 检索；来源在文末。本机产品事实以 `~/.zcode/AGENTS.md`（用户自己的
全局宪法，逐条记录 ZCode 3.8.1 机制）为权威，联网结果用于交叉与补全。）

## 一、ZCode 的 repo 治理机制（官方文档 + 本机事实合并）

| 机制 | ZCode 事实 | 对本设计的含义 |
|---|---|---|
| 指令注入 | 本机权威：3.8.1 自动组合 `~/.zcode/AGENTS.md` + **workspace 根 `AGENTS.md`**；**不支持 nested AGENTS**、不支持 imports/includes | 根 AGENTS.md 是两宿主唯一的共同自动注入通道 → 必须作唯一宪法入口；不能靠嵌套 AGENTS 分层 |
| Skills | **两级作用域**（2026-09-18 二次修正，依据随产品发布的官方 zcode-guide：`zcode-configuration-guide`/`diagnosing-skills`）：用户级 `~/.zcode/skills/<name>/SKILL.md` 与 **workspace 级 `<repo>/.zcode/skills/<name>/SKILL.md`（及 `.agents/skills/` 兼容层）**；发现顺序=user→.agents→workspace .zcode→workspace .agents→插件，同名首见者胜（user 压 workspace）；frontmatter name+description 必填、description ≤1024 chars（超限整枚丢弃）、正文 >100KB 截断；workspace 级可被 `.zcode/config.json` 按路径禁用；另支持从 Codex/Claude 导入（symlink/copy） | **ZCode 有 repo 内原生 Skill 发现**——repo 内 `.zcode/skills/` 即其项目级通道；跨宿主单真值可用 repo 内 symlink 农场实现（分片 003 修订版）。本机历史实证：嵌套 `workspace/.zcode/` 曾被用作项目配置目录 |
| Memory | 项目级、**默认关**；存于宿主侧 `~/.zcode/cli/memories/projects/<project>/memory/`（repo 外）；明文可编辑；明确**跳过项目指令文件已有内容**（与 AGENTS 类文件互补不重复） | 宿主私有、不入 repo → **不能作治理真值**（本机宪法同判）；repo 的 `MEMORY.md` 文件仍是唯一当前态真值 |
| Repo Wiki | 生成的架构导读，存 repo 外 `~/.zcode/v2/repo-wiki/<hash>/wiki.json`；断言带 file:line 锚；**重新生成即覆盖、无历史版本** | 只能作辅助阅读入口；其"覆盖式再生"违反本 repo 证据纪律 → 明确列为非权威补充 |
| 上下文 | GLM-5.3 深度集成，1M-token 上下文；上下文控制/压缩存在 | ZCode 侧容量宽裕，但 v5 仍按最坏情况（Codex 窗口）定档——成本只是约束之一，注意力质量同样随冗余退化 |
| 权限 | 高权限操作执行前需确认（本机宪法另有"上下文变更前确认"开关） | 与本项目"push/发布需授权"纪律天然对齐 |

## 二、AGENTS.md 跨工具标准（本设计的外部锚）

- 定位：开放的跨工具 repo 级 AI 指令标准（"README for agents"），由 **Agentic AI
  Foundation（Linux Foundation）托管**，60k+ 开源项目在用（openai/codex、
  apache/airflow 等）。
- 语义：根文件 + 可嵌套（最近者优先）；无必填节；用户对话指令优先于文件。
- 支持工具：OpenAI Codex、Cursor、Gemini CLI、Julep/Amp/Factory、Aider、opencode、
  Zed、Warp、VS Code、Devin、Windsurf、GitHub Copilot coding agent 等。
- 业界共存模式（对本设计直接可用）：(a) **单一真值源**——AGENTS.md 为 canonical，
  其他宿主文件引用或镜像；(b) **import/symlink 桥**——Claude Code 等不读 AGENTS.md
  的宿主用 import 把它拉进来；(c) **分层**——根 AGENTS.md 承跨工具公共层，
  宿主专属文件只放增量。
- 已知批评：无正式规范正文、采用实践不一致——所以本设计把"机械可校验"留在
  自家 runtime/validator，不指望标准本身。

## 三、结论：ZCode 侧"能用起来且不维护两套"的现实路径

> **2026-09-18 二次修正（用户提供另一 AI 的相反陈述触发复核）**：原稿"ZCode 无项目级
> Skill 发现"是**错误结论**，已撤回。随产品发布的官方 zcode-guide（`zcode-configuration-guide`
> 与 `diagnosing-skills`）明确：workspace 作用域真实存在——`<repo>/.zcode/config.json`
> （MCP/hooks/skill 禁用）、`<repo>/.zcode/skills/`、`<repo>/.zcode/commands/`，且
> workspace hooks 以 config 形式存在（需 `hooks.enabled: true`）。错误来源：(a) 文档站
> Skill 页以用户级为主、未展示 workspace 路径，我把"未见"当"不存在"；(b) 用户全局
> `~/.zcode/AGENTS.md` 只描述了用户级 skills 并称"Project Hook 被忽略"——该宪法条款与
> 随产品指南**冲突**，疑似过期（待用户在其全局治理中裁定更新）。本修正使 containment
> 结论变得更好：ZCode 原生触发可以在 repo 内实现（`.zcode/skills` symlink 农场），
> 全局零足迹。
>
> **宿主事实基线（防再漂移）**：本方案对 ZCode 机制的引用源钉定为随产品发布的
> zcode-guide 插件 **0.1.0**（`~/.zcode/cli/plugins/cache/zcode-plugins-official/
> zcode-guide/0.1.0/skills/zcode-configuration-guide/SKILL.md` 及 `diagnosing-skills`），
> 检索日 2026-09-18。宿主版本升级后须复核本表；用户全局宪法中的产品条款
> （"Project Hook 被忽略"、skills 仅用户级）与该基线冲突时，以较新者为准并
> 提请用户更新宪法——产品事实类漂移的教训已由本次修正支付过一次学费。
>
> **三次修订（2026-09-18 晚）：Codex 全局侧差分清单（上次同步锚点 = `~/.zcode`
> 立档日 2026-09-02）**。此后 `~/.codex` 治理已演进至 `GOVERNANCE_VERSION
> = 3.23.1`，ZCode 全局侧未跟进的增量按价值排序：(1) **学术数学表述强制协议
> `ACADEMIC_MATHEMATICAL_COMMUNICATION_V1`**（9/14，AGENTS +46 行并注入三个
> 核心 Skill）——数学/HoTT 任务的措辞分解纪律（悖论/HoTT 问题/不可停机/自指/
> 时间 vs 时序等词的强制分解），与本 repo 判词纪律同源但更强，**ZCode 侧会话
> 做本研究时缺这层全局协议**，最值得同步；(2) **GOVERNANCE_VERSION 版本锚
> 机制**（v3.20–3.23.1：薄路由 + current line + 8 stable references）——今日
> 两次漂移事故正是缺版本锚的代价，ZCode 宪法应同款设锚；(3) 分片 3.16 规范
> 作为领域路由表项接入（本 repo 已有自有 v2 合同，全局层只需薄路由）；
> (4) dev-notes 归档规范 + `dev-notes-archive` skill（含 `archive_turn.py`
> 457 行脚本，可直接复用）；(5) 三个 Codex 核心 Skill 的多轮合同注入（ZCode
> 四 Skill 停在 9/2 适配版，需内容 diff 决定逐项移植）；(6) 并行 worktree
> 认知合同（9/13，ZCode 多工作面部分对应，需适配）；(7) actor R-093（当前
> AGENTS 已 grep 不到，身份待同步时核实）。注：RTK 约定为 9/2 ZCode→Codex
> 反向流动，同步是双向的。**版本锚补充**：本方案对 Codex 全局层的引用基线
> = `~/.codex/GOVERNANCE_VERSION` 3.23.1（核对日 2026-09-18）。


> **2026-09-18 补查（用户质询触发）**：Codex CLI 的 Skill 发现有两个默认位置——
> 个人级 `~/.codex/skills/` 与**项目级 repo 内 `.codex/skills/`**（OpenAI Skills
> 文档及多源一致）。这意味着 repo 的 `.codex/skills/` 不是死路径而是 Codex 的
> 活通道——任何"搬走整棵树"的方案都会砍掉它。此事实已回写分片 003/010
> （默认方案改为树不动）。

1. **宪法层**：根 AGENTS.md 两宿主都自动注入（ZCode 本机事实 + Codex 原生）→
   唯一入口，零适配。
2. **SOP 层**：正文 canonical 留在 repo 树内；ZCode 靠 AGENTS 文本路由按档全文读
   （无宿主机制依赖）；可选的官方 symlink 导入通道留给用户按机器自装（非必须、
   默认不装——全局注入元数据会向所有项目收税）。
3. **执行层**：`cognition_runtime.py` 是纯 python3 CLI，ZCode 有 Bash——本 Session
   已经实际运行过 `plan`（被漂移 fail-closed 拦截，恰好证明可运行）。零改造复用。
4. **证据层**：SESSION.md/RUNS.json/runs 目录天然宿主中立（只是文件）；两宿主的
   原始 trajectory（Codex rollout jsonl / ZCode model-io）各留宿主侧作补充证据，
   repo 只收中立收据。
5. **ZCode 独有件**（project memory、repo wiki）：声明为宿主私有辅助件，禁入真值链。

## 来源

- [ZCode Agent | ZCode Docs](https://zcode.z.ai)（产品主页）
- [ZCode 文档：Skill](https://zcode.z.ai/cn/docs/skill)
- [ZCode 文档：Memory](https://zcode.z.ai/cn/docs/memory)
- [ZCode 文档：Repo Wiki](https://zcode.z.ai/cn/docs/repo-wiki)
- [agents.md 官方站](https://agents.md)
- [Augment Code – AGENTS.md vs CLAUDE.md](https://www.augmentcode.com)
- [Termdock – SKILL.md vs CLAUDE.md vs AGENTS.md](https://termdock.com)
- 本机权威：`~/.zcode/AGENTS.md`（ZCode 3.8.1 产品事实，用户自维护）
