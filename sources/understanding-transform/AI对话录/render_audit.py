#!/usr/bin/env python3
"""渲染《用户发言逐句审计账本》：把 sentence_ledger.json 的每句挂上作者身份与理解锚点。

作者身份三档：user（用户自写）/ relay-gpt（转发的 GPT 信件）/ relay-gemini（转发的 Gemini 回复）。
锚点指向《我的理解》文件（A0–A10，含子锚点）。规则：消息级默认 + 标记词覆盖 + 分节感知。
用法：python3 -B render_audit.py [--dir 目录]
"""
from pathlib import Path
import argparse, json, collections

DIR = Path(__file__).resolve().parent

# 消息级默认锚点与作者（key = sentence ledger 的 id 前缀）
MSG_META = {
    # Codex 38 轮（41 条用户消息）
    'C-T01-L9': 'A8', 'C-T02-L792': 'A9', 'C-T03-L815': 'A1', 'C-T04-L1761': 'A5',
    'C-T05-L1860': 'A5', 'C-T06-L2087': 'A4', 'C-T07-L2236': 'A9', 'C-T08-L2335': 'A2.2',
    'C-T09-L2415': 'A2.3', 'C-T10-L2486': 'A8', 'C-T11-L2841': 'A3', 'C-T12-L2862': 'A1',
    'C-T13-L2903': 'A2.4', 'C-T14-L2934': 'A5', 'C-T15-L2967': 'A0', 'C-T16-L3099': 'A9',
    'C-T17-L3163': 'A9', 'C-T18-L3590': 'A8', 'C-T19-L3754': 'A8', 'C-T20-L4641': 'A8',
    'C-T21-L4759': 'A8', 'C-T22-L5121': 'A0', 'C-T23-L5239': 'A1', 'C-T24-L5593': 'A1',
    'C-T25-L6159': 'A1', 'C-T26-L6543': 'A2', 'C-T27-L6763': 'A2.2', 'C-T28-L7074': 'A1',
    'C-T29-L7105': 'A1', 'C-T30-L10': 'A0', 'C-T31-L157': 'A8', 'C-T32-L409': 'A1.3',
    'C-T33-L440': 'A1.3', 'C-T34-L525': 'A5', 'C-T35-L548': 'A5', 'C-T36-L570': 'A8',
    'C-T37-L687': 'A8', 'C-T38-L757': 'A9', 'C-T38-L775': 'A9',
    # Web 56 条用户 Prompt
    'W-01': 'A9', 'W-02': 'A8', 'W-03': 'A9', 'W-04': 'A9', 'W-05': 'A8', 'W-06': 'A8',
    'W-07': 'A9', 'W-08': 'A0', 'W-09': 'A9', 'W-10': 'A9', 'W-11': 'A9', 'W-12': 'A9',
    'W-13': 'A0', 'W-14': 'A9', 'W-15': 'A9', 'W-16': 'A9', 'W-17': 'A10', 'W-18': 'A2',
    'W-19': 'A5', 'W-20': 'A10', 'W-21': 'A10', 'W-22': 'A0', 'W-23': 'A10', 'W-24': 'A10',
    'W-25': 'A10', 'W-26': 'A4', 'W-27': 'A3', 'W-28': 'A3', 'W-29': 'A10', 'W-30': 'A10',
    'W-31': 'A9', 'W-32': 'A9', 'W-33': 'A8', 'W-34': 'A8', 'W-35': 'A6', 'W-36': 'A6',
    'W-37': 'A6', 'W-38': 'A6', 'W-39': 'A6', 'W-40': 'A6', 'W-41': 'A6', 'W-42': 'A6',
    'W-43': 'A6', 'W-44': 'A5', 'W-45': 'A5', 'W-46': 'A10', 'W-47': 'A10', 'W-48': 'A10',
    'W-49': 'A10', 'W-50': 'A10', 'W-51': 'A5', 'W-52': 'A10', 'W-53': 'A10', 'W-54': 'A10',
    'W-55': 'A9', 'W-56': 'A9',
    # Gemini 22 条
    'G-01': 'A8', 'G-02': 'A0', 'G-03': 'A3', 'G-04': 'A10', 'G-05': 'A10', 'G-06': 'A1',
    'G-07': 'A2.2', 'G-08': 'A1', 'G-09': 'A0', 'G-10': 'A10', 'G-11': 'A3', 'G-12': 'A0',
    'G-13': 'A4', 'G-14': 'A6.1', 'G-15': 'A6.2', 'G-16': 'A6.3', 'G-17': 'A6.4',
    'G-18': 'A6.5', 'G-19': 'A6.6', 'G-20': 'A5', 'G-21': 'A5', 'G-22': 'A6.7',
}

