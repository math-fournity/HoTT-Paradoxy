# `zfcTr-D3-plan.md` 独立评审（第四份，Codex 会话接管后，2026-10-11）

> **性质**：对 `zfcTr-D3-plan.md` 的独立评审，附在旁边，不修改原计划。
> 继 `zfcTr-D3-plan-revision.md`（第二位 AI）、`Z0-D3-攻关包-最小完整版/PLAN-REVISION.md`
> （第三位 AI）、`zfcTr-D3-plan-review-3.md`（第三位 AI 的评审）之后。
> 本评审在 Codex 接管 Claude 的 CG-007 工作后写成，核对的实物是本机
> `/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`，308 个 .lean）
> 与仓库 `HoTT/formal/claude-cg001/godel-q-zfc-z0-full/` 的全量源码。

## 0. 直接回答：这个计划对吗？

**方向对，缺口定位已被后续工作缩小，但“缩小后的缺口”仍是真缺口。**

| 项 | 判断 | 依据 |
|---|---|---|
| §3 的 Bridge′ 弱化 | **正确且关键** | C-128（`Z0Bridge.lean`）已据此证成条件归约 |
| §4 `of_provability` 语义性 | **正确** | `LK/Interpretation.lean:443` 经完备性定理，无内化版本（全量 grep 确认） |
| §5 移植 ~1080 行 Σ1 完全性 | **不必做** | Foundation 的 `DerivabilityCondition/D3.lean` 已对 `Sh.craig` 直接 `inferInstance` 给出完整 D3（见 review-3 §2 三条实测） |
| §5.1 的 L1–L5 | **不必做** | 同上——Foundation 已做完，无需在本包重做 |
| §8 验收标准 | **正确，可采用** | F-011 五件事：落源码、三条标准公理、正负运行、收据、索引更新 |

## 1. 缺口的真实形状（与计划不同，请注意）

原方案把缺口写成“重做经翻译的 Σ1 完全性”。后续三段接续工作（Claude 的 W8、第三位 AI 的
`ShCraigElim` 系列、review-3）把它收得更小：

- C-390（`Z0UniBridge.lean`）把 Z0 完整形式归约到 `ShCraigElim`：
  `∀ σ, Provable Sh.craig ⌜σ⌝ (V) → Provable 𝗭𝗙𝗖 ⌜translate σ⌝ (V)`；
- `ShCraigElim` 再经 `bwd_of_shcraig_elim`（`keyE` 的 `bwd` 方向）归约；
- 已证的零件：C-391 `iVE` 计算规则与 `isSemiformula_iT`、C-392 归纳不变量 Σ1 谓词、
  C-393 `hWk`/`isFormulaSet_translateSeq`、C-394 `iT_quote_neg`、C-396 `iT`/`neg` 相容律
  九支中的五支、C-397 码层面 `neg` 对合律八支；
- **最后一步 = 证 `ShCraigElim` 剩余的 `nrel`/`all`/`exs` 支与 `hAxL`/`hCut`/`hShift` 三支回填**，
  及 `--rerun` 抓到正式收据。

也就是说：**真正的缺口不是“重做 Σ1 完全性”，而是一条句法消去链的一个方向**（`keyE.bwd`）。
它比原始方案估计的小得多，但仍然是一条尚未机器证明的精确引理，不是措辞问题——把 D3
改写成别的形式也绕不过同一数学内容（Foundation 的 `of_provability` 是语义的，搬不进 𝗜𝚺₁）。

## 2. 给下一个 AI 的补全包已备好

原计划与最小攻关包都只带了 169 个 Foundation 源文件，而项目闭包在 `1fb01b72` 下实际依赖
**308 个** Foundation 模块。第三位 AI 在沙箱里没有 Lean/Mathlib/Foundation，且 zip 只有 4 个
模块，所以无法编译、只能手推。

为此已新建 `外部资料/Z0-D3-攻关包-完整版/`：

- `Foundation/`：Foundation 全量源码 **308 个** .lean（commit `1fb01b72`，逐字一致）；
- `Project/`：目标证明包 `godel-q-zfc-z0-full` 全量（45 个 .lean + 配置），与仓库逐字一致；
- `Plans/`：三份计划/评审原文；
- `FOUNDATION_MODULES.md` + `foundation_modules_urls.txt`：308 个模块名、相对路径、
  **GitHub 原始地址**（`https://raw.githubusercontent.com/FormalizedFormalLogic/Foundation/1fb01b72.../<相对路径>`，
  已对 `D3.lean` 验证返回 200 / 8708 bytes），方便联网机器逐条 `curl -O` 复现；
- `README.md`：缺口定位、复现环境、下一件事的精确说明。

下一个 AI 现在可以在一个**完备、可编译**的基础上专攻 `ShCraigElim` 的剩余证明，而不是卡在缺模块。

## 3. 复现环境（务必照此，否则 import 闭包对不上）

- Lean 4.34.0（`leanprover/lean4:v4.34.0`）；本机 `/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0`。
- Foundation 源码 `/Volumes/D/HoTT-toolchain-cache/foundation-src`（commit `1fb01b72`）。
- Foundation olean 构建 `/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean`。
- 增量编译 `/tmp/d3build/devbuild.py`；收据工具仓库内
  `.claude/goals/CG-007-formalization-completion/tools/capture_run.py`、
  `verify_cg001_run.py`（见 `Project/README.md`、`BUILD.md`）。
- 配置锁 `Project/LEAN_TOOLCHAIN.json`、`Project/MATHLIB_CLOSURE.json`（commit 固化）。

## 4. 验收（与原计划 §8、仓库 F-011 门禁一致）

1. `ShCraigElim` 及组装后的 `zfcTr_D3_internalize` 落源码，无 `sorry`；
2. `#print axioms` 仅含 `propext`、`Classical.choice`、`Quot.sound`；
3. 正运行 + 至少一个负控制（内核应拒绝的变体）；
4. `capture_run.py` 抓到正式 run receipt，`verify_cg001_run.py --rerun` 精确重放一致；
5. 更新 CG-001 证据索引、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`形式化追踪/`。

一旦上列通过，`Z0Full.zfc_z0_full_of_D3_internalize` 立即给出 Z0 完整形式
`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ`，整个“形式化与机器证明”主线即告完成。
其余 8 个 git worktree 方向（图灵路线、时间结构、C6、HoTT 一侧、同一个 Q、抽象层综合、
分支形式包、更早形式化）在 `形式化追踪/README.md` 中均已标记 ✅ 或条件完成，无需再处理。
