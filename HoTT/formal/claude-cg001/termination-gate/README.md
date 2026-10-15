# termination-gate：终止检查是这道门（CG001-C-431）

> CG-010 的 H3a（研究发起人原话逐句对照）里唯一新补的证明。本机会话 91beaf35（012-Opus），2026-10-15；独立 worktree `claude/012-opus-w8`。精确命题、读法与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人 10-14 说，可停机“在算法设计中，更是一个算法合法的最根本的前提”。本包给这句话一个形式影子，只用 Lean 内核，不依赖任何公理：

- 不问停不停就接受递归定义，等于说每个命题上的每个自映射都有不动点。这样一来，`False` 与一切命题都证得出，数据版同样。
- 过了门的递归（每次调用都沿良基关系往下走），它的定义方程有解，没有矛盾。
- 负控制：在 Lean 里直接写 `loop : False := loop`，被终止检查拒绝。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/Gate/Core.lean` | 不设门的原则、三条崩塌、良基递归的正控制（只用 Lean 内核） |
| `GodelQ/Gate/QualificationGate.lean` | 命题对照 `qual_C431` 与公理审计 |
| `GodelQ/Negative/WrongLoop.lean` | 负控制：`loop : False := loop` |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包，逐字节复制自 `halting-without-lem` |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-TERMINATION-GATE-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-TERMINATION-GATE-NEG-01 --rerun --expect-rejected
```
