# Git worktree 下被忽略证据岛的定位与验证缺口

> 资产身份：`CANDIDATE_GOVERNANCE_FINDING / CONTRIBUTOR_ONLY`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前状态：`REPAIRED_AND_FRESH_VERIFIED_ON_CANDIDATE / NOT_INTEGRATED`

## 1. 发现

项目的 cognition loader、stable records 与 canonical verifiers 仍直接引用三类只在主
checkout 可达的被忽略证据：嵌套 `workspace/` repo、嵌套 `AI对话录/` repo，以及
`sources/local-gpt/ALL-Markdown-root/` 下的被忽略副本。主工作树
`/Volumes/D/HoTT_AI_HANDOFF_20260911` 恰好保留这些文件，所以原位运行可以通过。新建
linked worktree `/Volumes/D/HoTT-semantic-overview` 时，顶层 Git 只检出顶层 repo 跟踪的
对象；被忽略的目录和文件不会自动复制，导致同一顶层 commit 的 task hydration 与 canonical
verifier 在两个 checkout 得到不同结果。

这不是两个分支编辑同一文件产生的 merge conflict。它是当前治理记录和验证器使用了只在
某个 checkout 本地存在、却没有顶层 tracked 副本或显式 locator 的证据路径，因而不具备
worktree 间可达性。完整回归收据见
`semantic-overview/governance/WORKTREE-PORTABILITY-VERIFIER-CHECK.json`。

## 2. 可复现触发

### 2.1 task hydration

在 contributor worktree 执行：

```bash
python3 -B .codex/tools/cognition_runtime.py \
  --project-root /Volumes/D/HoTT-semantic-overview \
  plan --profile research --task A-HOTT-SELF-VALIDATION-ECONOMY-001
```

实际退出码为 `2`，唯一错误为：

```json
{"status":"BLOCKED","error":"MISSING_OR_UNREADABLE: workspace/.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md"}
```

同一文件在主工作树存在：

- 路径：`workspace/.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md`；
- bytes：`12459`；lines：`144`；
- SHA-256：`23724276957098b3044f413a157cfb7af1d165973e5c45a6904628e217ade442`；
- 嵌套 repo HEAD：`26fcecfbfecf6db66a70c1bf3e067159bce3eb6a`；
- 观察时嵌套 repo tracked tree clean。

顶层 `git check-ignore -v` 把该路径归因到 `.gitignore:4:workspace/`。因此顶层 common Git dir
共享分支、refs 和对象，并没有让该嵌套 repo 的工作文件进入 linked worktree。

本轮没有用主工作树路径静默补读后继续宣称 hydration 成功。研究任务改用不依赖这组路径的
`A-THEORY-ECONOMY-LEDGER-001`；其 research plan 成功，snapshot 为
`2c7e4ced3ccba1c1812363237cd9c8da087007057abfba4c7373f020fa51f985`。

### 2.2 canonical verifier 对照

在 contributor worktree 对项目规定的六类 verifier 做只读回归：

| verifier | contributor worktree | 主工作树对照 | 缺失输入 |
|---|---|---|---|
| governance shards | `PASS` | 未重复 | 无 |
| three-way cognition | `PASS`，revision 129 / 36 KC / 30 directions / 110 outcomes | 未重复 | 无 |
| understanding merge | exit `1`，26 errors | `PASS`，36/24 inventory | `AI对话录/理解章节/` 整目录 |
| fresh three-way | exit `1` | `PASS_WITH_SCOPE`，revision 129 | `sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md` |
| C11 ledger retrodiction | `PASS`，18 packages | 未重复 | 无 |
| proof version closure | `PASS_WITH_SCOPE`，17 frozen + 11 later | 未重复 | 无 |

understanding verifier 的 26 条错误由 1 条
`MISSING_HISTORICAL_SOURCE_DIRECTORY`、1 条 `MANIFEST_UNION_MISMATCH` 和 24 条
`NESTED_SOURCE_MISSING` 组成。fresh verifier 在调用 task
`A-AISTUDIO-COVERAGE-001` 时抛出
`MISSING_OR_UNREADABLE: sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md`。

两项在主工作树用相同 tracked verifier 和同一顶层 revision 129 运行均通过，证明失败变量是
checkout-local 被忽略证据是否存在，而不是 B04/B05 contributor 文件或 canonical state 被改坏。

