# 外部追溯审计交接包（2026-09-17；三发 + 第四弹首期 + 收官方案）

> 目的：外部 AI 追溯审计（角色 D，修订片 009/017）的进场文件。本包只列审计对象、
> 复核方法与边界，不代替审计本身。全部对象已本地提交（HEAD 含至
> `dev-notes/0018/0019` 的提交链）；无 push；非 VERSION_CLOSED。

## 1. 审计对象总表（主张—收据—提交对照）

| # | Claim | Proof | Run（exit） | 矩阵行 | 提交 |
|---|---|---|---|---|---|
| 1 | `CAND-F2-7-M2` | `MP-DEDEKIND-OMEGA-M2` | `20260917-…-M2-01`（exit 0，43.9s） | 矩阵 §M2 | `56750b0`+`f3bb849` |
| 2 | `CAND-F2-7-M3` | `MP-DEDEKIND-OMEGA-M3` | `20260917-…-M3-01`（exit 0，55.6s） | 矩阵 §M3 | `eb114f8`+`81ff363` |
| 3 | `CAND-F2-7-BP` | `MP-DEDEKIND-OMEGA-BP` | `20260917-…-BP-01`（exit 0，60.6s） | 矩阵 §BP | `cfaede5` |
| 4 | `CAND-F2-7-M3-UNC` | `MP-DEDEKIND-OMEGA-M3-UNC` | `20260917-…-M3-UNC-01`（exit 0，55.6s） | 矩阵 §M3-UNC | `de0ec91`+`9e3a273` |
| 5 | `CAND-F2-7-TA` | `MP-DEDEKIND-OMEGA-TA` | `20260917-…-TA-01..04`（主模块 exit 0；对照 exit 0；探针×2 exit 1 **预期失败即收据**） | 矩阵 §TA | `9d4b3c5` |
| — | 方案层 | 修订片 022–027（027 = 收官版） + ALIGNMENT-MATRIX-F2 v2 + 三发/M3-UNC/TA 各 CLAIM-PACKAGE | — | 分片校验器仅 2 个既有快照 FAIL | `184aa9b`→`a0edbe9` |
| — | 思想来源链 | GLM 三存档 + dev-notes/0011–0019（Q&A 一字不差） | — | — | `077de25`/`091529a`/`5ab8e2c`/`730d996`/`48d254f`/`0ec215b`/`d860c88`/`80ea527`/`11ed640`/`9eab868` |

前置锚点（早于本包）：M1 = `MP-DEDEKIND-OMEGA-M1`，run `…-M1-04`，commits
`1614c96`+`be0e0c8`；方案链 022/023/024/025（commits `184aa9b`/`dfa6fc4`/`6e87fdb`/`95d17ea`）。

## 2. 复核方法（逐发可重放）

- 每发重放命令见对应 `RUN.json` 的 `command_argv`（M1/M2/M3/M3-UNC/BP 为
  `--ignore-interfaces` 全量复检；TA-01..04 为 dev-loop 形态，见各 RUN.json
  `command_argv` 注记）。工具链身份：`TOOLCHAIN.json` + run `environment.txt` +
  `source-manifest.json`（含源码与依赖 sha256，重算即可比对）。
- 矩阵行与 CLAIM-PACKAGE 逐字对照：命题、量词、假设清单、禁止外推四栏必须
  与源码及 RUN.json scope 一致。
- 失败 run 纪律：M1 的 `-01..-03` 与 TA 的 `-03/-04`（预期失败探针）均须在盘。

## 3. 审计重点（建议优先级）

1. **M3-UNC 的去条件化**：`specA-inhabited-unc` 真的无 LEM 吗（ℚ 序判定是否
   真可构造、`f` 的定义是否暗含经典假设）——它同时修正了「判定表合法性依赖
   LEM」的旧叙事。
2. **TA 演示的边界**：`META_TOOL_CHECKED` 是否被如实标注（探针失败 = 元层工具
   检查记录，不是对象层定理，更不是不一致证明）。
3. **对齐矩阵的预测格**：A–G 类级预测（35 条）全部标注「逐条未核」——复核
   类级预测是否有过度概括。
4. **语义边界全线**：任何收据被读成「HoTT 不一致/被击毁=矛盾」均属误读
   （024 §2 / 025 §6 / 027 §8）。

## 4. 已登记的未闭合项（审计时按此口径）

- 完整 Dedekind cut（金形态）未构造；升格收费的完整实例化未做（027 §5/§9）。
- M4 主定理模式为草案（逐实例元定理，无全量单定理）；靶 A 的「不可归约」内部
  证明未做（路径 (i) 为元层检查记录）。
- 方向追踪/STATE 的 canonical 同步按导弹工作先例留待统一写回窗口（027 §0）。
- push 未授权；非 VERSION_CLOSED。

## 5. 边界

本包自身不是审计结论；`registers_new_claim: false`。审计发现问题请直接引用
RUN.json/矩阵行/commit hash，按 020 片可审计清单推翻或确认。
