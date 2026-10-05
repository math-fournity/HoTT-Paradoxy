# Earman–Norton `Infinite Pains`：F-A physical-continuum source snapshot

> **身份：** `PRIMARY_SOURCE_SNAPSHOT / READ_ONLY_ORIGINAL_PLUS_DERIVED_READING_AID`。
>
> **用途：** `C0R4 / F-A`：检验连续物理模型是否为一个固定 runner/supertask task 支付物理 bridge，或明确给出 task/physical-boundary 条件。

## 原件

| 字段 | 值 |
|---|---|
| 作者 | John Earman；John D. Norton |
| 题名 | *Infinite Pains: The Trouble with Supertasks* |
| 发表身份 | 收入 A. Morton 与 S. Stich 编 *Benacerraf and his Critics* (1996), pp. 231–261；作者页面列出相同题录。 |
| 获取 URL | `https://sites.pitt.edu/~jearman/EarmanNorton1996a.pdf` |
| 抓取日期 | 2026-10-05；`curl --fail --location` |
| PDF | `Earman-Norton-1996-Infinite-Pains.pdf`；17 页；SHA-256 `573cd7fc1c78390faafefcbaa65498ccc3dd36dbbf129727f5dc781980fd8fb8` |
| PDF 检查 | `file` = PDF 1.3；`pdfinfo` = 17 pages；printed pp. 232–237分别对应 PDF pp. 2–4 的连续段落。 |

## 派生阅读材料

| 文件 | 身份 | 校验／边界 |
|---|---|---|
| `Earman-Norton-1996-Infinite-Pains.txt` | `FAILED_TEXT_LAYER_RECORD` | `pdftotext` 仅产出17 bytes，不能作阅读依据。 |
| `mineru-basic/Earman-Norton-1996-Infinite-Pains.md` | `DERIVED_OCR_READING_AID` | MinerU 4.0.8 local/basic、17 页、OCR；不是原文权威。其内容须由原PDF页图复核。 |

本轮对 PDF pp. 2–4（printed pp. 232–237）完成 Poppler 视觉核验，确认 OCR 所用的下列关键段落和分页：

1. §2 明说 standard resolution 接受跑者的无限子行程，却认为这本身不阻止完成旅程；并区分“没有可指定的最后 act”和“不能完成全部 acts”。
2. §2/printed p.234 构造有连续速度/加速度的 staccato runner，并说在假设某个 Newtonian world 的 `F(t)=ma(t)` 时，Newton laws 保证该 runner 完成 supertask；随后将该结论限定为相对于 Newtonian mechanics 无内部矛盾的 consistency result。
3. §3/printed p.236 以理想化 bouncing ball 为例，明确写出有限几何级数与“infinite bounces in finite time”，同时强调实际球体不会如此、主张只是存在一致的可能 setting。

这些内容由后续 C0R4 card 逐字段解释；不得从本 README 直接推出 bare ZFC、actual physical world 或 Zeno–HoTT 的结论。
