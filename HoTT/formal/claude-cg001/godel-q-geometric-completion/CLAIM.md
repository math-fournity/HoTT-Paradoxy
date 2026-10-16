# CG001-C-127：`GeometricCompletion.lean` 在本机 Mathlib 上重放成功，八方向覆盖的最后一个缺口补齐

> **证明包**：`MP-CG001-GODEL-Q-GEOMETRIC-COMPLETION-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），单元 W9b；本机 Codex 会话，2026-10-09。授权原话（2026-10-09）：“按照你的想法，推进工作，直至‘形式化与机器化’彻底完成，而且必须 Cover 所有值得保留的 8 个当初的 git worktree 留下的工作方向。”
>
> **理论变体**：Lean 4（v4.34.0）加本机 Mathlib 构建（`5ed29652`，2329 个 `Mathlib.*` olean 在 `/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/.../.lake/build/lib/lean`），经典逻辑，内核公理只有 `propext`、`Classical.choice`、`Quot.sound`。不使用 Foundation。
>
> **身份**：本机重放与来源固定（不是新数学）。

## 0. 这个包做了什么、没做什么

上一轮八方向覆盖（CG001-C-123–C-126）把 dev-02/03/04 留在分支的 16 个 **Lean-core** 正源在 `dev` 上重新执行，
但把 dev-03/dev-04 的 `GeometricCompletion.lean` 排除在外，理由记为“本机 toolchain pin 未含 Mathlib 构建树”。
**本包核实这一理由不成立**：本机 `/Volumes/D/HoTT-toolchain-cache/` 下有一颗完整的 Mathlib `5ed29652` 构建
（`Mathlib/Analysis/SpecificLimits/Normed.olean` 存在）。CG-007 既有 pin 只列 8 个依赖包而不列 Mathlib 本体根，
是因为 CG-007 其余包不 import Mathlib；这是一个 pin 覆盖面的选择，不是能力缺失。

本包把 Mathlib 本体根纳入 `library_roots`（新工具 `make_mathlib_pins.py`），让 `GeometricCompletion.lean`
在本机可重放，并为它生成 `dev` 上的正式收据。

**没做什么**：没有改动源一字一句，也没有证明任何新命题。定理在分支上已被 GPT 线证明；本包只重执行。

## 1. 精确命题

编号 **CG001-C-127**：`GodelQ/GeometricCompletion.lean`（dev-03 与 dev-04 两份原件逐字节相同，SHA-256 见运行收据）
在 pinned Lean 4.34.0 与本机 Mathlib `5ed29652` 下**编译通过**（exit 0，stderr 空），8 条 `#print axioms`
全部只报告 `propext`、`Classical.choice`、`Quot.sound`。

命题本身（逐字见分支 `GeometricCompletion-CLAIM.md`，本包不改写）：
几何部分和 `zenoPartialSum n = 1 - (1/2)^n` 对每个自然数阶段严格小于 1、永不到达 1、并在实数拓扑中趋于 1；
因此“有极限结果”与“有有限阶段端点”两个形式谓词对这一具体序列不等价；另有一个闭区间 `[0,1]` 时间域的
正控制模型，其中轨迹确有终端参数。

**这不决定**：某个指定的物理或哲学过程是否在时间端点完成、芝诺的标准解说是否用了更强的完成概念、
ZFC 是否缺一个元理论判断、ZFC 是否不一致。分支 CLAIM 自己写明了这些是分开的义务。

## 2. 运行
| run | proof | 预期 | 退出 | 结果 |
|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-GEOMETRIC-COMPLETION-01` | `MP-CG001-GODEL-Q-GEOMETRIC-COMPLETION-001` | ACCEPT | 0 | `KERNEL_ACCEPTED_WITH_SCOPE` |

驱动：CG-006 的冻结 `zfc_lean_check.py`（以包为参数，禁网沙盒，绝对路径调用 pinned 二进制，不经过 elan 代理）。
pins 由本包新增的 `make_mathlib_pins.py` 生成，它与 CG-007 的 `make_pins.py` 只差一处：`library_roots` 增加
`mathlib` 根并让 `TOP["Mathlib"]` 指向它，`lean_path` 也把该根纳入。其余 pin 逻辑、二进制固定与闭包核Digest不变。

## 3. 文件

- `GodelQ/GeometricCompletion.lean`：逐字节复制自 `origin/dev-03:HoTT/formal/zfc-observation-boundary/GeometricCompletion.lean`（与 `origin/dev-04` 同路径文件逐字节相同）。
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：pins。`module_count` 1792，含 Mathlib 本体闭包。
- 分支上的命题全文与禁止外推：`git show origin/dev-03:HoTT/formal/zfc-observation-boundary/GeometricCompletion-CLAIM.md`。

## 4. 禁止外推

1. 不把“本机可重放”读成“这条线的结论被独立复核”。数学内容、范围与禁止外推仍以分支自己的 `CLAIM.md` 为准。
2. 不把本包读成几何完成性或芝诺问题被解决。它只是一个实分析控制：极限谓词与有限阶段谓词对该具体序列不等价。
3. 不声称 `Mathlib` 本体进入了 CG-007 其它包的 pin。只有本包含它；其它包仍只 pin 8 个依赖包加 Foundation 构建。
4. 本包不使用 Foundation，因此与 CG-007 其余包的 `MATHLIB_CLOSURE.json` 不可互换。

## 5. 索引路线

同 CG-007 全线：CG-001 证据索引、共享矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md`、`形式化追踪/05-分支上的形式包/`。
`RUN.json` 的 `index_status` 为 `PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`，`git_status` 为
`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`（commit 前捕获）。

## 6. 工具

`.claude/goals/CG-007-formalization-completion/tools/make_mathlib_pins.py`：`make_pins.py` 的变体，
把 Mathlib 本体构建根纳入 `library_roots` 与 `lean_path`。
