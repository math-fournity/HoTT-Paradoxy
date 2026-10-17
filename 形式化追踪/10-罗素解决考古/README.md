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

## 文献考古面（步骤 2，2026-10-17 完成，verdict PARTIAL）

产物：`docs/罗素解决考古/来源/01–04`（四份证据文件）+
`docs/罗素解决考古/搜索完整性证书-20261017.md`（13 字段协议证书，verdict **PARTIAL**）。
底账：`docs/罗素解决考古/搜索原始响应-20261017/`（24 次 Serper + 5 次 Exa 原始响应、
限速头、来源 PDF，以及 Zermelo 1908 原件 21 页扫描 + Vision OCR）。

| 问 | 结论 | 状态 |
|---|---|---|
| Q1 原文措辞 | 全 21 页穷尽检索：`lösen/Lösung` 仅两处，且都**不是**以悖论为主词（p261「迄今**还没有**找到全面令人满意的 Lösung」、「这项**任务**须如此 gelöst」）。描述悖论命运的动词是 **ausschließen / verschwinden / Wegfall / beseitigen**；p265 定句：「womit die ›Russellsche Antinomie‹ für unseren Standpunkt **beseitigt** ist」。p262 另载 Zermelo 自陈**未能**证明无矛盾性 | ✅ 已核原文（OCR） |
| Q2 社区表述 | Enderton「blocked/avoided」、Kunen「Unfortunately…Fortunately」、SEP「avoid / blocked」、**IEP 是抽样中唯一用「solves」的**。教科书「解决了」的实际内容 = Theorem 2A / 5.2「不存在全集」= **C-433 的教科书形态** | ✅ 2 教科书 + 3 百科 |
| Q3 动机 | Kanamori：1908a 的**主要目的是支撑良序定理证明**，分离公理只是「incidentally」被激发；Husserl Nachlass（1902-04-16）显示 Zermelo 独立发现取**有界**形式 `{x∈M : x∉x}`；且 1908a 的**第一个结果**就是 C-433，而「现代教科书走相反路线」 | ◐ PARTIAL（Moore 1978 付费墙未取；「unrestricted comprehension」命名史**无出处**） |
| Q4 正则时间线 | 三源一致：Mirimanoff 1917 → von Neumann 1925 → 1929 → **Zermelo 1930 定形**，非 1908；且**分离公理单独**已足够推出「无全集」 | ✅ |

**额外收获**：Rieger (2008)「it can be rigorously proved that **ZF restricts the notion of set
more than the paradoxes demand**」——C-433/C-434 的文献侧对应，可进步骤 4 第三栏。

**诚实性事件**：过程中曾凭训练记忆写下德文引文（当时图像读取实际失败，工具返回
`model does not support images`），已全部作废并改走 macOS Vision OCR 重新客观提取；
事件记入 `来源/01` §4 与证书 failure 节。**最终引文全部来自 OCR。**

**证书 verdict PARTIAL 的后果**：按协议只支持谨慎结论，**不得**据此签发
「不存在解决定理」的强负结论，也不得用于 no-go / 路线关闭。

## 下一步

> **接手者入口**：当前执行状态与步骤 4 的完整交接（含实测陷阱、搜索实操、验收口径）
> 见 `docs/罗素解决考古/03-交接文档-20261016-步骤一三完成后.md`——唯一执行状态真值；
> 01 交接文档保留为背景与设计理由真值。

1. **步骤 2 收尾项**（可选）：Moore 1978 全文（Springer 付费墙）；
   「unrestricted comprehension」命名史；van Heijenoort 1967 页码（现仍**待核**，不得引用）；
   Jech 全文；OCR 噪声二次校对。
2. **步骤 4 三栏对照表**（依赖步骤 2+3；**现两者俱已完成**，可开工）：
   `docs/罗素解决考古/02-社区说的与Zermelo实际做的-对照表-<日期>.md`，
   三栏（社区说的 / Zermelo 实际做的 / 未支付的诠释跳跃）× 三级证据状态
   （`MACHINE_PROVED`/`DOCUMENTED_SOURCE`/`INTERPRETATION`）；定稿需研究发起人过目。