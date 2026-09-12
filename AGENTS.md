# 顶层综合 Repo 工作规范

本文件是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 顶层新 repo 的项目级治理入口。它补充全局 `~/.codex/AGENTS.md`，不替代全局规则；若两者冲突，遵循更具体且不扩大授权的项目事实。项目目标是把 LocalGPT、WebGPT、Gemini 的历史工作、用户原始问题、理解章节和可验证产物组织成可持续的 HoTT 悖论/现实相对研究工作区。

## 当前工作根与来源边界

- 当前工作根必须是本目录的顶层 Git repo。开始前确认 `git rev-parse --show-toplevel` 等于本目录；`AI对话录/` 和 `workspace/` 是磁盘上保留的嵌套历史 repo，已由顶层 `.gitignore` 排除，不是当前工作根。
- `核心认知.md` 当前为 `core-cognition-generation-3`/27 个 `KC-*`：人工 curation 逐条审定三份用户指定 primary 的 88 条消息，只把用户本人关于悖论、HoTT 悖论挖掘、元数学和直接研究方法的精确原文范围纳入；转发 AI、supplemental、一般治理、附件和重复继续指令仍留在来源/Git，不进入当前 core。每次工作开始必须从第一行连续读到 EOF；manifest 只提供哈希、定位和处置，不能代替原文。`方向追踪.md`、`全景视野.md` 也必须按固定顺序全文加载。
- `理解章节/` 是历史认知闭包及本次 transform 的主要工作成果；它是需要继续审计、修订和分层的当前知识候选，不自动凌驾于底层代码、原始来源和 Git。
- `sources/` 是来源快照和提取原件区。除非用户明确授权，不在其中改写历史来源；需要修复提取规则时改 `scripts/audit/`，重建派生文件，并保留旧 hash/差异。
- `/Volumes/D/ALL-Markdown/aistudio-docs/` 按用户要求已移走且不恢复。`sources/local-gpt/HoTT_is_GONE_COMPLETE.md` 是有 hash 的历史 AI 产物，不是已经证明覆盖原目录的事实；覆盖结论必须标为 `NOT_PROVEN`，不得将旧 validator 的缺源 PASS 当成认证。
- `private-audit/` 被忽略并按最小权限保存本机 Codex 原始 trajectory。它是只读审计输入，不进入公开提交；审计 LocalGPT 时必须使用 canonical `session_trajectory.py`，不能另写 inline trajectory parser，也不能从隐藏推理推断事实。

## 启动闭包（每个新 Session、压缩恢复、跨目录接手）

1. 先读本文件、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`，确认当前需求、当前状态、开放问题和来源边界。
2. 读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md`、`.codex/skills/SKILL_ROLES.json` 和 `.codex/research/hott/STATE.json`；先区分 lifecycle 与 evidence status。
3. 按 `核心认知.md` → `方向追踪.md` → `全景视野.md` 固定顺序全文读取三件套，记录 generation/版本、SHA-256、字节、行数和实际 EOF；读取不是哈希检查，工具输出也不证明模型理解。任一 profile/task 都不得删减或重排三件套。
4. 纯治理/审计用 `plan --profile governance`；数学研究用 `plan --profile research`。选定 stable record 后先 `query --record <ID>`，再 `plan --profile research --task <ID>` 水合对应 `理解章节/`、`HoTT/`、代码、测试、运行产物和 Git 证据。machine manifest、raw ledger、validator、旧 Session/KC audit 默认不常驻。
5. 需要历史轨迹时，先使用 `audit/` 的覆盖入口、`sources/SOURCE_MANIFEST.json` 和 canonical reader 的输出，再回到原始文件。不能因“没有看到”断言不存在。

任何三件套/启动必读文件缺失、发生截断、源 hash 改变、Git 状态与记录不一致或无法区分历史/当前事实时，降低结论或进入 `BLOCKED_FULL_TRIO_COGNITION`，不要开始数学研究或用摘要补洞。先移除三件套之外的非必要载荷，不能裁剪用户核心原文。

