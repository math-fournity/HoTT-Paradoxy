# N40：unlabeled 二元素无规范选点的独立原生机器证明（MP-NOCANONICAL-001 / C-142–C-148）

日期：2026-09-13。Session：`S-RES-20260913-086-N40-NOCANONICAL-NATIVE`。本轮属于 N40 三选一中的第一项（“展平消去器完成 `NoCanonicalFinite` 常量定理”），但结论对该项的假设做了一次纠偏：被阻塞的不是消去器 β 归约，而是 N38 记录的“常量陈述”按字面为假。

## 1. 结论摘要

- 新增机器证明包 `MP-NOCANONICAL-001`（`C-142`–`C-148`），实际 kernel 目标源码是 `HoTT/formal/truncation-no-recovery/NoCanonicalPoint.agda`。`NoCanonicalFinite.agda` 是未被 final command 导入的 bridge/再导出文件；它被 source manifest 固定但该 run **没有**证明 bridge 自身已被检查。
- final run：`HoTT/verification/runs/20260913-MP-NOCANONICAL-001-02/`；Agda 2.8.0-3d04bac + Cubical v0.9；`--safe --cubical --guardedness`；exit 0、stderr 0 bytes、零 warning；生成时曾是 `EXACT_INDEX_SNAPSHOT_MATCH`，矩阵在 S088 演进后当前复验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION`；重放仍为 `EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 机器化的内容：unlabeled 二元素呈现 `Σ[ A ∈ Type ] ∥ A ≃ Bool ∥₁` 上**不存在统一选点**；其机制是 swap 自同构 `notEquiv` 给出的**非平凡自识别**，任何假想统一选点被迫成为 `not` 的不动点。它是对 agda-unimath `no-section-type-2-Element-Type` 所表达现象的独立 Cubical/Type₀ 类比；项目没有证明两个形式规格的保真翻译或等价，所以本包不是外部源码的“重放”。真正的外部源码重放由 S088 的 `MP-UNIMATH-NOSECTION-REPLAY-001` 承担。
- 判词：仍是资格/表示边界（`DEFENSE_WORKS` 族），**不是** HoTT 悖论；E6（真实自然使用链）未出现、未升级。

## 2. N38 → N40 纠偏（重要）

N38 把下列陈述记为“正确的常量形式”：

```text
(s : (b : Bool) → carrier (boolPresentation b)) → s false ≡ s true
```

本轮纸笔检查给出 `s = id` 这一显式反例候选：`boolPresentation` 在定义上常值，因而该目标归约为任意 `Bool → Bool` 的两端相等。这个**精确否定命题没有单独的 claim/run/index**，所以按 F-011 只能保留为 `PAPER_ONLY_WITH_EXPLICIT_COUNTEREXAMPLE_CANDIDATE`，不能作为本包已机器证明的 C-142–C-148 之一。N38 的旧阻塞诊断不再作为当前执行目标；若未来需要重新交付该否定命题，必须另建机器证明包。

正确内容是相干义务：对 `u : (X : UnlabeledTwoElement) → unlabeledCarrier X`，族自身的自识别 `swapSelfIdentification` 迫使 `subst unlabeledCarrier swapSelfIdentification (u X) ≡ u X`；与 `uaβ notEquiv` 复合后得到 `not (u X) ≡ u X`，与 `not≢const` 冲突。

## 3. 证明架构（claim 对应）

| claim | 定义 | 内容 |
|---|---|---|
| C-142 | `swapSelfIdentification` | `identityPresentation ≡ identityPresentation`；carrier 分支是 `ua notEquiv`，标签分支由截断命题性填满（`isProp→PathP` + `isPropPropTrunc`） |
| C-143 | `sectionRespectsSelfIdentification` | section 必须尊重族自识别（`subst` 形式），由 `J` 证明 |
| C-144 | `uniformChoiceFixedPoint` | `not (u X) ≡ u X`；由 C-143 与 `uaβ notEquiv` 复合 |
| C-145 | `noUniformChoice` | `((X : UnlabeledTwoElement) → unlabeledCarrier X) → ⊥` |
| C-146 | `labeledChoice` | 正控制：标签保留（`Σ A × (A ≃ Bool)`）时规范选点存在 |
| C-147 | `labelingsIdentified` / `labelingsDistinct` | 界面把 id/swap 标签识别为一，但两者作为标签数据仍不同 |
| C-148 | `uaNotEquivNotRefl` | `ua notEquiv ≡ refl → ⊥`：自识别非平凡 |

