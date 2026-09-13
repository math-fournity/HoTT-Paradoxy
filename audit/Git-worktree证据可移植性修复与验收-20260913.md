# Git worktree 证据可移植性修复与验收

> 日期：2026-09-13
>
> candidate：`802e4f890f07adeb50d32f7d8a3e1866d8d8d597`
>
> branch：`codex/semantic-overview`
>
> 判词：`VERIFIED_WITH_SCOPE_ON_FRESH_LINKED_WORKTREE / NOT_INTEGRATED`

## 1. 已修复的问题

revision 129 在主 checkout 的六类 canonical verifier 全部通过，但 linked worktree 只有 4/6：
understanding merge 依赖被忽略的 nested `AI对话录/理解章节`，fresh hydration 依赖被忽略的
`ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md`；另有 8 次 stable-record `workspace/**`
full-source 引用会使相关 task plans 失败。

本轮把三类决定性输入改为顶层 Git 可恢复路径：

1. 将 `sources/SOURCE_MANIFEST.json` 已固定的 42-file
   `sources/understanding-transform/AI对话录` transform snapshot 逐字节纳入顶层 Git；
2. understanding historical side 改读其中的 24-file `理解章节`，manifest 升 v2，entry path
   改为 repo-relative，并新增 tracked/path/source-tree 检查；
3. 8 个 `workspace/**` record refs（6 个 unique files）改到已有、逐字节相同的
   `sources/webgpt/workspace-snapshot/**`；
4. `A-AISTUDIO-COVERAGE-001` 删除 ignored duplicate path，保留已有 tracked、32,127 bytes、
   SHA-256 `ec2fe644…` 的同字节 artifact；coverage 仍为 `NOT_PROVEN`；
5. AGENTS、local Skill 3.7、PROTOCOL v2.7、LOAD_SET 4.1、F-016、ruling §22、README/docs 与
   current research locators 已同步；
6. revision 130 canonical checkpoint 已应用并提交，状态先保持
   `IMPLEMENTED_LOCAL_PENDING_FRESH_WORKTREE`。

source commit 为 `80da06ead06f38bc87ec8ebe7c82f72865401308`，静态路由/合同 commit 为
`d58dbfdbb4dd1f71c192801f57f49cfacc288933`，revision 130 commit 为
`802e4f890f07adeb50d32f7d8a3e1866d8d8d597`。

## 2. Fresh worktree 前置条件

从 revision 130 exact commit 创建：

```text
/Volumes/D/HoTT-portability-verify-802e4f8
HEAD 802e4f890f07adeb50d32f7d8a3e1866d8d8d597
DETACHED
```

没有 rsync、symlink 或手工复制 source。开始时机械确认：

- 顶层 `workspace/` 不存在；
- 顶层 `AI对话录/` 不存在；
- ignored old LocalGPT artifact path 不存在；
- tracked transform snapshot、tracked workspace snapshot 和 tracked LocalGPT artifact 均存在；
- Git status clean。

因此本次 PASS 不可能继续依赖原主 checkout 的三个 ignored islands。

## 3. 正向验收

| 检查 | 结果 |
|---|---|
| import manager | `PASS`；42 copied files、6 workspace mappings、8 record refs 全部 tracked/hash 一致 |
| governance shards | `PASS`；282 indexes、11 canonical、0 notices |
| three-way cognition | `PASS`；revision 130、36 KC、31 directions、111 outcomes |
| understanding merge | `PASS`；36/24、15 identical、9 different、historical source tracked |
| fresh three-way v3 | `PASS_WITH_SCOPE`；41 governance docs、46 research docs、5 portability tasks |
| C11 retrodiction | `PASS`；18 packages、17 device available、1 deliberate absent/no-consumer |
| proof version closure | `PASS_WITH_SCOPE`；17/90 frozen、11/39 later、85 source rows、50 index rows、6 historical gaps |

五个 explicit task hydration 的 document/hydrated-record 数分别为：

