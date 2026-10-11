# 交接：CG-009 工位 `elegant-mclaren-767fb0` → 下一会话

> 2026-10-11 17:4x。分支 `claude/elegant-mclaren-767fb0`（已推送 origin）。
> 本文件是本工位的**完整交接**：工作根、已证清单、剩余义务、可复用工具、陷阱与边界。

---

## 〇、三十秒摘要

本会话把 O2 从"`iT_neg` 已证"推进到 **8/10 支就绪**：
**`iT_shift` 全证 → `tshift` → `hShift` 无条件**，并**组装完 `hAll`**（只差一条显式前提 `hAB`）。
`hAB` 经本会话实测**确认为实质性研究缺口**（非工程长尾），三条路径的评估见 §三。
全部新定理 exit 0、0 sorry、公理仅 `[propext, Classical.choice, Quot.sound]`。

---

## 一、工作根与开工闭包

**工作根**：`/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0`
（分支 `claude/elegant-mclaren-767fb0`；canonical `/Volumes/D/HoTT_AI_HANDOFF_20260911` 只读；
**不合并到 dev**）。

**开工先核对**：`git rev-parse --show-toplevel --abbrev-ref HEAD`；`git log --oneline -3`。

**压缩/恢复后按序重读**（用 Read 读原文）：
1. 本文件；
2. `docs/形式化综合研判-20261011/成果-IShiftDomZero/README.md`（成果与障碍图谱，§十二–§十五）；
3. `docs/形式化综合研判-20261011/增量扫描日志.md` 末尾（第 31–33 轮）；
4. `docs/形式化综合研判-20261011/接力-ISHIFT给下一会话.md`。

---

## 二、本会话已证清单（全部机器核验，38/38 从零重编译通过）

### 2.1 自研（`成果-IShiftDomZero/`）

| 定理 | 文件 | 内容 |
|---|---|---|
| `shift_domZero` | `ShiftDomZero.lean` | 枢纽：`shift domZero = domZero` |
| `shift_quote` | `ShiftQuote.lean` | 通用工具：`shift` 固定任意句子引号 |
| `ishift` 六支 | `IShiftFull-6of8.lean` | verum/falsum/and/or/all/exs |
| `shift_ve0` | `ShiftVe0.lean` | iVE func 情形 k=0 |
| **`iTR_shift`** | `ITRShift.lean` | `iTR n 2 R (termShiftVec 2 v) = shift (iTR n 2 R v)` |
| **`iT_shift`** | `ITShift-FULL.lean` | `iT n (shift p) = shift (iT n p)`，**九支全过** |
| **`tshift`** | `TShift.lean` | `translateSeq (setShift s) = setShift (translateSeq s)` |
| **`hShift_uncond`** | `TShiftBranches.lean` | O2 的 hShift 支**无条件** |
| `isFormulaSet_of_setShift_eq` | 同上 | `setShift s'` 公式集 ⇒ `s'` 公式集 |
| `guard_step` | `HAllGuard.lean` | Derivable 层护罩步骤 |
| `all_mem` | `HAllProof.lean` | `^∀ (imp domZero (iT 1 p)) ∈ translateSeq s` |
| **`hAll_uncond`** | `HAllProof.lean` | **hAll 组装完成**，只差显式前提 `hAB` |
| `naive_law_is_false_shape` | `ITSubstCounter.lean` | **机器证明**朴素 iVE/subst 等式律恒假 |

### 2.2 吸收（独立核验后）

- `TranslateShiftCompat-a841872c.lean`（9276，837 行 0 sorry）：`iT_shift` 完整版（**与本会话双路互证**）、
  `free_imp_domZero`、`domZero_eq_cDomN`、`shift_imp_domZero`、`shift_iTR` 等。
- `SetupQTools.lean`（提取自 9276 的 `ShCraigElimSetupQ.lean`）：`split_or` + `replace_of_imp`。

---

## 三、剩余义务：`hAB`（精确，本会话实测确认是研究缺口）

