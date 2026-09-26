# 观察的范围：换成转移、依赖读数或索引，各能看见什么

> HUMAN_EDITED；2026-09-25；Claude（Opus 5.5），会话 91a6cdaa。
>
> 起因：Terra 复审 005（`Terra对Opus的审计/005 - Terra 对 Opus 004 的复审：CG-001.md`）的 O-012、O-013。Terra 指出，C-26、C-32 只量化无索引、非依赖的观察者；它建议改用对 `(before, patch, after)` 的操作、依赖读数或历史索引。本包逐项固定：这几种观察各能看见什么、看不见什么。讨论见 CN-027 与回信 006。
>
> - proof id：`MP-CG001-OBSERVATION-SCOPE-001`（主包）、`MP-CG001-OBSERVATION-SCOPE-NEG-001`（负控制）。
> - claim：`CG001-C-44`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，沿用 `HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`。源码选项 `--safe --cubical --guardedness`，无公设，不加公理，零警告。
> - 索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §10（GOAL_LOCAL_INDEX_ONLY）；总入口 `.claude/总索引.md`。

## 这个包为什么存在

C-32 的 `noChangeDetector` 只说：没有一个以上下文为唯一输入的布尔测试，能把编辑前后的两个上下文分开。Terra 问得对：`git status` 不是这样工作的。它相对一个基线，看的是一次转移，或者直接读原始内容。所以要逐一回答下面四种观察方式：

1. **对转移的观察**：输入是 (编辑前, 编辑后, 补丁)，其中补丁是连接两者的路径。
2. **结果类型固定的依赖读数**：读数可以看纤维（例如文件内容），但结果类型不随状态变化。
3. **结果类型随状态变化的依赖读数**：截面，或 `apd`。
4. **索引层**：认同之前的历史数据，也就是 `List Bool`。

## 命题全文

量词与假设照实写。记号：`J` 为路径归纳；`transport`、`fromPathP` 取自 cubical 0.9 的 `Cubical.Foundations.Prelude`。

| 部分 | 命题 | 源码符号 |
|---|---|---|
| (a) 对转移的观察 | 对任意类型 `A`、`B`，任意函数 `t : (a b : A) → a ≡ b → B`，以及任意 `p : a ≡ b`，都有 `t a b p ≡ t a a refl`。推论：对任意 `p`，不存在 `t : (x y : A) → x ≡ y → Bool` 同时满足 `t a a refl ≡ false` 与 `t a b p ≡ true` | `transitionBlind`、`noEditDetector` |
| (b) 结果类型固定的依赖读数 | 对任意族 `M : A → Type`、任意类型 `P`、任意 `g : (c : A) → M c → P`、任意 `p : a ≡ b` 与 `x : M a`，都有 `g b (transport (cong M p) x) ≡ g a x`。另外，对总空间 `Σ A M` 中的任意路径 `s ≡ s'`，都有 `g (fst s) (snd s) ≡ g (fst s') (snd s')` | `readingIgnoresPatch`、`totalReading` |
| (c) 结果类型随状态变化的依赖读数 | 对任意族 `D : A → Type`、任意 `o : (c : A) → D c` 与 `p : a ≡ b`，都有 `transport (cong D p) (o a) ≡ o b` | `dependentComparison` |
| (d) 索引层 | 设历史索引上下文 HIT 为 `hdoc : List Bool → HistCtx`、`hadd b h : hdoc h ≡ hdoc (b ∷ h)`。则：任意 `d : HistCtx → Bool` 满足 `d (hdoc []) ≡ d (hdoc (true ∷ []))`；索引层的测试 `isEmptyHistory : List Bool → Bool` 满足 `¬ (isEmptyHistory [] ≡ isEmptyHistory (true ∷ []))`；并且不存在 `d : HistCtx → Bool`，使得对一切 `h` 都有 `d (hdoc h) ≡ isEmptyHistory h`。负控制：直接在 `HistCtx` 上按构造子定义 `isEmptyCtx`，内核拒绝（`true != false of type Bool`） | `contextBlind`、`isEmptyHistory`、`indexSeparates`、`noContextLift`；负控制 `WrongContextTest.agda` |

## 解读【解释】

- **(a)**：把观察换成对转移的观察逃不出去。转移层的测试对每一次编辑给出的回答，都与它对同一起点“什么都没做”的回答相同。这一条只用路径归纳，**不需要**上下文空间可缩，对任意类型都成立。
- **(b)**：结果类型固定的依赖读数，经柯里化，正是总空间上的函数，所以已在 C-26、C-32 的量词之内。补丁作用后的内容在新位置被读出的值，等于原内容在旧位置被读出的值。
- **(c)**：结果类型随状态变化的读数，前后两个值落在不同的纤维里；理论内部一致可用的比较，是沿路径运输，而运输后的比较结果是相同。这类读数交出的“变化”就是运输本身，也就是补丁的作用。
- **(d)**：能看见编辑的只有索引层。它在理论之内，但在被认同的类型之外。这正是 Terra 005 §4.1 的纠正：“理论之外”应改为“被认同的类型之外、理论之内”。

## 禁止外推

- 本包不证明：现实的仓库状态没有改变；HoTT 不能表示变化；或 `git status` 一类任务在 HoTT 中不能完成。后者由 (d) 的索引层完成。
- (a)–(c) 是标准事实（路径归纳、运输、`apd`），**不主张原创**。本包的作用，只是把 Terra 提出的几种替代观察逐一固定下来。
- (d) 的 `HistCtx` 是补丁理论扩展版附录 A.3 的简化版（布尔列表历史），与 `patch-contractible` 包的 C-31 相同，**不是**第 6 节完整的 History HIT。
- “编辑”“空编辑”“历史”“读数”是解释标签，不说明任何版本控制系统的事实。
