# universe-ascent-stall 包修订记录

> 本包的 `CLAIM.md` 与 `AscentStallAtSets.agda` 已进入 GLM 运行收据 `20260926-GLM-ASCENT-STALL-01` 的 source-manifest（哈希锁定），`AscentStallAtSets.agda` 另进入 `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01` 与 `20260927-COPUS-HITSCAN-CERT-GLM-01`。按项目规则不改已收据文件；范围修订写在这里。
> 本文件由 Cloud-Opus 审计会话于 2026-09-27 新建（原包没有 REVISIONS.md），依据委托工作单 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §3（R1、R3、R6）与 §6 写入权限。审计全文：`Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` §2.4–2.5、`03-R1-HIT依赖闭包判定.md`、`05-R2至R8处置.md`。

## 2026-09-27：Cloud-Opus 审计修订（审计者写入）

> 编号约定：下文的 C-63、C-75、C-76 沿用 GLM 树的写法，指 Opus CG-001 目标内索引的 `CG001-C-NN`，不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 其它节里同号的 claim。

**形式层不变**【数学事实】：`universeLoopSpaceAtSetIsSet`（GLM-R2-C01）与 `noLevel2AscentAtSets`（GLM-R2-C02）在 Linux 复现中被内核接受（运行 `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01`），读法"对集合 X，Ω¹(U, X) 是集合、Ω²(U, X) 可缩"与形式命题一致，无断裂。

1. **"HIT-free imports only"（源码 L3–5 注释、索引 §9）措辞不准确，结论成立。** 导入闭包含 `Cubical.HITs.PropositionalTruncation*` 模块（经 `Cubical.Data.Sigma.Base` 等库基础设施），所以"只导入无 HIT 模块"不成立；但名称级依赖闭包确实无 HIT：GLM-R2-C01 闭包 189 名、GLM-R2-C02 闭包 190 名，均无 HIT（HITScan 证书 COPUS-R1-C02、COPUS-R1-C03，运行 `20260927-COPUS-HITSCAN-CERT-GLM-01`）。以后引用时写"名称级闭包无 HIT（COPUS-R1-C02/C03）"。

2. **CLAIM "这对 M1 归因意味着什么"第 2 条的"HIT……对全上升必要"撤回。** 该句有两种读法，都不成立：
   - 若"全上升"指**宇宙塔**逐层上升：KS 定理 5.9 已在本仓库对一切 n 机器重放，名称级闭包无 HIT——`KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))`（COPUS-KS-C01，运行 `20260927-COPUS-KS-UNIVERSE-TOWER-01`；HIT 证书 COPUS-R1-C05）。无 HIT 也能逐层上升，所以"必要"被机器证据否定。
   - 若指**单个宇宙 Type₀ 自身**没有 h-level：GLM 的依据只有"无 HIT 的 Type₀ 中无已知非集合成员"，这是知识状态，配不上"必要"。KS §6 的相容性论断（【来源转述】：每个 U_n 中的类型都是 n-截断应当相容；论文自述无已发表证明）支持"无 HIT 时证不出"，但那是来源级判断，不是本仓库机器事实。
   - 修正后的读法：**单个宇宙在集合成员处不再上升（GLM-R2-C02，机器）；单个 Type₀ 的"每层都不停"目前只有带 HIT 的证明（C-75），无 HIT 时应当证不出（来源级）；宇宙塔的逐层上升不需要 HIT（COPUS-KS-C01，机器），但需要大小分层提供上一层宇宙（COPUS-KS-C05：`step : NT L k → NT (ℓ-suc L) (suc k)`）。**

3. **同条"Kraus–Sattler 2015 的层级证法……本仓库未重放（来源）"与源码注释"source only"已过时**：见上条，一般 n 与 KS 定理 5.10（COPUS-KS-C03/C04）均已重放。

4. **CLAIM 第 1 条"第二层及以上的非平凡结构必须由非集合成员供料"**：作为关于**宇宙在 X 处的二阶及以上环路**的命题成立（这正是 GLM-R2-C02 的逆否：Ω²(U, X) 非平凡推出 X 不是集合）。补一句它在两条路线里的样子：C-75 中非集合成员由 HIT 提供（EM 空间）；塔路线中 U_{n+1} 的非集合成员是 `Loop_n`，由低一层宇宙本身造出（需要大小分层，不需要 HIT）。所以"需要非集合成员"不等于"需要 HIT"。

5. **"熄火"读法的桥**（R6）：`localGlobal : Ω^(2+n)(U, X) ≃ Π (x : X), Ω^(1+n)(X, x)` 的名称级闭包 201 名，无 HIT（COPUS-R6-C01，运行 `20260927-COPUS-HITSCAN-CERT-OPUS-01`）。因此"引擎在集合成员处熄火"= 无 HIT 的形式部分（C02）+ 无 HIT 的桥 + 解释层用词（"引擎""熄火"）。

6. **CLAIM 第 3 条"P-HIT 从竞争病因降为更高层的燃料供给方式，P-U 仍是每层的发动机"**：标【解释】（比喻）。机器证据支持的精确归因见 `Cloud-Opus审计并补完GLM/07-悖论卷宗-最终完整版（D4）.md` §4：单价性是两条路线共用的桥（把成员内部的相同提升到宇宙）；对"单个论域元素每层都不停"，P-HIT 是共同必要条件（来源级），不只是"燃料"；无 HIT 时由 P-S 顶上，但结论的主语换成宇宙塔。

7. **查重段"C-63 导入仅 Prelude/Univalence/Bool/Nullary——本来就是无 HIT 的"**：结论成立，理由不准确（C-63 的导入闭包同样含 PropositionalTruncation 模块）；名称级闭包 101 名、无 HIT，证书 COPUS-R1-C04（运行 `20260927-COPUS-HITSCAN-CERT-OPUS-01`）。

8. **收据**：GLM 原收据不改。它的 `source-manifest.json` 不是 canonical schema（`sources` 映射、无 `bytes`、无外部依赖行），canonical 形式的 Linux 复现见 `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01`，由 `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py --rerun` 逐字节重放核验（结果：`Cloud-Opus审计并补完GLM/11-收据核验结果.json`）。
