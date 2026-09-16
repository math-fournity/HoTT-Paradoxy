# MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001

## 固定身份

- proof ID：`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001`
- run ID：`20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01`
- claims：`C-223`–`C-226`
- source：`akaposi/cohtt@5babc385d01500c1777ff932dd8c79299a1d766a`，Git tree `13849af00ff393300c0ae6cdd47ba6ddfa0d1cd8`
- kernel：Agda 2.8.0-3d04bac，Cubical library v0.9

## 精确命题与边界

`C-223`：固定 groupoid syntax 是一个四 sort 的 Cubical Agda HIIT 编码：`Con`、`Sub`、`Ty`、`Tm`；它显式包含 substitution/composition、terminal context、context extension、`U/El`、Π、`lam/app`、β/η，以及 `U/El/Π` substitution 与 composition/identity 的二阶 coherence。`Sub` 与 `Tm` 构造时即为 set，`Ty` 构造时只要求 groupoid。

`C-224`：作者的 α-normalisation 模块机器证明：

```agda
isSetTy : (Γ : Con) → isSet (Ty Γ)
```

证明把 `Ty Γ` 作成 normal type `NTy Γ` 的 retract，再由 `isSetNTy` 得到 setness。

`C-225`：`TT.Groupoid.IsoSet` 构造 `isoCon`、`isoSub`、`isoTy`、`isoTm`，把 groupoid syntax 的四个 sort 与 set syntax 的相应 sort 对应；项目探针逐项重述这些类型并由原定理填充。

`C-226`：作者 `TT/README.agda` 所列全部 20 个当前 TT 模块与项目探针，在固定 Agda/Cubical 工具链下从源重放成功。上游 `cohtt.agda-lib` 缺 `name:`；重放 wrapper 只补 library name，并保留其 include/depend/flags。由于 `--hidden-argument-puns` 会使 Cubical v0.9 源码本身在全量 fresh 模式下重新解析失败，重放先用安全 cubical 基线生成固定依赖接口，再删除全部 cohtt 接口，按上游 flags 重新检查 20 个 cohtt 模块与探针。

## 不能推出

这个 exact slice 的对象理论只有 Π、一个 universe `U/El` 与参数化 base family；它没有自然数、一般 identity type、对象层 univalence、HIT、证明谓词、proof-code enumerator、conversion decider 或 arithmetic interpretation。因此它是 `G-HOTT-SYNTAX-001` 的首个 exact machine-replayed syntax slice，不是完整 HoTT calculus，也不证明 R4 不完备性。

论文的 setness／isomorphism 结果是 syntax/metatheory 边界证据，不是现实相对悖论。它反而显示：为了让 univalent models 与传统 set syntax 共存，作者显式加入 groupoid truncation 与二阶 coherence，再机器证明 syntax 落回 set；是否由这种经济安排产生 natural consumer 失配仍未发现。
