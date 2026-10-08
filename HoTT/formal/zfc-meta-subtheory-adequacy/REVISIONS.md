# C6A 收据修订谱系

所有三次正向 Lean 执行都接受了同一 `ApplicationAdequacy.lean` 源码；只有 `-03` 是当前 primary receipt。

| run | 代码内核结果 | 证据状态 | 为什么不作 primary |
|---|---|---|---|
| `20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-01` | exit 0 | `HISTORICAL_CAPTURE_SUPERSEDED` | capture 工具错误假定 Git root 的 `.git` 必为目录，受管 worktree因此无法作为支持路径资格化；首次手动 run 后补的 receipt缺 Lean external-binary pin。 |
| `...-02` | exit 0 | `HISTORICAL_CAPTURE_SUPERSEDED` | 已在 capture manifest 中 pin Lean binary，但初版 toolchain schema未提供 proof-version-closure 所需的 `lean.root`，closure verifier拒绝该 metadata。 |
| `...-03` | exit 0 | `PRIMARY_RUN / VERIFIED_WITH_SCOPE` | capture 工具按 Git top-level 支持 linked worktree、source manifest pin固定 Lean binary、toolchain满足 registry verifier，索引行已冻结。 |
| `20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-NEG-001` | exit 1 | `EXPECTED_NEGATIVE_CONTROL` | 正确拒绝将 paid-bridge case标为 failure。 |

这些收据都保留；没有用删除旧目录来伪造“一次即成功”的历史。修订仅涉及 capture/provenance 资格，不改变 C-369 的 Lean 命题或其来源范围。
