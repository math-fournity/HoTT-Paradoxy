# CG001-C-422：判不全不靠排中律——图灵对角论证的逻辑核心

> **证明包**：`MP-CG001-HALTING-WITHOUT-LEM-001`（`GodelQ/Diagonal/QualificationDiag.lean`）；负控制 `MP-CG001-HALTING-WITHOUT-LEM-NEG-001`。
>
> **目标包**：CG-007（`.claude/goals/CG-007-formalization-completion/`），W8 之后的单元。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-14；独立 worktree `claude/012-opus-w8`。
>
> **理论变体**：Lean 4（v4.34.0）内核。
> - `GodelQ/Diagonal/Core.lean` 只用 Lean 内核，不导入 Mathlib。它的定理不依赖任何公理，由包内审计（`Lean.collectAxioms`）机器核对。
> - `MathlibCodes.lean` 用 Mathlib（`5ed29652`）的可计算性库，是经典的。
> - 不涉及 HoTT 路径。
>
> **身份**：机器证明，范围见 §2 与 §6。

## 0. 这一条在研究里的位置

- 研究发起人 2026-10-14 问：ZFC 不判定“是否可以停机”、ZFC-1 把无法停机过程的理想型目标当作现实存在物来运算，这与哥德尔不完备性在“不可停机”上的关联是什么。原话见 `dev-notes/0118` 第 11 轮。
- CN-079 回答：“判不全是现实”，即任何机器都判定不了停机，“这个证明用不到排中律”；ZFC 自己造出来的，只是“真而不可证”的那个缺口。
- 那一句当时标为凭记忆的文献判断。研究发起人随后要求继续后续工作，本包就把它的逻辑核心做成机器证明。
- 研究发起人的相关原话：KC-000027（09-11）：“无法写出一个程序来验证所有程序的可计算性、计算合法性，这是程序、计算的哥德尔不完备性。”

## 1. 记号

- **编程系统** `ProgSystem`：
  - 程序与输入都用自然数编号；
  - `Halts e x`：程序 `e` 在输入 `x` 上停机；
  - `SaysNo d e x`：程序 `d` 在输入“对子 (e, x)”上停机并回答“否”；
  - **翻转程序** `flip`：对每个程序 `d`，有程序 `f`，`f` 在 `x` 上停机，恰好当 `d` 对 (x, x) 回答“否”。
- **恰好认出“永不停机”** `RecognizesNever S d`：`d` 对 (e, x) 回答“否”，恰好当 `e` 在 `x` 上永不停机。
- **完全的停机判定器** `Decides S SaysYes d`：对每个 (e, x)，“是”恰好当停机，“否”恰好当永不停机。
- **Mathlib 实例**：
  - 程序是 `Nat.Partrec.Code`，按 `Denumerable.ofNat` 编号；
  - `codeHalts e x`：`Code.eval` 在 `x` 上有定义；
  - `codeSaysNo d e x`：`d` 在 `Nat.pair e x` 上的值是 0；
  - `codeSaysYes`：那个值是 1。

## 2. 精确命题（类型逐字见 `GodelQ/Diagonal/QualificationDiag.lean`）

| 编号 | 定理 | 内容 | 公理 |
|---|---|---|---|
| CG001-C-422 | `qual_C422` | (1) `¬ (P ↔ ¬P)`，即说谎者的形状推出矛盾；(2) 任何有翻转程序的编程系统里，没有程序恰好认出“永不停机”；(3) 也没有完全的停机判定器；(4) 正控制：去掉翻转程序，恰好认出“永不停机”的程序可以存在 | **不依赖任何公理**（审计机器核对） |
| CG001-C-422（实例） | `qual_C422_codes` | Mathlib 的计算模型有翻转程序（`code_flip`：先运行 `d`，答 0 就停，否则永不停）；于是那里没有程序恰好认出“永不停机”，也没有完全的停机判定器 | 经典：`propext`、`Classical.choice`、`Quot.sound` |

## 3. 承接了原话的哪一部分

