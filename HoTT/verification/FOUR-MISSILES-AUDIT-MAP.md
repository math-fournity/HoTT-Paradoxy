# 四弹连发·同行评审工作 map（数学真理性与机器证明完备性审计）

> 身份：外部/同行 AI 追溯审计（角色 D，修订片 009/017 的用户闸门）的**进场路线图**。
> 本文档不是审计结论，也不替代任何证据；`registers_new_claim:false`。
> 目标：任何同行 AI **按本文档顺序完整加载**之后，即可独立对四弹连发的全部细节
> 做数学真理性与机器证明完备性审计。建立日期 2026-09-18；HEAD `7cc94c1`；
> 未 push、未 tag；工作树唯一脏文件 `dev-notes/0010`（永不触碰）。
> 配套进场文件：`HoTT/verification/AUDIT-HANDOFF-20260917.md`（审计对象总表）。

## 0. 一句话总览与四弹身份

四弹连发 = 用 Cubical Agda 内核（Agda 2.8.0-3d04bac + cubical v0.9）对「圆环悖论
非现实性」命题链做的一组**机器可核验**构造，落在 `HoTT/formal/dedekind-omega-missile/`。
逻辑主线（修订片 022–027）：过程层不可完成（M1）→ 交付类型空（M2）→ 任务识别层
拒绝（M3 / M3-UNC）→ 元层完成义务落差（第四弹：靶 A canonicity 演示 + 靶 B 对齐
矩阵 + 金形态 Dedekind cut 四条件）。**全程不声称 HoTT 不一致**；每张收据都带
禁止外推栏。

| 弹 | proof_id | claim | 一句话命题 | run（exit） | 矩阵节 |
|---|---|---|---|---|---|
| 一 | `MP-DEDEKIND-OMEGA-M1` | `CAND-F2-7-M1` | Pell 夹钳判别式 `D n = p²-2q²` 恒交替 ±1，夹钳两端在 ℚ 上永不相遇 | `…-M1-04`（0；`-01..-03` = InfectiveImport 失败历史，保留） | §M1 |
| 二 | `MP-DEDEKIND-OMEGA-M2` | `CAND-F2-7-M2` | `√2-irrational : ∀ q:ℚ → ¬(q·q ≡ 2r)`；交付类型 Spec_B 无居住者 | `…-M2-01`（0，43.9s） | §M2 |
| 三 | `MP-DEDEKIND-OMEGA-M3` | `CAND-F2-7-M3` | LEM 显式假设下 Spec_A 居住 + `¬(Spec_A ≃ Spec_B)` | `…-M3-01`（0，55.6s） | §M3 |
| 三·去条件 | `MP-DEDEKIND-OMEGA-M3-UNC` | `CAND-F2-7-M3-UNC` | 无 LEM 无 resizing 下 `specA-inhabited-unc` + 识别拒绝 | `…-M3-UNC-01`（0，55.6s） | §M3-UNC |
| 廉价副产品 | `MP-DEDEKIND-OMEGA-BP` | `CAND-F2-7-BP` | `decGapAt` 逐点判定 + `noGapWitness` Σ 居住性否定 | `…-BP-01`（0，60.6s） | §BP |
| 四·靶 A | `MP-DEDEKIND-OMEGA-TA` | `CAND-F2-7-TA` | UA-作公理注入下闭项 canonicity 破坏（元层演示） | `…-TA-01..04`（0/0/预期失败/预期失败） | §TA |
| 四·靶 A·AC | `MP-DEDEKIND-OMEGA-TA-AC` | `CAND-F2-7-TA-AC` | AC 选择函数公理注入下 `n-ac` 卡住（**本轮补登记**） | `…-TA-AC-01/02`（预期失败即收据） | §TA-AC |
| 四·靶 A·LEM | `MP-DEDEKIND-OMEGA-TA-LEM` | `CAND-F2-7-TA-LEM` | LEM 公理注入下 `n-lem` 卡住（**本轮新增补齐**） | `…-TA-LEM-01/02`（exit 42 预期失败，重放逐位一致） | §TA-LEM |
| 四·金形态 | `MP-DEDEKIND-OMEGA-GOLD` | `CAND-F2-7-GOLD` / `CAND-F2-7-GOLD-FULL` | Book §11.2 四条件 7/7（√2 的 ℚ 层 cut） | `…-GOLD-01`（部分装配期历史）/ `…-GOLD-02`（0，73.2s，全量 clean 重放） | §GOLD（两节） |

