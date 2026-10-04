# ZQCM-001 W-006 / V-SET-02 Source Notes — Fontanella 2016

> **来源身份：** Laura Fontanella, *How to Choose New Axioms for Set Theory?* (2016 author PDF). The title, author, first-page subject matter and bibliography agree with the chapter listed as pp. 27–42 in *Reflections on the Foundations of Mathematics*. The acquired 17-page author PDF is **not** asserted to be byte-identical to the published chapter pagination.
>
> **证据版本：** public author PDF, SHA-256 `014fd8c3d7f5cae93309ce397bc0fc480fe956a32c05efbfc9c0b79bc2954b52`; all 17 source pages and the ten key 300dpi pages (1–5, 8, 10, 12–14) are recorded in [`VISUAL-REVIEW.md`](VISUAL-REVIEW.md).
>
> **状态：** `FULL_AUTHOR_VERSION_ZFC_AXIOM_SELECTION_AND_POWER_SET_NEIGHBORHOOD_CONTROL_SCREENED / SOURCE_ONLY_VISUAL_CHECK_COMPLETE / POWER_SET_AND_REPLACEMENT_INEXHAUSTIBILITY_SOURCE_SEED / NOT_A_BARE_ZFC_CONSUMER / NOT_A_ZFC_Q / REMOTE_DERIVATIVE_NOT_QUALIFIED`.

## 可消费的来源事实

| Source ID | PDF页 | 来源事实 | 对当前语料的作用 | 禁止外推 |
|---|---:|---|---|---|
| C-W006-VSET02-01 | 1–3 | 作者把ZFC中CH、Whitehead problem、constructibility、AC、large cardinals与Projective Determinacy放入“怎样选择新公理”的问题；她区分ordinary mathematics中的用途、独立性结果和公理选择。 | 固定最基本的反混同：一个命题独立于ZFC、一个额外公理能处理它、一个公理在实践中有用，都是不同于发现ZFC理论级Q的命题。 | 不能把“不由ZFC决定”说成ZFC矛盾、计算张力或P命中。 |
| C-W006-VSET02-02 | 4–5 | Foundation历史上用来阻断Russell；作者把iterative conception写为`V_0`、successor Power Set和limit union的分层叙述，明确说这种迭代过程是否穷尽所有可能集合并不obvious，同时称其对描述集合类有practical merits。 | 这是对Power Set／阶段形成邻域的直接一手来源：它为后续精确提问提供历史和哲学起点，也同时保留作者的限定。 | “not obvious”是对Foundation内在辩护的作者保留，不是由ZFC公理推出的矛盾、不可计算性或ordinary consumer失败。 |
| C-W006-VSET02-03 | 6–7 | 作者区分intrinsic与extrinsic justification、可验证后果、pluralism与maximality；`ZFC + measurable cardinals`和`ZF+V=L`可在作者讨论的证据框架中并列，仍需额外理由选择。 | 说明公理选择研究可产生有内容的多理论竞争，而不自动产生对ZFC的错误诊断。 | 不得把未被refuted、理论不相容或公理的fruitfulness混同为Q。 |
| C-W006-VSET02-04 | 8–9 | 本文写出constructible hierarchy的局部递归：`L_0=∅`、`L_{α+1}`取在`L_α`中可定义的子集、limit union，并明说`L`是class；随后把`V=L`、内模型与large-cardinal语言区分讨论。 | 提供whole-`V`、局部`L_α`、class、模型与对象语言之间必须逐一标出的来源控制。 | `L_α ⊨ φ`的局部语义和class叙述不能被偷换为ZFC有whole-`V` truth predicate、内部自指或P5预支使用。 |
| C-W006-VSET02-05 | 10–12 | 作者把inaccessible cardinal的`Uniformity`、`Inexhaustibility`和`Reflection`列为intrinsic motivations；其中Inexhaustibility的文字为集合宇宙不能被Power Set或Replacement等basic operations穷尽，因而有未由这些操作生成的基数；她随后讨论`V_κ`封闭、紧致性及`j:V→M`的large-cardinal特定结构。 | **可保留的最强线索：** 这是与Power Set站位直接相邻的已发表动机文本。它指向的研究动作不是宣布Q，而是寻找一个版本固定的bare-ZFC consumer，检验是否真有“形成尚未支付而已被同一任务使用”的结构。 | 本文的结论方向是为large-cardinal axiom提供动机；`V_κ`、`M`、embedding和满足关系都带模型／大基数／元层支付。相似的“不可穷尽”用词不能替代P1–P6或同一任务证明。 |
| C-W006-VSET02-06 | 13–15 | 作者报告Reinhardt-cardinal式`j:V→V`与ZFC不相容、AD/PD、Ultimate-L方案、forcing与PFA/MM；她在2016来源时点将Ultimate-L模型的构造列为尚未建成／开放的研究问题，并明示条件性后果。 | 提供两种强反控制：社区已对一种全宇宙自嵌入形状有具体防线；未完成研究构造与理论内部Q必须分开。 | 不得把来源报告当作本项目机器证明；不得把开放构造、强公理相对一致性或forcing extension转述为ZFC自身的未支付Done。 |
| C-W006-VSET02-07 | 16–17 | References给出Feferman–Friedman–Maddy–Steel、Maddy、Hamkins、McLarty、Reinhardt、Woodin、Zermelo等可追溯候选。 | 建立受限backward citation map，尤其是公理选择、反射与原始集合论来源。 | 每一引文仍须独立冻结作品身份、取得版本、核验原文并固定消费者；不能因该列表自动扩展为Q证据。 |

## 对 Power Set 站位的资格判断

这篇文章首先支持的是一个**来源级的邻域定位**：Power Set／Replacement／iterative hierarchy确实是集合论工作者用来讨论“宇宙形成、不可穷尽、反射与新增公理”的显眼核心位置。这个结果响应“应从明显的理论承诺开始”，但并没有完成P到Q的推断。

本文没有给出一个ordinary bare-ZFC interface中的固定对象`u`、原生形成`F`、同层实际消费者`C`、同一操作／观察／Done，以及`C`在`F`尚未支付时预支使用`u`的来源事实。大基数、`V_κ`、`L`、forcing、inner model和elementary embedding正是需要分层登记的额外付款或元层装置。

因此本项的有效写回是：

```text
POWER_SET_NEIGHBORHOOD_SOURCE_SEED
  + AXIOM_SELECTION_AND_STANDARD_DEFENSE_CONTROL
  + ACTUAL_CONSUMER_GAP_REMAINS
  + Q_NOT_QUALIFIED
```

下一条最小判别行动不是把“Inexhaustibility”改写成悖论，而是从本文受限backward map中选取一份版本固定的原典或实际数学消费者材料，检查它是否跨越此处明确列出的 `ordinary consumer / same task / formation payment` 缺口。若不能跨越，则这篇文献继续作为Power Set站位的防跳跃控制，而不是被强行重读为Q。
