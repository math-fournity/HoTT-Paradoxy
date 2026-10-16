# P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001：HoTT Book Cauchy 实数构造的实际语料审计

**状态：** `NOT_A_P13_CONSUMER_WITHIN_FIXED_P17_SOURCES / DEFENSE_EXPLICIT_APPROXIMATION_RELATION_HII_DATA / TASK_DIFFERENT_FROM_P13_MN_DONE / P18_FIFTH_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`

## 固定来源与版本

- 论文：arXiv `2604.24782v1`，2026-04-23，Jackson Brough；[HTML 原文](https://arxiv.org/html/2604.24782)。
- 代码 locator：[`utahplt/hott-reals`](https://github.com/utahplt/hott-reals)，README 将其定位为 HoTT Book §11.3 的 Cubical Agda 实现；本轮只以 `git ls-remote` 固定 `main` 为 `9fcc142b86d0c1e2bd6d06f86f7617200ad74857`，没有 clone、下载或编译。

## 直接 source audit

论文清楚地区分了三个历史构造：经典 quotient Cauchy sequence 的 completeness 需要 countable choice；Bishop setoid 使等价相容性证明持续成为负担；Dedekind cut 在 predicative type theory 带来 universe-level tracking。它引入的不是“任意静态对象自动已完成”，而是一个带有明确构造子和条件的 higher inductive-inductive definition。

固定定义中：

1. 每个 rational `q` 给出 `rational(q) : ℝ`；
2. `limit(x)` 只能接收 `x : ℚ₊ → ℝ` 和 `IsCauchy(x)` 的证据；
3. `path(u,v)` 只能接收对每个正有理精度的 closeness 证据；
4. closeness relation 与 `ℝ` 同时定义，并对 rational/limit 的组合情形给出构造子；
5. 论文特别说明，在 Agda 形式化中 `IsCauchy(x)` 的证明 `φ` 被显式追踪，而非省略。

这不是 P13 中的内在同胚 `H_intrinsic`，也不是有限 ambient-homeomorphism 重建或连续 curve-embedding 变形。

## P7 五项判定

| 项 | 固定来源事实 | 判词 |
|---|---|---|
| `K-input` | 输入包括 `ℚ₊ → ℝ`、`IsCauchy`、closeness relation、精度索引和相应证明；`φ` 在 Agda 中显式追踪。 | `FAILS_BARE_H_INPUT` |
| `K-output` | 输出是 HoTT Book Cauchy real、closeness、代数/序结构和 real-completion相关结果。 | `NOT_P13_DONE_AMBIENT_OR_CURVE` |
| `K-claim` | 论文的完成是 Cauchy approximation 的 limit constructor 与 Archimedean ordered field 构造，不声称去点圆/开区间的 source-operation recovery。 | `NO_P13_COMPLETION_CLAIM_FOUND_WITHIN_FIXED_SOURCES` |
| `K-forgetting` | 近似、精度、relation 和 HIT/HII constructors 直接成为定义/消去条件；固定来源内未找到 `H_intrinsic → Done_ambient^fin / Done_curve` 的 bridge。 | `NO_BARE_H_TO_DONE_BRIDGE_FOUND_WITHIN_FIXED_SOURCES` |
| `K-version` | arXiv v1 + Git main SHA 已冻结；只审论文直接段落、README 和 remote ref identity。 | `VERSION_PINNED_SOURCE_INSPECTED_WITH_SCOPE` |

## 正控制、反解释与范围

**正控制：** 它是一个真实的、近期的 Cubical Agda HoTT Book real construction，且输入的近似/精度/关系/路径构造子都显式存在；这避免将“完成”误读成缺少过程条件的裸断言。

**最强反解释：** Cauchy real `limit` 确实把一个满足条件的 Cauchy approximation 映为一个 real，因此它值得后续的现实—完成语义审计。但这条 completion 所需输入不同于 P13 的 M/N operation contract；把两者当同一任务会重新犯替换原 X 的错误。

**范围：** 作者的“无 postulate/hole type-check”是来源陈述；本项目没有重放该代码。没有主张该实现对所有 real-number consumers、HoTT Book §11.2 的逻辑选项或 P13 原任务作出全局结论。

## 波次定位与裁决

1. **最终目标连接：** P17 检验实际 real-layer completion 是否已在其输入中保留所有需要的构造资格，而不是把抽象对象存在自动读作实际完成。
2. **全局坐标：** P3 `K_app` 的 source audit；它提供了与旧 B1a/实数层话题相邻、但尚未与原圆环任务合并的独立证据。
3. **实际价值：** 确认论文中“completion”是一个显式的 Cauchy approximation constructor，并给出 task-difference 与证据保留边界。
4. **为何关闭本分母：** 固定论文、README 与 ref identity 已回答 P7 的本地问题；扩展到仓库其余文件或编译不是本 P17 的允许范围。
5. **下一选择：** P18 必须选择新的、未审的实际消费者分母，并在开始前重新比较其任务是否更接近 P13 或构成独立但可桥接的 real-layer问题。
6. **裁决：** `CLOSE_WITH_SCOPE / NOT_A_P13_CONSUMER_WITHIN_FIXED_P17_SOURCES / SWITCH_BRANCH_TO_P18_SUCCESSOR_DISCOVERY`。

## 禁止外推

- 这不证明 HoTT Book Cauchy reals 没有哲学、模型或应用层面的现实对应问题。
- 这不证明任何形式化实数构造都保留了同一资格。
- 这不构成 HoTT 内部矛盾、证明器 BUG 或“HoTT 已被击落”的结论。
