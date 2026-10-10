# Foundation R3 重放修订记录

| Run | 结果 | 原因与处置 |
|---|---|---|
| `20261005-MP-FOUNDATION-INCOMPLETENESS-R3-001-01` | `CAPTURE_CONTRACT_INVALID_FOR_EXACT_RERUN` | capture 将 `lake build` 输出与 qualification 输出拼接进 `stdout.txt`，但 `RUN.command_argv` 只能重放 qualification；通用 verifier 因重放字节不相同而应拒绝。该 run 保留为不可覆盖的收据设计失败，不进入 claim matrix。 |
| `20261005-MP-FOUNDATION-INCOMPLETENESS-R3-001-02` | `EXTERNAL_TREE_LABEL_UNQUALIFIED` | `source-manifest` 使用了未被通用 verifier 登记的 tree label；论文本体未重跑失败，收据仍不能通过 external-dependency validation。 |
| `20261005-MP-FOUNDATION-INCOMPLETENESS-R3-001-03` | primary candidate | 复用通用 verifier 已有的同一 Foundation tree label，并保留 build 输出与 qualification 输出分离；主 run 可走完整 source/run/index validation。 |
| `20261005-MP-FOUNDATION-INCOMPLETENESS-R3-NEG-001-03` | negative candidate | 与 primary 使用同一 Foundation build，省略 `T.SoundOnHierarchy 𝚺 1` 后在 typeclass synthesis 处被拒绝。 |

这些修订只改善证据收据的 command/output 保真性；它们不扩大 C-369 到 HoTT、ZFC 或过程完成桥。