## 1. 按序加载清单（缺一不可；顺序即审计前置条件）

**第 0 层·项目认知（先建闭包，再碰任何证据）**
1. `AGENTS.md`（项目宪法）、`README.md` + `README/` 分片、`MEMORY.md` + `MEMORY/` 分片、
   `feature-list.md`、`rulings.md`。
2. 认知四件套**全文**（固定顺序，不得重排或摘要替代）：
   `核心认知.md` → `方向追踪.md` → `全景视野.md` → `扩展认知.md`。
   均为 v2 分片索引：先读索引完整 table + `last_shard` + `append_target`，再按 table
   顺序读全部分片。`核心认知.md` 为唯一单文件（generation-7 / 46 KC，从 STATE 取身份）。
3. `.codex/research/hott/STATE.json`（仅按字段提取，820KB 勿整体读）、
   `RESUME.md`（停止点 173 之后继续）、`.codex/cognition/LOAD_SET.json`、
   `PROTOCOL.md`、`SKILL_ROLES.json`。

**第 1 层·治理与方案链**
4. `.codex/skills/hott-local-session-governance/SKILL.md`（本地治理入口）、
   `hott-paradox-search-sop/SKILL.md`（七段执行循环）、
   `.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`
   （系统化完备性意识：搜索张量、omission scan、coverage 判据）。
5. 修订片链 `Atria的方案/修订片/001..027`，四弹相关 = **022 → 023 → 024 → 025 →
   026 → 027**（027 = 收官版：§1 两类承载系统、§2 身份与主定理模式、§3 三靶、
   §4 证明论落位与拒证二元性、§5 债务定位、§9 未闭合项、§10 不声称的）。
6. `Atria的方案/修订片.md`（修订片总索引，先读 table 再定位分片）。

**第 2 层·主张与证据索引**
7. `HoTT/CLAIM_EVIDENCE_MATRIX.md`（**唯一主张—证据索引**，816 行；含 §追加登记节
   M3-UNC / TA / TA-AC / TA-LEM / GOLD×2）。判词等级语义见本文档 §6。
8. `HoTT/verification/AUDIT-HANDOFF-20260917.md`（审计对象总表 + 复核方法 + 未闭合项口径）。

**第 3 层·每发的精确契约（CLAIM-PACKAGE，逐字）**
9. `HoTT/formal/dedekind-omega-missile/CLAIM-PACKAGE.md`（M1）、
   `CLAIM-PACKAGE-M2.md`、`CLAIM-PACKAGE-M3.md`、`CLAIM-PACKAGE-M3-UNC.md`、
   `CLAIM-PACKAGE-GOLD.md`（四条件完整版）。每包固定：精确命题、量词、假设清单、
   禁止外推、重放命令、工具链身份。

**第 4 层·run 收据（五件套：RUN.json / stdout.txt / stderr.txt / environment.txt /
source-manifest.json）**
10. `HoTT/verification/runs/` 下 18 个导弹相关目录（见 §3 重放清单）。先读 `RUN.json`
    的 `scope` / `non_goals` / `status` / `exit_code`，再核对 `source-manifest.json`
    的源码与依赖 sha256。

**第 5 层·源码与工具链**
11. `HoTT/formal/dedekind-omega-missile/` 全部 `.agda`（14 个主源 + 探针）+
    `compile.sh`（canonical 编译脚手架）+ `TOOLCHAIN.json` + `AGDA_LIBRARIES` +
    `CutGoldForm-DESIGN.md`（含 U 谓词勘误，plan-revise `0150b29`）+
    `CanonicityCounterexample-DESIGN.md` + `ALIGNMENT-MATRIX-F2.md`（靶 B：F2 缺口层
    7 条 + A–G 35/35 逐条审计）+ `README.md`。
12. 工具链本体：`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda`
    （sha256 `ac285c19…`）+ cubical v0.9 树（tree sha256 `73ccfbaf…`，
    tag commit `b150186d`）。

