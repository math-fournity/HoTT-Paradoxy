# CN-082：Zermelo 1908 原文里没有「解决」，只有「排除 / 消失 / 失效 / 消除」

> **身份**：AI 综合 + 机器提取（OCR），依据：Zermelo 1908 原件 21 页扫描（GDZ IIIF）
> + macOS Vision OCR 的**全页穷尽检索**。非记忆，非转引。
> 证据文件：`docs/罗素解决考古/来源/01-Zermelo1908-原文OCR与措辞核验.md`。

## 一、做了什么

把「Zermelo 到底用了哪个动词」从**印象之争**变成**可检索的文本事实**：
取得原件全部 21 页（Math. Ann. 65, 261–281），逐页 OCR，然后用一个正则
（`lös*|gelöst|Lösung|beseitig*|ausschlie*|vermeid*|verschwind*|Wegfall`）
扫过全文，逐个命中看上下文。

## 二、结果（这是本条的核心）

`lösen / Lösung` 在全文只出现**两处，且都不是以悖论为主词**：

1. p261：「…Widersprüche oder ›Antinomiéen‹ … und bisher noch keine
   allseitig befriedigende **Lösung** gefunden haben.」
   —— 说的是悖论**迄今还没有**令人满意的解决。
2. p261 同页：「Diese **Aufgabe** muß in der Weise ge[l]öst werden…」
   —— 被「解决」的是**这项任务**（公理化的任务），不是悖论。

真正用在悖论身上的动词是四个，全部属于「挡/消」族：

| 动词 | 页 | 原文 |
|---|---|---|
| ausschließen | 261 | 「…die Prinzipien eng genug einschränkt, um alle Widersprüche **auszuschließen**」 |
| verschwinden | 262 | 「…daß die bisher bekannten ›Antinomieen‹ sämtlich **verschwinden**…」 |
| Wegfall | 264 | Richard 悖论「für unseren Standpunkt in **Wegfall**」 |
| beseitigt | 265 | 「…womit die ›Russellsche Antinomie‹ für unseren Standpunkt **beseitigt** ist」 |

还有一处容易被忽略、但分量很重：p262 Zermelo 自己写
「Selbst die gewiß sehr wesentliche ›Widerspruchslosigkeit‹ meiner Axiome
habe ich **noch nicht** streng beweisen können」——他**没有**声称证明了无矛盾性。

## 三、为什么这件事重要（与研究纲领的关系）

研究发起人的框架里，「宣布完成 ≠ 过程完成」。这一条把该模式**第一次落到了
原文措辞层**：一百多年后社区说的是「ZFC **解决**了罗素悖论」，而 Zermelo 本人
写的是「悖论**消失 / 被消除**」，且**自陈没有证明无矛盾性**。
词的更换不是措辞习惯问题——**「解决」是一个完成性谓词，「排除/消失」是准入性描述**，
前者声称的账，后者从来没有付过。

这不是我在替 Zermelo 谦虚，是他自己用的词。

## 四、Kanamori 给的另一半（见证据 04）

Kanamori 指出：Zermelo 1908a 的**第一个结果**就是「每个集合 M 都有一个子集
{x∈M : x∉x} 不属于 M」——即本包 **C-433**；而「**现代教科书通常走相反的路线**」，
用罗素悖论反证无全集。

也就是说：Zermelo 是**正面构造**出「缺失的那个子集」（准入层拒绝的精确形态），
教科书把它**重述成了反证法的悖论叙事**。叙事的转向发生在教科书这一层，
不在 Zermelo 那一层。

## 五、边界

- 证书 verdict 是 **PARTIAL**：Q1 这一问本身已核到原文，但整个步骤 2 未回答
  Q3 的命名史，故**不得**据此签发「不存在解决定理」的强负结论。
- OCR 含扫描/字体噪声（`Antinomiéen`、`ge[l]öst`），对外正式引用前建议对照原件再校一次。
- 过程中曾凭训练记忆写过数段德文引文（当时图像读取实际失败），**已作废**；
  本条所有引文来自 OCR。
