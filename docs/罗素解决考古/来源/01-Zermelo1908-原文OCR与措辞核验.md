# 证据 01：Zermelo 1908 原文措辞核验（OCR 客观提取）

> **来源身份**：DOCUMENTED_SOURCE（扫描原件 + 机器 OCR）。
> **原件**：E. Zermelo, *Untersuchungen über die Grundlagen der Mengenlehre. I*,
> Mathematische Annalen 65 (1908), 261–281。
> **获取**：GDZ（Göttinger Digitalisierungszentrum）IIIF，PPN235181684_0065，
> canvas 270–290（= 印刷页 261–281），2000px 宽 JPEG。
> **图像端点**：`https://manifests.sub.uni-goettingen.de/iiif/image/gdz:PPN235181684_0065:<8位序号>/full/2000,/0/default.jpg`
> **OCR 方法**：macOS Vision（VNRecognizeTextRequest，accurate，de-DE + en-US，
> usesLanguageCorrection=false），本地工具 `/tmp/vnocr`。OCR 文本落
> `搜索原始响应-20261017/zermelo1908-pages/ocr/pNNN.txt`。
> **抓取/处理时间（UTC）**：2026-10-17T05:36:14Z

## 1. 页面 SHA-256（前 16 位）

| 印刷页 | 文件 | sha256[:16] |
|---|---|---|
| 261 | zermelo1908-pages/p261.jpg | e1f64c5ac69cb037 |
| 262 | zermelo1908-pages/p262.jpg | 36f30c1c12963520 |
| 264 | zermelo1908-pages/p264.jpg | f46a33bf9442e48c |
| 265 | zermelo1908-pages/p265.jpg | dc9d3c190afda37c |

## 2. 关键段落逐字（OCR 原文，含 OCR 噪声，未润色）

### 2.1 p261（首页，论文纲领）—— Aufgabe 的 Lösung，不是悖论的 Lösung

> „Nun scheint aber gegenwärtig gerade diese Disziplin in ihrer ganzen Existenz
> bedroht durch gewisse Widersprüche oder »Antinomiéen«, die sich aus ihren
> scheinbar denknotwendig gegebenen Prinzipien herleiten lassen und bisher noch
> keine allseitig befriedigende **Lösung** gefunden haben."

> „Diese Aufgabe muß in der Weise ge[l]öst werden, daß man die Prinzipien einmal
> eng genug einschränkt, um alle Widersprüche **auszuschließen**, gleichzeitig aber
> auch weit genug ausdehnt, um alles Wertvolle dieser Lehre beizubehalten."

**要点**：`Lösung`/`gelöst` 在本页出现，但主词是 **„diese Aufgabe"**（这项任务），
且前一处的 Lösung 说的是悖论**迄今还没有**令人满意的解决。纲领动词是
**ausschließen**（排除矛盾）。

### 2.2 p262 —— 已知悖论「全部消失」

> „Selbst die gewiß sehr wesentliche »Widerspruchslosigkeit« meiner Axiome habe ich
> noch nicht streng beweisen können, sondern mich auf den gelegentlichen Hinweis
> beschränken müssen, daß die bisher bekannten »Antinomieen« sämtlich
> **verschwinden**, wenn man die hier vorgeschlagenen Prinzipien zugrunde legt."

**要点**：Zermelo 自己**没有**声称证明了无矛盾性（Widerspruchslosigkeit）；他只说已知悖论
**消失**（verschwinden）。

### 2.3 p264 —— Richard 悖论「失效」

> „…und damit die »Antinomie Richard« oder die »Paradoxie der endlichen Bezeichnung«
> … für unseren Standpunkt in **Wegfall**."

### 2.4 p265（定理后的考古关键句）—— 罗素悖论「被消除」

> „Aus dem Theorem folgt, daß nicht alle Dinge x des Bereiches B Elemente einer und
> derselben Menge sein können; d. h. der Bereich B ist selbst keine Menge, – womit
> die »**Russellsche Antinomie**« für unseren Standpunkt **beseitigt** ist."

**要点**：描述罗素悖论命运的动词是 **beseitigt**（被消除），且带限定语
**„für unseren Standpunkt"**（就我们的立场而言）。

## 3. 全 21 页词汇穷尽检索（客观，非记忆）

检索式：`lös*|gelöst|Lösung|beseitig*|ausschlie*|Ausschließung|vermeid*|verschwind*|Wegfall`

| 词 | 印刷页 | 是否指悖论 |
|---|---|---|
| Lösung | 261 | **否**——「迄今还没有令人满意的解决」 |
| gelöst | 261 | **否**——「这项任务必须这样被解决」 |
| auszuschließen | 261 | 是（纲领：排除一切矛盾） |
| verschwinden | 262 | **是**（已知悖论全部消失） |
| vermeidet | 262 | 否（避免形式上使用基数） |
| Wegfall | 264 | **是**（Richard 悖论失效） |
| beseitigt | 265 | **是**（罗素悖论被消除） |
| verschwinden/verschwindet | 266 | 否（乘积为零的数学用法） |
| verschwindenden | 269 | 否（非空集合） |
| vermeidet | 272 | 否（证明手法的比较） |

**结论（Q1）**：全文中 `lösen`/`Lösung` 从未以「悖论被解决」为主词出现；
描述悖论命运的动词是 **ausschließen / verschwinden / Wegfall / beseitigen**。

## 4. 诚实性注记

本文件第 2 节引文全部来自上述 OCR，未经记忆重构。工作过程中曾出现过一段
**凭训练记忆写下的德文引文**（未 OCR 核对），已作废，不作为证据；本文件是取代它的
客观版本。OCR 含扫描/字体噪声（如 `Antinomiéen`、`ge[l]öst`），忠实保留未润色；
正式对外引用前建议对照 GDZ 原件图像再校一次。