**第 6 层·思想来源与历史（语义边界锚点）**
13. `GLM/` 三存档（第四弹思想来源之一/二/三，一字不差）+ `dev-notes/0011..0023`。
14. Git 链：`git log --oneline d905453..HEAD`（四弹全链提交，含每次 plan-revise 与
    reflection 提交）。

## 2. 逐发命题—判据表（数学真理性审计入口）

每行给出：精确命题（机器检查形态）／量词与假设／禁止外推／**反证条件**（什么证据可推翻）。

### M1（第一枚·过程层不可完成）
- 命题：`pell-gap-never-closes : (n : ℕ) → (D n ≡ 1r) ⊎ (D n ≡ -1r)`，
  `gap-never-zero : (n : ℕ) → ¬ (D n ≡ pos 0)`，其中 `p'/q'` 互递推 `p'=p+2q, q'=p+q`，
  初值 (1,1)，`D n = p_n² - 2q_n²`。
- 假设：纯 Cubical Agda，`--safe --cubical --guardedness`，无 LEM / 无 resizing /
  无追加公理。环恒等式由 `Cubical.Tactics.CommRingSolver` 的 `solve! ℤCommRing` 反射求解。
- 禁止外推：不声称 HoTT 矛盾；不声称 `∀ q:ℚ, q·q≠2`（那是 M2）；不声称「实数完备性
  非现实」可交付；命题是 ℤ 层环计算，不依赖 UA / path / HIT。
- 反证条件：给出某个 `n` 使 `D n ≡ pos 0` 可构造（或递推/初值被证与 Book §11.2 夹钳
  不同构），则 M1 倒。

### M2（第二枚·交付类型空）
- 命题：`√2-irrational : ∀ q : ℚ → ¬ (q ·ℚ q ≡ 2r)` 与
  `spec-B-empty : ¬ (Σ q : ℚ, q ·ℚ q ≡ 2r)`。
- 假设：同 M1 纯度；证明路径 = ℚ set quotient 提取（`rec2` 点构造子定义性归约 +
  `eq/⁻¹` + `Int.abs`）→ ℕ 无穷下降（奇偶工具包 + 平方膨胀 + 偶平方引理 + 手写强归纳）。
- 禁止外推：不声称「任何过程不停机」的元语言命题（证的是类型无居住者；
  「任何策略不可能交付」为语义读法，按 `ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS` 交付）。
- 反证条件：给出 `q : ℚ` 与 `q·ℚq ≡ 2r` 的构造，则 M2 倒（同时也直接威胁 M3/M3-UNC/
  GOLD 的 eq 支——located 支消费 `√2-irrational`）。

### M3 / M3-UNC（第三枚·任务识别层拒绝）
- 命题（条件版）：`specA-inhabited : LEMᵒ → Spec_A`（`LEMᵒ = (A:Type₀)→isProp A→A⊎(A→⊥)`
  为**显式假设**）；`M3-L1 : LEMᵒ → ¬ (Spec_A ≃ Spec_B)`。
  命题（去条件版）：`specA-inhabited-unc : Spec_A`（无条件，ℚ 序可构造判定 `_≟_`
  直接定义 `f`）+ `M3-L1-unc : ¬ (Spec_A ≃ Spec_B)`。
- 假设：M3 带 LEMᵒ；M3-UNC **无 LEM、无 resizing、无任何追加假设**（027 §5 待核发现
  被核实为真）。M3-UNC 复用 M3 的类型与 M2 的 `spec-B-empty`（source-manifest 固定
  M2 源码哈希 = 消费依赖）。
- 禁止外推：不声称 Spec_A 无条件居住的「实数层」版本（判定表在 ℚ 层免费，理想元素
  本体升格才收费）；不声称「A=B 内部可证」——M3-L1 恰证明其在 J=规格等价判据下被核
  否定；逼选「两支都命中」是论证锚定，非单一机器定理。
- 反证条件：给出 `Spec_A ≃ Spec_B` 的构造（则与 `spec-B-empty` 矛盾，整链倒）；
  或证明 `specA-inhabited-unc` 的 `f` 定义暗含经典假设（则 027 §5 去条件化判定倒）。

### BP（廉价副产品）
- 命题：`decGapAt : (n:ℕ) → (D n ≡ pos 0) ⊎ ¬ (D n ≡ pos 0)`；
  `noGapWitness : ¬ (Σ n:ℕ, D n ≡ pos 0)`（消费 M1 的 D / gap-never-zero）。
