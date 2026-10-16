// GUI-LINEAGE-KB：八线研究脉络知识库提取
// 依据 dev-docs/GUI研究脉络知识库提取workflow方案.md（权威合同）§3 DAG、§4 R1-R9、§5 门禁 G1-G8。
// 拓扑：8 个逐线提取 agent（独立上下文，并发，用户限定最多 4 个同时在跑）→ 有界补轮循环
//       → 1 个跨线综合 agent → 1 个独立审计 agent；门禁中所有可由命令决定的部份由脚本以
//       world.run 机验（build_scope.py / check_lineage.py），不交给子代理自述。

interface ScopeAnchorSummary {
  total: number;
  anchored: number;
  mechanical_window: number;
  export_absent_prose: number;
  unresolved_prose_docs: string[];
}
interface ScopeLine {
  export: { path: string; lines: number; sha256: string };
  fork: { parent_branch: string; parent_doc: number; parent_rollout: string };
  own_docs: number;
  adjudication_rounds: number;
  anchor_summary: ScopeAnchorSummary;
}
interface Scope {
  lines: Record<string, ScopeLine>;
  invisible_turns_total: number;
}

interface LineResult {
  /** 线名，例如 dev-08。 */
  line: string;
  /** 写出的 THREAD.md 工作区相对路径。 */
  threadPath: string;
  /** 写出的 DISCOVERIES.tsv 工作区相对路径。 */
  tsvPath: string;
  /** 该线自有轮总数（块坐标，取自 scope.json）。 */
  ownRounds: number;
  /** DISCOVERIES.tsv 实际覆盖的自有轮数。 */
  roundsCovered: number;
  /** THREAD.md 的层数。 */
  layers: number;
  /** DISCOVERIES.tsv 的数据行数。 */
  rows: number;
  /** 自报仍未覆盖的 round（应为空数组）。 */
  missingRounds: string[];
  /** 一句话：本线最关键的一次转向是什么，为什么转。 */
  keyTurn: string;
  /** 本线沉淀给后续线、或被后续线接走的最重要一条发现。 */
  propagated: string;
  /** 需要 Master 登记到 ledger 的不确定项；没有则空数组。 */
  unknowns: string[];
}

interface SynthesisResult {
  routeGraphPath: string;
  evolutionPath: string;
  crossFeedPath: string;
  kbIndexPath: string;
  /** CROSS-FEED.md 中给出归宿的 D3 资产 A-ID 条数。 */
  assetsAccountedFor: number;
  /** 两说并陈、交审计员处置的冲突。 */
  conflicts: string[];
  unknowns: string[];
}

interface AuditResult {
  auditPath: string;
  /** 逐门结论与一句话证据。 */
  gates: { gate: string; verdict: 'PASS' | 'FAIL'; evidence: string }[];
  /** 判为 FAIL 的门及其责任线。 */
  linesToFix: string[];
  /** 审计员用种子 gui-lineage-audit-v1 独立复跑 G3 的结果。 */
  g3: { sampled: number; verbatimMatched: number; seed: string; failedTokens: string[] };
  /** 已转写进 AUDIT.md「遗留未知」节、待研究发起人裁定的条目。 */
  legacyUnknowns: string[];
  /** 请 Master 代写进 ledger 的登记条目。 */
  ledgerEntries: { kind: string; note: string; state?: 'OPEN' | 'CLOSED'; supersedes?: string }[];
}

interface Gap {
  line: string;
  missing_rounds: string[];
  anchor_failures: number;
  enum_failures: number;
  column_failures: number;
  thread_missing: boolean;
  tsv_missing: boolean;
  covered: number;
  own_rounds: number;
}

const LINES = ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07'];
const BASE_COMMIT = '6d8a665244ed964b3eaa24c5860cb8f1bf758fdf';
const WORKROOT = '/Users/aurolafly/.codex/worktrees/wflow-gui-lineage-kb/HoTT_AI_HANDOFF_20260911';
const LEDGER = 'wflow-lineage/ledger.jsonl';
const LEDGER_APPEND_PY = [
  'import json, os, sys',
  'p, raw = sys.argv[1], sys.argv[2]',
  'entry = json.loads(raw)',
  'd = json.load(open(p, encoding="utf-8"))',
  'd.setdefault("entries", []).append(entry)',
  'tmp = p + ".tmp"',
  'open(tmp, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\\n")',
  'os.replace(tmp, p)',
  'print("appended %s -> %d entries" % (entry.get("node"), len(d["entries"])))',
].join('\n');

const SHA_PY = [
  'import hashlib, sys',
  'for p in sys.argv[1:]:',
  '    h = hashlib.sha256()',
  '    f = open(p, "rb")',
  '    for c in iter(lambda: f.read(1 << 20), b""):',
  '        h.update(c)',
  '    f.close()',
  '    print("%s\\t%s" % (p, h.hexdigest()))',
].join('\n');

