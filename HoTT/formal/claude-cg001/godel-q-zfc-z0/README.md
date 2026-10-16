# godel-q-zfc-z0：Z0 的条件形式（CG001-C-103）

CG-006 的 S6。哥德尔第二不完备定理对 Foundation 中真实的 𝗭𝗙𝗖（Z0：“𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停机”）还没有形式化；本包把它化成两条精确的 Lean 前提，并在这两条前提下证出结论。命题全文与禁止外推见 [`CLAIM.md`](CLAIM.md)。

## 文件

| 文件 | 内容 |
|---|---|
| `GodelQ/ZFC/Z0Shadow.lean` | 算术影子 `Sh`、`Sh_provable_iff`、`Sh_consistent`、`R0_le_Sh`、条件定理 `zfc_z0_conditional` 与 `sh_z0_conditional` |
| `GodelQ/Negative/WrongZ0WithoutISigma1.lean` | 负控制：只给 `Sh.RE`、不给 `𝗜𝚺₁ ⪯ Sh` |
| `GodelQ/ProcessObservation.lean` 等 15 个依赖模块 | 与 `../godel-q-zfc/` 的同名文件逐字节相同 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,893 个模块）的编译产物哈希，由 `make_z0_pins.py` 生成 |

## 重放

在仓库根目录：

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-01 --rerun
```

负控制加 `--expect-rejected`，运行目录换成 `20261008-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-01`。

## 运行

| run | proof | 结果 | 重放（2026-10-08） |
|---|---|---|---|
| `20261008-CG001-GODEL-Q-ZFC-Z0-01` | `MP-CG001-GODEL-Q-ZFC-Z0-001` | KERNEL_ACCEPTED_WITH_SCOPE，exit 0，stderr 0 B，五条定理的公理报告全为 propext、Classical.choice、Quot.sound | PASS_WITH_SCOPE（`.claude/goals/CG-001-targeted-overview/verification/20261008-CG001-GODEL-Q-ZFC-Z0-01.json`） |
| `20261008-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-01` | `MP-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-001` | KERNEL_REJECTED（细化阶段，实例 `𝗜𝚺₁ ⪯ Sh` 找不到），exit 1 | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED |

目标内索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §26。共享矩阵：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的 CG-006 S6 一节。
