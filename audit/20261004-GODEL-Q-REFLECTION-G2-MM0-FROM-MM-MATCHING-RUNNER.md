# G2：MM0 matching runner、`set.mm` 注释兼容派生与 wholesale translation

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **阶段身份：** `G0/G2_TARGET_MAPPING_CONTROL`。本报告资格化一个版本固定的 M 层 companion translator；它不将该 translator 写成 ZFC 内部的 `mFS`／`Prov_T` 构造。
>
> **主判词：**
>
> ```text
> MM0_MATCHING_RUNNER_BUILT_AND_QUALIFIED
> RAW_SETMM_DIRECT_PARSE_REJECTED_WITH_SCOPE
> COMMENT_NORMALIZED_SETMM_TRANSLATED_AND_MMB_VERIFIED_WITH_SCOPE
> M_LEVEL_WHOLESALE_TRANSLATION_ONLY
> ACTUAL_SETMM_TO_MFS_MAPPING_NOT_SUPPLIED_WITH_SCOPE
> INTERNAL_PROVABILITY_ADEQUACY_NOT_SUPPLIED_WITH_SCOPE
> ACTUAL_DIAGONAL_NOT_SUPPLIED_WITH_SCOPE
> PARENT_COMPLETION_ACCEPTANCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE
> ```

## 1. 本轮精确问题

此前 [set.mm internalization requalification](20261004-GODEL-Q-REFLECTION-G2-SETMM-INTERNALIZATION-REQUALIFICATION.md) 已定位 `digama0/mm0` 的 `from-mm` 为唯一实际 database wholesale translator 候选，但固定 `lts-13.27`／GHC 8.6.5 在当时的 macOS ARM 现场没有 matching runner。

本轮只检验下列 M 层问题：

```text
fixed mm0-hs source + its locked compiler family
  + fixed set.mm database
  → can an actual translator consume the database and emit MM0/MMB?
  → can the separate reference `mm0-c` verifier from that fixed MM0 source consume the emitted artifact?
```

这不是下列问题：

- raw `set.mm` 是否已被 ZF 内部构造成 `T ∈ mFS`；
- `mPPSt/mThm` 是否已被证明与 external `set.mm` proof relation adequate；
- `Prv` 是否被定义并证明 adequate；
- 是否存在 target-specific Gödel sentence、fixed point 或 internal provability theorem；
- `Accept_set.mm` 是否与芝诺／圆环／fixed H0 的 `OriginDone` 有桥；
- bare ZFC 是否不一致、不完备或在时间维度观察不足。

## 2. 冻结输入与工具链

| 对象 | 冻结身份 | 作用 |
|---|---|---|
| Metamath database | `set.mm@160ebb63ec17ff00a809520a420c92914a424622`；SHA-256 `d8420798…`；51,466,065 bytes | actual proof database input |
| MM0 source | `digama0/mm0@0d414c0bfdaaeb7fea571895127abc1fa5a3d956` | `mm0-hs from-mm` 与 reference `mm0-c` 来源 |
| locked resolver | `mm0-hs/stack.yaml` = `lts-13.27` | source-declared GHC package set |
| matching compiler | GHC 8.6.5 x86_64 bindist under Rosetta | exact resolver compiler version |
| Stack | x86_64 Stack 3.11.1 | uses the frozen resolver and `--system-ghc --compiler ghc-8.6.5` |
| C compiler bridge | ARM Homebrew LLVM 22.1.6 cross-targeting `x86_64-apple-macos11` | only repairs host architecture mechanics; it does not change MM0 source or resolver |

完整 source / tool / artifact hash 图在 [run receipt](../HoTT/verification/runs/20261004-SOURCE-REPLAY-MM0-FROM-MM-JCOMPAT-001/RUN.json) 与 [source manifest](../HoTT/verification/runs/20261004-SOURCE-REPLAY-MM0-FROM-MM-JCOMPAT-001/source-manifest.json) 中保存。

## 3. matching runner 的实际资格化

初始 ARM Stack preflight 只得到 `S-9443`：没有 `macosx-aarch64` 的 GHC 8.6.5 setup。为避免把本机 GHC 9.4.8 伪称为同一工具链，本轮下载并校验官方 x86_64 GHC 8.6.5 bindist（SHA-256 `dfc1bdb1…`）和 x86_64 Stack 3.11.1（SHA-256 `0776b73c…`）。

两个本机机制缺口需要单独支付：

1. inherited `host_alias=arm64-apple-darwin20.0.0` 会让老 GHC configure 把 x86 bindist 当作 ARM host；在 `env -i` 的 clean environment 中，以 `--build/--host/--target=x86_64-apple-darwin` 重配后，configure exit `0`；
2. Rosetta 下的 Apple `xcrun` 无法加载 host 仅有的 ARM CommandLineTools library。GHC 生成 x86 汇编后会在链接阶段失败。一个明确的 wrapper 改由 native ARM LLVM 以 x86 target 执行 `clang/ar/ranlib/strip/ld/libtool`，并保留 GHC 8.6.5 生成的 x86 binary。

资格化正控制是一个简单 Haskell program：GHC 8.6.5 编译 `Simple.hs`，输出为 `Mach-O 64-bit executable x86_64`，在 Rosetta 下运行并输出预期文字。随后 Stack 对 `mm0-hs` 的完整依赖图执行 `Completed 59 action(s)`，并生成 x86_64 `mm0-hs` executable。完整 build log 已在 run receipt 原样保留。