## 研究与证据纪律

本 repo 保存的是研究过程和认知交接，不预设 HoTT 必然矛盾，也不把用户的 Z 铁律直接当作已证明的元定理。研究必须区分：

- 数学对象被定义；命题被推导；算法可执行；某一次运行完成；对所有输入有效完成；现实对应可实施。这些状态不能互相冒充。
- HoTT 的内部规则、一般计算/反射界限、某个公理或现实解释的新增义务。共享机制可以有 HoTT 实例，但不能写成 HoTT 独有。
- 用户提出的方向 A（现实可完成而理论化引入额外完成困难）与方向 B（现实不可完成却把理论对象当作已获得能力）是研究方向/候选构造，不是未经核验的缺陷结论。
- AI 自述、旧文档 PASS、有限玩具模拟、文件存在、Git 提交和单次测试各自只能证明其明确范围。重要主张必须有多样审计锚点：用户原文、AI 可见回答、tool call/result、代码/文档、运行结果、Git commit 和当前 hash。

## 写入、Git 与交接

- 新增或修改需求、当前状态、稳定设计、审计账本、验证结果、研究方向或研究成果投影时，按 `.codex` 的唯一 owner 路由写回；不要制造第二份当前真值。只有用户新的悖论/元数学原文或对此类工作意识的明确修正进入 core generation；一般治理裁定进入 rulings/Feature；候选/优先级/下一动作进入 `方向追踪.md` + STATE，结果/证据/失败/未知进入 `全景视野.md` + 底层 evidence owner。
- `scripts/audit/core-cognition-curation-v3.json` 是当前人工纳入/排除与语义边界 owner；`scripts/audit/build_core_cognition.py` 是 core/manifest/transition 的 canonical manager。默认只检查，显式 `--write` 才生成；不手工润色生成物。新增用户悖论/元数学原文时建立新 generation 和全量迁移收据，旧代由 Git/tag 保留，不在旧代末尾直接追加。
- 每个工作单元结束前，生成 `.codex/research/hott/sessions/<session-id>/CORE_COGNITION_AUDIT.md`，逐一列出当前 generation 的全部 `KC-*`：对齐、深化、纠偏、张力、偏航或不适用，并附本轮证据定位。不能用“总体一致”替代逐编号遍历；旧审计是 archive evidence，不自动成为下轮输入。
- `.codex/tools/cognition_runtime.py` 的 `plan/read/check` 是只读加载器；checkpoint 默认 dry-run，只有用户已授予的写权限和显式 `--apply` 才能写入状态。不要伪造模型理解认证。
- Git 操作遵守全局基线规范：精确检查 dirty/index，保留既有嵌套 repo 与用户修改，精确 stage，提交后回读 HEAD、hash、验证结果。顶层 repo 的本次初始化与提交由用户本轮明确授权；不自动 push、发布、恢复已移走目录或删除历史。

## 任务路由

- 只做历史审计/交接：读治理 Skill 和审计脚本，不自动启动新数学研究。
- 继续 HoTT 悖论研究：先完成本文件与本地治理 Skill 的闭包，再加载业务 Skill `hott-paradox-research`；每轮只推进一个可检查构造/未知点，并记录失败和证据边界。
- 修改本地治理框架：先重新建立 closure，再按全局治理自维护 Gate 识别 C01–C10，修改 owner、schema、脚本和运行入口，执行验证并提交；项目专属变化不误改 dirty 的共享治理主库，不把 WebGPT 历史副本当作当前 host 配置。
- 发现来源快照与实际环境冲突：保留双方、记录 conflict/unknown 和适用范围；不得用新文件名或新 hash 掩盖冲突。

本项目的成功标准不是文件数量，而是未来 AI 能在有限误判风险下知道“用户要什么、过去各 AI 实际做了什么、哪些产物可复现、哪些结论未证实、当前应从哪里继续，以及本轮是否沿着全部核心认知航向工作”。
