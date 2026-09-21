# ABX-1–3：原对象、任务合同与首个实际消费者分母

> 状态：`FORMAL_COMPONENTS_QUALIFIED_WITH_SCOPE / NO_K_WITHIN_D_ABX_1 / NO_NEW_HOTT_DEFECT_CLAIM`  
> 运行收据：[ABX-1-FORMAL-QUALIFICATION.json](ABX-1-FORMAL-QUALIFICATION.json)  
> 范围：一个实际 Dedekind 圆—开区间模型、既有内核证明包，以及一个明确很小的消费者源码分母；不是对 HoTT、Cubical 或拓扑学的全局负结论。

## 1. ABX 的第一个可执行对象

ABX 不再把“`M` 是圆去一点、`N` 是线段”留为比喻。当前采用已保存的原生 Agda-unimath 模型：

| ABX 符号 | 当前精确定义 | 已有证据 | 不能偷换成 |
|---|---|---|---|
| (C) | `RealCircle`：Dedekind 实数平面上的单位圆 | C-281、C-283–C-292 | 任意拓扑圆或物理环 |
| (p) | `east = (1,0)` | `NativeRealCircleQualification.agda` | 未指定的任意删点 |
| (M_w) | `PuncturedRealCircle = Σ q:C, q ≠ east` | C-283/C-284 | 自动带可除分母的坐标域 |
| (M_s) | `StrongPuncture = Σ q:C, apart(x(q),1)` | C-283–C-290 | 与 (M_w) 无条件相同 |
| (N) | 原 `OpenRealInterval`，严格 (0<u<1) 的度量子空间 | C-281、C-289/C-290 | 闭区间或带端点的参数域 |
| (H_{top}) | `strongCircleUnitHomeomorphism` 及 `strongIntervalTypePath` | C-290 | 来源、边界图、操作或 Done 的相等 |

这里有一项不能省略的事实：对直接逻辑删点 (M_w)，到 (N) 的同胚/类型路径在当前构造中需要 `Lift`；对强删点 (M_s)，实际连续互逆和 univalence 的类型路径已给出。故 ABX 不能把“删一点”未加条件地写成“总有同胚”，也不能把强域的正例写成对全部弱删点的免费结论。

## 2. (X)、来源代理与双 Done

当前模型把用户所说的“圆去点—开区间—闭合/复原”落实成两个不同层次。

`mCompletion : [0,1] → C` 是原 (M_s) 参数化的闭参数延拓；内点处与 `strongCircleUnitHomeomorphism` 的逆一致，端点 `0`、`1` 都映到同一 `east`。`nCompletion : [0,1] → Plane` 则把端点映到两个不同平面点。C-291/C-292 已机器检查这些精确陈述。两个参数仍不同；终点是同一**像点**，不是“两个不同点具有零距离”。

用户所称的来源/复原信息在本轮先用一个诚实受限的代理表示：

```text
RichCurve = Σ A : Type, CurveData(A)
CurveData(A) =
  parametrization : N ≃ A
  realize          : A → Plane
  close            : [0,1] → Plane
  closeContinuous
  agreesInterior

U(RichCurve) = Bare(RichCurve) = A
```

它记录参数化、平面实现、连续闭图和内点一致；它**不**声称装下现实中的全部生产历史、材料条件或所有允许操作。这个受限代理足以检验 “只保留裸载体” 是否遗漏已声明的闭图观察。

对 `actualInput`，定义两种完成条件：

```text
Done_weak(r)   := Bare(r) = targetCarrier(actualInput)
Done_strong(r) := Satisfies(actualInput,r)
                := Done_weak(r) × Denotes(actualInput,r)
Denotes(i,r)   := ∀u:[0,1], close(r,u) = close(source(i),u)
```

这正是 ABX 所需的 A/B 分离：静态载体处理只给出 `Done_weak`；过程/图保真要求还需要 `Denotes`。它不是把 `RealitySame` 删除出规格，而是将可检验的来源—闭图部分写成附加观察。

## 3. 已经存在的正反控制

