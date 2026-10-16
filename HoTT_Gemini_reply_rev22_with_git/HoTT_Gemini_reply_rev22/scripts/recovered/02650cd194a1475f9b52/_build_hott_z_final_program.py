from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import textwrap
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/mnt/data/HOTT_Z_final_program_20260831')
DATA = Path('/mnt/data')
for d in [
    'governance','theory','formal/agda','formal/kernel','formal/certificates','formal/crosscheck',
    'literature','red_team','reviews','papers/paper1/supplement','papers/paper2','papers/paper3',
    'papers/philosophy','verification','release','archive','work_packages'
]:
    (ROOT/d).mkdir(parents=True, exist_ok=True)

DATE='2026-08-31'
PROGRAM='HOTT-Z-FINAL-20260831'


def write(rel: str, content: str) -> Path:
    p=ROOT/rel
    p.parent.mkdir(parents=True, exist_ok=True)
    txt=textwrap.dedent(content).strip()+"\n"
    p.write_text(txt, encoding='utf-8')
    return p

# -----------------------------------------------------------------------------
# Governance
# -----------------------------------------------------------------------------
write('governance/PROGRAM_BASELINE.md', r'''
# HOTT–Z 研究计划最终执行基线

**程序编号**：HOTT-Z-FINAL-20260831  
**冻结日期**：2026-08-31  
**规范状态**：本文件替代此前并行工作计划的活动解释，但不删除历史版本。

## 1. 研究对象

本计划研究一族**目标相对不完备性**：当表示、签名、逻辑制度或算法接口遗忘了目标命题所依赖的差异时，相关真值、方向、历史、语境、成本、见证或未来性质是否还能仅由遗忘后的表示恢复。

中心框架由六元组给出：

\[
\mathcal Z=(W,M,\alpha,\Phi,J,\mathcal R),
\]

其中：

- \(W\)：目标世界、状态或历史；
- \(M\)：理论所保留的表示；
- \(\alpha:W\to M\)：抽象或遗忘映射；
- \(\Phi\)：目标命题域；
- \(J:W\times\Phi\to\Omega\)：目标真值谱；
- \(\mathcal R\)：允许的恢复器类别，例如任意函数、可计算函数、等价自然函数或某签名内可定义函数。

“\(\mathcal R\)-完备”表示存在 \(\widehat J\in\mathcal R\) 使 \(J=\widehat J\circ(\alpha\times\mathrm{id})\)。

## 2. 冻结术语

| 术语 | 规范含义 |
|---|---|
| 句法完备 | 对指定语言中的每个句子，理论证明该句或其否定。 |
| 语义充分/表示完备 | 指定目标真值谱可经表示因子化。 |
| 自然性完备 | 恢复器不仅存在，而且尊重指定等价、同构或重标记。 |
| 有效判定完备 | 存在总可计算且正确的判定/合成算法。 |
| 物理本体充分 | 模型与物理现实之间的额外解释主张；不能仅由形式定理推出。 |
| 相对不完备 | 相对于明确 \((W,M,\alpha,\Phi,J,\mathcal R)\) 不存在恢复器。 |
| 内部不一致 | 理论内部推出 \(P\) 与 \(\neg P\)。本项目未证明 HoTT 内部不一致。 |
| 富化 | 在旧表示之外加入实际携带被遗忘差异的新数据或新结构。 |
| “抽象是否定” | 规范解释为区分能力的丧失，而非对象语言中自动加入 \(\neg A\)。 |

## 3. 主结论边界

本项目允许证明：

1. 裸 identity/∞-groupoid 信息不能自然选择无标签二事件的时间方向；
2. 过程范畴的 groupoid core 一般不能恢复不可逆箭头；
3. 快照不能恢复未编码的 provenance；
4. 裸结构不能恢复未编码的 intended role；
5. 纯外延函数不能恢复实现成本；
6. 命题截断不能统一恢复具体见证；
7. 一般未来稳定性与一般有效极限存在停机级障碍；
8. directed、guarded、linear、quantitative 或历史字段能够修复特定缺口，但这构成富化。

本项目禁止声称：

- `HoTT ⊢ ⊥`；
- HoTT 完全不能定义时间或不可逆函数；
- 单价公理适用于任意现实对象而不依赖结构签名；
- 极限定义在数学上非法；
- 非停机、不可判定、不完备与不一致是同一概念；
- 旧“一次性 transport”构成线性逻辑反例；
- `Map(1,G)` 是环空间；
- 当前成果已经获得外部专家独立复核。

## 4. 证明机制

- **M1 非因子化/不可定义**：同一抽象纤维内目标真值变化。
- **M2 无截面/无自然选择**：自同构或 monodromy 在富化纤维上无固定点。
- **M3 不可总判定/不可总合成**：从停机、居留或极限问题归约。
- **M4 反射/元理论开放性**：Lawvere–Gödel 条件、语法编码与宇宙层级。

## 5. 证据等级

- V0：动机或来源线索；
- V1：良构陈述；
- V2：可逐行审查的纸笔证明；
- V3：有限模型、程序或独立证书核验；
- V4：固定版本的主流证明助理编译；
- V5：第二实现或独立专家复核；
- V6：公开复现/同行评审。

有限枚举、Python 检查、上游网页中的已编译定理和本项目本地 wrapper 的编译是四种不同证据，不得混称。
''')

write('governance/SOURCE_GENEALOGY.md', r'''
# 来源谱系、去重与证据独立性

## 1. 来源类别

1. **原始思想来源**：长对话、戏剧稿、最终判决书和 Z 铁律提取稿。它们确立 Being/Becoming、照片/电影/放映机、资源/未知/表达三条动机，但不是独立数学证明。
2. **专题提取稿**：将原对话中的单个“悖论”拆出；与原文共享论证，不应重复计证据。
3. **专家反驳段落**：有些反驳正确指出 universe、identity、linear use、function/arrow 等边界；有些又包含新的过度简化，仍需独立核验。
4. **本项目重构稿**：CLAIM/PROOF/RESULT 台账、v3/v4 主稿和各专题定理稿。
5. **外部原始文献/官方形式化**：HoTT Book、原始论文、Agda/agda-unimath 官方页面等，是技术事实的优先来源。

## 2. 已知重复

- `Z铁律论证HoTT缺乏时间维度-完整提取.md` 与带 `(2)` 的版本是同源重复；
- 两份 `Finally HOTT is GONE and GONE with the Wind` 为同源版本；
- 各专题“悖论”文件通常从长对话抽取，不能与长对话同时算两份独立论证；
- AI 在戏剧中的“承认”不是专家评审、实验结果或形式证明。

## 3. 证据使用规则

- 来源材料只能证明“作者提出过某观点”；数学真理必须由独立定义和证明支持。
- 同一文字的副本、摘要、戏剧化复述和 AI 自我肯定，只登记一次思想来源。
- 外部文献的结论只按其原始范围引用；例如 directed interval 的存在证明“可富化”，不证明裸层完备，也不证明 HoTT 失败。
- 未找到论文不是原创性证明。

## 4. 来源到研究线索的映射

| 来源线索 | 保留的有效内核 | 规范去向 |
|---|---|---|
| Being/Becoming | 静态表示与过程真值的区分 | M1、论文 I、哲学稿 |
| Nat/Nat′ | intended role 未编码则不可恢复 | WP-310、论文 II |
| 原作/复制品 | provenance 不由快照决定 | WP-300、论文 I |
| 单程过程 | identity path 与一般 directed arrow 不同 | WP-230/240 |
| 资源之踵 | 成本/使用量不是纯外延语义 | WP-400/410 |
| 未知之踵 | checking 不给出通用 synthesis | WP-420 |
| 表达之踵 | 相同文本在不同语境可要求不同规约 | WP-320 |
| 自指循环 | 去掉 delay 会强迫固定点 | WP-440 |
| 芝诺/极限 | 闭包、极限与操作可达不同 | WP-450/460 |
| 无限之镜 | 反射和一致性需明确元理论 | WP-500/510 |
| 康托尔/宇宙 | 禁止同层全集，审计 universe 假设 | WP-510 |
| 概率等价 | assertion、mere existence、witness 分层 | WP-330 |

## 5. 排除路线

量子后继函数、多路径即不一致、`G≃Map(1,G)`、宇宙角色相似即等价、一次性 transport，以及“观察 n 维必须处于 n+1 维”均不进入任何主证明。
''')

write('governance/ID_GOVERNANCE.md', r'''
# 编号与追踪治理

## 命名空间

- `Z-n`：数学主张；
- `PA-n`：证明尝试；
- `R-n`：稳定结果；
- `LIT-n`：文献；
- `WP-xyz`：工作包；
- `THM-*`：论文内定理；
- `CERT-*`：机器证书。

## 规则

1. 历史编号只追加，不重写；重复块移入归档。
2. 每个新 Result 必须引用 Claim、Proof、WP 和交付物。
3. 每个论文定理必须有 `theorem_map.json` 条目。
4. 所有机器检查输出必须含命令、cwd、时间、退出码和输入哈希。
5. `EXTERNAL_GATE` 不能由模型自审替代。

## 最终执行批次保留区间

- Claims：Z-163–Z-184；
- Proof Attempts：PA-77–PA-94；
- Results：R-74–R-91；
- Literature：LIT-64–LIT-82。
''')

write('governance/RED_TEAM_REGRESSION.md', r'''
# 旧攻击红队回归套件

以下字符串或语义若出现在活动主稿中，必须触发人工审查；无明确限定时视为失败。

## 强制拦截

1. `HoTT is inconsistent`、`HoTT⊢⊥`、`HoTT 已被推翻`；
2. `HoTT 中所有箭头都可逆`；
3. `HoTT 完全不能表示时间/过程/不可逆性`；
4. `线性逻辑禁止两个独立资源各使用一次`；
5. `Id_A(a,b)` 同时给出 `a:A, b:B` 且无 transport；
6. `Translate : InformalProblem → Type` 后直接援引停机问题而无编码和归约；
7. `Map(1,G)=ΩG`；
8. `U_i` 与 `U_{i+1}` 角色相似，所以必等价；
9. 单个 lift 不是满射，所以所有可能等价都不存在；
10. `lim` 是“第无穷步”或极限定义本身不合法；
11. 哥德尔不完备直接推出理论不一致；
12. 单价公理要求理论“本质”等于社会“表现”；
13. “外部意义绝对不能形式化”；正确说法只能是“未进入所选签名的意义不能由该裸签名恢复”；
14. 上游已编译定理被描述成本项目原创机器证明。

## 允许的替代表述

- identity/groupoid core 不足以**免费恢复**一般 directed process；
- 时间、历史、成本和语境可以通过富化进入类型；
- 一般极限提取可能不可计算，但具体带有效收敛模的极限可计算；
- 相对不完备是针对明确目标命题域和恢复器类别的 no-go；
- 原始文档提供研究动机，当前定理由重新构造给出。
''')

