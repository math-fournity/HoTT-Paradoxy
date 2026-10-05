# C-370–C-374：来源对应 cubical proof-code fragment

> **证明包：** `MP-CUBICAL-GODEL-FRAGMENT-001`。
>
> **理论身份：** 项目定义的 `CCTTmini₀`；它只与 cctt/redtt 的 Nat、`suc`、Path/refl
> 表面构造对应，不是任何上游实现的完整元理论。

## 精确命题

| Claim | Agda declaration | 精确范围 |
|---|---|---|
| C-370 | `positiveAccepted` | 固定 context `Nat ∷ []` 中，`reflC (sucC (varC 0))` 被 total certificate checker 接受。 |
| C-371 | `positiveWitness` | 该正例携带 `Deriv Γ₁ (erase positiveC) (Path Nat ... ...)` 的明确 typing derivation。 |
| C-372 | `illScopedRejected` | 空 context 中的 `varC 0` 被拒绝。 |
| C-373 | `wrongSucRejected` | `sucC (reflC zeroC)` 被拒绝，故 checker 不把路径证书误作 Nat certificate。 |
| C-374 | `checkedSound` / `checkSound` | 每一个成功 `Checked Γ c` 在类型中携带 `Deriv Γ (erase c) A`；对已返回的 accepted result 可消去得到该 derivation。 |

## 支付的桥

本包首次把下列有限片段放进同一个 machine-checked object：

```text
RawCert → erase → Tm
       → structurally recursive check
       → Checked carrying Deriv
```

它因此支付 GZ-008 的 **certificate syntax / structural checker / soundness** 子义务。

## 不支付

- 没有 Nat-valued Gödel编码、decoder、quotation 或 diagonal fixed point；
- 没有 general substitution、definitional equality、universe、Π/Σ、Glue、`coe`、`hcom`、HIT 或 univalence；
- 没有证明该 fragment 的 rules 与 cctt/redtt 完整语义等价；
- 没有 HoTT H0 transport、actual `Accept_ZFC`、`OriginDone` bridge、`SameFullQ` 或 bare ZFC 理论精度结论。

`WrongCCTTmini.agda` 是负控制：它要求已接受正例被拒绝，kernel 必须拒绝该伪命题。
