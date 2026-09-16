<!-- governance-shard:v2
logical_id: LIT-HOTT-COMPUTABILITY-001
shard_id: 005
index: ../LIT-HOTT-COMPUTABILITY-001.md
-->

# 2LTT replacement机器结果与消费者下一步

## 机器结果

`MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` / C-227–C-232 已把 2LTT §2.7 的条件推演在 main 中机器化。形式化使用独立 inner code/`El`，使内层 `Jᵢ` 只能消去到内层 code；`R` 因而不能被宿主 Cubical Path 的更强消去规则绕过。

- C-227 对应论文式 (2.14)：outer UIP 使任意 strict loop 的编码等于内层反身路径；
- C-228 对应论文式 (2.13)：依赖内层路径 `p` 的外层 `StrictWitness p` 经 context-uniform `R` 成为内层 path-induction motive；
- C-229 从 ELIM-R 的常值族实例得到 based UIP，再由内层 Π/J 得到 full inner UIP；
- C-230 排除任何带非平凡 inner loop 的 replacement fragment；
- C-231 以原生 Cubical Möbius family 证明 `S¹.loop ≠ refl`；
- C-232 证明删去两层 strict-UIP 桥后，原生 `NativeR X = X` 具有 FORM/INTRO/dependent-ELIM 形状。

COMP-R 没有进入 record，说明 FORM-R、INTRO-R 与 ELIM-R 的子接口已经足以推出 UIP。run `20260915-MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001-01` 为 exit 0、stderr 0、index rows frozen、exact replay；Git 状态仍是 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。

## 判词

数学核现为 `MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE`。它不是 basic 2LTT/HoTT 的矛盾，也不是学界未想到的 HoTT BUG：Theorem 2.20 已公开指出该限制，并把不保 base change 与 crisp/modal 限制作为解释和规避方向。

它仍是方向 A/B 的强候选形状：模型侧逐对象 replacement 可以存在；理论把它提升为内部统一、对 context 自然的 type former后，新增的 uniformity 把外层 UIP 传播到内层并坍缩高阶结构。当前缺失的不是这条条件推演，而是一个预先存在的自然消费者以及现实/模型侧的同一任务比较。

## 下一 bounded successor

`NATURAL-CONSUMER-002` 以 C-227–C-232 为冻结数学核，调查并预注册：

1. 2LTT/HTS、Reedy fibrant replacement、semisimplicial types、modal/crisp type theory 与实现源码中，哪些调用者实际要求 `R` 作用于依赖内层路径的外层类型；
2. 调用者要求逐对象 replacement、稳定 reindexing、judgmental naturality、dependent elimination 中的哪一层；
3. 改成 crisp/outer-only 操作后，原任务是否仍可完成，支付的是显式参数、层级移动、外部选择还是丢失内部可替换性；
4. 现实/模型侧“逐例可做”与内部侧“统一可用”能否固定为同一 input、observation 与 completion，而不是把元层存在性换成对象层算法；
5. 若无 natural consumer，则把本候选封为 `KNOWN_INCOMPATIBLE_EXTENSION_BOUNDARY` 并返回 CE-MAP、Oracle、ambient R2 与完整 R4。

完整机器与距离审计见 `audit/2LTT内部纤维替换导致UIP机器证明与悖论判别-20260915.md`。
