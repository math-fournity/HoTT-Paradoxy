---
name: zfc-q-corpus-map
description: "Build a traceable corpus of literature relevant to discovering ZFC Q: acquire and verify PDFs, derive MinerU reading text, map bibliography and citations, and route only qualified leads into Q analysis when the user invokes ZFC-Q-CORPUS-MAP-SOP."
metadata:
  version: "1.2.0"
  role: "task-scoped-corpus-research"
  sop_name: "ZFC-Q-CORPUS-MAP-SOP"
---

# ZFC Q 可追溯语料落盘、MinerU 与文献地图

仅当用户明确引用 `ZFC-Q-CORPUS-MAP-SOP`、要求继续该总语料工程，或明确要求其 acquisition、MinerU、地图或Q lead阶段时使用。先完成 repo-cognitive-closure、项目最高指示与四件套，再读取：

- [总语料 SOP](../../../dev-docs/ZFC-Q语料落盘与文献地图SOP.md)
- [项目档案根](../../../audit/ZFC-Q-CORPUS-MAP/README.md)
- [HOTT-MOTIVE-ZFC 档案](../../../audit/HOTT-MOTIVE-ZFC/README.md)，仅作为已存在的 seed／control 支线。

## 目标与边界

目标是为发现 ZFC Q 尽可能完成一个声明范围内的可追溯文献 corpus：作品身份、获取路线、PDF验证、MinerU派生、书目／引文地图、coverage remainder和Q lead 都可复核。不是写博士论文，不要求临床系统综述模板，不以文献数、下载数或地图完成自动声称ZFC Q、ZFC矛盾或数学结论。

“全部”只指冻结并可持续扩展的 corpus 范围；每次必须记录未获得、付费／访问、语言、版本和强引用余项。

## 执行顺序

1. 冻结一个 corpus batch：研究问题、理论位置、seed、数据库／作者／引文入口、语言／时期、纳入排除和停止条件。
2. 建立 WorkCard 与 AcquisitionCard。作品身份先用 DOI、作者、出版社、arXiv、正式会议／项目档案校准；浏览器或用户提供URL只记 access provenance。
3. 用 math-paper-harvest 的原件优先路线取得全文。每个文件执行 PDF身份、页数、题名／文本层和 SHA-256 核验；失败或版本不明保持 unavailable／mismatch。
4. 对已验证且本 batch 需要处理的 PDF，先用 ZCode 同源的 `direct remote standard` MinerU 质量通道。禁止以本地 `basic` 结果作为本项目的阅读或判断依据。保留原始 remote zip、展开的 Markdown/JSON 与身份收据；随后渲染二值化页图，逐页进行视觉核验，并对 Q 相关公式、表格、脚注、定义、量词和出现差异的页面作 300dpi 级复核。**每实际看完一页，必须在打开下一张页图前立即向 `VISUAL-REVIEW.md` 写入该页的审计行；未写入行的视觉印象不能作为证据。**原 PDF 是权威，MinerU Markdown/JSON 只是派生阅读材料。
5. 在 bibliography、citation和coverage map登记 work family、版本关系、backward／forward trace、筛选和余项。
6. 只有来源经 R/Z/Q/E、same-task、source payment和模式 P 资格化后，才从 Q LeadCard 进入 HOTT-MOTIVE-ZFC、P-FORGE或其他专门候选工作；地图本身不启动P-DAG。

## 获取和 MinerU 的不可跳过规则

- arXiv、作者／机构、出版社／会议正式页、DOI resolver和用户浏览器访问路线可以用于 acquisition；下载路径不是书目或内容权威。
- 用户提供的 `sci-hub.jp` 等访问线索只记在 AcquisitionCard 的 access provenance。PDF 仍须与 DOI／作者／题名／页码和原文版本核验；不能把该路径写成一手学术来源或以它绕过版本审计。
- 内建网页检索是公开资料的默认路线。只有某个已冻结 work 的获取确实需要真实页面交互、`test` profile 的持久状态或视觉核验时，才可使用 BrowserOS MCP；每次使用前加载 `browseros-safe-use`，建立自己的 session／标签组，并记录它解决的具体 acquisition gap。BrowserOS 不是一般搜索的替代品，也不用于绕过访问或安全验证。
- MinerU使用本机既有 runtime；研究发起人已授权正常公开学术PDF走 ZCode 同源的 direct remote standard 解析。远程路径不改变本地App daemon或配置；清晰敏感的文件仍须另行确认。远程解析失败时记录失败收据，转入原 PDF 的视觉阅读，不能静默降级到本地 `basic` 或把派生文本抬升为原文。
- 视觉核验的输入、页图、比对范围、结果和高精度证据必须写入 batch 的 `VISUAL-REVIEW.md`。该文件还是**唯一的可恢复视觉游标**：压缩、Session 恢复或交接后，先读取它的当前游标；没有对应页级行、或被标为`RENDERED_UNAUDITED`的图，即使先前曾在对话中看过，也一律视为未审阅并从原 PDF 页图重新开始。被用于判定的页图是可追溯证据，不能只留在临时目录；`VISUAL_PASS±` 或 `SOURCE_PRIORITY` 只描述该派生段的可用性，不构成数学或 ZFC Q 结论。

## 完成边界

一个 batch 只有在其 declared work families 都有 acquisition／unavailable处置、已得PDF通过身份核验、要求的MinerU派生完成或有失败记录、地图与余项更新、每个Q lead有资格状态时才可称 COMPLETE_WITH_SCOPE。它不证明所有相关文献已尽、也不证明没有ZFC Q。
