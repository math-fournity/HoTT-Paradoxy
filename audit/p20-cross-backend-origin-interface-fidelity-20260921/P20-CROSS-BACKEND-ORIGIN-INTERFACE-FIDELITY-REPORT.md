# P20-CROSS-BACKEND-ORIGIN-INTERFACE-FIDELITY-001：C-320 与 C-325 的跨后端保真边界

**状态：** `NO_REGISTERED_FIELD_PRESERVING_TRANSLATION_WITHIN_DECLARED_DENOMINATOR / BACKEND_SEMANTICS_DISTINCT / P21_SYNTHESIS_AND_STOP_DECISION_NEXT / NO_PROOF_ASSISTANT_BUG_OR_HOTT_DEFECT_CLAIM`

## 固定比较对象

| 侧 | 固定对象 | 后端与语义范围 |
|---|---|---|
| 实际 source/operation control | C-320，`hott-z.NativeTaskIntegration.CurveRun/Success` | agda-unimath / `--without-K --exact-split`，带本地 foundation postulates 的 HoTT 风格开发 |
| 最小表达性 control | C-325，`OriginDirectedDiagram` | Cubical Agda 2.8.0 / cubical-0.9 / `--safe --cubical`，native Path/HIT 环境 |

## 本地审计

在当前记录的 source、run manifest、claim matrix、proof-version closure 和 P6/P7/P19 资产中，没有找到一个同时满足以下条件的登记翻译：

1. 输入为 C-320 的 `RichCurve`、`CurveRun`、`Success`、closed diagram、continuity、slice、bound 等字段；
2. 输出为 C-325 的完整 `OriginDirectedDiagram`，而不是只取 bare carrier 或手工有限标签；
3. 有字段保持定理，至少覆盖 source/boundary、operation/trace、observation/Done；
4. 有保存的 machine proof 与 run receipt；
5. 固定两个后端/版本之间的语义保真解释。

该搜索发现的是一个**证据缺口**，不是“没有任何可能翻译”的全局否定定理。

## 公开来源检查

Agda 官方 `--without-K` 文档说明它限制会导入 UIP 的模式匹配，以保持与 HoTT 一类理论的相容性；Cubical Agda 文档则单独描述 interval、Path、transport、composition、Glue 和 HIT 的 native cubical 设施。两份文档支持“二者不是自动同一语义后端”的谨慎判断，但不提供本项目 C-320→C-325 的具体翻译。[Without K 文档](https://agda.readthedocs.io/en/v2.6.3/language/without-k.html)，[Cubical Agda 文档](https://agda.readthedocs.io/en/latest/language/cubical.html)

## 判词与范围

`NO_REGISTERED_FIELD_PRESERVING_TRANSLATION_WITHIN_DECLARED_DENOMINATOR` 意味着：P19 的最小 Cubical 正控制不能被用来证明完整 actual `CurveRun` 已经获得 native Cubical 表达；C-320 也不能被用来反驳 C-325 的最小表达性。它们是不同后端上的不同、范围明确的控制。

这不意味着 Agda、Cubical Agda、agda-unimath 或 HoTT 本身发生错误。要把证据缺口变成理论问题，仍需一个明确的 required translation、一个保真义务，以及该义务为何由目标理论或实际消费者承担的证据。

## 波次定位与下一动作

1. **最终目标连接：** P20 防止跨后端结果被伪装为同一理论中的 P 与非 P，也定位了真实的保真桥义务。
2. **全局坐标：** P4/理论—实现差异的预资格化审计；尚未触发 P4 缺陷调查。
3. **实际价值：** 把“缺翻译”从模糊担忧变为五项可检查的缺口清单。
4. **下一动作：** P21 进行一次跨 P1/P3/P4 的综合与停止决策：判断是否存在已命名、可执行的字段保持翻译任务；若不存在，不继续堆叠接口模型，而把该桥列为 `PARK_PENDING_CONCRETE_TRANSLATION_TARGET` 并从开放 ingress 选择下一独立方向。
5. **裁决：** `CLOSE_WITH_SCOPE / P21_SYNTHESIS_AND_STOP_DECISION_NEXT`。

## 禁止外推

- 不声称不存在所有 future translations 或所有模型解释。
- 不声称 `--without-K` 与 `--cubical` 必然不一致。
- 不声称实际 K、实现 BUG、HoTT 不一致或 HoTT 缺陷。
