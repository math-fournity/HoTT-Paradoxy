# Quality / 验证与风险

当前验证输出在 `audit/verification-report.json`、`validation/` 和 `.codex/verification/`；通过只覆盖明确样本、范围和断言。

当前 AI 数学结论的强制交付门禁见 [`数学结论机器证明与证据留存规范.md`](数学结论机器证明与证据留存规范.md)：证明源码由 `HoTT/formal/` 持有，proof assistant/kernel 运行原件由 `HoTT/verification/runs/<run-id>/` 持有，claim/proof/run 当前索引由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 持有。外部库结论必须区分源码审读、实际导入闭包重放和当前项目自证；literate Agda 的公设清点只计算 `agda` code fence 内声明。规则/静态验证通过不等于未来数学结论已证明。

当前 Git 可恢复性登记为 `HoTT/verification/PROOF_VERSION_CLOSURE.json`；它把 17 个 current package 固定到 exact proof-asset commit，并保持旧 matrix rows/run receipts 不变。Git closure 只证明资产可恢复，不重证数学。

多 worktree 下认知与 verifier 输入的可移植性见 [`Git多Worktree证据可移植性合同.md`](Git多Worktree证据可移植性合同.md)。current `full_sources` 不得直接依赖 ignored nested working tree；tracked snapshot/import 与 fresh linked-worktree 正负验收分别证明文件身份和运行可恢复性。
