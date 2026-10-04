# G2：`set.mm` 的对象层编码与 provability 边界重资格化

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **身份：** `EXACT_DATABASE_VERIFIER_REPLAY + SOURCE_INTERNALIZATION_INSPECTION / NOT_A_BARE_ZFC_THEOREM`。

> **判词：** `SET_CODED_FORMULA_AND_GENERIC_FORMAL_SYSTEM_ASSETS_SOURCE_VERIFIED / ACTUAL_SETMM_INTERNAL_PRV_AND_DIAGONAL_NOT_PAID`。

## 1. 为什么这会修正 G0 的来源判断

此前 G0 正确地冻结了 `set.mm` 的外部 proof-acceptance interface，却把它内部已有的 ZF 级语法资源概括得过窄。冻结 revision `160ebb…` 实际包含：

1. 用集合编码的一阶公式、有效公式集和 satisfaction construction；
2. 用集合定义的 generic Metamath formal system、substitution、closure、provable pre-statement 和 theorem；
3. 一个抽象 provability-logic fragment，含 conditional Baby Gödel / Löb consequences。

这些是 G2 的真实 source assets，不能因它们不是完整结果而被忽略。另一方面，source 本身把最关键的实例化义务写得很清楚：`Prv` 是 lacking a definition 的 primitive；为有效理论构造满足 HBL 条件的 predicate 和 Gödel sentence “is still a project”。

## 2. 精确数据库与 verifier replay

数据库是 `metamath/set.mm@160ebb63ec17ff00a809520a420c92914a424622`。下载到项目外 `/Volumes/D` 缓存后，强 ETag、51,466,065-byte length、本地 SHA-256 和 Git tree 的 blob SHA-1 均交叉一致。

固定 `metamath-exe@9898f5d1bb27045d764dd01672862a1c2a3b4f5e` 用 Apple clang 编译成功；随后对该 exact database 运行 `VERIFY PROOF *`，exit `0`。输出报告：

```text
252401 statements
3072 $a statements
47917 $p statements
All proofs in the database were verified in 9.21 s.
```

完整命令、环境、hash、stdout 与空 stderr 均在 [run receipt](../HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/RUN.json)。

这个 run 证明的是**这个外部 verifier 接受该精确数据库中的形式 proof**。它不证明 ZFC 的模型论 soundness、ZFC 一致性，或任何从形式 proof validity 到芝诺／圆环／H0 的完成桥。

## 3. 对象层已经支付的资源

| GodelizationCard 字段 | `set.mm` 的直接 source asset | 证据标签 | 支付范围 |
|---|---|---|---|
| `Code` | ZF 内的 Gödel-set formula code、`Fmla` 与递归 satisfaction | `df-goel`、`df-goal`、`df-fmla`、`fmla` | 支付 set-coded formula syntax，不等于 actual database 的全部 proof code。 |
| `ObjectCodeBridge`（部分） | 公式 code 是 ZF 内 set object，变量 indices 位于 `ω`；satisfaction 定义按 formula height 递归 | 同上、`fmlasuc` | 这是真实的**set-code**路线；它说明“code 必须是 numeral”只适用于 arithmetic specialization。 |
| generic `Check` / theorem relation | `mFS`、`mSubst`、`mCls`、`mPPSt`、`mThm` 以 ZF set object 形式定义 | `df-mfs`、`df-mpps`、`df-mthm` | 对 generic Metamath formal systems 的内部 representation。 |
| finite witness | theorem 有可定义的 provable-pre-statement witness，且有 finite DV witness variant | `mthmpps`、`mthmppsfi` | 对 `T ∈ mFS` 的 generic theorem/proof relation 强化；仍不是 source mapping。 |
| external acceptance | full pinned database verifier replay | current run receipt | 接受整个 actual proof database。 |

## 4. 仍未支付的关键桥

### 4.1 actual `set.mm` 到 internal formal-system object 的 mapping

formal-system section 的注释说它描述的 formal system “of which set.mm is one”。但在精确 section 与全文件针对 `set.mm` / `setmm` / `mFS` / `mThm` / `mPPSt` 的 source scan 中，没有发现一个 source-declared object把当前 database本身构造成明确的 `T ∈ mFS` instance。这个是**受扫描范围限定的 source gap**，不是数学上不存在编码的结论。

### 4.2 `Prv` 与 InternalProvabilityAdequacy

provability-logic section 明文规定：

```text
Prv is a primitive expression lacking a definition.
We do not construct this predicate in this section; this is still a project.
```

`ax-prv1`–`ax-prv3` 因而是加入的 derivability assumptions；`bj-babygodel` / `bj-babylob` 是在给定 Gödel/Löb sentence 和 `Prv` 条件下的 conditional consequences。它们不把 `Prv` 证明为 actual `set.mm` proof checker 的内部 adequate representation，也不构造相关 sentence。

### 4.3 Diag、OriginDone 与现实桥

没有当前 source 将 generic formula code用于一个 actual `set.mm` Gödel sentence，也没有 `Accept_set.mm → OriginDone_Zeno/Circle/H0` 的 source contract。故这轮不能启动 G3、G4、G5 或 parent-Q attribution。

## 5. 对方案的实际改变

此前的 `NumeralBridge` 现在被一般化为 **`ObjectCodeBridge`**：

```text
arithmetic target: code → numeral / term in T
set-theoretic target: code → internal set/class object and usable formula position in T
```

G2 的 Metamath 子路线由此获得一个真实源头：它可以追踪 actual database mapping、internal representation of its proof relation、adequacy of `Prv`，再检查是否可能有 target-specific diagonalization。此刻的状态是：

```text
G2_SETMM_OBJECT_CODING_SOURCE_REQUALIFICATION_ACTIVE_WITH_SCOPE
ACTUAL_SETMM_TO_MFS_MAPPING_OPEN
INTERNAL_PROVABILITY_ADEQUACY_OPEN
ACTUAL_DIAGONAL_OPEN
PARENT_COMPLETION_BRIDGE_OPEN
```

这不重开 F-050，也不授权把 generic `mFS` objects、conditional `bj-babygodel`，或 external verifier acceptance 写成 bare ZFC 的不完备性／矛盾或项目实际 Q。

## 6. 下一项最小判别行动

只继续一件事：对 exact source / companion sources 检查是否存在一个可冻结的 `set.mm → mFS` construction，以及该 construction能否把 actual proof database接入 internal `mPPSt/mThm` representation。若没有，结论是 `SOURCE_MAPPING_OPEN_WITH_SCOPE`；若有，才逐项进入 `ObjectCodeBridge`、`InternalProvabilityAdequacy` 与 `Diag` 的 payment audit。