## 3. 影响范围

### 3.1 `workspace/` stable-record sources

当前 `STATE.json` 中共有 8 次 `workspace/**` full-source 引用，去重后为 6 个文件，涉及 3
个 stable records：

| stable record | 路径 | 主工作树 | contributor worktree | SHA-256 |
|---|---|---:|---:|---|
| `A-C5-PARADOX-DISTANCE-001`、`A-HOTT-RESEARCH-DIRECTION-001` | `workspace/.codex/research/hott/candidates/RP-B01/PLAN.md` | 有 | 无 | `b19f81133b4a9e6af53c42ad844730bcc7a31ba0cd466b6b11f6dea6fddd2c65` |
| `A-C5-PARADOX-DISTANCE-001`、`A-HOTT-RESEARCH-DIRECTION-001` | `workspace/.codex/research/hott/candidates/RP-B01/CLAIMS.json` | 有 | 无 | `0599d57fa6696feaa8a46f544e945a05455b5db76540bfedf0f46ecd65bd664f` |
| `A-C5-PARADOX-DISTANCE-001` | `workspace/.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/CLAIMS.json` | 有 | 无 | `ff57c4d5908a3eb82ae8ced367655fe35c6c557dcee3aca9e9b564925b3631d1` |
| `A-C5-PARADOX-DISTANCE-001` | `workspace/.codex/research/hott/reviews/TRANSITION-ABSTRACTION-002/CLAIMS.json` | 有 | 无 | `2a279e0b1646a6b7afaa26e1cfcae569c50f883b51eb250852af49aacefda280` |
| `A-HOTT-RESEARCH-DIRECTION-001` | `workspace/.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md` | 有 | 无 | `71ba5c7cc07704727ddb347a63327d780d876e069645260f2c4b8b9695f32925` |
| `A-WEBGPT-R041-PAPER-001` | `workspace/.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md` | 有 | 无 | `23724276957098b3044f413a157cfb7af1d165973e5c45a6904628e217ade442` |

六个文件都被嵌套 `workspace` repo 跟踪，但没有被顶层 repo 跟踪。影响不是所有 governance 或
research plan 都失败，而是 hydration 是否成功取决于选中的 stable record 是否递归触达这三
条记录。这种条件性更容易被误判成某个 contributor 的环境坏了。

### 3.2 `AI对话录/理解章节` historical source

顶层 `.gitignore:3` 排除整个 `AI对话录/`。主工作树中的该目录本身是另一 Git repo，观察到：

- nested HEAD：`c70b01ca26c01c2078a4c0cd31a65d5fbda27fb0`；
- `理解章节/` 当前有 24 个文件；
- nested working tree 不是 clean：除 `.DS_Store` 外，
  `理解章节/B1-本地GPT工作史.md` 与 `理解章节/读遍账本.md` 有未提交修改；
- 当前顶层 `audit/understanding-chapter-merge-manifest.json` 对这两个文件记录的 SHA-256
  分别为 `dcef4ccbcc33b3b98388b0fb1d317d5538fa3e9cc07fe8457a6a54a3a3b2c5f5` 与
  `7b65dd29e05b25fae38d54ed1c2310786ab5c14ca3f6794f36bea29931bd2cb1`，与观察时
  nested working bytes 一致；
- 同一 nested HEAD 中两文件的 blob SHA-256 分别是
  `c6dc4e954635979db51118e8571bd20764121f714ea29bfd5a5cb1e014b0d6d7` 与
  `d9e4f598898147de95961fb5b6054ef89424a5775e7abb33d79db519e42f5d97`，并不等于 manifest
  固定值。

这意味着当前 merge manifest 的 PASS 不仅依赖一个外部 repo，还依赖该 repo 的 mutable、
未提交 working tree。manifest 顶层字段 `source_git_head=6f98ac71336db405ad52f4b4ee4f93c8e50b57aa`
没有把这些 nested bytes 绑定到可恢复的 nested commit；各 entry 还保存了主 checkout 的绝对
路径。当前 bytes 可能是有意保留的历史源，本 finding 不裁决其内容，也不修改它们；问题在于
其证据身份尚未版本闭合。