- 【证明】“判不全”的逻辑核心不用排中律，实际上不用任何公理：假设有程序恰好认出“永不停机”，把它的翻转程序喂给翻转程序自己，就得到 `P ↔ ¬P` 的形状，矛盾。
- 【证明】这条论证在真实的计算模型里落地：Mathlib 的部分递归函数代码有翻转程序（`code_flip`）。
- 【判断】经典逻辑只出现在“翻转程序存在”这句正面的编程事实里，那是 Mathlib 可计算性库本身的写法，Mathlib 自己的 `ComputablePred.halting_problem` 也依赖它。“认不全”那一步不依赖它。
  - 所以 CN-079 那句话可以从凭记忆改为有证明：判不全不靠排中律。
  - 它是任何能写出翻转程序的计算装置的性质，不是哪个理论的选择造成的。
- **没有承接**：
  - 不用排中律的算术（Heyting 算术）同样不完备，这是关于理论的版本，仍是文献，本包没有证明；
  - 本包也不证明 Mathlib 那一侧的“翻转程序存在”可以构造地证出，那要一套不依赖选择公理的计算模型。

## 4. 公理审计（机器核对）

`QualificationDiag.lean` 末尾的 `run_cmd` 用 `Lean.collectAxioms` 核对，违反即报错，编译失败：
1. **构造一侧**：`qual_C422`、`no_liar`、`no_never_recognizer`、`no_decider`、`recognizer_without_flip` 不依赖 `Classical.choice`。实际的公理清单为空，审计把清单打印出来。
2. **对照一侧**：`code_flip`、`codeSystem`、`qual_C422_codes` 与 Mathlib 的 `ComputablePred.halting_problem` 必须依赖 `Classical.choice`。这说明审计不是空的，也说明仓库里此前经 Mathlib 停机定理的证明（C-86、C-104、C-420 等）都是经典的。

## 5. 与已有命题的关系

- **C-86、C-104、C-105、C-420**：这些结果都经 Mathlib 的停机定理，是经典的证明。C-422 给出同一个对角论证的构造性核心，并在同一个计算模型里落地。
- **C-418**：两次选择在构造性底座上是同一条原则。C-422 说明“判不全”本身不需要那条原则：不用 LPO，也不用排中律。
- **CN-079 §3.1**：“判不全是现实，‘真而不可证’是 A 造的缺口”。前半句的计算部分由本包支付。

## 6. 负控制

| proof id | 文件 | 被否定的说法 | 预期 |
|---|---|---|---|
| `MP-CG001-HALTING-WITHOUT-LEM-NEG-001` | `GodelQ/Negative/WrongRecognizerWithoutFlip.lean` | 在“什么都不停机、判定器一律回答‘否’”的系统里，也没有程序恰好认出“永不停机”（照搬对角论证，但没有翻转程序） | 拒绝：`hd d d` 是 `True ↔ ¬False`，不是 `P ↔ ¬P` 的形状；正面定理 `recognizer_without_flip` |

## 7. 文件

- `GodelQ/Diagonal/Core.lean`：编程系统、对角论证、正控制（只用 Lean 内核）；
- `GodelQ/Diagonal/MathlibCodes.lean`：Mathlib 计算模型的翻转程序与实例（经典）；
- `GodelQ/Diagonal/QualificationDiag.lean`：命题对照与公理审计；
- `GodelQ/Negative/WrongRecognizerWithoutFlip.lean`：负控制；
- `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`：固定的 Lean 文件与导入闭包的逐模块哈希。

## 8. 禁止外推

1. 不推出 ZFC ⊢ ⊥，也不说经典数学错了。
2. 构造一侧的定理以“翻转程序存在”为前提。这条前提在 Mathlib 的计算模型里被证明了，但那个证明是经典的；本包不声称有一个完全不用选择公理的计算模型。
3. 这是关于“程序认出永不停机”的结果，不是关于理论的不完备性（Heyting 算术的不完备是文献，没有证明）。
4. “判不全是现实”“A 造的缺口”是 CN-079 的读法，不是定理。
5. 图灵的定理是经典结果（1936）。新的只是把“它不用排中律”在仓库里机器核对，并接到研究发起人的读法上。
