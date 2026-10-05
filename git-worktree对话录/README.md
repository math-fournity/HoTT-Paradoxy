# git-worktree 对话录：GUI 导出、trajectory 谱系与 worktree 导航

> 资产属性：HUMAN_EDITED。<br>
> 唯一 owner：本目录 README；范围：本目录八份 Codex GUI 对话导出的谱系、原始 trajectory locator 与 Git/worktree 证据导航。<br>
> 建立时间：2026-10-05。导出快照集最初由 Git commit 7b1f7f604d019508ed2d1ee982645937cad0bab8 纳入版本控制。<br>
> 证据边界：本文件不复制任何对话正文、工具输出、隐藏推理或补丁；它只保存未来审计所需的最小定位信息。它不作 HoTT、ZFC 或项目研究结论。

本目录中的八份 Markdown 是 GUI 可见对话的简洁导出：保留用户和助手在 GUI 中可见的消息，以及每轮可见的改动文件胶囊。它们不是原始 JSONL trajectory，也不能取代原始 trajectory。

这些文件具有共享的历史前缀：有些是同一 Codex 对话的 continuation rollover，有些是从同一父对话在不同 cutoff 处分叉出的新对话。若逐个从头阅读，会反复阅读同一段历史；若只按标题或当前 Git branch 猜测，又会把对话继承关系和 Git 历史混为一谈。本 README 的目的就是让未来审计者先定位关系，再只读需要的分支增量。

## 先读这一节：三种不能混同的事实

| 概念 | 这里的含义 | 可回答的问题 | 不能推出什么 |
|---|---|---|---|
| 逻辑对话线程 | Codex thread ID，例如 01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5 | 哪个 GUI 对话从哪个逻辑父对话 fork | 它不等于某一份 JSONL 文件 |
| rollout / trajectory | 一份物理 JSONL；同一逻辑线程可以有多份 rollover | 共享历史精确截在哪里 | rollout 顺序不等于 Git branch |
| Git/worktree 现场 | trajectory 中的 CWD、segment-start Git snapshot、可用的 hook 旁证，以及今天的 git worktree list | 运行时目录在哪里、哪些 Git 信息被直接记录 | 当前 worktree 的 branch 不能反推某一次历史文件修改的 branch |

本 README 中的 fork cutoff 一律采用 Codex 的双条件：

1. 父 rollout 只继承 byte offset 严格小于 B 的记录；
2. 同时只继承 ordinal 严格小于 N 的记录。

两项都是 exclusive cutoff，必须一起使用。offset 是逻辑 JSONL byte offset，不是“在 GUI 里看到的第几行”；不要用文本相似度或人工找相同段落来替代它。

## 快速使用路径

1. 先查看下面的关系图，确定问题落在共享祖先、dev-08 主线，还是某一个 child branch。
2. 只阅读目标 GUI 导出；若问题显然发生在它分叉之前，优先转向父 rollout，而不是重复通读多个 sibling 导出。
3. 若需找出 GUI 文本中的精确分叉消息、工具调用、文件改动或 Git 证据，使用下方的 audit 再生成命令；GUI-only 导出本身故意不带 raw locator。
4. 不要根据目录名、GUI 标题、当前 branch 或当前 worktree 位置猜测历史文件修改发生在哪个 branch。先检查精确 native tool invocation 的 audit provenance。

## 对话分叉关系图

图中的 Rxx 是下方“原始 trajectory 清单”的稳定别名。方括号中的 byte / ordinal 是父 rollout 的共享前缀 cutoff；child 的新增对话从该 cutoff 之后开始。

