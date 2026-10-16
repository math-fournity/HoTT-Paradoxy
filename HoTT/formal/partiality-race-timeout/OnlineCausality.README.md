# MP-ONLINE-CAUSALITY-001：在线因果资格的第一机器构造

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`

本包执行 `DIR-L-TIME-WORK-DIMENSION` 的下一判别动作：**区分"完整流函数"与"只读已到达输入的在线策略"**，并给出精确边界与正控制。

## 固定构造

- 源演算：时间索引输入流 `Stream := ℕ → Bool`；时刻 n 的可见前缀 `Prefix n`（前 n+1 个输入的嵌套对）；
- 在线策略 `OnlineStrategy := (n : ℕ) → Prefix n → Bool`（时刻 n 只能读前缀）；
- 完整流函数 `CompleteMove := Stream → Bool`（可读整条流）。

## 冻结命题

- `C-106`：不存在在时刻 0 读出第二个输入的在线策略——时间 0 的前缀是单个值，无法区分两个见证（`s₁ = const false` 与 `s₂ = false,true,…`）。
- `C-107`：正控制——第一个输入在时刻 0 即可在线读取。
- `C-108`：正控制——第二个输入从时刻 1 起可在线读取（`readSecond (suc n) p = first n (snd p)`）。
- `C-109`：知识缺口——完整流函数 `s ↦ s 1` 存在且正确，但时刻 0 在线策略不存在：**完整知识 ≠ 在线资格**。

## 解释边界（判词）

判词：`ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS`（判词阶梯第二级的结构性版本）：

- 该边界不来自人为合同：它是"时刻 n 只能读前缀"这一建模事实的直接后果；
- 正控制（C-107/C-108）说明在线资格是分任务的：读第一个输入可以，读第二个输入必须等到时刻 1；
- 不是 HoTT 悖论：类型论如实区分了"知道整条流"与"按序只读已到达输入"；若某个 consumer 要求在线策略完成前视任务（例如时刻 0 输出未来的值），那是该 consumer 的合同越级，而不是理论失败。

## 不证明（非目标）

- 不证明物理时间、延迟或资源成本主张；不主张 HoTT 独有；
- 不覆盖 guarded/clocked 类型论的完整翻译（本包是 ℕ-indexed 在线模型）；
- 不证明所有在线任务不可完成（正控制即为反例）。

## 证明身份

- proof ID：`MP-ONLINE-CAUSALITY-001`
- claim IDs：`C-106`–`C-109`
- final run：`20260912-MP-ONLINE-CAUSALITY-001-01`
- source：`OnlineCausality.agda`
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件见 `../../verification/runs/20260912-MP-ONLINE-CAUSALITY-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
