# godel-q-geometric-completion：分支的实分析控制在本机 Mathlib 上重放（CG001-C-127）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W9b。精确命题、来源与禁止外推见 `CLAIM.md`。

## 这个包做了什么

上一轮八方向覆盖把 dev-03/dev-04 的 `GeometricCompletion.lean` 记为“本机 toolchain pin 未含 Mathlib 构建树”，
因此没有给它 `dev` 上的收据。本包核实本机**有**完整的 Mathlib `5ed29652` 构建，缺的只是 pin 没列它。
纳入 Mathlib 本体根后，这条 117 行的实分析源在 pinned Lean 4.34.0、禁网沙盒下编译通过，8 条公理报告全是三条标准公理。

## 文件

| 文件 | 内容 |
|---|---|
| `GodelQ/GeometricCompletion.lean` | 逐字节复制自 `origin/dev-03`（`origin/dev-04` 同路径文件逐字节相同） |
| `LEAN_TOOLCHAIN.json` | pinned Lean 4.34.0 二进制与 core 文件的逐字节与 SHA-256 |
| `MATHLIB_CLOSURE.json` | 导入闭包 1792 个模块的 SHA-256，含 Mathlib 本体根与 8 个依赖包 |

## 复现

```bash
python3 -B .claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py \
  --package HoTT/formal/claude-cg001/godel-q-geometric-completion \
  GodelQ/GeometricCompletion.lean
```

pins 重新生成：

```bash
python3 -B .claude/goals/CG-007-formalization-completion/tools/make_mathlib_pins.py \
  --package HoTT/formal/claude-cg001/godel-q-geometric-completion
```

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-GEOMETRIC-COMPLETION-01` | `MP-CG001-GODEL-Q-GEOMETRIC-COMPLETION-001` | 接受 | 0（stderr 0 B；8 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | `KERNEL_ACCEPTED_WITH_SCOPE` | 精确重放一致 |

索引：CG-001 目标 `证据索引.md`，以及共享矩阵末节。
