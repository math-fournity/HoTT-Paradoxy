<!-- governance-shard:v2
logical_id: ASTRA-NATIVE-MOTION-BUNDLE-30
shard_id: 003
index: ../第三十轮执行报告.md
-->

# 固定末态图的Weak覆盖条件

不能把当前Strong参数图默认为原Weak去点圆的无条件全覆盖。本轮将这项原有剩余义务直接接到当前已经构造的末态函数：

```
WeakFinalCoverage = ∀w : PuncturedRealCircle,
  ∃u : OpenRealInterval, motion(1,u) = plane(w)

ChosenWeakFinalOutput = ∀w : PuncturedRealCircle,
  Σu : OpenRealInterval, motion(1,u) = plane(w)
```

第一个存在是命题截断的存在，第二个显式给出参数。C319证明：

```
WeakFinalCoverage ↔ Lift ↔ RealNonzeroApartness
Lift → ChosenWeakFinalOutput
```

充分方向消费已有原Weak同胚，得到原u，并以原motionAtOne与实际逆律证明命中原点。必要方向从固定末态图的mere覆盖消去到Strong命题：原参数化产生的点具有Strong证据，同点等式将其运输到输入w。没有从截断里任意抽出数据。RNZA连接复用原C307的实际实数坐标归约，不是假定名称相同。

这一必要性针对**这份固定末态图的完整Weak覆盖**。它不是任意可能同胚的必要性，不是LEM必要性，也不证明P相对于当前整个基础库独立或必须另加为公理。未构造无条件Lift/RNZA，也未证明其否定。给定原则可兑现与原则无法由基线推出是两项不同义务。

这是把已有原则刻画接到当前具体过程的消费者所得的精确结果，不自封为新的基础缺陷。接下来的四层审计必须检查原任务是否确实要求这种全覆盖、理论是否作出相应无条件承诺，以及现实参考侧是否在同一输入/完成标准下取得了该能力。
