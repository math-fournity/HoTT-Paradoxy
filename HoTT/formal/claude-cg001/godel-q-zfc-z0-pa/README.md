# godel-q-zfc-z0-pa：𝗭𝗙𝗖 解释 𝗣𝗔；Z0 只剩一条前提（CG001-C-109、C-110）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W3，本机会话 d58e0c0d，Opus 5.5，2026-10-08。精确命题与禁止外推见 `CLAIM.md`。

## 这个包做了什么

C-103 把 Z0（“𝗭𝗙𝗖 证明不了自己的矛盾搜索永不停”）化成两条前提：`Sh.RE` 与 `𝗜𝚺₁ ⪯ Sh`。本包证明了后一条，而且更强：

- 在 𝗭𝗙𝗖 的每一个模型里，自然数（ω）满足全部皮亚诺公理，连同对任意算术性质的数学归纳；
- 所以 𝗭𝗙𝗖 证明皮亚诺算术每一个定理的翻译（`paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`）；
- 于是 𝗭𝗙𝗖 的算术影子扩张 𝗣𝗔 与 𝗜𝚺₁，Z0 只剩一条前提 `Sh.RE`。

做法：
- ω 上的加乘律与序，每条用 ω 归纳证明；
- 任意算术公式在 ω 上定义的子集，由它的翻译在模型中定义，所以分离公理把它取成集合，ω 最小性给出归纳；
- 为了用 Foundation 对标准算术结构的现成化简，同一个 ω 另取一个类型同义词带标准解释，再用恒等双射把公式的真假传回来。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| CG-005/006 的 16 个模块（`ProcessObservation` 至 `Effective`）与 `ZFC/Soundness.lean` | 逐字节复制 |
| `GodelQ/ZFC/OmegaLaws.lean` | ω 上的加法、乘法的交换、结合、分配与各条序公理（Zermelo 模型） |
| `GodelQ/ZFC/PAModel.lean` | 标准解释的同义词 `W M`；𝗣𝗔⁻；归纳模式；`(N M) ⊧* 𝗣𝗔`；`paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔` |
| `GodelQ/ZFC/Z0Shadow.lean` | C-103（逐字节复制） |
| `GodelQ/ZFC/Z0PA.lean` | `𝗣𝗔 ⪯ Sh`、`𝗜𝚺₁ ⪯ Sh`；Z0 只带 `Sh.RE` |
| `GodelQ/ZFC/QualificationZ0PA.lean` | 命题对照 `qual_C109`、`qual_C110` |
| `GodelQ/Negative/WrongZ0WithoutRE.lean` | 负控制：不给 `Sh.RE` |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,893 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-PA-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-01 --rerun --expect-rejected
```

## 运行（2026-10-08）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261008-CG001-GODEL-Q-ZFC-Z0-PA-01` | `MP-CG001-GODEL-Q-ZFC-Z0-PA-001` | 接受 | 0（62 秒，stderr 0 B；94 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261008-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-01` | `MP-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-001` | 拒绝 | 1：实例 `Theory.RE Sh` 找不到 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261008-CG001-GODEL-Q-ZFC-Z0-PA-*.json`；索引：同目标 `证据索引.md` §29；共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
