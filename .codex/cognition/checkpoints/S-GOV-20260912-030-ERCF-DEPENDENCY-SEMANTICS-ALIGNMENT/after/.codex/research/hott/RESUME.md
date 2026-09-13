# 接续指针

## 每个新 Session/压缩后的固定恢复

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 和本地治理 Skill/PROTOCOL/LOAD_SET/STATE。
2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`；当前为 generation-4/36 KC，manifest/旧 receipt 不能替代。
3. 当前问题先 query `A-HOTT-SELF-VALIDATION-ECONOMY-001`，全文读 `理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md`；需战略背景再读 C3/A11/self-reference/RP-B01。
4. 数学研究使用 research profile，先 query stable record 再显式 task hydrate；结束按当前 manifest 全部 KC 人工回评，并交叉更新 core/direction/panorama 的正确 owner。

## 当前停止点

S030 已把 `A-ERCF-FACTORIZATION-FORMAL-001` 的验证依赖与开放研究母题分开：proof 只依赖已验证的 F-011 Gate，C4/ERCF 父方向保留为 `research_parent`，因此 task plan 不再把已闭合证明误列为 review_required。

S029 已修复 `A-ERCF-FACTORIZATION-FORMAL-001` 的 research task hydration：空 stderr 作为 raw evidence 原样保留在 run，并由 RUN.json/hash/verifier 路由，不再进入要求非空正文的 `full_sources`。

S028 已完成 ERCF-1/2 的通用机器证明：`MP-ERCF-001`/`C-59`–`C-66` 由 Lean 4.33.1 kernel 接受，final run `20260912-MP-ERCF-001-02` 已索引且 exact replay 一致；源码、stdout/stderr、环境与 source manifest 都在 repo。当前未 commit，所以只能称 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

这个结果不是 HoTT 悖论。源码只用普通 `Type` 和 Lean equality；它证明 E₀/因子化 walking skeleton 可表达，并排除把 E₀ 本身当作 HoTT coverage gap。C4 整体仍为 `PAPER_ONLY_WITH_MACHINE_PROVED_GENERAL_FACTORIZATION_CORE`。

下一步不是 ERCF-3，也不是再造一个任意投影：先固定一个原生支持 propositional truncation 或 quotient/HIT 的 HoTT/cubical 系统，机器证明受保护 consumer 正例，再检验一个来自实际用法的 witness/代表元/时序 consumer。若系统正确拒绝，结论是 `DEFENSE_WORKS`；只有合法自然接口与同任务桥梁都闭合，才可能升级为 HoTT 特定候选。
