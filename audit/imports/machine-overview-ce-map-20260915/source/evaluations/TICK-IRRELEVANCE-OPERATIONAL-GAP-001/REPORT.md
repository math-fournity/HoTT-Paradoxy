# Tick irrelevance 与当前归约：CCTT 的内外层操作观察边界

状态：`NATIVE_REPLAYED / REPRESENTATION_BOUNDARY / HOTT_BUG_NOT_ESTABLISHED / LOCAL_UNCOMMITTED`

判词：

```text
EXTENSIONAL_TICK_IRRELEVANCE_WITH_METALEVEL_OPERATIONAL_SPLIT
NATURAL_USAGE_MISMATCH_NOT_FOUND_IN_FROZEN_SET
```

## 1. 结论先行

本工作单元关闭了上一轮留下的最大工具链未知，并找到了一个比“guard 不能随意擦除”更精确的 HoTT-adjacent 自观察现象：

> CCTT 在**操作层**必须区分 forcing tick `◇` 与 ordinary tick，因为只有前者使 guarded fixed point 在当前检查步骤判断展开；但在**外延层**，`tirr` / `force-delay` 又为不同 tick application 构造 Path。若把“现在是否发生归约”内化为一个尊重该 Path 的 `Tick → Bool` 观察者，就会得到 `true ≡ false`。

这一内外层张力是真实的，不再只由论文文字支持：本轮构建了论文配套的 Agda `forcing-ticks` branch，并原生运行了 `◇`、ordinary tick、`pfix'` 与 `force-delay` 的正负对照。

它仍然不是 HoTT BUG。实际系统通过三项安排阻止冲突：

1. ticks 不形成普通对象层类型，而属于特殊的 lock/tick 语法；
2. checker 在 Haskell 元层用 `Tick` / `ForcingTick` 与 `FTDia` 分支决定归约；
3. `pfix`、`tirr` 与 `force-delay` 提供的是 Path，未被当作 judgemental equality。

因此当前结果是一个具体的**自观察表示边界**：理论内部可以沿 Path 推理结果，却不能把自己元层 reducer 的“此刻是否展开”无条件当作 Path-invariant 数据。固定源码中的真实消费者都保留了这条边界。

## 2. 冻结身份

- evaluation：`TICK-IRRELEVANCE-OPERATIONAL-GAP-001`
- scope：`SCOPE.json`
- freeze：`FREEZE.json`
- freeze SHA-256：`df0cb0b1edb10b9ad18e18be4368733627cef0d0dea36b282ebe98c52d3e55f2`
- decisions：`DECISIONS.json`
- run：`runs/20260913-TICK-IRRELEVANCE-OPERATIONAL-GAP-001/RUN.json`
- deterministic SHA-256：`cf622133e8aa1260c1bfa68f475308c259caece65ce06529efb5cb6b8451a6a5`
- source systems：3
- pinned artifacts：18
- pinned source trees：4
- G1–G8 + consumer anchors：54，全部命中
- native probes：9，全部命中冻结预期，首次与内部 replay 字节一致，独立 `--rerun` 再次一致

Freeze 在 `DECISIONS.json`、8 个最终 probe source、正式 run、报告、测试和 Session 不存在时产生。它固定了来源、G1–G8、自然消费者 Gate、交叉签名、等式搜索文法、9 个 probe 的目的与预期类别。设计者仍是同一个 AI，所以它只提供先后与防改题证据，不是 blind evaluation 或原创性证明。

## 3. 固定理论与真正被比较的观察量

本轮固定：

| 层 | 固定对象 |
|---|---|
| 理论说明 | CCTT / *Greatest HITs*，arXiv:2102.01969v3 |
| reference library | `agda/guarded` forcing-ticks，commit `cf0c438214cb10874ac1a7650f8d0d69677db57e` |
| checker source | `agda/agda` forcing-ticks，commit `5bec849bec6c7aa40e068db99c5a1f5eab47a874` |
| native checker | 本轮从该 commit 构建的 Linux arm64 `Agda 2.6.3` |
| Cubical control | Agda 2.8.0-3d04bac + Cubical v0.9 |

