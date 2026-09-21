# P10-SECOND-SUCCESSOR-DISCOVERY-001：离开定向簇后的第二次候选选择

**状态：** `SUCCESSOR_SELECTED / COQHOTT_CIRCLE_COEQUALIZER_CORPUS_CANDIDATE / P11_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM`
**日期：** 2026-09-21
**当前目标边：** P3 的实际库/形式化消费者边；P10 本身只选择一个新的有界分母，不对它作最终 K 判词。

## 1. 判词改变凭据

P8、P9 已分别在 Rzk 实现和 sHoTT `diruniv` 语料中得到“显式定向/协变结构仍在输入层”的范围防御。继续读取同一 directed/simplicial 簇不会改变 `K-input` 或 `K-claim`。P10 因而只比较四个未覆盖入口：未审规则、非定向实际消费者、独立更强 `R/Done` 和理论—实现差异。

要改变的不是“HoTT 是否有缺陷”的判词，而是当前 next：从 P10 的开放 discovery 转为一个版本固定、可按 P7 五项 K 条件审计的外部 source corpus。正结果只会使该 source 获得后续同任务失配检验资格；负结果只会关闭它的固定分母。P10 不新增数学命题、内核运行或总体否定结论。

## 2. 公开与本地双重侦察

公开一手来源中，Coq-HoTT 的实际 [`Circle.v`](https://github.com/HoTT/Coq-HoTT/blob/master/theories/Spaces/Circle.v) 把圆定义为两个 `Unit` 恒等映射的 homotopy coequalizer；其 [`Coeq`](https://hott.github.io/Coq-HoTT/coqdoc-html/HoTT.Colimits.Coeq.html) 文档给出显式 `coeq`、`cglue` 和递归/消去的相容性条件。Coq-HoTT 是公开 HoTT 库，其项目身份和版本冻结由其 [GitHub repository](https://github.com/HoTT/Coq-HoTT) 与 [library paper](https://arxiv.org/abs/1610.04591) 支持。项目内实际克隆固定 `master@e3deab71b9cb53a22c00ab39dea4699dd2c89a13`，并保存所选五个 blob/SHA 于 `P10-COQHOTT-CANDIDATE-FREEZE.json`。

本地侦察给出以下去重裁决：

| 入口 | 本地/公开证据 | 裁决 | 为什么不直接成为 K |
|---|---|---|---|
| Cubical `S¹` C-304 | `astra-s1-consumer-check/SC00.agda` 已固定 base/loop、编码—解码与六控制 | `PARTIAL_REUSE` | 同为 HIT 圆机制，但不是 Coq-HoTT 的 coequalizer 定义、版本或下游 Torus 调用。 |
| ABX `D_ABX_1/2/3` | point-set/本地 direct consumers/Book core 已有有界审计 | `NEARBY_ONLY` | 三者未固定 Coq-HoTT Circle/Coeq/Torus 这一外部 source chain。 |
| `N∞` 的一点评紧化/内在拓扑 | Escardó 的工作讨论离散自然数的一点评紧化与收敛序列 | `NEARBY_NOT_SAME_TASK` | 对象是离散 `ℕ` 与序列收敛，不是原 `C,p,M,N,e` 的圆去点—闭合—复原任务，也没有实际 K。 |
| P4 实现差异 | P1–P9 没有同一规则的跨实现语义不一致 | `NO_TRIGGER` | 不能仅因 Coq-HoTT 使用另一实现就把它升级为实现错误审计。 |

## 3. 选择的候选：Coq-HoTT Circle/Coeq 与实际 Torus consumer

选择下一分母 `P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001`，其固定源码为：

```text
HoTT/Coq-HoTT@e3deab71
  theories/Colimits/Coeq.v
  theories/Spaces/Circle.v
  theories/Spaces/Torus/Torus.v
  theories/Spaces/Torus/TorusEquivCircles.v
```

它不是把“端点无限接近”作为极限叙述。`Circle.v` 明确写出：

```text
Circle := Coeq Unit Unit idmap idmap
base   := coeq tt
loop   := cglue tt
```

而 `Coeq_rec` 的输入要求一个从基础载体到目标的函数，外加对每个粘合生成元的明确相容路径。`TorusEquivCircles.v` 作为实际下游消费者，使用 `Circle_rec`、给定 torus 的 base/loops/surface，再证明 `Torus ≃ Circle × Circle`。因此它是直面“识别/闭合”操作的非定向 HoTT library corpus，同时也带有足以构成最强反解释的显式 glue/coherence 数据。

### P7 预审（不是最终 P11 判词）

| P7 条件 | P10 已见直接证据 | 仅供候选选择的初步判断 |
|---|---|---|
| `K-version` | commit、五个 blob、SHA、入口路径已冻结 | `PASS_VERSION_IDENTITY` |
| `K-input` | `Coeq` 接受显式 `B,A,f,g`；Circle 固定为 `Unit,id,id`；递归还接收 glue coherence | `LIKELY_FAIL_AS_K / EXPLICIT_GLUE_STRUCTURE` |
| `K-output` | Circle 的 base/loop 与 Torus—Circle 乘积等价可定位 | `OUTPUT_LOCATABLE_BUT_NOT_DONE_S` |
| `K-claim` | 已读选段没有 `OpenRealInterval`、`C,p,M,N,e`、闭合 trace 或原 `Done_strong` 声明 | `UNRESOLVED_UNTIL_FIXED_SOURCE_AUDIT` |
| `K-forgetting` | 构造与递归都显式携带映射、glue 和 coherence | `LIKELY_FAIL_AS_K / EXPLICIT_DATA` |

P11 的工作是把这些初步事实变成版本固定、逐项的 source audit，并检查 Circle→Torus 的实际调用是否产生任何与原 `Done_s` 同名的承诺。它不可以因为 P10 的预审就提前宣告防御、K 或 HoTT 缺陷。

## 4. 波次定位与停止

1. **最终目标连接：** P10 为实际消费者边找到一个直接表达“粘合/闭合”的非定向外部 HoTT source，而不是继续在定向簇中增加同义防御。
2. **全局坐标：** P1 固定共同任务；P2、P3 首次分母未命中；P5–P7 固定后继与 K 门槛；P8/P9 关闭定向防御；P10 选择新的 P3 source candidate。
3. **实际价值：** 新增的是可定位的 Coq-HoTT coequalizer construction 与真正下游 Torus consumer，能够测试“端点识别”在非定向 HoTT 实践中是否需要显式数据。
4. **为什么不继续 P10：** P10 的分母是四类入口的选择，不是第二次外部库审计。其预注册动作已经完成；继续搜索更多名称会违反单一候选与令牌经济。
5. **裁决：** `SWITCH_BRANCH / SUCCESSOR_SELECTED`。P11 尚未启动；其启动必须先由总体计划把此真实 candidate 写成下一有界分母，再按 P7 审计。

## 5. 禁止外推

- 本报告没有运行 Coq-HoTT，也不证明其 source 或 metatheory正确；
- Coequalizer/HIT circle 不等于原点集 `C \ {p}`、开区间 `N`、来源历史或原 `Done_strong`；
- `N∞` 的邻近文献不构成圆环同任务证据；
- P10 的选择不等于已经发现 K，也不等于 P11 已经执行。
