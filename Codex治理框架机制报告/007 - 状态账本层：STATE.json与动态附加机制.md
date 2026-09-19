# 状态账本层：STATE.json 与动态附加机制

## 1. `.codex/research/hott/STATE.json`（840KB / ≈223,524 tokens；always_full_boot + dynamic_state）

**作用**：机器记录账本+当前指针。结构：`records`（322 条：session/result/
formal_mathematical_result/t3_pulse/audit…各带 lifecycle_status、evidence_status、
path、depends_on、source_hashes）、`active`（5 条当前任务资格）、`latest_session`、
`current_core`（generation 身份）、`review_due/unresolved/structural_tension`、
`revision`。HEAD.json.tracked 对全部可变文件保存 hash 做漂移检测。

**目的**：让"存在哪些记录、各自什么状态、依赖什么证据"成为**可机器校验**的事实
（hash 对账、stale 传播），支撑投影生成、任务资格判定、水合展开。它防的失败：
(a) F4 历史冒充当前——靠 lifecycle 轴；(b) 证据腐烂无人知——靠 source_hashes
stale 检测；(c) 依赖混淆——靠 depends_on/research_parent/related_records 三分。

**原理**：三个关键设计。

1. **双状态轴**（lifecycle vs evidence）：一条记录可以"生命周期活着但证据待复核"
   或反之。这是 F4 防御的核心机关：`historical_session_auto_load=false` +
   `evidence_status_grants_load_eligibility=false`——历史会话不因待复核自动复活。
   没有这个分离，"证据状态"会被迫承担"任务资格"职责，导致要么历史全量复活
   （爆炸）要么误删（失忆）。
2. **依赖语义三分**：`depends_on`（验证依赖，递归水合+stale 传播）≠
   `research_parent`（谱系，不水合）≠ `related_records`（叙事，不水合）。
   这是 ruling §16 修复的产物（S086–88 审计发现叙事性 depends_on 污染任务
   上下文，task plan 曾达 3.68–29.42MB；拆分后降到 0.84–0.93MB——feature-list
   F-012 记录了这场框架最成功的减容战役）。**原理：上下文里只放验证所需，
   谱系留给导航**。
3. **HEAD.tracked+fail-closed**：任何被跟踪文件与 HEAD 哈希不符 → `plan` 直接
   BLOCKED（姊妹报告 P1 亲测触发）。原理：状态一致性是全部下游（投影/资格/
   水合）的前提，宁可不跑不可带病跑。

**为什么它成了最贵的文件**（姊妹报告根因一）：它被放在 always_full_boot——
"每会话全文"。但细读其数据构成会发现，全文必读买到的**指针价值**
（active 5 条+latest+current_core+revision，约几千字符）只占文件 0.x%；
97.5% 是 records 账本，其中 1/3 是历史 session 档案。**双状态轴已经把
"历史不复活"做对了，但复活闸门挡的是任务资格，挡不住字节过境**——
机制设计止步于语义层，没有对应的容量层配套（记录退休/归档通道）。
对比核心认知：同为保真账本，core 有 generation 退休机制所以 12K 稳定；
STATE 没有退休机制所以 5 天 113 倍。这不是原则错误，是**机制只建了一半**。

## 2. 动态附加：latest session SESSION.md + active 记录路径（graph() 动态组装）

**作用**：graph() 在固定清单之外，自动追加最新会话的 SESSION.md（≈1.2–2.4K
tokens）和 active 记录指向的文档（当前：方向追踪/全景视野[与四件套去重]、
goal.md、R4 任务记录、PREMISE-001 修订片）。

**目的**：**增量续接**——让新会话拿到"上一轮结束时的精确停止点与当前活跃
任务"，而不必读全部历史会话。这是框架中唯一贯彻"只给增量"的地方，
与 `historical_session_auto_load=false` 构成一对：全部历史不可见是失忆，
全部历史可见是爆炸，latest+active 是中间的正确解。

**原理**：latest-session 单条 + lifecycle 资格过滤 active 集。它证明框架完全
**知道怎么做按需加载**——这个模式（指针常驻、内容按 ID 水合）正是 STATE
本身应该采用的形态：active[] 就是"热状态"的雏形，只是 records 账本没有被
对称地移出常驻层。

## 3. 与 STATE 配套的两件执行机制（顺带定位）

- **checkpoint 事务**（runtime checkpoint --apply）：原子写 SESSION+RUNS+审计集，
  before/after 全量副本，result.json 唯一收据。目的：防状态损坏/并发写/伪造收据
  （ruling §16 的教训：S086–88 缺收据且禁止追溯伪造）。原理：事务+fail-closed+
  乐观锁。代价：磁盘乘法（139×2.9M=187M）与过重事务被绕过（P2）。
- **hydration_diagnostics**（plan 输出）：document_count/total_bytes/largest/
  query_first_promoted。目的：让"这个任务要装配多少上下文"在动手前可见，
  防"review_required=[] 就宣称可接手"。原理：自暴露预算——框架给自己装的
  油表。它是姊妹报告所有测量的先声：框架已经会报告自己的成本，只是没有人
  据此行动。

## 三问总结

作用=机器真值账本+当前指针+增量续接；目的=让记录状态、依赖、漂移可机械校验，
防历史复活、证据腐烂、上下文污染；原理=双状态轴+依赖三分+hash 锚定+
latest/active 增量模式。机制设计的前半（语义防伪）精良且被实战检验
（F-012 减容 97%），后半（容量退休）缺失，使它成为框架理念与体量冲突的
爆心。