~~~text
共享的已归档根对话
R00  01a0fb08-ef43-7210-9ea7-41e27c6aa32d
└── R01  01a0fb73-d88b-78b3-a677-349c4641c47e
    └── dev-08  01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5
        │   branch launch: R02
        │   GUI export selected rollout: R06
        │
        ├── dev-02  01a10533-7f5c-79b2-8d00-a5d797205ee5
        │   parent rollout R03 [byte < 148640383; ordinal < 46347]
        │
        ├── dev-03  01a1039a-331b-7c92-acdc-38841283cac8
        │   parent rollout R03 [byte < 92354831; ordinal < 41209]
        │   └── dev-04  01a10533-f07b-7d21-ada8-cd136ce61dd5
        │       parent rollout R04 [byte < 43240412; ordinal < 45352]
        │
        ├── dev-06  01a106f7-75c0-7dd0-b135-63d0393bd6cf
        │   parent rollout R03 [byte < 220743046; ordinal < 51663]
        │   └── dev-07  01a10700-dd83-7171-8601-127270b94e9e
        │       parent rollout R05 [byte < 2345476; ordinal < 51768]
        │
        ├── dev-01  01a1083d-3515-7403-9b43-a5e02d8fc2d5
        │   parent rollout R06 [byte < 12006738; ordinal < 55523]
        │
        └── dev-09  01a10843-afd2-7063-82f8-259c56f359e9
            parent rollout R06 [byte < 12827453; ordinal < 55673]
~~~

共享祖先本身也有两条精确边：

| child | 逻辑父线程 | 父 rollout | cutoff |
|---|---|---|---|
| R01 | R00 | R00 | byte < 13088624；ordinal < 1490 |
| dev-08 branch launch R02 | R01 | R01 | byte < 39034595；ordinal < 4120 |

这里的拓扑不是 Git commit graph。它说明的是用户在 GUI 里能看到的会话历史如何继承；一个 child GUI 导出因而会包含其所有祖先的可见前缀。

## 每条分叉的精确定位

| Child GUI 导出 | 逻辑父线程 | 直接父 rollout | 精确父 cutoff | child 的实际 branch-launch rollout |
|---|---|---|---|---|
| dev-08 | 01a0fb73-d88b-78b3-a677-349c4641c47e | R01 | byte < 39034595；ordinal < 4120 | R02 |
| dev-02 | dev-08 | R03 | byte < 148640383；ordinal < 46347 | R08 |
| dev-03 | dev-08 | R03 | byte < 92354831；ordinal < 41209 | R04 |
| dev-04 | dev-03 | R04 | byte < 43240412；ordinal < 45352 | R10 |
| dev-06 | dev-08 | R03 | byte < 220743046；ordinal < 51663 | R05 |
| dev-07 | dev-06 | R05 | byte < 2345476；ordinal < 51768 | R12 |
| dev-01 | dev-08 | R06 | byte < 12006738；ordinal < 55523 | R07 |
| dev-09 | dev-08 | R06 | byte < 12827453；ordinal < 55673 | R13 |

特别注意三种容易误读的情况：

- dev-08 的 GUI 导出选中的是后期 rollover R06；它真正从共同祖先分叉时的 launch JSONL 是 R02。
- dev-04 的 GUI 导出选中 R09，但它从 dev-03 取得共享前缀的 cross-thread branch launch 是 R10。
- dev-06 的 GUI 导出选中 R11，但它从 dev-08 取得共享前缀的 cross-thread branch launch 是 R05；dev-07 又是从 R05 分叉，不是从 dev-06 的后期选中 R11 分叉。

## GUI 导出文件与 trajectory 的对应

| 标签 | GUI 标题（必须精确匹配） | 本目录导出文件 | GUI 导出所选 raw rollout | cross-thread branch launch raw |
|---|---|---|---|---|
| dev-08 | 🌟 08 - 哥德尔 | dev-08 - 20261005T140115Z-01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5-042fff9e8b82-gui.md | R06 | R02 |
| dev-01 | 🌟 01 - ZFC-1 | dev-01 - 20261005T093957Z-01a1083d-3515-7403-9b43-a5e02d8fc2d5-3647494d3660-gui.md | R07 | R07 |
| dev-02 | 02 - ZFC-1 | dev-02 - 20261004T101101Z-01a10533-7f5c-79b2-8d00-a5d797205ee5-b04cf56b8548-gui.md | R08 | R08 |
| dev-03 | 03 - ZFC-1 | dev-03 - 20261004T103128Z-01a1039a-331b-7c92-acdc-38841283cac8-4ccfd58f1aa3-gui.md | R04 | R04 |
| dev-04 | 04 - ZFC-1 | dev-04 - 20261004T102801Z-01a10533-f07b-7d21-ada8-cd136ce61dd5-9c791ac1226d-gui.md | R09 | R10 |
| dev-06 | 🌟 06 - ZFC-1 | dev-06 - 20261004T160420Z-01a106f7-75c0-7dd0-b135-63d0393bd6cf-cd2523908155-gui.md | R11 | R05 |
| dev-07 | 🌟 07 - ZFC-2 ω 的完成性 | dev-07 - 20261004T162033Z-01a10700-dd83-7171-8601-127270b94e9e-a573664c5370-gui.md | R12 | R12 |
| dev-09 | 🌟 09 - 哥德尔 | dev-09 - 20261005T051816Z-01a10843-afd2-7063-82f8-259c56f359e9-a79ef407f501-gui.md | R13 | R13 |

