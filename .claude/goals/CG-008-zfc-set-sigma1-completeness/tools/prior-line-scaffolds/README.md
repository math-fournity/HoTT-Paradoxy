# 先前工作线的试验脚手架（从 /tmp 抢救）

> 2026-10-11 从 `/tmp` 保存。逐字节与原文件一致（保存时逐个 `cmp` 核对过）。
> **这些不是本目标包的产物**，而是 D3 攻坚线（2026-10-09 至 10-11）留下的试验脚手架。
> 保存理由：它们记录了「怎么把 𝗭𝗙𝗖 包编译起来、怎么批量探针、怎么生成记录」，
> 对任何继续做 CG-008 的人都有复现价值；留在 `/tmp` 会被系统清理。

## 文件

| 文件 | 来源 | 用途 |
|---|---|---|
| `compile_deps.sh` | `/tmp/z0work/` | 把 24 个依赖模块一次性编译进持久构建目录 |
| `iter.sh` | `/tmp/z0work/` | 迭代构建 |
| `probe.py` | `/tmp/z0probe/` | 单文件探针驱动（读 `/tmp/z0probe/<name>.lean`，用固定 `LEAN_PATH` 编译） |
| `LEANPATH` | `/tmp/z0probe/` | 当时用的 `LEAN_PATH` 快照 |
| `claim.py` | `/tmp/z0probe/gen/` | 生成 `CLAIM.md` 片段 |
| `neg.py` | `/tmp/z0probe/gen/` | 生成负控制 |
| `handoff.py` | `/tmp/z0probe/gen/` | 生成交接文档 |

## 注意

- 这些脚本里的路径是**当时**的（指向 `/tmp/z0d3mod`、`/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/`、
  elan 工具链路径）。**不要直接运行**；当作「当时怎么做的」的记录来读。
- 本目标包自己的驱动是上一级的 `build_z0.py`（从 `/tmp/build_z0.py` 抢救，用于本 worktree）。
- 未抢救：`/tmp/z0probe/` 下 263 个两字母命名的 `#check` 刮擦探针（一次性试验，无独立价值）；
  `/tmp/z0d3mod/`（9.6 MB，同一线的重建工程，可由上述脚本重放）；
  `/tmp/z0_build_lib/`（构建缓存，可再生）。
