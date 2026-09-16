# LIT-HOTT-COMPUTABILITY-001 首轮来源资格化与接口映射

日期：2026-09-14  
范围：Parametric CT、Oracle Modalities、2LTT、CSL 2026 groupoid syntax，并与 Post 1944 completion/order 连接。

## 本轮形成的真实链

1. **Parametric CT**：固定 109 文件 Coq 源树与 20 文件目标闭包；C-219–C-222 在 Coq 8.13.2 机器重放，把 R2 从 synthetic implication 推进到“显式 EPF_bool/SCT 前提下的 internal `~ decidable`”。
2. **Oracle Modalities**：固定 `awswan/oraclemodality@e6e3f75`，codeload 与 Git export 的 34 文件、142,253 bytes、tree SHA `06bbc48b…` 一致；MIT 源码完整导入 `audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities/source-e6e3f75/`。
3. **2LTT**：重读 §2.1/2.4/2.6/2.7，确认 paper suggested syntax 非完整 raw specification、basic conservativity 与 strengthenings 必须分开、internal fibrant replacement 会推出 UIP 的 source-reported no-go。
4. **Groupoid syntax**：固定 91 文件作者仓库并通过 C-223–C-226 两阶段 Cubical Agda exact replay，取得首个可执行 `G-HOTT-SYNTAX` slice。
5. **Post 对照**：Post §11 的 adaptive query 时序与 Oracle `queryOracleAndContinue` 对齐；“有限 extension 有最后元素 stage”与“当前能认证全部出现”分离，映射到 completion qualification，而不替代时间／运动轴。

## Oracle Modalities 的精确前提地图

源码中的能力分为两层：

| 层 | 源码位置 | 资格 |
|---|---|---|
| higher/oracle modality、Turing reducibility | `OracleModality.agda` | HoTT/Cubical 结构真实参与；仍依赖导入的基础公理模块 |
| negative resizing classifier | `Axioms/NegativeResizing.agda:24–31` | `postulate` |
| Markov induction／unbounded search | `Axioms/MarkovInduction.agda:39–43` | `postulate` 后导出 Markov principle |
| `φ₀` machine + unique halting time | `Axioms/ComputableChoice.agda:38–40` | `postulate` |
| computable choice | `Axioms/ComputableChoice.agda:67–72` | `postulate` |
| ECT/CT | 同文件 `:93–102` | 从上述前提推导，不是 ambient universe 裸定理 |
| relativised choice/jump/parallel search/continuity | `RelativisedCC.agda`、`ParallelSearch.agda`、`Continuity.agda` | 模态 consumer；继承上游前提 |

作者声明工具链为 Agda 2.6.4.3 + Cubical v0.7；当前项目尚未构建该 exact environment，故这里只作 `SOURCE_QUALIFIED`，不称 theorem replay。

## 对八轴张量的修订

- `TC-06 Modalities × OP-11 CrossModel × CC-oracle continuation × OL-modal inhabitance × CP-decidability` 获得真实 source seed；
- `TC-11 2LTT × OP-02 ExternalToInternal × CC-fibrant replacement × CP-context stability` 新增高判别候选；
- `TC-09 Syntax × OP-12 Coherence pressure` 从 `PENDING` 获得 machine-replayed groupoid syntax slice；
- R2 oracle 增加三阶判词：synthetic implication／conditional internal negation／unconditional internal negation；
- Post 的 adaptive query 与 completion certificate 区分进入时序轴；它不覆盖运动、连续性与稠密性轴。

## 当前最强判词与下一步

```text
THREE_BREADTH_SLICES_HAVE_REAL_EVIDENCE
/ POST_PRIMARY_REVIEWED
/ R2_CONDITIONAL_INTERNAL_NOT_DECIDABLE_MACHINE_REPLAYED
/ ORACLE_MODALITIES_FULL_SOURCE_QUALIFIED_NOT_REPLAYED
/ G_HOTT_SYNTAX_FIRST_EXACT_MACHINE_REPLAYED_SLICE
/ CAND_2LTT_FIBRANT_REPLACEMENT_UIP_PROMOTED
/ AMBIENT_UNCONDITIONAL_R2_R4_NATURAL_CONSUMER_REALITY_BRIDGE_OPEN
```

下一有界研究优先转 `CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001`，因为它同时具备自然理论动机、HoTT 高阶结构、明确消融、source-reported theorem 与“逐例可做→统一内化新增困难”的方向 A/B 形状。并行保留 Oracle Modality 的旧工具链重放与 modal→ambient consumer 搜索；若候选最后只是人为加入不相容规则，应降级并回到下一 cell。