## 原始 trajectory 清单

以下是用于上图与本目录导出的 raw JSONL 定位。SHA-256 是 2026-10-05 读取时的完整文件身份；重审前应重新计算，而不是只相信路径仍存在。

~~~text
R00  archived shared root
     /Users/aurolafly/.codex/archived_sessions/rollout-2026-10-02T01-14-21-01a0fb08-ef43-7210-9ea7-41e27c6aa32d.jsonl
     sha256 bccc9aa8895a9d614e29277ceb33f136e8d675e00f0b1d0d2ac999df22fc8f6e

R01  archived shared continuation / dev-08 logical parent
     /Users/aurolafly/.codex/archived_sessions/rollout-2026-10-02T03-11-08-01a0fb73-d88b-78b3-a677-349c4641c47e.jsonl
     sha256 77739801c671c2fe6511acd29744aa5bbfd173cf75eb306774a771bfc76a89d5

R02  dev-08 cross-thread branch launch
     /Users/aurolafly/.codex/sessions/2026/10/02/rollout-2026-10-02T05-46-39-01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5.jsonl
     sha256 a06ca4f365fcb9fe55d47ee3ae53aacd36f31202b851fc726c34661937e7b5b8

R03  dev-08 rollover that is the physical parent of dev-02, dev-03 and dev-06
     /Users/aurolafly/.codex/sessions/2026/10/03/rollout-2026-10-03T03-08-14-01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5_01a10097-8df9-7dd0-8009-8357ebc59781.jsonl
     sha256 7c271701272efe5a628bdccfd1a6f4cd48c33414fd448ac3c7ccf52989c95ac3

R04  dev-03 selected and branch-launch rollout; physical parent of dev-04
     /Users/aurolafly/.codex/sessions/2026/10/03/rollout-2026-10-03T17-09-59-01a1039a-331b-7c92-acdc-38841283cac8.jsonl
     sha256 3cf8502e3fbcc19aca83473b1ce5909e18b0e41b1eeb0eafc4c7e3265fdc00af

R05  dev-06 cross-thread branch launch; physical parent of dev-07
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T08-50-43-01a106f7-75c0-7dd0-b135-63d0393bd6cf.jsonl
     sha256 a14c4f34d6bf6944dae8e1d6d5ce2de4a193997297f883bb3914f3ff435cf43c

R06  dev-08 GUI export selected rollout; physical parent of dev-01 and dev-09
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T13-24-08-01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5_01a107f1-c8f6-7bb0-8b78-484d4565d489.jsonl
     sha256 22ecd8973b0f438048a672629b33341751ae79bf2087e0ad2fdf8eb729dcee62

R07  dev-01 selected and branch-launch rollout
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T14-46-31-01a1083d-3515-7403-9b43-a5e02d8fc2d5.jsonl
     sha256 dfcb74b922de7381a2d943efff398ddc135b0c20ca404ccccdc7572352f0bea5

R08  dev-02 selected and branch-launch rollout
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T00-37-03-01a10533-7f5c-79b2-8d00-a5d797205ee5.jsonl
     sha256 4cf0765aef5ad7f0cd1fcd84cf0d227254e09f8c87422255f148e5e003bf551c

