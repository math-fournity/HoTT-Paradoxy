# Feature / 当前需求状态

本文件是当前 feature 状态 owner；历史来源中的“已完成”不自动改变这里的状态。

| ID | 需求 | 当前状态 | 证据/下一步 |
|---|---|---|---|
| F-001 | 顶层目录成为综合 Git repo，保留原嵌套来源边界 | IMPLEMENTED | `git log`、`.gitignore`、`audit/governance-impact.md` |
| F-002 | 保存 LocalGPT、WebGPT、Gemini 来源快照和 provenance | IMPLEMENTED_WITH_SCOPE | `sources/SOURCE_MANIFEST.json`；私有 trajectory 仅在 ignored `private-audit/` |
| F-003 | 三份用户指定 primary 中的用户直接悖论/元数学原文，按人工语义单元和 UTC 连续编号组成 `核心认知.md`；转发 AI、supplemental、一般治理、附件和无新增认识的重复只留 disposition/history | VERIFIED_WITH_SCOPE_VERSION_CLOSED | SRC：`rulings.md` §2、§9、§12；DES：`audit/核心认知generation-3与加载治理v3实施证据-20260912.md`；IMP：curation+builder+core/manifest/913-row transition；VER：core tests 7/7、verifier PASS；EVD：同一实施证据；generation-3=27 KC/88 messages，模型理解/数学未认证 |
| F-004 | 记录所有可见 AI response、tool event、work product、claim-evidence | VERIFIED_WITH_SCOPE | 四类主 ledger + WebGPT/Gemini 专项 ledger + `audit/cross-source-reconciliation.json`；句级语义裁决仍明确待人工复核 |
| F-005 | 顶层 `.codex` 在每个新 Session/压缩恢复全文加载 core→direction→panorama；governance/research profile 分层，stable record 显式水合证据；STATE lifecycle/evidence 分离；结束逐 KC 回评和原子 checkpoint | MECHANICALLY_VERIFIED_VERSION_CLOSED | SRC：`rulings.md` §5、§8–§13；DES/EVD：generation-3/v3实施证据；IMP：LOAD_SET v3、runtime 3.0、双 Skill/PROTOCOL、STATE v2；VER：runtime 27/27、three-way 4/4+manifest themes、S013–S018 checkpoints；默认 15/20 docs，fresh model behavior NOT_RUN |
| F-006 | 以审计结果更新 `理解章节/`，达到交接/博士论文级而非摘要级 | IN_PROGRESS_WITH_FILE_LEVEL_MERGE | 已新增 C0、历史边界层、逐文件 merge manifest 和 canonical 顶层选择；2,396 条 claim 的句级语义/数学 owner 修订仍待下一波 |
| F-007 | 不恢复用户移走的 `aistudio-docs`，明确替代材料覆盖是否可证明 | VERIFIED_BOUNDARY | 缺源 validator 失败；coverage 仍 `NOT_PROVEN` |
| F-008 | 未来每个工作单元按当前 generation 的全部核心认知逐编号评估方向；旧回评保留但不自动常驻 | MECHANICALLY_VERIFIED_VERSION_CLOSED | SRC：`rulings.md` §5；DES/IMP：PROTOCOL、本地治理 Skill、audit scaffold/verifier；VER：S013 27/27（1 deepened/4 aligned/22 untouched）、S014–S018 各 27/27 untouched，均通过 denominator/placeholder/evidence 检查；EVD：六个 Session |
| F-009 | 以 `方向追踪.md` 和 `全景视野.md` 统筹两个 GPT 的历史方向/成果，并与 `核心认知.md` 交叉决定更新归属；不把 AI 结果写入用户原文 | EXHAUSTIVE_REGISTER_WITH_SCOPED_SEMANTIC_REVIEW | `方向追踪.md`、`全景视野.md`、`audit/cross-source-reconciliation.json`、审计/方案；22,226 行均可发现和回源，2,396 条 claim 的直接语义仍开放 |
| F-010 | 永久保留三件套当前逻辑全文作为压缩恢复不可替代输入；三件套之外的机器索引、历史收据和任务证据分层查询/按需水合；输入保真与模型行为是不可互替的双轨验收 | INPUT_FIDELITY_MECHANICALLY_VERIFIED_MODEL_BEHAVIOR_NOT_RUN_VERSION_CLOSED | SRC：`rulings.md` §9–§13；DES：跨压缩升级方案 v3+实施证据；IMP：LOAD_SET/runtime/STATE v2；VER：revision 18 fresh Python full-trio EOF/hash、profile/task与四类负向 PASS，历史文档新路径可显式水合，fresh model behavior 明确 NOT_RUN；EVD：fresh receipt+实施证据 |
