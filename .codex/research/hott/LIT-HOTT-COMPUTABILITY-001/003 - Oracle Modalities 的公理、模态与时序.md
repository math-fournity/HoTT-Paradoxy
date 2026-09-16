<!-- governance-shard:v2
logical_id: LIT-HOTT-COMPUTABILITY-001
shard_id: 003
index: ../LIT-HOTT-COMPUTABILITY-001.md
-->

# Oracle Modalities 的公理、模态与时序

## HoTT 特有结构确实进入了计算理论

`OracleModality.agda` 不是把经典 Turing machine 名词搬进类型论。它以 nullification／higher modality 形成 oracle-relative universe，定义记录 `_≤T_`，证明 reflexivity、transitivity、many-one implies Turing 等结构；`RelativisedCC.agda` 构造 relativised computable choice 与 Turing jump，`ParallelSearch.agda` 使用 relativised Markov principle，`Continuity.agda` 给出局部有限查询依赖。

这使 `TC-06 Modalities × OP-11 CrossModel × CC-oracle-consumer` 成为真实 HoTT-specific cell。它也与 Post §11 对齐：查询 `queryOracleAndContinue n e` 的 continuation 根据当前 oracle answer 选择后续 code，后问依赖前答；这属于“时序”，不是运动／时空稠密性意义上的“时间”。

## 能力来自哪些显式前提

完整源树审读定位四组 `postulate`：

- `Axioms/NegativeResizing.agda:24–31`：小 classifier `Ω¬¬`、解释与 retraction；
- `Axioms/MarkovInduction.agda:39–43`：`markov-ind`，随后导出 Markov principle 与 unbounded search；
- `Axioms/ComputableChoice.agda:38–40`：step-indexed machine `φ₀` 与唯一 halting time；
- 同文件 `:67–72`：`ComputableChoice`，随后在 `:93–102` 导出 ECT 与 CT。

所以源码通过类型检查时，也只证明“在这些 postulate 作为 trusted inputs 的理论中，后续定理由 kernel 验证”；它不证明这些原则在 ambient Cubical HoTT 中成立。当前项目尚未以作者声明的 Agda 2.6.4.3/Cubical v0.7 重放，状态保持 `SOURCE_INSPECTED_WITH_SCOPE`。

## 候选与反解释

`CAND-HOTT-EPF-MODALITY-001` 的可证伪形式现在更清楚：

1. 在 oracle/reflection modality 内固定 CT/ECT/EPF 类能力；
2. 寻找真实 consumer 是否把 modal inhabitant／code／query result 提升到 ambient universe；
3. 固定同一 task、oracle、输入、观察与 completion；
4. 消融 modality、negative resizing、Markov induction、computable choice 与 univalence，定位必要因素；
5. 若 consumer 明列这些前提或输出仍留在 modality 内，则判 `DEFENSE_WORKS`；若悄然提升，才进入方向 B。

Post 的“finite set 有最后元素 stage，但一般不能认出完成点”提供另一 consumer search：查找是否有人从 mere finiteness／truncated enumeration 取得 chosen completion stage。当前 C-141 与 Oracle 源码都没有实施这种越级。
