<!-- governance-shard:v2
logical_id: GODEL_ZFC_CONVERGENCE_SOP
shard_id: 004
index: ../哥德尔式ZFC理论精度收敛闭环SOP.md
-->

# 认知闭包、恢复、写回与Goal启动词

## 1. 认知闭包的唯一入口

本 SOP 的跨 Session 工作记忆由 [GODEL-ZFC-CONVERGENCE-001](../../认知闭包/GODEL-ZFC-CONVERGENCE-001.md) 持有。它不是 proof/source/run 的第二副本，而是当前路线图的最小恢复层：

```text
TaskDescriptor
→ frozen total route set
→ current/parked/blocked RouteUnitRecord pointers
→ paid/unpaid bridge ledger
→ current source and Git snapshot
→ exact next unit / successor / reopen conditions
```

任何一次实际执行都必须在开始时读它，在自然单位结束时更新它。只读本 SOP 的名字、近期聊天、Git commit message 或 `MEMORY` 摘要都不足以恢复当前路线。

## 2. 进入、压缩恢复与 worktree 变更

### 2.1 首次启动或明确 `/goal`

1. 执行全局 `repo-cognitive-closure`，确认当前 repo root、worktree、HEAD、branch/detached 状态、完整 index 和 dirty ownership；
2. 读项目 `AGENTS.md`、`hott-local-session-governance`、`TASK_ROUTING.md`、`最高指示.md`；
3. 读本 SOP index + 001–004，以及 `GODEL-ZFC-CONVERGENCE-001`；
4. 以 `RESEARCH_GENERATION` 角色按四件套顺序全文加载：`核心认知.md → 方向追踪.md → 全景视野.md → 扩展认知.md`，再完成相关 KC 的 source-first 复核；
5. 读当前 `rulings.md`、F-050/F-049/F-048、`MEMORY` 当前队列、R3–R4、T-PRECISION、ZFC-H0 M0–M5 和本轮 route 所需底层 source/proof/run；
6. 检查 closure 的 `active_route`。若无未完成 active unit，按第 002 片选择 `G0-R3-SOURCE-REPLAY-001`；
7. 写本轮 `RouteUnitRecord` 的候选构造与反证条件，才开始新的来源调查或形式化。

### 2.2 压缩、换 Session 或换 worktree 后

不得用“我记得上一轮做到了哪里”。按下列顺序恢复：

1. 将闭包中的 `snapshot` 与实际 `git rev-parse HEAD`、`git status --porcelain=v1 --untracked-files=all` 比较；
2. 若 plan、closure、source hash、Feature/MEMORY owner、current worktree 或上一 unit 的底层 evidence 有变化，则标记受影响 route `STALE`；
3. 重读本 SOP、closure、最高指示与本轮 route 直接依赖；研究角色还重读四件套和相关 source；
4. 回到上一 `RouteUnitRecord` 的 `successor`，而不是从标题、最近文件或最大编号重新选方向；
5. 若这个 successor 依赖外部条件，登记它为 `EXTERNAL_BLOCKED`，并由第 003 片选择 independent READY route；
6. 恢复说明必须公开本轮角色、已读版本／EOF、父结果、active route、未支付桥、上一 scoped verdict 和本轮动作。

## 3. 唯一写回责任

| 事实 | 唯一 owner | 何时更新 |
|---|---|---|
| 用户对“不得中途停下、须持续闭环”的裁定 | `rulings.md` | 本 SOP 创建／裁定变更时 |
| 总路线、状态机、完成条件 | 本 SOP | 方案被证据或用户修正改变时 |
| 当前 active route、最新 unit、paid/unpaid、下一动作、stale/blocked | `GODEL-ZFC-CONVERGENCE-001` | 每个自然单位结束和压缩前 |
| 高层当前队列 | `MEMORY/` | canonical writer 且 file baseline 安全时；否则 closure 记录待写回，不覆盖其他 writer |
| 当前需求与交付状态 | F-050/F-049/F-048 | 需求或验收身份真的改变且 canonical owner 可安全更新时 |
| 数学命题与机器证据 | `HoTT/formal/`、runs、claim matrix、相应 audit | 仅在 source/run/index 全部闭合后 |
| 历史谱系 | 精确 Git commit 与 dev-notes | 每次方案修订、单元结算与对话结束时 |

没有安全 baseline 时，不为让表格“看起来最新”而覆盖 dirty `MEMORY` 或 `feature-list`。记录 `WRITEBACK_DEFERRED_DUE_TO_CONCURRENT_DIRTY_OWNER`，在可安全集成时补写。

## 4. 闭包更新模板

每次自然单位结束，在 closure 的 Route Ledger 原位更新一行，并追加一份紧凑 `UnitRecord`：

```markdown
### GZ-<serial> · <route> · <date>

- **parent gap：**
- **fixed target：**
- **own construction / falsifier：**
- **sources and code actually read：**
- **proof/run or source evidence：**
- **verdict with scope：**
- **does not establish：**
- **successor and changed discriminant：**
- **reopen if：**
- **write-back status / exact commit：**
```

若一个工作单元只做了治理或环境恢复，也必须说明它没有支付哪项数学义务，并给出返回数学主链的下一动作。

## 5. `/goal` 启动词

以下文本是此方案唯一推荐的启动词：

```text
按照SOP=GODEL-ZFC-CONVERGENCE-SOP，恢复认知闭包
GODEL-ZFC-CONVERGENCE-001，并继续执行哥德尔式 ZFC 理论精度收敛闭环。

先核对当前 worktree、Git 状态、用户授权和上一 RouteUnitRecord；完整加载本 SOP、闭包、
R3–R4、T-PRECISION、ZFC-H0 M0–M5 以及当前 route 的直接证据。实际研究前按项目协议
全文加载四件套并完成 source-first 对齐。

每个自然单位必须冻结 target、理论/来源版本、对象/元层、OriginDone/FormalDone、自己的候选构造、
反证条件和正负控制；随后才调查一手论文、开源实现与 proof assistant，并将差分、机器证明或
有界来源结论写入 RouteUnitRecord。局部 source/model/compiler/bridge 缺口只能关闭该 target，
必须生成改变判别面的 successor，或登记可验证的外部阻塞后转向独立 READY 路线。

不得把一般 Gödel 不完备性、宿主 proof assistant、条件 fixture、timeout、来源沉默或项目自定义接口
升级为 bare ZFC 的理论精度结论；不得把一个局部关闭写成总完成。只有本 SOP 第003片 C1–C4
的总完成条件满足，才可结束 /goal。每单位更新闭包与对应 owner，并用精确 Git commit 保留方案和证据谱系。
```

这个启动词不自动获得网络、worker、push、tag、外部写入或清理其它 writer 的权限。

## 6. 方案本身的验收

在宣布本方案“已准备可用”前，检查：

- [ ] `GODEL-ZFC-CONVERGENCE-SOP` 在 `dev-docs/README.md` 和 `TASK_ROUTING.md` 可发现；
- [ ] index、4 个 shard 和 `GODEL-ZFC-CONVERGENCE-001` 路径、标题、链接通过分片验证；
- [ ] R3/R4、T-DIAG、M1–M5 的职责未被复制为第二份当前真值；
- [ ] 每个 local close 都有 successor 或明确 external blocker；
- [ ] 总完成只引用 C1–C4，未偷加“无下一步”作为终止条件；
- [ ] 未来 Session 的恢复顺序不依赖当前聊天；
- [ ] 本方案的准备不被写成 Gödel、HoTT 或 ZFC 的数学结论；
- [ ] exact `/goal` 文本少于 4000 Unicode 字符。
