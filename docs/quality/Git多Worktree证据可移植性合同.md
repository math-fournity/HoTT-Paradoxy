# Git 多 Worktree 证据可移植性合同

> 资产：`HUMAN_EDITED / CURRENT_PROJECT_QUALITY_CONTRACT`
>
> 标识：`WORKTREE_EVIDENCE_PORTABILITY_V1`
>
> 适用：本顶层 HoTT 综合 repo 的 cognition `full_sources`、source snapshots、merge manifests、
> canonical verifiers 与 linked worktree 验收。
>
> 状态：`IMPLEMENTED_ON_CANDIDATE_BRANCH / FRESH_WORKTREE_VERIFICATION_REQUIRED`

## 1. 目的

Git worktree 为同一顶层 repo 提供独立工作文件和 index，并共享 objects/refs。它不会复制被
顶层 `.gitignore` 排除的嵌套 repo、未跟踪目录或某个 checkout 的 mutable working tree。

本合同保证：凡是当前认知加载、stable-record hydration 或 canonical verifier 作出 PASS 所
必需的输入，都能从接受后的顶层 Git commit 恢复，或由显式固定的外部 locator 读取。主
checkout 恰好存在某个 ignored 文件，不能成为 current PASS 的隐含前提。

## 2. 证据身份分类

| 身份 | 是否可作 current 决定性输入 | 要求 |
|---|---:|---|
| 顶层 tracked file/blob | 是 | 路径、commit 与内容可由顶层 Git 恢复 |
| 顶层 tracked byte snapshot | 是 | 保留原路径/repo/状态 provenance；snapshot bytes 不原位改写 |
| exact external Git blob | 条件允许 | locator 同时固定 repo identity、commit OID、blob path、bytes、SHA-256；读取失败时 fail closed |
| ignored nested repo working file | 否 | 只能作导入来源或现场观察，不能直接进入 current `full_sources` |
| ignored/untracked local copy | 否 | 找到 tracked 同字节副本时改路由；否则先导入或建立 locator |
| 历史文档中的原路径文字 | 允许保留为 provenance | 不得让 loader/verifier把该文字当作当前可读路径 |

本项目当前采用 tracked file/snapshot 路线，没有引入 external-locator schema。以后确有多个
外部 evidence repo 的长期需要时，再按 schema、CRUD、hash、故障与兼容要求单独设计。

## 3. Current 输入不变量

### 3.1 Stable records

`STATE.json.records[*].full_sources`、`resolution.evidence` 与 `source_hashes` 中由 task plan 实际
展开的 repo-relative 路径必须满足：

1. 路径指向顶层 Git tracked file；
2. 文件在当前 HEAD 或 checkpoint payload 的预期新 index 中存在；
3. 若同一历史来源另有 ignored 原路径，只在 provenance/receipt 中保留，不作为第二个必读
   current path；
4. 同字节替代必须实际比较 bytes/SHA-256，不能根据文件名推定；
5. 路径迁移需更新所有 current consumers，历史 checkpoint 和旧收据保持不变。

### 3.2 Canonical verifiers

verifier 的成功不能依赖运行者预先手工复制 ignored 目录。verifier 必须从自身
`--project-root` 解析 current 路径，并在适用时检查：

- manifest 声明的 source directory 存在；
- source file 和 manifest 都在 `git ls-files --cached` 中；
- entry 路径与 manifest owner 路径一致；
- bytes/SHA-256、文件集合、计数与 tree digest 一致；
- 缺目录、未跟踪、hash 漂移和路径身份错配具有不同错误；
- 失败不得静默回退到 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 或其它 checkout。

### 3.3 Source manifests

`sources/SOURCE_MANIFEST.json` 是 2026-09-12 生成时的 provenance 快照。它可以记录源 repo
的原绝对位置、当时 dirty 状态和以后不一定本地存在的历史树；这些字段是历史身份，不代表
每个 worktree 都应拥有全部外部语料。

current task 若需要其中某个文件，必须另走 tracked snapshot/file 或 exact locator。本轮
`sources/understanding-transform/AI对话录` 的 42 文件 tree 已按 manifest 的
`b20abd5e…` digest 纳入顶层 Git；完整 1,209 文件 `ALL-Markdown-root` 历史树仍是外部快照，
current A-AISTUDIO hydration 只读取已有 tracked 同字节 artifact。

## 4. 本轮三项迁移

### 4.1 WebGPT workspace records

`STATE.json` 中 8 次、去重后 6 个 `workspace/**` full-source 引用改指
`sources/webgpt/workspace-snapshot/**`。迁移前逐文件验证旧主 checkout bytes 与 tracked
snapshot bytes 相同；映射由 `audit/worktree-portability-source-import-20260913.json` 固定。

### 4.2 Understanding historical source

