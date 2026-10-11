# 编译与验收命令

本包 4 个文件必须放在完整 repo 的对应路径下编译（它们 import 包内更早的 20 个模块）。

## 一次性 setup

```bash
REPO=/Volumes/D/HoTT_AI_HANDOFF_20260911
PKG=$REPO/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
# 把本包的 4 个文件覆盖进去（Z0Blocked.lean 是要改的那个）
cp 外部资料/Z0-D3-攻关包/Leanservice/*.lean $PKG/GodelQ/ZFC/
```

## 开发中迭代编译（快，约 60 秒全链）

```bash
cd $PKG
python3 -B /tmp/d3build/devbuild.py . <24 个模块，按依赖次序>
```

正式收据工具（会拒绝 `sorry`，所以只能在证完之后用）：

```bash
cd $REPO
python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_run.py \
  --package HoTT/formal/claude-cg001/godel-q-zfc-z0-full \
  --run-id <RUN_ID> --proof-id <PROOF_ID> \
  --claim-id CG001-C-121 --claim-id CG001-C-122 \
  --expect ACCEPT \
  --source <24 个模块，最后一个 Z0Blocked.lean> \
  --scope "..." --non-goal "..."
```

## 禁止

- 不得把带 `sorry` 的文件列进收据源；
- 不得改 `Leanservice/Z0Full.lean` 的定理类型（它已被收据固定）；
- 不得改 Foundation / Mathlib 源码。

---

## 现有收据（W8 已过核的部分，作为起点证据）

`20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01`：

- status `KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，71.7 秒；
- 112 条 `#print axioms` 全部只有 `propext`、`Classical.choice`、`Quot.sound`；
- 30 个源文件哈希固定；
- `verify_cg001_run.py --rerun` 返回 `PASS_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH`。

其中过核的关键定理（`Z0Full.lean`）：`zfcTr`、`zfcTr_HBL2`（D2）、`zfcTr_con_iff`、
`zfcTr_sigma1`、`zfcTr_D3_standard`（正对照）、`zfc_z0_full_of_D3_internalize`（**条件结论**）。

---

## 24 个模块的编译次序（最后一个是要改的）

```
GodelQ/ProcessObservation.lean
GodelQ/EffectiveTheory.lean
GodelQ/GodelZenoRunner.lean
GodelQ/FoundationArith.lean
GodelQ/ZFC/SetLanguage.lean
GodelQ/ZFC/SchemaDelta1.lean
GodelQ/ZFC/ReplacementDelta1.lean
GodelQ/ZFC/ZFCDelta1.lean
GodelQ/ZFC/NumeralCode.lean
GodelQ/ZFC/NeverRE.lean
GodelQ/ZFC/OmegaArith.lean
GodelQ/ZFC/NumeralSemantics.lean
GodelQ/ZFC/ArithInterp.lean
GodelQ/ZFC/R0Model.lean
GodelQ/ZFC/Effective.lean
GodelQ/ZFC/Soundness.lean
GodelQ/ZFC/OmegaLaws.lean
GodelQ/ZFC/PAModel.lean
GodelQ/ZFC/Z0Shadow.lean
GodelQ/ZFC/Z0PA.lean
GodelQ/ZFC/ShRE.lean
GodelQ/ZFC/InternalTranslate.lean
GodelQ/ZFC/TranslateRE.lean
GodelQ/ZFC/Z0Full.lean
GodelQ/ZFC/Z0Blocked.lean
```
