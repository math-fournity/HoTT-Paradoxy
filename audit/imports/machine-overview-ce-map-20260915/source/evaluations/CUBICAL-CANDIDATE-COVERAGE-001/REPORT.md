# 有界完成性候选的机器证明相对完备性

> Evaluation：`CUBICAL-CANDIDATE-COVERAGE-001`  
> Proof：`PF-CUBICAL-CANDIDATE-COVERAGE-001`  
> Run：`20260914-CUBICAL-CANDIDATE-COVERAGE-001`  
> Verdict：`BOUNDED_GRAMMAR_RELATIVE_COMPLETENESS_WITH_TASK_PRESERVING_REDUCTION`  
> Global HoTT coverage：`NOT_ESTABLISHED`  
> Reality correspondence：`FORMAL_TASK_FIELDS_PRESERVED / PHYSICAL_BRIDGE_NOT_ESTABLISHED`

## 1. 这项证明解决了什么

先前协调器可以报告某个声明文法已被完整枚举，但“完整”仍主要由 Python 生成器、计数与顺序扰动实验支撑。本包把一个精确的小型分母移入 Cubical Agda 内核：

```agda
data Raw : ℕ → Type where
  never : Raw n
  now    : Bool → Raw n
  laterR : Raw n → Raw (suc n)
```

对每个 bound `n`，`allRaw n` 是有限列表。内核接受：

```agda
allRaw-complete : (r : Raw n) → r ∈ allRaw n
```

因此该枚举的分母由 `Raw n` 的类型直接给出，覆盖结论不依赖“本次恰好生成了多少个对象”的经验判断。

## 2. 规范化为什么没有换题

`normalize` 只把显式 `laterR` syntax 化为既有 R041 canonical representation：

```text
never                    ↦ ω
now b                    ↦ ret 0 b
laterR r                 ↦ later (normalize r)
```

本包没有用“结果相同”一句话替代任务对应，而是分别证明：

1. `RawConv r b ⇔ Conv (normalize r) b`；
2. 对任意 horizon `k`，`rawDeadline k r ≡ deadline k (normalize r)`；
3. `reduceCandidate` 保持 horizon；
4. `reduceCandidate` 保持 expected observation；
5. raw 与 canonical candidate 的 actual deadline observation 相等；
6. 每个 reduced candidate 都属于同一 fixed-task 的 `canonicalSpace`。

这些等价/相等使用当前 Cubical Agda 的 native Path。因而，就这个 TaskSpec 而言，缩减没有删除 consumer、改变观察窗或替换完成判据。

## 3. 五个机器主张

| Claim | 内核接受的内容 | 边界 |
|---|---|---|
| `MP-CCC-RAW-ENUMERATION-001` | 每个 `Raw n` inhabitant 出现在 `allRaw n` | exact bounded grammar only |
| `MP-CCC-NORMALIZATION-SEMANTICS-001` | convergence 与任意 deadline observation 被规范化保持 | no arbitrary consumer theorem |
| `MP-CCC-TASK-PRESERVATION-001` | horizon、expected、actual observation 被 reduction 保持 | formal TaskSpec fields only |
| `MP-CCC-REDUCED-COVERAGE-001` | 每个 reduced candidate 出现在 canonical generated space | no full HoTT candidate reduction |
| `MP-CCC-CONTROLS-001` | immediate/later membership、too-early/on-time、divergence 与 later-never collapse | fixed controls only |

Run 的 source manifest 固定 5 个 repo files 和 5 个外部 toolchain artifacts。Agda 2.8.0-3d04bac + Cubical v0.9 首轮 exit 0、stderr 0；matrix 6 rows 已冻结；独立 rerun 为 `EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`。

## 4. 保留的 Cubical 诊断

Agda 对 `allRaw-complete` 报告 `UnsupportedIndexedMatch`：该函数对通过 Path transport 隐藏的 indexed `Raw` value 不保证 judgemental reduction，因为当前 Cubical Agda 尚不支持所需的 `suc` constructor injectivity computation。

该诊断不否定 theorem 的内核接受；它限制的是特定 transported input 上的计算行为。当前包的枚举、controls、normalization 和 TaskSpec consumer 都由普通 constructors 生成，没有在 transport 下执行 `allRaw-complete`。因此 run、claim、non-goals 和专项测试全部保留这条边界，而没有静默关闭 warning。

## 5. 它使完备性前进了多少

这项结果建立了第一个机器证明的 `COMP-2` slice：

```text
exact bounded candidate type
  → exhaustive finite enumerator
  → canonical reduction
  → semantic/task preservation
  → reduced-space coverage
```

它仍未建立 `COMP-4`。当前没有函数把“所有与 HoTT 非现实性有关的候选”映射到 `Raw n`，更没有证明这种映射保持 arbitrary Path/HIT consumer、proof search、自指结构和现实对应。`Raw n` 也没有使用 univalence、HIT eliminator 或 higher coherence；所以本包是用 Cubical Path 核验的 partiality/deadline coverage theorem，不是 HoTT 专属性定理。

其研究意义在于：今后每次声称“某候选族被统观完整”，应当复制这一证书形状，并扩大 `CandidateClass` 与 preservation theorem，而不能只扩大循环次数。

## 6. 复核

```bash
python3 scripts/audit/verify_formal_proof_run.py \
  --run-dir HoTT/verification/runs/20260914-CUBICAL-CANDIDATE-COVERAGE-001 \
  --rerun

python3 -m unittest \
  machine-overview/tests/test_cubical_candidate_coverage.py
```

当前结果：formal verifier `PASS_WITH_SCOPE`；index `EXACT_INDEX_SNAPSHOT_MATCH`；native replay `EXACT_EXIT_STDOUT_STDERR_MATCH`；专项回归 4/4。