观察问题不是“两个 term 最后是否 Path-equal”，而是：

```text
当前 type-checking/reduction 步骤中，
这个 tick application 是否使 dfix judgementally unfold？
```

冻结答案为：

```text
observe(◇)        = true
observe(ordinary) = false
```

这是 exact checker reduction relation 的操作观察，不是物理秒数、运动连续性或宇宙时间本体。

## 4. 配套 checker 已从源码构建并实际运行

上一轮只能让标准 Agda 2.8.0 对 forcing-ticks 源给出 expected version mismatch。本轮通过隔离 Docker 构建关闭了该缺口：

- source commit：`5bec849…`
- source Git tree：`97fabad0b01ea385b5c810fdfb1d6c640bff9031`
- GHC：9.0.2
- Cabal：3.4.1.0
- build：`-O0`，404/404 library modules + executable link
- binary：161,708,104 bytes
- binary SHA-256：`31a5ea292d2aa9a58df49eafc5f08ded25bddbac6ce81f45caf4d2f065a6212f`
- Docker image：`sha256:48ccd2705f82149c5a34de520ee19c08ed1f0134f99588171eb72e798e3b591b`
- run network：`none`

构建输入用 `cabal.project.freeze` 和 `plan.json` 固定，正式 build 在 dependency freeze 后以 `--offline` 完成。完整路径、哈希、依赖版本、8 次 build attempt 与信任边界在外置缓存的 `BUILD-RECEIPT.json`，并由 `SCOPE.json` 固定。

构建过程的失败没有被抹掉：

1. 误选 amd64 base，主动终止；
2. 过早设置不存在的 `TMPDIR`，`ca-certificates` 失败；
3. 旧 Cabal 内建 transport 不支持 HTTPS；
4. 旧 Cabal 无法满足 2026 Hackage TUF root 的签名阈值；
5. `v2-freeze` 错带 target 参数；
6. `-O1` 在 440 MB bitcode 上运行 LLVM 超过 25 分钟，因优化与证明任务无关而中止；
7. `-O0` 404/404 和 link 完成后，`list-bin` 调用语法使最后复制失败；
8. 直接从唯一 linked executable 复制，版本检查和 fresh-container `Clocked.Primitives` smoke 均 exit 0。

Hackage 获取的诚实边界也保留：旧客户端无法验证当前 TUF root 后，使用 HTTPS/curl + `secure=False` 取得索引，再固定 index/freeze/plan 与本地字节哈希；这不是发布方签名认证。它不影响 exact Git source commit 的身份，但限制“依赖来源认证”的最强说法。

## 5. 真正的 CCTT 操作差异

checker 源码不是只看名字。`LockKind` 明确区分：

```haskell
data LockKind = Tick
              | ForcingTick
```

`primForcingAppDep` 的 reducer 又明确分支：

```text
FTEmb ...  → ordinary application
FTDia ...  → advanceCase ... True
```

而 fixed-point 特例只有 `True` 才展开：

```text
reducePFix False ... = no reduction
reducePFix True  ... = pfix beta/unfolding
```

这组三处源码同时被完整 414-file checker tree inventory 与 literal anchors 锁定。

原生 `P05` 使用同一个常值 algebra：

```agda
zeroAlg : ∀ {k} → ▹ k Nat → Nat
zeroAlg _ = zero

family : ∀ k → ▹ k Nat
family k = dfix {k = k} zeroAlg

diamond-unfolds : force family k0 ≡ zero
diamond-unfolds = refl
```

checker 接受 `refl`，说明经 forcing application at `◇` 后，左端确实在 judgemental reduction 中成为 `zero`。

## 6. Ordinary tick 有 Path，但没有同样的 judgemental unfolding

同一个 `zeroAlg` 在 ordinary tick 下，`pfix'` 给出：

```agda
ordinary-unfolds-by-path
  : ∀ {k} → ▸ k \ α → dfix {k = k} zeroAlg α ≡ zero
ordinary-unfolds-by-path α = pfix' zeroAlg α
```

`P06` exit 0。但把右侧改成 `refl` 的 `P07` exit 42，诊断保留未展开的：