- 判据意义：机械确认「判定已完成 ≠ 搜索不终止」的区分（025 片 §5 更正的根据）。
- 反证条件：给出 `Σ n, D n ≡ pos 0` 的成员（与 M1 的 `gap-never-zero` 同源倒）。

### TA / TA-AC / TA-LEM（第四弹靶 A·元层 canonicity 演示）
- 命题（TA）：UA-作公理（postulate，无计算规则）注入下，闭 ℕ 项
  `n = if subst (λX→X) (ua not not not-not not-not) true then 0 else 1` 的范式为
  中性卡住形态；内核对 `n ≡ zero` / `n ≡ suc zero` 的 refl 均判不可互换
  （TA-03/04 错误消息含完整卡住范式 `if transp (λ i → e i) i0 true then zero else 1`）。
- 命题（TA-AC）：`ch : (n:ℕ)→Σ[k∈ℕ] P n k` 公理注入下 `n-ac = ch 0 .fst` 卡住
  （`ch 0 .fst != zero` / `!= 1`）。
- 命题（TA-LEM）：`LEM : (A:Set)→A⊎(A→⊥)` 公理注入下 `n-lem`（with 分支归约）卡住
  （`n-lem | MissileFourChargeDemo.LEM ℕ != zero` / `!= 1`）。
- 身份纪律：`META_NEGATIVE_CHECK_AS_EXPECTED` / `META_TOOL_CHECKED`——**元层工具检查
  记录，不是对象层 `¬ (n ≡ zero)` 的证明**（027 §4 拒证二元性：不可归约性是元层性质，
  本 repo 只记录内核拒绝 refl 这一事实）。刻意无 `--safe` 的 postulate 注入是演示内容
  本身，非工程疏忽。
- 禁止外推：不声称 HoTT 不一致（非规范 ≠ 矛盾，027 §8）；不声称覆盖全部 canonicity
  破坏形态（Huber 完整结果仍 `SOURCE_REPORTED_NOT_REPLAYED`）。
- 反证条件：若有人给出 TA-03/04 中 n 的 `zero` 或 `suc zero` 范式归约（或证明该闭项
  在 UA-作公理下确有典范范式），则该演示失效；TA-AC/TA-LEM 同理。

### GOLD / GOLD-FULL（金形态·Book §11.2 四条件）
- 命题：`(1)` `·-mono-≤-nn : (k a b : ℚ) → 0r ≤ k → a ≤ b → k·ℚa ≤ k·ℚb` 与
  `·-mono-<-nn : 0r < k → a < b → k·ℚa < k·ℚb`（补库无 ℚ 乘法单调性引理的缺口；
  路线 = elimProp3 + 代表元 ℤ 链 + `≤-·o`）；
  `(2)` 勘误版谓词 `L q := (q<0r) ⊎ ((0r≤q) × (q·ℚq<2r))`、
  `U q := (0r<q) × (2r<q·ℚq)` 均为 hProp；
  `(3)` 四条件 7/7：inhabitedL / inhabitedU / disjoint（`L q → U r → q < r`）/
  roundedL→ / roundedU→ / **roundedL← / roundedU←**（δ := t·¼r 内在路线，U 侧
  `q := r - (r·r-2r)·¼r`，witness 不依赖代表元选择）/ located（`q<r → L q ⊎ U r`，
  eq 支消费 `√2-irrational`）。
- 假设：`--safe --cubical --guardedness --two-level`，**无 LEM、无 resizing、无任何
  追加假设**；`--ignore-interfaces` 全量 clean 重放。
- 禁止外推（四条边界）：(a) 这是 **ℚ 层单个 cut（√2）**，不声称「实数完备性」/
  「ℝ 不可达」或任何 ℝ 层命题——取等价类、塌缩「ℝ 取值命题」到单一 Ω 的升格仍需
  LEM 或 propositional resizing（DESIGN §4 登记的收费位置，**未机械化**）；
  (b) 不声称 HoTT/立方类型论矛盾；(c) `rounded←` witness 是 ℚ 层显式 δ 项；
  (d) `registers_new_claim:false`——ℚ 层标准可构造计算，非 HoTT 元定理。
