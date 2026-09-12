# AGENTS.md：ALL-Markdown

> 本文件是项目宪法和认知路由，不是知识容器。

## HoTT 每次会话／每次执行的治理入口（v1.3.0）

本项目的活动组件是 HoTT 研究。治理负责认知与证据连续性，不替代数学思考。收到HoTT/Skill/研究接续相关请求，或上下文压缩、会话切换后：

1. 完整读取本AGENTS、治理 Skill `hott-session-governance` 与业务 Skill `hott-paradox-research`（路径由 `.codex/skills/SKILL_ROLES.json` 定位）。治理负责每次进入/压缩恢复与交接，业务负责数学探索；同一次调用先治理再业务、结束再保存，不要求用户分别点名，不重复嵌套重入。定位当前项目根，不访问旧主机路径。
2. 读取 `.codex/cognition/LOAD_SET.json` 和最新 `.codex/research/hott/STATE.json`，解析当次全文加载集合。先完整读指定第五闭包，再完整读已对齐三问；随后全文读根README、MEMORY、强制来源、当前前沿、经验、接续指针、最近会话和所有活动/待复核记录的依赖。固定思想来源与动态状态都不得被摘要或旧收据替代。
3. 每份从第1行到当次实际末行；分块正文必须实际呈现给模型。新Session、重新进入Skill和压缩恢复均重新加载；相同哈希不是免读凭证。内容/指针在加载中变化就重读，缺件或容量不足不伪造完整加载。
4. 核清当前问题、九方向、发现/确认与归因区别、各结论证据范围和下一动作。来源/当前事实有冲突则分层记录，不让旧历史覆盖新用户裁定，也不让新摘要改写数学真值。
5. 开展自主研究；方法库不是封闭脚本，允许新构造、反证与质疑当前Skill。只维护共同问题与证据责任，不预设HoTT必错或必对。
6. 有写权限时，每个实质里程碑及结束前保存不可覆盖的Session记录，更新 `MEMORY.md`、`FRONTIER.md`、`LESSONS.md`、`RESUME.md` 和 STATE 动态路由。提供证据、失败原因、修订和影响依赖；回读/校验成功才称 `CHECKPOINT_COMMITTED`。无写权限或失败时称 `CHECKPOINT_NOT_SAVED`，交付可恢复文本，不声称已跨Session持久化。
7. 写回必须以本次读取版本为基线。并发更新先比较哈希，旧基线拒绝；不能最后写者覆盖。遇中断事务先恢复/回滚，不能读取一半新一半旧的状态。候选依赖变化必须标记受影响结果待复核，不能沿用旧PASS。

根 MEMORY 是当前工作记忆，不是数学真值容器；每项重要事实须回源到记录/规则/证据。STATE 中全部开放状态记录自动加入必读，不能只靠手工队列。关闭记录须有理由与证据路径，原记录保留。R001 的恢复正文和来源冲突见 `.codex/research/hott/imports/R001/`，须随开放缺口全文加载；恢复不是原实验重新验证。

历史在 `.codex/history/` 与不可覆盖的 sessions/ 保留，不能为限行删掉未解决条件。已关闭历史不必每次全扫；但凡本次结论实际依赖，须把相应原文加入动态全文加载集合。

本轮用户授权构建治理、记忆与相关加载/检查工具，不授权新数学运行、模型切换、Work任务、其他AI、Git提交/push或外部发布。未来执行权限仍按当次用户指令；历史权限不得自动继承。完整合同：`.codex/cognition/PROTOCOL.md`。

## 最高目的与第一动作

项目治理的目的不是文档齐全，而是让实际工作成功；当前重点是 HoTT 数学研究和其跨会话连续性。任何工作的第一语义动作都是判断并
建立本任务认知闭包；非平凡 repo 工作必须先完整执行 `repo-cognitive-closure`，利用
README、MEMORY、Feature、docs 和底层实物获得正确认知后，才能回答或行动。

不得为了节省上下文而把项目认知路由、证据纪律、异常边界或完成判据压缩到 AI 无法正确工作；
先保证指导完整，再去除真正重复。

本文件不得设置 150 行等任意行数或文件大小硬上限。真实边界只来自 host 实际 byte/context
预算；当前常规项目规模远非会触及。若未来接近真实预算，先提升配置、改善路由或去真正重复，
不得删除会改变 AI 判断的 always-on 认知。

