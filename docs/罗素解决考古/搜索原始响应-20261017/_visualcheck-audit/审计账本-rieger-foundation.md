# 审计账本：rieger-foundation（二值化页图，2026-10-17）

## 0. 批次身份

- **对应 MinerU markdown**：`mineru_md/rieger-foundation.md`（单份，页码 1–23）。
- **源 PDF**：`搜索原始响应-20261017/rieger-foundation.pdf`（A4，595×842 pts）。
- **产物目录**：`_audit-binary/rieger-foundation/`，`page-001.png` 起，页码统一 3 位。
- **转换执行**：ConvertAgent-B，2026-10-17（开始 07:00:30 -0400），工作根 `/Volumes/D/HoTT_AI_HANDOFF_20260911`（dev）。

## 1. 定参引用（探针定参，全项目统一，不得更改）

- 渲染分辨率：**`-r 300`**。
- 管线（两步）：`pdftoppm -png -gray -r 300`（抗锯齿灰度渲染）→ `magick -threshold 50% -strip -define png:bit-depth=1 -compress zip`（二值化 + 真 1-bit PNG zip 压缩）。
- 不用 `-mono` 直出（8-bit 存储致 4 MB+/页）；不加 `compression-strategy`（实测反而变大）。
- 依据：`_visualcheck-audit/探针定参记录.md`（已提交 2e7fcd88），§5 最终定参。

## 2. 转换与自检

- **转换时间**：2026-10-17 07:00:30 -0400（批内逐页循环，每份 PDF 一批）。
- **源 PDF 页数（pdfinfo）**：23。
- **产物页数自检**：23 个 `page-*.png` 文件，`ls | wc -l` = 23 = pdfinfo Pages。✅ **PASS，无缺失无缺页**。
- **位深自检**（抽查 page-012 IHDR 字节偏移 24）：`01` = 真 1-bit，灰度色彩类型。✅
- **抽查清晰度**（analyzeImage，page-012 裁剪局部 2481×1600，两次调用一致）：正文清晰可读（抄录验证成功：Russell VCP II 原则与 Gödel [1944] 讨论段），笔画无断裂无粘连，上标（²⁰/²¹）与脚注完整。✅ **达标**。

## 3. 逐页 SHA-256（前 16 位）

| 页 | SHA-256（前 16 位） |
|---|---|
| page-001 | `6f5f78342a67188d` |
| page-002 | `3f6f182c761b0202` |
| page-003 | `f1ab9977ecba385e` |
| page-004 | `ba03801c0b46909f` |
| page-005 | `ed3e2399590495dc` |
| page-006 | `d1b746b6447823ca` |
| page-007 | `4c4a866717942fa1` |
| page-008 | `dbb2a702fd83d0be` |
| page-009 | `c69d0680c0f0a3fb` |
| page-010 | `b9ab56a2fa9bfebc` |
| page-011 | `dc814cc29389f14f` |
| page-012 | `5e1a14abac1fa0f7` |
| page-013 | `a3d1ad1b74cfd042` |
| page-014 | `ac4334fa680e97bf` |
| page-015 | `382d3afc8b7fa945` |
| page-016 | `5e090f9bc5e2f4eb` |
| page-017 | `a458200ba4531470` |
| page-018 | `9ca227c3705933f7` |
| page-019 | `f171bf1ccc76c2cf` |
| page-020 | `6b1e05eaeb5f2eef` |
| page-021 | `d60fd32525cd3b84` |
| page-022 | `6bd343d2894e64b8` |
| page-023 | `ae20ca64065b0b4c` |

## 4. 逐页结论索引（由审计代理填写）

（本区由审计代理填写：逐页视觉审计结论、问题页标记、与 MinerU markdown 的对照结果。）