// 上一次运行（被用户的停止通知中断，六条线仍在飞）遗留下的待登记项：dev-08/dev-02 两个 agent
// 回报的未知与口径说明。R6/R8 口径下 agent 不自行改 ledger，这些必须由 Master 的脚本代写，
// 否则审计员看不到、G8 也失去对象。原文两条在停止通知中被截断，已在 note 里注明。
const HANDOFF: { kind: string; node: string; note: string }[] = [
  {
    kind: 'GATE_TOOL_FIXED', node: 'PRE-7',
    note: '两个 dev-08/dev-02 提取 agent 报告的 check_lineage.py 缺陷属实并由 Master 修复：' +
          'G1 循环里 sorted(covered & own) 排在 own 赋值之前（UnboundLocalError），只在某线 THREAD.md ' +
          '存在时触发，故空树预处置未暴露。修复=把 own = {d[\'doc\'] for d in s[\'docs\']} 提前；' +
          '另增 G3_full 门（每个非 MISSING 判词必须在导出原文/该轮 QA 文档/D3 任一语料中逐字出现）。' +
          '修复后 dev-08 127/127、dev-02 13/13 通过，384 个判词全部逐字命中。',
  },
  {
    kind: 'CALIBER_NOTE', node: 'PRE-8',
    note: 'dev-02 agent 登记：round 0013 的 scope 锚是 codex_fallback（anchor_line=14161/' +
          'anchor_block_end=14165），其用户原话「全部推送」在导出 L14154（UNIQUE 区间）早于锚点行；' +
          '该行 export_line 因此留空、以 round 单锚定位。不影响 R1（至少其一可定位），但属坐标口径说明。',
  },
  {
    kind: 'CONFLICT', node: 'PRE-9',
    note: 'dev-02 agent 登记：round 0009 的用户长文 L13919-13941 与父线 dev-08 L13868-13899 逐字节相同' +
          '（manifest 判 SHARED，dev-08 的 0091/0092 亦含同文），GUI查阅索引 §2 只列 dev-02/0003。' +
          '轮次归属按 QA 块坐标记 round 0009；文本去重与跨线归属需 N9 在 CROSS-FEED.md 处置、N10 核。',
  },
  {
    kind: 'CALIBER_NOTE', node: 'PRE-10',
    note: 'dev-02 agent 登记：机械轮 0001/0002/0008（anchor_status=no_prose_mechanical_round，' +
          'environment_context 与 external_codex_apps_open_page）无 prose 可摘，相关行 verdict_token ' +
          '记 MISSING（D02-L8-003 分叉基座、D02-L3-012 round 0008），G3 抽样会跳过；' +
          'round 0001/0002 摘到的逐字 token 是机械内容本身。',
  },
  {
    kind: 'UNKNOWN', node: 'PRE-11',
    note: 'dev-02 agent 登记：generation-14 core curation 候选 KC-000063（D02-L7-039）状态 parked——' +
          'canonical STATE/HEAD 有未提交 checkpoint 未覆盖，且 dev-02 与 dev-03 各有一份互相竞争的 v14 ' +
          '草稿（八线分叉后复盘 §9.2），未成为 current core。属研究状态登记，非本 workflow 的数学结论。',
  },
  {
    kind: 'CONFLICT', node: 'PRE-12',
    note: 'dev-02 agent 登记（原文在停止通知中被截断）：C-359–C-365 与 canonical dev 上的同名 claim ' +
          '撞号。即审计 K4 预登记项（C-359~C-365 同号异组、C-369 三义、C-370 起三组）。完整表述见 ' +
          'wflow-lineage/lineage/dev-02/THREAD.md 第 10 节；G5 按方案 §5 预登记处理。',
  },
  {
    kind: 'LINE_PROVENANCE', node: 'PRE-13',
    note: 'dev-08 agent 自建机验结果（因当时的脚本缺陷，非官方输出）：G1 覆盖 127/127 无缺；' +
          'G2 双锚/枚举/列数失败 0（154 行均 12 列）；G3 用默认种子 gui-lineage-audit-v1 抽 30/153 ' +
          '个判词逐字命中，未命中 0；G5 carried 行 artifact_ref 路径全部可解析。已由修复后的 ' +
          'check_lineage.py 复跑确认（G1/G2/G3_full/G5_mech 均 pass）。',
  },
  {
    kind: 'CALIBER_NOTE', node: 'PRE-14',
    note: 'dev-08 agent 登记（原文在停止通知中被截断）：与 scope.json 有关的口径分歧需 Master 登记。' +
          '完整表述见 wflow-lineage/lineage/dev-08/THREAD.md 附录 C「本线读法与陷阱自记账」；' +
          'N10 须逐条核该附录与 dev-02 THREAD 第 10 节。',
  },
];

const extractors: Record<string, Agent> = {};
for (const line of LINES) {
  extractors[line] = agent(`${line} 线脉络提取员`, {
    system:
      '你是 GUI-LINEAGE-KB 的逐线提取员：只读八份冻结输入层，为本线从末轮回溯到分叉点重建研究脉络与发现清单。' +
      '你只写自己被分配的两个文件，不写其它任何文件，不改任何输入层，不 git add、不切分支、不读 ~/.codex 下的原始 rollout。' +
      '锚点、轮号、判词都必须能在原文逐字复核；证据不足就如实写 MISSING 或登记未知，绝不编造行号或判词，也不产出任何数学结论。',
  });
}

const scopeText = await files.read('wflow-lineage/scope.json');
const scope = JSON.parse(scopeText) as Scope;

function briefFor(line: string): string {
  const s = scope.lines[line];
  const a = s.anchor_summary;
  return (
    `${line}：导出 ${s.export.path}（${s.export.lines} 行）；分叉自 ${s.fork.parent_branch}#${s.fork.parent_doc}；` +
    `自有轮 ${s.own_docs} 个（块坐标清单见 scope.json 的 docs[]）；裁决#3 轮数 ${s.adjudication_rounds}；` +
    `锚点：唯一锚 ${a.anchored}、机械轮窗口 ${a.mechanical_window}、导出缺文轮 ${a.export_absent_prose}` +
    `${a.unresolved_prose_docs.length ? '（' + a.unresolved_prose_docs.join(',') + '）' : ''}。`
  );
}

