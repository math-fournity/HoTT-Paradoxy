# ZCode 宿主接入说明 · zcode-integration v1.0.0

> 建立：2026-09-11，接手 Session `S-GOV-20260911-041-ZCODE-INTEGRATION`（ZCode Desktop 3.8.1）。
> 上层：本文件是 `governance/ENTRYPOINT.md`（portable handoff v1.0）在 ZCode 宿主上的特化操作说明。
> 冲突裁决顺序：根 `AGENTS.md` → `governance/ENTRYPOINT.md` → `.codex/cognition/PROTOCOL.md` → 本文件。本文件不修改原协议 1.3.0、原引擎 1.3.0、业务 Skill 1.3.4 的任何规则。

## 1. 定位与不变量

本文件说明 ZCode Desktop 宿主如何正确承载本项目：哪些材料 ZCode 会自动加载、哪些必须显式读取、哪些宿主机制不可作为治理真值。它解决的是**接入与路由**，不产生第二套状态：

- 不复制、不镜像任何可变状态（STATE/MEMORY/FRONTIER/LESSONS/RESUME 只经 `.codex/skills/hott-paradox-research/scripts/cognition_runtime.py` 唯一引擎 checkpoint 更新）；
- 不声称宿主已自动加载任何未实际进入当前模型上下文的正文；
- 不改变 `.codex` 物理存储、`governance/PATHS.json` 路径映射与 exchange 协议；
- 本文件自身是治理文档，修订须留 Git 历史，原字节不覆盖删除。

## 2. ZCode 产品事实基线

来源：产品事实权威库 `/Users/aurolafly/zcode`（`docs/governance/ZCode治理机制限制与Codex框架安装说明.md` 等），原核查 2026-08-25，本 Session 复核仍一致。产品版本 **ZCode 3.8.1 / build 3.8.1.5310**。

| 机制 | 事实 | 对本项目的含义 |
|---|---|---|
| 指令组合 | 仅自动组合全局 `~/.zcode/AGENTS.md`（先附加）与 workspace 根 `AGENTS.md`（项目主指令）；不支持 nested AGENTS、imports/includes、rule 文件自动选择 | workspace 根 `AGENTS.md` 是 ZCode 唯一自动入口；`governance/`、`.codex/`、`认知闭包/`、`HoTT/` 一律显式读取 |
| Skills | 用户级 `~/.zcode/skills/<name>/SKILL.md`；description 超 1024 chars 整个 Skill 丢弃，body 超 100KB 截断；启用过多 metadata 每 turn 进 context 会退化 | 项目内 Skill 不注册为 ZCode user Skill（见 §5）；项目内 `.codex/skills/` 对 ZCode 无特殊身份，只是普通目录 |
| Hooks | 项目 Hook 被忽略（安全设计）；user Hook 在 `~/.zcode/cli/config.json`，Session 启动时快照，改后需 fresh Session | 本项目不依赖任何 Hook 承载治理；勿在项目内放 hook 期望生效 |
| Project Memory | 默认关闭；仅主对话使用；不可浏览/清空；不可作可审计治理真值 | 仓库内 `MEMORY.md` 是唯一当前态 owner；禁止把 STATE/MEMORY 内容镜像进 ZCode Project Memory |
| CLI/ACP | 当前无支持的 ZCode CLI/ACP；Desktop 不能被外部 broker 自动控制 | 本项目一切操作经用户在 ZCode 会话内实际执行；无后台自动运行承诺 |
| 会话轨迹 | raw model-io 在 `~/.zcode/cli/rollout/model-io-sess_*.jsonl` | 行为验收的 L1/L2 证据源；含完整上下文，永不入 Git/公开回答（见 §8） |

## 3. 加载映射

**ZCode 自动加载（每 turn 组合）：**

1. `~/.zcode/AGENTS.md`（用户全局治理，含跨宿主共享能力索引路由）
2. `<workspace>/AGENTS.md`（本项目宪法，含 R040 跨 AI 移交入口节）

**ZCode 不会自动加载、必须按 `governance/ENTRYPOINT.md` 与 `.codex/cognition/LOAD_SET.json` 显式全文读取的（固定集合摘要）：**

- `governance/ENTRYPOINT.md`、`PATHS.json`、`WORKFLOW.md`、`EXCHANGE_PROTOCOL.md`、`HANDOFF_RESEARCH_STATUS.md`、本文件
- `.codex/skills/SKILL_ROLES.json`、`hott-session-governance/SKILL.md`、`hott-paradox-research/SKILL.md`
- `.codex/cognition/PROTOCOL.md`、`USER_REQUIREMENTS.md`、`LOAD_SET.json`
- 第五认知闭包、已对齐三问、用户原话、Z/时间 owner、主张矩阵、Theory Schema
- `MEMORY.md`、`README.md` 与 `.codex/research/hott/` 下 STATE/FRONTIER/LESSONS/RESUME、最近会话、全部开放状态记录及递归依赖（由 `govern.py plan` 动态展开）

研究类工作开始前，固定集合 + 动态集合必须全部真正进入当前模型上下文；治理/维护类工作（如本轮）至少完整读取治理链，并如实记录未加载范围。

## 4. ZCode 会话标准流程

