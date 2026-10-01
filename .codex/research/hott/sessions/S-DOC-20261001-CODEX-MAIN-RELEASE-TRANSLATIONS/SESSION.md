# S-DOC-20261001-CODEX-MAIN-RELEASE-TRANSLATIONS

为 `main` 的下一次受控生成补齐多语发布源：核查现有 Opus 翻译，新增 `CLAIMS` 的俄、德、法、英文模板。此会话只翻译和校验已存在的发布说明与证据陈述；不产生或修改数学命题、证明、运行收据、STATE、方向或全景投影。

- host: Codex Desktop（本机）
- model: GPT-5（当前 Codex 宿主提供；未从文件或模型自述推断额外版本）
- tier: T1-standard
- role: MECHANICAL_CONTEXT
- authorization: 研究发起人于 2026-10-01 要求核对 Opus 的 repo 文档翻译进度，并补齐 README、社区稿与 `CLAIMS.md` 范围中尚缺的译文；顺序固定为中文、俄文、德文、法文、英文，内容主要服务 `main`。
- branch and delivery boundary: 当前工作根为 `dev`（HEAD `5419e8c5da43`）；`main` 是由 `dev` 生成且不得直接编辑的结果分支。本单元不提交、不生成分支引用、不 push。

## load_receipt

T1 启动核已消费：根 `AGENTS.md`、`README.md` 索引与任务相关的 001 分片、`MEMORY.md` 索引与 001/002 分片、`feature-list.md`、`rulings.md`、`.codex/AGENTS.md`、`PROTOCOL.md`、`LOAD_SET.json`、`TASK_ROUTING.md`、角色表、local-session-governance Skill、最高指示；STATE 只消费 hot 字段。全局 `repo-cognitive-closure`、`repo-requirements-decisions`、`repo-cognition-governance`、`repo-detailed-design` 和 `repo-verification-risk` 的当前工作法也已加载。

本单元没有在用户的 HoTT 原意、数学哲学、现实对应或数学结论上作出判断，因而没有触及任何核心认知条目：当前 generation-10 的 54/54 KC 均为 `NOT_TOUCHED`。最高指示按 `MECHANICAL_CONTEXT` 消费：本单元保护的是面向外部读者的证据边界；最危险的偏差是把译文或文件存在误写成新数学结论、已发布 main 或已验证端到端发布。

## 发现、边界与写回

1. `HEAD` 已版本化五语 README 的发布模板；现有语言顺序与用户要求一致。
2. 工作树中已有社区审计入口和 01–03 的 16 个俄、德、法、英文译本；每个 `translation:v1` header 的 source/hash/language 和语言栏都与中文源文件一致，但它们仍是未提交文件。
3. `scripts/release/build_main_release.py` 与 `main-release-spec.json` 是 Opus 留下的 dirty 实现，增加了社区稿与 `CLAIMS` 译文的发布合同；本会话不改写它们。
4. 原来缺失的是 `scripts/release/main-CLAIMS-RU.md`、`-DE.md`、`-FR.md`、`-EN.md`。本会话新增四份模板，全部记录 `CLAIMS.md` 第 1–3 节当前 body SHA-256 `51922184847767cbfa2f6f69cdcde9d3f9ff07e43631d367e6bb6eb251c0e0aa`，使用同一语言顺序、中文权威声明和 `RUN_TABLE` 生成占位符。
5. `OWNER_UPDATE` 只落在这四个发布模板与本 T1 session 记录。语言顺序的实现 owner 是既有 `scripts/release/main-release-spec.json`；不为这个发布配置另造 Feature、rulings 或第二份当前真值。

## 验证

- `python3 -m py_compile scripts/release/build_main_release.py`：PASS。
- 读取 `python3 -B scripts/release/build_main_release.py --source HEAD --claims-body-sha`：输出与四份 header 的 body SHA 一致。
- 自定义只读静态校验：四个 `CLAIMS` header、五语语言栏、允许的四个生成占位符、无尾随空白；社区稿 16 个 header/hash/bar；四份模板对中文来源的 backticked formal token、package ID、claim ID、run ID 覆盖：PASS。
- `git diff --check`：PASS。

端到端 `build_main_release.py --source <commit> --out <dir>` 尚未运行：该脚本有意只读取提交中的 source，当前改动与既有 Opus 文件都尚未被用户授权提交。提交后应在包含全部翻译源和发布脚本变更的精确 `dev` commit 上运行该构建，再独立审阅输出和 `RELEASE-MANIFEST.json`；该动作不等同于授权直接修改或 push `main`。
