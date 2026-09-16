# D - PSJ 验收阈值增补

> 对应 GPT 原片：`../GPT的方案/HoTT机器统观后续工作方案/004 - PSJ提升来源与HoTT必要性判决.md` §6。
> 修改性质：为 PromotionSource 七层分母钉死"source-grounded vs synthetic"的最小验收阈值。

## D1. 阈值钉死

004 片 §6 给了七层分母顺序，但未钉死"多强的来源算 source-grounded"。本增补要求 PSJ 在
冻结 comparison pool 的同时，**冻结一条最小验收阈值**：

一个来源只有**同时满足以下三条**才可标 `SOURCE_GROUNDED_PROMOTION_SOURCE`：

1. **先在性**：该来源先于本项目候选存在（可引用时点、版本、commit/页码）；
2. **可引用三要素**：该来源显式给出 input、observation、completion（或其可提取等价物）；
3. **非本项目/本项目 AI 生成**：来源不是本项目生成的 synthetic translation，也不是本项目
   AI 的自述。

不满足任一者 → 降为 `SYNTHETIC_CALIBRATION_CONSUMER` 或 `RESEARCHER_SUPPLIED_INTERPRETATION`，
不能进入 A1 的 PromotionSource 环节。

## D2. 与七层分母的关系

七层分母（理论规则 → 论文 → 库 API → proof assistant/编译器 → 应用合同 → 用户解释 →
synthetic）保留为**搜索顺序**；阈值 D1 是**验收闸**。第 5 层（外部应用合同）与第 6 层（用户
解释）必须额外通过 D1.3（非本项目 AI 生成），且第 6 层进入 A1 前需所有者对"用户解释是否
构成自然 consumer"作裁定（延续 010 片 §11 仅用户可裁定事项）。

## D3. 防"口味分派"复发

九轮互审三次重演过"审查者口味分派"风险（GLM-3 W3 预警、GPT-3 操作化、阈值仍未定）。阈值
D1 是可机械核对的（先在时点、三要素、非本项目），可消除大部分自由裁量。

## D4. 采纳判据

- [ ] PSJ TaskSpec 含冻结的 D1 阈值；
- [ ] 每个候选的 PromotionSource 判定附 D1 三要素的逐项证据定位。