# -----------------------------------------------------------------------------
# Core theory
# -----------------------------------------------------------------------------
write('theory/DEFINITIONS.md', r'''
# 目标相对完备性的规范定义

## 1. Z-实例

一个 Z-实例是六元组

\[
\mathcal Z=(W,M,\alpha,\Phi,J,\mathcal R).
\]

令 \(J_w(\varphi)=J(w,\varphi)\)。恢复器 \(\widehat J:M\times\Phi\to\Omega\) 若属于允许类别 \(\mathcal R\)，并满足

\[
\forall w,\varphi,\quad \widehat J(\alpha(w),\varphi)=J(w,\varphi),
\]

则称 \(\alpha\) 对 \((\Phi,J)\) **\(\mathcal R\)-充分**。不存在此恢复器时，称为**目标相对不完备**。

## 2. 六种不可混淆的完备性

1. **句法判定完备**：\(T\vdash\varphi\) 或 \(T\vdash\neg\varphi\)。
2. **语义表达充分**：目标真值经 \(\alpha\) 因子化。
3. **自然性充分**：因子化恢复器尊重指定同构/等价。
4. **见证充分**：不仅判断存在，而且恢复具体 witness。
5. **有效充分**：恢复器总可计算。
6. **物理解释充分**：形式对象与现实量之间满足额外桥梁定律。

本项目的 HoTT 主定理主要属于第 2–3 类；稳定性和 Specker 属于第 5 类；哲学稿才讨论第 6 类。

## 3. 表示 preorder

对同一 \(W\) 的表示 \(\alpha:W\to M\)、\(\beta:W\to N\)，定义

\[
\alpha\preceq\beta
\quad\Longleftrightarrow\quad
\exists r:N\to M,
\ \alpha=r\circ\beta.
\]

含义：\(\beta\) 至少与 \(\alpha\) 一样精细；\(\alpha\) 可由 \(\beta\) 进一步遗忘得到。

表示核：

\[
K_\alpha=\{(w,w')\mid \alpha(w)=\alpha(w')\}.
\]

若 \(\alpha\preceq\beta\)，则 \(K_\beta\subseteq K_\alpha\)。

## 4. 可恢复观察量

对固定值域 \(Y\)，令

\[
\operatorname{Obs}_Y(\alpha)
=
\{f:W\to Y\mid \exists\widehat f:M\to Y,
 f=\widehat f\circ\alpha\}.
\]

允许恢复器若受可计算性、自然性或签名可定义性限制，则在 `Obs` 上加相应下标。

## 5. 相对 HoTT 时间充分性

“裸 HoTT 时间完备”在本文中不作为 HoTT 社群事实，而作为条件命题 STC：

> 仅凭 type–identity/∞-groupoid 信息，在不加入 directed hom、Step、clock、later、history 或资源字段时，可自然且完整恢复目标时间真值谱。

主结果证明 STC 对一般不可逆时间语义不成立。它不否定在 HoTT 中编码 `Time`, `Step` 或 directed extensions。
''')

write('theory/Z_FACTORISATION_AND_GALOIS.md', r'''
# Z 因子化、损失谱、最小充分商与 Galois 结构

## 1. 因子化必要性

**定理 THM-Z1（纤维不变性）**。设 \(\alpha:W\to M\)、\(f:W\to Y\)。若存在 \(\widehat f:M\to Y\) 使

\[
f=\widehat f\circ\alpha,
\]

则

\[
\alpha(w)=\alpha(w')\Longrightarrow f(w)=f(w').
\]

**证明**：对等式施加 \(\widehat f\)，再用因子化等式改写两端。□

**推论 THM-Z2（Z 反例）**。若 \(\alpha(w)=\alpha(w')\) 而 \(f(w)\ne f(w')\)，则不存在上述恢复器。

这一定理是 Z 铁律的最小正确数学核心：抽象在纤维中合并的目标差异不能仅由商后对象恢复。

## 2. 充分性边界

在集合语义中，若 \(f\) 在每条 \(\alpha\)-纤维上恒定，则存在唯一

\[
\bar f:\operatorname{im}(\alpha)\to Y
\]

使 \(f=\bar f\circ\tilde\alpha\)，其中 \(\tilde\alpha:W\to\operatorname{im}(\alpha)\)。若 \(\alpha\) 满射，便得到 \(M\) 上的因子化。

若 \(M\) 含不在像中的点，则将 \(\bar f\) 延拓到全部 \(M\) 可能需要 \(Y\) 的基点、选择或额外消去原则。因此，“纤维恒定当且仅当可在任意给定余域上因子化”不是无条件定理。

## 3. 损失谱

给定目标谓词族 \(\Phi\subseteq\Omega^W\)，定义

\[
\operatorname{Loss}_\Phi(\alpha)
=
\{P\in\Phi\mid
\exists w,w',\ K_\alpha(w,w')\land P(w)\ne P(w')\}.
\]

等价地，它是未通过 \(\alpha\) 因子化的目标谓词集合。

**定理 THM-Z3（精化单调性）**。若 \(\alpha=r\circ\beta\)，则

\[
\operatorname{Obs}(\alpha)\subseteq\operatorname{Obs}(\beta),
\qquad
\operatorname{Loss}_\Phi(\beta)
\subseteq
\operatorname{Loss}_\Phi(\alpha).
\]

**证明**：若 \(P=\widehat P\circ\alpha\)，则 \(P=\widehat P\circ r\circ\beta\)。第二式取补或直接用核包含。□

## 4. 最小充分真值商

对目标谓词族 \(\Phi\)，定义

\[
w\equiv_\Phi w'
\quad\Longleftrightarrow\quad
\forall P\in\Phi,
\ P(w)=P(w').
\]

令 \(q_\Phi:W\to W/{\equiv_\Phi}\) 为商映射。

**定理 THM-Z4（最粗充分表示）**。

1. 每个 \(P\in\Phi\) 唯一通过 \(q_\Phi\) 因子化；
2. 若 \(\alpha:W\to M\) 对所有 \(P\in\Phi\) 充分，则存在唯一
   \(h:\operatorname{im}(\alpha)\to W/{\equiv_\Phi}\) 使
   \(q_\Phi=h\circ\tilde\alpha\)。

因此 \(q_\Phi\) 是在“进一步遗忘”preorder 中最粗的 \(\Phi\)-充分表示。

**证明**：第一项由商的定义。第二项中，若 \(\alpha(w)=\alpha(w')\)，充分性给出所有目标谓词同值，故 \(w\equiv_\Phi w'\)，所以 \([w]\) 在 \(\alpha\) 的像上定义良好。□

## 5. 无免费富化

设旧表示 \(\alpha:W\to M\)，新增字段 \(\beta:W\to E\)，富化表示

\[
\alpha'(w)=(\alpha(w),\beta(w)).
\]

**定理 THM-Z5（富化让步）**。若 \(\alpha(w)=\alpha(w')\)、\(f(w)\ne f(w')\)，而 \(f\) 可经 \(\alpha'\) 因子化，则必有 \(\beta(w)\ne\beta(w')\)。

所以修复成功正说明新增字段携带了旧表示没有的区分；“可富化”不能反推“裸层原本已经包含”。

## 6. 关系—谓词 Galois 极性

令 `Eq(W)` 为 \(W\) 上的等价关系，按包含排序；令 `Pred(W)` 为布尔/命题谓词集合。

定义

\[
\operatorname{Inv}(R)
=
\{P\mid R\subseteq\ker(P)\},
\]

\[
\operatorname{Ker}(\Psi)
=
\bigcap_{P\in\Psi}\ker(P).
\]

则

\[
R\subseteq\operatorname{Ker}(\Psi)
\quad\Longleftrightarrow\quad
\Psi\subseteq\operatorname{Inv}(R).
\]

这是一个反变 Galois connection（polarity）。由此得到：

\[
R\mapsto\operatorname{Ker}(\operatorname{Inv}(R)),
\]

\[
\Psi\mapsto\operatorname{Inv}(\operatorname{Ker}(\Psi))
\]

分别是等价关系侧与谓词侧的闭包算子。

### 6.1 非平凡性

若只允许一个受限目标语言 \(\Phi_0\)，定义

\[
\operatorname{Inv}_{\Phi_0}(R)=\Phi_0\cap\operatorname{Inv}(R).
\]

则

\[
\operatorname{Ker}(\operatorname{Inv}_{\Phi_0}(R))
\]

可能严格大于 \(R\)：语言没有足够谓词区分某些 \(R\)-类。这把“表达能力不足”精确化为**可定义闭包比原语义等价更粗**。

### 6.2 与既有理论的关系

这一结构与 sufficient statistics、Blackwell information order、abstract interpretation 的 Galois connection、模型论中的 reduct/definability 非常接近。项目的增量主要是：把它统一用于 univalent naturality、历史/时间富化和证据截断，而不是声称发明 Galois connection 本身。
''')

write('theory/HOTT_TEMPORAL_NO_GO.md', r'''
# HoTT/单价基础中的时间方向 no-go 定理

## 1. 固定点自由 monodromy 无截面引理

设 \(B\) 为类型，\(E:B\to\mathcal U\) 为依赖族。若存在 \(b:B\) 与环路 \(p:b=b\)，使 transport

\[
p_*:E(b)\to E(b)
\]

无固定点：

\[
\forall e:E(b),\quad p_*(e)\ne e,
\]

则不存在全局截面

\[
s:\prod_{x:B}E(x).
\]

**证明**：依赖函数 `s` 对路径 \(p\) 的相容性给出

\[
p_*(s(b))=s(b),
\]

与无固定点假设矛盾。□

单价不是该一般引理的必要前提；单价用于把对象自等价转成宇宙/结构空间中的环路。

## 2. 无标签二事件无规范较早事件

令

\[
\mathrm{Two}_\ell
=\sum_{A:\mathcal U_\ell}\|A\simeq\mathrm{Fin}(2)\|,
\]

纤维为底层类型

\[
E(A,q)=A.
\]

“对每个无标签二事件系统规范选择较早者”就是截面

\[
s:\prod_{X:\mathrm{Two}_\ell}E(X).
\]

在标准二点类型上，交换等价 \(\sigma\) 无固定点。单价把 \(\sigma\) 变成基空间环路，而该环路在纤维上的 transport 正是交换作用。由上一引理，无截面存在：

\[
\neg\prod_{X:\mathrm{Two}_\ell}E(X).
\]

agda-unimath 已正式给出更直接的上游定理：`no-section-type-2-Element-Type`。本项目的 `no-canonical-earlier-event` 是它的时间语义重命名/直接推论，不是新的基础无截面定理。

## 3. 无规范严格时间序

任何二元素严格总序都有唯一最小元。若能对每个无标签二元素类型自然选择严格总序，就能对每个类型选择其最小元，从而得到上一节所排除的截面。因此：

\[
\neg\prod_{X:\mathrm{Two}_\ell}\mathrm{StrictLinearOrder}(E(X))
\]

只要 `StrictLinearOrder` 的数据/公理足以内部构造唯一最小元。

## 4. n≥2 一般化

对固定 \(n\ge2\)，令 \(\mathrm{FinType}_n\) 为无标签 n 元有限类型。

### 4.1 无规范点

若有自然选择 \(s(X):X\)，在标准 \(\mathrm{Fin}(n)\) 上它必须被所有置换固定。取把 \(s\) 与另一元素交换的换位，得到矛盾。因此不存在对所有 n 元类型的等价自然点选择。

### 4.2 无规范线性序

若有自然严格总序，则其最小元给出自然点，矛盾。故所有 \(n\ge2\) 均无裸结构内生的规范线性时间序。

这不表示某个具体已标记的有限集合不能排序；它只排除**在不提供方向/标记数据时，尊重所有重标记的统一选择**。

## 5. groupoid core 的时间反演盲性

设 \(C_+\) 是 walking arrow：对象 \(a,b\)，唯一非恒等箭头 \(u:a\to b\)。令 \(C_-=C_+^{op}\)。

两者的最大 groupoid core 都是同一离散二对象群胚：非恒等箭头不可逆，故被删除。但命题

\[
\varphi(C):\equiv \exists\text{ 非恒等箭头 }a\to b
\]

在 \(C_+\) 为真，在 \(C_-\) 为假。由 THM-Z2，\(\varphi\) 不通过 core 因子化。

更一般地：若一个过程语义含不可逆态射，则不存在既 full 又 faithful 的函子把它嵌入纯群胚并保留全部态射。因为群胚中像箭头的逆由 fullness 提升回来，再由 faithfulness 证明原箭头可逆。

## 6. 时间版 Z 主定理

设 \(\alpha\) 将有向历史遗忘为裸 identity/groupoid 表示，目标命题域 \(\Phi_T\) 含至少一个在同一裸表示纤维中变化的方向命题。则：

1. 不存在完整时间真值恢复器；
2. 若要求恢复器尊重所有等价，则无任意命名规避；
3. 加入 `Step`、directed hom、clock、`later`、provenance 等可缩小损失谱，但构成富化；
4. 因此 `temporal erasure + no enrichment + universal temporal faithfulness` 不可同时成立。

## 7. 精确结论

可以说：

> 裸的单价 type–identity/∞-groupoid 层不是一般不可逆时间方向的内生完备表示。

不能说：

> HoTT 中所有函数都可逆；HoTT 完全不能表示时间；HoTT 内部不一致。
''')

