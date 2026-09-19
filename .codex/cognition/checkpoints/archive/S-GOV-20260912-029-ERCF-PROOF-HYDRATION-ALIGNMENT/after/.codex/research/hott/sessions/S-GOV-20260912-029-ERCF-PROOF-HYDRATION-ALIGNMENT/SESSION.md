# S-GOV-20260912-029-ERCF-PROOF-HYDRATION-ALIGNMENT

- 触发：`plan --profile research --task A-ERCF-FACTORIZATION-FORMAL-001` 返回 `EMPTY_REQUIRED_FILE: HoTT/verification/runs/20260912-MP-ERCF-001-02/stderr.txt`。
- 根因：零字节 stderr 是正确、必须保留的 raw run evidence；runtime 的 `full_sources` 面向可读认知正文，拒绝空文件也是正确行为。stable record 把两类资产混在同一加载列表。
- 修复：空 stderr 原件、其 SHA-256 和 RUN.json 均不修改；仅从 result record 的 `full_sources`/`resolution.evidence` 删除直接正文水合，继续通过 RUN.json、source manifest 和 verifier 路由。
- 数学状态：`MP-ERCF-001`/`C-59`–`C-66` 不变；仍是一般 Lean 结果、未提交、非 HoTT 悖论。
- 三件套：无语义变化；只同步 revision 29/generation 013。core 不变。
- Git：未 commit、未 tag、未 push。
