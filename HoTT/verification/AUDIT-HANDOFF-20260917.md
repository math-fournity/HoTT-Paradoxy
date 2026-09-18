# 外部追溯审计交接包（2026-09-17 建立；2026-09-18 更新：金形态四条件完整版入库）

> 目的：外部 AI 追溯审计（角色 D，修订片 009/017）的进场文件。本包只列审计对象、
> 复核方法与边界，不代替审计本身。全部对象已本地提交（HEAD = `7cc94c1`，
> 含至 `dev-notes/0023` 的提交链）；无 push；非 VERSION_CLOSED。
> 2026-09-18 更新（一）：金形态（Book §11.2 四条件）已**完整过核**并作为审计对象 #6 入表；
> §4 未闭合项相应修正（ℚ 层已闭合，剩余 = ℝ 层升格）。
> 2026-09-18 更新（二·四弹全面审计）：AC 格 stuckness 收据（TA-AC-01/02，`9be3cbe`）
> 此前**未在矩阵登记**，现已补登记为对象 #7；LEM 格演示此前仅有源码声明无收据，现已
> 补齐两个负向探针（TA-LEM-01/02，对象 #8，**重放逐位一致**）。同行评审工作 map 已备：
> `HoTT/verification/FOUR-MISSILES-AUDIT-MAP.md`（按序加载即可独立审计）。

## 1. 审计对象总表（主张—收据—提交对照）

| # | Claim | Proof | Run（exit） | 矩阵行 | 提交 |
|---|---|---|---|---|---|
| 1 | `CAND-F2-7-M2` | `MP-DEDEKIND-OMEGA-M2` | `20260917-…-M2-01`（exit 0，43.9s） | 矩阵 §M2 | `56750b0`+`f3bb849` |
| 2 | `CAND-F2-7-M3` | `MP-DEDEKIND-OMEGA-M3` | `20260917-…-M3-01`（exit 0，55.6s） | 矩阵 §M3 | `eb114f8`+`81ff363` |
| 3 | `CAND-F2-7-BP` | `MP-DEDEKIND-OMEGA-BP` | `20260917-…-BP-01`（exit 0，60.6s） | 矩阵 §BP | `cfaede5` |
| 4 | `CAND-F2-7-M3-UNC` | `MP-DEDEKIND-OMEGA-M3-UNC` | `20260917-…-M3-UNC-01`（exit 0，55.6s） | 矩阵 §M3-UNC | `de0ec91`+`9e3a273` |
| 5 | `CAND-F2-7-TA` | `MP-DEDEKIND-OMEGA-TA` | `20260917-…-TA-01..04`（主模块 exit 0；对照 exit 0；探针×2 exit 1 **预期失败即收据**） | 矩阵 §TA | `9d4b3c5` |
| 6 | `CAND-F2-7-GOLD-FULL` | `MP-DEDEKIND-OMEGA-GOLD`（金形态 cut·四条件完整版） | `20260918-…-GOLD-02`（`--ignore-interfaces` 全量 clean 重放，exit 0，stderr 0，73.2s） | 矩阵 §GOLD（四条件完整版节） | `4bc020d`+`f2fd012`+`8285ea2` |
| 7 | `CAND-F2-7-TA-AC` | `MP-DEDEKIND-OMEGA-TA-AC`（AC 格 stuckness，**本轮补登记**） | `20260917-…-TA-AC-01/02`（探针×2，exit 字段记 1，**预期失败即收据**：`ch 0 .fst != zero` / `!= 1`） | 矩阵 §TA-AC（本轮补建） | `9be3cbe` |
| 8 | `CAND-F2-7-TA-LEM` | `MP-DEDEKIND-OMEGA-TA-LEM`（LEM 格 stuckness，**本轮新增补齐**） | `20260918-…-TA-LEM-01/02`（探针×2，exit 42，**预期失败即收据**：`n-lem | LEM ℕ != zero` / `!= 1`；重放逐位一致） | 矩阵 §TA-LEM（本轮新建） | 本轮提交 |
| — | 方案层 | 修订片 022–027（027 = 收官版） + ALIGNMENT-MATRIX-F2 v2 + 各 CLAIM-PACKAGE（含 `CLAIM-PACKAGE-GOLD.md` 四条件完整版） | — | 分片校验器仅 2 个既有快照 FAIL（`CHECKPOINT_AFTER_SHARDS_NOT_COPIED`，`f0cfb2f` 已登记） | `184aa9b`→`a0edbe9` |
| — | 思想来源链 | GLM 三存档 + dev-notes/0011–0023（Q&A 一字不差） | — | — | `077de25`…`5c868b6` |

前置锚点（早于本包）：M1 = `MP-DEDEKIND-OMEGA-M1`，run `…-M1-04`，commits
`1614c96`+`be0e0c8`；方案链 022/023/024/025（commits `184aa9b`/`dfa6fc4`/`6e87fdb`/`95d17ea`）。
金形态分阶段历史收据：`20260917-…-GOLD-01`（第一装配期，`615fbd2`，矩阵保留为
历史登记节，已被 §6 完整版节取代——历史节内的「未装配」表述按时间点理解，不作当前真值）。

## 2. 复核方法（逐发可重放）

- 每发重放命令见对应 `RUN.json` 的 `command_argv`（M1/M2/M3/M3-UNC/BP/GOLD-02 为
  `--ignore-interfaces` 全量复检；TA-01..04 为 dev-loop 形态，见各 RUN.json
  `command_argv` 注记）。工具链身份：`TOOLCHAIN.json` + run `environment.txt` +
  `source-manifest.json`（含源码与依赖 sha256，重算即可比对）。