# 整条消息为转发（GPT 信件）的 id 前缀
FULL_RELAY = {'G-14', 'G-15', 'G-16', 'G-17', 'G-18', 'G-19', 'G-22'}

# 混合消息：从标记词起进入转发区（之后全部 relay-gemini）
RELAY_FROM_MARKER = {
    'W-38': ('致 OUT-002', 'relay-gemini'),
    'W-39': ('致 OUT-002', 'relay-gemini'),
    'W-40': ('**结论：**', 'relay-gemini'),
    'W-42': ('致 OUT-005', 'relay-gemini'),
    'W-43': ('致 OUT-006', 'relay-gemini'),
}

# 混合消息：仅这些开头的句是用户自写，其余为转发
OWN_ONLY_MARKERS = {
    'W-44': ('本来我觉得', 'HoTT难道', '现在，Astra', '我：', 'Gemini，你的看法', 'Gemini:'),
    'W-45': ('本来我觉得', 'HoTT难道', '现在，Astra', '我：', 'Gemini，你的看法', 'Gemini:'),
}

# G-12 任务书的分节锚点（按最近一次出现的节标记分派）
G12_SECTIONS = [
    ('一、我们真正想找什么', 'A0'), ('二、必须同时保留两个方向', 'A3'), ('三、ASK究竟是什么意思', 'A3'),
    ('四、历史例子提供的是机制启发', 'A2'), ('五、此前已经做过什么', 'A6'), ('六、当前最值得你帮助推进的方向', 'A10'),
    ('七、你应怎样使用HoTT知识与Theory Schema', 'A8'), ('八、怎样既保持创造性', 'A7'),
    ('九、这次希望你交付的内容', 'A10'), ('十、让你的输出能够被后续研究吸收', 'A9'),
]

ANCHOR_DESC = {
    'A0': '总目标：在找什么（双向/非内部矛盾/最优雅形态/过程结论现象谱）',
    'A1': 'Z铁律：抽象=否定/前提改变结论改变/X≠Y/否定分层',
    'A1.3': '合取（联言）命题：现实事件=条件全真；理论替换合取项；悖论=反证法信号',
    'A2': '参照悖论谱（A2.1芝诺合取反证法；A2.2罗素假集合非法程序；A2.3 Better Best；A2.4圆环；A2.5 shenchensh与Matrix量子化；A2.6说谎者）',
    'A3': 'ASK 计算合法性：定义/两类方向/依据被略过替换扩大加强',
    'A4': '时间维度：四层区分/工作维度vs对象/程序对照/不想让时间参与思考',
    'A5': '对HoTT的怀疑与演进：核心怀疑→分层裁决→逻辑+几何+程序继承计算不完备/自指不可越过',
    'A6': 'Gemini论辩收获（A6.1-A6.7七封信：过度认领教训/RP-B01/缠绕数/提取接口/正向对照/收敛）',
    'A7': '认识纪律：philosophy-first/训练数据是历史prior/先内部重建再外部比较/不预设对错',
    'A8': '材料与保全：原文非摘要/语料完备性/外部AI审计/Theory Schema',
    'A9': '工作治理：闭包/Skill/MEMORY/代码保全/统计口径/交接工程',
    'A10': '怎么找：先验模式匹配/成对证据/承诺归属/恢复条件/机器验证/自主推进',
}


