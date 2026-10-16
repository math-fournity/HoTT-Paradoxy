# S-RES-20260913-MACHINE-OVERVIEW-M4-L3

- **目标**：在隔离 worktree 中执行 M4-lite 三任务同预算评测，并对第一条 L3 obstruction 的 natural-use bridge 做冻结七源审计；产出能够决定升级、收口或返修搜索方法的证据包。
- **授权与边界**：用户在审阅上一轮提交与下一步说明后明确说“开始”。本轮只写 `/Volumes/D/HoTT-machine-overview` 的 `feat/machine-overview-m1`；起始 HEAD `1aa1a6e32c0f59459f79ebc76f74e8f2b5be97a5`。未 merge、tag、push、写 main 或应用 main-line checkpoint；commit 尚未授权。
- **认知闭包**：沿用并复核 generation-4/36-KC 四件套、research profile、机器统观方案 M4/M3 原始验收、strict-v2/L3 handoff、0.2.0 代码/运行实物与当前 Git 边界。主工作树已由另一 AI 前进，故继续保持 worktree 隔离。
- **冻结**：`M4-LITE-L3-001/PROTOCOL.json` 先固定三任务角色、ACCEPT/ACCEPT/REJECT gold、时间双坐标、三模式、预算和禁外推；`DESIGN-FREEZE.json` 在七个未来输入均不存在时核对 `search.py` 与 `025938a…` blob 同 hash、46 tests PASS，并冻结 native adapters。冻结后 search/adapter 未改。
- **实现**：coordinator 0.3.0 新增三个 fail-closed symbolic native renderer、四种 observation/mechanism 对应分类、原生失败报告；新增 `m4_eval.py`、`L3M4Support.agda`、共享 profile、三 TaskSpec/grammar/case 链；`search.py` 字节未变。
- **M4 原生结果**：Path 正例与显式事件正例均为 0/0/42(expected)/0 exact replay；finite-to-exact 候选为 main 42 / controls 0 / negative 42 / failed-main replay 42，status `NATIVE_CHECK_FAILED`，没有升级。
- **M4 比较**：full enumeration 194 checks，same-designer LLM subset 41，hybrid feedback 46；三模式各 3/3 冻结决策正确、0 false promotion；hybrid 删除被拒 exact-lift 规则后目标候选为 0。deterministic digest `199793e000ba3de879d0f85c225b20b876775ccfa34f5abac9829004c8a90028`。由于同一 AI 设计任务/规则，结论严格限为 descriptive M4-lite。
- **自然使用审计**：冻结 HoTT Book、Agda 2.8.0 manual、Cubical v0.9 全 1,111 文件树、Cubical Agda、GCTT v2、CCTT v3、Directed HoTT v1。remote bytes 与 page text 位于 repo 外 cache，manifest 固定 hash；inventory deterministic digest `89972826f625e03a303d8de2985319dee7a5c9c44cd1e32bccc1039324aa81e5`。
- **审计判词**：7/7 来源、42/42 E1–E6 cells 完成、0 hit。HoTT Book 的 time analogy、GCTT unfolding interval、Directed HoTT execution path 均保留为 strongest counter-reading；仍分别由 pure homotopy caveat、later/ω 和新增 directed `hom` 结构阻止命中。判词 `BOUNDED_NEGATIVE_COMPLETE / L3_CANDIDATE_NOT_UPGRADED / REPRESENTATION_BOUNDARY / DEFENSE_WORKS_IN_SCOPE`，禁止外推全球不存在。
- **失败与纠正**：native adapter 冻结前探针发现 event Target 缺 product import并修复；一次含 `rm` 的 `/tmp` 探针命令被主机策略拒绝且无副作用；NC-02 frozen URL 的 `cubical.rst` 返回 404，独立 correction receipt 按同 commit tree 修正为 `cubical.lagda.rst`；系统无 `pdftotext`，改用固定 bundled Python 3.12.14/pypdf 6.10.0；natural-audit tests 先后发现 import path 与函数名错误并在生成 inventory 前修复。
- **验证**：49/49 tests PASS；workspace `VALID`（8 case revisions / 23 runs / 10 reviews / 0 errors / 1 registered interrupted legacy attempt）；M4 replay PASS；natural inventory replay PASS；191 JSON parse PASS；42-cell decision integrity PASS；diff check PASS。
- **治理写回**：更新 worktree-local README、registry、handoff、M4 report、natural audit owners与本 Session；不更新 revision-118 STATE/方向/全景/claim matrix。新数学 claim 为 0；正式主线投影留给 M5 集成。
- **Git 状态**：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；全部 `dev-notes/` 明确排除在实现变更之外。
