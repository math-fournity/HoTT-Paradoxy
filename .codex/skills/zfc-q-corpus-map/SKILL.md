---
name: zfc-q-corpus-map
description: "Build a traceable corpus of literature relevant to discovering ZFC Q: acquire and verify PDFs, derive MinerU reading text, map bibliography and citations, and route only qualified leads into Q analysis when the user invokes ZFC-Q-CORPUS-MAP-SOP."
metadata:
  version: "1.0.0"
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
4. 对已验证且本 batch 需要处理的 PDF，使用本地 MinerU。原 PDF 是权威，MinerU Markdown/JSON 只是派生阅读材料；记录命令、版本、输入哈希、输出路径、覆盖页和失败。
5. 在 bibliography、citation和coverage map登记 work family、版本关系、backward／forward trace、筛选和余项。
6. 只有来源经 R/Z/Q/E、same-task、source payment和模式 P 资格化后，才从 Q LeadCard 进入 HOTT-MOTIVE-ZFC、P-FORGE或其他专门候选工作；地图本身不启动P-DAG。

## 获取和 MinerU 的不可跳过规则

- arXiv、作者／机构、出版社／会议正式页、DOI resolver和用户浏览器访问路线可以用于 acquisition；下载路径不是书目或内容权威。
- 用户提供的 `sci-hub.jp` 等访问线索只记在 AcquisitionCard 的 access provenance。PDF 仍须与 DOI／作者／题名／页码和原文版本核验；不能把该路径写成一手学术来源或以它绕过版本审计。
- MinerU使用本机既有 runtime；不安装模型、不改变服务、不上传到远程。解析失败、质量层不可用或原件不清晰时记录具体边界，不能静默换工具或把派生文本抬升为原文。

## 完成边界

一个 batch 只有在其 declared work families 都有 acquisition／unavailable处置、已得PDF通过身份核验、要求的MinerU派生完成或有失败记录、地图与余项更新、每个Q lead有资格状态时才可称 COMPLETE_WITH_SCOPE。它不证明所有相关文献已尽、也不证明没有ZFC Q。
