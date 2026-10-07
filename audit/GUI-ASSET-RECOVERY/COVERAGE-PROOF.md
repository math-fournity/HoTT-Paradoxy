# D1 · 覆盖证明：八份 GUI 导出全行覆盖阅读战役

> SOP：`GUI-EXPORT-ASSET-RECOVERY-SOP` ｜ 执行者：ZCode（GLM-5.3）新会话（R-4）｜ 完成日：2026-10-07
> 机器裁判：`python3 -B scripts/audit/verify_gui_line_coverage.py --final` → **OVERALL: PASS, remainder=0（终期模式：含抽样引文比对）**（完整输出原文见 §5）
> 抽样种子（冻结于 manifest）：`acada769e45a3487…`（sha256("GUI-ASSET-RECOVERY-v1"+八文件排序哈希拼接)）

## 1. 总账

- 语料总量 **T = 126,503 行**（八文件，`split(b'\n')` 计）；去重后义务行 **D = 26,786**；SHARED 指针行 = 99,717。
- 归类结果：**covered = 26,786，remainder = 0**。每行要么在 READ 收据区间内（义务行），要么属于与已读区间逐字节相同、由 manifest 指针覆盖的 SHARED 区间。
- 收据账本 `ledger.jsonl`（append-only）：READ 717 条 + RELOAD 144 条（G4 终期重载）+ 元条目（SESSION_START/FILE_DONE/CHECKPOINT/CORRECTION/PROTOCOL_NOTE/RESUME）41 条。两条无效 span 收据（R0650/R0690）由 CORRECTION `voids` 机制按 003§3 纠错语义失效（PROTOCOL_NOTE 已登记），由替位收据覆盖正确区间。

## 2. 每文件表（总行 / SHARED / 义务(UNIQUE) / READ 收据 / RELOAD 收据 / 合计）

| 文件 | 总行 | SHARED | 义务行 | READ | RELOAD | 合计 |
|---|---|---|---|---|---|---|
| dev-08 | 18458 | 0 | 18458 | 32 | 17 | 49 |
| dev-03 | 13602 | 11372 | 2230 | 104 | 15 | 119 |
| dev-04 | 13784 | 12653 | 1131 | 86 | 19 | 105 |
| dev-02 | 14194 | 13413 | 781 | 78 | 17 | 95 |
| dev-06 | 15468 | 14829 | 639 | 58 | 19 | 77 |
| dev-07 | 15138 | 14820 | 318 | 39 | 18 | 57 |
| dev-01 | 17161 | 16019 | 1142 | 105 | 20 | 125 |
| dev-09 | 18698 | 16611 | 2087 | 215 | 19 | 234 |
## 3. G4 确定性抽样引文核验（每文件 K=20，种子冻结）

抽样方法（002§2.3/004§1，完全确定性）：对文件 f 的每行 i 计算 `h = sha256(seed + f + ":" + str(i))`，按 h 十六进制升序取前 20 行。样本清单与完整引文形式（逐字或前200字符+总长+整行SHA-256前16位）冻结于 `samples.json`；逐字/截断引文表见 `G4-QUOTES.md`（160 行，机器生成，验证脚本按同一规则重算比对）。

写作前已按 005§4 对照表对每条抽样行所在窗口执行 RELOAD（144 窗，收据 RL0733-RL0876，每窗=样本行±5 聚类），引文出自当前上下文原文。

## 4. G4b 全文件 token 覆盖复跑（003§9.7）

每文件全文件扫描（含 SHARED）的判词/门规格 token 检查结果——所有缺失 token 逐 token 定位核实**全部仅出现于 SHARED 区间（义务行残留=0）**，按 003§5「SHARED 指针已覆盖」豁免（各文件笔记已登记；dev-08 义务行占比 100% 故缺失=0）：

```text
dev-01: 全文件token类=341 缺失=42 仅SHARED=42 义务行残留=0
dev-02: 全文件token类=314 缺失=42 仅SHARED=42 义务行残留=0
dev-03: 全文件token类=308 缺失=3 仅SHARED=3 义务行残留=0
dev-04: 全文件token类=304 缺失=42 仅SHARED=42 义务行残留=0
dev-06: 全文件token类=340 缺失=45 仅SHARED=45 义务行残留=0
dev-07: 全文件token类=328 缺失=45 仅SHARED=45 义务行残留=0
dev-08: 全文件token类=354 缺失=0 仅SHARED=0 义务行残留=0
dev-09: 全文件token类=353 缺失=41 仅SHARED=41 义务行残留=0```

## 5. 验证脚本完整输出原文（--final 终期模式；不裁剪；VOIDED 行为 CORRECTION 失效说明）

```text
[PASS] 1_identity — T=126503 D=26786 seed=acada769e45a3487
[PASS] 2_alignment_replay — shared_bytes_verified=99717 lines
  VOIDED by CORRECTION: R0650 dev-09:17928-17928
  VOIDED by CORRECTION: R0690 dev-09:18435-18610
[PASS] 3_receipt_hash
[PASS] 3b_receipt_span
[PASS] 3c_ledger_meta — read=715 reload=144 meta=41
[PASS] 4_coverage_final — D=26786 covered=26786 remainder=0
    dev-08  unique= 18458 covered= 18458 remainder=    0 receipts= 49
    dev-03  unique=  2230 covered=  2230 remainder=    0 receipts=119
    dev-04  unique=  1131 covered=  1131 remainder=    0 receipts=105
    dev-02  unique=   781 covered=   781 remainder=    0 receipts= 95
    dev-06  unique=   639 covered=   639 remainder=    0 receipts= 77
    dev-07  unique=   318 covered=   318 remainder=    0 receipts= 57
    dev-01  unique=  1142 covered=  1142 remainder=    0 receipts=125
    dev-09  unique=  2087 covered=  2087 remainder=    0 receipts=232
[PASS] 5_sample_quotes — k=20/file seed frozen

OVERALL: PASS  (coverage.json written; remainder=0; FINAL 要求 remainder=0)
```

## 6. 诚实边界声明

本证明给出的是 001 片 C3 定义的可审计代理：冻结身份 + diff 式区间对齐重放 + 逐收据字节切片哈希 + 行号锚定分层笔记 + 确定性抽样引文 + token 覆盖自查。**"主观阅读体验"不在可证范围内**；审计者可按 005 片 §6 清单以自己的新鲜种子做反向质询与独立复跑。执行期间发生的全部偏差与修复（漏收据补录、class_counts 更正、区间11 补录、尾部截断补齐、R0650/R0690 voids）均以 CORRECTION/PROTOCOL_NOTE 留痕于 ledger.jsonl，未改写任何既有收据。
