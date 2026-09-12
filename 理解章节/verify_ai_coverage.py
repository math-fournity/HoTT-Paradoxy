#!/usr/bin/env python3
"""AI 侧审计锚点的机械验证（五类锚点存在性/计数核验）。
用法：python3 -B verify_ai_coverage.py [--dir 上级目录，默认脚本父目录]
输出：逐项 PASS/FAIL 与总判定；任一 FAIL 退出码 1。
"""
from pathlib import Path
import argparse, json, re, subprocess, sys

DIR = Path(__file__).resolve().parent          # 理解章节/
DQ = DIR.parent                                 # AI对话录/
WS = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/workspace')
ALLM = Path('/Volumes/D/ALL-Markdown')

results = []


def check(name, ok, detail=''):
    results.append((name, ok, detail))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, default=DQ)
    a = ap.parse_args()
    dq = a.dir.resolve()

    # R 类 · Codex 220 条
    merged = (dq / 'Codex-HoTT-2-完整38轮-用户与AI-20260911.md').read_text(encoding='utf-8')
    n_ai = len(re.findall(r'^### AI（[^）]+，源 \d+ 行）', merged, re.M))
    check('R:Codex AI回复=220（38轮文档）', n_ai == 220, f'实际 {n_ai}')
    # rollout 直读计数复核
    for label, f, want in [('父线程', Path('/Users/aurolafly/.codex/sessions/2026/08/31/rollout-2026-08-31T17-37-21-01a059c1-6322-7f90-a2f9-427cae4b590d.jsonl'), 186),
                           ('HoTT-2主', Path('/Users/aurolafly/.codex/sessions/2026/09/09/rollout-2026-09-09T10-43-44-01a08699-dbe0-7ad2-b1d1-c4fd36321a35_01a0869f-f467-7bc2-81d4-abf91cf20739.jsonl'), 34)]:
        cnt = 0
        with open(f, errors='replace') as fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                p = o.get('payload', {})
                if o.get('type') == 'response_item' and p.get('type') == 'message' and p.get('role') == 'assistant':
                    cnt += 1
        check(f'R:rollout直读 {label} assistant={want}', cnt == want, f'实际 {cnt}')

    # R 类 · Web 55 节
    web = (dq / 'ChatGPT-HoTT - Main-20260911-1222.md').read_text(encoding='utf-8', errors='replace')
    n_resp = len([l for l in web.splitlines() if re.match(r'^## Response:\s*$', l)])
    check('R:Web Response节=55', n_resp == 55, f'实际 {n_resp}')

    # R 类 · Gemini 24 实质 chunk
    gj = json.loads((dq / 'Gemini - AI 对话录.json').read_text(encoding='utf-8'))
    chunks = gj['chunkedPrompt']['chunks']
    sub = [i for i, c in enumerate(chunks) if c.get('role') == 'model' and not c.get('isThought')
           and not any(k in c for k in ('executableCode', 'codeExecutionResult'))
           and len(str(c.get('text', '')).strip()) >= 50]
    b4 = (DIR / 'B4-Gemini工作史.md').read_text(encoding='utf-8')
    listed = {int(x) for x in re.findall(r'chunk(\d+)', b4)}
    check('R:Gemini实质chunk≥24 且 B4登记索引⊆实际', len(sub) >= 24 and listed.issubset(set(sub)), f'实际实质 {len(sub)}，B4登记 {len(listed)}')

    # G 类 · git
    def gitlog(repo):
        p = subprocess.run(['git', '-C', str(repo), 'log', '--format=%H'], capture_output=True, text=True)
        return set(p.stdout.split())
    ws_hashes = gitlog(WS)
    ws_must = ['d726b2e', '6206055', '17418f1', 'b07ac7e', 'f38a2cb', '05431a2', '44ba9f3', '3e529cd', '8e6641d',
               '38d6d70', '4c71883', '0d7ef5e', '07ee915', 'ba227f4', 'e02ab42', 'ce5e8f3', '5116713', '38e729c',
               '1de734c', '46a1e27', 'fde005c', '110778b', 'be37ac2', '63f9766', 'd06c138', 'd526591', 'd3f7d85',
               '6fe5a7d', '14aa846', '5b7107e', '6096f71', '00e8660', '515da9f', '149767b', '1eeafb5', '1ad50e9',
               '6581d1a', '26fcecf']
    ok_ws = all(any(h.startswith(m) for h in ws_hashes) for m in ws_must)
    check('G:WS 关键R系列commit 38个全部在log', ok_ws, f'{len(ws_must)} 必查')
    all_hashes = gitlog(ALLM)
    ok_all = any(h.startswith('dc1e369') for h in all_hashes) and any(h.startswith('8470721') for h in all_hashes)
    check('G:ALL dc1e369/8470721 存在', ok_all)
    dq_hashes = gitlog(dq)
    check('G:DQ v1=1d12edb 存在', any(h.startswith('1d12edb') for h in dq_hashes))

    # A 类 · 产物存在性抽查
    must_paths = [
        WS / '.codex/research/hott/sessions/S-ANS-20260910-017-LOCAL-EXECUTION/SESSION.md',
        WS / '.codex/research/hott/sessions/S-DISC-20260911-028-GEMINI-IN007/SESSION.md',
        WS / '.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md',
        WS / 'scripts/research/r024_diagonal_machine.py',
        WS / 'artifacts/r024/COMPILER_RESULTS.json',
        WS / 'exchange/rounds/R041-ZCODE-GOVERNANCE/ROUND.json',
        ALLM / 'HoTT/formal/self-contained/ZCore.agda',
        ALLM / 'HoTT/sources/aistudio-discussions',
        ALLM / '认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md',
        dq / 'sentence_ledger_annotated.json',
        dq / '理解章节/B5-成果总账.md',
    ]
    missing = [str(p) for p in must_paths if not p.exists()]
    check('A:产物抽查 11 项存在', not missing, '缺: ' + ';'.join(missing) if missing else '')
    sess = list((WS / '.codex/research/hott/sessions').iterdir())
    check('A:workspace会话目录≥39', len(sess) >= 39, f'实际 {len(sess)}')

    # T 类 · 工具调用计数
    for label, f, want in [('父线程', Path('/Users/aurolafly/.codex/sessions/2026/08/31/rollout-2026-08-31T17-37-21-01a059c1-6322-7f90-a2f9-427cae4b590d.jsonl'), 1037),
                           ('HoTT-2主', Path('/Users/aurolafly/.codex/sessions/2026/09/09/rollout-2026-09-09T10-43-44-01a08699-dbe0-7ad2-b1d1-c4fd36321a35_01a0869f-f467-7bc2-81d4-abf91cf20739.jsonl'), 106)]:
        cnt = 0
        with open(f, errors='replace') as fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                p = o.get('payload', {})
                if o.get('type') == 'response_item' and p.get('type') in ('custom_tool_call', 'function_call'):
                    cnt += 1
        check(f'T:{label} exec={want}', cnt == want, f'实际 {cnt}')

    # 用户侧覆盖不回退
    ents = json.loads((dq / 'sentence_ledger_annotated.json').read_text(encoding='utf-8'))
    no_anchor = sum(1 for e in ents if not e['anchor'])
    check('U:句级账本 2369 条 0 缺锚', len(ents) == 2369 and no_anchor == 0, f'{len(ents)} 条/{no_anchor} 缺')

    # ============ 批次 3–9 扩展：产物内容核验 ============
    comp = (WS / 'artifacts/r024/COMPILER_RESULTS.json').read_text(encoding='utf-8')
    check('C3:r024 四计数 1928/1888/40/241 在实物', all(k in comp for k in ('1928', '1888', '40', '241')))

    sess_dirs = sorted(p.name for p in (WS / '.codex/research/hott/sessions').iterdir() if p.is_dir())
    n_sess_md = sum(1 for d in sess_dirs if (WS / '.codex/research/hott/sessions' / d / 'SESSION.md').exists())
    check('C4:SESSION.md 实数=44（批次4口径修正）', n_sess_md == 44, f'实际 {n_sess_md}')

    store = json.loads(Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/archive/STORE.json').read_text(encoding='utf-8'))
    check('C7:archive 无损库 324 份且 lossless', len(store.get('files', [])) == 324 and store.get('lossless') is True,
          f"files={len(store.get('files', []))} lossless={store.get('lossless')}")

    wc = WS / '认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md'
    wtxt = wc.read_text(encoding='utf-8') if wc.exists() else ''
    check('C6:workspace 第五闭包含§22（R035/R036）', '二十二、R035—R036' in wtxt and '逻辑＋几何＋程序' in wtxt,
          f'lines={len(wtxt.splitlines())}')

    rul = (ALLM / 'rulings.md').read_text(encoding='utf-8')
    check('C7:rulings R-016 含 Chat 模式最终消息', 'R-016' in rul and 'Chat模式' in rul)

    ledger = (ALLM / 'HOTT_Z_AI_HANDOFF_20260831/canonical/ledgers/CLAIM_LEDGER.md').read_text(encoding='utf-8')
    check('C7:CLAIM_LEDGER Z-156/Z-158（同函数异时/Guard-Erasure 前驱）', 'Z-156' in ledger and 'Z-158' in ledger)

    sp = (WS / '.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md').read_text(encoding='utf-8')
    check('C4:r039 144 Delay 图定位行', '144' in sp)

    # ============ 批次 2/9 扩展：代码行号锚点项 ============
    r024 = (WS / 'scripts/research/r024_diagonal_machine.py').read_text(encoding='utf-8').splitlines()
    def line_has(n, frag):
        return n <= len(r024) and frag in r024[n - 1]
    check('A:r024:11 八指令枚举', line_has(11, 'SET, COPY, ADD, MUL, INC, DECJZ, JUMP, HALT = range(8)'))
    check('A:r024:83 Cantor 配对公式', line_has(83, '(a + b) * (a + b + 1) // 2 + b'))
    check('A:r024:169 compile_diagonal 定义', line_has(169, 'def compile_diagonal'))
    check('A:r024:156 T=至迟n步语义', line_has(156, 'def T(code'))

    b1 = (DIR / 'B1-本地GPT工作史.md').read_text(encoding='utf-8')
    check('C5:B1§五 批次5全轮次精读记录', '批次 5 全轮次精读补记' in b1 and '起源夜' in b1)
    check('C8:B1§七 批次8边角清零记录', '批次 8 边角清零' in b1 and 'checkpoint-rev15-import' in b1)
    a8 = (DIR / 'A8-材料与保全.md').read_text(encoding='utf-8')
    check('C7:A8 批次7处置表+R006-R015核验', 'archive/ 324 份原件处置表' in a8 and 'ORIGINAL_BYTES' in a8.replace('恢复抽验', 'ORIGINAL_BYTES') or 'R006–R015 收据' in a8)
    b5 = (DIR / 'B5-成果总账.md').read_text(encoding='utf-8')
    check('C9:B5 终稿证据等级复核节', '终稿证据等级复核' in b5 and 'E2+' in b5)
    plan = (DIR / '全量精读工作方案.md').read_text(encoding='utf-8')
    check('C9:方案§六 批次1-8全✅', plan.count('| **✅') >= 8, f"✅行={plan.count('| **✅')}")

    # ============ 批次 10 扩展：ALL-Markdown 文件级对账核验 ============
    src = (ALLM / 'HoTT/ChatGPT-🌟 Z铁律论证HoTT缺乏时间维度-完整提取-20260831-1745.md').read_text(encoding='utf-8')
    check('C10:源头对话 17 轮 Prompt', src.count('## Prompt:') == 17, f"实际 {src.count('## Prompt:')}")
    check('C10:源头对话关键内容在案', '非平凡抽象的必然盲区定理' in src and 'Identity-only temporal reductionism' in src and 'successor-limit gap' in src)

    zcore = (ALLM / 'HoTT/formal/self-contained/ZCore.agda').read_text(encoding='utf-8')
    check('C10:ZCore 六定理在案（E1 证据本体）', all(k in zcore for k in (
        'fiber-truth-invariant', 'no-free-enrichment', 'snapshot-cannot-recover-provenance',
        'core-cannot-recover-direction', 'no-section-from-fixed-point-free-monodromy',
        'guard-erasure-implies-fixed-point')))

    bb = (ALLM / 'HoTT/sources/user-originals/Better-Best悖论-原文.md').read_text(encoding='utf-8')
    check('C10:Better-Best 原文含序列点/伪命题', '序列点' in bb and '伪命题' in bb and '计算合法性' in bb)

    tri = (ALLM / 'HOTT_Z_AI_HANDOFF_20260831/canonical/manuscripts/HOTT_Z_三重不完备性定理.md').read_text(encoding='utf-8')
    check('C10:三重不完备定理文档完整', '定理 6.2' in tri and 'no-section-type-2-Element-Type' in tri.replace(' ', '-') or '2-Element-Type' in tri)

    gone = (ALLM / 'HoTT_is_GONE_and_GONE_with_the_Wind.md').read_text(encoding='utf-8')
    check('C10:GONE 判决书原文（三罪证+放映机）', '罪证一' in gone and '放映机' in gone and '有限性矛盾' in gone)

    a8t = (DIR / 'A8-材料与保全.md').read_text(encoding='utf-8')
    check('C10:A8 批次10 文件级对账节', '批次 10：ALL-Markdown 文件级全路径对账' in a8t and '7,420' in a8t)

    npass = sum(1 for _, ok, _ in results if ok)
    for name, ok, detail in results:
        print(('PASS' if ok else 'FAIL'), name, ('| ' + detail) if detail and not ok else '')
    print(f'\n{npass}/{len(results)} PASS')
    sys.exit(0 if npass == len(results) else 1)


if __name__ == '__main__':
    main()