机制围栏：负结论同时依赖 univalence（提供非平凡 carrier 路径）与截断的命题性（使该路径成为**自**识别）；去掉截断即失去自识别并恢复正控制（C-146）。

## 4. 工程决策：源码冻结与行稳定性

- 新 claim 不追加到 `TruncationNoRecovery.agda`，而是新建 `NoCanonicalPoint.agda`。原因是运行 `-01`/`-02`/`-03` 的 `source-manifest` 钉住了 `TruncationNoRecovery.agda` 的字节哈希；修改它会立刻使历史 run 的 source pinning 失败，并迫使共享 proof row 再次改行（`-01`/`-02` 已因早期改行处于历史态）。本轮把该文件恢复到冻结字节（SHA-256 `934c154c…`，与 S084 evidence 副本逐字节相同），并验证 `-03` 仍为 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + `PASS_WITH_SCOPE`。
- 新 proof id 独立成行（`MP-NOCANONICAL-001`），claim 只 append（C-142+），不重写任何旧行。
- `-01`（C-142–C-147）在加 C-148 后被 `-02` 取代；`-01` 作为同源历史 run 保留，不覆盖。

## 5. 运行收据

| run | 覆盖 claim | 状态 | 索引 | 重放 |
|---|---|---|---|---|
| `20260913-MP-NOCANONICAL-001-01` | C-142–C-147 | `KERNEL_ACCEPTED_WITH_SCOPE` | 冻结后被 `-02` 行改写取代（历史） | — |
| `20260913-MP-NOCANONICAL-001-02` | C-142–C-148 | `KERNEL_ACCEPTED_WITH_SCOPE` | 当前 `ROW_STABLE_AFTER_INDEX_EVOLUTION`（生成时 exact） | `EXACT_EXIT_STDOUT_STDERR_MATCH` |

两 run 均：exit 0、stderr 0 bytes、零 warning；外部依赖 5 项（Agda release asset/binary、Cubical release asset、library file、source tree）哈希核验通过；source manifest 固定 4 个文件（`NoCanonicalPoint.agda`、`TOOLCHAIN.json`、`AGDA_LIBRARIES`、`NoCanonicalFinite.agda`）。其中只有目标及其实际 imports 由该 Agda command 检查；把未导入 bridge 放进 manifest 只证明其字节被绑定，不等于 kernel 消费了它。

## 6. 不能推出

- 不证明 HoTT 内部矛盾；不证明“现实不可完成”或任何物理时间结论。
- 不证明任何具体派生开发误用该接口；S086 当时 `hott-z/NoCanonicalPoint.agda` 仍为 `SOURCE_REPORTED_NOT_REPLAYED`，该历史状态后来由 S088 的固定外部库重放收口。
- 不把本包升级为 `NATURAL_USAGE_MISMATCH`：E6 需要真实、固定版本、可回查的自然消费者与同一任务下的资格越级；本包只机器化“接口自身拒绝统一选点”。
- 不主张原创性：该现象是 univalence 下标准的 no-section 论证。

## 7. 对 E6 搜索的影响

本包把 E6 反向搜索（“有没有自然消费者把 unlabeled 接口当 labeled 用”）的**接口侧**钉死为机器事实：接口本身不可能提供统一选点，因此任何作出该承诺的自然消费者必然要自带额外数据或假设（那就不再是资格越级）。这与 N36/N37 的有界负结论同向，并把 S083 的 `SOURCE_REPORTED_NOT_REPLAYED` 推进为“同命题在本 repo 工具链内的原生结果”；E6 仍 OPEN。