### 4.1 接手验收（首次或换机）

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911   # 包根
python3 -B workspace/scripts/handoff/verify_package.py --package-root .
git -C workspace rev-parse HEAD && git -C workspace status --short && git -C workspace fsck --full
```

注意：密封包清单 `validation/FILE_MANIFEST.json` 只对接手时点负责。接收方一旦开始工作（新增文件、checkpoint、commit），顶层重跑 `verify_package.py` 会报"Unexpected files"——这是预期行为，此后完整性以 Git 差异对 `handoff-r040` 基线与 exchange 增量协议为准。

### 4.2 生成读取计划

```bash
cd workspace
python3 -B scripts/handoff/govern.py plan --output exchange/outbox/<本轮>-plan.json
```

### 4.3 全文读取（含 RTK 关键警告）

本机 ZCode 配置了 RTK 输出压缩 Hook（`PreToolUse` 自动重写 Bash 命令输出）。**`govern.py read` 输出的 `BEGIN_FULL_TEXT` 块被过滤或压缩后，不再是"全文进入上下文"**。因此：

- 全文认知加载一律用 `rtk proxy` 绕过过滤：`rtk proxy python3 -B scripts/handoff/govern.py read --snapshot <s> --path <p> --start-line <n> --max-bytes 20000`；或
- 直接用 ZCode 内置 Read 工具读文件（不经该 Hook），再自行核对 plan 中的行数/哈希一致性。

普通状态检查（`git status`、`ls`、清单统计）用压缩输出没有问题。

### 4.4 RECEIVER_ACK

按包外层 `onboarding/RECEIVER_ACK.template.md` 写真实接手记录（实际 HEAD、读过的文件/卷、未读与缺失、理解、验证状态、下一动作），不预填 PASS。研究续作前必须完成完整核心加载；未完成就如实标注。

### 4.5 工作、checkpoint 与提交

新代码先落 `scripts/` 再执行；研究/治理成果经唯一引擎 checkpoint（先 dry-run 后 apply，payload 格式见 `.codex/skills/hott-paradox-research/templates/session-checkpoint.md`），然后本地 Git commit。本地 commit 已获用户 2026-09-10 授权；push、对外发送、模型切换始终需要新的明确授权。

### 4.6 增量交换

exchange 协议命令不变（`delta_tool.py round-init/export/verify/stage`），见 `governance/EXCHANGE_PROTOCOL.md`。ZCode 侧无任何自动发送能力。

## 5. Skills 策略：默认不注册

本项目两个 Skill（`hott-session-governance` 1.0.0、`hott-paradox-research` 1.3.4）**默认不注册为 ZCode user Skill**：

- 用户全局治理要求只启用最小核心 Skill 集，避免 metadata 膨胀降低 auto-trigger；
- 项目 Skill 的加载义务由 LOAD_SET 显式清单承担，注册成宿主 Skill 并不产生额外加载保证（description/body 限制反而可能截断/丢弃正文）；
- 复制 Skill 正文到 `~/.zcode/skills/` 会制造第二份可变副本，违反单真值源不变量。

如用户未来明确要求 slash 入口，正确做法是建**指针 Skill**：`~/.zcode/skills/hott-zcode-entry/SKILL.md` 的 body 只含一条指令——完整读取本仓库 `AGENTS.md` 与 `governance/ENTRYPOINT.md` 后按计划恢复（description ≤1024 chars，body <100KB，不含任何状态）。这是用户级主机配置，不属于本仓库内容，须用户自己在 fresh Session 前配置并确认实际加载。

## 6. Hooks / Plugin 边界

项目内 Hook 对 ZCode 无效（被忽略）。不要为治理装第三方 Plugin；本文件与原框架不依赖任何 Hook/Plugin 语义。唯一相关 Hook 是全局 RTK 输出压缩，其风险与对策见 §4.3。

## 7. Project Memory 边界

ZCode Project Memory（默认关闭、不可审计）不承载本项目任何状态。当前态唯一 owner 是仓库内 `MEMORY.md` 与 `.codex/research/hott/STATE.json`，只能经唯一引擎 checkpoint 更新。

## 8. 会话轨迹证据与隐私

ZCode 行为验收分层（L1 raw 注入 / L2 实际读取 / L3 复述 / L4 认知执行 / L5 行为接受）以 `~/.zcode/cli/rollout/model-io-sess_*.jsonl` 为证据。该文件可能包含完整上下文与凭据 metadata：**永不进入 Git、普通日志或公开回答**；报告只引用路径、模式、键名、计数和哈希。"模型复述了规则"不证明 L1/L2；同理，本文件被读出也不证明模型理解——以 RECEIVER_ACK 与实际工作为准。

## 9. 本机已验证 / 未验证

本 Session（2026-09-11）实际验证：

- `verify_package.py --package-root .` PASS（5,729 文件哈希、HEAD=tag `handoff-r040`、fsck、快照一致性、324 份原件字节重建）；验证前移出了误放在包根内的自引用 ZIP；
- `git rev-parse/status/fsck` 干净一致；
- `govern.py plan` 正常（revision 40，snapshot `446bf757…`，488 documents）；
- `govern.py install-entry --directory .zcode` 实际执行成功（见 §10）。

未验证/不适用：其他机器上的 ZCode 行为；ZCode 对 workspace `AGENTS.md` 的自动组合在本机是产品事实但每台机器需自行确认；原生证明助手（Lean/Agda/Rocq/HoTT 内核）本机未运行，历史 NOT_RUN 不因接手升级。

## 10. 项目内 ZCode 指针入口

按 portable 协议的官方机制生成（非手写）：

```bash
python3 -B scripts/handoff/govern.py install-entry --directory .zcode
```

产物 `.zcode/HOTT_ENTRYPOINT.md` 是转接文件，指向根 `AGENTS.md` 与 `governance/ENTRYPOINT.md`。**ZCode 不会自动发现项目内 `.zcode/` 目录**——该文件的作用是给按惯例查找的人/AI 一个明确指针，"写了入口不等于宿主已自动加载"。

## 11. 维护

本文件随治理演进原位修订，Git 保留历史；语义变化时递增版本号并在 Session 记录中说明。它不进入数学认知链（不在 LOAD_SET 固定清单），由 `MEMORY.md` 路由——ZCode 接手会话必读 MEMORY，因而必然发现本文件。