1. **同胚与全字段运输正控制。** `reexpressed actualInput` 通过给定同胚的 univalence 运输完整 `CurveData`，有有限 `Run`，并满足 `Done_strong`。这证明 HoTT/类型运输不会自动删除一个明确携带的字段。
2. **裸 (N) 的反控制。** 预选 `nRich` 满足 `Done_weak`，但 `plainNDoesNotDenote` 与 `plainNNotSatisfied` 证明它不满足这个具体 `Done_strong`。`bareCheckIsInsufficient` 因而否定“每个同载体输出都足以满足闭图”的函数。
3. **复原不能被绝对否定。** `PointRestoration` 证明，在指定点相等可判定时，`Puncture ⊎ Unit ≃ C`；`RationalRestoration` 给出有理圆实例。它排除“任何 N 都绝不可能得到任何闭合/复原对象”的说法。相反，HIT `S¹` 的路径补对象没有该特定 split；那不是实数点集圆命题。
4. **操作合同正反对照。** 同一 `nRich,mRich` 对存在 `CurveRun`（连续嵌入曲线族），但在另一个明确规定为全平面同胚步骤的 `Success` 合同中没有成功；`noCurveAmbientEquivalence` 证明二者不可等价。它说明 A/B 只有在 Input、允许操作、Observation 和 Done 一致时才可比较。

此外，C-293 的 `noAnyBarePathLift` 与 `noUniformBareRecovery` 给出了更窄的恢复边界：任何裸类型路径都不能把预选 `mData` 恰好运输成预选直线 `nData`，且不存在同时把两个裸类型固定恢复为那两份指定富化数据的统一函数。这是**预选数据的统一恢复否定**，不是“裸 (N) 不能产生任何恢复”的全称定理。

## 4. ABX-2 的首个精确候选及其判词

由上一节可以写出第一个精确的 ABX-2 候选：

```text
不是：N 无法变成 M。
而是：不存在仅按 Bare 类型、同时把 StrongPuncture 恢复为 mRich
      且把 OpenRealInterval 恢复为 nRich 的统一 recover；
并且预选 nRich 不满足 actualInput 要求的完整闭图 Done。
```

这个候选已由 C-293/C-296 的现有内核包支持，证据等级为 `FORMAL_CHECKED_WITH_SCOPE`。它建立的是**表示/任务边界**。它尚未把 `R_origin` 扩张为“真实历史”，也未表明任何 HoTT 消费者错误地将弱完成当强完成。

## 5. D_ABX_1：首个实际消费者检索分母

为防止“没看到”被写成“全 HoTT 没有”，本轮只冻结以下分母：

| 项 | 检查对象 | 实际结果 | 与 K 的关系 |
|---|---|---|---|
| D1 | pinned agda-unimath 的 `uniform-homeomorphisms-metric-spaces` | `uniform-homeo` = 等价 + 双向一致连续；消费者把它用于 complete/total-bounded 性质 | 没有本圆、来源字段或 `Done_strong` |
| D2 | `uniform-homeomorphism-unit-interval-proper-closed-interval-real-numbers` | 单位**闭**区间到任意 proper closed interval 的缩放，并用来传递 total boundedness | 不是 (M/N) 或删点复原任务 |
| D3 | `NativeSourceContract` | 真正使用原 (M_s/N) 等价，但要求 `Denotes`，并拒绝裸 `nRich` | 反向控制：保留强任务 |
| D4 | `NativeTaskIntegration` | 同 pair 的两种操作合同被明示为不等价 | 反向控制：不把一项成功冒充另一项 |
| D5 | Cubical v0.9 全 `*.agda` 的 `homeomorphism|Homeomorphism` 字面扫描 | 0 个字面命中 | 仅说明无以该名称出现的文件；不能代替语义全库搜索 |

因此本分母的结论是 `NO_K_WITHIN_DECLARED_DENOMINATOR`：没有发现一个实际使用位置将 (H_{top}) 或 (U) 当作该 `Done_strong` 的完成。它不证明所有 HoTT、Cubical、论文或未来库都没有 K；也不证明 HoTT “安全”或“不安全”。

## 6. 下一步与停止条件

下一步应只扩大一个新的 K 分母，或在用户补充“允许操作/来源保持”的精确定义后，把 `R_origin` 从 `RichCurve` 代理升级为更强合同。若新消费者仍保留 `Denotes`/操作合同，登记为 `DEFENSE_PRESERVES_TASK`；若它实际把 `Done_weak` 当 `Done_strong`，才进入 ABX-4 的同任务失配证明。

