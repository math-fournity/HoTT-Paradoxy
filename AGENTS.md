# 顶层综合 Repo 工作规范

本文件是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 顶层新 repo 的项目级治理入口。它补充全局 `~/.codex/AGENTS.md`，不替代全局规则；若两者冲突，遵循更具体且不扩大授权的项目事实。项目目标是把 LocalGPT、WebGPT、Gemini 的历史工作、用户原始问题、理解章节和可验证产物组织成可持续的 HoTT 悖论/现实相对研究工作区。

## 当前工作根与来源边界

- 当前工作根必须是本目录的顶层 Git repo。开始前确认 `git rev-parse --show-toplevel` 等于本目录；`AI对话录/` 和 `workspace/` 是磁盘上保留的嵌套历史 repo，已由顶层 `.gitignore` 排除，不是当前工作根。
- `核心认知.md` 当前身份必须从 `STATE.current_core` 与 manifest 动态取得；本轮为 `core-cognition-generation-4`/36 个 `KC-*`。它保留三份历史 primary 的既有 27 个用户原文单元，并允许以后把 hash-pinned 的一手用户悖论/元数学原文通过 incremental curation 纳入新 generation；转发 AI、supplemental、一般治理、附件和操作指令仍留在来源/Git，不进入 current core。每次工作开始必须从第一行连续读到 EOF；manifest 只提供哈希、定位和处置，不能代替原文。`方向追踪.md`、`全景视野.md` 也必须按固定顺序全文加载。
- `理解章节/` 是历史认知闭包及本次 transform 的主要工作成果；它是需要继续审计、修订和分层的当前知识候选，不自动凌驾于底层代码、原始来源和 Git。
- `sources/` 是来源快照和提取原件区。除非用户明确授权，不在其中改写历史来源；需要修复提取规则时改 `scripts/audit/`，重建派生文件，并保留旧 hash/差异。
- `/Volumes/D/ALL-Markdown/aistudio-docs/` 按用户要求已移走且不恢复。`sources/local-gpt/HoTT_is_GONE_COMPLETE.md` 是有 hash 的历史 AI 产物，不是已经证明覆盖原目录的事实；覆盖结论必须标为 `NOT_PROVEN`，不得将旧 validator 的缺源 PASS 当成认证。
- `private-audit/` 被忽略并按最小权限保存本机 Codex 原始 trajectory。它是只读审计输入，不进入公开提交；审计 LocalGPT 时必须使用 canonical `session_trajectory.py`，不能另写 inline trajectory parser，也不能从隐藏推理推断事实。

## 启动闭包（每个新 Session、压缩恢复、跨目录接手）

1. 先读本文件、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`，确认当前需求、当前状态、开放问题和来源边界。
2. 读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md`、`.codex/skills/SKILL_ROLES.json` 和 `.codex/research/hott/STATE.json`；先区分 lifecycle 与 evidence status。
3. 按 `核心认知.md` → `方向追踪.md` → `全景视野.md` 固定顺序全文读取三件套，记录 generation/版本、SHA-256、字节、行数和实际 EOF；读取不是哈希检查，工具输出也不证明模型理解。任一 profile/task 都不得删减或重排三件套。
4. 纯治理/审计用 `plan --profile governance`；数学研究用 `plan --profile research`。选定 stable record 后先 `query --record <ID>`，再 `plan --profile research --task <ID>` 水合对应 `理解章节/`、`HoTT/`、代码、测试、运行产物和 Git 证据。`depends_on` 只表示会传播 stale 的真实验证依赖；动机、先后、叙事、研究归属和接续关系必须使用不递归水合的 `research_parent`/`related_records`。每次 task plan 都要检查 `hydration_diagnostics`，query-first 巨型账本不得被间接提升为正文，除非本任务明确以其全文为决定性证据。
5. 需要历史轨迹时，先使用 `audit/` 的覆盖入口、`sources/SOURCE_MANIFEST.json` 和 canonical reader 的输出，再回到原始文件。不能因“没有看到”断言不存在。