### 3.3 `ALL-Markdown-root` 被忽略副本

fresh verifier 需要的旧路径受
`sources/local-gpt/ALL-Markdown-root/.gitignore:2:/*` 排除，没有进入顶层 Git。主工作树中的
该文件为 32,127 bytes / 490 lines，SHA-256
`ec2fe644c608637ec9465342f4948140494662706b5861bfea5dff712a0980fa`。

顶层 repo 已经跟踪 `sources/local-gpt/HoTT_is_GONE_COMPLETE.md`，其 bytes、行数和 SHA-256
与被忽略旧副本完全相同。这个子缺口不需要新的 external locator；最小修复是把当前 stable
record 与 fresh verifier 的输入路由改到现有 tracked 副本，并重绑相应 state/snapshot 证据。

## 4. 为什么最终 merge 本身不能修复

Git worktree 可以隔离两个 AI 对同一顶层 repo 的文件修改；每个分支在自己的 checkout 中
维护候选文档，最终 integrator 可以按 exact commit 审查和合并。这能解决并发写入和 current
owner 冲突。

这里的 `workspace` 六文件、`AI对话录` 24 文件和 `ALL-Markdown-root` 旧副本都没有以这些
路径进入顶层 repo 的 commit 图。无论把哪一个 contributor 分支 merge 到 main，普通 merge
都不会携带被忽略嵌套 repo 的 working tree，也不会记录应该去哪个外部 root、哪个 nested
commit 读取。只有显式把证据或定位合同纳入可版本化真值，问题才会消失。现有 tracked
LocalGPT 同字节副本是一个可直接重路由的例外。

## 5. 候选修复

### 5.1 项目内最小修复

按三个子缺口分别做最小处理：

1. `ALL-Markdown-root`：把 `A-AISTUDIO-COVERAGE-001` 的 full source 改指现有 tracked
   `sources/local-gpt/HoTT_is_GONE_COMPLETE.md`；两者当前逐字节相同，仍须在事务中复核 hash；
2. `workspace`：把 6 个 stable-record 必需文件逐字节导入顶层 tracked source/audit 区，记录
   原 nested root、commit OID、路径、bytes 和 SHA-256，并更新三个 stable records；
3. `AI对话录/理解章节`：先由 integrator 识别 24 文件中应被冻结的确切 working bytes；对
   两个 dirty 文件明确保存“nested HEAD blob”与“当前 working bytes”的差异，再把被接受的
   历史版本导入顶层 tracked source 区；
4. 重建 understanding merge manifest，使所有 source 路径为 repo-relative tracked 路径，
   并记录真实的来源 repo/commit/working-tree 状态；
5. 保存 machine-readable import manifest，保留原路径为 provenance，不把副本冒充原始 repo；
6. 在一个由 Git 新建、没有手工复制任何 ignored island 的 clean linked worktree 上运行三条
   受影响 task hydration 与全部六类 verifier。

这个方案最符合当前 loader/verifier 的 repo-relative path 模型。它不应把整个历史
`workspace/` 或 `AI对话录/` 无差别纳入顶层 repo；只导入当前 stable records 与历史 merge
验证真正依赖的固定文件。

### 5.2 可复用 locator 扩展

若项目有长期保留多个嵌套/外置 evidence repo 的真实需要，可以给 source schema 和 loader
增加显式 locator，例如：

```json
{
  "kind": "git_blob",
  "repo": "/Volumes/D/HoTT_AI_HANDOFF_20260911/workspace",
  "commit": "26fcecfbfecf6db66a70c1bf3e067159bce3eb6a",
  "path": ".codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md",
  "sha256": "23724276957098b3044f413a157cfb7af1d165973e5c45a6904628e217ade442"
}
```

loader 应从指定 commit 的 blob 读取并复核哈希，而不是从某个 checkout 的 mutable working
tree 读取。绝对路径仅描述本机 repo 位置；commit、path 和 hash 才固定证据身份。若 repo、
commit 或 blob 不可用，应以特定错误失败关闭。

这个扩展只有在多 repo evidence 是稳定需求时才值得引入。即使采用 locator，也不能指向
mutable working tree；`AI对话录` 两个 dirty 文件必须先取得可恢复 blob identity。对当前
`workspace` 六文件与 24 个 understanding 历史源，tracked import 仍是较小方案。