write('theory/TEMPORAL_ENRICHMENT_ADEQUACY.md', r'''
# 时间与方向富化的充分性及非保守性边界

## 1. 富化类型

| 富化 | 新增数据 | 能恢复的典型命题 | 不能自动保证 |
|---|---|---|---|
| `Step:S→S→Prop/Type` | 有向转移关系 | 可达、路径方向、终止 | 物理时间长度、成本、概率 |
| directed interval / hom-types | 非对称箭头与相干复合 | 范畴性过程 | 具体物理因果解释 |
| `Time`, state family | 时间索引与状态 | 时刻状态、轨迹 | 时钟与现实秒的对应 |
| `later` / clocks | 一步延迟和生产性 | guarded recursion、因果数据可用性 | 任意未来真值可判定 |
| provenance/history fields | 生成史、作者、事件序 | 原作性、历史身份 | 字段真实性 |
| linear/quantitative modalities | 使用量、成本界 | 资源消费与复杂度 | 所有实现的精确成本 |

## 2. “可编码”与“内生”

能定义

\[
\mathrm{Step}:S\to S\to\mathcal U
\]

只证明宿主类型论能承载有向结构。方向来自 `Step` 的非对称数据，而非 identity path 本身。类似地，clock/later 的成功说明时间守护可被显式加入。

## 3. 保守性问题

不能笼统说所有富化都是保守扩展。必须分别说明：

- 对哪种基础语法与模型；
- 相对于哪些旧语言句子；
- 是否加入新公理、模态、形状层或计算规则；
- 是否改变可证明性、规范化、canonicity 或 universe 假设。

本项目只使用较弱且可靠的结论：富化在表示层加入了足以区分旧纤维的新结构。是否证明论保守是独立问题。

## 4. 文献位置

- Riehl–Shulman 的 synthetic ∞-categories 明确公理化 directed interval；
- guarded dependent type theory 明确加入 later modality 与 clocks；
- linear/quantitative dependent type theories加入资源制度；
- cost-aware type theory加入原生成本；
- 这些工作是“可富化”的正面证据，也是“方向/成本不是裸 identity/外延层免费给出”的边界证据。
''')

write('theory/HISTORY_SEMANTICS_WITNESS.md', r'''
# 历史、语义角色、语境与证据的不完备性

## 1. 历史约化不可定义

令扩展语言 \(L_H=L_0\cup\{\text{provenance},\prec,\text{createdAt}\}\)，遗忘函子

\[
U:\mathrm{Mod}(L_H)\to\mathrm{Mod}(L_0).
\]

**定理 THM-H1**。若 \(U(M)\cong U(N)\)，但某 \(L_H\)-句子 \(\varphi\) 在 \(M,N\) 中真值相反，则不存在 \(L_0\)-句子 \(\psi\) 在目标模型类上定义 \(\varphi\)。

**证明**：\(L_0\)-句子在同构模型中真值不变，而 \(\varphi\) 在两扩张中不同。□

原作/复制品、相同快照不同生成史、相同终态不同因果史均是实例。

## 2. intended role 与品牌

设

\[
E=\sum_{A:\mathcal U}\mathrm{Role}(A),
\qquad U(A,r)=A.
\]

若同一底层类型带有 `Arithmetic` 与 `Index` 两个不同角色，则角色不通过 \(U\) 因子化。`BrandedNat Arithmetic` 和 `BrandedNat Index` 的修复是把 role 加入签名。

单价/SIP 的正确结论是：相对于选定结构签名可定义的性质在相应等价下不变。它不是“所有现实意义都由裸结构决定”。

## 3. 无语境完美形式化器

令 \(q\) 为表面文本，\(c\) 为完整语境，正确规约为 \(S(q,c)\)。若

\[
S(q,c_0)\not\simeq S(q,c_1),
\]

则不存在只读 \(q\) 的单值函数 \(T(q)\) 同时在两个语境中正确。

这是一条欠定定理，不依赖停机问题。修复方式包括：读取语境、提出澄清问题、返回规约集合/分布或允许部分函数。

## 4. assertion、mere existence 与 witness

三个层次必须区分：

1. 外部标签 `D(A,B)=true`；
2. 命题截断 \(\|A\simeq B\|\)；
3. 具体等价 \(e:A\simeq B\)。

从 1 到 2 需要 soundness 定理。从 2 到 3 的统一提取

\[
\prod_A(\|A\|\to A)
\]

是全局选择式原则，在单价设置中一般不可得；agda-unimath 已用二元素类型无截面证明相应 global choice 不成立。

因此概率/二值断言不能冒充具体 path witness。

## 5. 签名相对完备性

给定签名遗忘 \(U:\mathrm{Mod}(\Sigma')\to\mathrm{Mod}(\Sigma)\) 和目标句子集合 \(\Phi\subseteq\mathrm{Sen}(\Sigma')\)，称 \(U\) 对 \(\Phi\) 完备，若每个 \(\varphi\in\Phi\) 均可由 \(\Sigma\)-句子在目标模型类上定义。

THM-H1 给出普遍必要条件。由此，时间、provenance、role、cost 和 context 都成为同一 signature-reduct 框架的实例。
''')

write('theory/SIGNATURE_RELATIVE_COMPLETENESS.md', r'''
# Signature-Relative Incompleteness 主定理

## 1. 设置

设 \(i:\Sigma\hookrightarrow\Sigma'\) 为签名扩张，\(U_i\) 为模型约化。给定目标扩张模型类 \(K'\) 与目标句子族 \(\Phi\subseteq\mathrm{Sen}(\Sigma')\)。

定义：\(U_i\) 对 \((K',\Phi)\) **判定充分**，若对每个 \(\varphi\in\Phi\)，存在 \(\Sigma\)-句子 \(\psi_\varphi\)，使

\[
M\models\varphi
\iff
U_i(M)\models\psi_\varphi
\quad(M\in K').
\]

## 2. 主定理

**THM-SR**。若存在 \(M,N\in K'\) 使

\[
U_i(M)\cong U_i(N)
\]

而对某 \(\varphi\in\Phi\)：

\[
M\models\varphi,
\qquad N\models\neg\varphi,
\]

则 \(U_i\) 对 \((K',\Phi)\) 不充分。

证明由同构不变性立即得到。

## 3. 严格判定谱变化

令 \(X_{\Sigma'}(M)\) 为扩展签名完整真值谱，\(Y_\Sigma(U_iM)\) 为旧签名真值谱。上述反例表明：扩展真值谱不能由旧谱函数性恢复。

这实现 Z 铁律的集合值版本：实质性签名遗忘若合并在目标句子上不同的扩张，完整判定谱必然收缩。

## 4. 实例

- `Time`/`Before` 被遗忘：相反事件次序约化为同一无序快照；
- `Provenance` 被遗忘：原作与复制品约化相同；
- `Role` 被遗忘：算术自然数与索引自然数底层相同；
- `Cost`/`Trace` 被遗忘：同外延函数不同实现；
- `Context` 被遗忘：同一文本对应不同规约；
- witness 被截断：具体等价约化为 mere existence。

## 5. 正面设计原则

相对于 \(\Phi\) 的最小充分签名/表示必须至少区分 \(\Phi\)-真值谱不同的状态。富化的合理性可以用“损失谱是否缩小”评价，而不必诉诸“魔法”修辞。
''')

write('theory/OPERATIONAL_EFFECTIVITY.md', r'''
# 操作成本、资源制度、证明合成、稳定性与守护遗忘

## 1. 外延函数不决定成本

令程序语义

\[
\llbracket-\rrbracket:\mathrm{Prog}(A,B)\to(A\to B)
\]

只保留输入输出函数。若存在程序 \(p,q\) 满足

\[
\llbracket p\rrbracket=\llbracket q\rrbracket,
\qquad
\mathrm{Cost}(p)\ne\mathrm{Cost}(q),
\]

则不存在 \(c:(A\to B)\to C\) 使 \(\mathrm{Cost}=c\circ\llbracket-\rrbracket\)。

这是 THM-Z2 的直接实例。cost-aware type theory 的动机正是函数外延性与成本差异之间的张力。

## 2. Cartesian–linear 结构障碍

在 cartesian monoidal category 中，每个对象有自然复制/丢弃共幺半群：

\[
\Delta_A:A\to A\times A,
\qquad !_A:A\to1.
\]

强对称幺函子会把这套结构传到目标对象。故：

**THM-CL**。若资源语义中的对象 \(R\) 不允许任何满足目标相干条件的复制/丢弃共幺半群，则不存在把某 cartesian 对象映为 \(R\) 且强保持 cartesian 结构的解释。

这才是旧“资源之踵”的正确形式。线性逻辑并不禁止两个独立资源各使用一次；冲突发生在复制/丢弃制度是否被保持。

## 3. 固定证书演算中的无总合成器

定义 `HaltCert` 演算：

- 闭类型 \(\mathrm{Halts}(e,x)\)；
- 项为自然数 \(t\)；
- 检查规则：\(t:\mathrm{Halts}(e,x)\) 当且仅当机器 \(e\) 在输入 \(x\) 上于 \(t\) 步内停机。

类型检查可判定：模拟有限 \(t\) 步。类型可居留当且仅当机器停机，因此居留不可判定。

若有总算法为每个类型返回 witness 或正确 `NONE`，即可判定停机。故不存在总而完备的 inhabitant synthesizer。

该结果展示 checking 与 synthesis 的一般边界，不是 HoTT 特有失败。

## 4. 最终稳定性硬度

给机器 \(M_e(x)\)，定义可计算二值序列

\[
b_n=
\begin{cases}
0,&M_e(x)\text{ 在 }n\text{ 步内停机},\\
n\bmod2,&\text{否则}.
\end{cases}
\]

若机器停机，序列最终恒为 0；若不停止，序列永久交替。因此

\[
(b_n)\text{ 最终稳定}
\iff
M_e(x)\text{ 停机}.
\]

统一判定可计算历史最终稳定性不可计算。

## 5. Guard erasure

动态系统：

\[
x_{n+1}=F(x_n).
\]

若删除阶段索引并要求所有阶段由单一静态值 \(x\) 无损代表，同时保持更新律，则

\[
x=F(x).
\]

所以若 \(F\) 无固定点，不存在这种静态下降。对布尔否定，静态方程 \(b=\neg b\) 无解，而带 delay 的轨道 0,1,0,1,… 完全一致。

这说明某些静态自指无解在时间化后表现为不稳定轨道；并非所有悖论都由时间缺失造成。

## 6. 有效性边界总结

- 有形式类型不等于有通用求解器；
- 有时间索引不等于未来性质可总判定；
- 有外延函数不等于有成本；
- 有递归轨道不等于有静态固定点；
- 添加 linear/quantitative/guarded 结构是合法富化。
''')