这证明的是固定 source 的 matching **M-level runner** 已经可运行；它不证明该 runner 的输出与任何 ZFC 内部对象同一。

## 4. raw input 的直接反控制

直接命令：

```text
arch -x86_64 mm0-hs show-bundled <raw set.mm@160ebb>
```

以 exit `1` 停止，并给出：

```text
parse failed ""wff""as
```

错误定位到 raw source 第 387 行的 `$j` comment metadata：

```text
varcolorcode "wff" as "0000FF";
```

固定 `MM0.FromMM.Parser` 只认识 single-quoted `$j` strings。这个结果是 **raw current database 与 pinned translator 的直接 parser incompatibility**。它既不指控 `set.mm` 的形式内容，也不允许把随后派生输入的成功说成“raw-byte direct replay”。

## 5. 受控 `$j`-comment compatibility derivative

为区分“现代 annotation 语法不兼容”与“Metamath formal database 不兼容”，创建了外置派生文件 `set.mm-mm0-jstring-compat-160ebb.mm`。唯一变动是六条 `$j` comments 中的颜色 metadata：

```text
varcolorcode / altvarcolorcode
  "wff" / "setvar" / "class"
→ 'wff' / 'setvar' / 'class'
```

生成器要求每个精确旧文本仅出现一次；它记录 input/output bytes 都为 `51,466,065`、raw SHA-256 `d8420798…`、derived SHA-256 `c7560de2…`，以及逐条替换清单。派生 manifest 是 run receipt 的受版本化副本。

这不是 raw database 的 byte-identical replay。它的形式内容保持性通过一个独立控制检查：固定 `metamath-exe@9898f5d…` 对派生文件读取 `252401` 个 statement（`3072` 个 `$a`，`47917` 个 `$p`），并以 exit `0` 重新验证所有 proofs，用时 `8.60 s`。

该控制支持下列有限表述：**官方 Metamath verifier 将该六条 `$j` 颜色注释规范化后的文件当作无错误且 proof-equivalent 的 database。** 它不证明任何关于 MM0 或 ZFC 的内部语义等价。

## 6. `from-mm` 的实际运行与 reference MMB 检查

在 compatibility derivative 上，`show-bundled` 以 exit `0` 成功读取全库，并输出：

```text
230 bundled theorems, 300 total copies
```

小切片控制：

```text
mm0-hs from-mm <derived database> -f id -o id.mm0 id.mmb
mm0-c id.mmb < id.mm0
```

生成 `4,837`-byte MM0 和 `960`-byte MMB；`mm0-c` exit `0`，stdout/stderr 均为空。

完整运行：

```text
mm0-hs from-mm <derived database> -o set.mm0 set.mmb
mm0-c set.mmb < set.mm0
```

结果如下：

| 产物 | 外置大小 | SHA-256 | verifier 结果 |
|---|---:|---|---|
| `set.mm0` | 20,573,423 bytes | `ece0cf86…` | supplied as MM0 specification |
| `set.mmb` | 42,894,087 bytes | `28badc4f…` | `mm0-c` exit `0` |
| `mm0-c` | arm64 reference verifier built from fixed `main.c` | `fadc026d…` | stdout/stderr empty |

生成的 20 MiB / 41 MiB artifacts 保留在外置缓存，Git 只保存 re-computable identity、命令、环境和小型 raw receipts。这样不会把第三方数据库或大规模 generated proof artifact 混入项目 Git。

## 7. 对 G0/G2 的影响

旧的 runner blocker 已经解除：`MM0_FROM_MM_EXACT_REPLAY_BLOCKED_BY_GHC_8_6_5_MACOS_AARCH64` 不再是当前状态。

取代它的分层结论是：

```text
raw source direct parser replay: rejected at six modern $j metadata strings
comment-normalized formal database: translated and MMB-verified
translation layer: M-level wholesale database translation
```

它加强了 `set.mm` 子路线的实际可执行性，并提供可审计的 cross-formalism translation evidence。它**没有**填补 Appendix C 指出的内部化义务：

```text
raw/derived database
→ explicit infinite-variable extension
→ internal T ∈ mFS construction
→ actual mPPSt/mThm relation
→ adequate internal Prv
→ target-specific diagonal
```

因此 `ObjectCodeBridge`、`InternalProvabilityAdequacy`、`Diag`、`OriginDone`、`ρ`、Bridge 与 parent completion consumer 都保持未支付。G1、G3–G6 仍不释放，F-050 也保持 `CLOSED_WITH_SCOPE`。

## 8. 下一动作与停止条件

本 branch 的 matching-runner ingress 已被消耗。下一项有判别力的动作只能是以下之一：

1. 找到或构造一个版本固定且可审计的 **internal** `set.mm → mFS`／`Prv` adequacy construction；
2. 找到一个同一 source owner 同时给出 ZFC-facing acceptance、指定 `OriginDone` 和 bridge/task switch/rejection；
3. 研究发起人明确授权从 Appendix C 的规格自行开始 internal mapping construction。

继续反复运行同一 external translator、把 comment-normalized MMB 当作 raw internal mapping，或把 M-level verification 直接接到芝诺／圆环／H0，都不会推进 G2 的未支付义务。
