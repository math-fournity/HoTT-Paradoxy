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

### 4.4 Appendix C 对 actual-database mapping 的直接边界

[Metamath book Appendix C §C.4](https://us.metamath.org/downloads/metamath.pdf) 直接讨论 database 与 abstract formal system 的关系：一个有限 Metamath database 通常只能描述 formal system及其 universe 的有限子集；若要间接描述整个无限 formal system，需要进一步形式化 Appendix 的说明语言。它也把 `$d/$f/$e/$a/$p` source statements 与 formal-system pre-statements/statements 作说明性对应。

这恰好解释本卡的 source boundary：`set.mm` 已 formalize Appendix C 的 generic ZF objects，却没有在本次 exact database source 中给出一项 source-declared construction，把这个有限 source file本身作为一个完整、明确的 internal `T ∈ mFS` object。该书说“in principle”可以继续形式化，不能被改写成这一步已经在 `set.mm@160ebb…` 被完成。

### 4.5 有限 raw database 与 `mFS` 无穷变量条件

对 exact raw source 的可重放 lexical inventory保存在 [source-inventory](../HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/source-inventory.json)。它在移除 Metamath comments 后记录：

```text
355 distinct $v tokens
1474 distinct $c tokens
```

而 `ismfs` 的 source comment和assertion要求：对每个 variable typecode，type function 的相应 preimage不是有限集。这不是矛盾：Appendix C正是用一个无限 variable universe描述 abstract formal system，有限 database仅选择其中可用的有限 source representation。

它给 actual mapping 加上一项明确 obligation：

```text
finite source tokens
  → explicit infinite-variable extension
  → proof of its relation to the raw database frames
  → internal T ∈ mFS construction
```

因此“把 raw `set.mm` 的 `$v` list直接拿来当 `mVR`”是一个受控反例，不是对 ZFC、set.mm 数学内容或无限变量本身的反例。

### 4.6 MM0 的近邻翻译控制

`digama0/mm0@0d414c0bfdaaeb7fea571895127abc1fa5a3d956` 是一个相关但不同的 companion source。其 README（SHA-256 `a62a362b425e74cdfa0881c74a5ca08adc7951876d770757b6a2f9f6d5994e46`）明确把 `examples/set.mm0` 描述为对 **set.mm axiom system 的 hand translation**，并说明相应 proof file是 WIP；`set.mm0` 内容 SHA-256 为 `1123b3e9ec3315a32a629035df04bc96ca5004a00a0adc4fba226b280c8b5dd4`。

它证明的是一个重要的 DifferentTarget control：一个新语言中的手工 ZFC axiom specification，即使未来可被其 verifier检查，也不自动给出

```text
exact raw set.mm database
→ internal mFS object
→ internal mPPSt/mThm relation
→ adequate Prv / diagonal
```

因此 MM0 是 actual mapping obligation 的近邻对照，不是 payment。

### 4.7 `from-mm` 的真实能力与当前 host toolchain gap

同一固定 MM0 source 的 `mm0-hs/README.md` 和 `MM0.FromMM` source 实际给出命令：

```text
mm0-hs from-mm MM-FILE [-o MM0-FILE MMU/MMB-FILE]
```

它声称 wholesale translation from Metamath to MM0 + proof format，因而是唯一值得继续检验的 actual-database M-layer translation candidate。当前不能把它报告为已运行：该 source 的 `stack.yaml` 锁定 `lts-13.27`（GHC 8.6.5）；`STACK_ROOT` 和 `TMPDIR` 均放外置缓存的 preflight 在本机 macOS ARM 上得到 Stack `S-9443`，提示没有 `ghc-8.6.5` 的 `macosx-aarch64` setup。当前已装 GHC 9.4.8 不等价于这个 lock。

因此本卡的准确状态是：

```text
MM0_FROM_MM_SOURCE_CAPABILITY_IDENTIFIED
MM0_FROM_MM_EXACT_REPLAY_BLOCKED_BY_GHC_8_6_5_MACOS_AARCH64
NO_TRANSLATION_OUTPUT_OR_MAPPING_CLAIM
```

重开条件是一个支持 GHC 8.6.5 的匹配 runner、来源维护者提供的版本固定可执行物，或被单独资格化的等价 toolchain；在任一条件出现前，不用新 GHC / 新 resolver 伪造 exact replay。

### 4.8 本机 matching runner 现场

当前 host 只检测到 Docker client，没有可连接的 OrbStack daemon；`limactl list` 也报告没有 Lima instance。没有启动新的 VM、container或下载新镜像，因为那会改变环境而不是重放现有固定 source。故本轮的 `from-mm` 阻断不是“尚未尝试容器”，而是**当前可观察 runner inventory中没有一个可复用的 matching runner**。

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

exact source 与官方 Appendix C 已完成这一项 source-level检查：没有 source-declared `set.mm → mFS` construction；Appendix明确把完整 internal description留作需要进一步形式化的工作。因此本 source branch当前收束为：

```text
SETMM_OBJECT_CODE_ASSETS_VERIFIED_WITH_SCOPE
ACTUAL_SETMM_TO_MFS_SOURCE_MAPPING_NOT_SUPPLIED_WITH_SCOPE
INTERNAL_PROVABILITY_ADEQUACY_NOT_SUPPLIED_WITH_SCOPE
ACTUAL_DIAGONAL_NOT_SUPPLIED_WITH_SCOPE
```

只有一个新的版本固定 companion construction，或研究发起人授权从 Appendix C 规格自行构造并机器验证 actual mapping，才重新打开这条 G2 branch。
