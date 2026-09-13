# MP-ONLINE-CAUSALITY-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。

本文件记录在线因果资格的第一机器构造：区分完整流函数与只读已到达输入的策略。

## 1. 触发与依据

- 触发：S040 后 `方向追踪.md` §6 第 4 项（在线因果资格第一机器构造）。
- 依据：`DIR-L-TIME-WORK-DIMENSION` 的下一判别动作（选一个真实在线接口，区分完整流函数与按到达顺序读取的策略）；`OUT-W-TEMPORAL-TRANSPORT` 与 `OUT-L-TIME-BOUNDARY` 的历史背景。

## 2. 本轮构造

- 源演算：`Stream := ℕ → Bool`；时刻 n 的可见前缀 `Prefix n`（前 n+1 个输入的嵌套对）；在线策略 `(n) → Prefix n → Bool`；完整流函数 `Stream → Bool`。
- 反例：两个流在时刻 0 的前缀都是单个 `false`，但第二个输入不同（`false` vs `true`），因此时刻 0 的在线策略无法读出第二个输入。
- 正例：`readFirst`（时刻 0 读第一个输入）与 `readSecond`（自时刻 1 起读第二个输入）。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-106` | 不存在时刻 0 读出第二个输入的在线策略 | `no-zero-time-lookahead` |
| `C-107` | 第一个输入在时刻 0 可在线读取 | `readFirst`、`first-input-online`、`first-correct` |
| `C-108` | 第二个输入自时刻 1 起可在线读取 | `readSecond`、`second-input-online-later` |
| `C-109` | 完整流函数 `s ↦ s 1` 存在且正确，而时刻 0 在线策略不存在 | `complete-second`、`complete-second-correct`、`knowledge-gap` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-ONLINE-CAUSALITY-001-01/`；
- 同一 Agda 2.8.0 + Cubical v0.9 工具链；exit 0，stderr 0 字节，零警告；
- 独立重放：`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`；
- 矩阵第八次增长后重放九个旧包，全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。

## 5. 失败与修订谱系

初版用 `Fin` 索引前缀，触发 Cubical 的 `UnsupportedIndexedMatch` 警告（`suc` 单射在 Cubical 中不受支持）；改为嵌套对前缀后零警告通过。命题未削弱。

## 6. 判词与边界

判词：`ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`。

- 边界来自"时刻 n 只读前缀"的建模事实，不是人为不相容合同；
- 在线资格分任务、分时刻：读第一个输入可以，读第二个输入须等到时刻 1；
- 不是 HoTT 悖论：若 consumer 要求时刻 0 输出未来值，是合同越级；
- 不主张物理时间、HoTT 独有或 guarded/clocked 完整翻译。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