R09  dev-04 GUI export selected rollover
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T04-38-20-01a10533-f07b-7d21-ada8-cd136ce61dd5_01a10610-67a7-76e0-b398-21ea02e729f8.jsonl
     sha256 43508b3dce755e384cf83f101e7f6073294f4c375d7ee4eb23c6a6e83d6f6294

R10  dev-04 cross-thread branch launch
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T00-37-32-01a10533-f07b-7d21-ada8-cd136ce61dd5.jsonl
     sha256 33c143b876e0c8e66c750eaff7361a5615202613b91e0762059a4bc0b4b926fc

R11  dev-06 GUI export selected rollover
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T11-35-11-01a106f7-75c0-7dd0-b135-63d0393bd6cf_01a1078e-0a8f-7d91-ad4e-cb0af2298950.jsonl
     sha256 bb0a1b3150cdb1e28dd0d16cdd5564f1a225fa0ba51a6d319f5a941106bb0f76

R12  dev-07 selected and branch-launch rollout
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T09-00-59-01a10700-dd83-7171-8601-127270b94e9e.jsonl
     sha256 5436ac8b7b7af269200928d30252e955f49cd7bc7f10de30d55441aa9d5f34dc

R13  dev-09 selected and branch-launch rollout
     /Users/aurolafly/.codex/sessions/2026/10/04/rollout-2026-10-04T14-53-36-01a10843-afd2-7063-82f8-259c56f359e9.jsonl
     sha256 5d91c1181a5945d4fb9af996251d6353a2606d3c1f268b6d5148b8e51de0540e
~~~

## Git branch 与 worktree 证据

所有八份 audit-mode 导出都得到 lineage status COMPLETE，但 Git execution-context status 都是 PARTIAL_MIXED_EVIDENCE。因此这里采用三个层级，且不跨层推断：

1. segment-start Git snapshot：session_meta 中在该 physical rollout 开始时记录的 branch（若有）和 commit；
2. at-run CWD：raw tool record / at-run hook 所记录的工作目录；
3. current attachment：2026-10-05 运行 git worktree list 时的当前本机状态，只用于帮助找到目录，不是历史执行证据。

### 运行时目录和 Git snapshot

branch omitted 表示该 session_meta 没有记录 branch 字段；它不能被自动改写为“确定是 detached”，也不能由今天的 branch 名补齐。

| 导出 | 运行时 CWD（raw 记录） | branch-launch segment-start snapshot | selected-export segment-start snapshot |
|---|---|---|---|
| dev-08 | /Volumes/D/HoTT_AI_HANDOFF_20260911 | dev @ a89c1d2ef7090479b5e5ee7884ba52670991ed78 | dev @ 82543441b51d4d0d6d3b1e816290fdb130d88898 |
| dev-01 | /Users/aurolafly/.codex/worktrees/bdfd/HoTT_AI_HANDOFF_20260911 | branch omitted @ 9ffca5e045a6aac34ed2720c720e9329a914686b | 同 branch launch |
| dev-02 | /Users/aurolafly/.codex/worktrees/a329/HoTT_AI_HANDOFF_20260911 | branch omitted @ e10771d96940f43ebfb7747898bb1ce6ecb29b17 | 同 branch launch |
| dev-03 | /Users/aurolafly/.codex/worktrees/10c8/HoTT_AI_HANDOFF_20260911 | branch omitted @ dc55ab58a00b640e5dcf957fc84a86afb5cea21f | 同 branch launch |
| dev-04 | /Users/aurolafly/.codex/worktrees/3d2f/HoTT_AI_HANDOFF_20260911 | branch omitted @ 83cebaa5cff291c28e879e1e3b4be6179142d6a0 | branch omitted @ 4ed282fd1d1b372a37965ff77127e62bfe4daf3f |
| dev-06 | /Users/aurolafly/.codex/worktrees/cad0/HoTT_AI_HANDOFF_20260911 | branch omitted @ d38cbedbac3a2ef3ec9127fe82b8bb08b63c6ef2 | codex/h0-z0-priority-realignment @ 5cf4ab063b280ed7f24220526896642f28ee51a2 |
| dev-07 | /Users/aurolafly/.codex/worktrees/05ef/HoTT_AI_HANDOFF_20260911 | branch omitted @ d38cbedbac3a2ef3ec9127fe82b8bb08b63c6ef2 | 同 branch launch |
| dev-09 | /Users/aurolafly/.codex/worktrees/a38d/HoTT_AI_HANDOFF_20260911 | branch omitted @ 9ffca5e045a6aac34ed2720c720e9329a914686b | 同 branch launch |

