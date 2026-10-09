# godel-q-zfc-z0-full：Z0 的内部化只差一条引理（CG001-C-121、C-122）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W8。精确命题、唯一阻塞引理与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- **问题**：C-120 给出“𝗭𝗙𝗖 证明不了它的算术影子的一致性句（翻译后）”。要把它读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”，需要把“证明”本身也搬进算术理论 𝗜𝚺₁。
- **做法**：不用 Foundation 那个靠选择挑出来的 Σ1 一致性句，改用一条**显式的**可证性谓词——`𝔅Z(x) := 𝗭𝗙𝗖 证明 x 的翻译`，即 `Provable 𝗭𝗙𝗸 (iT 0 x)`——作为 𝗭𝗙𝗖 算术影子 `Sh` 的可证性谓词。它逐字由 C-119 的内部翻译 `iT` 给出，没有选择。
- **结果**：
  - D1、D2（HBL2）都是定理；
  - `𝔅Z` 的一致性句与 Foundation 的 `𝗭𝗙𝗸.consistent` 在 𝗜𝚺₁ 中等价；
  - `𝔅Z σ` 是 Σ1 句；
  - D3 在标准模型 ℕ 中成立（正对照）；
  - **完整形式 `𝗭𝗙𝗸 ⊬ (𝗭𝗙𝗸.consistent)ᵗ` 以唯一一条阻塞引理为条件成立**（C-122）。
- **还差一条**：`zfcTr_D3_internalize`，即“𝗭𝗙𝗸 证明了 σ 的翻译，就能证明‘𝗭𝗙𝗸 证明了 σ 的翻译’这句话的翻译”。这是经翻译的形式化 Σ1 完全性，见 `CLAIM.md` §4。它带未证标记，因此不进入收据源。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 21 个依赖模块（`ProcessObservation` 至 `ZFC/ShRE.lean`） | 与 `../godel-q-zfc-z0-translate/` 逐字节相同 |
| `GodelQ/ZFC/Z0Full.lean` | `TrProvable`/`trProv`、`zfcTr`、D1、D2、一致性句等价、Σ1 层级、ℕ 中正对照、完整形式的条件形式 |
| `GodelQ/ZFC/Z0Blocked.lean` | **唯一阻塞引理** `zfcTr_D3_internalize`；带未证标记，**不是**任何运行的编译源 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01 --rerun
```

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01` | `MP-CG001-GODEL-Q-ZFC-Z0-FULL-001` | 接受 | 0（71.7 秒，stderr 0 B；112 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |

本包没有负控制运行，理由见 `CLAIM.md` §3。校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01.json`。索引：同目标的 `证据索引.md` §35，以及共享矩阵末节。