- 金形态等价入口：`sh HoTT/formal/dedekind-omega-missile/compile.sh CutGoldForm.agda --ignore-interfaces`
  （仓库根执行）。当前工作树 `CutGoldForm.agda` / `CutInfra.agda` 的 sha256 已核与
  GOLD-02 的 `source-manifest.json` 一致（`81b7b139…` / `7caf7f97…`）。
- 矩阵行与 CLAIM-PACKAGE 逐字对照：命题、量词、假设清单、禁止外推四栏必须
  与源码及 RUN.json scope 一致。
- 失败 run 纪律：M1 的 `-01..-03` 与 TA 的 `-03/-04`（预期失败探针）均须在盘。
- **负向探针退出码注（2026-09-18 审计发现）**：当前机器按 `command_argv` 重放
  TA-AC-01/TA-03 等负向探针，stdout/stderr 与收据**逐位一致**（如 TA-AC-01：
  431B，sha256 `f7b37d65…`），但退出码观察为 **42** 而收据 `exit_code` 字段记 **1**。
  内核拒绝证据（UnequalTerms + 中性卡住范式）完全可复现，差异仅在退出码整数字段
  （记录偏差，非证据偏差）；本轮新增的 TA-LEM-01/02 按实际观察记录 exit 42 并已
  现场验证三匹配（exit/stdout/stderr）。历史收据不予改写，在此如实登记。
- **收据 schema 注**：导弹链 16 个 run 的 `RUN.json` 均无 canonical 验证器
  `scripts/audit/verify_formal_proof_run.py` 要求的 `index` 快照字段（该字段由
  `mark_proof_run_indexed.py` 在矩阵登记后盖戳，但该脚本绑定 `C-\d+` 旧编号体系与
  `PROOF_VERSION_CLOSURE.json`，不适用于 `CAND-F2-7-*` 导弹链）。因此导弹链收据
  目前**不能**通过 `--rerun` 级 canonical 校验；替代核验路径 = 手工按
  `command_argv` 重放 + `source-manifest.json` 哈希比对 + 矩阵行逐字对照
  （FOUR-MISSILES-AUDIT-MAP §重放清单已逐条给出）。

## 3. 审计重点（建议优先级）

1. **金形态四条件完整版（对象 #6，当前最高价值）**：这是本链路第一个**完整**的机器
   对象。复核点：(a) Book §11.2 四条件的 7/7 方向是否真的全部在 `CutGoldForm.agda`
   内、无 postulate / 无追加假设；(b) 勘误版谓词 `U q := (0r<q)×(2r<q·q)` 的正性合取
   是否确为必要（反例 q=−2，plan-revise `0150b29`）；(c) `rounded←` 的 δ 见证是否
   确为**内在 ℚ 项**（不依赖代表元选择）；(d) 边界四条（单个 cut、非完备性、
   非 HoTT 矛盾、非元定理）是否与源码 scope 一致。
2. **M3-UNC 的去条件化**：`specA-inhabited-unc` 真的无 LEM 吗（ℚ 序判定是否
   真可构造、`f` 的定义是否暗含经典假设）——它同时修正了「判定表合法性依赖
   LEM」的旧叙事。
3. **TA 演示的边界**：`META_TOOL_CHECKED` 是否被如实标注（探针失败 = 元层工具
   检查记录，不是对象层定理，更不是不一致证明）。
4. **对齐矩阵的预测格**：A–G 类级预测（35 条）全部标注「逐条未核」——复核
   类级预测是否有过度概括。
5. **语义边界全线**：任何收据被读成「HoTT 不一致/被击毁=矛盾」均属误读
   （024 §2 / 025 §6 / 027 §8 / 矩阵 GOLD 节禁止外推 (b)）。

## 4. 已登记的未闭合项（审计时按此口径；2026-09-18 修正）

- ~~完整 Dedekind cut（金形态）未构造~~ → **已修正**：金形态 ℚ 层四条件
  （inhabited×2 / disjoint / rounded 双向 / located）**已完整过核**（对象 #6）。
  剩余缺口**精确定位**：把 cut 取等价类、把「ℝ 取值命题」塌缩到单一 Ω 的
  **ℝ 层升格未机械化**——DESIGN §4 登记的 LEM/propositional-resizing 收费位置
  仍为**登记**而非机器证据（不声称「升格必需 LEM」已证）。
- δ 路线完备性未论证：不声称内在 ℚ 项见证形态已被穷尽（金形态有界负收尾的
  前置完备性论证未做）。
- M4 主定理模式为草案（逐实例元定理，无全量单定理）；靶 A 的「不可归约」内部
  证明未做（路径 (i) 为元层检查记录）。
- STATE checkpoint 机械层未触碰：`STATE.revision` 仍为 169，S170–S175 的 Session
  证据（SESSION/RUNS/分片审计集）落盘但未经 canonical checkpoint 事务应用
  （0022 禁止事项，沿 170–174 模式，收据缺口如实登记，不伪造事务）；
  全景视野/方向追踪为 checkpoint 管理文档，写回随该事务挂起。
- 导弹链收据的 canonical schema 缺口（见 §2 收据 schema 注）：`index` 快照字段缺失，
  `verify_formal_proof_run.py --rerun` 不可用；升级需先打通 `CAND-*` 编号体系与
  `PROOF_VERSION_CLOSURE.json` 的映射（未做，登记为工程债）。
- 负向探针收据 `exit_code` 字段记录偏差（见 §2 退出码注）：证据可复现，字段待统一。
- push 未授权；非 VERSION_CLOSED。

## 5. 边界

本包自身不是审计结论；`registers_new_claim: false`。审计发现问题请直接引用
RUN.json/矩阵行/commit hash，按 020 片可审计清单推翻或确认。
