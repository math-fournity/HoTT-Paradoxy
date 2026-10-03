# ZQCM-001 W-003 Source Notes — Krivine, arXiv:1502.00112v4

> **身份：** FULL_PRIMARY_CLASSICAL_REALIZABILITY_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / NOT_A_ZFC_Q。
>
> **原件：** `originals/Krivine_2015_Bar_recursion_classical_realisability_arXiv1502.00112v4.pdf`；arXiv:1502.00112v4；11页；SHA-256 `4bbed1b843f46be19b6226481faf55445efaf57bcde6b208a4ac9363da862ba3`。
>
> **阅读边界：** direct remote MinerU没有可用导出；本记录只使用原 PDF 的150dpi逐页和关键300dpi图。页图与逐页证据见`VISUAL-REVIEW.md`的`VR-W003-001`至`VR-W003-011`。

## 原件给出的精确结构

1. **p.1：论题与适用域。** 文章把 bar recursion 放在 classical realizability 语境，讨论 proof–program correspondence、BBC realizability algebra、countable choice（CC）与 dependent choice（DC）。关于 ZF、well ordering 与 continuum hypothesis 的表述都在与该 algebra 关联的模型中，并由 closed `λ_c`-terms／附加理论条件限定。
2. **pp.2–3：运行语义被显式给出。** BBC algebra具有 terms、processes、stacks、continuation、execution preorder、proof-like terms和具体执行规则；这不是从 bare ZFC 句子自动抽取程序的描述。
3. **pp.3–4：ZFC 与 realizability model 被严格分层。** `ZF_ε`是 ZF 的 conservative extension，带 non-extensional strong membership；从 ordinary ground model `M` of ZFC（或ZF+V=L）构造 realizability model `N`。`M`与`N`可以同 domain，但文中明确说它们不具有同一 language 或 truth values；p.4还说明在`M`中成立的函数性表述一般不在`N`中成立。
4. **pp.5–9：交付由额外的实现证据支付。** p.5明确说从实现给定算术公式的 proof-like term得到程序，前提是所用 axioms themselves have such realizers；文章随后把ZF axioms、BBC algebra的bar recursion、CC/DC与相应realizer逐项连接。p.7–9的CC/DC结论针对`ZF_ε`公式和与BBC algebra关联的模型。
5. **p.10：后续结论仍依赖 ground-model 假设。** well ordering、choice、constructible reals和continuum-hypothesis的链条引入ultrafilter及`M_D`；choice依赖`M ⊨ ZFC`，constructibility／CH再依赖`M ⊨ V=L`。
6. **p.11：引用边界。** 该页列Berardi–Bezem–Coquand、Berger–Oliva、Krivine 2011–2014、Streicher与Spector等作为理论谱系；它们是受限的bibliographic leads，不是已经确认的 ordinary-ZFC consumer。

## 对 P5 与 ZFC Q 的处置

这篇原件使下列宽泛说法失去资格：**“ZF 或 ZFC 必然没有 proof–program／realizability 语义。”** 文中确实构造、运行并使用了带 ZF 关联的经典 realizability 语义。

但它没有满足当前 P5／Q 门：

- 来源中的可运行对象是`Λ`、`Π`、BBC algebra、`ZF_ε`、ground model `M`和realizability model `N`的组合，不是 ordinary bare ZFC 内一个固定的 actual consumer；
- “交付”依赖明示的 proof-like terms、realizers、algebra、model及可见的 axiomatic／ground-model条件；
- 原件没有给出同一 ordinary ZFC consumer 在自己的 program-like Done 未支付时预支使用对象的来源事实；
- 因而它不能形成 P5 命中、同一任务卡或 ZFC Q。

当前处置是`MODEL_SEMANTIC_PAYMENT_CONTROL_NOT_Q`。若以后找到一个版本固定的 ordinary ZFC consumer，能在同一对象、操作、观察与Done下跨越上述模型／支付边界，才可重开专门 bridge；仅有同类“存在程序”措辞、ZF model或realizability名词不重开。