任何三件套/启动必读文件缺失、发生截断、源 hash 改变、Git 状态与记录不一致或无法区分历史/当前事实时，降低结论或进入 `BLOCKED_FULL_TRIO_COGNITION`，不要开始数学研究或用摘要补洞。先移除三件套之外的非必要载荷，不能裁剪用户核心原文。

## 研究与证据纪律

本 repo 保存的是研究过程和认知交接，不预设 HoTT 必然矛盾，也不把用户的 Z 铁律直接当作已证明的元定理。研究必须区分：

- 数学对象被定义；命题被推导；算法可执行；某一次运行完成；对所有输入有效完成；现实对应可实施。这些状态不能互相冒充。
- HoTT 的内部规则、一般计算/反射界限、某个公理或现实解释的新增义务。共享机制可以有 HoTT 实例，但不能写成 HoTT 独有。
- 用户提出的方向 A（现实可完成而理论化引入额外完成困难）与方向 B（现实不可完成却把理论对象当作已获得能力）是研究方向/候选构造，不是未经核验的缺陷结论。
- AI 自述、旧文档 PASS、有限玩具模拟、文件存在、Git 提交和单次测试各自只能证明其明确范围。重要主张必须有多样审计锚点：用户原文、AI 可见回答、tool call/result、代码/文档、运行结果、Git commit 和当前 hash。

## 数学结论交付前机器证明门禁

<!-- math-proof-delivery-gate:v1
proof_source_root: HoTT/formal
proof_run_root: HoTT/verification/runs
proof_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
-->

标识：`MATH_PROOF_BEFORE_DELIVERY_V1`。本 repo 中，当前 AI 在最终答复、研究正文、方向/成果投影或当前状态中把一个数学命题作为已经成立的**数学结论**交付之前，必须完成与该精确命题相称的机器证明。数学结论包括但不限于定理、引理、等价、蕴含、不可能性、存在/不存在、全称性质、反例所否定的一般命题，以及被提升为已证事实的模型性质。

交付 Gate 按下列顺序执行：

