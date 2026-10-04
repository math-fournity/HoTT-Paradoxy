# ZFC-H0 总证明闭环：F1-E Guarded Cubical Agda forcing-ticks 与 Clocked Lift

> **身份：** `RESEARCH_COGNITION_CLOSURE / M1_EXACT_TARGET_QUALIFICATION / SOURCE_AND_TYPECHECK_ATTEMPT / NOT_H0MAP`。
>
> **冻结 source：** `agda/guarded` branch `forcing-ticks`，commit
> `cf0c438214cb10874ac1a7650f8d0d69677db57e`。
>
> **结论状态：** `CLOCKED_LIFT_SOURCE_PRESENT / FORCING_TICKS_COMPILER_VARIANT_GAP_WITH_SCOPE / CLOCKED_LIFT_POSTULATE_BOUNDARY / NATIVE_H0_TO_CLOCKED_TRANSLATION_UNPAID`。

## 1. 本项目的先验问题

GCTT prototype 的 clocked CoNat 已经显示一个类比；但 H0 需要更强的东西：不仅有
`▷κ`，还要有能把 clock-indexed delayed continuation 收回为无显式 clock 的 observation，
并使 finite `runFor` 的结果保持。检验目标是：

```text
Does an exact clocked Cubical Agda source supply
  (i) clock / tick / forcing-tick primitives,
  (ii) guarded Lift or coinductive Delay carrier,
  (iii) a force operation, and
  (iv) an actual typechecker compatible with the source?
```

即使四项全有，也还必须检查 native Cubical Agda H0 的 `Delay`、universe、EM1、HIT 和
finite trace 是否能翻译；这张卡不预先假定答案。

## 2. 冻结源码中实际存在的 clocked Lift 路线

`src/Clocked/Primitives.agda` 使用 `Cl`、`Tick`、`FTick`、forcing tick `◇`、
`▹ k A`、`force` 与 `prev` 所需的 primitives。`force` 的精确形状是：

```text
force : (∀ k → ▹ k (A k)) → ∀ k → A k
```

`src/Clocked/Lift.agda` 定义：

```text
data Lift (k : Cl) (A : Set) where
  now  : A → Lift k A
  step : ▹ k (Lift k A) → Lift k A
```

再定义 `∀Lift A` 与 coinductive record `∀Lift' A`，其中 `now/step` 的递归结构、`out∀`
到 `∀ k → Lift k A` 的投影、以及由 clocks/forcing ticks 回收 delayed branch 的过程都在源码中。
这比“某篇论文说可处理 coinduction”强：它给出了接近 H0 `Delay` 的实际类型构造与 operation shape。

但同一文件还显式写出：

```text
-- Assuming clock irrelevant A.
postulate
  in∀       : (∀ k → Lift k A) → ∀Lift A
  out-in-∀  : out∀ (in∀ m) ≡ m
```

因此 source 本身没有把 `out∀ / in∀` 的完整反向充分性作为无前提内核定理交付。这个 postulate
boundary 必须保留，不能把它写成 full Delay equivalence 或 H0Map。

## 3. 当前 Cubical Agda 的实际类型检查

该库 README 明确要求 Agda 的 `forcing-ticks` branch。为区分“本机 Agda 完全没有相关语法”与
“本机不是该 exact compiler variant”，我在项目固定 Cubical Agda 2.8.0-3d04bac 上实际运行：

```text
agda --ignore-interfaces --library-file=... -l cubical-0.9 \
     -i <guarded>/src <guarded>/src/Clocked/Lift.agda
```

结果如下：

1. `--help` 显示当前 compiler 有 `--guarded` 与 `--guardedness` 两个不同开关；
2. checker 开始读取 `Clocked.Lift` 和 `Clocked.Primitives`，说明普通 Cubical/guarded syntax
   不是在 parse 前被拒；
3. 随后出现 `Ignoring unknown attribute: @ftick`，并在 `FTick : Cl → LockU` 的 declaration 处以
   `[InvalidTypeSort] funSort Set LockU is not a valid sort` 停止，exit `42`。

这说明本机的 fixed Cubical Agda 2.8.0 不实现此 source 所依赖的 forcing-tick primitive interface。
它**不**证明 forcing-ticks compiler 不存在，也不反驳 source 的 intended semantics；它精确证明了：

```text
CURRENT_CUBICAL_AGDA_2_8_0_NOT_THE_FORCING_TICKS_VARIANT_REQUIRED_BY_THIS_SOURCE
```

### 3.1 尝试构建 README 指定的 matching compiler

