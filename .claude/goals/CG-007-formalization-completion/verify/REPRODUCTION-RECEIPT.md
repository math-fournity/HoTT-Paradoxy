# 独立复现收据：Master 的 AllBlockerQ 装配（2026-10-14，本线 CG-007 会话 d58e0c0d）

> **身份**：`INDEPENDENT_REPRODUCTION / NOT_A_NEW_RECEIPT`。这是**第三方独立复现**已有结论，
> 不产生新的机器证明主张。原装配及其收据归 Master（`ASSEMBLY-RECEIPT.md`，提交 `d7b55676`）。
> 本文件的独特角度是**两处移植冲突的语义保真核验**（Master 与 004-Flash 均未覆盖此角度）。

## 1. 编译复现

```
ASM     = elegant-mclaren/.cg009-verification/master-assembly-poc-20261014
ASM_OUT = .claude/goals/CG-007-formalization-completion/verify/repro-build   （全新空目录）
ASM_SEED= elegant-mclaren/.cg009-verification/master-verify-9276-20261014    （9276 自己的 52 个 olean）
driver  = driver.py 原样复制为 driver_repro.py，未改一行逻辑
```

结果（`verify/repro.log`）：

```
ok   GodelQ.MasterAssemblyProbe
=== done: compiled=74 skipped=0 failed=0 in 210s ===
```

- **`skipped=0`**：全部 74 个模块从源重编译，无一复用 Master 的输出——这是独立性的关键。
- 全部 74 个 `.log` 中 **`error:` 计数 0、`sorryAx` 计数 0**。
- 三条公理报告（`GodelQ_MasterAssemblyProbe.log`）：
  ```
  'GodelQ.MasterAssemblyProbe.bridgeB'         depends on axioms: [propext, Classical.choice, Quot.sound]
  'GodelQ.MasterAssemblyProbe.allKey_uncond'   depends on axioms: [propext, Classical.choice, Quot.sound]
  'GodelQ.MasterAssemblyProbe.allBlockerQ_uncond' depends on axioms: [propext, Classical.choice, Quot.sound]
  ```

**判据**（舰队定型纪律，`形式化追踪/99-更新日志.md`）：进程 exit code + `#print axioms` 不含 `sorryAx`。
本复现两项全过，与 Master 收据（`d7b55676`）及 004-Flash 复现（`1a2e1214`，41/41）**结论一致**。

## 2. 移植冲突的语义保真核验（本复现的独特贡献）

Master 记录的移植冲突有两处。**这两处此前没有人核过"是否只影响消解、不改语义"**。

### 冲突 1：`TranslateShiftCompat` 取 9276 版（63 声明）而非 NL 版（61 声明）

**核验结果：9276 版是 NL 版的严格语义超集。**

| 项 | 9276 版 | NL 版（PoC 实际采用的那份） |
|---|---|---|
| 顶层声明数 | 63 | 61 |
| 文件名 | `codex/9276-cg007-w8-d3/.../TranslateShiftCompat.lean` | `elegant-mclaren/.../master-assembly-poc-20261014/GodelQ/ZFC/TranslateShiftCompat.lean` |
| 行数 | 1365 | 1335 |

- **名称集合**：PoC 那份的 61 个名字**全部**出现在 9276 版的 63 个里；反向为空集。
- **9276 多出的两个**：`iT_qqVerums`、`isUFormula_qqVerums`（004-Step 报过 `iT_qqVerums` 已证）。
- **签名比对**：61 个共有声明逐一比对"声明头到第一个 `:=` 之前"的规范化文本
  （空白折叠），**61/61 逐字节相同**。

⟹ 采用 9276 版**不会**改变任何被消费定理的签名或陈述。多出的两条是纯增益。
**这条超集关系是真保真的，不是"取大的那份碰巧也能过"。**

### 冲突 2：`len_qVec` 撞名，5 处加 `Bootstrapping.` 前缀

**核验结果：纯命名空间限定，无语义改动。**

以 `ITSubstOpen4.lean` 为样本（Master 记录 5 处前缀都在此文件）：

| 项 | NL 源（`nice-lovelace` round31） | PoC 版 |
|---|---|---|
| 行数 | 262 | 262 |
| `len_qVec` 出现次数 | 9 | 9（其中 5 处带 `Bootstrapping.` 前缀） |
| 去掉前缀后与源逐字节比较 | — | **完全相同（`True`）** |

即 PoC 版 = NL 源 做**唯一一处**字符串替换 `len_qVec → Bootstrapping.len_qVec`。
`Bootstrapping.len_qVec` 与无前缀的 `len_qVec` 指向 Foundation 的同一条定理
（无前缀时被本包的 `len_qVec_qVec_eq` 遮蔽，加前缀是**恢复原本意图的消解目标**）。

⟹ **这 5 处改动只影响名字消解，不触碰任何定理的内容或证明体。** 若漏加前缀，
`rw [len_qVec hX]` 会错误地改写成同名的本包辅助引理——所以这处前缀是**修复**而非规避。

## 3. 结论

1. Master 的 `allBlockerQ_uncond` 装配在**独立工作区、全新输出目录、`skipped=0`** 下复现成功：
   74/74 编译通过，公理三条，无 sorryAx。这是该结论的**第三个**独立确认
   （Master 原收据 + 004-Flash 41/41 + 本线 74/74）。
2. 两处移植冲突**都只是机械差异，无语义改动**：
   `TranslateShiftCompat` 是严格语义超集（61/61 签名逐字节相同）；
   `len_qVec` 是唯一字符串替换（去掉前缀后与源逐字节相同）。
3. 因此 **`AllBlockerQ` 无条件证成这一结论不依赖于移植选择**——
   换成另一版 `TranslateShiftCompat`、或去掉前缀，都不会改变可证性。

## 4. 复现方法（供后续会话）

```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911
ASM=/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/.cg009-verification/master-assembly-poc-20261014 \
ASM_OUT=/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/goals/CG-007-formalization-completion/verify/repro-build \
ASM_SEED=/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0/.cg009-verification/master-verify-9276-20261014 \
python3 -B .claude/goals/CG-007-formalization-completion/verify/driver_repro.py
```

`ASM_OUT` 必须是一个**空目录**（driver 见到已存在的 `.olean` 就跳过，`skipped=0` 才算独立复现）。
约 210 秒。

## 5. 边界

- 本文件**不**主张新定理；主张的是"已有结论在第三方工具链与工作区下复现，且移植选择无实质影响"。
- 未核验的部分：`iT_subst_open` 的一般律证明内容本身（那是 001-Flash 的资产，Master 已核）；
  `allKey_of_bridge`/`allBlockerQ_of_key` 的证明内容本身（004-Flash 的资产，Master 已核五条）。
  本复现核的是**装配**与**移植保真**。
- 种子 olean 用 9276 自己的（52 个），与 Master、004-Flash 一致。