| record | documents | hydrated records | untracked documents |
|---|---:|---:|---:|
| `A-AISTUDIO-COVERAGE-001` | 53 | 2 | 0 |
| `A-C5-PARADOX-DISTANCE-001` | 78 | 1 | 0 |
| `A-HOTT-RESEARCH-DIRECTION-001` | 228 | 10 | 0 |
| `A-WEBGPT-R041-PAPER-001` | 204 | 3 | 0 |
| `A-HOTT-SELF-VALIDATION-ECONOMY-001` | 244 | 13 | 0 |

## 4. 负向控制

### N1：修改 imported byte

给 historical A0 追加一个 LF 后：

- import manager：`BYTE_COUNT_MISMATCH:IMPORTED_FILE`；
- understanding：`SOURCE_SNAPSHOT_FILE_ROWS_MISMATCH`、
  `SOURCE_SNAPSHOT_TREE_HASH_MISMATCH`、`NESTED_HASH_MISMATCH:A0-总目标.md`。

### N2：工作文件存在但从 index 移除

仅对临时 worktree 执行 `git rm --cached` 移除 historical A1：

- import manager：`IMPORTED_PATHS_NOT_TRACKED`；
- understanding：`NESTED_SOURCE_NOT_TRACKED:A1-Z铁律.md`。

这证明“文件碰巧存在”不能替代 tracked identity。

### N3：stable record 改回 ignored path

把 A-C5 的 PLAN route 改回 `workspace/**`，并同步临时 HEAD state hash 以越过一般 dirty-state
检查后，fresh task hydration 仍以
`MISSING_OR_UNREADABLE: workspace/.codex/research/hott/candidates/RP-B01/PLAN.md` 失败，
没有回退到主 checkout。

### N4：manifest 路径身份漂移

把 A0 entry 的 nested path 改指 A1、保持其它字段不变，understanding verifier 以
`NESTED_PATH_IDENTITY_MISMATCH:A0-总目标.md` 拒绝。

四次改写后均从 detached `HEAD` 精确恢复。最终 import、understanding、fresh 再次通过，Git
status clean；验证 worktree 随后由 `git worktree remove` 删除。

## 5. C01–C10 影响结果

| ID | 结果 |
|---|---|
| C01 | `UPDATE`：ruling §22、F-016、验收语义 |
| C02 | `UPDATE_PROJECT_ONLY`：项目 quality contract；共享治理 repo 因并行 dirty 工作未混入本提交 |
| C03 | `UPDATE`：PROTOCOL/Skill/LOAD_SET/import+merge managers |
| C04 | `UPDATE`：project AGENTS 启动与失败边界 |
| C05 | `UPDATE`：README/docs/source maps/current locators |
| C06 | `UPDATE`：tracked/path/tree checks、five-task fresh、四个负向控制 |
| C07 | `NO_CHANGE`：config/Rules/Hooks/plugins/secret/权限不变 |
| C08 | `NOT_APPLICABLE`：无产品 host adapter 变化 |
| C09 | `UPDATE_CANDIDATE`：三个 candidate commits；无 shared tag、无 push |
| C10 | `UPDATE`：ignored 原路径留 provenance；1,209-file ALL-Markdown tree 仍外部历史 snapshot |

remainder = `0`。

## 6. 结论边界

该 fresh run 证明 candidate commit 的项目文件、hydration 和 verifier 不再要求三个 ignored
source islands。它不证明模型理解、不重证数学、不关闭 aistudio coverage，也不把
`codex/semantic-overview` 自动变成 `main` current truth。

revision 131 可以据此把 F-016 与 `A-WORKTREE-EVIDENCE-PORTABILITY-001` 从 pending 改为
`VERIFIED_WITH_SCOPE`。最终 integrator 仍须用 expected target HEAD 审查 candidate；若 main
在此期间占用 revision 130/131 或修改相关 schema，必须在 target 重新生成 checkpoint，不直接
移植候选序号。
