# 编译

## 一次性准备

把骨架文件放到项目包的对应位置（本 repo 工作根 `/Volumes/D/HoTT_AI_HANDOFF_20260911`
或你自己的检出）：

```bash
PKG=<repo>/HoTT/formal/claude-cg001/godel-q-zfc-z0-full
cp Z0D3Skeleton.lean $PKG/GodelQ/ZFC/
```

## 迭代编译（快，全链约 60 秒）

需要 `devbuild.py`（`.claude/goals/CG-007-formalization-completion/tools/` 之外的历史 scratchpad
`/tmp/d3build/devbuild.py`，约 30 行；若不在，我这里附一份同功能的最小版 `05-源码/devbuild_min.py`）。

```bash
python3 -B devbuild.py $PKG \
  GodelQ/ProcessObservation.lean GodelQ/EffectiveTheory.lean GodelQ/GodelZenoRunner.lean \
  GodelQ/FoundationArith.lean GodelQ/ZFC/SetLanguage.lean GodelQ/ZFC/SchemaDelta1.lean \
  GodelQ/ZFC/ReplacementDelta1.lean GodelQ/ZFC/ZFCDelta1.lean GodelQ/ZFC/NumeralCode.lean \
  GodelQ/ZFC/NeverRE.lean GodelQ/ZFC/OmegaArith.lean GodelQ/ZFC/NumeralSemantics.lean \
  GodelQ/ZFC/ArithInterp.lean GodelQ/ZFC/R0Model.lean GodelQ/ZFC/Effective.lean \
  GodelQ/ZFC/Soundness.lean GodelQ/ZFC/OmegaLaws.lean GodelQ/ZFC/PAModel.lean \
  GodelQ/ZFC/Z0Shadow.lean GodelQ/ZFC/Z0PA.lean GodelQ/ZFC/ShRE.lean \
  GodelQ/ZFC/InternalTranslate.lean GodelQ/ZFC/TranslateRE.lean GodelQ/ZFC/Z0Full.lean \
  GodelQ/ZFC/Z0D3Skeleton.lean
```

## 正式收据（证完之后）

```bash
cd <repo>
python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_run.py \
  --package HoTT/formal/claude-cg001/godel-q-zfc-z0-full \
  --run-id <RUN_ID> --proof-id <PROOF_ID> \
  --claim-id CG001-C-121 --claim-id CG001-C-122 \
  --expect ACCEPT --scope "..." --non-goal "..."
```

收据工具会**拒绝含 `sorry` 的源**，所以只能在证完之后用。

## 禁止

- 不得把带 `sorry` 的文件列进收据源；
- 不得改 `Z0Full.lean` 的定理类型（已被收据固定）；
- 不得改 Foundation / Mathlib 源码；
- 不得为了通过而加 `axiom`、`native_decide`、`unsafe`、`opaque`、`debug.skipKernelTC`。
