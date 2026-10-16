+# T-PRECISION 认知加载器 bootstrap HEAD repair

> **身份：** `COGNITION_INTEGRITY_REPAIR / PRECHECKPOINT_BOOTSTRAP / NO_MATHEMATICAL_CLAIM`。
>
> **repair branch base：** `f07d9801a5279e93aac883460ca9d0acc7190416`。
>
> **触发：** `cognition_runtime.py plan --profile research --task F-052` 在 Git-clean repair worktree 中以 `UNCOMMITTED_STATE: MEMORY/001 - 当前执行队列.md` fail-closed。

## 1. 诊断

`.codex/cognition/HEAD.json` 与 `STATE.json` 均仍写 revision `298` 和
`S-GOV-20261002-CORE-GENERATION-13-ONEPASS-P`，没有未完成 transaction 或 writer lock。
但 HEAD 的 `tracked` 表仍引用旧字节，而下列四个 mutable owner 已在随后提交中改变：

| 路径 | HEAD 旧 hash | 当前 Git-clean bytes |
|---|---|---|
| `MEMORY/001 - 当前执行队列.md` | 从旧 HEAD 读取 | `4fd0dc7390b633f1be10751dfd93a774b5da0b493ac71a782ea63ac5cefb419b` |
| `MEMORY/003 - 当前验证状态与顺序日志.md` | 从旧 HEAD 读取 | `5d75b54e69720d593ef4b4d76917069c04a8640d13cdc4a53766104fb004e411` |
| `全景视野/003 - 当前机器证明包与原生重放.md` | 从旧 HEAD 读取 | `9546e5d553daae17d5d7fa6dfc122828781697804425b3bc829dd7fe658a4ced` |
| `方向追踪/002 - 治理与用户方向.md` | 从旧 HEAD 读取 | `429fc32118cd2a5f58d344f5320fe35496b8ab89737794c7de65a9f36ad2115f` |

这不是数学或来源结论的变化；它是旧 revision 的 hash inventory 与已提交 current owners 脱节。由于 runtime 的 `checkpoint` 在 payload 预处理时也调用 `plan`，不能直接用普通 checkpoint 修复这一循环。

## 2. 受限 bootstrap 动作

本 repair 只把上述四个 `tracked` 值更新为当前文件的 SHA-256；它不改变 revision、latest session、STATE records、数学 claim、Feature、MEMORY 语义或任何来源结论。旧 HEAD 的字节保留于 Git 父提交，且本审计固定其原因和范围。

bootstrap 完成后，必须立即：

1. 调用 `plan` 并取得新 snapshot；
2. 用新 `S-GOV-20261005-T-PRECISION-CLOSURE-REPAIR` session bundle 运行带 `--apply` 的正式 checkpoint；
3. 由 checkpoint 增加 STATE revision、写入新的 HEAD 与 transaction/result receipt；
4. 仅在 `result.json.status=CHECKPOINT_COMMITTED` 后，才称自动 hydration 恢复。

若任一项失败，本 repair 只能称 `BOOTSTRAP_HEAD_REFRESHED_PENDING_CHECKPOINT`，不得伪称 checkpoint 已完成。

## 3. 边界

- 不把 hash repair 说成 T-OBS、T-DIAG、T-Meta 或 T-ZFC 的数学进展；
- 不重开 `CURRENT_T_PRECISION_SOURCE_DENOMINATOR_CLOSED_WITH_SCOPE`；
- 不替代未来 actual source payment、user-defined OriginDone 或 new proof run 的重开条件；
- 不修改 canonical `dev` 的另一写入者 dirty files；当前工作只在独立 repair branch 中进行。

## 4. 验证与原件保留

正式 checkpoint 返回 `CHECKPOINT_COMMITTED`，随后 `plan --profile research` 和带该 snapshot 的
`check --profile research` 均通过。分片结构校验亦通过。

checkpoint 的 `before/` 与 `after/` 目录按合同逐字节保存所有 mutable owner；其中包含早已存在于
投影／阐释原件中的尾随空格和末尾空行。因此全量 `git diff --check` 会对这些**收据副本**报告格式提示。
不得为使该检查变绿而改写 before/after bytes。HEAD、STATE、repair session 和本审计自身的 scoped
diff check 另行通过。