```text
lineFix zeroAlg Agda.Primitive.Cubical.i0 ...
```

因此这里不是“一个证明写法更方便”。相同 endpoint proposition 有 Path witness，却没有 judgemental computation witness。

`force-delay` 给出更直接的同对象对照：

```agda
force-delay
  : (f : ∀ k → ▹ k (A k))
  → ∀ k → ▸ k \ α
  → force f k ≡ f k α
```

其定义沿 `ftirr ◇ (emb α)` 走一条 Path。`P08` 用 exact library theorem exit 0；`P09` 对同一 `family` 把它换成 `refl`，exit 42，诊断为：

```text
zero != lineFix zeroAlg ...
```

这条正负对照是本轮的中心证据：

```text
Path equality available
≠
same current judgemental reduction available
```

## 7. 内部 operational observer 的条件坍缩

为检查“把 reducer 自身的判断放回对象层”会发生什么，本轮在安全 Cubical Agda 中固定 HIT：

```agda
data ExtTick : Type₀ where
  forcing ordinary : ExtTick
  tirr : forcing ≡ ordinary
```

若存在：

```text
observe forcing  = true
observe ordinary = false
```

那么 congruence 沿 `tirr` 给出 `observe forcing ≡ observe ordinary`，于是：

```agda
noOperationalObserver
  : (observe : ExtTick → Bool)
  → observe forcing ≡ true
  → observe ordinary ≡ false
  → ⊥
```

`P01` 被 Agda 2.8.0/Cubical v0.9 接受。该文件同时有两个正控制：

- HIT 上的 constant observer 可以定义；
- 去掉 `tirr`、保留两个 operation constructors 后，区分它们的 Bool observer 可以定义。

`P02` 还尝试直接写：

```agda
isForcing forcing = true
isForcing ordinary = false
```

内核以 `[CoverageIssue]` 拒绝，因为缺失 `isForcing (tirr i)`；这不是依赖上面反证证明脚本的同义测试。`P03` 则确认已有 `tirr` 也不使 `forcing ≡ ordinary` 可由 `refl` 完成，内核以 `[UnequalTerms]` 拒绝。

这些都是 `machine-overview` 的 conditional exploration，不是 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 中的新数学 claim。它们支持的是模型对应：为什么 CCTT 不把 tick form 暴露为普通对象层 discriminator。

## 8. 机器搜索与交叉签名

### 8.1 源码交叉签名

机器在冻结的四棵树中寻找六项必要信号：

| 信号 | 实际值 | 最小值 | 结果 |
|---|---:|---:|---|
| `force-delay` | 2 | 2 | PASS |
| `tick-irr/ftirr/tirr` | 6 | 6 | PASS |
| diamond-only source comment | 1 | 1 | PASS |
| checker `LockKind/ForcingTick` | 15 | 15 | PASS |
| checker `FTDia → ... True` | 1 | 1 | PASS |
| checker `reducePFix False/True` | 2 | 2 | PASS |

这使 candidate 的最初发现不依赖报告作者先写好结论：只有 Path 侧与 reducer 侧同时出现才产生交叉签名。签名只发现位置，不裁定误用。

### 8.2 冻结等式文法的完整搜索

搜索图只有四个 Bool 项与三项输入：

```text
FORCING-OBSERVATION     : observe(forcing) = true
TICK-PATH-CONGRUENCE    : observe(forcing) = observe(ordinary)
ORDINARY-OBSERVATION    : observe(ordinary) = false
```

允许 symmetry 与最多三次 equality composition。完整搜索检查 6 条定向边，找到唯一最小见证：

```text
sym FORCING-OBSERVATION
; TICK-PATH-CONGRUENCE
; ORDINARY-OBSERVATION
```

即 `true ≡ false`。反向枚举顺序得到相同见证集；分别删除三项输入中的任何一项，目标路径数均变成 0。

这只证明冻结小文法内的完整性。它没有证明 CCTT 真的含有那个 `observe`；相反，源码和负控制显示实际系统把它留在元层。

## 9. 九项原生探针

