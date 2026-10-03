# HMZ-001：R-Cards — HoTT 创建动机的来源报告

> **阅读规则：** 每张卡只报告来源真的说了什么，并保留其限定词。卡片下的“反投影意义”是本项目的解释，不能回写成作者关于 ZFC 的断言。

## HMZ-R-001 — 基础语言与日常机器验证

```text
source identity:
  HMZ-S-003, Voevodsky 2014 IAS slides 15–18;
  corroborated by HMZ-S-004, IAS 2014 Origins page.
exact locator:
  HMZ-S-003 derived text lines 241–300 (slides 15–18).
claim class:
  CONTRASTIVE_CRITIQUE + CAPABILITY_GOAL.
literal minimum:
  “languages of Predicate Logic ... are too limited”; existing foundations
  could not “directly express” the cited 2-theory objects.
source-reported motivation:
  Voevodsky ties the desired foundation to a language usable in ordinary
  mathematical work and precise enough for computer verification, not merely
  a consistency standard for a few base theorems.
what the source does not claim:
  No internal contradiction of ZFC; no theorem that ZFC cannot encode every
  cited object; no Power Set/Replacement/Extensionality diagnosis; no P-shaped Q.
linked Z cards:
  HMZ-Z-002, HMZ-Z-003.
```

**反投影意义。** 这是一个关于语言、表示和日常使用的动机，不是一条“ZFC 没有某对象”的命题。它要求寻找的
是一个同一工作任务中，某个 ZFC 表达或形成方式把“可被使用的对象”过早交付的来源；在找到该任务前，只能停为
`Z_SIDE_UNDER_SPECIFIED`。

## HMZ-R-002 — 直接公理化 homotopy types，而非把它们还原为集合

```text
source identity:
  HMZ-S-002, Voevodsky 2010, PDF pp. 1–2.
exact locator:
  PDF p. 1, “key features” items 1–4; p. 2, direct formalization paragraph.
claim class:
  NOVEL_OBJECT_LANGUAGE + CAPABILITY_GOAL.
literal minimum:
  direct axiomatization of “the world” of homotopy types “instead of the world of sets”.
source-reported motivation:
  Higher/categorical mathematical thinking should be natively axiomatized and
  formalized in dependent type systems.
what the source does not claim:
  It does not say that ZFC is inconsistent, that ZFC cannot represent homotopy
  types by encodings, or that a set produced by ZFC lacks a formation certificate.
linked Z cards:
  HMZ-Z-002, HMZ-Z-005.
```

**反投影意义。** “instead of sets”提出的是对象语言和表示层的竞争，而不是自动给 Power Set、集合形成或
集合存在造成一个未支付义务。HoTT Book 的内部累计层级是这一点的直接反控制。

## HMZ-R-003 — 结构同一性与 conventional foundations 的官方立场

```text
source identity:
  HMZ-S-001, HoTT Book introduction.tex:15–24;
  HMZ-S-006, PDF p. 3 / derived lines 139–150.
exact locator:
  HoTT Book introduction.tex:17–19; APW 2013, p. 3.
claim class:
  CONTRASTIVE_CRITIQUE + REPRESENTATION_COST.
literal minimum:
  isomorphic structures can be identified, despite incompatibility with the
  “official” doctrines of conventional foundations.
source-reported motivation:
  Univalence makes an identification common in mathematical practice part of
  the foundational language, while retaining structure in the ways an
  identification is made.
what the source does not claim:
  It does not assert that all set-theoretic mathematics treats any two
  isomorphic structures as equal, that ordinary Choice promises a natural
  representative, or that a universal family follows from a coarse classifying object.
linked Z cards:
  HMZ-Z-001.
```

**反投影意义。** 这是首批来源中最接近 `H0 → Z0` 的入口，但也最容易把“任选代表”偷换为“自然地、兼容地
给出代表”。Mumford 的消费者是本轮立即执行的反控制。

## HMZ-R-004 — 高阶对象的直接逻辑描述

```text
source identity:
  HMZ-S-001, HoTT Book introduction.tex:18–24;
  HMZ-S-006, PDF pp. 3–4 / derived lines 155–166.
exact locator:
  HoTT Book introduction.tex:18–19; APW 2013, p. 4.
claim class:
  NOVEL_OBJECT_LANGUAGE + CAPABILITY_GOAL.
literal minimum:
  higher inductive types provide “direct, logical descriptions” of basic
  homotopy spaces and constructions; the Book says the two ideas are not
  captured *directly* in classical set-theoretic foundations.
source-reported motivation:
  Spheres, cylinders, truncations and localizations can be formed and reasoned
  about by native type-theoretic principles.
what the source does not claim:
  “not directly” is not “cannot be encoded”; it does not single out a ZFC
  axiom, a self-reference, or a universal execution/formation operator.
linked Z cards:
  HMZ-Z-002, HMZ-Z-004.
```

**反投影意义。** 本卡要求未来调查 representation cost 和实际 consumer，而不是将“直接”解释成已证明的
ZFC 不能完成性。

## HMZ-R-005 — 可被 proof assistant 实现的基础

```text
source identity:
  HMZ-S-001, HoTT Book preface.tex:91–92;
  HMZ-S-002, PDF pp. 1–2 and p. 9;
  HMZ-S-006, PDF pp. 3–5.
exact locator:
  preface.tex:91–92; Voevodsky 2010 p. 2 (Coq foundations) and p. 9
  (constructiveness discussion); APW 2013 p. 4–5.
claim class:
  CAPABILITY_GOAL + HISTORICAL_CONTEXT.
source-reported motivation:
  UF is tied to a mathematics foundation implementable in a computer proof
  assistant; the Book reports that some material was first developed in that
  formal setting.
what the source does not claim:
  It does not say that every mathematical existence proof must yield an
  executable object, that all ZFC use is noncomputable, or that a proof assistant
  timeout reflects a ZFC theorem.
linked Z cards:
  HMZ-Z-003.
```

**反投影意义。** 这条卡与项目的计算／存在张力有关，但它首先要求严分：ZFC 的对象语言、ZFC 的证明论、
proof assistant 的实现和具体数学家的交付任务。没有这种分层，不允许把“机器友好”直接反投为 ZFC 的 Q。

## HMZ-R-006 — 兼容与反向控制：HoTT 内的累计层级

```text
source identity:
  HMZ-S-001, HoTT Book setmath.tex:7–27 and 1755–1760.
claim class:
  HISTORICAL_CONTEXT + CONTROL.
source-reported fact:
  The Book distinguishes HoTT sets from ZF sets, investigates an internal
  cumulative hierarchy V, and states a model-of-ZFC-with-choice theorem under
  additional assumptions.
what it controls:
  A contrastive UF motive cannot be read as a blanket claim that ZFC is
  inexpressible, unavailable or already refuted.
linked Z cards:
  HMZ-Z-005.
```

这张卡不是 “HoTT 对 ZFC 的批评”，而是防止本项目把两种基础的竞争性叙述夸张成不兼容或漏洞结论。