artifact.table('lines', {
  title: '八线提取进度',
  columns: [
    { field: 'line', label: '线' },
    { field: 'ownRounds', label: '自有轮' },
    { field: 'roundsCovered', label: '已覆盖' },
    { field: 'layers', label: 'THREAD 层数' },
    { field: 'rows', label: '发现行数' },
  ],
  key: 'line',
});

async function appendLedger(entry: Record<string, unknown>): Promise<string> {
  const r = await world.run('python3', [
    '-c', LEDGER_APPEND_PY, LEDGER, JSON.stringify(entry),
  ]);
  return r.stdout.trim();
}

/** 已落地文件的 sha256 指纹（LINE_DONE 的溯源字段）。文件不存在则不计入。 */
async function fileHashes(paths: string[]): Promise<Record<string, string>> {
  const existing: string[] = [];
  for (const p of paths) {
    const probe = await world.run('python3', [
      '-c', 'import sys,os\nsys.exit(0 if os.path.exists(sys.argv[1]) else 1)', p,
    ]);
    if (probe.exitCode === 0) existing.push(p);
  }
  if (existing.length === 0) return {};
  const r = await world.run('python3', ['-c', SHA_PY].concat(existing), { timeoutMs: 300000 });
  const out: Record<string, string> = {};
  for (const line of r.stdout.trim().split('\n')) {
    const idx = line.indexOf('\t');
    if (idx > 0) out[line.slice(0, idx)] = line.slice(idx + 1);
  }
  return out;
}

function linePrompt(line: string): string {
  const skeleton =
    line === 'dev-08'
      ? 'dev-08 另加共享前缀 #1–#75 骨架层，只建层名＋一句话，不逐轮展开'
      : '无共享前缀骨架层任务';
  return [
    `你是 GUI-LINEAGE-KB 的 ${line} 线提取 agent（只读子代理）。工作根：${WORKROOT}（下称 W）。`,
    `第一动作：读 W/wflow-lineage/scope.json 的 lines.${line} 段——它给本线权威的自有轮清单（docs[].doc）、每轮在 GUI 导出里的锚点（anchor_line/anchor_block_end/anchor_window）、分叉父子（fork）与裁决#3 轮数。你的 round 字段必须取自该清单。`,
    `本线速览（由脚本从 scope.json 计算，一切锚数据以 scope.json 原文为准）：${briefFor(line)}`,
    `输入（全部只读，路径相对 W）：${scope.lines[line].export.path}；audit/GUI-SYNTH-REDO/qa/${line}/（NNNN.md 切片 + _index.jsonl 源 rollout 坐标 + _branch.json）；audit/GUI-ASSET-RECOVERY/{manifest.json, notes/${line}.md, assets-ledger.md, D3-资产登记v2-20261007.md}；.claude/goals/CG-006-zfc-complete-formalization/{八线分叉后复盘.md, GUI查阅索引.md, Targets与Profile.md} 中与 ${line} 相关的节；docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md。`,
    `任务：写 W/wflow-lineage/lineage/${line}/THREAD.md（分层脉络，尾→分叉；${skeleton}）与 W/wflow-lineage/lineage/${line}/DISCOVERIES.tsv（12 列，制表符分隔，无表头：id line layer round export_line type claim verdict_token artifact_ref status propagated_to notes）。`,
    '硬规则（与方案 §4 R1-R9 一致）：R1 双锚——每行给 export_line 与 round 至少其一；export_line 用 scope.json 的锚点，不许把 _index.jsonl 的 rollout 行号当导出行号。R2 判词逐字——从导出原文摘，不改大小写/下划线，找不到才标 MISSING 并说明。R3 身份四类标注——用户原话【原话】、GPT 结论【自述】、机器证明【证明】、审计者或你的判断【判断】，不得互相冒充。R4 轮数口径——块坐标 round 来自 scope.json 清单，裁决#3 分线总数只作并列引用，两者不互换。R7 不得产出任何数学结论。R9 语料固有缺口不得算你的失职、也不得掩饰。',
    'R6/R8 的执行方式（与方案原稿措辞唯一的差异，目的是避免 8 个并发 agent 读改写同一个 ledger.jsonl 而互相覆盖）：除上面两个文件外不得写任何文件；ledger.jsonl 由 Master 的脚本统一追加，你要登记的条目写进返回结果的 unknowns 字段，不要自己去改 ledger。',
    '已知陷阱：判词字符串大量存在于 assets-ledger.md/D3（如 TERMINAL_CLEANUP_WITHOUT_CLOSE、NO_MODEL_RECALL_CANDIDATE）；机械轮（anchor_status=no_prose_mechanical_round）的 User 块只有 environment/page/goal 等机械内容，仍须在 DISCOVERIES 覆盖并在 THREAD.md 说明它是机械轮；研究发起人的核心提问段落在多条线逐字重复（Q/A/B 段），勿把别线或别轮的同一段文本归到本轮；goal 续跑块内嵌有早轮原文；dev-08 的 #112 哥德尔原话只在分支 dev-notes，GUI 导出内有；anchor_status=export_absent_prose 的轮在 A 层导出没有原文，只能引 QA 文档并在 THREAD.md 说明。',
    '完成判据：DISCOVERIES.tsv 覆盖 scope.json 给的本线全部 round；THREAD.md 每一层都有“为什么转向”（引用户原话或 GPT 自述里的理由）。',
    '返回结构化的 LineResult：line、threadPath、tsvPath、ownRounds、roundsCovered、layers、rows、missingRounds、keyTurn、propagated、unknowns。',
  ].join('\n');
}