| ID | 检查 | 结果 | 含义 |
|---|---|---|---|
| P01 | internal observer collision + controls | exit 0 | conditional collapse 可由 native Cubical 检查 |
| P02 | 直接定义 path-respecting discriminator | exit 42 `[CoverageIssue]` | HIT eliminator 要求处理 tick Path |
| P03 | 把 Path constructor 当 `refl` | exit 42 `[UnequalTerms]` | Path 不升级为判断相等 |
| P04 | exact `Clocked.Primitives` | exit 0 | forcing-ticks branch 工具链真正可用 |
| P05 | `◇` 下 `dfix` unfolding 用 `refl` | exit 0 | diamond 当前归约成立 |
| P06 | ordinary tick 用 `pfix'` | exit 0 | ordinary endpoint 有 Path |
| P07 | ordinary tick 改用 `refl` | exit 42 | ordinary 当前归约不成立 |
| P08 | exact `force-delay` Path | exit 0 | forcing result 与 ordinary application Path-equal |
| P09 | `force-delay` 改用 `refl` | exit 42 | Path 不能当作同一步判断展开 |

9/9 首次与 evaluator 内 replay 的 exit/stdout/stderr 字节一致；独立 `verify --rerun` 再次对 9/9 得到相同字节。

## 10. 真实消费者审计

固定 source set 中最接近越界的四个点是：

| consumer | 分类 | 为什么没有越界 |
|---|---|---|
| `force-delay` definition | `PATH_ONLY` | 构造 interval-indexed Path，不声称 `refl` |
| `Clocked.Lift.fwd` | `NO_PROMOTION` | 显式构造 `λ k → λ α → ...` 全时钟族，并以 `subst` 使用 `pfix'` |
| checker diamond branch | `JUDGEMENTAL_COMPUTATION` | 本身就是 meta reducer；不是由 Path 推出 |
| checker ordinary branch | `NO_PROMOTION` | `FTEmb` 走普通应用，`reducePFix False` 不展开 |

完整六文件 library tree 中，`force-delay` 只在定义处出现，没有 downstream caller。`Clocked.Lift` 的真实消费者使用 `force` 和 `pfix'`，但支付了全时钟与 Path transport 两项责任。414-file checker tree 则明确把 operation decision 保留在 meta syntax。

因此自然消费者 Gate 的六项条件没有同时满足，`natural_usage_mismatches=[]`。这是固定集合中的 bounded negative，不是对所有 CCTT 应用或全部学术文献的不存在定理。

## 11. 理论经济账本

| 项 | 本轮定位 |
|---|---|
| 理论收入 | guarded fixed point、coinductive encoding、不同 tick application 的统一外延推理 |
| 被悬置因子 | reducer 对 forcing/ordinary tick form 的操作区分 |
| 预先保留的支付装置 | `Tick`/`FTick` 特殊 sort、clock abstraction、residual context、`FTDia` meta branch |
| Path 支付装置 | `pfix`、`tirr`、`force-delay` 只承诺内部 Path |
| 复活问题 | “这个 term 现在是否 judgementally unfold？” |
| 同阶段状态 | forcing yes；ordinary no |
| 同层状态 | meta checker 可观察；普通 object function 不可无条件观察 |
| 删除支付装置的后果 | internal Bool observer 与 tick Path 联合得到 `true ≡ false` |
| 现有判词 | `REPRESENTATION_BOUNDARY`，无 natural promotion |

这正对应用户所说的“理论为了经济性拿掉或转移现实因素，到了非平凡问题它又回来”。这里回来的是**当前归约资格**：外延 reasoning 可以忘掉 tick identity；自我观察 reducer 时，这个 identity 重新成为决定因素。

## 12. “时间”与“时序”的位置

本轮属于时间问题中的**时序／阶段可用性**：tick 被论文解释为 time has passed 的证据，ordinary/forcing 区分决定某项计算此刻能否展开。

它不处理芝诺问题中的时间、时空与运动结构：没有连续/非连续、稠密性、无限可分或物理运动模型。因此它不能取代 L3 运动结构线，也不能支持量子时空判断。

