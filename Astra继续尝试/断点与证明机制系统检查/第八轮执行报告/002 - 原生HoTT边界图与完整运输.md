<!-- governance-shard:v2
logical_id: ASTRA-BREAKPOINT-EXECUTION-8
shard_id: 002
index: ../第八轮执行报告.md
-->

# 原生HoTT边界图与完整运输

本片的数学结论来自`GeometricBoundaryObservation.agda`的实际Cubical Agda核验。它编码上片同一整数坐标表，使用原生Path、Σ和ua；并没有把Lean Eq称作HoTT Path。

## 1. C-278：结构差异被原生类型论识别

`Coord=ℤ×ℤ`，nBoundary/mBoundary逐项采用上片坐标表。实际导入既有`BoundaryIncidence.agda`，现有真实观察输入填入其distinct/collapsed条件。

已核命题：

- 任意`e : Coord ≃ Coord`和端标签等价，都不能使n边界图与m边界图交换。
- `RichDiagram = Σ(A : Type), Bool→A`的这两个实例之间不存在Path。
- 忘记边界函数后，两实例的环境载体都为Coord，载体Path是refl。
- 一个只接收该裸环境载体的恢复函数，不能同时按给定Path规格恢复这两个不同的RichDiagram。

最后一项不是“任何恢复都不可能”：它的输入相同，输出却被要求同时匹配这两个被证明不同的结构。它也没有再次把给定p的`∀x,x≠p`当作来源恢复问题。

**native Bare的准确身份是边界图的环境载体。** 它不是第一片Lean中的开曲线像子空间。这两个forget接口分别写清；本轮只接通共同边界观察，不把它们冒充一个已经全量翻译的完整对象接口。

## 2. C-279：ua的非恒等正控制

对任意`e : Coord ≃ Coord`，`transportDiagram`使用原生`ua`、`ΣPathP`和`ua-gluePathExt`给出从nDiagram到`(Coord,e∘nBoundary)`的Path。数据随载体一起运输。

具体实例交换两个坐标：(1,0)变成(0,1)。`swappedRightCoordinate = refl`实际核验该计算；`swappedStillSeparate`证明两端分离沿完整结构路径保持。它不是不透明postulate的同名UA，也不是仅做恒等控制。

本片支持的裁定是：所声明的边界数据放入结构后，原生HoTT能区分两图，并能在配套运输时保持区别；当前观察到的结果不是HoTT被迫丢掉这项条件。

## 3. 实际消费的三个上游接口

固定cubical v0.9源码树中的有限接口清单如下，非全库搜索：

| 接口 | 实际声明与调用 |
|---|---|
| `ua` | `Cubical/Foundations/Univalence.agda:35`，输入类型等价，输出类型Path；实现用Glue |
| `ua-gluePathExt` | 同文件:74，将元素连同该类型Path搬运；本模块逐端点调用 |
| `ΣPathP` | `Cubical/Data/Sigma/Properties.agda:63`，要求首分量Path以及沿它的第二分量PathP；不是只给载体Path就得到整个结构Path |

这些声明已回到正文核对，并由本模块实际消费。当前三接口没有向本模块提供“忘记边界后仍免费得到任意目标边界”的规则；`noRichDiagramPath`与完整运输正控制进一步给出该具体实例的机器判别。

未检查社区所有程序、模型或用户解释，不能由这一清单宣布全库无误用。
