# 归档：/tmp/d3probe 的独有内容（2026-10-10 Codex 会话 01a120e6）

> 2026-10-11 由 CG-009 会话归档。原位置 `/tmp/d3probe/`（用户要求 tmp 不留代码与文档）。
> **只归档了在 git 中找不到副本的部分**；其余（`GodelQ/` 下的包文件、两个 toolchain JSON）
> 均为既有资产的副本，未重复归档。

## 内容

| 文件 | 说明 |
|---|---|
| `FINDINGS.md` | R-新 的最终判定（含 `shCh` 构造成功、`mem_iff` 三行打通、`ProperOn ℕ` 不可证的实测记录） |
| `NOTES.md` | 会话笔记 |
| `probes/Z0L3Probe.lean` | Z0 第 3 层探针 |
| `probes/Z0Delta1Probe.lean` | Δ1 探针 |
| `probes/Z0Delta0Probe.lean` | Δ0 探针 |

## 未归档（有既存副本，已核实）

- `/tmp/d3probe/GodelQ/**`（ProcessObservation、EffectiveTheory、ZFC/* 等）——既有包资产的副本；
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`——toolchain pin，可由 `make_pins.py` 重生成。

## 同时清理的其他 tmp 项（核实后）

| 路径 | 核实结论 |
|---|---|
| `/tmp/headsver/head-version.lean` | 与 `/Volumes/D/HoTT-worktrees/_probe-quarantine/ProbeHeadVersion.lean` 逐字节相同（sha `41935eb3…`） |
| `/tmp/geomtest/*.lean` | 与 `HoTT/formal/claude-cg001/godel-q-geometric-completion/GodelQ/GeometricCompletion.lean` 逐字节相同（sha `d6f8be09…`） |
| `/tmp/d3replay/**` | `Qualification.lean`/`WrongMissingSoundness.lean` 已在 `HoTT/formal/claude-cg001/external-foundation-incompleteness/GodelQ/` |
| `/tmp/d3build/**`（74 MB） | 增量编译缓存 + `devbuild_ns.py` 副本；工具脚本已在各 goal 包内有正式版本 |
| `/tmp/isf2.olean`、`sdz.olean`、`tp3.olean` | 本会话探针的临时 olean 产物 |