## 6. 不采用的修补方式

- 不让 loader 发现文件缺失后静默回退到主工作树；这会让证据来源取决于本机 checkout 布局，
  也会绕过 hash/commit 身份；
- 不把 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 硬编码成所有 worktree 的 fallback；
- 不用 symlink 把 contributor 的 `workspace/` 指向主工作树 mutable 文件；
- 不复制整个 `workspace/` 后声称它已进入顶层 Git；
- 不让 canonical verifier 依赖 nested repo 的未提交 working bytes 后仍声称 top-level commit
  已自足；
- 不为 `ALL-Markdown-root` 重复制已有同字节 tracked 文件；
- 不把一次主工作树成功的 snapshot 当作所有 linked worktree 的可移植收据。

## 7. 验收场景

未来 integrator 若接受修复，应至少核验：

1. 在只有主工作树保存旧嵌套 repo 的初始场景中，新 linked worktree 能通过显式 tracked
   import 或 pinned locator 完成三个 `workspace` record 和 `A-AISTUDIO-COVERAGE-001` 的
   hydration；
2. 修改导入副本或外部 blob 后，SHA-256 漂移必须失败；
3. locator 的 nested commit 不存在或 path 在该 commit 不存在时，必须给出可区分错误；
4. 不允许退回读取另一个 checkout 的同名 mutable 文件；
5. 原有纯顶层 tracked sources 的 plan/read/check 行为和 snapshot 确定性保持不变；
6. understanding manifest 能从 tracked source 或 exact commit blob 重算 36/24 inventory，
   不读取 nested mutable working tree；
7. 六类 canonical verifier 在 fresh linked worktree 全部达到各自声明的 PASS 状态；
8. fresh linked worktree 测试必须由 Git 创建，不用预先手工复制 `workspace/`、`AI对话录/`
   或 `ALL-Markdown-root` 粉饰结果。

## 8. 写回边界

本文件只登记 contributor 复现的治理缺口和候选修复。它没有修改：

- `.codex/research/hott/STATE.json`；
- `LOAD_SET.json`、`PROTOCOL.md` 或 cognition runtime；
- 顶层 `.gitignore`；
- 三个 stable records 的 current identity；
- 主工作树、嵌套 `workspace` repo 或 dirty 的 `AI对话录` repo。

最终是否采用 tracked import，或把 external/Git-blob locator 提升为项目乃至全局治理能力，
应由用户选定的 integrator 在 canonical target 上完成影响分析、source identity 裁决、
schema/manager/validator 更新和 fresh-worktree 验收。当前可确定的一点是：Git worktree 解决
并发编辑隔离，不会自动使被忽略证据岛可移植；原项目治理框架需要补上这一运行模型。

## 9. Candidate 修复结果（2026-09-13）

用户随后明确要求当前 AI 执行本修复。`codex/semantic-overview` 已完成项目内实现：source
commit `80da06e…`、static routing commit `d58dbfd…`、revision 130 checkpoint commit
`802e4f8…`。最终方案复用了已有 tracked workspace/LocalGPT 同字节副本，并只把旧
SOURCE_MANIFEST 已固定的 42-file transform snapshot 纳入顶层 Git。

从 `802e4f8…` 新建的 detached linked worktree 没有顶层 `workspace/`、顶层 `AI对话录/` 或
旧 LocalGPT ignored artifact；五个 portability task plans 全部水合且无 untracked document，
六类 canonical verifier 全 PASS。byte tamper、index removal、stable path 回退和 manifest path
漂移四类控制全部按特定错误失败关闭，恢复后 worktree clean 并已删除。证据：

- `audit/Git-worktree证据可移植性修复与验收-20260913.md`；
- `audit/worktree-portability-fresh-acceptance-20260913.json`；
- `.codex/research/hott/sessions/S-GOV-20260913-130-WORKTREE-EVIDENCE-PORTABILITY/`。

因此本 finding 对 candidate branch 已 `CLOSED_WITH_SCOPE`；对 canonical `main` 保持
`NOT_INTEGRATED`。若 target revision/schema 前进，integrator 必须从 exact OID 重新审查并在
target 分配唯一 checkpoint identity。
