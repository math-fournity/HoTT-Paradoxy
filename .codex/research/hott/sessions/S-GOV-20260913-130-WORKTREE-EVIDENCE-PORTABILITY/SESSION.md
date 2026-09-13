# S-GOV-20260913-130-WORKTREE-EVIDENCE-PORTABILITY

- 用户授权：在看到 linked worktree 4/6 与三个 ignored evidence islands 后，用户明确要求“你把这事做了吧”（ruling §22）。
- 目标：让 current hydration 与 canonical verifier 的决定性输入由顶层 tracked file/snapshot 恢复；不依赖主 checkout ignored working tree。
- source baseline：`80da06ead06f38bc87ec8ebe7c82f72865401308`；42-file transform snapshot 按 SOURCE_MANIFEST hash 导入，旧 nested bytes 未改。
- static implementation：`d58dbfdbb4dd1f71c192801f57f49cfacc288933`；合同、Feature/ruling、AGENTS/Skill/PROTOCOL/LOAD_SET、manifest v2 与 verifiers 已提交。
- 路由：8 个 `workspace/**` refs（6 unique）改到 `sources/webgpt/workspace-snapshot/**`；A-AISTUDIO 删除 ignored 同字节重复路径；understanding historical side 改 tracked transform snapshot。
- 当前证据：import 42/42 PASS；workspace 6/6 / 8 refs PASS；understanding 36/24 PASS；governance shards 与 three-way rev129 PASS；pre-checkpoint fresh 对旧 LocalGPT path fail closed。
- 完成边界：本 checkpoint 只登记 IMPLEMENTED_LOCAL_PENDING_FRESH；必须 commit 后从 exact OID 新建无 ignored islands 的 linked worktree做正负验收。
- 非目标：不修改原 nested repos，不恢复 aistudio-docs，不改变数学 claim/研究判词，不 merge main，不 push/tag，不修改 machine-overview worktree。

## C01–C10 固定影响闭包

- C01 `UPDATE`：ruling §22、F-016 与验收状态已新增。
- C02 `UPDATE_PROJECT_ONLY`：新增项目证据可移植性合同；共享 `/Users/aurolafly/codex` 当前有其它未提交治理工作，本修复不混入该 repo，shared contract 后续独立审查。
- C03 `UPDATE`：项目 PROTOCOL v2.7、local governance Skill 3.7、LOAD_SET 4.1 与 source/merge managers 已同步。
- C04 `UPDATE`：项目 AGENTS 新增 `WORKTREE_EVIDENCE_PORTABILITY_V1`；全局 AGENTS 不变。
- C05 `UPDATE`：README、docs/source maps、current understanding evidence locators 与 replacement routes 已更新。
- C06 `UPDATE`：understanding verifier 增加 path/tracked/tree checks；fresh verifier覆盖五个 portability tasks；正负/fresh验收已固定。
- C07 `NO_CHANGE`：Codex config、Rules/Hooks/plugins、权限和 secret 边界未改变。
- C08 `NOT_APPLICABLE`：没有产品专属 host adapter 或 OpenCode runtime 变化。
- C09 `UPDATE_CANDIDATE`：source/static commits 已固定；revision 130 待提交；contributor branch 不创建共享 tag、不 push。
- C10 `UPDATE`：旧 ignored 路径保留为 provenance，历史 checkpoint/receipt 不改；完整 1,209-file ALL-Markdown snapshot 与 shared-generic follow-up 保持显式边界。
- remainder：`0`。