### 当前可定位的 worktree（仅作寻找目录用）

下表是 2026-10-05 的 git worktree list 快照。它不应覆盖上表的历史证据。

| 对话 | 当时的 at-run CWD | 当前本机可见的相关 attachment |
|---|---|---|
| dev-08 | /Volumes/D/HoTT_AI_HANDOFF_20260911 | 同一路径当前为 dev-08 @ 81e2f12c933e7936343e0b68cae933dc96bc698f |
| dev-01 | /Users/aurolafly/.codex/worktrees/bdfd/HoTT_AI_HANDOFF_20260911 | 同一路径当前为 dev-01 @ d56ddf1ac531f03b1ab97b4ae019c9d87079fc2a |
| dev-02 | /Users/aurolafly/.codex/worktrees/a329/HoTT_AI_HANDOFF_20260911 | 同一路径当前为 dev-02 @ 4005fa806d342d89248e3d954cbb4f69277538f4 |
| dev-03 | /Users/aurolafly/.codex/worktrees/10c8/HoTT_AI_HANDOFF_20260911 | at-run 路径当前为 codex/zfc-observation-boundary-proof @ 34eab1a2e60fc4f131e1ddc0ed171acacde662e8；另有 dev-03 snapshot：/Users/aurolafly/.codex/worktrees/dev-03-workspace-snapshot-20261004，dev-03 @ 854a6aba2839c57d1739fb42f4a02ac635942dbe |
| dev-04 | /Users/aurolafly/.codex/worktrees/3d2f/HoTT_AI_HANDOFF_20260911 | 同一路径当前为 dev-04 @ f97bbcb445231bce0f253976458f6e2eccadaab6 |
| dev-06 | /Users/aurolafly/.codex/worktrees/cad0/HoTT_AI_HANDOFF_20260911 | 同一路径当前为 dev-06 @ af0d9c5c7ee8d779c054066057c7c278959bf7df |
| dev-07 | /Users/aurolafly/.codex/worktrees/05ef/HoTT_AI_HANDOFF_20260911 | at-run 路径当前为 codex/h0-z0-pattern-first-convergence @ d4594f248d24e0417ed82f13217f2da1a8e58343；该次快照中未见本地 dev-07 branch 的 attachment |
| dev-09 | /Users/aurolafly/.codex/worktrees/a38d/HoTT_AI_HANDOFF_20260911 | at-run 路径当前 detached @ dcf12f4bf6b93700847149a32404a83ecba562a8；另有 dev-09 snapshot：/Users/aurolafly/.codex/worktrees/dev-09-snapshot，dev-09 @ 1c34aaee734ef983d4f63eef8d8012b7dc7f3624 |

### 对“哪个 branch 上修改了文件”的审计规则

本文件可以可靠地告诉审计者：某个会话 segment 在哪个 CWD 中运行、segment 开始时的 Git snapshot 是什么、以及当前如何找到对应 worktree。它不能可靠地宣布“该 GUI 回复列出的所有文件都在某个 branch 上修改”，原因是：

- 一个 segment 可跨越多个 Git state；
- 部分 tool context 的 Git branch / HEAD 未被历史 sidecar 捕获；
- 当前 worktree attachment 可能已在对话结束后移动；
- GUI FileChange 胶囊只表示可见文件变动，不携带 native tool invocation 的完整 Git proof。

因此，若问题针对某一文件修改，必须运行该会话的 audit export，查找该 FileChange 对应的原生 tool invocation 及其 pre/post hook sidecar。没有完整同一 invocation 的 Git sidecar 时，结论必须保持 UNKNOWN 或 PARTIAL，不能用此 README 的 current attachment 补造历史 branch。

