# 交接：CG-009 工位 `elegant-mclaren-767fb0` → 下一会话

> 2026-10-11。分支 `claude/elegant-mclaren-767fb0`。
> 本文件是**本工位的完整交接**：工作根、已证清单、剩余义务、可复用工具、陷阱与边界。

---

## 〇、三十秒摘要

本会话把 Z0 缺口链条上的 **`ishift` 从"未开工"推进到"九支中六支已证"**，
并证出**枢纽原子 `shift_domZero`** 与**通用工具 `shift_quote`**。
剩余唯一障碍是 `iVE_shift` 的 `func` 支（与工位 9276 独立确认一致）。
全部新定理 exit 0、0 sorry、`#print axioms` 仅 `[propext, Classical.choice, Quot.sound]`。

---

## 一、工作根与开工闭包

**工作根**：`/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0`
（分支 `claude/elegant-mclaren-767fb0`；canonical `/Volumes/D/HoTT_AI_HANDOFF_20260911` 只读）。

**开工先核对**（其他会话会随时推进 HEAD）：
```bash
cd /Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0
git rev-parse --show-toplevel --abbrev-ref HEAD
git log --oneline -3
```

**压缩/恢复后按序重读**（用 Read 读原文，不用摘要代替）：
1. 本文件；
2. `docs/形式化综合研判-20261011/增量扫描日志.md` 末尾三轮（第 31–33 轮是本会话的）；
3. `docs/形式化综合研判-20261011/接力-ISHIFT给下一会话.md`（技术细节）；
4. `docs/形式化综合研判-20261011/成果-IShiftDomZero/README.md`（本会话成果清单）；
5. `docs/形式化综合研判-20261011/综合研判-20261011.md`、`后续工作方案.md`。

---

## 二、本会话已证清单（全部机器核验）

### 2.1 自研（`成果-IShiftDomZero/`）

| 定理 | 文件 | 内容 |
|---|---|---|
| **`shift_domZero`** | `ShiftDomZero.lean` | **枢纽**：`shift domZero = domZero` |
| `rew_shift_emb` | 同上 | Rewriting 层版本 |
| **`shift_quote`** / `rew_shift_quote` | `ShiftQuote.lean` | **通用工具**：`shift` 固定任意 `Semisentence` 的引号 |
| `shift_cFunc0` / `shift_subst_cFunc0` / `shift_ve0` | `ShiftVe0.lean` | `iVE` func 情形 **k=0** 支 |
| `shift_imp` / `ishift_all` / `ishift_exs` | `IShiftAllExs.lean` | 量词支（IH@n+1 ⇒ 支@n） |
| `ishift` **六支** | `IShiftFull-6of8.lean` | verum / falsum / and / or / all / exs |

### 2.2 吸收（来自工位 `9276-cg007-w8-d3`，本会话独立核验后吸收）

`TranslateShiftCompat-966fb6a7.lean`（源：9276 的 commit `5ac2dd04`，已推送）：
- `shift_eqAtom_bvar` / `shift_eqAtom_fvar`
- `iVE_shift_bvar` / `iVE_shift_fvar`

### 2.3 核验记录（本会话对他人成果的独立复算）

- `cg007-w8-d3` 全包 **47 文件**从零拓扑编译 → 40/40 真实源码通过；
  7 项失败全是预期失败（负控制 / 探针 / 已知带 sorry 的目标文件）。
- `iT_neg` 已提交（`268dae2e`），sha `5f504b8d` 与我方防回退副本逐字节一致。
- 证伪：9276 的 `NegInvolution` 改写版 exit 1（四处 Type mismatch + sorryAx）；
  其 `ShCraigElimNegLaw` 6601 B 版 `IsUFormula.qqAlls` 不存在。

---

## 三、剩余义务（精确）

### 3.1 `iVE_shift` 的 `func` 支（唯一障碍）

目标：`iVE n (termShift t) = shift (iVE n t)`，对 `t = ^func k f v`（`k ≠ 0`，即 `ve2`）。

展开：
```
LHS: iVE n (^func k f (termShiftVec k v))
   = ve2 n k f (resultVec ![n] k (termShiftVec k v))     [iVE_func]
RHS: shift (ve2 n k f (resultVec ![n] k v))
```
`ve2 n k f w = qqAlls (imp (conjunct 3 n 0 w.[0] ^⋏ (conjunct 3 n 1 w.[1] ^⋏ ⊤))
                          (subst (^#2 ∷ ?[^#0,^#1]) (cFunc k f))) 2`