- 反证条件：给出某条件的反例（如 `L q ∧ U r` 但 `r ≤ q`；或 `L q` 但不存在更大
  `p ∈ L`），则 GOLD-FULL 倒；U 谓词若去掉 `0r<q` 合取会立即在 q=−2 处破坏 disjoint
  （plan-revise `0150b29` 的勘误正因此）。

## 3. 重放清单（机器证明完备性审计入口）

canonical argv 形态（自包含环境；`--ignore-interfaces` 保证输出不依赖接口缓存）：

```
/usr/bin/env XDG_DATA_HOME=/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-data \
  XDG_CONFIG_HOME=/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-config \
  TMPDIR=/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/tmp \
  /Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda --ignore-interfaces \
  --library-file=/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/dedekind-omega-missile/AGDA_LIBRARIES \
  -l cubical-0.9 -i /Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/dedekind-omega-missile \
  HoTT/formal/dedekind-omega-missile/<Module>.agda
```

等价入口（金形态）：`sh HoTT/formal/dedekind-omega-missile/compile.sh CutGoldForm.agda --ignore-interfaces`
（仓库根执行；已验证当前 HEAD clean 重放 exit 0 / stderr 0 / stdout sha256 与 GOLD-02
收据逐位一致 `671549d5…`）。

逐 run 重放预期（模块 → run → 预期 exit → 备注）：

| 模块 | run | 预期 exit | 备注 |
|---|---|---|---|
| `MissileOneProcessLayer.agda` | M1-04 | 0 | `-01..-03` exit 42（InfectiveImport，被 Gate 用过的失败历史，保留不删） |
| `MissileTwoUniversalIrrationality.agda` | M2-01 | 0 | 43.9s |
| `MissileThreeVerdictCollision.agda` | M3-01 | 0 | 55.6s；LEM 显式假设 |
| `MissileThreeUnconditional.agda` | M3-UNC-01 | 0 | 55.6s；无 LEM |
| `MissileByproductGapDecidable.agda` | BP-01 | 0 | 60.6s |
| `CutGoldForm.agda` | GOLD-01 / GOLD-02 | 0 / 0 | GOLD-02 = 全量 clean 重放；01 = 部分装配期历史 |
| `MissileFourTargetA-UACounterexample.agda` | TA-01 | 0 | 主模块（含 postulate UA） |
| `MissileFourTargetA-ProbeControl.agda` | TA-02 | 0 | 对照组 |
| `MissileFourTargetA-ProbeZero.agda` | TA-03 | 预期失败 | 记录值 1；当前机器重放 42（见 §5 退出码注） |
| `MissileFourTargetA-ProbeSucZero.agda` | TA-04 | 预期失败 | 同上 |
| `MissileFourTargetA-ProbeACZero.agda` | TA-AC-01 | 预期失败 | 记录值 1；stdout 逐位可复现 |
| `MissileFourTargetA-ProbeACSuc.agda` | TA-AC-02 | 预期失败 | 同上 |
| `MissileFourTargetA-ProbeLEMZero.agda` | TA-LEM-01 | 42 | **本轮新增**；已双重重放验证三匹配 |
| `MissileFourTargetA-ProbeLEMSuc.agda` | TA-LEM-02 | 42 | 同上 |

重放后核对三件事：(a) exit 与 `RUN.json.exit_code`；(b) stdout/stderr 与收据文件
逐位一致（sha256 在 RUN.json 内）；(c) 源码 sha256 与 `source-manifest.json` 一致
（注意：若干源码在 run 之后合法演进过，如 S089 修复、脚本升级、M1 入库——以当前
HEAD 的源码哈希为准重算比对，历史 manifest 记录的是当时哈希）。

## 4. 交叉引用矩阵（方案 × 主张 × 证据 × 提交）

