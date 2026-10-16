# godel-q-zfc-runner-arrival：跑者的到达句（CG001-C-117、C-118）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W5，本机会话 d58e0c0d，Opus 5.5，2026-10-09。精确命题与禁止外推见 `CLAIM.md`。

## 这个包做了什么

C-101 把哥德尔–芝诺跑者落到 𝗭𝗙𝗖 上时，留了一个参数：一族“到达句”，要求 𝗭𝗙𝗖 逐个证明它与永不停机句等价。本包给出这一族句子，并付清这个参数。

- **到达句是什么**：通常的数学说“跑者到了”，是说剩余距离趋于 0。也就是说，对每个精度 2⁻ᴷ，从某一步起剩余距离都不超过它。剩余距离 ≤ 2⁻ᴷ，恰是“到这一步，跑者已经减半至少 K 次”，也就是前 K 步那个过程都还没停。这句话可以直接写成算术句，再经翻译写成集合论的句子 `arrS a`。
- **𝗭𝗙𝗖 证明了什么**：对每个过程，𝗭𝗙𝗖 证明“它的跑者到达”当且仅当“它永不停机”。到达句不是永不停机句本身：一个以“存在”开头，一个以“任意”开头。在 𝗭𝗙𝗖 的标准模型里，到达句的意思恰是跑者到达。
- **由此得到**：C-101 的跑者部分不再带参数。有一个跑者确实到达，𝗭𝗙𝗖 在每一刻都确认它尚未停，位置每一刻都小于 1，极限也存在，𝗭𝗙𝗖 却证明不了它的到达句。
- **C-115 也改用到达句**：C6 的审查里，“证明标准解不充分”现在取作证明到达句，即证明极限判词“到了”。仍有无穷多个、列不全的跑者，标准解对它确实出错，𝗭𝗙𝗖 却证明不了。
- **一个技术点**：旧的停机公式 `ΦH` 是 Foundation 用选择公理挑出的 Σ1 公式，在非标准模型里怎样表现无从推理。所以本包另写了一个停机公式 ΦS，它与到达句来自同一个“到第 k 步为止已停机”的公式。等价是对 ΦS 证的。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 21 个依赖模块 | 逐字节复制：18 个自 `godel-q-zfc-z0-pa`，3 个自 `idea-t-c6-p` |
| `GodelQ/ZFC/ArrivalArith.lean` | 算术层：θ、`stopF`、`haltsF`、`halvedF`、`arrF`；𝗣𝗔⁻ 模型里的等价；剩余距离与减半次数；标准模型里的读法 |
| `GodelQ/ZFC/ArrivalZFC.lean` | 𝗭𝗙𝗖 层：ΦS、`arrS`、`𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a`；`zfcEffective'`、`zfcRunner`；C-101 不带参数；C-115 改用到达句 |
| `GodelQ/ZFC/QualificationArrival.lean` | 命题对照 `qual_C117`、`qual_C118` |
| `GodelQ/Negative/WrongArrivalOldPhi.lean` | 负控制：同一论证换成旧的停机公式 |
| `GodelQ/Negative/WrongHaltingRunnerArrives.lean` | 负控制：会停的过程的到达句为真 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,889 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-01 --rerun --expect-rejected
```

另一个负控制把 `NEG-01` 换成 `NEG-02`。

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-001` | 接受 | 0（73 秒，stderr 0 B；139 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-01` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001` | 拒绝 | 1：类型不符（`haltsS ΦS a` 对 `haltsS ΦH a`） | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-02` | `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-002` | 拒绝 | 1：目标 `¬(zero.eval 0).Dom` 未解 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-*.json`。索引：同目标的 `证据索引.md` §33，以及共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具已进入收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