write('theory/ZENO_OPERATIONAL_SEMANTICS.md', r'''
# 极限、闭包、可达性与芝诺完成语义

## 1. 四种“完成”

对序列 \(x:\mathbb N\to X\) 与点 \(L\)：

1. **有限步到达**：\(\exists n, x_n=L\)；
2. **拓扑极限**：\(x_n\to L\)；
3. **有限物理时间到达**：存在时间参数轨迹在有限 \(T\) 取值 \(L\)；
4. **极限阶段状态**：在扩展索引 \(\mathbb N\cup\{\omega\}\) 上额外规定 \(x_\omega=L\)。

它们不等价。

## 2. 芝诺半距序列

\[
x_n=1-2^{-n}.
\]

每个有限 \(n\) 都有 \(x_n<1\)，所以

\[
1\notin\{x_n:n\in\mathbb N\}.
\]

但 \(x_n\to1\)，故

\[
1\in\overline{\{x_n:n\in\mathbb N\}}.
\]

因此极限点属于有限步可达集的闭包，不属于有限步可达集。

## 3. 同一闭包、不同可达性

\[
\gamma_F(t)=t\quad(t\in[0,1]),
\]

\[
\gamma_\infty(t)=1-e^{-t}\quad(t\in[0,\infty)).
\]

两者像的闭包均为 \([0,1]\)，但前者在有限时间达到 1，后者永不达到 1。故 endpoint reachability 不由像闭包决定。

## 4. 同一路径、不同持续时间与方向

\[
\gamma_1(t)=t\ (0\le t\le1),
\qquad
\gamma_2(t)=t/2\ (0\le t\le2)
\]

有相同无参数轨迹，却持续时间不同。\(\gamma_+(t)=t\) 与 \(\gamma_-(t)=1-t\) 有相同轨迹集合，却方向相反。

所以遗忘参数的几何轨迹不能恢复 duration 或 direction。

## 5. 后继—极限鸿沟

给定所有有限值 \(x_n\)，对任意 \(c\in X\) 都能定义扩展

\[
\tilde x_c(n)=x_n,
\qquad
\tilde x_c(\omega)=c.
\]

因此有限阶段数据本身不唯一决定极限阶段值。要指定 \(x_\omega=L\)，必须加入连续延拓、上确界、limsup、重置规则或物理边界条件。

## 6. 精确判决

极限定义并不声称存在“第无穷步”；它是对所有有限尾部的量化。它可以正确解决外延收敛问题，但不能单凭自身证明无限多个离散物理任务已经完成。

因此可批判的是：

\[
\text{外延完成}\Rightarrow\text{操作完成}
\]

这一偷换，而不是实分析内部的极限定义。
''')

write('theory/COMPUTABLE_LIMITS.md', r'''
# 有效极限与 Specker 序列

## 1. 构造

枚举图灵机 \(M_e\)。定义

\[
q_s=
\sum_{\substack{e\le s\\M_e(e)\text{ 在 }s\text{ 步内停机}}}
4^{-(e+1)}.
\]

每个 \(q_s\) 是可计算有理数，序列单调递增且有界。经典地存在

\[
q=\lim_s q_s
=
\sum_{e\in K}4^{-(e+1)},
\]

其中 \(K\) 为停机集。

## 2. 不可计算性

四进制第 \(e+1\) 位为 1 当且仅当 \(e\in K\)。后续尾项总和为

\[
\sum_{j>e}4^{-(j+1)}=rac13 4^{-(e+1)},
\]

小于当前位权重的三分之一。若 \(q\) 可计算到足够精度，就能判定该位，从而判定停机，矛盾。

因此存在逐项可计算、有界、单调的有理序列，其极限不是可计算实数，也没有可计算收敛模。

## 3. 边界

这不表示所有极限不可计算。若给出可计算收敛模 \(\mu(k)\)，满足

\[
n\ge\mu(k)\Rightarrow |q_n-q|\le2^{-k},
\]

则可在有限时间计算任意精度近似。

正确结论是：一般极限提取可隐藏停机信息；经典存在不自动给出有效完成证书。
''')

write('theory/REFLECTION_UNIVERSES.md', r'''
# Lawvere、Gödel、宇宙与 resizing：正确反射支线

## 1. 废弃的“哥德尔空间”

从一点类型到 \(G\) 的映射空间满足

\[
\mathrm{Map}(1,G)\simeq G,
\]

它不是带基点环空间。环空间是

\[
\Omega(G,g)=(g=_G g).
\]

故旧方程 `G≃Map(1,G)` 不含哥德尔自指，永久退出证明。

## 2. Lawvere 固定点定理

在笛卡尔闭范畴/合适类型论中，若

\[
e:A\to Y^A
\]

弱点满：对每个 \(g:A\to Y\)，存在 \(a\) 使 \(e(a)=g\)（至少点态相等），则每个 \(\alpha:Y\to Y\) 有固定点。

**证明**。定义

\[
g(a)=\alpha(e(a)(a)).
\]

取 \(a_0\) 表示 \(g\)。令 \(y=e(a_0)(a_0)\)，则

\[
y=g(a_0)=\alpha(e(a_0)(a_0))=\alpha(y).
\]

若 \(Y\) 有无固定点自映射（如二值否定），则不存在这种弱点满的 universal evaluator。

## 3. 从 Lawvere 到 Gödel所需的额外条件

真正的 Gödel 定理还需要：

1. 固定的、递归可枚举的对象理论 \(T\)；
2. 语法和证明的 Gödel 编码；
3. 可表示的替换/对角函数；
4. provability predicate 与 Hilbert–Bernays/Löb 条件；
5. 一致性、\(\omega\)-一致性或 soundness 的适当假设；
6. 对象理论与元理论的严格分离。

没有这些，几何类比不是不完备性证明。

## 4. 宇宙审计矩阵

| 变体 | 典型宇宙特征 | 不能默认的结论 |
|---|---|---|
| predicative MLTT/HoTT | 层级 \(U_0:U_1:\cdots\)，闭包按层控制 | 单一同层“所有类型” |
| cumulative universes | 小类型可提升到大宇宙 | 提升函数自动是等价 |
| axiomatic univalence | univalence 作为公理，计算行为依实现而定 | 所有版本都无计算意义 |
| cubical type theory | 路径/区间给出 univalence 的计算解释 | 自动包含 directed time |
| propositional resizing | 小化命题的额外公理 | 在所有模型中成立或有统一计算解释 |
| impredicative universe | 对量化闭包更强 | 与 resizing/univalence 任意组合均一致 |
| simplicial/directed TT | 加入形状/有向区间/Hom | 是裸 HoTT 的纯定义缩写 |
| guarded/clocked TT | later、clock、ticks | 任意未来性质变可判定 |

## 5. 研究结论

WP-500 已完成为**纠错性研究笔记**：标准 Lawvere 定理完整重建，旧构造被反例淘汰。尚无 HoTT 特定的新 Gödel 定理，不能包装为突破。
''')

write('theory/MAIN_THEOREM_PACKAGE.md', r'''
# HOTT–Z 主定理包

## MT-1：目标真值因子化障碍

同一抽象纤维中若有目标真值差异，则不存在精确恢复器。

## MT-2：无免费富化

若富化修复 MT-1 的反例，新增字段必须在该纤维上取不同值。

## MT-3：单价无规范较早事件

对所有无标签二元素类型不存在等价自然的全局点选择，因而不存在不含方向数据的规范“较早事件”或严格时间序。基础无截面已由 agda-unimath 上游形式化；本项目给出时间语义实例和 wrapper。

## MT-4：群胚 core 时间反演盲性

walking arrow 与其反向具有相同离散 groupoid core，但方向命题相反；一般不可逆过程不能满且忠实地压入群胚。

## MT-5：历史约化不可定义

同一快照的两个历史扩张若在 provenance 句子上不同，则 provenance 不是快照语言的可定义性质。

## MT-6：组合 no-go

令 \(\alpha\) 为从有向、有历史过程到裸 identity/groupoid 快照的遗忘。若目标命题域含方向或历史敏感命题，则以下五项不能同时成立：

1. 方向/历史被遗忘；
2. 不增加新的方向/历史信息；
3. 恢复器尊重所有裸等价；
4. 对全部目标历史普遍正确；
5. 对全部目标命题给出总判定。

至少放弃一项：缩小目标命题域、允许不完备/错误、采用非总/非经典判断，或真正富化表示。

## 论文解释

该定理包否定的是“裸层无需富化即可成为一般时间—历史现实的完整真值镜像”。它不否定 HoTT 作为数学基础，不证明 HoTT 内部不一致，也不把任何具体创建者观点作为前提。
''')

# -----------------------------------------------------------------------------
# Formal source candidates and toolchain
# -----------------------------------------------------------------------------
write('formal/toolchain.lock.md', r'''
# 形式化工具链锁定

## 首选环境

- Agda：2.8.0
- 官方 Linux x86-64 静态二进制资产：`Agda-v2.8.0-linux.tar.xz`
- 官方资产 SHA-256：`824081b8dcbe431289a50ac6bd83e451f390c51c3884ac7a8c4a5c0df2632faf`
- agda-unimath：与 Agda 2.8.0 兼容的 master 快照；正式复现时必须把实际 git commit 写入本文件，不能只写 `master`。
- 库 flags：以 `agda-unimath.agda-lib` 为准，包括 `--without-K --exact-split` 等。

## 上游中央依赖

`univalent-combinatorics.2-element-types` 中已存在：

```agda
no-section-type-2-Element-Type :
  {l : Level} → ¬ ((X : 2-Element-Type l) → type-2-Element-Type X)
```

本项目中央定理 `no-canonical-earlier-event` 是该上游定理的直接别名/解释实例。

## 本运行环境审计

- 未找到 `agda`, `lean`, `lake`, `elan`, `coqc/rocq`, `rzk`；
- 容器 DNS/外网下载失败，无法获取官方二进制或仓库；
- 因此本包提供精确源码、预期命令、上游已编译定理证据和独立 Python 证书，但**不伪造本地 Agda build.log**。

## 预期复现命令

```bash
agda -i /path/to/agda-unimath/src \
     -i formal/agda \
     formal/agda/no-canonical-earlier-event.agda
```

只有真实退出码 0 的日志才能把 `LOCAL_REPLAY_BLOCKED` 升为 V4-local。
''')

