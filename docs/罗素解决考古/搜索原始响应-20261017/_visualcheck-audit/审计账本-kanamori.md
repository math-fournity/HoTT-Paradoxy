# 审计账本：kanamori（二值化页图，2026-10-17）

## 0. 批次身份

- **对应 MinerU markdown**：`mineru_md/kanamori.md`（单份，页码 1–32）。
- **源 PDF**：`搜索原始响应-20261017/kanamori.pdf`（595×842 pts）。
- **产物目录**：`_audit-binary/kanamori/`，`page-001.png` 起，页码统一 3 位。
- **转换执行**：ConvertAgent-B，2026-10-17（开始 07:04:43 -0400），工作根 `/Volumes/D/HoTT_AI_HANDOFF_20260911`（dev）。

## 1. 定参引用（探针定参，全项目统一，不得更改）

- 渲染分辨率：**`-r 300`**。
- 管线（两步）：`pdftoppm -png -gray -r 300`（抗锯齿灰度渲染）→ `magick -threshold 50% -strip -define png:bit-depth=1 -compress zip`（二值化 + 真 1-bit PNG zip 压缩）。
- 不用 `-mono` 直出（8-bit 存储致 4 MB+/页）；不加 `compression-strategy`（实测反而变大）。
- 依据：`_visualcheck-audit/探针定参记录.md`（已提交 2e7fcd88），§5 最终定参。

## 2. 转换与自检

- **转换时间**：2026-10-17 07:04:43 -0400（批内逐页循环，每份 PDF 一批）。
- **源 PDF 页数（pdfinfo）**：32。
- **产物页数自检**：32 个 `page-*.png` 文件，`ls | wc -l` = 32 = pdfinfo Pages。✅ **PASS，无缺失无缺页**。
- **位深自检**（抽查 page-016 IHDR 字节偏移 24）：`01` = 真 1-bit，灰度色彩类型。✅
- **抽查清晰度**（analyzeImage，page-016 裁剪局部 1925×1600，两次调用一致）：正文清晰可读（抄录验证成功：Burali-Forti Paradox 与 Russell [1903]/[1906] 讨论段），逻辑公式（∀u(∀x(x∈u→φ(x))→...)）与特殊符号（∀/∃/∈/∉/φ）可辨认，笔画无断裂无粘连。✅ **达标**。

## 3. 逐页 SHA-256（前 16 位）

| 页 | SHA-256（前 16 位） |
|---|---|
| page-001 | `e0f3a6716e6ec85d` |
| page-002 | `df9ef83b373227f5` |
| page-003 | `4893297ceaacc860` |
| page-004 | `3a97f7fb92818f91` |
| page-005 | `99d1f3e61c55509c` |
| page-006 | `f48efdc9fb2bcde4` |
| page-007 | `2e6098c5fd5a10df` |
| page-008 | `46edde839ee03cc4` |
| page-009 | `9dab78e4662d1b8f` |
| page-010 | `50a043f795886999` |
| page-011 | `c845d1a301187b55` |
| page-012 | `bb6f074833e83eae` |
| page-013 | `6f759774d816e2a4` |
| page-014 | `29c59b2d070ff77f` |
| page-015 | `c25a73589918ba65` |
| page-016 | `780a7efcff6485b8` |
| page-017 | `084a4fd6e1d1a7f4` |
| page-018 | `5fe3c371aedb4ada` |
| page-019 | `bcf2d580631b3ba8` |
| page-020 | `cd7893882a7e1f25` |
| page-021 | `ffce12690d6f49be` |
| page-022 | `c5a71e596d6729be` |
| page-023 | `1fc961150b81bcc3` |
| page-024 | `ed6788929c39f609` |
| page-025 | `24fa392a289cc4af` |
| page-026 | `01cddfaf4ea634f4` |
| page-027 | `5ba38a045f9340c2` |
| page-028 | `db6266b80dcbd29f` |
| page-029 | `c0cbca275eb892c3` |
| page-030 | `ec8c323985a3a96c` |
| page-031 | `1bde2949da714705` |
| page-032 | `609d1bf87129addc` |

## 4. 逐页结论索引（由审计代理填写）

（本区由审计代理填写：逐页视觉审计结论、问题页标记、与 MinerU markdown 的对照结果。）