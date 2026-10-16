# Z0-D3 补充包二 · 全量源码 + 缺口骨架（2026-10-11）

**这份包补的是"上一份包不够"的地方。** 它不重复讲背景：目标、缺口、可用引理、
已判死的路线都在 `../../Z0-D3-攻关包-最小完整版/`，先读那一份，再读这一份。

## 上一份包缺了什么

外部复核 AI 在沙箱里对 `Z0-D3-攻关包-最小完整版` 做了独立通读，反馈（逐字保留在
`01-先读这个/外部复核反馈-原文.md`）里三条可核实的缺口：

1. **Foundation 只给了 27 个模块，闭包要 167 个。** 它无法读 `Proof/Typed.lean`、
   `CraigTrick.lean`、`R0/Basic.lean` 等决定性的文件，只能"对着看不见的 API 写证明"。
2. **`source-manifest.json` 没进包**（只有它的哈希），所以它核不了"三个不动文件
   是否与收据钉死的哈希一致"。
3. **没有可编译环境**，连"编译 24 个模块确认环境通"都做不了。

## 这份包装了什么

```
Z0-D3-补充包二-全量源码与缺口骨架/
├── README.md                        本文件
├── 01-先读这个/
│   ├── START.md                     60 秒版：这一包相对上一包的增量
│   ├── 外部复核反馈-原文.md          外部 AI 的逐字反馈（未删改）
│   └── 反馈核对表.md                逐条核对：哪条成立、哪条不成立、证据在哪
├── 02-Foundation全量源码/           308 个 .lean（55987 行，3.1 MB）
│   └── Foundation/...               **整个 Foundation 源码树**，不是 167 个子集
├── 03-项目模块/                     32 个 .lean + 两个 pin 文件
│   └── GodelQ/...                   项目侧全部模块，含 Z0Layer1/Z0Layer1Emb
├── 04-缺口骨架/
│   ├── 缺口骨架.lean                **本机编译通过的精确骨架**（含唯一 sorry 的位置）
│   ├── 第二层公式保持性.lean        本机已证的 7 条引理（可直接用）
│   ├── 第一层语法交换律.lean        本机已证的 7 条引理（可直接用）
│   ├── 宇宙多态桥.lean              **本机过核**：宇宙层级障碍清除 + bwd 归约为一条消去
│   ├── 宇宙多态桥-负控制.lean        **本机被拒**：模型真值不能直接当可证性
│   ├── 缺口的精确形状.md            **把 bwd 拆到零件级**：缺哪一步、有哪两条路
│   ├── 编译验证记录.md              三个骨架文件的本机 exit 0 记录
│   └── 编译指令.md                  三种编译方式：完整环境 / 从零构建 / 单文件探针
└── 05-收据与哈希/
    ├── W8-source-manifest.json      30 个源文件的 SHA-256 + 553 外部依赖
    ├── W8-stdout.txt                112 条 #print axioms 原始输出
    ├── W8-RUN.json                  运行元数据
    └── verify_package.py            自验脚本（不需要 Lean）
```

## 相对上一包的**唯一实质变化**

| | 上一包 | 这一包 |
|---|---|---|
| Foundation 源码 | 27 个模块 | **308 个（全量）** |
| 项目模块 | 27 个 | 32 个（+ Z0Layer1、Z0Layer1Emb、SeqTranslateFormula 等） |
| `source-manifest.json` | 缺 | **在** |
| 缺口骨架 | `Z0D3Skeleton.lean`（6 条已证） | 加 `第二层公式保持性.lean`（7 条已证）与 `缺口的精确形状.md` |
| 源码地址 | 无 | `06-源码地址.md`：Foundation 每处引用的 pinned-commit 直链 |
| 外部反馈核对 | 无 | **逐条核对表** |

## 自验（不需要 Lean）

```bash
cd 05-收据与哈希 && python3 verify_package.py
```

期望输出：Foundation 全量 308 个、项目模块 32 个哈希一致、缺口骨架可解析。

## 目标命题（与上一包相同，逐字）

```lean
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V)
```

它一旦成立，`GodelQ/ZFC/Z0Full.lean:117` 的 `zfc_z0_full_of_D3_internalize`
（已过核、无 `sorry`）立即给出完整形式 `𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`。

## 不要做的事

- 改 Foundation / Mathlib 源码。
- 留 `sorry` 冒充完成。卡住就把卡点写成一条精确的 Lean 命题，标在 `CLAIM.md` 里。
- 重复已判死的四条路（见上一包 `04-攻坚路线/ROUTES.md` 与 `03-可用的已证引理/API.md` §E）。