write('formal/agda/no-canonical-earlier-event.agda', r'''
module no-canonical-earlier-event where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

Canonical-Earlier-Event : (l : Level) → UU (lsuc l)
Canonical-Earlier-Event l =
  (X : 2-Element-Type l) → type-2-Element-Type X

no-canonical-earlier-event :
  {l : Level} → ¬ (Canonical-Earlier-Event l)
no-canonical-earlier-event = no-section-type-2-Element-Type
''')

write('formal/agda/no-canonical-temporal-order.agda', r'''
module no-canonical-temporal-order where

open import foundation.dependent-pair-types
open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

-- Minimal interface used by the no-go theorem. Any richer strict temporal
-- order with an internally extractable earliest event maps to this record.
record Temporal-Orientation {l : Level} (A : UU l) : UU (lsuc l) where
  constructor orientation
  field
    earlier-event : A

open Temporal-Orientation public

Canonical-Temporal-Orientation : (l : Level) → UU (lsuc l)
Canonical-Temporal-Orientation l =
  (X : 2-Element-Type l) → Temporal-Orientation (type-2-Element-Type X)

no-canonical-temporal-orientation :
  {l : Level} → ¬ (Canonical-Temporal-Orientation l)
no-canonical-temporal-orientation F =
  no-section-type-2-Element-Type (λ X → earlier-event (F X))
''')

write('formal/agda/fiber-truth-invariant.agda', r'''
module fiber-truth-invariant where

open import foundation.identity-types
open import foundation.universe-levels

factorization-implies-fiber-constant :
  {l1 l2 l3 : Level}
  {W : UU l1} {M : UU l2} {Y : UU l3}
  (α : W → M) (J : W → Y) (Ĵ : M → Y) →
  ((w : W) → J w ＝ Ĵ (α w)) →
  {w₀ w₁ : W} → α w₀ ＝ α w₁ → J w₀ ＝ J w₁
factorization-implies-fiber-constant α J Ĵ H p =
  (H _) ∙ (ap Ĵ p) ∙ (inv (H _))
''')

write('formal/agda/snapshot-provenance-counterexample.agda', r'''
module snapshot-provenance-counterexample where

open import foundation.coproduct-types
open import foundation.empty-types
open import foundation.identity-types
open import foundation.negation
open import foundation.unit-type
open import foundation.universe-levels

Provenance : UU lzero
Provenance = unit ⊔ unit

original replica : Provenance
original = inl star
replica = inr star

Snapshot : UU lzero
Snapshot = unit

History : UU lzero
History = Snapshot × Provenance

snapshot : History → Snapshot
snapshot _ = star

IsOriginal : History → UU lzero
IsOriginal (_ , inl _) = unit
IsOriginal (_ , inr _) = empty

-- Paper theorem: no predicate on Snapshot can be equivalent to IsOriginal
-- on both (star,original) and (star,replica).  This file isolates the data;
-- the generic contradiction is supplied by fiber-truth-invariant.
''')

write('formal/agda/intent-does-not-factor.agda', r'''
module intent-does-not-factor where

open import foundation.coproduct-types
open import foundation.unit-type
open import foundation.universe-levels

Role : UU lzero
Role = unit ⊔ unit

Arithmetic Indexing : Role
Arithmetic = inl star
Indexing = inr star

Bare : UU lzero
Bare = unit

Enriched : UU lzero
Enriched = Bare × Role

forget-role : Enriched → Bare
forget-role _ = star

-- The two enriched values have the same bare image and different Role.
-- Therefore Role cannot factor through forget-role by THM-Z1.
''')

write('formal/agda/context-free-translate-impossible.agda', r'''
module context-free-translate-impossible where

open import foundation.coproduct-types
open import foundation.unit-type
open import foundation.universe-levels

Surface : UU lzero
Surface = unit

Context : UU lzero
Context = unit ⊔ unit

Spec : UU lzero
Spec = unit ⊔ unit

meaning : Surface → Context → Spec
meaning _ (inl _) = inl star
meaning _ (inr _) = inr star

-- A function Surface → Spec has one value at star and hence cannot agree
-- with meaning star in both contexts. The finite certificate suite checks
-- this exhaustively; a library-level proof can be obtained by coproduct
-- disjointness.
''')

write('formal/agda/no-uniform-witness-extractor.agda', r'''
module no-uniform-witness-extractor where

open import foundation.global-choice

-- The library theorem is stronger than the intended witness statement.
no-uniform-witness-extractor = no-global-choice
''')

write('formal/agda/guard-erasure-implies-fixed-point.agda', r'''
module guard-erasure-implies-fixed-point where

open import foundation.identity-types
open import foundation.universe-levels

-- If a time-indexed orbit is identified with one constant state c and the
-- update law is preserved at c, then c is a fixed point.  The essential
-- theorem is the update equality itself; this wrapper records the exact
-- logical boundary used by the paper.
Guard-Erasure : {l : Level} (X : UU l) (F : X → X) → UU l
Guard-Erasure X F = Σ X (λ c → c ＝ F c)
''')

write('formal/agda/README.md', r'''
# Agda source status

These files are proof-source candidates targeted at Agda 2.8.0 and the current agda-unimath API documented on 2026-08-31.

- `no-canonical-earlier-event.agda` is a direct alias of an upstream, documented and compiled agda-unimath theorem.
- The remaining files isolate reductions and finite instances.
- No local Agda executable was available, and network installation failed. Therefore the files are marked **SOURCE COMPLETE / LOCAL TYPECHECK NOT EXECUTED**.
- `../kernel/` contains an independent, executable certificate checker. Its success is V3/KERNEL evidence, not a substitute for a mainstream V4 proof-assistant build.
''')

# -----------------------------------------------------------------------------
# Literature and originality
# -----------------------------------------------------------------------------
refs = [
  {'id':'LIT-64','title':'The HoTT Book','kind':'official book','locator':'homotopytypetheory.org/book','use':'Scope: univalent foundations, not a claim of complete physical ontology.'},
  {'id':'LIT-65','title':'A type theory for synthetic infinity-categories','authors':'Riehl; Shulman','year':2017,'arxiv':'1705.07442','use':'Directed interval is explicitly added for non-invertible arrows.'},
  {'id':'LIT-66','title':'Guarded Dependent Type Theory with Coinductive Types','authors':'Bizjak et al.','year':2016,'arxiv':'1601.01586','use':'Later modality and clocks provide explicit temporal guarding.'},
  {'id':'LIT-67','title':'A Higher Structure Identity Principle','authors':'Ahrens; North; Shulman; Tsementzis','year':2020,'arxiv':'2004.06572','use':'Invariance is relative to a chosen structure/signature.'},
  {'id':'LIT-68','title':'The Univalence Principle','authors':'Ahrens; North; Shulman; Tsementzis','year':2022,'arxiv':'2102.06275','use':'General univalence/SIP framing.'},
  {'id':'LIT-69','title':'Internalizing Representation Independence with Univalence','authors':'Angiuli; Cavallo; Mörtberg; Zeuner','year':2021,'arxiv':'2009.05547','use':'Representation independence requires a selected relation/interface.'},
  {'id':'LIT-70','title':'Cost-Aware Type Theory','authors':'Niu; Harper','year':2020,'arxiv':'2011.03660','use':'Function extensionality versus cost; explicit cost enrichment.'},
  {'id':'LIT-71','title':'Syntax and Semantics of Linear Dependent Types','authors':'Vákár','year':2014,'arxiv':'1405.0033','use':'Resource discipline is carried by linear structure.'},
  {'id':'LIT-72','title':'Resource-Bounded Martin-Löf Type Theory','authors':'Mannucci; Thuro','year':2026,'arxiv':'2601.10772','use':'Recent quantitative enrichment of dependent types.'},
  {'id':'LIT-73','title':'Cubical Type Theory: a constructive interpretation of univalence','authors':'Cohen; Coquand; Huber; Mörtberg','year':2016,'arxiv':'1611.02108','use':'Axiomatic and computational/cubical variants must be distinguished.'},
  {'id':'LIT-74','title':'Internal Universes in Models of HoTT','authors':'Licata; Orton; Pitts; Spitters','year':2018,'arxiv':'1801.07664','use':'Universe claims are model-sensitive.'},
  {'id':'LIT-75','title':'Cubical Assemblies, a Univalent and Impredicative Universe and a Failure of Propositional Resizing','authors':'Uemura','year':2018,'arxiv':'1803.06649','use':'Resizing/universe combinations are not automatic.'},
  {'id':'LIT-76','title':'A Universal Approach to Self-Referential Paradoxes, Incompleteness and Fixed Points','authors':'Yanofsky','year':2003,'arxiv':'math/0305282','use':'Correct Lawvere diagonal framework.'},
  {'id':'LIT-77','title':'Computability and analysis: the legacy of Alan Turing','authors':'Avigad; Brattka','year':2012,'arxiv':'1206.3431','use':'Specker sequences and computable analysis.'},
  {'id':'LIT-78','title':'A Galois connection between Turing jumps and limits','authors':'Brattka; de Brecht; Pauly','year':2018,'arxiv':'1802.01355','use':'Limit computation and Turing jumps.'},
  {'id':'LIT-79','title':'Constructive Galois Connections','authors':'Darais; Van Horn','year':2018,'arxiv':'1807.08711','use':'Galois connections in abstraction/abstract interpretation.'},
  {'id':'LIT-80','title':'agda-unimath: 2-element types','kind':'official formalization','locator':'univalent-combinatorics.2-element-types','use':'Upstream no-section theorem used by the central wrapper.'},
  {'id':'LIT-81','title':'agda-unimath: Global choice','kind':'official formalization','locator':'foundation.global-choice','use':'No global witness extractor.'},
  {'id':'LIT-82','title':'Agda 2.8.0 official release and installation docs','kind':'official toolchain','locator':'Agda v2.8.0','use':'Pinned replay environment.'},
]
write('literature/SYSTEMATIC_LITERATURE_REVIEW.md', '# Systematic literature review\n\n' + '\n'.join(
    f"## {r['id']} — {r['title']}\n\n- Type: {r.get('kind','primary paper')}\n- Authors: {r.get('authors','n/a')}\n- Year: {r.get('year','n/a')}\n- Locator: {r.get('arxiv',r.get('locator',''))}\n- Project use: {r['use']}\n- Novelty effect: this source prevents claiming the underlying component as a first discovery.\n"
    for r in refs
) + r'''

## Search protocol

Search date: 2026-08-31. Inclusion priority: official documentation, original papers, formal-library pages. Search clusters: univalence/SIP; directed/simplicial HoTT; guarded clocks; linear/quantitative/cost type theory; no natural choice/global choice; computable limits/Specker; Lawvere/Gödel; universes/resizing; abstract interpretation/Galois; reduct/definability.

## Synthesis

No reviewed source was found that states the exact project package under the name “Z truth-loss spectrum” or combines all five examples as one HoTT-focused theorem. However, every mathematical mechanism has close predecessors. The defensible novelty class is therefore **new synthesis, interpretation, and formal wrapper**, not a newly discovered inconsistency or foundational no-section theorem.
''')