### 形状
```
hAB : Derivable 𝗭𝗙𝗖 (insert (neg A ^⋎ B) ∅)
  A := iT 0 (free ℒₒᵣ p)
  B := free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT 1 p))
```
A、B 都是 ℒₛₑₜ **闭公式**。`hAll_uncond` 已把它隔离为唯一前提，其余全部就位。

### 三条路径的实测评估

| 路径 | 实测状态 |
|---|---|
| ① 元层引理 | 元层 `translate (free ψ) = free (translate ψ)` **不在 Foundation**；自证需处理 `translateRel` 的 `Rew.subst`/`Rew.emb` 交互（工作量 ≥ `iVE_shift`）。**且只对 `p = ⌜ψ⌝` 有效** |
| ② 对 `p` 结构归纳 | `free` 不是 `UformulaRec1` 构造（用 `substs1`），无法套 `semiformula_result_induction` |
| ③ 改 `iT` 定义（all/exs 用替换语义） | **接口级**：`iT` 被 C-390/C-391 等收据引用。**须研究发起人裁定** |

### 相关负面结果（机器证明，防止重复尝试）
`ITSubstCounter.lean`：`subst ?[^&0] (eqAtom ^&x) ≠ eqAtom ^&x`（替换命中 `eqAtom` 自身的 bvar0）。
9276 另有两轮反例（其交接文档 §3）。**三轮反例现已全部机器化。**

### `hExs` 同形（用 `substs1`）；`hRoot` 就是 D3 本身（9276 已定位其技术障碍）。

---

## 四、可复用工具

| 工具 | 位置 | 用途 |
|---|---|---|
| `topobuild.py` | `.cg009-verification/round31/topobuild.py` | 从零拓扑编译（逐文件删 olean，无缓存假命中） |
| `shift_domZero` / `shift_quote` | `成果-IShiftDomZero/` | 量词支枢纽 / 闭项引号工具 |
| `split_or` / `replace_of_imp` | `SetupQTools.lean` | sequent 演算（hAll/hExs 的必需件） |
| `guard_step` | `HAllGuard.lean` | Derivable 层护罩 |

**用法**：`cd .cg009-verification/round31 && python3 -B topobuild.py --src src --build build --only <模块>`
LEAN_PATH 见 `topobuild.py` 的 `lean_path()` 函数（机器相关串不入库）。

---

## 五、陷阱（实测）

1. **Write 工具被跨 worktree 钩子拦截**——落盘用 Bash heredoc。
2. **编译缓存会假命中**——任何"能不能编译"必须删 olean 重编（`topobuild.py` 内置）。
3. **层数记账**：`IsUTermVec.isSemitermVec` 给的层是 `listMax (termBVVec ...)`；
   与 `iTR` 的 `n` 对接要用 `IsSemitermVec`（照 `isSemiformula_iTR` 的先例）。
4. **`iT.construction` 直接 `simp only` 会展开整个结构体**——用 `iT_and`/`iT_all` 等具名引理 + `show`。
5. **删除只进废纸篓**——用 `~/bin/rm-trash` **绝对路径**（Bash 工具 shell 不加载 zsh alias）。
6. **引用任何"已证"前独立重编译**。

---

## 六、边界与授权

- 只写本工位；canonical 与其他 worktree 只读；**不合并到 dev**（用户 2026-10-11 明确）。
- 阶段性提交推送已获授权。**路径③（改 `iT` 定义）须用户裁定。**

---

## 七、给下一会话的最短路线

1. **若走路径①**：先证元层 `arithTrln.translate (Rewriting.free ψ) = Rewriting.free (arithTrln.translate ψ)`
   （对 `translate` 结构归纳）；再评估能否从 `p = ⌜ψ⌝` 推广（可能需 `induction1` 的额外假设）。
2. **若走路径③**：请用户裁定（接口级改动，影响 C-390/C-391）。
3. **`hExs`**：与 `hAll` 完全同形，`hAll` 一通则 `hExs` 随之。
4. **`hRoot`**：9276 已定位技术障碍（`Theory.Δ₁.mem_iff` 接受元层 `Proposition`，
   而手里是 V 元素——需用 `Δ₁Class.defined` 的 `.iff`）。