def msg_key(e):
    return e['id'].split('-S')[0].split('-R')[0].split('-ATT')[0]


def annotate(entries):
    for e in entries:
        key = msg_key(e)
        author = 'user'
        anchor = MSG_META.get(key, 'A9')
        if e['block'] == 'platform':
            author = 'platform'
        elif e['block'] in ('relay', 'attachment', 'ai_response'):
            author = {'relay': 'relay', 'attachment': 'user', 'ai_response': 'ai'}[e['block']]
            if e['block'] == 'relay':
                author = 'relay'
                anchor = MSG_META.get(key, 'A6')
        elif key in FULL_RELAY:
            author = 'relay-gpt'
        elif key in RELAY_FROM_MARKER and e['block'] == 'own':
            marker, role = RELAY_FROM_MARKER[key]
            if marker in e['text']:
                e['_in_relay'] = True
            if e.get('_in_relay'):
                author = role
        elif key in OWN_ONLY_MARKERS and e['block'] == 'own':
            if not any(e['text'].startswith(m) for m in OWN_ONLY_MARKERS[key]):
                author = 'relay-gemini'
        if key == 'G-12' and e['block'] == 'own':
            anchor = anchor_for_g12(e['text'], getattr(annotate, '_g12_cur', 'A0'))
        e['author'] = author
        e['anchor'] = anchor
    # 第二遍处理 RELAY_FROM_MARKER 的延续（标记句之后保持 relay）
    active = {}
    for e in entries:
        key = msg_key(e)
        if key in RELAY_FROM_MARKER and e['block'] == 'own':
            marker, role = RELAY_FROM_MARKER[key]
            if active.get(key):
                e['author'] = role
            if marker in e['text']:
                active[key] = True
                e['author'] = role
    return entries


def anchor_for_g12(text, current):
    for header, anchor in G12_SECTIONS:
        if text.startswith(header) or header in text[:len(header) + 4]:
            annotate._g12_cur = anchor
            return anchor
    return current


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, default=DIR)
    a = ap.parse_args()
    d = a.dir.resolve()
    data = json.load(open(d / 'sentence_ledger.json', encoding='utf-8'))
    entries = annotate(data['entries'])
    # 验证
    missing = [e['id'] for e in entries if not e['anchor']]
    assert not missing, f'缺锚点: {missing[:5]}'
    stats = collections.Counter()
    for e in entries:
        stats[f"{e['src']}:{e['block']}"] += 1
        stats['author:' + e['author']] += 1
    # 渲染账本
    out = ['# 用户发言逐句审计账本（三份对话录 · 38+111+22 遍历单元）\n']
    out.append('> 生成：render_audit.py（规则见表头）；锚点指向《我的理解-悖论与HoTT悖论捕捉-20260911.md》。')
    out.append('> 作者身份：user=用户自写；relay-gpt=用户转发的GPT信件；relay-gemini=用户转发的Gemini回复；relay=围栏转述块。\n')
    cur_unit = None
    for e in entries:
        key = msg_key(e)
        if key != cur_unit:
            cur_unit = key
            src_name = {'codex': 'Codex', 'web': 'ChatGPT网页', 'gemini': 'Gemini'}[e['src']]
            out.append(f"\n## {src_name} · {key}\n")
        t = e['text'].replace('\n', ' ')
        if len(t) > 160:
            t = t[:160] + '…'
        out.append(f"- `{e['id']}` [{e['author']}] → **{e['anchor']}** ｜ {t}")
    (d / '用户发言逐句审计账本-20260911.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    json.dump(entries, open(d / 'sentence_ledger_annotated.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(json.dumps({'total_entries': len(entries), 'missing_anchor': len(missing),
                      'stats': dict(stats)}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
