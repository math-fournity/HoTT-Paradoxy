# SEM-B05：reflection `declarePostulate` 与 safe-mode 边界探针

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTROLLED_AXIOM_INTRODUCTION_PROBE`
>
> 分支：`codex/semantic-overview`
>
> run：`20260913-SEM-B05-REFLECTION-POSTULATE-SAFE-001-01`

本目录保存四个最小 Agda 2.8 探针，用于区分三个事实：reflection API 具有显式声明
postulate 的能力；默认模式允许源程序借此扩展当前理论；safe 模式拒绝这项操作，但仍允许
只生成普通证明项的 reflection。这里的 `true ≡ false` 是受控错误目标，用来显示新公理
究竟在哪里进入，不是对无附加公理 Agda 的定理。

## 固定输入

- Agda：`2.8.0-3d04bac`；
- Agda binary SHA-256：
  `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e`；
- primitive root：
  `/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-data/agda/2.8.0-3d04bac/lib/prim`；
- `Agda/Builtin/Reflection.agda` SHA-256：
  `ef851b831795fea34125c6cd17fb81675ed9eb62c871addb5951082cb1732b13`；
- B04 对照 solver SHA-256：
  `4e34f147a01b4ffce9deb863c25521fd997dddc1a072e94e1b03f5cf444a7882`；
- agda-unimath TCM wrapper SHA-256：
  `519f08b73ba6dd29cac3a41566a1b356147b9e27d96ba9970f1dd550c0b8a52e`。

`source-manifest.json` 固定 runner、四个探针、13 个 Agda primitive 源文件、两个 B04
对照源码、toolchain manifest 和 Agda 二进制，共 22 项。

## 四个探针

| 文件 | 控制变量 | 预期与结果 |
|---|---|---|
| `SemB05Unsafe.agda` | 明确调用 `declarePostulate`，默认模式 | exit `0`；文件通过，因为宏显式增加了目标类型的公理 |
| `SemB05Safe.agda` | 相同宏体，源文件声明 `--safe` | exit `42`；`[SafeFlagPostulate]` |
| `SemB05SafeReflectionPositive.agda` | `--safe`，宏只把 `refl` 交给 `unify` | exit `0`；safe mode 没有一概拒绝 reflection |
| `SemB05NoAxiomNegative.agda` | 不调用 reflection/postulate，直接以 `refl` 证明 `true ≡ false` | exit `42`；`[UnequalTerms]` |

runner 还把 `SemB05Unsafe.agda` **同一份字节**加上命令行 `--safe` 重跑，得到同样的
`[SafeFlagPostulate]`。这样可以排除两个源文件之间其它差异导致结果的解释。除 module 名、
`OPTIONS --safe` 和解释注释外，unsafe/source-safe 两份源码的规范化主体相同，SHA-256 都是
`1bb92b865b1bff62ad359d7d40e647a83bf2068aa7d86629af2286c13dc8b1b1`。

## 宏实际做的事

受控宏依次：

1. 用 `inferType` 读取洞的目标类型；
2. 用 `freshName` 分配新名字；
3. 用 `declarePostulate` 在该目标类型上声明新公理；
4. 构造指向新公理的 `def` term；
5. 用 `unify` 将它填入洞。

默认模式的 exit `0` 因而表示“扩展后的理论包含一个 `true ≡ false` 公理，并接受对它的
引用”。它不表示未扩展理论计算或推导出了该等式。safe 模式的错误明确指出无法在 safe flag
下声明该公理。

## 重放

从本 worktree 根运行：

```bash
python3 -B semantic-overview/tools/run_sem_b05.py
```

现有 run 目录受到拒绝覆盖保护，因此重复调用应 exit `2`。新的证据运行必须分配新的 run
ID，不得覆盖当前原始 stdout/stderr。

## 与 B04 的边界

B04 固定的 `solve-Precategory!` solver 直接调用 `declare-postulate` 的次数为零；它构造
soundness lemma 加 `refl` 的证明项。B05 证明的是 **API 能力及模式边界**，不能因为两个
对象都使用 reflection 就把 B05 的显式公理引入归因给 B04 solver。