/** 文件行数（用于接手线的行数统计）。文件不存在返回 0。 */
async function countRows(path: string): Promise<number> {
  const r = await world.run('wc', ['-l', path]);
  const m = /^\s*(\d+)\s/.exec(r.stdout);
  return m ? Number(m[1]) : 0;
}

const lineResults: Record<string, LineResult> = {};

phase('核对开工条件并重建范围表');
const root = await world.run('git', ['rev-parse', '--show-toplevel']);
const descends = await world.run('git', ['merge-base', '--is-ancestor', BASE_COMMIT, 'HEAD']);
if (root.stdout.trim() !== WORKROOT) {
  throw new Error(`工作根不符：${root.stdout.trim()}`);
}
if (descends.exitCode !== 0) {
  throw new Error(`分支头不是 ${BASE_COMMIT} 或其子孙，按用户指令停下`);
}
await world.run('mkdir', ['-p'].concat(LINES.map((l) => `wflow-lineage/lineage/${l}`)));
const rebuilt = await world.run('python3', ['-B', 'wflow-lineage/tools/build_scope.py'], {
  timeoutMs: 900000,
});
if (rebuilt.exitCode !== 0) {
  throw new Error(`build_scope.py 失败：${rebuilt.stderr.slice(0, 800)}`);
}
// 先跑一次机验，据缺口决定要派哪些线：已通过 G1/G2 的线绝不重派（上一个运行已完成的 dev-08/dev-02
// 就是这样被排除的）；机验输出不可解析则 fail closed，不猜。
const preGate = await world.run('python3', [
  '-B', 'wflow-lineage/tools/check_lineage.py', '--json',
], { timeoutMs: 900000 });
let todo: string[] = [];
try {
  const pre = JSON.parse(preGate.stdout.trim().split('\n').pop() ?? '{}') as { gaps: Gap[] };
  todo = (pre.gaps ?? []).map((g) => g.line).filter((l) => LINES.indexOf(l) >= 0);
} catch {
  throw new Error(`机验门禁输出不可解析，拒绝凭猜测派节点：${preGate.stdout.slice(-400)}`);
}
for (const h of HANDOFF) {
  await appendLedger({
    kind: h.kind, agent: 'master', node: h.node, ts: 'workflow-start',
    path: ['wflow-lineage/lineage'], state: 'OPEN', note: h.note,
  });
}
// 为盘上已有的线补溯源指纹（上一个运行的 LINE_DONE 没有 sha256 字段）。
for (const line of LINES) {
  if (todo.indexOf(line) >= 0) continue;
  const threadPath = `wflow-lineage/lineage/${line}/THREAD.md`;
  const tsvPath = `wflow-lineage/lineage/${line}/DISCOVERIES.tsv`;
  const hashes = await fileHashes([threadPath, tsvPath]);
  if (Object.keys(hashes).length === 0) continue;
  await appendLedger({
    kind: 'LINE_PROVENANCE', agent: 'master', node: `N-prov-${line}`, ts: 'workflow-start',
    path: [threadPath, tsvPath],
    sha256: hashes, state: 'CLOSED',
    note: `${line} 在上一个运行已完成并通过本运行机验，本运行不重派；此处补录产物 sha256 与交接登记。`,
  });
  const own = scope.lines[line].own_docs;
  lineResults[line] = {
    line, threadPath, tsvPath, ownRounds: own, roundsCovered: own,
    layers: 0, rows: await countRows(tsvPath), missingRounds: [],
    keyTurn: `从上一个运行接手，已通过本运行机验（G1 覆盖 ${own}/${own}、G2 无失败行、G3_full 判词全部逐字命中）；本运行未重算层数，关键转向以该线 THREAD.md 为准。`,
    propagated: '', unknowns: [],
  };
}
await appendLedger({
  kind: 'RUN_START', agent: 'master', node: 'N0', ts: 'workflow-start',
  path: ['wflow-lineage/scope.json'], state: 'CLOSED',
  note: '续作运行开工：工作根与分支头核验通过，build_scope.py 重建范围表成功（输入层未被改动）。' +
        `八线自有轮合计 ${LINES.reduce((n, l) => n + scope.lines[l].own_docs, 0)}（块坐标）；` +
        `不可见用户轮 ${scope.invisible_turns_total} 个（R-9.2）。` +
        `据机验缺口派节点：${todo.join('、') || '无（全部已通过）'}；` +
        `已补登记上一次运行的交接项 ${HANDOFF.length} 条。`,
});
log(`开工核验通过；本运行只派 ${todo.length} 条线（${todo.join('、')}），其余已通过机验不重派`);

phase('逐线提取尚未完成的 GUI 线');
await Promise.all(
  todo.map(async (line) => {
    try {
      const r = await extractors[line].ask<LineResult>(linePrompt(line));
      lineResults[line] = r;
      report(r, 'lines');
      await appendLedger({
        kind: 'LINE_DONE', agent: `${line}线提取员`, node: `N-${line}`, ts: 'workflow',
        path: [r.threadPath, r.tsvPath].filter((p) => p.length > 0),
        sha256: await fileHashes([r.threadPath, r.tsvPath].filter((p) => p.length > 0)),
        state: 'CLOSED',
        note: `${line}：覆盖 ${r.roundsCovered}/${r.ownRounds} 轮，THREAD ${r.layers} 层，DISCOVERIES ${r.rows} 行；关键转向：${r.keyTurn}` +
              (r.unknowns.length ? `；待登记未知 ${r.unknowns.length} 条` : ''),
      });
    } catch (e) {
      const msg = String(e).slice(0, 300);
      lineResults[line] = {
        line,
        threadPath: `wflow-lineage/lineage/${line}/THREAD.md`,
        tsvPath: `wflow-lineage/lineage/${line}/DISCOVERIES.tsv`,
        ownRounds: scope.lines[line].own_docs, roundsCovered: 0, layers: 0, rows: 0,
        missingRounds: [], keyTurn: `提取失败：${msg}`, propagated: '',
        unknowns: [`提取失败：${msg}`],
      };
      report(lineResults[line], 'lines');
    }
  }),
);
log(`八线提取阶段结束：${LINES.map((l) => `${l} ${lineResults[l].roundsCovered}/${lineResults[l].ownRounds}`).join('，')}`);

