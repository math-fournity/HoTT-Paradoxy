# S-GOV-20260913-131-WORKTREE-PORTABILITY-FRESH-ACCEPTANCE

- 目标：依据 revision 130 exact-commit fresh evidence 关闭 F-016 的 pending 状态。
- tested commit：`802e4f890f07adeb50d32f7d8a3e1866d8d8d597`；fresh worktree 未包含顶层 workspace/dialogues 或 legacy LocalGPT ignored path。
- 正向：import 42/42；workspace 6/6/8 refs；五个 task plans 全部 untracked=0；六类 canonical verifier PASS。
- 负向：byte tamper、index removal、旧 workspace route、manifest path identity 四类全部按特定错误失败；逐项恢复后正向再 PASS，Git clean，worktree 已删除。
- evidence：`audit/worktree-portability-fresh-acceptance-20260913.json`（SHA-256 `e5ab194a…`）与 `audit/Git-worktree证据可移植性修复与验收-20260913.md`。
- 状态：`A-WORKTREE-EVIDENCE-PORTABILITY-001` → `VERIFIED_WITH_SCOPE_FRESH_LINKED_WORKTREE / complete`；从 review_due/unresolved 移除。
- 边界：candidate 未 merge main；共享治理 repo 当前有并行 dirty 工作，本轮不修改；不 push/tag；无数学 claim。

## C01–C10 最终影响

- C01–C06：项目 ruling/Feature、合同、Skill/PROTOCOL/LOAD_SET、AGENTS/README 与 fresh/negative evidence 均 `UPDATE_VERIFIED`。
- C07：`NO_CHANGE`（config/Rules/Hooks/plugins/secret/权限不变）。
- C08：`NOT_APPLICABLE`（无 host adapter 变化）。
- C09：`UPDATE_CANDIDATE`（revision 131 与 commits；无 shared tag/push/main merge）。
- C10：`UPDATE`（历史 paths/provenance 与 external 1,209-file snapshot 边界保留；shared generic follow-up 未冒充完成）。
- remainder：`0`。