| 方案文档 | 关键矩阵行 | run | commit | CLAIM-PACKAGE |
|---|---|---|---|---|
| 022（圆环悖论非现实性定位） | — | — | `184aa9b` | — |
| 023（两枚导弹·反弹机制） | — | — | `dfa6fc4` | — |
| 024（执行击落·交付纪律） | `CAND-F2-7-M1` | M1-04 | `1614c96`+`be0e0c8` / `6e87fdb` | `CLAIM-PACKAGE.md` |
| 025（第三枚·ASK 与 LEM 判据搬运） | `CAND-F2-7-M2` / `-M3` | M2-01 / M3-01 | `56750b0`+`f3bb849` / `eb114f8`+`81ff363` / `95d17ea` | M2 / M3 |
| 026（三枚齐射记录） | `CAND-F2-7-BP` | BP-01 | `cfaede5` | — |
| 027（第四弹收官版） | `CAND-F2-7-M3-UNC` / `-TA` / `-TA-AC` / `-TA-LEM` / `-GOLD` / `-GOLD-FULL` | M3-UNC-01 / TA-01..04 / TA-AC-01/02 / TA-LEM-01/02 / GOLD-01/02 | `de0ec91`+`9e3a273` / `9d4b3c5` / `9be3cbe` / 本轮提交 / `615fbd2`+`4bc020d`+`f2fd012`+`8285ea2` | M3-UNC / GOLD（四条件完整版） |
| `ALIGNMENT-MATRIX-F2.md`（靶 B） | A–G 35/35 逐条 | — | `9be3cbe`（F2-4 格升级） | — |

027 §2.3 的主定理模式是**逐实例元定理**（不存在单条覆盖定理）：判据 = 已声明实例
是否都有收据。当前已声明实例 = M1 / M2 / M3 / M3-UNC / BP / TA / TA-AC / TA-LEM /
GOLD-FULL，全部有 run 收据（GOLD-01 保留为部分装配期历史，被 GOLD-02 取代）。


> **修复验收**：本节缺口与 `REMEDIATION-CHECKLIST-20260918.md`（公开评审前修复·审计 Checklist）逐项对应；该表给出每项的验证命令、状态与证据指针，是修复完成度的验收仪器，本 map 是四弹既有状态的进场文件。
## 5. 已知缺口明细（审计时按此口径；2026-09-18 四弹全面审计结果）

**已在本轮修复**
1. **TA-AC 矩阵登记缺失**：收据（`9be3cbe`）的 `index_status` 声称
   `INDEXED_IN_CLAIM_EVIDENCE_MATRIX` 但矩阵无行 → 已补建 `CAND-F2-7-TA-AC` 节。
2. **LEM 格演示无收据**：`MissileFourChargeDemo.agda` 声明 n-lem / n-ac 双演示，
   仅 AC 格有探针收据 → 已补 TA-LEM-01/02（canonical argv、双重重放验证）。
3. **027 §9/§10 过时表述**：「canonicity 反例本轮未跑核」→ 已拆分为「三类公理注入
   stuckness 已跑核（TA / TA-AC / TA-LEM）」+「Huber 完整结果仍
   `SOURCE_REPORTED_NOT_REPLAYED`」；§10 相应修正为「不声称其为**对象层**定理」。

**仍登记的缺口（不声称已闭合）**
4. **负向探针 exit_code 字段偏差**：当前机器重放 TA-03/04、TA-AC-01/02，stdout/stderr
   与收据**逐位一致**（TA-AC-01：431B，sha256 `f7b37d65…`），但退出码观察为 **42**
   而收据字段记 **1**。内核拒绝证据完全可复现，差异仅在退出码整数字段（记录偏差）；
   历史收据不予改写。**审计建议**：以 stdout/stderr 的内核拒绝消息为证据本位，
   exit_code 仅作参考。（新 TA-LEM 收据按实际观察记录 42。）
5. **收据 canonical schema 缺口**：导弹链 18 个 run 的 `RUN.json` 均缺
   `verify_formal_proof_run.py` 要求的 `index` 快照字段（该字段由
   `mark_proof_run_indexed.py` 盖戳，但该脚本绑定 `C-\\d+` 旧编号与
   `PROOF_VERSION_CLOSURE.json`，不适用于 `CAND-F2-7-*` 链）。故 `--rerun` 级
   canonical 校验不可用；替代核验 = §3 手工重放 + manifest 哈希 + 矩阵行逐字对照。
6. **状态字面过时**：多数早期收据行/`git_status` 仍标 `LOCAL_UNCOMMITTED` /
   `MACHINE_PROVED_LOCAL_UNCOMMITTED`，而证据实际已入库（HEAD `7cc94c1` 工作树仅
   `dev-notes/0010` 脏）。这是状态字面更新，非数学缺口；真实当前态 =
   `LOCAL_COMMITTED_NOT_PUSHED`（未 push，非 VERSION_CLOSED）。
