# 截断不可恢复族与 unlabeled 二元素无规范选点（C-134–C-147）

本目录同时承载两个已索引的原生 Cubical Agda proof package：

| proof id | 覆盖 claim | 源码 | 状态 |
|---|---|---|---|
| `MP-TRUNC-NORECOVERY-001` | `C-134`–`C-141` | `TruncationNoRecovery.agda` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY` |
| `MP-NOCANONICAL-001` | `C-142`–`C-148` | `NoCanonicalPoint.agda`（bridge：`NoCanonicalFinite.agda`） | `MACHINE_PROVED_LOCAL_UNCOMMITTED / UNLABELED_FINITE_NO_CANONICAL_POINT` |

两个包都不新增“HoTT 悖论”结论。`TruncationNoRecovery.agda` 保持字节冻结，使 `-01`/`-02`/`-03` 三个 run 的 source pinning 与行稳定性继续成立；新 claim 只做 append（`C-142`+），新源码进入独立模块。

## MP-TRUNC-NORECOVERY-001（C-134–C-141，摘要）

- `C-134`（`pointConstructorsForceEquality`）：任意源 `A`、集合 `S`、实现 `h : A → S`、读出 `g : ∥ A ∥₁ → S`，若 `g` 在每个 point constructor 上与 `h` 一致，则任意两点 `h a₀ ≡ h a₁`。
- `C-135`（`noPointRecovery`）：加上分离见证后，`g` 与逐点保持证明不可能共存。
- `C-136`/`C-137`：Bool 与 ℕ 两个实例（分离对 `false/true`、`0/1`）。
- `C-138`（`propositionValuedTestExists`）：正控制——目标是 mere proposition 时同一形状完全可用。
- `C-139`（`noSectionCandidate`）/`C-140`（`noCompletionCandidate`）：把上述内容写成理论内部的“完成候选类型为空”。
- `C-141`（`isFinSetLikeNoUniformEnumeration`）：`isFinSet` 形状接口（`Σ n × ∥ A ≃ Fin n ∥₁`）的统一枚举读出不存在。

机制：`squash₁` 是任意两个 point constructor 之间的路径，`cong g` 把它带到目标；递归子 motive 可用只因“集合中的路径类型是命题”（`isOfHLevelPath'`）。

## MP-NOCANONICAL-001（C-142–C-148，unlabeled 二元素无规范选点）

本包是本 repo 内对派生开发文件 `HoTT/formal/agda-unimath/hott-z/NoCanonicalPoint.agda`（即 agda-unimath 的 `no-section-type-2-Element-Type`：`¬ ((X : 2-Element-Type l) → type-2-Element-Type X)`）所携带**命题**的原生重放。库本体不在本 repo，派生文件仍按 `SOURCE_REPORTED_NOT_REPLAYED` 登记；本模块用固定工具链自带的原语把同一命题重新机器化。

- `C-142`：unlabeled 呈现 `Σ[ A ∈ Type ] ∥ A ≃ Bool ∥₁` 以及由 swap 自同构 `notEquiv` 诱导的**非平凡自识别** `swapSelfIdentification : identityPresentation ≡ identityPresentation`；其 carrier 分支是 `ua notEquiv`，标签分支由截断的命题性填满。
- `C-143`（`sectionRespectsSelfIdentification`）：该族的任何 section 必须尊重族自身的识别（`subst` 形式的相干义务）。
- `C-144`（`uniformChoiceFixedPoint`）：把 C-143 与 `uaβ notEquiv` 复合后，任何假想的统一选点都被迫成为 `not` 的不动点：`not (u X) ≡ u X`。
- `C-145`（`noUniformChoice`）：因此不存在对所有 unlabeled 二元素呈现的统一选点（与 agda-unimath 命题同内容）。
- `C-146`（`labeledChoice`）：正控制——保留标签数据（`Σ[ A ∈ Type ] (A ≃ Bool)`）时规范选点存在；围栏来自被遗忘的标签，而非二元素载体。
- `C-147`：界面把 id-标签与 swap-标签识别为一（`labelingsIdentified`），而两个标签作为数据仍然不同（`labelingsDistinct`）；两条合起来精确刻画截断遗忘的是什么。
- `C-148`（`uaNotEquivNotRefl`）：该自识别的 carrier 分支不是恒等路径（`ua notEquiv ≡ refl → ⊥`），故它是非平凡自识别。

机制围栏：本包的负结论依赖 univalence（`ua notEquiv` 给出非平凡 carrier 路径）与截断的命题性（使标签分支可被填满、并让该路径成为**自**识别）。若去掉截断、保留标签为数据，则自识别消失且正控制存在（C-146）。

### N38 → N40 纠偏记录

N38 探针曾把 `(s : (b : Bool) → carrier (boolPresentation b)) → s false ≡ s true` 记为“正确的常量形式”。该陈述按字面为假：呈现族在定义上常量，类型就是 `Bool → Bool`，`s = id` 即构成反例；普通 dependent function 不携带相干义务，任何消去器形状都无法修复它。正确内容是上述“统一选点不存在 / 不动点义务”命题——它不是消去器 β 归约问题，而是相干义务问题。

## 工具链与运行

- Agda 2.8.0-3d04bac（官方 release asset，发布方 SHA-256 校验）+ Cubical v0.9（tag commit 固定、source-tree 确定性哈希 `73ccfbaf…`）。
- 两包源码均在 `{-# OPTIONS --safe --cubical --guardedness #-}` 下通过；精确命令与原始输出见 `HoTT/verification/runs/<run-id>/`。
- 两个包都不依赖 postulate、choice 或经典原理。

## 不能推出

不证明 HoTT 内部矛盾；不证明“现实的完成性”或物理时间结论；不证明任何具体派生开发误用该接口；不把 `DEFENSE_WORKS` / 资格边界升级为 `NATURAL_USAGE_MISMATCH`；E6（真实自然使用链）仍在别处审计。