phase('补齐未覆盖轮次并修正不合规行');
let correctionRounds = 0;
let machineUnreadable = false;
for (let round = 0; round < 2; round++) {
  const chk = await world.run('python3', [
    '-B', 'wflow-lineage/tools/check_lineage.py', '--json',
  ], { timeoutMs: 900000 });
  const lastLine = chk.stdout.trim().split('\n').pop() ?? '';
  let gaps: Gap[] | null = null;
  try {
    gaps = (JSON.parse(lastLine) as { gaps: Gap[] }).gaps ?? [];
  } catch {
    gaps = null;
  }
  if (gaps === null) {
    machineUnreadable = true;
    log('机验输出无法解析为 JSON：跳过补轮判断，终门复验会暴露该问题');
    break;
  }
  if (gaps.length === 0) {
    log('机验无缺口，进入跨线综合');
    break;
  }
  correctionRounds++;
  log(`第 ${correctionRounds} 轮补修：${gaps.map((g) => g.line).join('、')}`);
  await Promise.all(
    gaps.map(async (g) => {
      try {
        const r = await extractors[g.line].ask<LineResult>([
          `补修（第 ${correctionRounds} 轮）。Master 的机验 wflow-lineage/tools/check_lineage.py --json 报告你负责的 ${g.line} 线仍有缺口：`,
          JSON.stringify(g),
          '逐项处理：missing_rounds 里的每个 round 至少补一行 DISCOVERIES（纯机械轮写“机械轮，无用户提问实质内容”）；' +
            'anchor_failures 按 scope.json 的 anchor_line/anchor_block_end/anchor_window 改正 export_line；' +
            'column_failures 把该行补成或改成 12 列；enum_failures 把 type/status 改成法定枚举；' +
            'thread_missing/tsv_missing 则重建文件。',
          `仍然只允许写 W/wflow-lineage/lineage/${g.line}/THREAD.md 与 DISCOVERIES.tsv。修完在返回里报告最新数字。`,
        ].join('\n'));
        lineResults[g.line] = r;
        report(r, 'lines');
      } catch (e) {
        lineResults[g.line] = {
          ...lineResults[g.line],
          keyTurn: `补修失败：${String(e).slice(0, 200)}`,
          unknowns: [...lineResults[g.line].unknowns, `补修失败：${String(e).slice(0, 300)}`],
        };
      }
    }),
  );
}
if (correctionRounds > 0) {
  await appendLedger({
    kind: 'CORRECTION', agent: 'master', node: 'N-corr', ts: 'workflow',
    path: ['wflow-lineage/lineage'], state: 'CLOSED',
    note: `共执行 ${correctionRounds} 轮补修后进入综合阶段。`,
  });
}