没有把“请用 forcing-ticks branch”当成不可操作的文献建议。我冻结并检出
`agda/agda@forcing-ticks:5bec849bec6c7aa40e068db99c5a1f5eab47a874`，该 branch 的
`src/full/Agda/TypeChecking/Primitive/Cubical.hs` 确实含 `FORCINGTICK`、`primForcingApp`、
`primForcingAppDep` 等 target primitives。

其自带 `stack-9.0.1.yaml` 要求 GHC 9.0.1；Stack 在 macOS ARM 上没有该版本的 setup，首先得到
`S-9443`。仓库也给出并声明支持 `stack-8.10.7.yaml`，因此我在隔离的
`/Users/aurolafly/.cache/agda-forcing-ticks-stack-5bec849/` 下载 GHC 8.10.7，而不触碰系统 GHC。
该 setup 在 configure 阶段因本机只有 Command Line Tools、没有完整 Xcode 的 `xcodebuild`，以
exit `77` 停止：`C compiler cannot create executables`。

因此当前可观察事实是：matching compiler source 和 primitives 已冻结、build 已真实启动并在环境配置处
失败；还没有得到 matching compiler binary，也没有运行 `Clocked.Lift.agda` 成功。这个状态必须写成：

```text
FORCING_TICKS_COMPILER_BUILD_ATTEMPTED
MATCHING_COMPILER_BUILD_BLOCKED_BY_LOCAL_XCODE_TOOLCHAIN_WITH_SCOPE
```

它不改变 source-level `Lift/∀Lift` 或 postulate 判断，也不能被解释为 Agda forcing-ticks 理论不一致。

## 4. 对 H0Map 的影响

| H0 map 字段 | 此 source 支持 | 尚未支付 |
|---|---|---|
| delayed constructor | `Lift k A` 的 `now/step` 直接给出。 | native H0 `Delay A` 到 `∀Lift A` 的 translation。 |
| coinductive carrier | `∀Lift'` 是显式 coinductive record。 | target 的 complete no-postulate equivalence/adequacy。 |
| force-like observation | forcing ticks 与 `force` 在 primitives 中定义。 | H0 `force : Delay A → A ⊎ Delay A` 的 exact correspondence。 |
| finite observation | `Lift`/relation/lemma infrastructure存在。 | `runFor` definition 与每个 fuel 的 trace-preservation theorem。 |
| target compiler | README 指向 matching forcing-ticks branch。 | 本机只有 different compiler variant；还未 typecheck source under matching compiler。 |
| H0 library closure | 与 Cubical Agda 有 surface relation。 | exact H0 `EM₁`、suspension、truncation、h-level/universe and `QuestioningDelay` map。 |

所以本 target 新增了一条有价值的 M1 路线，但不关闭 M1：

```text
CLOCKED_LIFT_SOURCE_PRESENT
FORCING_TICKS_COMPILER_VARIANT_GAP_WITH_SCOPE
CLOCKED_LIFT_POSTULATE_BOUNDARY
M1_FULL_H0MAP_UNPAID
```

## 5. 下一可判别动作

下一动作必须在以下两项中选一项，而不是继续扩大“clocked”关键词：

1. 取得 README 指定、版本固定的 Agda forcing-ticks compiler，并在隔离 source tree 中重跑
   `Clocked.Lift.agda`；随后构造最小 `ClockedDelay`，将 `now/step/force` 同 fixed H0 的
   `force/later/never/runFor` 逐字段比对；
2. 若 source 的 `in∀ / out-in-∀` 必须保留 postulate、或 exact forcing-ticks target 仍不能承载
   native H0 closure，登记`CLOCKED_LIFT_ADEQUACY_GAP_WITH_SCOPE`，再向另一个 exact semantic target
   迁移。

任何结果都不能由 `Lift` 与 `Delay` 名义相像直接推出 H0Map。

项目内已准备 `ClockedLiftDelayControl.agda` 和错误控制文件，精确提出 target-side
`force/never/runFor/never-silent`。它们目前是 `UNRUN_CANDIDATE_SPECIFICATION`：只有 matching
compiler 实际接受或拒绝后，才可进入 claim matrix；在此之前不是机器证明。

## 6. 入口

- [frozen forcing-ticks source](https://github.com/agda/guarded/tree/cf0c438214cb10874ac1a7650f8d0d69677db57e)
- [Clocked Lift](https://github.com/agda/guarded/blob/cf0c438214cb10874ac1a7650f8d0d69677db57e/src/Clocked/Lift.agda)
- [Clocked primitives](https://github.com/agda/guarded/blob/cf0c438214cb10874ac1a7650f8d0d69677db57e/src/Clocked/Primitives.agda)
- [repository README](https://github.com/agda/guarded/blob/cf0c438214cb10874ac1a7650f8d0d69677db57e/README.md)
