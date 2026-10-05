# C5F 外部原典快照：混合系统中的 Zeno 执行与模型完整性（2026-10-05）

> **身份：** `SOURCE_SNAPSHOT_MANIFEST / C5F_INPUT / POSITIVE_COMPARISON_CONTROL / NOT_A_BARE_ZFC_VERDICT`。

| 文件 | 原始 URL／身份 | SHA-256 | C5F 用途 |
|---|---|---|---|
| `Berkeley-EECS-2006-114.html` | UC Berkeley EECS technical-report landing page, Zheng 2006 | `c04ede9683eca12097f5b0b9365248c3d84c37102d0dbc03b60a03c69bb777b6` | 官方元数据与摘要：Zeno execution、model incomplete、post-Zeno completion。 |
| `Zheng-Simulating-Zeno-Hybrid-Systems.pdf` | `https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/Archive/EECS-2006-114.pdf` | `e43e78fdeee8da2e5657d11a9bad07f9aed4f0c6b33398795689df74712d0771` | 一手技术报告：定义、物理系统／抽象、simulation halt、post-Zeno states和模型补全。 |
| `Zheng-Simulating-Zeno-Hybrid-Systems.txt` | 上一 PDF 的本地 `pdftotext -layout` 阅读派生物，不是独立来源 | `3bb068accc5b5f8d917b347f8622bec32b7636af5ce74dd56359adae13a54c48` | 稳定定位 PDF 阅读段落；原始权威仍是 PDF。 |

## 严格边界

- 此 source 的 Zeno execution 是 hybrid system 中“有限时间内无限个**离散 transition**”；它不能自动等同于 IEP Standard Solution 下连续 runner 的 subpath／action 读法。
- 它给出的是 process-sensitive modeling 的正控制：Zeno behavior 可被诊断为 abstraction-induced model incompleteness并通过 post-Zeno state扩展处理；它不是 ZFC 的形式化或 ZFC 的反例。
- 不从它推出物理时空离散、标准实分析错误、或本项目用户圆环任务已经解决。
