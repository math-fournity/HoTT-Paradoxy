# 来源、前提与署名

本包区分当前作者的任务形式化、既有库的数学构造及原典的解释。固定版本证明可复核，不意味所有继承公设均已获整体一致性证明，也不意味旧AI判词被库作者认可。

## 原生几何配置

agda-unimath父commit：`7b81411d9f60afec359d29ed1e4edf43f4711c8a`。包中实际使用的是`agda-unimath-no-erasure`派生源码，不是未修改上游；精确树hash：`3787fb34df15515246da11b90b609d3a2063f15e234f19c1e7f64553c4990f57`。

两处差别为reflection/erasing-equality中的恒等证明替换，以及library名称/相关选项；原补丁在`provenance/HoTT/formal/agda-unimath/no-erasure/identity-replacement.patch`。父归档hash和差异前后hash见同目录TOOLCHAIN。没有隐藏修改其余库源码。

library选项为without-K、exact-split、no-import-sorts、auto-inline、no-require-unique-meta-solutions、no-postfix-projections。它不是safe Cubical。库中funext、univalence、截断/替换等原基础公设保留；几何包没有因此获得全库声性认证。继承内容应沿依赖图和源码直接审阅。

agda-unimath署名与MIT许可保留在`vendor/unimath/LICENSE.md`及原源码。上游：[UniMath/agda-unimath](https://github.com/UniMath/agda-unimath/tree/7b81411d9f60afec359d29ed1e4edf43f4711c8a)。

## Cubical配置

Cubical v0.9 commit：`b150186d2544e7efeddd31e5d14a8b9ecbb100f7`；精确树hash：`73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81`。库本身safe/cubical/guardedness等选项来自原`.agda-lib`；Sqrt2TaskComparison显式two-level，源项保留其原OPTIONS。

该配置与上述without-K公设式库分开运行，没有把两套演算混合成一个新全局理论。Cubical署名及MIT与个别文件例外保留于`vendor/cubical/LICENSE`、SPDX及原文件；[上游固定commit](https://github.com/agda/cubical/tree/b150186d2544e7efeddd31e5d14a8b9ecbb100f7)。

## Book固定原典

The Univalent Foundations Program，*Homotopy Type Theory: Univalent Foundations of Mathematics*；固定commit：`578b85cc8d586b1677ec4335148adeb443057d24`；许可CC BY-SA 3.0，见[许可](https://creativecommons.org/licenses/by-sa/3.0/)。`references/`内十二份摘录保留原文字节，范围和上游URL见PRIMARY-SOURCES.json；只是摘录，不冒充全文。

| 文件和原行范围 | 本包用于核对的内容 |
|---|---|
| basics 1–210，748–805，1706–1808，2165–2360 | 类型/路径解释、transport、univalence、带结构对象 |
| logic 159–255，353–558，598–701 | 命题即类型、限定排中律/大小、截断存在 |
| reals 1–26，85–215，316–365，3204–3225 | 实数路线/宇宙处理、不等与apartness、原则练习 |
| formal 1073–1207 | 指定语法的规范化/规范性及扩张边界 |

这些段落明确讨论运输后的结构、受限消去及不同实数大小处理，不为“裸等价可兑现任意预设结构或过程”提供直接承诺。本文只报告该固定范围的阅读结果，不称全领域文献穷尽。原典数学断言在未被本包重放的部分仍是来源报告。

## 当前研究与未决

形式化输入和主run由各入口exact source commit固定；原M1/M2/M3/B1a通过算术依赖保留其真实类型，未复制旧强判词作本包结论。用户圆环问题是研究动机，本文未把全部原意自动等同于RichCurve或CurveRun。

原广义来源/现实操作对应、实际错误能力承诺、圆环到算术的同任务桥、Weak原则相对整个基线的地位、原创性与外部审阅仍未闭合。本包只在本地生成，不代替任何公开授权或整体完成判词。
