# 事实修正：ZCode 有 workspace 级 .zcode 目录（我此前判断错误）（2026-09-18）

## 用户提问（逐字）

> 不完全是。ZCode **有**项目仓库里的 `.zcode` 目录，用来做 per-project 配置；只是默认不一定会自动生成一整套目录，所以看起来会像"没有"。
> （中略：对方 AI 给出 Claude/.claude、Codex/.codex、ZCode/.zcode 对照表，引用官方文档：workspace 级 skills `<workspace>/.zcode/skills/<skill-name>/SKILL.md`、项目级配置目录 `<project>/.zcode/` 跟着仓库走、项目约定=仓库根 AGENTS.md、全局约定=`~/.zcode/AGENTS.md`；另指出 /init 不一定铺出完整 .zcode overlay、会话数据/checkpoint/wiki 在 ~/.zcode 不进仓库。）
> 以上是另外一个AI说的，为什么和你说的不一致？

## AI 最终回复（逐字，与对外回复一致）

**对方 AI 是对的，我此前"ZCode 无项目级 Skill 发现"的判断是错的，已核实并修正设计报告。核实依据是随 ZCode 产品一起发布的官方指南（zcode-guide 插件：`zcode-configuration-guide` 与 `diagnosing-skills`），它明确写着：ZCode 的扩展资源有用户/ workspace 两级作用域——workspace 配置文件 `<repo>/.zcode/config.json`（MCP、hooks、skill 禁用），workspace skills `<repo>/.zcode/skills/<name>/SKILL.md`（另有 `.agents/skills/` 兼容层），workspace commands `<repo>/.zcode/commands/`；skills 发现顺序=user .zcode → user .agents → workspace .zcode → workspace .agents → 插件，同名首见者胜（user 压 workspace，更深的 cwd 位置压 repo 根）；workspace hooks 以 config 形式存在、需 `hooks.enabled: true`。本机还有历史实证：嵌套仓库 `workspace/.zcode/` 曾被用作项目配置目录（内含 HOTT_ENTRYPOINT.md）。**

为什么不一致——三个来源层面的原因，两个是我的责任：(1) **我把"未见"当成了"不存在"**：文档站 Skill 页以用户级 skills 为主，我的抓取摘要里甚至闪过"导入对话框有 project 目标"的线索，但没展示 workspace 路径，我据此下了否定结论——这违反了本 repo 自己的纪律（"不能因'没有看到'断言不存在"）。(2) **我过度信任了你的全局宪法**：`~/.zcode/AGENTS.md` 写"User Skills 在 ~/.zcode/skills"、"Project Hook 被忽略"，我把它当作完整且最新的产品事实；现在它与随产品指南直接冲突（workspace skills/commands/MCP/hooks 都存在），疑似该宪法条款已过期——这是**你的**全局治理资产，是否更新由你裁定（我已把它列为 v5 决策点 6）。(3) 对方 AI 看的可能是当前完整文档/更新版本，而我的两次网络抓取都没落到 workspace 作用域那一页。三方对照的教训：产品事实要以随产品发布的指南 + 实测为准，宪法里的产品条款也要标版本。

这个修正让设计**变得更好**而不是更糟：ZCode 的原生触发可以在 repo 内实现 containment——v5 修订为 `<repo>/.zcode/skills/<name>` → 符号链接指向 `.codex/skills/<name>`，**随 git 提交**：ZCode 原生发现三枚 SOP、真值仍是单株树、`~/.zcode` 全局零足迹（你上一轮担心的跨项目元数据税与误触发彻底消失，连"可选全局导入"都不需要了）。合同层不变（宿主最小合同：根 AGENTS 注入 + 文件读 + shell 执行）；文本路由仍是必要条件，`.zcode/skills` 与 `.codex/skills` 一样只是原生加速器。待实测项：两宿主对 symlink 目录的发现行为，已进 P2 验收门。设计报告分片 002（机制表+二次修正注记）、003（ZCode 接入段+矩阵行）、010（验收门+决策点 5/6）已同步修订。