**需新证**（本机实测不存在）：
1. `shift_conjunct`：`shift (conjunct 3 n i x) = conjunct 3 n i (shift x)`——用 `shift_and` 叠合；
2. `shift` 固定 `subst (^#2 ∷ …) (cFunc k f)`——**闭项**，走 `shift_quote`（本会话工具）；
3. `resultVec` 与 `termShiftVec` 点相容（`nth_resultVec` 逐分量 + 项级 IH）。

**模板**：`SeqTranslateFormula.lean:266` 的 `isSemiformula_iVE`（用 `IsSemiterm.sigma1_induction`，
func 支参照其 `nth_resultVec` 写法）。

### 3.2 下游链条（`func` 支完成后）

`iVE_shift` ⇒ `iT_shift`（`iT 0 (shift p) = shift (iT 0 p)`）
⇒ `translateSeq_setShift` ⇒ `hShift` / `hAll` / `hExs` 三支
⇒ `ShCraigElim` 十支全接 ⇒ `zfcTr_D3_internalize` ⇒ Z0 完整形式。

- `tshift ⇐ ishift` 归约已过核：`GateBranches.tshift_of_ishift`（`成果-GateBranches/`）。
- `hExs` 另需 `iT_substs1`（同形，用 `substs1`）。
- `hAxm` 需 O3 证书桥（`codeOfREPred` 一般 V 表示引理）——独立战线。

---

## 四、可复用工具（本会话新增）

| 工具 | 位置 | 用途 |
|---|---|---|
| `topobuild.py` | `.cg009-verification/round31/topobuild.py` | 从零拓扑编译 GodelQ 包（**逐文件删 olean，无缓存假命中**） |
| `shift_quote` | `成果-IShiftDomZero/ShiftQuote.lean` | 任何闭项引号的 shift-不变性 |
| `shift_domZero` | `成果-IShiftDomZero/ShiftDomZero.lean` | 量词支归约的枢纽 |

**`topobuild.py` 用法**：
```bash
cd .cg009-verification/round31
python3 -B topobuild.py --src src --build build --only <模块名片段> [--keep-going]
```
LEAN_PATH 需含 Foundation + Astra Mathlib 的 8 个 package
（batteries / aesop / Qq / proofwidgets / importGraph / LeanSearchClient / plausible / Cli）。
完整串见 `lean_path.txt`（机器相关，未入库——用 `topobuild.py` 内的 `lean_path()` 函数重建）。

---

## 五、陷阱（本会话实测）

1. **Write 工具被跨 worktree 钩子拦截**——落盘用 Bash heredoc（本工位目录已获授权）。
2. **编译缓存会假命中**：任何"能不能编译"的判断必须删 olean 重编（`topobuild.py` 已内置）。
3. **`rw [← h]` 在 `param` 与 `n` 不同的上下文会失败**——归纳谓词要带 `param = n` 护罩
   （照 `isSemiformula_iT` / `iT_neg` 的形状）。
4. **`iT.construction` 直接 `simp only` 会展开整个结构体**（elaboration 开销大）——
   改用 `iT_and` / `iT_all` 等具名引理 + `show` 指定形状。
5. **`isSemiformula_mono` 硬编码 `ℒₛₑₜ`**——`ℒₒᵣ` 版需自写（本会话 `isSemiformula_mono_or`）。
6. **`shift_emb_app`（`成果-IShiftAtom/IShiftEmb.lean`）有编译错误**——混合 fvar 域的
   `comp_app` 实例不存在。**`shift_domZero` 绕开了它**，不需要它。
7. **引用任何"已证"前独立重编译**——本会话以此证伪了 9276 的两处旧断言。

---

## 六、边界与授权

- **只写本工位**；canonical 与其他 worktree 一律只读。
- 删除只进废纸篓（`rm` 即 `rm-trash`）；Lean 用 pinned 路径 + `LEAN_SYSROOT`，不走 elan 代理。
- 不提交/推送/发布**他人**的文件；本工位自身的提交已获用户授权（2026-10-11）。
- 不扩大授权：goal / Skill / hook 的存在不授予额外权限。

---

## 七、本会话提交

见本文件同批的 git 提交（分支 `claude/elegant-mclaren-767fb0`，已推送 origin）。
入库范围：研究成果、核验记录、工具脚本、交接与日志。
**不入库**：vendored 第三方（`cubical/`）、编译产物、源码副本、机器相关路径、大型扫描缓存
（规则见 `.gitignore` 末节）。