## 如何再次生成 GUI 导出

导出器是：

~~~text
/Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py
~~~

默认 GUI 模式只输出 GUI 可见内容与每轮 changed-file capsule，并写入私有目录：

~~~text
/Users/aurolafly/.codex/trajectory-ref-exports/
~~~

以下命令按当前 GUI 标题精确匹配。标题有歧义、会话被删除或状态库中不存在时，工具会停止而不会猜测；不要手动以近似标题代替。

~~~sh
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "🌟 08 - 哥德尔"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "🌟 01 - ZFC-1"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "02 - ZFC-1"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "03 - ZFC-1"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "04 - ZFC-1"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "🌟 06 - ZFC-1"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "🌟 07 - ZFC-2 ω 的完成性"
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode gui "🌟 09 - 哥德尔"
~~~

重新生成分叉、raw locator、工具与 Git/worktree 面包屑时，才显式使用 audit 模式，例如：

~~~sh
python3 /Users/aurolafly/.codex/governance-tools/trajectory_gui_ref_export.py --mode audit "🌟 06 - ZFC-1"
~~~

audit 输出是私有审计工作材料，不应把 raw JSONL、完整命令、工具结果、系统提示或审计 Markdown 直接复制进这个版本化目录。若 GUI-only 导出需要更新，先核对 audit 的 lineage status、Rxx 路径和 SHA-256，再有意识地把新的 GUI-only 文件作为新的快照纳入 Git。

要核验本 README 的 raw identity，可对任一 Rxx 路径执行：

~~~sh
shasum -a 256 /absolute/path/to/the/Rxx.jsonl
~~~

如果 SHA-256 与上表不一致，当前 raw 文件已不是这次快照分析过的同一字节序列；应重跑 audit，而不是把旧 cutoff 直接当作对新文件的充分说明。

## 面向未来审计 AI 的最小工作流

1. 先读本 README 的关系图、精确 fork table 和目标行。
2. 只打开与问题直接相关的 GUI export；把 ancestor prefix 视为共享，不用在每个 sibling 中重复通读。
3. 如需判断问题发生在 fork 前还是 fork 后，按 Rxx 与双 cutoff 回到原始 JSONL；不要以 Markdown 段落位置推断。
4. 如需审计一项文件改动或命令，使用 exact title 的 audit 模式，沿 FileChange → native tool invocation → hook sidecar 回查。
5. 将结论分为：GUI 可见内容、raw lineage、at-run CWD、segment-start Git snapshot、完整 per-operation Git proof、current filesystem attachment；缺一层就明确写 UNKNOWN/PARTIAL。

## 本 README 的验证记录与更新清单

- [x] 本目录八份 GUI export 全部列入。
- [x] 八个目标的 lineage audit 均为 COMPLETE。
- [x] 每条 cross-thread 分叉都记录了逻辑父线程、物理父 rollout、双 exclusive cutoff 和 child branch-launch rollout。
- [x] selected rollout 与 branch-launch rollout 不同的 dev-08、dev-04、dev-06 已显式区分。
- [x] 每个 GUI export、raw trajectory locator、运行 CWD、segment-start Git snapshot 和当前 worktree 定位都分层记录。
- [x] Git execution context 的 PARTIAL_MIXED_EVIDENCE 限制已保留；未把 current worktree 状态伪装成历史文件修改证明。
- [x] README 不包含对话正文、原始工具输出、隐藏推理或补丁。

新增或替换导出时，必须重新执行下列核验后再修改本 README：

1. 用 GUI title 运行 GUI 模式，确认目标 thread 唯一。
2. 对需要谱系的条目运行 audit 模式，记录 COMPLETE/PARTIAL 状态、rollout ID、双 cutoff、raw path 和 SHA-256。
3. 对跨 Git/worktree 的主张只记录原始证据实际支持的层级；不要从当前 filesystem 回填历史。
4. 更新关系图、Rxx 清单、worktree 表和这个 checklist，再以精确路径进行 Git review 与提交。
