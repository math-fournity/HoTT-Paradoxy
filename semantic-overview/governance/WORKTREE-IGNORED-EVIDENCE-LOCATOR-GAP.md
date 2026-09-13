# Git worktree 下被忽略嵌套证据的定位缺口

> 资产身份：`CANDIDATE_GOVERNANCE_FINDING / CONTRIBUTOR_ONLY`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前状态：`REPRODUCED / CURRENT_OWNER_NOT_MUTATED`

## 1. 发现

项目的 cognition loader 把若干 `workspace/**` 路径登记为 stable record 的
`full_sources`。主工作树 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 恰好保存了一个被顶层
`.gitignore` 排除的嵌套 Git repo `workspace/`，所以这些路径在主工作树可读。新建 linked
worktree `/Volumes/D/HoTT-semantic-overview` 时，顶层 Git 只检出顶层 repo 跟踪的对象；被
忽略的嵌套 repo 及其工作文件不会自动复制，导致同一顶层 commit 的 task hydration 在两个
worktree 得到不同结果。

这不是两个分支编辑同一文件产生的 merge conflict。它是 stable record 使用了一个只在某个
checkout 本地存在、却没有显式 locator 的证据路径，因而不具备 worktree 间可达性。

## 2. 可复现触发

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

## 3. 影响范围

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

## 4. 为什么最终 merge 本身不能修复

Git worktree 可以隔离两个 AI 对同一顶层 repo 的文件修改；每个分支在自己的 checkout 中
维护候选文档，最终 integrator 可以按 exact commit 审查和合并。这能解决并发写入和 current
owner 冲突。

这里的六个底层证据没有进入顶层 repo 的 commit 图。无论把哪一个 contributor 分支 merge
到 main，普通 merge 都不会携带另一个被忽略嵌套 repo 的工作树内容，也不会记录应该去哪个
外部 root、哪个 nested commit 读取。只有显式把证据或定位合同纳入可版本化真值，问题才会
消失。

## 5. 候选修复

### 5.1 项目内最小修复

把这 6 个 stable-record 必需文件逐字节导入顶层 repo 的 tracked source/audit 区：

1. 为每个文件记录原嵌套 repo root、commit OID、原路径、bytes 和 SHA-256；
2. 保存一个 machine-readable import manifest；
3. 将三个 stable records 的 `full_sources` 改指向顶层 tracked 副本；
4. 保留原路径为 provenance，不把副本冒充原始 repo；
5. 在新的 clean linked worktree 上运行受影响的三条 task hydration。

这个方案最符合当前 loader 的 repo-relative path 模型，变更面也最小。它不应把整个历史
`workspace/` 无差别导入，因为 stable records 当前只要求这 6 个文件。

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

这个扩展只有在多 repo evidence 是稳定需求时才值得引入。对当前 6 文件缺口，tracked import
是较小方案。

## 6. 不采用的修补方式

- 不让 loader 发现文件缺失后静默回退到主工作树；这会让证据来源取决于本机 checkout 布局，
  也会绕过 hash/commit 身份；
- 不把 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 硬编码成所有 worktree 的 fallback；
- 不用 symlink 把 contributor 的 `workspace/` 指向主工作树 mutable 文件；
- 不复制整个 `workspace/` 后声称它已进入顶层 Git；
- 不把一次主工作树成功的 snapshot 当作所有 linked worktree 的可移植收据。

## 7. 验收场景

未来 integrator 若接受修复，应至少核验：

1. 在只有主工作树保存旧嵌套 repo 的初始场景中，新 linked worktree 能通过显式 tracked
   import 或 pinned locator 完成三个受影响 record 的 hydration；
2. 修改导入副本或外部 blob 后，SHA-256 漂移必须失败；
3. locator 的 nested commit 不存在或 path 在该 commit 不存在时，必须给出可区分错误；
4. 不允许退回读取另一个 checkout 的同名 mutable 文件；
5. 原有纯顶层 tracked sources 的 plan/read/check 行为和 snapshot 确定性保持不变；
6. fresh linked worktree 测试必须由 Git 创建，不用预先手工复制 `workspace/` 粉饰结果。

## 8. 写回边界

本文件只登记 contributor 复现的治理缺口和候选修复。它没有修改：

- `.codex/research/hott/STATE.json`；
- `LOAD_SET.json`、`PROTOCOL.md` 或 cognition runtime；
- 顶层 `.gitignore`；
- 三个 stable records 的 current identity；
- 主工作树或嵌套 `workspace` repo。

最终是否采用 tracked import，或把 external/Git-blob locator 提升为项目乃至全局治理能力，应由
用户选定的 integrator 在 canonical target 上完成影响分析、schema/manager/validator 更新和
fresh-worktree 验收。
