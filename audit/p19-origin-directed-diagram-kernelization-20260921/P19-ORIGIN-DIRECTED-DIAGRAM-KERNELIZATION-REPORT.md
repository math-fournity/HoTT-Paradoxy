# P19-ORIGIN-DIRECTED-DIAGRAM-KERNELIZATION-001：最小来源—过程—完成结构的原生表达性控制

**状态：** `MINIMAL_ORIGIN_STRUCTURE_EXPRESSIBLE_WITH_SCOPE / BARE_FORGETFUL_NEGATIVE_CONTROL / FULL_TRANSPORT_POSITIVE_CONTROL / ACTUAL_C320_CROSS_BACKEND_BINDING_NOT_ESTABLISHED / P20_CROSS_BACKEND_ORIGIN_INTERFACE_FIDELITY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`

## 已核实的机器结果

`OriginDirectedDiagram.agda` 在 Cubical Agda 2.8.0 / cubical-0.9 中定义最小对象

```text
Σ static : RichDiagram . ((Bool → Bool) × Bool)
```

其中 static 保存结构化 boundary/source 图，余下字段是最小 trace/done 标签。C-325 机器检查表明：

1. `originN` 和 `originM` 的 `bareOrigin` 相同；
2. 两完整结构之间没有 path；
3. 单一 `Type → OriginDirectedDiagram` 恢复函数不能同时恢复两个给定对象；
4. 完整 static diagram 可以经 `liftStatic` 沿 native path transport，且 trace/done 标签保持。

前两次 capture 的类型失败（未导入 `∘`、错误 Sigma-path witness）被保留；修复后的第三次 run exit 0，且已进入 C-325、source manifest、index-row manifest 与 proof-version closure。

## 与原 C-320 的绑定审计

C-320 的 `CurveRun nRich mRich` 是实际 Agda without-K / agda-unimath 源中的 rich geometric record：它包含 `at`、`closedAt`、joint continuity、slice homeomorphism、initial/final diagrams 和 space bound。P19 的 Cubical object只复现了其中“结构能被共同保存和裸载体不足”的最小模式。

两者并不已经是同一个类型，也没有当前机器证明的翻译：C-320 的 source 位于 `hott-z.NativeTaskIntegration`，而 C-325 使用 native Cubical Agda。故不能把 C-325 的表达性正控制声称为“完整原过程已经进入 Cubical HoTT”，也不能从两个后端不同推断实现错误。

## 波次定位

1. **最终目标连接：** P19 排除了“来源/操作/完成字段根本无法在 native HoTT/立方语义中表达”的过强解释。
2. **全局坐标：** P1 对象理论线；P3 仍因同类重复处于暂停，不是被宣布完成。
3. **实际价值：** 获得一个 version-closed machine proof of an explicit full-structure transport/bare-forgetful separation control，并精确暴露 C-320→C-325 的跨后端绑定义务。
4. **下一选择：** P20 只审这条跨后端 origin-interface fidelity 义务：是否存在保持 fields/claims 的翻译、已登记的保真解释，或明确不能建立的证据；它不重做 P19 的最小接口。
5. **裁决：** `CLOSE_WITH_SCOPE / SWITCH_BRANCH_TO_P20_CROSS_BACKEND_FIDELITY`。

## 禁止外推

- C-325 不是完整 Circle/Interval 物理、几何或来源过程的形式化。
- C-325 不证明 HoTT 无法表达原任务，也不证明 HoTT 已实现原任务。
- 未建立跨后端翻译是当前证据缺口，不是 proof assistant bug、理论矛盾或 HoTT 缺陷。
