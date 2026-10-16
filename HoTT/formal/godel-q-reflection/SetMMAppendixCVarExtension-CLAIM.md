# C-369：`set.mm` Appendix-C 变量扩张的源绑定机器化控制

> **Proof package：** `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001`。
>
> **Claim：** `C-369`。
>
> **身份：** `MACHINE_PROVED_M_LEVEL_SOURCE_BOUND_VOCABULARY_EXTENSION`。

## 精确命题

令 `RawVar` 和 `rawVarType` 是由
`scripts/audit/generate_setmm_appendix_c_vocabulary.py` 从固定
`set.mm@160ebb63ec17ff00a809520a420c92914a424622` 的 `$v` / `$f`
声明所生成的 Lean 数据。该生成器固定：355 个不同 source variable、1474 个
不同 constant，以及 `wff=61`、`setvar=139`、`class=155` 的变量类型分布。

`SetMMAppendixCVarExtension.lean` 定义：

```text
ExtendedVar = raw RawVar | fresh RawType Nat
variableType : ExtendedVar → RawType
```

并由 Lean core 证明：

1. `rawEmbedding` 保持每个生成的 source variable 的 `$f` type；
2. `rawEmbedding` 为单射；
3. 对每个 source `RawType`，`freshFamily typecode : Nat → ExtendedVar`
   为单射，且每个像的 `variableType` 都是该 `typecode`；
4. 任意 `raw variable` 与任意 `fresh typecode index` 可区分；
5. 因而每一种 source variable type 都有一个显式的、可数无限的 fresh extension。

## 它对 G2 支付什么

这给出 Appendix C 所需的“有限 source vocabulary 不能直接当作无限 variable
universe、但可由 fresh family 扩张”的**M 层、源文件绑定正控制**。它直接对应
`ismfs` 中“每个 variable type 的 preimage 非有限”的一个构造性前置。

## 它没有支付什么

该包没有：

- 将 252,401 个 actual `set.mm` statements 的 frame 全部映入 `mAx`／`mStat`；
- 在 ZF／`set.mm` **内部**构造某个 `T ∈ mFS`；
- 将 47,917 条 external verified proof trace 译为 `mPPSt` 或 `mThm`；
- 定义或证明 actual `set.mm` checker 的内部 adequate `Prv`；
- 构造 quote、substitution、fixed point、target diagonal 或任何不完备性 theorem；
- 将 proof acceptance 与芝诺、圆环或 H0 的 `OriginDone`／`ρ`／completion bridge 关联。

所以 `C-369` 不能释放 G1、G3–G6，也不能把 M 层的 Lean 定理称为 ZFC 的对象语言定理。

## 控制与运行

- 正向源文件：`SetMMAppendixCVarExtension.lean`；
- machine-managed 输入：`SetMMAppendixCGenerated.lean`；它必须由生成器从 pinned raw source 重生并按字节匹配；
- 负控制：`WrongSetMMFiniteVocabulary.lean` 故意把 `raw v000` 写成
  `fresh wff 0`，必须被 Lean 拒绝；
- 当前 primary run 与负控制由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的 C-369 行拥有；
  该矩阵行而非本 claim 文件记录可变的 run ID，避免证明源码闭包因索引指针更新而漂移。

## 与当前源审计的关系

Appendix C 给出 database/frame 到 abstract formal-system component 的说明性
correspondence；[G2 source audit](../../../audit/20261004-GODEL-Q-REFLECTION-G2-SETMM-INTERNALIZATION-REQUALIFICATION.md)
说明它尚未提供 exact database 的内部 `mFS` witness。本包不把两者混同：它仅开始把
其中“无限 variable extension”这一个明确子义务写成可检查构造。