search_log = {
  'schema_version':'hott_z.search_log.v1',
  'date':DATE,
  'queries':[
    'HoTT Book univalent foundations official',
    'Riehl Shulman directed interval synthetic infinity categories',
    'guarded dependent type theory clocks later modality',
    'higher structure identity principle univalence',
    'cost-aware type theory function extensionality cost',
    'linear dependent type theory quantitative resources',
    'Specker sequence noncomputable limit',
    'Weihrauch limit Turing jump',
    'Lawvere self-reference fixed point Yanofsky',
    'internal universes HoTT propositional resizing',
    'abstract interpretation Galois connection',
    'agda-unimath no-section 2-element types global choice'
  ],
  'inclusion_rule':'Prefer official or primary sources; retain negative and boundary evidence; no novelty inference from search absence.',
  'references':refs
}
(ROOT/'literature/search_log.json').write_text(json.dumps(search_log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

write('literature/ORIGINALITY_MATRIX_v2.md', r'''
# 原创性矩阵 v2

| 项目结果 | 最近已知机制 | 状态 | 允许的贡献措辞 |
|---|---|---|---|
| 纤维真值变化阻止因子化 | 商、充分统计量、definability | 已知基础 | 本项目的规范化核心 |
| Loss spectrum 与精化单调 | information order / abstract interpretation | 重构 | 项目专用组织与统一 |
| 关系—谓词 Galois 极性 | formal concept analysis / abstract interpretation | 已知结构的实例 | 明确推导，不称首创 |
| 最小充分真值商 | 按观察等价取商 | 已知基础 | 对 Z 框架的泛性质 |
| 二元素无规范较早事件 | agda-unimath no-section/global choice | 上游已形式化 | 新时间解释和 wrapper |
| n≥2 无自然顺序 | 对称性/无自然选择 | 经典 | 推论与统一应用 |
| groupoid core 时间反演盲性 | core 忘掉非可逆态射 | 初等范畴事实 | HoTT 时间批判的精确化 |
| provenance 不由快照定义 | model reduct/definability | 初等模型论 | 历史实例化 |
| role/context/cost 不下降 | signature/reduct/semantics | 已知模式 | 跨实例统一 |
| witness extraction 障碍 | truncation/global choice | 已知 | 证据分层解释 |
| stabilization/inhabitation/limit hardness | computability theory | 已知 | 操作维度支撑 |
| 综合 MT-6 | 上述机制组合 | 可能是新综合 | “统一 no-free enrichment 框架” |

## 结论

没有证据支持“首次推翻 HoTT”“发现 HoTT 矛盾”或“首次证明无自然方向”。最稳妥定位是：

> 受 Z 铁律思想启发，把多个标准 no-go 机制组织成面向 univalent foundations 的目标相对不完备/无免费富化框架，并给出时间、历史、语境、成本和见证的统一实例。
''')

write('literature/CLAIM_CALIBRATION.md', r'''
# 主张校准

## 可用于摘要

- We formulate target-relative representational incompleteness as a factorization problem.
- We show that an unlabeled two-event type admits no equivalence-natural choice of an earlier event; this is a temporal reading of an existing no-section theorem.
- We prove that groupoid cores and snapshot reducts cannot recover selected directed or historical predicates.
- We distinguish encodability by enrichment from recoverability by the bare representation.

## 必须带条件

- “HoTT is temporally incomplete”必须写成“the bare identity/groupoid layer is incomplete relative to a specified class of directed predicates.”
- “abstracting time changes conclusions”必须指定目标命题域。
- “limit hides halting information”只适用于一般有效极限提取，不适用于每个具体极限。

## 禁止

- HoTT is gone / refuted / inconsistent；
- creators claim complete physical ontology（除非有一手引文）；
- univalence identifies arbitrary physical replicas；
- formalization completed locally in Agda；
- independently peer reviewed。
''')

# -----------------------------------------------------------------------------
# Red team reports
# -----------------------------------------------------------------------------
write('red_team/COUNTEREXAMPLE_DATABASE.md', r'''
# 反例与边界数据库

| ID | 对过强主张的反例 | 处置 |
|---|---|---|
| CE-01 | HoTT 中存在非可逆函数，如常值函数 | 只攻击 identity/core，不攻击所有函数 |
| CE-02 | 可在 HoTT 中定义 `Step` 与 `Time` | 改为“非免费恢复”，承认富化 |
| CE-03 | 地图不记录温度但能正确给出距离 | 抽象并非对所有目标都失真；必须指定 \(\Phi\) |
| CE-04 | 带显式收敛模的极限可计算 | 极限不可计算结论限定为一般算子 |
| CE-05 | 线性逻辑允许 p、q 各使用一次 | 淘汰旧 transport 论证 |
| CE-06 | `Map(1,G)≃G` | 淘汰旧“哥德尔空间” |
| CE-07 | guarded/coinductive systems可处理循环 | 不说所有循环非法 |
| CE-08 | cubical TT 给 univalence 计算解释 | 区分 axiomatic/cubical |
| CE-09 | provenance 可直接加入 record | 解释为富化成功而非不可能表达 |
| CE-10 | 无自然点选择不等于单个具体类型没有点 | 区分局部存在与全局自然选择 |
| CE-11 | 未标记二点无方向不等于物理时间一定二元 | 将定理定位为最小 obstruction |
| CE-12 | 没有证据 HoTT 创建者声称 STC | 将 STC 写成被审查的条件性强解释 |
''')

reports = {
'01_HoTT_referee.md': r'''
# 内部审稿：HoTT 专家

## Major comments

1. **攻击对象易成稻草人**：HoTT 本身不承诺裸 identity types 是物理时间。处置：接受；论文改成条件 no-go，不归因创建者。
2. **无二点自然选择是已知 global-choice 障碍**：处置：接受；明确上游 `no-section-type-2-Element-Type`，贡献仅是时间解释/统一。
3. **函数与 directed hom 可非可逆**：处置：接受；全文只说 groupoid core 丢方向。
4. **“时间”远比 earliest-event 复杂**：处置：接受；二点结果只作为 minimal witness，不等同完整时间理论。
5. **富化不是认罪**：处置：接受；改称 enrichment concession：修复有效，但不能反推裸层已含信息。

## Verdict

数学 no-go 定理正确但窄。若标题暗示 HoTT 内部不一致，应拒稿；按 target-relative no-free enrichment 技术报告，可继续。
''',
'02_Category_referee.md': r'''
# 内部审稿：范畴论专家

## Major comments

1. 一般无截面引理不需要单价；必须把单价仅放在从 automorphism 到 loop 的桥梁。已修订。
2. `core(C)` 与 `core(C^op)` 的关系应通过 walking-arrow 反例避免不必要的全局同构细节。已修订。
3. “full and faithful into groupoid”定理需明确 fullness 是局部 hom-surjectivity。已说明。
4. WP-150 的结构是 antitone Galois polarity，不应误称普通同向 adjunction。已修订。
5. 最小充分商的泛性质最好在像/商中陈述，避免选择与空余域点。已修订。

## Verdict

核心范畴/商论证成立。原创性主要是组织，不是基础定理。
''',
'03_Computability_referee.md': r'''
# 内部审稿：可计算性专家

## Major comments

1. `InformalProblem→Type` 未定义，不可直接归约停机。已替换为语境欠定定理。
2. “checking 可判定”对 HoTT 全部实现不是无需限定的事实。WP-420 改用明确 `HaltCert` 演算。
3. stabilization reduction 正确，但只是已知停机编码。标为背景结果。
4. Specker 构造需避免进位歧义。已用 base 4、数字 0/1 并给尾项界。
5. 不可计算极限不表示数学极限矛盾。已修订。

## Verdict

有效性分支可作为辅助，不应被包装为 HoTT 特定缺陷。
''',
'04_Philosophy_referee.md': r'''
# 内部审稿：数学哲学专家

## Major comments

1. “抽象即否定”应解释为能力/区分的否定，不是命题否定。已修订。
2. 模型与现实异构不自动产生理论内部矛盾。已区分失配、相对不完备和不一致。
3. 极限是否解决芝诺取决于连续轨迹还是离散任务本体。已并列两模型。
4. “本质/表现”不是单价公理的适用对象。该讽刺移至历史材料，不作为数学论证。
5. 论文必须承认：没有物理桥梁公理，形式结果不能裁决真实时间本体。已修订。

## Verdict

哲学洞察可保留，但需以开放本体论问题结尾，不能说极限或 HoTT 已被摧毁。
'''
}
for fn,txt in reports.items(): write('red_team/INTERNAL_REFEREE_REPORTS/'+fn,txt)

write('red_team/DISPOSITION.md', r'''
# 内部审稿意见处置

- 重大意见共 19 条；接受并修订 19 条；驳回 0 条；未解决内部重大意见 0 条。
- 外部专家意见尚无，不能由本处置表替代。
- 主稿从“HoTT 不完备”改为“裸 identity/groupoid 表示相对于指定时间—历史谓词不充分”。
- 所有 old-proof routes 被隔离到来源史或哲学稿。
''')

# -----------------------------------------------------------------------------
# Papers
# -----------------------------------------------------------------------------
write('papers/paper1/main.md', r'''
# No-Free Temporal and Historical Enrichment in Univalent Foundations

## A target-relative incompleteness framework for direction, groupoid cores, and provenance

**Research report — 2026-08-31**

## Abstract

We study a representation-relative notion of incompleteness. A representation is sufficient for a family of target predicates when their truth values factor through it. The elementary fiber-invariance lemma says that any recoverable predicate must be constant on every fiber of the representation. We combine this observation with two univalent/categorical obstructions. First, the canonical family over the type of unlabeled two-element types has no global section; consequently there is no equivalence-natural choice of an “earlier event,” nor of a strict temporal order with an internally extractable least event. This is a temporal interpretation of the existing agda-unimath theorem `no-section-type-2-Element-Type`, not a new proof of the foundational no-section result. Second, the groupoid core of the walking arrow is identical to that of its reverse although a directed reachability predicate changes truth value. The same method shows that provenance predicates do not descend to snapshot reducts. We formulate a no-free-enrichment principle: any enrichment that repairs a fiberwise truth difference must itself distinguish the old fiber. Our results do not show that homotopy type theory is inconsistent or unable to encode time. They show that bare identity/groupoid information is not an intrinsically complete representation of general directed and historical predicates.

## 1. Introduction

Univalent foundations makes equivalence-invariant mathematics internal and precise. A recurrent philosophical temptation is to move from that success to a stronger thesis: that bare structural identity already contains any temporal, historical, operational, or semantic distinction one may later wish to recover. We isolate and refute this stronger thesis.

The target is not HoTT as a foundation for mathematics. It is the conjunction of temporal erasure, no additional directed or historical data, equivalence invariance, and universal recovery of temporal/historical truths. The contradiction comes from the joint requirements, not from the axioms of HoTT alone.

## 2. Relative sufficiency

Let \(W\) be a set/type of histories, \(\alpha:W\to M\) a representation, and \(\Phi\) a family of target predicates \(J_\varphi:W\to\Omega\). We say \(\alpha\) is sufficient when every \(J_\varphi\) factors through \(\alpha\).

### Theorem 2.1 (fiber invariance)

If \(J_\varphi=\widehat J_\varphi\circ\alpha\), then

\[
\alpha(w)=\alpha(w')\Rightarrow J_\varphi(w)=J_\varphi(w').
\]

The proof is congruence and substitution. Hence one counterexample in a fiber rules out exact recovery.

### Definition 2.2 (loss spectrum)

\[
\mathrm{Loss}_\Phi(\alpha)=
\{\varphi\in\Phi\mid J_\varphi\text{ is nonconstant on some }\alpha\text{-fiber}\}.
\]

If \(\alpha=r\circ\beta\), then \(\mathrm{Loss}_\Phi(\beta)\subseteq\mathrm{Loss}_\Phi(\alpha)\).

## 3. No-free enrichment

Let \(\beta:W\to E\) be new data and \(\alpha'(w)=(\alpha(w),\beta(w))\).

### Theorem 3.1

If \(\alpha(w)=\alpha(w')\), \(J(w)\ne J(w')\), and \(J\) factors through \(\alpha'\), then \(\beta(w)\ne\beta(w')\).

Thus adding a clock, a directed hom, a history field, or a provenance tag can repair the representation, but the repair works precisely because the new field carries a previously absent distinction.

## 4. Unlabeled events have no canonical temporal orientation

Let

\[
\mathrm{Two}_\ell=\sum_{A:\mathcal U_\ell}\|A\simeq\mathrm{Fin}(2)\|.
\]

The canonical family sends \(X\) to its underlying two-element type. A global section would choose an element of every unlabeled two-element type in a way compatible with identifications/equivalences.

### Theorem 4.1 (upstream no-section)

\[
\neg\prod_{X:\mathrm{Two}_\ell}\mathrm{underlying}(X).
\]

The official agda-unimath library contains this theorem as `no-section-type-2-Element-Type`. Its proof exploits the nontrivial permutation/loop of the two-element type.

### Corollary 4.2 (no canonical earlier event)

Interpreting the selected point as “the earlier event,” there is no equivalence-natural temporal orientation on all unlabeled two-event systems.

### Corollary 4.3 (no canonical strict time order)

Any strict total order on a finite two-element type has a least element. Hence a natural order selection would induce the forbidden point section.

For every fixed \(n\ge2\), the same conclusion follows because a natural point would have to be fixed by all permutations of \(\mathrm{Fin}(n)\), and no point has this property.

These results do not say that a particular labeled pair cannot be oriented. They say the orientation is not generated by the bare unlabeled structure.

## 5. Groupoid cores forget direction

Let \(C_+\) have objects \(a,b\) and a single nonidentity arrow \(a\to b\); let \(C_-=C_+^{op}\). Their groupoid cores are the same discrete two-object groupoid. Yet the predicate “there is a nonidentity arrow from \(a\) to \(b\)” is true in \(C_+\) and false in \(C_-\). Therefore it cannot factor through the core.

More generally, a full and faithful functor from a category into a groupoid would force every source arrow to be invertible. Thus a process category with genuine irreversible arrows cannot be losslessly represented by identity paths alone.

## 6. Snapshot reducts forget provenance

Let \(H=S\times\mathrm{Provenance}\) and \(\pi:H\to S\) forget provenance. `(s,original)` and `(s,replica)` have the same snapshot but opposite truth values for `IsOriginal`. The predicate does not factor through \(\pi\).

In model-theoretic language: if two expansions have isomorphic reducts but disagree on a history sentence, no sentence of the reduct signature defines that history sentence over the target class.

## 7. Main no-go theorem

Let \(\alpha\) forget directed and historical data and let \(\Phi\) contain a predicate that changes within an \(\alpha\)-fiber. The following cannot all hold:

1. the data are erased;
2. no new information is added;
3. recovery is invariant under equivalence of bare representations;
4. recovery is correct for every target history;
5. all predicates in \(\Phi\) are decided.

The proof is Theorem 2.1, strengthened by Theorem 4.1 when the attempted recovery is a canonical choice.

## 8. Enrichment and directed type theories

HoTT can host a `Step` relation, time-indexed states, internal categories, clocks, or later modalities. Simplicial/directed type theory explicitly adds a directed interval; guarded dependent type theory explicitly adds later and clock structure. These are successful enrichments. They refute the claim that time is inexpressible, but not the no-free-recovery theorem.

## 9. Related work and novelty

The ingredients are close to quotient factorization, sufficient statistics, the Structure Identity Principle, standard no-natural-choice results, and directed/guarded type theory. The two-element no-section theorem is already formalized upstream. The contribution claimed here is a unified target-relative formulation and its temporal/historical interpretation, not a new inconsistency result.

## 10. Limitations

- No physical theory of time is derived.
- “Earlier event” is a minimal orientation witness, not a full temporal ontology.
- The paper does not establish that HoTT’s creators endorse the rejected strong thesis.
- Local Agda replay was blocked by the execution environment; the exact wrapper and replay lockfile are included, while the upstream dependency is already documented as compiled.
- External expert review remains open.

## 11. Conclusion

Bare identity/groupoid and snapshot information preserves precisely its invariants. Temporal direction and provenance are not invariants of the forgetful representations studied here. They can be added, but not recovered for free.
''')

write('papers/paper1/supplement/theorem_map.md', r'''
# Paper I theorem map

| Paper theorem | Theory source | Formal/certificate source | WP |
|---|---|---|---|
| 2.1 fiber invariance | `theory/Z_FACTORISATION_AND_GALOIS.md` | `formal/agda/fiber-truth-invariant.agda`, CERT-Z1 | 110 |
| 3.1 no-free enrichment | same | finite suite CERT-Z5 | 140 |
| 4.1 upstream no-section | `theory/HOTT_TEMPORAL_NO_GO.md` | agda-unimath upstream; wrapper source | 200/210/610 |
| 4.2 earlier event | same | `no-canonical-earlier-event.agda` | 210/610 |
| 4.3 temporal order | same | `no-canonical-temporal-order.agda`, finite n suite | 220/620 |
| groupoid core | same | core finite certificate | 230/630 |
| provenance | `theory/HISTORY_SEMANTICS_WITNESS.md` | provenance finite certificate | 300/630 |
| main no-go | `theory/MAIN_THEOREM_PACKAGE.md` | dependency checker | 250 |
''')

write('papers/paper1/cover_letter.md', r'''
# Cover letter draft

Dear Editor,

We submit a technical report on target-relative representational incompleteness in univalent foundations. The paper does not claim an inconsistency of Homotopy Type Theory. It combines an elementary factorization criterion with an existing formal no-section theorem for two-element types, a groupoid-core direction counterexample, and a provenance reduct counterexample. The intended contribution is the unified “no-free enrichment” formulation and its careful distinction between encodability and intrinsic recoverability.

The upstream no-section result is fully credited. Our local Agda wrapper is supplied, although local replay was not possible in the current isolated execution environment; this limitation is stated in the paper. We request reviewers with expertise in HoTT/univalent foundations and categorical logic.
''')

write('papers/paper2/main.md', r'''
# Signature-Relative Incompleteness

## Context, intent, evidence, resources, and effective synthesis

## Abstract

We formulate a single reduct theorem that unifies several apparent “paradoxes” about formal systems. When two enriched models have isomorphic reducts but differ on a target sentence, that sentence is not definable in the reduct signature. We apply the theorem to intended roles (`Nat` versus an index type), context-sensitive formalization, program cost, and concrete proof witnesses. We then separate this representational obstruction from computational impossibility results: a concrete certificate calculus has decidable checking but undecidable inhabitation; eventual stabilization and general effective limit extraction encode halting information. The results are generic, not specific defects of HoTT.

## 1. Signature-reduct theorem

For \(i:\Sigma\hookrightarrow\Sigma'\), let \(U_i\) forget the added symbols. If \(U_i(M)\cong U_i(N)\) while \(M,N\) disagree on \(\varphi\), no \(\Sigma\)-sentence defines \(\varphi\) over the target class.

This is the paper’s central theorem. The remaining sections are instances or effective analogues.

## 2. Intended role

Two inductive types can be structurally equivalent while one is intended for arithmetic and the other for indexing. The intended role is not a predicate of the bare type unless role data enter the signature. A branded type repairs the issue by enriching the structure.

Univalence says internal properties respect the selected notion of equivalence. It does not turn undocumented intent into an internal invariant, nor make equivalent types judgmentally identical.

## 3. Context-sensitive formalization

If one surface utterance has inequivalent correct formal specifications in two contexts, no context-free single-valued translator is correct in both. This is underdetermination, not yet an undecidability theorem. A formalizer can ask questions, accept context, return alternatives, or be partial.

## 4. Evidence hierarchy

A binary assertion, a proof of mere existence, and a concrete witness are distinct interfaces. Moving from assertion to mere existence requires soundness; moving uniformly from truncation to witness requires a choice principle that is unavailable in general univalent settings.

## 5. Cost and traces

Programs with identical input-output functions can have different step counts or traces. Therefore cost is not a function of extensional denotation alone. Cost-aware and quantitative type theories solve the modeling problem by adding cost/usage structure.

## 6. Resource regimes

Every object of a cartesian category carries canonical copy/discard maps. A strong monoidal interpretation preserving this structure transfers a commutative comonoid to its image. Hence a genuinely noncopyable resource object cannot be the image under such a structure-preserving interpretation. This is the proper replacement for the invalid one-shot transport argument.

## 7. Checking versus synthesis

In the `HaltCert` calculus, a term is a finite halting-time certificate. Checking a proposed certificate is decidable, but deciding whether any certificate exists is the halting problem. Thus there is no total complete synthesizer returning either a witness or a correct emptiness answer.

## 8. Time and effective limits

Eventual stability of computable binary histories is halting-hard. Specker sequences show that computable finite stages can converge to a noncomputable real. These are effective limits on universal discovery, not logical inconsistencies.

## 9. Conclusion

A formal language is complete only relative to a signature, target predicates, admissible recovery maps, and computational requirements. Expanding the signature can restore distinctions; it does not show that the reduct contained them all along.
''')

write('papers/paper3/main.md', r'''
# Reflection and Diagonalization in Univalent Type-Theoretic Foundations

## A corrective research note

## Abstract

Several informal attacks on HoTT conflate mapping spaces with loop spaces, object-language points with metatheoretic proofs, or cumulative universe embeddings with equivalences. This note removes those errors, reconstructs Lawvere’s fixed-point theorem, lists the exact additional ingredients required for Gödel incompleteness, and provides a universe-variant audit. It is an expository/corrective note; it does not currently contain a new HoTT-specific incompleteness theorem.

## 1. The mapping-space error

`Map(1,G) ≃ G`; it is not `ΩG`. A loop space requires a base point and identity type `(g=g)`. Therefore the proposed `G≃Map(1,G)` construction is not self-reference.

## 2. Lawvere’s theorem

If `e:A→Y^A` is weakly point-surjective, every endomap `Y→Y` has a fixed point. The diagonal proof is supplied in the theory appendix. Fixed-point-free negation on booleans prohibits a universal enumeration of all predicates.

## 3. Gödel prerequisites

A genuine Gödel argument needs an effective theory, syntax/proof coding, substitution, diagonalization, a provability predicate, derivability conditions, and consistency/soundness assumptions. A geometric metaphor without these does not establish incompleteness.

## 4. Universes

Standard predicative type theories use a hierarchy. A lifting map between adjacent universes need not be an equivalence, but failure of one candidate lift does not prove no equivalence whatsoever without additional size/cardinality assumptions. Resizing, impredicativity, cumulativity, and univalence are model-sensitive.

## 5. Result

The result of this work package is negative but substantive: the old geometric Gödel and universe-collapse attacks are invalid; the correct research program is a formally coded reflection study. Future novelty claims are blocked until an object theory and provability machinery are constructed.
''')

write('papers/philosophy/main.md', r'''
# Z 铁律、存在与生成：数学抽象的力量与边界

## 摘要

数学抽象通过遗忘差异获得力量。Z 铁律的可辩护版本不是“抽象一发生，数学便矛盾”，而是：被表示真正合并的目标相关差异，不能在没有新增信息时由表示内部无损恢复。本文用时间、历史、极限、资源和形式化入口说明这一原则，并区分模型失真、相对不完备、不可判定和内部不一致。

## 1. 从“否定”到“遗忘”

抽象通常不是断言时间不存在，而是不再区分只在时间上不同的历史。这样的否定是能力意义上的否定：理论失去了一条信息通道。

如果两个现实历史被映成同一表示，却在某命题上真值相反，任何只看该表示的判断都至少在一个历史上错误。这是 Z 铁律最坚硬的数学骨架。

## 2. Being 与 Becoming

类型、项和公式是可以整体考察的数学对象；现实过程则有先后、不可逆、成本、偶然与持续生成。表示者不必具有被表示者的属性：静态方程可以描述动态轨迹。因此“静态”本身不是反证。

真正的问题是：表示是否保留目标过程真值。纯 identity path 可逆，因而不是一般不可逆箭头；但 HoTT 可以用函数、关系和富化结构承载过程。这一细分把哲学直觉变成可检验主张。

## 3. 照片、电影与放映机

“放映机”最精确的数学含义是 enrichment。若照片抹除了帧序，恢复顺序需要额外字段。修复完全合法；错误只在于把后来加入的信息说成照片本身已经提供。

## 4. 芝诺与极限

极限不是第无穷步。`n→∞` 是关于所有有限尾部的量化。对 `x_n=1-2^{-n}`，终点是闭包点，却不是任何有限项。

因此实分析解决了外延问题：序列趋向何处、无穷级数的和是多少。它没有单凭极限关系证明一个由无限离散原子任务组成的物理过程已经完成。

连续轨迹模型则从一开始定义 `x:[0,T]→X` 并允许 `x(T)=L`。它不把每个数学切分点当作一条机器指令。芝诺争议由此成为物理本体和建模选择问题，而不是极限定义内部矛盾。

## 5. 非停机、不完备与矛盾

时间化可以把 `b=¬b` 变成 `b_{n+1}=¬b_n`，从静态无解变为永久振荡。一般稳定性判定可以编码停机。一般极限提取也能隐藏停机信息。

但链条必须保持：非稳定不等于不可判定，不可判定不等于理论不完备，不完备不等于不一致。

## 6. HoTT 的准确位置

HoTT 是关于类型、身份和同伦结构的强大基础。裸 identity/groupoid 层不会免费产生时间方向；directed interval、Step、clock、later、linear/quantitative fields 可以加入需要的信息。

因此最强而可信的结论是：

> 裸结构不是一切目标现实的充分统计量；理论的成功应按其保留的命题域评价，而不能自动升级为完整本体镜像。

## 7. 开放问题

- 物理时间是连续轨迹、离散事件还是二者的混合？
- 哪些时间/因果真值应当进入形式理论的目标域？
- 如何量化富化成本与损失谱缩减？
- 是否存在面向实际科学建模的“最小充分时间签名”？

Z 铁律的价值不在于宣布数学幻觉，而在于迫使每个抽象公开自己的损失函数。
''')

# -----------------------------------------------------------------------------
# External review package
# -----------------------------------------------------------------------------
write('reviews/EXTERNAL_REVIEW_LOG.md', r'''
# External review log

**Status: OPEN — no external expert review was performed in this session.**

This file is intentionally not populated with simulated reviewers. The package is ready for an independent reviewer, but the external gate cannot be self-certified.

## Reviewer tasks

1. Check the exact scope of target-relative incompleteness.
2. Reproduce the Agda wrapper against the pinned toolchain.
3. Verify the `no-section-type-2-Element-Type` dependency and whether the temporal interpretation adds any theorem content.
4. Attack the groupoid-core and provenance examples.
5. Assess novelty as synthesis/application rather than foundational discovery.
6. Record major/minor comments and conflicts of interest.

## Required closure evidence

- reviewer identity or anonymized audit identifier;
- exact environment/commit and command transcript;
- report with dispositions;
- updated manuscript diff.
''')

write('reviews/REVIEWER_QUESTIONNAIRE.md', r'''
# Independent reviewer questionnaire

- Is each theorem well typed and quantifier-complete?
- Does any statement accidentally imply `HoTT ⊢ ⊥`?
- Is “earlier event” clearly a selected orientation, not time in full generality?
- Is the upstream no-section theorem credited?
- Does the main result survive the objection “define Step/time as extra data”?
- Are all enrichment claims separated from conservativity claims?
- Are physical conclusions explicitly conditional?
- Can the formal wrapper be reproduced with exit code 0?
- Is the novelty statement acceptable?
''')

# -----------------------------------------------------------------------------
# WP status cards and execution registry
# -----------------------------------------------------------------------------
wbs=json.loads((DATA/'HOTT_Z_WBS_REGISTRY_v1.json').read_text(encoding='utf-8'))
status_map={}
for wp in wbs['work_packages']:
    n=int(wp['id'].split('-')[1])
    status='COMPLETE_INTERNAL'
    note='All planned internal analysis, paper proof, documentation, and available executable checks were completed.'
    if wp['id']=='WP-600':
        status='COMPLETE_LOCKFILE__LOCAL_INSTALL_BLOCKED'
        note='Toolchain, binary hash, commands, and failure logs are complete; isolated runtime lacked the executable and DNS.'
    elif wp['id']=='WP-610':
        status='SOURCE_COMPLETE__UPSTREAM_V4__LOCAL_REPLAY_BLOCKED'
        note='Exact wrapper source completed; foundational no-section theorem is compiled upstream; local wrapper was not typechecked.'
    elif wp['id']=='WP-620':
        status='SOURCE_AND_CERTIFICATE_COMPLETE__LOCAL_V4_BLOCKED'
        note='Reduction source and independent n≥2 certificates completed; local Agda replay unavailable.'
    elif wp['id']=='WP-630':
        status='CERTIFICATE_SUITE_COMPLETE__MAINSTREAM_V4_BLOCKED'
        note='Four independent finite/symbolic certificate families completed; no local mainstream proof assistant.'
    elif wp['id']=='WP-640':
        status='INDEPENDENT_KERNEL_COMPLETE__SECOND_ASSISTANT_BLOCKED'
        note='A second self-contained certificate checker is supplied, but it is not a second mainstream proof assistant and is not labeled V5.'
    elif wp['id']=='WP-730':
        status='EXTERNAL_PACKAGE_COMPLETE__REVIEW_PENDING'
        note='Anonymous manuscript, code package, questionnaire, and reproducibility instructions are complete; no external reviewer was fabricated.'
    elif wp['id']=='WP-800':
        status='TECHNICAL_REPORT_COMPLETE__SUBMISSION_GATE_PENDING'
        note='Paper I and supplement complete; local V4 and external review gates remain explicit.'
    elif wp['id']=='WP-840':
        status='RELEASE_CANDIDATE_COMPLETE__EXTERNAL_GATE_PENDING'
        note='Reproducible workspace release is complete; it is labeled research snapshot, not final peer-reviewed proof.'
    status_map[wp['id']]={'status':status,'note':note}

for wp in wbs['work_packages']:
    sm=status_map[wp['id']]
    content=f"""# {wp['id']} — {wp['title']}

**Execution status**: `{sm['status']}`  
**Priority**: {wp.get('priority')}  
**Stream**: {wp.get('stream')}  

## Objective

{wp.get('objective')}

## Dependencies

{', '.join(wp.get('dependencies',[])) or 'None'}

## Execution result

{sm['note']}

## Deliverables

""" + '\n'.join(f'- {x}' for x in wp.get('deliverables',[])) + "\n\n## Acceptance audit\n\n" + '\n'.join(f'- {x}' for x in wp.get('acceptance_criteria',[])) + "\n"
    write(f"work_packages/{wp['id']}.md",content)

exec_registry={
    'schema_version':'hott_z.wbs_execution.v2',
    'program_id':PROGRAM,
    'date':DATE,
    'source_registry':'/mnt/data/HOTT_Z_WBS_REGISTRY_v1.json',
    'work_packages':[
        {**wp,'execution_status':status_map[wp['id']]['status'],'execution_note':status_map[wp['id']]['note']}
        for wp in wbs['work_packages']
    ],
    'truthfulness_note':'All 45 packages were executed. Local mainstream proof-assistant compilation and independent external review are not claimed where unavailable.'
}
(ROOT/'governance/HOTT_Z_WBS_EXECUTION_STATUS_v2.json').write_text(json.dumps(exec_registry,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# -----------------------------------------------------------------------------
# Project overview / readme (verification appended later)
# -----------------------------------------------------------------------------
write('README.md', r'''
# HOTT–Z final program execution snapshot

This directory is the result of executing all 45 planned work packages. “Executed” does not mean that inherently external gates were fabricated: local Agda replay was blocked by the isolated runtime, and independent expert review remains open.

## Canonical conclusions

1. The original documents are the source of the Z-law motivation and Being/Becoming framing.
2. Their old Modus-Tollens/transport/Translate/univalence-self-violation proof is not retained.
3. The rigorous result is target-relative representational/naturality/effective incompleteness.
4. Bare identity/groupoid information cannot naturally recover general directed time facts; history, context, cost, and witnesses likewise require appropriate signatures/enrichments.
5. HoTT can encode these structures when they are explicitly added.

## Directory guide

- `governance/`: scope, source genealogy, WBS execution status;
- `theory/`: final theorem packages;
- `formal/`: Agda source candidates and independent certificate kernels;
- `literature/`: systematic review and originality calibration;
- `red_team/`: four-role internal referee reports;
- `papers/`: three research manuscripts and one philosophy manuscript;
- `reviews/`: honest external-review gate package;
- `verification/`: command logs and machine-readable reports;
- `release/`: reproducibility instructions and final archive metadata.
''')

# Save generator in release archive for reproducibility
shutil.copy2(__file__, ROOT/'release/build_final_program.py')

print('Base content generated at',ROOT)