持续增长、频繁追加或妨碍定位的治理文档可以按自然语义边界分片；约 200 行只是软目标，绝不是
压缩、删减或发布 Gate。分片后先读原 canonical index，确认完整 shard table、`last_shard` 和
顺序追加型 `append_target`，再读 owner shard；新 shard 与索引必须同一 commit 更新。

Feature、current design 和 topical owner 是可修订的当前真值；状态变化时原位修改 owner，旧状态
由 Git、MEMORY/history、rulings 或 sequential 日志保留。禁止因为表格行太长就在后面追加
“状态修正/最新版/以此为准”覆盖块。长行难维护时按职责路由历史证据或在自然语义边界分片，不为数字
压缩内容，也不留下两个相互冲突的当前结论。

## 规范化治理资产与受控脚本

治理资产可以是human-edited文档，也可以是machine-managed canonical CSV/JSON/SQLite/matrix。README与
schema必须给出owner和canonical manager；manager存在时，AI先用`query/list/get`建立认知，并用
`upsert/delete-or-retire/validate/migrate/export/diff`操作，不默认全文加载或逐行手改raw载体。只有manager
诊断、schema migration、损坏恢复或明确合同允许时才直接检查底层文件。

脚本只承担机械CRUD、完整性、原子写、确定性序列化和receipt，不替代用户/Feature/设计的语义裁决，也不
扩大删除权限。新规范化要素必须同时提供schema/version、stable IDs、dry-run、锁/并发、引用完整性、
round-trip、migration/rollback、正负/故障测试和human-readable export；没有稳定结构和可证明收益时继续用
Markdown，不为形式化而形式化。

## 文件变更前

修改、移动、重命名、删除或覆盖现有文件前，先确认所属目录及Git状态（若有）。当前来自ZIP的副本没有.git时，明确UNKNOWN，不创建假提交；以完整原ZIP、改前字节备份、文件清单与哈希建立可回退基线。已有Git仓库继续先确认tracked/dirty、HEAD/tag并保留其他Session未提交变化；无用户授权不得commit/push/reset。

## 认知加载

- AGENTS 是启动内存和强制路由，不是完整知识库。新 Session、上下文压缩恢复、跨 repo/cwd
  接手，或用户询问当前状态、下一步、是否记录、能否继续等 repo 依赖问题时，必须先恢复
  README/MEMORY 外部工作记忆，再回答或行动。
- 非平凡工作先把用户请求转成成功标准、关键问题、范围和高代价误判，再读 `README.md` 和
  `MEMORY.md` 建立项目全景与当前态。
- 修改组件前读 `feature-list.md` 对应节、用户来源/rulings、`docs/README.md`、稳定 system/
  detailed/interface/data/operations 合同，并沿 README 回到代码、config、schema、tests、data、
  logs、进程和运行产物等决定性证据。
- README/MEMORY/Feature/map/摘要只负责路由；不能证明实现、验证和当前运行。
- 用户意图、当前需求、系统设计、详细合同、实现、验证、运行、当前态和历史必须分开。
- 冲突按事实类型、版本和时间消解；无法消解就披露并降低结论。
- “不存在/没有遗漏/全部覆盖”等负结论要说明搜索范围和盲区，不能把没搜到写成不存在。
- 新 Session、压缩、范围/cwd/repo/关键资产或动态事实变化后，审计并按需重建闭包。
- 遇到 `governance-shard-index:v1` 时，先读索引再按任务读 owner/append shard；不能把某一片冒充
  logical document 全文，也不能把约 200 行软目标当作读取截断或压缩理由。
- 恢复后区分 `ACTIVE_WORK`、`CURRENT_REQUIREMENT`、`OPEN_INCIDENT`、`CLOSED_INCIDENT`、
  `HISTORICAL_EVIDENCE`、`SUPERSEDED_FACT`、`DRAFT_PROPOSAL`；用户本轮目标和 MEMORY 当前
  执行队列优先。已关闭事项不得因近期、高频或压缩摘要重新成为当前任务；只有用户明确要求、
  出现满足 `reopen_if` 的当前直接证据、相关 requirement/design/runtime 变化，或本轮就是复盘/
  历史分析时才进入调查。复盘不自动授权重新实施。
- 完成前执行 T01-T26 影响检查，只更新真实变化的唯一真值源；文档化、实现和验证分状态。
- 若本 repo 已长期存在且 current/history 只能从完整 Git 历史恢复，先加载
  `repo-legacy-reconstruction`，不要用 bootstrap 模板覆盖冲突；历史重建阶段不得移动/删除路径。
