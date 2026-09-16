# MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001：内部纤维替换导致 UIP 的最小两层机器构造

本包机器化 Annenkov–Capriotti–Kraus–Sattler 2017/2023 版 2LTT 论文 §2.7、Theorem 2.20 的核心推演。它使用一个边界保持的代数接口区分外层类型与内层 type code，使内层路径消去只能返回内层 code；因此，外层见证类型必须先经过 `R` 才能进入内层路径归纳。

固定假设如下：

- 外层是 Agda 的归纳等式 `E._≡_`，具有 J；外层 UIP 是显式字段 `strictUIP`；
- 内层由 `Inner`、`El`、`Idᵢ`、`reflᵢ`、受限 `Jᵢ` 与 `Πᵢ/lamᵢ/appᵢ` 给出；
- `R : Type → Inner`、`r` 与依赖消去器 `elimR` 分别对应 FORM-R、INTRO-R、ELIM-R；
- 证明不声明 COMP-R 字段，也不使用计算律。因此，本包证明的是论文假设的一个更弱子接口已经足以推出 UIP，而不是假定 COMP-R 后才得到结论。

## 冻结命题

| claim | 精确机器结果 |
|---|---|
| `C-227` | `strict-loop-canonical`：外层 UIP 经两次 `encode` 给出论文式 (2.14)。 |
| `C-228` | `lifted-witness`：把依赖内层路径 `p` 的外层 `StrictWitness` 统一送入 `R`，得到论文式 (2.13) 的机器对应。 |
| `C-229` | `based-uip` 收缩每个内层环路，`inner-uip` 由内层 Π 与 J 推出任意两个内层恒等证明相等。 |
| `C-230` | `replacement-excludes-nontrivial-loop`：若某个内层类型带一个不可收缩环路，则完整 replacement fragment 导出 `⊥`。 |
| `C-231` | 原生 Cubical 正反控制：Möbius family 证明 `S¹.loop ≠ refl`。这确认目标 HoTT 内层确有被 UIP 消灭的高阶结构。 |
| `C-232` | 消融正控制：在单一 Cubical universe 中，`NativeR X = X` 同时满足 FORM/INTRO/依赖 ELIM；因此只看到一个 R 形接口不够，关键条件是外层 UIP 桥与 `R` 在内层路径依赖语境中的统一可用性。 |

## 结论范围

本包将论文的 source-reported 结论提升为本项目中的机器核验条件定理：**上述最小两层 replacement fragment 蕴含内层 UIP，并排除任何非平凡内层环路。** `S¹.loop ≠ refl` 是原生 Cubical 控制，显示这与通常 HoTT 的高阶结构冲突。

它没有给出该 record 的模型，也没有把原生 Cubical `Type` 冒充成完整 2LTT 模型；抽象 fragment 与 `S¹` 控制之间的模型解释仍依赖论文给出的 2LTT 语义。它没有证明基本 2LTT 或 HoTT 自身矛盾。失败对象是把逐对象、通常不保 base change 的外部 fibrant replacement 提升为对任意上下文统一可用的内部 `R`。论文已经公开指出该限制以及 crisp/modal 规避方向，因此这不是“学界未想到的 HoTT BUG”。

对用户研究框架而言，它是一个强的方向 A/B 候选实例：逐对象外部操作可以存在；理论化的统一内化额外要求 context stability，并把外层 UIP 传播为内层 UIP。要升级成现实相对悖论，还需证明某个自然消费者确实要求这种错误提升，并给出与现实同一任务的正反执行对照；本包本身不完成该桥梁。