phase('跨线综合脉络、演进与资产归宿');
const synthesis = agent('跨线综合员', {
  system:
    '你是 GUI-LINEAGE-KB 的跨线综合员：把八线的 THREAD.md 与 DISCOVERIES.tsv 综合成跨线传播图、五个概念的跨线演变史、' +
    'D3 六百一十九条资产的逐条归宿表和知识库总入口。只写自己被分配的四个文件，不修改任何既有产物；' +
    '两说冲突时并陈并交审计员处置，不擅自裁决；不产出任何数学结论。',
});
const lineSummary = LINES.map((l) => {
  const r = lineResults[l];
  return `${l}：${r.roundsCovered}/${r.ownRounds} 轮、${r.layers} 层、${r.rows} 行；关键转向：${r.keyTurn}；被接走/沉淀：${r.propagated}`;
}).join('\n');
const synthesisResult = await synthesis.ask<SynthesisResult>([
  '你是 GUI-LINEAGE-KB 综合 agent。读 W/wflow-lineage/lineage/*/THREAD.md 与 W/wflow-lineage/lineage/*/DISCOVERIES.tsv 全部，' +
    '加上 audit/GUI-ASSET-RECOVERY/D3-资产登记v2-20261007.md 与 .claude/goals/CG-006-zfc-complete-formalization/{Targets与Profile.md}。',
  '写四个文件：W/wflow-lineage/lineage/ROUTE-GRAPH.md（节点=层、边标注 供给/否决/接走，带轮次锚）；' +
    'W/wflow-lineage/lineage/EVOLUTION.md（P/Q/Done(OriginDone)/Z0/想法T 五概念的跨线演变，每步锚 round+行号）；' +
    'W/wflow-lineage/lineage/CROSS-FEED.md（D3 619 条逐条归宿：carried/parked/superseded/cold/open 之一＋一句理由，A-ID 必须逐字出现）；' +
    'W/wflow-lineage/lineage/KB-INDEX.md（总入口、所有相对链接校验表）。',
  '规则同方案 §4 R1-R9：每步带轮次锚与导出行号；两说冲突并陈写进返回的 conflicts；不得产出数学结论。',
  '分叉图按 audit/GUI-SYNTH-REDO/qa/_tree.json：dev-04 分叉自 dev-03#13、dev-07 分叉自 dev-06#3，' +
    '其余六线分叉自 dev-08（dev-01#111、dev-02#86、dev-03#75、dev-06#97、dev-09#113、dev-08 自 archive-01a0fb73#10）。',
  '八线提取结果速览（供你对账，细节以文件为准）：',
  lineSummary,
  '本运行已代上次运行登记的交接项在 ledger（kind 为 CALIBER_NOTE / CONFLICT / UNKNOWN / ' +
    'GATE_TOOL_FIXED，node PRE-7..PRE-14）：其中 dev-02 round 0009 与父线 dev-08 逐字节相同的跨线归属、' +
    'C-359~C-365 撞号（K4），必须由你在 CROSS-FEED.md 里给出处置；dev-02 THREAD 第 10 节与 ' +
    'dev-08 THREAD 附录 C 是这两条线的完整未知项清单。',
  '不要自己改 ledger.jsonl；要登记的条目写进返回结果，由 Master 的脚本代写。',
  '返回 SynthesisResult：routeGraphPath、evolutionPath、crossFeedPath、kbIndexPath、assetsAccountedFor、conflicts、unknowns。',
].join('\n'));
report({
  stage: '跨线综合', routeGraph: synthesisResult.routeGraphPath,
  assets: synthesisResult.assetsAccountedFor, conflicts: synthesisResult.conflicts.length,
  unknowns: synthesisResult.unknowns.length,
});
await appendLedger({
  kind: 'SYNTH_DONE', agent: '综合员', node: 'N9', ts: 'workflow',
  path: [synthesisResult.routeGraphPath, synthesisResult.evolutionPath,
         synthesisResult.crossFeedPath, synthesisResult.kbIndexPath],
  state: 'CLOSED',
  note: `四个综合文件已写；CROSS-FEED 给出归宿的资产 ${synthesisResult.assetsAccountedFor} 条；` +
        `并陈冲突 ${synthesisResult.conflicts.length} 条、未知 ${synthesisResult.unknowns.length} 条，交审计员处置。`,
});

phase('请第一次来的 AI 检验知识库入口，并据以修订');
const reader = agent('冷到访的知识库读者', {
  system:
    '你是一个第一次来到这个知识库的 AI，任务是替未来的使用者判断：从这个入口出发，能不能在有限跳数内' +
    '回答该回答的问题。你只看入口与它链接到的东西，不改任何文件；发现答不了的问题就具体指出缺哪一跳。',
});
interface ReaderResult {
  /** 未来 AI 会问、而按现在的入口答不出来或要绕远的问题。 */
  blockedQuestions: string[];
  /** 入口里含糊、指代不明或名不副实的地方。 */
  unclearSpots: string[];
  /** 读者自己能否在 3 跳内回答五类标准问题，逐类说明。 */
  threeHopCheck: string[];
}
const readerResult = await reader.ask<ReaderResult>([
  '你现在是一个第一次来到这个知识库的 AI，对这个项目此前的对话一无所知。',
  `只读 W/wflow-lineage/lineage/KB-INDEX.md 以及它链接过去的文件（不要读 git-worktree对话录/ 的八份长导出）。`,
  '按方案 §8 的验收口径回答：从 KB-INDEX 出发，能否在 ≤3 跳内回答这五类问题——' +
    '(1) 某条线在某个阶段想做什么；(2) 某轮得到了什么判词；(3) 为什么转向；(4) 哪个发现被哪条线接走；' +
    '(5) 某个资产现在何处。逐类给出你实际经过的跳数，答不出就说是哪一类、卡在哪。',
  '然后指出：入口里哪些地方含糊或名不副实；哪些问题你会答不出；要让一个陌生 AI 少绕弯，还缺什么。',
  '不要修改任何文件，也不要去核实内容真假——那是对照原文的活，不是你的活。',
  '返回 ReaderResult：blockedQuestions、unclearSpots、threeHopCheck。',
].join('\n'));
report({ stage: '入口可用性', blocked: readerResult.blockedQuestions.length, unclear: readerResult.unclearSpots.length });
const needRevision = readerResult.blockedQuestions.length + readerResult.unclearSpots.length > 0;
if (needRevision) {
  const revision = await synthesis.ask<SynthesisResult>([
    '有第一次来的 AI 读了 KB-INDEX，报告它答不出或看不明白以下事项：',
    JSON.stringify(readerResult, null, 1),
    '请只修订 KB-INDEX.md（必要时微调其指向的层标题，但不得改八线 THREAD.md 与 DISCOVERIES.tsv 的实质内容），' +
      '使上述每一个 blocked question 都能在 ≤3 跳内被回答，并消除 unclear spots。',
    '仍然不得产出数学结论，不得自己改 ledger.jsonl。返回修订后的 SynthesisResult。',
  ].join('\n'));
  report({ stage: '入口修订', kbIndexPath: revision.kbIndexPath, assets: revision.assetsAccountedFor });
  await appendLedger({
    kind: 'REVISION', agent: '综合员', node: 'N9-rev', ts: 'workflow',
    path: [revision.kbIndexPath], state: 'CLOSED',
    note: `冷到访读者提出 ${readerResult.blockedQuestions.length} 个答不出、${readerResult.unclearSpots.length} 处含糊，综合员据此修订 KB-INDEX。`,
  });
} else {
  await appendLedger({
    kind: 'REVISION', agent: '综合员', node: 'N9-rev', ts: 'workflow',
    path: [synthesisResult.kbIndexPath], state: 'CLOSED',
    note: '冷到访读者未提出阻塞性问题，KB-INDEX 不修订。',
  });
}