旧 `AI对话录/理解章节` 是 ignored nested repo working tree。其 24 个文件已经包含在
`sources/SOURCE_MANIFEST.json` 固定的 42 文件 transform snapshot 中。本轮将该 transform
snapshot 的原字节显式加入顶层 Git；merge manifest 的 historical directory 改为：

```text
sources/understanding-transform/AI对话录/理解章节
```

两个与 nested `HEAD` 不同的 working files 继续保留 manifest 已固定的 working bytes；没有
回退、润色或改写。新 merge manifest 使用 repo-relative path，并把 source-manifest hash、
42 文件 tree hash、原 nested repo HEAD 和 snapshot scope 写入 provenance。

### 4.3 LocalGPT artifact

旧 full source：

```text
sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md
```

与 tracked 的 `sources/local-gpt/HoTT_is_GONE_COMPLETE.md` 在迁移时均为 32,127 bytes，
SHA-256 均为 `ec2fe644c608637ec9465342f4948140494662706b5861bfea5dff712a0980fa`。
current record 删除旧 ignored path，保留 tracked path；完整 ALL-Markdown 历史树身份不因此
改变，coverage 仍为 `NOT_PROVEN`。

## 5. Machine-managed source snapshot

`scripts/audit/import_worktree_portability_sources.py` 是本轮 import/verification manager：

- `import` 只从获准 source checkout 读取；在 destination/receipt 已存在时拒绝覆盖；
- 先对照既有 `SOURCE_MANIFEST` 的 42 文件行与 tree digest，再逐字节复制；
- 对 workspace 6 文件与 LocalGPT artifact 只验证已有 tracked 等价路径，不重复复制；
- receipt 记录来源 checkout/head/dirty、目标 base、manifest hash、所有文件 hash 与 record 映射；
- `verify --require-tracked` 不读取原 nested repos，能在 fresh linked worktree 独立运行。

历史 source 中原有 trailing whitespace 或文件结尾形态按字节保留。普通
`git diff --check` 对该冻结 snapshot 可能报告旧格式；验收应对 snapshot 使用 manifest/hash
校验，对本轮创作的代码、合同和 current owners 单独执行 `git diff --check`。不得为了通过
格式检查而改写历史 bytes。

## 6. Fresh-worktree 验收

最终验证必须从候选 commit 创建新的 detached linked worktree；不得从主 checkout rsync、
symlink 或复制 ignored source。至少执行：

1. import manager `verify --require-tracked`；
2. `A-AISTUDIO-COVERAGE-001`、`A-C5-PARADOX-DISTANCE-001`、
   `A-HOTT-RESEARCH-DIRECTION-001`、`A-WEBGPT-R041-PAPER-001` 与
   `A-HOTT-SELF-VALIDATION-ECONOMY-001` 的 research task plans；
3. governance shards、three-way cognition、understanding merge、fresh three-way、C11 ledger
   retrodiction、proof version closure 六类 canonical verifier；
4. source snapshot 文件集合/hash/tree digest；
5. `git status`，确认测试没有依赖或生成 ignored evidence island。

验收 worktree 在结束后才能删除；删除前保存 exact candidate OID、命令、退出码与输出摘要。

## 7. 负向控制

在隔离的临时 worktree 中至少验证：

- 修改一个 imported understanding byte → source/import/understanding hash 检查失败；
- 从 index 移除一个 imported file，但保留工作文件 → `NESTED_SOURCE_NOT_TRACKED` 或 import
  tracked check 失败；
- 把一个 stable-record path 改回 `workspace/**` → fresh task hydration 以
  `MISSING_OR_UNREADABLE` 失败；
- 修改 manifest entry path 指向同 hash 的别处 → path identity check 失败；
- 缺原 ignored repos 但 tracked inputs 完整 → 全部正向验收仍通过。

负向控制只改临时 worktree，不能污染候选 branch 或主 checkout。

## 8. 集成与完成

本候选仍遵循双轨 worktree 合同：candidate branch 可以包含 current-owner checkpoint，但在
用户指定 integrator 并审查 exact OID 前不成为 `main` current truth。集成时应：

1. 冻结 candidate OID 和 expected target HEAD；
2. 检查 target 自 base 后的 STATE revision、source snapshot 与 verifier 变化；
3. 只分配一次 canonical revision；若 target 已占用本候选 revision，重新生成 checkpoint，
   不追溯篡改候选收据；
4. 在 target 的 fresh linked worktree 重跑本合同 §6；
5. 保存 accepted/deferred/rejected 与 rollback 入口；
6. 未经授权不 push、不移动共享 tag。

完成判据是：当前决定性输入全部为 tracked/pinned，五个 task hydration 和六类 verifier 在无
ignored islands 的 fresh worktree 通过，正负控制成立，checkpoint/Git 收据可恢复。主 checkout
原位 PASS 或文件存在本身不够。