1. 固定稳定 claim/proof ID、命题全文、量词、假设、公理、宇宙/类型论变体、依赖和禁止外推；自然语言结论必须能与形式命题逐项对照。
2. 将证明源码、项目文件和必要的锁定依赖信息保存到 `HoTT/formal/` 的合适 topic/claim 子目录；不得把聊天代码块、内存变量或 `/tmp` 中的唯一副本当作证明资产。
3. 使用能验证该命题真实语义的 proof assistant/kernel 实际运行。HoTT、univalence、cubical path、HIT、截断或高阶结构相关结论必须使用相应原生系统，或另有已机器证明的保真翻译；普通 Lean `Eq`、Python 枚举或有限测试不得冒充原生 HoTT 证明或无限/全称定理。
4. 把每次作为交付依据的运行保存到 `HoTT/verification/runs/<run-id>/`；至少包含 `RUN.json`、原始 `stdout.txt`、`stderr.txt`、`environment.txt` 和 `source-manifest.json`，记录工具/版本、命令、退出状态、源码与依赖哈希、时间、结论范围以及失败。临时构建缓存可以位于 `/tmp`，但最终证据不得只存在于 repo 外。
5. 在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 中建立或更新唯一索引行，连接 claim ID、proof ID、形式命题、源码、run receipt、证据等级和禁止外推；随后检查所有路径、哈希和实际 kernel 结果。
6. 只有 Gate 1–5 全部通过，才可使用 `MACHINE_PROVED` / `FORMAL_CHECKED_WITH_SCOPE` 或“已证明/数学结论”等交付措辞。Git 未获授权或尚未提交时，必须另标 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`，不能声称跨 Session/机器可恢复。

无法完成机器证明时，不得把该命题作为数学结论交付。可以继续保存和讨论，但必须降格为 `QUESTION`、`CONJECTURE`、`HEURISTIC`、`PAPER_ONLY`、`COUNTEREXAMPLE_CANDIDATE` 或 `SOURCE_REPORTED_NOT_REPLAYED`，并明确缺少的证明义务。外部论文或历史 AI 声称的定理可以按来源身份转述，但在本 repo 重新运行前不能冒充“当前 AI 已机器证明”。有限穷举/模型检查只有在有限域、完备枚举和命题对应关系均固定时才证明该有限命题。

本门禁不要求把每个猜想都强行形式化，也不禁止在证明前探索；它要求的是：**未证明的内容不能被交付为已经成立的数学结论。** 详细合同见 `docs/quality/数学结论机器证明与证据留存规范.md`。

## 写入、Git 与交接

- 新增或修改需求、当前状态、稳定设计、审计账本、验证结果、研究方向或研究成果投影时，按 `.codex` 的唯一 owner 路由写回；不要制造第二份当前真值。只有用户新的悖论/元数学原文或对此类工作意识的明确修正进入 core generation；一般治理裁定进入 rulings/Feature；候选/优先级/下一动作进入 `方向追踪.md` + STATE，结果/证据/失败/未知进入 `全景视野.md` + 底层 evidence owner。
- 当前人工纳入/排除与语义边界 owner 必须从 `STATE.current_core.curation` 取得（本轮为 `scripts/audit/core-cognition-curation-v4.json`）；`scripts/audit/build_core_cognition.py` 是 core/manifest/transition 的 canonical manager。默认只检查，显式 `--write` 才生成；不手工润色生成物。新增用户悖论/元数学原文时建立 hash-pinned source、新 generation 和全量迁移收据，旧代由 Git/tag 与 curation lineage 保留，不在生成物末尾手工追加。
- 每个工作单元结束前，生成 `.codex/research/hott/sessions/<session-id>/CORE_COGNITION_AUDIT.md`，逐一列出当前 generation 的全部 `KC-*`：对齐、深化、纠偏、张力、偏航或不适用，并附本轮证据定位。不能用“总体一致”替代逐编号遍历；旧审计是 archive evidence，不自动成为下轮输入。
- `.codex/tools/cognition_runtime.py` 的 `plan/read/check` 是只读加载器；checkpoint 默认 dry-run，只有用户已授予的写权限和显式 `--apply` 才能写入状态。每个 applied checkpoint 必须在同一事务中写入 `SESSION.md`、`RUNS.json` 和通过当前 generation 全量/顺序检查的 `CORE_COGNITION_AUDIT.md`，并产生 `.codex/cognition/checkpoints/<session-id>/transaction.json`、before/after 副本和 `result.json`。只有 canonical `result.json.status=CHECKPOINT_COMMITTED` 才能证明 checkpoint 已应用；Session 自写的 `POST-CHECKPOINT.json` 只能引用该收据，不能自我证明。历史缺收据只能登记缺口，禁止追溯伪造事务。
- Git 操作遵守全局基线规范：精确检查 dirty/index，保留既有嵌套 repo 与用户修改，精确 stage，提交后回读 HEAD、hash、验证结果。顶层 repo 的本次初始化与提交由用户本轮明确授权；不自动 push、发布、恢复已移走目录或删除历史。

## 任务路由

- 只做历史审计/交接：读治理 Skill 和审计脚本，不自动启动新数学研究。
- 继续 HoTT 悖论研究：先完成本文件与本地治理 Skill 的闭包，再加载业务 Skill `hott-paradox-research`；每轮只推进一个可检查构造/未知点，并记录失败和证据边界。
- 修改本地治理框架：先重新建立 closure，再按全局治理自维护 Gate 识别 C01–C10，修改 owner、schema、脚本和运行入口，执行验证并提交；项目专属变化不误改 dirty 的共享治理主库，不把 WebGPT 历史副本当作当前 host 配置。
- 发现来源快照与实际环境冲突：保留双方、记录 conflict/unknown 和适用范围；不得用新文件名或新 hash 掩盖冲突。

本项目的成功标准不是文件数量，而是未来 AI 能在有限误判风险下知道“用户要什么、过去各 AI 实际做了什么、哪些产物可复现、哪些结论未证实、当前应从哪里继续，以及本轮是否沿着全部核心认知航向工作”。
