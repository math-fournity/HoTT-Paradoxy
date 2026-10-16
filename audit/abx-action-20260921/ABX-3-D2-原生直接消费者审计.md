# ABX-3 D_ABX_2：原生圆/开区间直接消费者审计

> 状态：`SOURCE_INSPECTED_WITH_SCOPE / NO_K_WITHIN_D_ABX_2`  
> 机器可复算分母：[ABX-3-D2-DIRECT-CONSUMERS.json](ABX-3-D2-DIRECT-CONSUMERS.json)  
> 边界：只扫描项目自有 `HoTT/formal/agda-unimath/hott-z` 中直接 import 六个 ABX 根模块的源码；不代表 agda-unimath、Cubical、HoTT Book 或论文的全库语义搜索。

## 分母与完备性

`D_ABX_2` 的成员条件是：一个 `*.agda` 文件直接 import 以下至少一项：

```text
NativeOpenInterval / NativeRichCurve / NativeSourceContract /
NativeTaskIntegration / PunctureApartness / NativeCompletion
```

脚本枚举到 29 个文件，逐个记录路径、SHA-256、触发 import、分类和关键锚点；所有 29 个预注册分类均有成员，`remainder=0`。这是一个**文件选择分母**的穷尽结论，不是对每个语义命题的全自动证明。

## 与 ABX 最接近的七个消费者

| 文件 | 代码实际做什么 | ABX 判断 |
|---|---|---|
| `NativeCurveTask.agda` | 裸类型 `BareStep` 有一步 `bareSuccess`，但 `noUniversalTraceLift` 禁止把它统一提升为带闭图的 `AmbientStep` | 明确拒绝裸步骤→强任务的提升；不是 K |
| `NativeCurveTaskControls.agda` | 对 `mRich → transportedRich` 的**全字段** transport 给出 `fullTransportSuccess` | 正控制：保留字段时可成功；不是 K |
| `NativeRichCurve.agda` | `noAnyBarePathLift`、`noUniformBareRecovery` 限定预选富化数据的统一裸恢复 | 表示边界，不是“任何复原不可能” |
| `NativeSourceContract.agda` | `plainNNotSatisfied` 与 `bareCheckIsInsufficient` 拒绝只看载体的强完成判定 | 强 Done 防线；不是 K |
| `NativeTaskIntegration.agda` | 同一 `nRich,mRich` 在 `CurveRun` 成功、在 `Success` 失败；两类型不可等价 | 操作合同分离；不是 K |
| `NativeMotionComplete.agda` | `WeakFinalCoverage ↔ Lift`，只有给出 Lift 才构造指定输出 | 不免费完成弱域覆盖；不是 K |
| `WeakLiftConsumer.agda` | `RealNonzeroApartness` 显式给出后才获得弱删点同胚，且 `refinementPreservesPoint` 保持同一原点 | 条件且保点的正控制；不是 K |

其余 22 项分属几何/闭图构造、同胚与连续性前提、或显式的 Markov/可数选择原则分析。它们没有 `RichCurve` 的强 Done 结果；即便有 `Done` 这个局部名称，也不是将 `H_top` 识别为 `Satisfies(actualInput,·)` 的调用。

## 结果与限制

该分母的结果是 `NO_K_WITHIN_D_ABX_2`。更具体地说，29 个本地直接 import 者中没有发现一个代码位置同时：

1. 只依据 (H_{top}) 或 (U=Bare)；
2. 忽略 `RichCurve` 的闭图/来源代理；并且
3. 将结果声明为当前 `Done_strong` 或同一过程任务的完成。

这很有信息量：在当前最贴近原圆模型的实际代码里，已有消费者没有把抽象误写成强复原；最接近的例子反而把所需原则、来源字段和操作合同显式化。它仍不能支持“HoTT 没有风险”的全局结论，也不能否定未来某个真正 K。

下一次扩展必须改动分母，而不是再次扫描同一 29 文件。合格的后继是一个预注册的外部库版本、论文实现或确实有 `H_top/U → Done` 声明的调用链；若没有这样的新输入，ABX 的当前可证结论就止于两个有界无命中和表示边界。

