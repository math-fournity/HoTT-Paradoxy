# ZFC-H0 总证明闭环：F1-C 原 CCHM 实现缺口与 clocked-cubical 候选

> **身份：** `RESEARCH_COGNITION_CLOSURE / M1_TARGET_SELECTION / SOURCE_AND_CODE_REVIEW / NOT_H0MAP`。
>
> **研究对象：** fixed Cubical Agda H0 的 native coinductive `Delay` 是否可进入一个具有 cubical set/presheaf semantics 的精确 target calculus。

## 1. 本项目自己的候选翻译

在阅读 candidate source 前，F1-B 已固定一个最小翻译义务。fixed H0 的 `Delay` 是 native `--guardedness` coinductive record，核心形状为：

```text
force : Delay A → A ⊎ Delay A
never.force = later never
runFor : ℕ → Delay A → Maybe A
```

若转向 clocked cubical theory，不能只说“二者均处理 coinduction”。必须实际给出：

```text
native Delay A
  -> guarded Delayκ A
  -> clock-quantified coinductive target
```

并证明 `force/later/never/runFor` 的有限观察保持；最后还要把该 map 同 H0 的 universe、EM1、HIT、h-level 依赖合成。预期反控制是：clock、`later` 或 tick 参数若不是 fixed H0 的输入，目标只是一条不同 variant，不能成为 H0Map。

## 2. 原 CCHM implementation 的直接代码审查

`mortberg/cubicaltt` 的 README 把该仓库描述为 experimental Cubical Type Theory implementation，并列出 path、composition/transport、univalence、identity types 及一些 HIT。其 reserved-keyword list 含 `data`、`hdata` 等，但不含 `record`、`coinductive` 或 clock construct。

更决定性的是其 `Exp.cf` grammar：declaration rule 只有 `DeclDef`、`DeclData`、`DeclHData`、`DeclSplit`、`DeclUndef`、`DeclMutual`、opaque/transparent；不存在 native record declaration 或 coinductive record rule。

因此，这一结论仅针对该具体版本的 implementation：

```text
ORIGINAL_CUBICALTT_IMPLEMENTATION_GAP_WITH_SCOPE
```

它表示 fixed H0 的 source term 不能直接作为该 implementation 的 term；它不证明抽象 CCHM cubical-set semantics 不可扩展，也不对 bare ZFC 作任何结论。

## 3. clocked-cubical 文献与开源接口对照

| candidate | 资料实际说明 | 对 fixed H0 的差别 |
|---|---|---|
| GCTT | guarded recursive types、later modality、guarded fixed point；以 cubical category × ω 的 presheaf 给语义。 | 单-clock GCTT 的递归对象含显式 `▷`；资料还将 clock quantification 视为得到 first-class coinductive types所需扩展。 |
| Clocked Cubical Type Theory / *Greatest HITs* | multi-clock guarded recursion 与 Cubical Type Theory/HITs 结合，给 denotational semantics；通过 clock quantification 编码 coinductive types。 | 有实际 coinductive encoding路线，但输入有 clocks/ticks；尚无 native Cubical Agda `Delay` 到它的 translation。 |
| Agda `--guarded` | tick/later 的语言接口，与 guarded Cubical Agda 相关。 | fixed H0 使用的是 `--guardedness` 的 coinductive-record productivity check，而非 `--guarded`；二者不能按标志名合并。 |

当前判词：

```text
CLOCKED_CUBICAL_COINDUCTION_SEMANTIC_CANDIDATE
NATIVE_UNGUARDED_DELAY_TO_CLOCKED_TRANSLATION_UNPAID
```

## 4. F1-C 的下一可验证动作

冻结一个 CCTT/CloTT source/version及其实际 grammar or implementation，建立 `H0ClockTranslationCard`：

```text
SourceType / TargetType / clock binder / later constructor /
force-later-never equations / runFor observation /
universe-HIT closure / translation theorem or exact missing rule
```

如果 source target 要求 H0 中没有的 clock parameter，或无法表达 native `Delay` 的 `force` record，它得到 `CLOCKED_VARIANT_GAP_WITH_SCOPE`。若一条 explicit translation 真实存在，才开始对其 preserve/reflect theorem 作原生机器化。

## 5. 一手来源与开源代码

- [CCHM paper](https://arxiv.org/abs/1611.02108)
- [original `cubicaltt` README](https://github.com/mortberg/cubicaltt)
- [original `cubicaltt` grammar](https://github.com/mortberg/cubicaltt/blob/master/Exp.cf)
- [GCTT](https://arxiv.org/abs/1611.09263)
- [Greatest HITs / Clocked Cubical Type Theory](https://arxiv.org/abs/2102.01969)
- [Agda 2.8 guarded type theory documentation](https://agda.readthedocs.io/en/v2.8.0/language/guarded.html)
- [Agda coinduction documentation](https://agda.readthedocs.io/en/v2.8.0/language/coinduction.html)