7. **3 个 `MP-LEGACY-*` 行**（`MP-LEGACY-ZCORE` / `-NO-CANONICAL-POINT` /
   `-TWO-EVENT`）：门禁前的聚合收据，状态如实标为
   `LEGACY_AGGREGATE_RECEIPT_REPLAY_REQUIRED_FOR_NEW_DELIVERY`（其中一个已被
   pinned 重放取代）。非虚假声明，但**不得**当作当前机器证明。
8. **ℝ 层升格未机械化**：把 cut 取等价类、塌缩「ℝ 取值命题」到单一 Ω 的
   LEM / propositional-resizing 收费位置**仅登记**（DESIGN §4 / 027 §9），不声称
   其必需性已证。
9. **δ 路线完备性未论证**：不声称内在 ℚ 项见证形态已被穷尽（金形态有界负收尾的
   前置完备性论证未做）。
10. **靶 A「不可归约」内部证明未做**：路径 (i) 为元层检查记录（027 §4）。
11. **STATE checkpoint 机械层未触碰**：`STATE.revision` 仍 169；S170–S176 的 Session
    证据落盘但未经 canonical checkpoint 事务应用（0022 禁止事项，沿 170–175 模式，
    收据缺口如实登记，不伪造事务）；全景视野/方向追踪为 checkpoint 管理文档，写回
    随该事务挂起。
12. **Huber 结果**：`SOURCE_REPORTED_NOT_REPLAYED`（论文级外部结果，不升级）。
13. **push 未授权；非 VERSION_CLOSED**。

## 6. 判词等级语义（裁决时按此解读）

- `MACHINE_PROVED` / `KERNEL_ACCEPTED_WITH_SCOPE`：内核接受，且范围 = 命题本身；
  **不**把解释性外推一并升级。
- `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED`：已入库未 push，非 VERSION_CLOSED
  （跨机器可恢复性未证）。
- `META_TOOL_CHECKED` / `META_NEGATIVE_CHECK_AS_EXPECTED`：**元层工具检查记录**，
  不是对象层定理；负向探针 = 「refl 被核拒绝」这一事实的存档，加上内核亲自打印的
  中性卡住范式。**不可**读作 `¬ (t ≡ zero)` 的对象层证明，更不可读作不一致证明。
- `SOURCE_REPORTED_NOT_REPLAYED`：外部论文/来源陈述，本 repo 仅转述，未重放。
- `LEGACY_AGGREGATE_RECEIPT_*`：门禁前聚合收据，重交付时必须产生新 run package。
- `PENDING_KERNEL` / 草案：无机器证据，仅方案。

推翻/确认的举证要求（020 片可审计清单）：任何结论变更必须直接引用 RUN.json /
矩阵行 / commit hash / 源码行号；不得以「文档说」「旧 Session 记得」「LLM 一致」
为据。

## 7. /tmp 收录核查（用户第三问）

已全量核查 75 个正式 run 的 `RUN.json` + `source-manifest.json` 的 `command_argv`：
**零 `/tmp/` 引用**；75 个 manifest 声明的源码文件 **0 缺失**；15 个哈希不匹配 =
run 后文件合法演进（S089 修复、脚本升级、M1 入库），非代码遗失。`/tmp` 下 84 个
脚本均为一次性脚手架（草稿、daemon、浏览器杂项）；唯一值得复核的
`/tmp/TwoLevelReplacementUIP.agda`（4446B 草稿）已由正式版
`HoTT/formal/two-level-fibrant-replacement-uip/TwoLevelReplacementUIP.agda`
（7227B，sha 与 manifest 一致）取代。**结论：无重要代码滞留 /tmp。**
本轮新增的 TA-LEM 收据亦全部落在 `HoTT/verification/runs/`（canonical 路径）。

## 8. 边界

本文档是审计路线图，不是审计结论；`registers_new_claim:false`。四弹是 ℚ 层/元层
工程验收，不声称 HoTT 不一致、不声称 ℝ 完备性已证、不声称 LEM-resizing 收费位置
已机械化、不声称 δ 路线完备、不声称第四弹已全量机械化（027 §6 的「四弹一体收官
判定」= 学说 + 首实例核收据）。前提判定全部
`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`——**外部追溯审计是用户闸门，本文档为其
进场文件之一**。
