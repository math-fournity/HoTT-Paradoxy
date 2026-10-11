# CG-007 开发探针存档（**不是收据，不是证明资产**）

> 这些 `.lean` 文件是从开发工作副本（原先只在 `/tmp/d3build/src/...`）**原样搬进 Git** 的
> 临时探针。它们的作用是留下"当时用什么接口、试过哪条路、哪条路失败"的字节级痕迹，
> 供下一轮不必重新摸索。
>
> **身份**：`DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM`。
> 它们**不**是任何运行的编译源，**不**进入 `source-manifest.json`，**不**支撑任何数学结论。
> 有的含未证标记（见下表），有的只是 `#check`/`example` 清单。

## 为什么放这里

原先的迭代方式是把包复制到 `/tmp/d3build/src/` 再改，探针也只留在那儿。
`/tmp` 会被系统清理，且不在 Git 里——核心代码或文档的唯一副本留在 `/tmp` 是不可接受的。
项目 `AGENTS.md` 的「形式化与追踪的写入边界」一节现在明确禁止这样做；
本目录是那次整理留下的探针存档。

开发迭代请改用仓库内工具（见 `../tools/README.md`）：

```bash
T=.claude/goals/CG-007-formalization-completion/tools
PKG=HoTT/formal/claude-cg001/godel-q-zfc-z0-full

# 增量编译（缓存在 <repo>/.cg007-build/，已 gitignore）
python3 -B $T/devbuild.py $PKG <按 import 拓扑序的模块…>

# 单文件探针（可 import 已编译模块；探针文件本身放仓库内，别放 /tmp）
python3 -B $T/lean_probe.py $PKG .claude/goals/CG-007-formalization-completion/probes/<name>.lean
```

## 清单

### 早期接口探针（`Probe1`–`Probe6`）

摸清 Foundation 侧可用接口与"看起来能省的路"是否可行。`Probe3` 含未证标记。

### 第 1 层语法交换律探针（`ProbeL1`–`ProbeL16`）

`arithTrln.translate` 与 `neg/⋏/⋎/∀¹/∃¹/rel/nrel` 的交换律摸底；
`ProbeL9`–`ProbeL16` 是 `conjunct`/`shiftVec` 公式性（后成为
`SeqTranslateFormula.lean` 的 `isSemiformula_conjunct`、`isSemitermVec_shiftVec_V`）的探路。
`ProbeL3` 含未证标记。

### 第 2 层公式保持性探针（`ProbeW8a`–`ProbeW8p`、`ProbeW8Neg`）

`iVE` 三条计算规则 → `isSemiformula_iVE` → `domZero`/`iTR` → 主定理 `isSemiformula_iT`
的逐步探路。对应成品是 `GodelQ/ZFC/SeqTranslateFormula.lean`（CG001-C-391，已收据）。
`ProbeW8Neg` 是"把 `iVE` 的 bvar 规则写错"的负控制草稿（正式版是
`GodelQ/ZFC/WrongIVELayer.lean`）。

### 施工图（`SeqTranslateDerivable.lean`）

第二层主定理 `derivable_translateSeq` 的**未编译施工图**：10 个 `Derivation.*` 支的构造子调用
是**猜测**，辅助引理（`translateSeq_isFormulaSet`、`fstIdx_axL` 等）当时不存在。
**不要当既有成果用**；搬进正式包时必须逐条修。

### 开工探针（`W8TranslateProbe.lean`）

第二层开工时的接口清单（`#check` 为主），记录"哪些名字存在、签名是什么"。

## 边界

- 这些文件**不得**加进 `capture_run.py --source`；加了会被驱动拒绝或污染源清单。
- 需要把某个探针的结论变成交付物时，把结论重写进 `HoTT/formal/claude-cg001/<pkg>/` 的正式模块，
  走 `capture_run.py` + `verify_cg001_run.py --rerun` 出收据，而不是引用本目录。
- 含未证标记的探针（`Probe3`、`ProbeL3`）**永远**不能进收据源。
