# 罗素解决考古（2026-10-16 起）

> 「ZFC 解决了罗素悖论」——当初的形式化证明是什么？工作假说（QUESTION 状态）：不存在；
> Zermelo 1908 做的是公理删除/准入层拒绝，「解决」是未经支付的非形式诠释跳跃。
> 工作包批准与四步方案见 `docs/罗素解决考古/01-交接文档-20261016.md`（唯一交接真值）。
> 本章只记进度、缺口与方向；命题全文在各证明包的 `CLAIM.md`，运行收据在
> `HoTT/verification/runs/`。

## 已落地的形式化面（步骤 1+3，2026-10-16）

包：`HoTT/formal/claude-cg001/russell-archaeology/`（`CLAIM.md` 含命题全文与禁止外推）。
四条核心定理与合取定理 `qual_russell_arch` 不依赖任何公理（`#print axioms` 清单为空）。

| 编号 | 层 | 一句话 | 状态 |
|---|---|---|---|
| CG001-C-432 | 对角 | `¬∃ R, ∀ x, x ∈ R ↔ x ∉ x`：纯逻辑，零集合论公理——对角论证是一阶逻辑自身的，不是 ZFC 的贡献 | ✅ run `20261016-CG001-RUSSELL-ARCH-01` |
| CG001-C-433 | 分离 | 分离式成员刻画 ⇒ `R_A ∉ A`：定理而非矛盾（准入层拒绝）；负控制把 C-432 的对角结尾照搬过来被 Lean 拒绝（`R ∉ R` 给不出 `R ∈ A ∧ R ∉ R`） | ✅ run `-01` + `-NEG-01` |
| CG001-C-434 | 正则 | 正则 + 单元素集 ⇒ `∀ x, x ∉ x`：准入禁止（1930 年代第二道门） | ✅ run `-01` |
| CG001-C-435 | 无界概括 | 无界概括（命题形态 hypothesis）⇒ `False`：爆炸的充分条件是被删除的它，不是对角论证 | ✅ run `-01` |

- 位置修正：交接文档原写 `HoTT/formal/russell-archaeology/`，实际落 `claude-cg001/` 下
  （收据工具 `capture_run.py` 的包白名单只接受 `HoTT/formal/claude-cg001/<pkg>`），
  交接文档三处路径已同步修正。
- 考古定位：核心命题用显式自包含前提承载，Foundation 库的 `𝗭`（Schindler 教科书口径，
  含正则公理，与 1908 历史系统不同）只在标注清楚的实例化节作前提提供者。

## 下一步

> **接手者入口**：当前执行状态与步骤 2/4 的完整交接（含实测陷阱、搜索实操、验收口径）
> 见 `docs/罗素解决考古/03-交接文档-20261016-步骤一三完成后.md`——唯一执行状态真值；
> 01 交接文档保留为背景与设计理由真值。

1. **步骤 2 文献考古**（未开工）：四问——Zermelo 1908 原文措辞（ausschließen/lösen，
   必须核原文）；「solved」叙事最早出处（SEP 与教科书）；无界概括命名史与 Zermelo 动机
   （良序定理 vs 悖论）；正则公理 1930s 时间线（von Neumann 1925 / Zermelo 1930）。
   双引擎检索（Serper /search+/scholar + Exa）+ Search Completeness Certificate；
   原始响应落 `docs/罗素解决考古/搜索原始响应-<日期>/`，逐段 hash-pinned 落 `来源/`。
2. **步骤 4 三栏对照表**（依赖步骤 2+3；3 已完成）：
   `docs/罗素解决考古/02-社区说的与Zermelo实际做的-对照表-<日期>.md`，
   三栏（社区说的 / Zermelo 实际做的 / 未支付的诠释跳跃）× 三级证据状态
   （`MACHINE_PROVED`/`DOCUMENTED_SOURCE`/`INTERPRETATION`）；定稿需研究发起人过目。