# HMZ-007：覆盖、分母闭合与停止

| 来源 | 处理 | R/Z/Q disposition |
|---|---|---|
| WoLLIC 2011 | 全 9 slides 已读；R-014 已固定。 | `R_SOURCE_REPORTED`；配对未归因。 |
| Werner 1997 | 17 页原件中与互编码、ZFC semantics、Aczel encoding、Power、Replacement／Choice、结论有关的页已读。 | `SOURCE_PAYMENT + MODEL_SEMANTIC_BOUNDARY`。 |
| rocq-archive/zfc | 冻结 commit tree 已归档；README、`zfc.v`、`Axioms.v`、`Replacement.v`、`Russell.v`、`Hierarchy.v`、`Omega.v`已源码审读。 | `SOURCE_INSPECTED_WITH_SCOPE`；guard/payment controls。 |
| Paulson/Grayson | 复用 HMZ-001／003的冻结 locator。 | 形式化层与计算／axiom层控制。 |

## 可重算分母

```text
included logical sources: 5
new physical originals: 2 (Werner PDF; rocq archive tarball)
new derived source views: 10
R cards: 1
Z cards: 4
Q cards: 3
consumer controls: 5
remainder: 0 within the frozen “WoLLIC ↔ Werner ZFC-in-CIC pairing” scope
```

## 停止与重开

本 run 达到 `DENOMINATOR_COMPLETE_WITH_SCOPE`，不表示所有 ZFC-in-Coq 文献已读。下列材料会重开或生成 successor：

1. Voevodsky 或同一历史来源明确点名 WoLLIC 所说的 ZFC attempts；
2. 一个真实 ZFC-in-Coq consumer 把 `Ens`/Power/Replacement 的存在升级为同一 Done 的可运行／自然交付，却没有 source-visible payment；
3. 一个 source-preserving `H0→Z0` transport，通过 T0–T5；
4. 一个 Power Set R-source bridge 而非仅仅同词出现。
