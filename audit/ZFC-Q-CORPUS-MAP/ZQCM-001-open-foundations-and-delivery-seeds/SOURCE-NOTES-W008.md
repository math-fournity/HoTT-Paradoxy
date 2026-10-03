# ZQCM-001 W-008 Source Notes — Matthews 2023/2024

> **身份：** FULL_PRIMARY_REALIZABILITY_GUIDE_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q。
>
> **原件：** `originals/Matthews_2023_Guide_to_Krivine_Realizability_arXiv2307.13563.pdf`；arXiv `2307.13563v2`；Richard Matthews；65页；SHA-256 `2297f7b0c93bf4e17209f4466df8fa75624d12142d79d0cf19c6b76574505fac`。
>
> **阅读边界：** official remote MinerU attempt `MIN-REMOTE-QUAL-008` returned `server_not_running`; no local service was started. This note uses the original PDF’s 65 source-only page records `VR-W008-001` through `065` and 300dpi checks on pp.11, 15, 16, 18, 19, 30, 46.

## 原件给出的精确结构

1. **pp.1–13：计算语义有明确的承载体。** BHK、lambda calculus、terms、stacks、processes、pole、realizers、truth/falsity values、one-step evaluation和`quote`都被定义。它们不是裸ZFC对象，也不是从存在断言中自动析出的程序。
2. **pp.14–30：`ZF_ε`到ZF及Weak Power Set是有条件的模型构造。** `ε`、`∈`、`≃`、`ZF_ε`、ground model `V`、algebra `A`、rank recursion、model reduction和theory preservation逐一出现。Weak Power Set的见证明确写为`P(dom(a)×Π)×Π`，并使用ground-model Collection和Infinity的递归name构造。
3. **pp.21–49：表示、函数和Choice不是自动可运输的。** 作者针对non-extensional equality、pair encoding、ordered pairs、functions、reish names和universal lift给出具体定义。Remark 16.8说明一般不能把ground-model function lift为extensional function，因为reish images未必保留所需的extensional equality；后续以class-function universal lift和明确函数处理该边界。NEAC／DC同样依赖countable algebra、`quote`、ground-model AC、enumeration和minimal ordinal。
4. **pp.50–61：非平凡模型、forcing与realizability的关系都具备前提和翻译。** 特定algebra的生成器、pole和preorder固定其归约结论；forcing到realizability的翻译被明示为会失去computational content。两模型的“same”需要`τ`／`σ`、complete Boolean algebra、rank和formula-complexity induction。
5. **pp.62–65：numeral comparison与书目边界。** Church numeral比较在指定lambda terms和reduction rules中完成；references提供Krivine、Friedman、McCarty、Rathjen等受限backward leads，不能凭题名继续膨胀work family。

## 对 P、Power Set 与 ZFC Q 的处置

本来源强化三项控制：

- **P5 delivery control：** proof/program、existence和realizer只在指定calculus、model、truth/falsity value和adequacy规则下建立；它不能反向要求ordinary ZFC为其存在量词交付程序。
- **Power Set payment control：** `ZF_ε`的Weak Power Set与realizability-model中的canonical weak-power-set函数，均有明确domain、stack、ground-model Collection和recursive-name支付。
- **transport / representation control：** Ground-function到extensional-function的普遍lift在来源中被明确指出可能失败；但该失败是固定realizability模型的`reish`／equality／functionhood问题，且作者给出universal-lift路线。它可成为未来固定ordinary ZFC consumer的严格反事实条件，不能单独构成同一任务的Q。

当前处置为`MODEL_SEMANTIC_PAYMENT_AND_TRANSPORT_CONTROL_NOT_Q`。重开条件是一个版本固定的ordinary ZFC consumer，同时要求同一对象、同一操作、同一观察与program-like Done，并且其使用跨越本来源已列出的model／language／lift／payment边界；重复的realizability、Power Set、choice、fixed-point或transport关键词不重开。
