# 哥德尔式 Q 证明包（CG001-C-84 至 C-94）

本目录是 Claude 线目标包 CG-005 的 Lean 4 证明包。它把研究发起人 2026-10-04 的 “ZFC Failure” 论证（bare ZFC 在时间维度上的理论观察力不完备）按哥德尔的方式形式化：过程取作部分递归程序，原过程完成取作停机，理论的接受接口取作它对“永不停机”的证明，对角点由 Kleene 第二递归定理实际构造。

- 精确命题、前提、ZFC 实例化所依赖的标准元定理与禁止外推：[CLAIM.md](CLAIM.md)。
- 设计、逐项对照与归因：`.claude/goals/CG-005-godel-q-synthesis/设计.md`；人话综合：同目录 `综合报告.md`。

## 文件

| 文件 | 内容 | 命题 |
|---|---|---|
| `GodelQ/ProcessObservation.lean` | 过程完成与阶段观察；Kleene–罗素对角；完备观察者不可枚举；补丁塔 | C-84 至 C-87 |
| `GodelQ/EffectiveTheory.lean` | 有效理论的 Q：Π1 可靠、哥德尔 I 过程形式、魔鬼交易；非空与必要性控制 | C-88 至 C-90 |
| `GodelQ/GodelZenoRunner.lean` | 哥德尔–芝诺跑者（圆环读法、平凡芝诺控制）；A_general ⟺ Q 完备；ZFC-1 二难 | C-91、C-94 |
| `GodelQ/ProvabilityLogic.lean` | HBL 前提下的 Löb、哥德尔 II、自用 P 的崩塌、ZFC-1 严格更强；一致模型（只用 Lean 核心） | C-92 |
| `GodelQ/OmegaQuestion.lean` | 同一个 ω 追问：芝诺、H0（参数）、过程停机；P_fin 被否定；可观察性分界 | C-93 |
| `GodelQ/Qualification.lean` | C-84 至 C-94 的精确类型逐条重述并打印公理 | 全部 |
| `GodelQ/Negative/*.lean` | 四个负控制（可靠性、一致性、有效性、Gödel II） | 见 CLAIM §5 |
| `LEAN_TOOLCHAIN.json` | 固定的 Lean v4.34.0 文件哈希 | — |
| `MATHLIB_CLOSURE.json` | 本项目 Mathlib 构建在导入闭包中 1,692 个模块的编译产物哈希；覆盖目录里本目标编译的 8 个模块 | — |

## 运行

| 运行 | proof id | 结果 |
|---|---|---|
| `HoTT/verification/runs/20261007-CG001-GODEL-Q-01` | MP-CG001-GODEL-Q-001 | KERNEL_ACCEPTED_WITH_SCOPE；内核公理只有 propext、Classical.choice、Quot.sound（C-92 无公理） |
| `…/20261007-CG001-GODEL-Q-NEG-SOUNDNESS-01` | MP-CG001-GODEL-Q-NEG-SOUNDNESS-001 | KERNEL_REJECTED（预期） |
| `…/20261007-CG001-GODEL-Q-NEG-CONSISTENCY-01` | MP-CG001-GODEL-Q-NEG-CONSISTENCY-001 | KERNEL_REJECTED（预期） |
| `…/20261007-CG001-GODEL-Q-NEG-EFFECTIVENESS-01` | MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001 | KERNEL_REJECTED（预期） |
| `…/20261007-CG001-GODEL-Q-NEG-GODEL-II-01` | MP-CG001-GODEL-Q-NEG-GODEL-II-001 | KERNEL_REJECTED（预期） |

核对：`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --rerun`（负控制加 `--expect-rejected`），五个运行逐字节重放一致，输出存 CG-001 `verification/`；另在干净目录中独立重放，全部一致（`.claude/goals/CG-005-godel-q-synthesis/replays/clean-replay-20261007.log`）。索引：GOAL_LOCAL_INDEX_ONLY（CG-001 证据索引 §24）；共享矩阵待 integrator 登记。

## 复现

在仓库根目录：

```bash
python3 -B .claude/goals/CG-005-godel-q-synthesis/tools/godelq_lean_check.py --package HoTT/formal/claude-cg001/godel-q GodelQ/ProcessObservation.lean GodelQ/EffectiveTheory.lean GodelQ/GodelZenoRunner.lean GodelQ/ProvabilityLogic.lean GodelQ/OmegaQuestion.lean GodelQ/Qualification.lean
```

前提：本机存在 `~/.elan/toolchains/leanprover--lean4---v4.34.0`、`/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed29652…` 与覆盖目录 `/Volumes/D/HoTT-toolchain-cache/godel-q-mathlib-ext-v4.34.0`。驱动在编译前核对全部固定哈希，任何一项不符即退出 3；编译在 `sandbox-exec` 的禁网沙箱里进行，不经 elan 代理。在别的机器上复现，需要同一 Mathlib commit 的构建，并按 `make_godelq_pins.py` 重新生成固定记录（会改变哈希，属于新运行，不是本运行的逐字节重放）。
