# 编译与收据命令

## A. 增量编译（开发期）

工具：`.claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py`
（去掉 sandbox-exec 的本地变体；正式收据仍用包内冻结的 zfc_lean_check.py）。

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full
python3 -B .claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py \
    $PKG GodelQ/ZFC/ShCraigElimNegLaw.lean
```
看 `exit code`；0 即通过，非 0 看 stdout/stderr 的报错行。缓存同目录 `devbuild_ns/godel-q-zfc-z0-full/`。

## B. 依赖顺序（编译单个文件前先编其 import 闭包）

Z0Full → SeqTranslate → SeqTranslateFormula → NegInvolution* → 你的新文件。
（`*` 号文件含 sorryAx，与本任务无关，编译它们只是因为它们在被依赖链里；不要把它们当源。）

## C. 正式收据（F-011）

```bash
python3 -B .claude/goals/CG-007-formalization-completion/tools/capture_run.py \
    --package HoTT/formal/claude-cg001/godel-q-zfc-z0-full \
    --run-id 2026MMDD-CG001-Z0-SHCRAIGELIM-01 \
    --proof-id MP-CG001-Z0-SHCRAIGELIM-001 \
    --claim-id CG001-C-NNN --expect ACCEPT \
    --source GodelQ/ZFC/Z0Full.lean --source GodelQ/ZFC/ShCraigElimNegLaw.lean \
    --source GodelQ/ZFC/ShCraigElim.lean \
    --scope "..."
```
然后用 `verify_cg001_run.py --rerun` 精确重放一致。注意：**含 sorry 的文件不能进收据源**
（zfc_lean_check.py 纯文本扫描未证标记会拒收）。

## D. 陷阱

- 中文注释里出现未证标记的英文词也会被驱动判为 FORBIDDEN_SOURCE_MARKER；写注释避开。
- 用 Python 写 .lean 比 zsh heredoc 稳（中文转义）。
- `#print axioms` 必须只剩 propext / Classical.choice / Quot.sound。