phase('跑门禁机验并把结果交给审计员');
const machineGates = await world.run('python3', [
  '-B', 'wflow-lineage/tools/check_lineage.py', '--json',
], { timeoutMs: 900000 });
log(`门禁机验退出码 ${machineGates.exitCode}`);

phase('独立审计 G1–G8 并出具 AUDIT.md');
const auditor = agent('独立审计员', {
  system:
    '你是 GUI-LINEAGE-KB 的独立审计员：按方案 §5 的 G1–G8 逐门取证。机器能判的照录机验结果并抽核其判 negative 的行，' +
    '需要读原文判断的（判词逐字、资产归宿语义、落点语义、口径一致）你自己读原文核。你只写 AUDIT.md 一个文件，' +
    '不修改任何既有产物；证据不足就判 FAIL 或登记遗留未知，不用“总体一致”替代逐项遍历，也不产出任何数学结论。',
});
const auditResult = await auditor.ask<AuditResult>([
  '你是 GUI-LINEAGE-KB 审计 agent。对 W/wflow-lineage/lineage/ 全部产物按方案 §5 门禁 G1-G8 逐项验，' +
    '产出 W/wflow-lineage/lineage/AUDIT.md（逐门 PASS/FAIL＋证据定位：文件、round、行号）。',
  '机验结果（由脚本跑 check_lineage.py --json 得到，你不要自己跑它，直接采用并抽核其中判 negative 的行）：',
  machineGates.stdout.trim().split('\n').pop() ?? '',
  '机验边界：G4_mech 只证明 619 个 A-ID 在 CROSS-FEED.md 出现过，“有归宿＋一句理由”的语义要你逐条核；' +
    'G5_mech 只证明 carried 行的 artifact_ref 路径可解析，落点是否真承载该判词要你核。',
  'G3 判词逐字：用种子 gui-lineage-audit-v1，由你本人独立地抽 30 个 verdict_token 回导出原文逐字比对' +
    '（不得采信 Master 预检、check_lineage.py 的 G3_pre 或任何 agent 自述）。',
  'G5 carried 落点用 git 可验（撞号区 C-359~C-365/C-369/C-370 起按方案 §5 G5 预登记处理，不算 agent 失败）。',
  'G7 确认全部文本的轮数字段符合 R-4（块坐标 round 与裁决#3 分线总数分列，不互换）。',
  `G8：ledger 不得有未结 CONFLICT/UNKNOWN。要处置的有三类：综合员并陈的 ${synthesisResult.conflicts.length} 条冲突与其 unknowns；` +
    '本运行开工时代上一次运行登记的交接项（ledger 里 node PRE-7..PRE-14，kind 为 CALIBER_NOTE/CONFLICT/UNKNOWN/' +
    'GATE_TOOL_FIXED，正文见各条 note）；以及你自己在审计中新发现的。逐条处置：能在原文裁定的写结论并置 ' +
    'state=CLOSED；只能留给研究发起人的，写进 AUDIT.md「遗留未知」节，并在 ledgerEntries 里给一条 ' +
    'state=CLOSED、supersedes 指明被它取代的 node 的登记，说明已转写 AUDIT.md 第几节；' +
    '既不能裁定也不转写的才留 state=OPEN（那会让 G8 如实失败）。',
  `入口可用性：冷到访读者对 KB-INDEX 提出 ${readerResult.blockedQuestions.length} 个答不出、` +
    `${readerResult.unclearSpots.length} 处含糊，综合员已据此修订；你要核这些修订是否真的消除了阻塞，` +
    '以及修订有没有把谁的实质内容改错。',
  '不得改任何既有文件，只写 AUDIT.md；不要自己改 ledger.jsonl，要登记的条目写进返回的 ledgerEntries，由 Master 的脚本代写。',
  '返回 AuditResult：auditPath、gates、linesToFix、g3、legacyUnknowns、ledgerEntries。',
].join('\n'));
report({
  stage: '独立审计', auditPath: auditResult.auditPath,
  gatesPass: auditResult.gates.filter((g) => g.verdict === 'PASS').length,
  gatesTotal: auditResult.gates.length,
  g3: `${auditResult.g3.verbatimMatched}/${auditResult.g3.sampled}`,
  legacyUnknowns: auditResult.legacyUnknowns.length,
});
for (const e of auditResult.ledgerEntries) {
  await appendLedger({
    kind: e.kind, agent: '审计员', node: 'N10', ts: 'workflow',
    path: ['wflow-lineage/lineage/AUDIT.md'],
    state: e.state ?? 'OPEN', ...(e.supersedes ? { supersedes: e.supersedes } : {}),
    note: e.note,
  });
}
await appendLedger({
  kind: 'AUDIT_DONE', agent: '审计员', node: 'N10', ts: 'workflow', path: [auditResult.auditPath],
  state: auditResult.gates.every((g) => g.verdict === 'PASS') ? 'CLOSED' : 'OPEN',
  note: `G1-G8：${auditResult.gates.map((g) => `${g.gate}=${g.verdict}`).join(' ')}；` +
        `G3 抽样 ${auditResult.g3.verbatimMatched}/${auditResult.g3.sampled} 逐字命中（seed ${auditResult.g3.seed}）；` +
        `遗留未知 ${auditResult.legacyUnknowns.length} 条。`,
});