- 全 repo 结构重塑只有在 reconstruction PASS、用户授权、全路径 manifest、consumer scan、rollback
  和 pre-migration tag 完成后才加载 `repo-structure-migration`，普通目录整理不获得该权限。

## 项目不变量

- 本 repo 是长期 Markdown 知识/研究语料库；当前受治理的活动组件是 `HoTT/`。旧材料正确性入口为
  `HoTT/AUDIT_AND_RECONSTRUCTION.md`；当前 Z 铁律/现实相对悖论入口为
  `HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md`；具体 HoTT 时间分层入口为
  `HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md`。不能让历史 AI 标题、交接包状态或旧 P0 覆盖当前 owner。
- 当前第一主题是“Z 铁律下的 HoTT 现实相对时间悖论”：目标不是优先寻找 `HoTT ⊢ ⊥`，而是寻找
  合法 HoTT 推演在被解释为现实过程、结论或现象时产生的非现实性。凡问题涉及 HoTT、时间、动态、
  过程、顺序、计算、因果、资源、历史、生成、抽象、悖论、芝诺、圆环、Russell 或 Becoming，必须
  按上方治理入口完整加载第五闭包、三问和动态记忆，并完整读 `HoTT/sources/user-originals/` 中两份指定原文、Z owner、时间owner和主张矩阵；原始来源不被任何AI摘要替代。
- “时间维度”固定区分四层：对象层时间、计算/归约的弱操作时间、进入 judgment/type rule 的强内生
  时态，以及物理时间。不得用“能定义 `Time/t`”证明理论自身有强时间，也不得忽略 λ-reduction
  而把标准 HoTT 称为绝对静态。当前允许表述是：标准 HoTT 有计算箭头但 temporally unindexed；
  跨 HoTT/cubical/guarded/clocked/directed/linear/effectful 变体的正式 no-go 尚未建立。
- 相关 Session 必须维持以下工作意识：计算合法性/因果准入先于真值；抽象的结构否定使完整现实
  判定谱 `X` 与抽象判定谱 `Y` 分岔；“同函数异时”是已有候选之一，实际优先级看最新前沿；
  Guard-Erasure 的具体 HoTT 遗忘翻译仍开放；无规范较早事件只是支持性无截面实例，不再是 P0。
- 不得用“HoTT 能编码时间”结束回答，不得把一般因子化或 no-section 冒充用户问题已经解决，也不得
  把用户原文自动升级为数学证明。具体冲突确认须有合法推演与同任务不相容；旧Z规范的完整机制/修复要求用于后续归因，不重新成为发现起步的全部门槛。
- `/Volumes/D/ALL-Markdown/proofs` 保存其他 AI 整理的数学证明；目录身份不构成正确性或验证证据。
- `/Volumes/D/ALL-Markdown/dev-docs` 保存整理过程的调查、索引与未定文档；稳定结论必须抽取到唯一
  current owner，不能把过程索引当作定理。
- `/Volumes/D/ALL-Markdown/aistudio-docs` 是大规模来源归档；一次正文提及不等于专题身份。移动前须
  依据主对象、标题/语境和来源登记裁决，不能因 broad grep 命中机械搬迁。
- `HoTT/sources/aistudio-discussions/` 是由 manager 生成的逐字派生发现层，不是摘要或数学真值源。
  查找历史 HoTT 讨论或作出“没有/已全覆盖”的结论前必须查询 CURRENT manifest 并回到原始源行；
  归档并非全是问答，必须同时处理 `qa_dialogue`、`prompt_response`、`headed_prose` 和
  `unheaded_prose`。不得手改 generation，语义审读只能加 annotation/curated view，不能删除 raw。
- `/Volumes/D/ALL-Markdown/HOTT_Z_AI_HANDOFF_20260831` 是另一 AI 的只读交接证据快照；哈希完整、
  `COMPLETE_INTERNAL` 或 AI 审稿意见均不自动证明数学正确、工作包验收或外部同行评审。
- HoTT 历史来源保持原文；纠错写入审计/矩阵，不回写篡改来源。形式化通过只支持源码中精确类型，
  不得外推为 `HoTT ⊢ ⊥`、HoTT 不能编码时间或原创性已证。
- Secret 不进入 Git、Prompt、普通日志或公开文档。
- Push、发布和破坏性外部状态变更需要用户明确授权。