这一限制不是弱化结果，而是使它可定位：本轮精确回答“Path equality 为什么不等于现在已经算出”，而没有把所有时间问题收窄为先后关系。

## 13. 与核心认知和既有工作关系

本结果把四条此前分开的线接到一个真实规则点：

1. `KC-000011`–`KC-000013`：理论思考过程的时序与 ASK；
2. `KC-000015` / `KC-000018` / `KC-000029`：抽象、否定现实前提与理论经济；
3. `KC-000025`–`KC-000028` / `KC-000036`：理论对自己的计算/验证活动能否同层观察；
4. 前一 bridge 的 GCTT/CCTT guard-erasure 与 L5 host reflection 分层。

它也纠正上一轮报告的一项环境边界：forcing-ticks binary 不再是 unavailable。现在的边界是**已构建、已运行、但 local Docker/external-cache scoped**。

一般“Path 不等于 judgemental equality”和“内部函数必须尊重 Path”都是已知核心，本轮不声称原创。新增的是项目内的具体对应闭合：exact CCTT paper → exact guarded library → exact historical checker branch → native `◇`/ordinary/force-delay probes → complete fixed-tree consumer classification。

原创性身份：

```text
KNOWN_INTENSIONAL_EXTENSIONAL_CORE_WITH_NEW_PROJECT_OPERATIONAL_CORRESPONDENCE
```

## 14. 为什么仍不是 HoTT BUG

若实际理论包含一个 ordinary object function：

```text
isForcing : Tick → Bool
```

同时接受 forcing/ordinary 的 Path 与两端不同结果，那么 conditional collapse 会成为内部问题。但固定 CCTT 恰好不作这组联合承诺：ticks 不是普通 type，operation observation 在 meta reducer，Path 只用于内部外延推理。

所以本轮显示的是：

```text
theory can reason extensionally about results
while its checker retains intensional operational knowledge
that is not freely reflectable as an internal invariant
```

这是理论的自我透明度边界和分层代价。它可以成为用户数学哲学下的一个精彩“悖论形状”，却还没有现实应用或理论 consumer 越过边界，因此不能写成 `NATURAL_USAGE_MISMATCH`，更不能写成内部不一致。

## 15. 下一最小可验动作

下一工作单元应为 `REFLECTED-TICK-REDUCTION-OBSERVER-001`：

1. 在已经可运行的 exact forcing-ticks checker 中固定 Agda Reflection 的 `reduce`/`normalise`/quotation 能力；
2. 让 host `TC` 分别观察 `◇` 与 ordinary tick 下的同一个 `dfix` application；
3. 检查宏是否能把这个 meta observation reify 成对象层 Bool 或 proof；
4. 再沿 `pfix`/`force-delay` Path 要求 congruence；
5. 记录是 host/object fence 正确拒绝、显式 syntax refinement 正常工作，还是出现一条真实的 Path→operation promotion。

这一步把本轮的操作观察与上一轮的 `HOST_TC` 角色真正接起来。如果只能对 quotation/syntax 工作，就登记为细化表示的正控制；如果能对 path-identified object value 产生不同的可替换对象结果，才出现足以进入 `NATURAL_USAGE_MISMATCH`、甚至 checker soundness 调查的候选。

## 16. 证据边界

- 本报告未新增 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 行；所有数学形状保持 `NATIVE_CHECKED_CONDITIONAL_EXPLORATION`。
- `Clocked.Primitives` 自身声明 postulate/primitive builtins；编译通过不单独证明 CCTT 一致性。
- checker build 是 local Linux arm64 Docker artifact，未 commit/push/export；scope 缺少该 external cache 或 image 时应 fail closed。
- `-O0` 只改变 compiler binary 的性能优化，不改变 pinned source reduction rules；本轮不比较性能。
- full `Clocked.Lift` 尚未用历史匹配的 Cubical library 原生重放；本轮对它的 consumer 判词是 source-inspected。
- paper 明说未证明 canonicity；本轮 probes 只覆盖声明的 narrow slice。
- 没有物理时间或现实应用证据。
- 当前全部 repo 资产仍在独立 worktree，未 commit、merge、tag 或 push。