phase('终门复验并交付知识库');
const finalGates = await world.run('python3', [
  '-B', 'wflow-lineage/tools/check_lineage.py', '--json',
], { timeoutMs: 900000 });
const finalLast = finalGates.stdout.trim().split('\n').pop() ?? '{}';
let finalGapCount = -1;
let finalGaps: Gap[] = [];
try {
  const p = JSON.parse(finalLast) as { exit_code: number; gaps: Gap[] };
  finalGaps = p.gaps ?? [];
  finalGapCount = p.exit_code;
} catch {
  finalGapCount = -1;
}
const auditAllPass = auditResult.gates.every((g) => g.verdict === 'PASS');
const finalPass = finalGapCount === 0 && auditAllPass;
await appendLedger({
  kind: 'FINAL_GATE', agent: 'master', node: 'N-final', ts: 'workflow',
  path: ['wflow-lineage/lineage/AUDIT.md'], state: finalPass ? 'CLOSED' : 'OPEN',
  note: `终门机验 exit=${finalGapCount}${machineUnreadable ? '（补轮阶段机验输出曾不可解析）' : ''}，` +
        `审计逐门 ${auditResult.gates.map((g) => `${g.gate}=${g.verdict}`).join(' ')}；` +
        `未结缺口 ${finalGaps.length} 项${finalPass ? '' : '（未宣称完成，移交研究发起人裁定）'}。`,
});

try {
  await artifact.file('kb-index', 'wflow-lineage/lineage/KB-INDEX.md', {
    title: '八线研究脉络知识库 · 总入口',
    description: '任一未来 AI 从这里出发，≤3 跳内回答某条线在某个阶段想做什么、得到了什么判词、为什么转向、哪个发现被哪条线接走、某资产现在何处。',
    primary: true,
  });
} catch {
  log('KB-INDEX.md 缺失或过大，未发布');
}
try {
  await artifact.file('audit-report', 'wflow-lineage/lineage/AUDIT.md', {
    title: 'G1–G8 门禁审计报告',
    description: '独立审计员逐门 PASS/FAIL 与证据定位。',
  });
} catch {
  log('AUDIT.md 缺失，未发布');
}

const findings = LINES.map((l) => {
  const r = lineResults[l];
  const gap = finalGaps.find((g) => g.line === l);
  return {
    where: `wflow-lineage/lineage/${l}/THREAD.md + DISCOVERIES.tsv`,
    what: `${l}：覆盖 ${r.roundsCovered}/${r.ownRounds} 自有轮，THREAD ${r.layers} 层、发现 ${r.rows} 行。关键转向：${r.keyTurn}`,
    evidence: `check_lineage.py --json：${gap ? `仍有缺口 ${JSON.stringify(gap)}` : '无缺口'}；分叉自 ${scope.lines[l].fork.parent_branch}#${scope.lines[l].fork.parent_doc}`,
    status: gap ? ('unconfirmed' as const) : ('verified' as const),
    severity: gap ? ('high' as const) : ('low' as const),
  };
});
for (const g of auditResult.gates.filter((x) => x.verdict === 'FAIL')) {
  findings.push({
    where: 'wflow-lineage/lineage/AUDIT.md',
    what: `门禁 ${g.gate} 未通过：责任线 ${auditResult.linesToFix.join('、') || '未指定'}`,
    evidence: g.evidence,
    status: 'verified' as const,
    severity: 'high' as const,
  });
}

return {
  conclusion: finalPass
    ? `GUI-LINEAGE-KB 八线提取完成并通过 G1–G8：八条线共 ${LINES.reduce((n, l) => n + lineResults[l].roundsCovered, 0)} 个自有轮（块坐标）全部有脉络与发现记录，` +
      `D3 资产归宿由 CROSS-FEED.md 逐条给出，KB-INDEX.md 为总入口；审计员 G3 抽样 ${auditResult.g3.verbatimMatched}/${auditResult.g3.sampled} 个判词逐字命中。` +
      '提交范围仅 wflow-lineage/，未 push。'
    : `GUI-LINEAGE-KB 未通过全部门禁，不宣称完成：终门机验 exit=${finalGapCount}，未结缺口 ${finalGaps.length} 项，` +
      `审计未过门 ${auditResult.gates.filter((g) => g.verdict === 'FAIL').map((g) => g.gate).join('、') || '无'}。` +
      '未完成节点与恢复入口见 AUDIT.md 与 ledger，移交研究发起人裁定。',
  findings,
  verified: [
    `wflow-lineage/tools/build_scope.py 重建范围表（exit ${rebuilt.exitCode}），确认八份导出与 QA 树未被改动`,
    `wflow-lineage/tools/check_lineage.py --json 在补轮循环、综合后、终门三处运行（末次 exit ${finalGapCount}），门禁结论以其退出码与 JSON 为准`,
    `G3 判词逐字抽样由独立审计员用种子 ${auditResult.g3.seed} 复跑：${auditResult.g3.verbatimMatched}/${auditResult.g3.sampled}`,
  ],
  notCovered: [
    '裁决#3 的 124 轮逐轮身份未重算——该口径定义在 raw rollout 上，本任务禁止读 ~/.codex 下的原始 JSONL，故逐轮只用 QA 块坐标 round，124 只作分线总数并列引用（ledger PRE-4 裁定条目）',
    'G4/G5 的语义部分（每条资产是否真有归宿＋一句理由、每个 carried 落点是否真承载该判词）由审计员读原文判断，机验只给下界',
    `语料固有缺口：导出缺文轮与 ${scope.invisible_turns_total} 个不可见用户轮无法覆盖，已登记为 R-9 而非 agent 失职`,
  ],
};
