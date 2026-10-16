#!/usr/bin/env python3
"""按官方 App 语义提取 HoTT-2 线程的完整 38 轮对话（用户消息 + AI 回复）。

结构依据（2026-09-11 官方对账）：
  - 轮次 turn = 一条真实用户消息及其后的 AI 回复（官方 thread_history 语义；
    机器注入 <skills_instructions>/<multi_agent_role>/<environment_context>/AGENTS 指令等
    是 contextual user messages，计入轮内上下文脚注，不算轮、不算用户消息）。
  - 合并视图 = 父线程全部 29 轮（第 29 轮"三问"被 <turn_aborted> 中断）
    + HoTT-2 主文件 9 轮（"三问"重发并完成）= 38 轮，与用户 App 界面计数一致。
  - AI 回复 = response_item/message/role=assistant（event_msg agent_message 通道为 0，
    已核验无重复）。
用法：python3 -B extract_merged_thread.py [--dir 目录]
"""
from pathlib import Path
import argparse, datetime, hashlib, json, re

DIR = Path(__file__).resolve().parent
PARENT = '/Users/aurolafly/.codex/sessions/2026/08/31/rollout-2026-08-31T17-37-21-01a059c1-6322-7f90-a2f9-427cae4b590d.jsonl'
ROOTF = '/Users/aurolafly/.codex/sessions/2026/09/09/rollout-2026-09-09T10-37-05-01a08699-dbe0-7ad2-b1d1-c4fd36321a35.jsonl'
MAIN = '/Users/aurolafly/.codex/sessions/2026/09/09/rollout-2026-09-09T10-43-44-01a08699-dbe0-7ad2-b1d1-c4fd36321a35_01a0869f-f467-7bc2-81d4-abf91cf20739.jsonl'
OUT = 'Codex-HoTT-2-完整38轮-用户与AI-20260911.md'

TAG = re.compile(r'^\s*<[a-zA-Z_][a-zA-Z0-9_-]*(\s|>)')
MACHINE_PREFIXES = ('# AGENTS.md instructions for', 'Caveat:')
WRAPPER_NAMES = {'<skills_instructions': 'skills 指令', '<multi_agent_role': '多代理角色',
                 '<multi_agent_mode': '多代理模式', '<environment_context': '环境上下文',
                 '<recommended_plugins': '插件推荐', '<user_instructions': '用户指令',
                 '<codex_internal_context': '内部目标上下文', '<turn_aborted': '轮中断标记'}


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def classify(text):
    if not text.strip() or text.startswith(MACHINE_PREFIXES):
        return 'machine'
    if TAG.match(text):
        return 'machine'
    return 'real'


def wrapper_label(text):
    for k, v in WRAPPER_NAMES.items():
        if text.lstrip().startswith(k):
            return v
    return '上下文注入'


def parse_turns(path):
    """按官方 turn_context 段切轮：每段含≥1条真实用户消息才算一轮；
    纯机器注入段并入下一轮的上下文脚注（官方 thread_history 的 29/9 轮语义）。"""
    turns = []
    stats = {'assistant': 0, 'user_real': 0, 'machine': 0}
    pending_ctx = []
    cur = None

    def flush():
        nonlocal cur, pending_ctx
        if cur is not None and (cur['user'] or cur['ai']):
            turns.append(cur)
        elif cur is not None:
            for note in cur['ctx']:
                pending_ctx.append(note)
        cur = None

    with open(path, encoding='utf-8', errors='replace') as f:
        for lineno, line in enumerate(f, 1):
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            t, p = o.get('type'), o.get('payload', {})
            ts = o.get('timestamp', '')
            if t == 'turn_context':
                flush()
                cur = {'user': [], 'ai': [], 'ctx': list(pending_ctx), 'aborted': False}
                pending_ctx = []
                continue
            if cur is None:
                cur = {'user': [], 'ai': [], 'ctx': [], 'aborted': False}
            if t == 'response_item' and p.get('type') == 'message':
                role = p.get('role')
                text = ''.join(c.get('text', '') for c in p.get('content', []) if isinstance(c, dict))
                if role == 'user':
                    if classify(text) == 'real':
                        stats['user_real'] += 1
                        cur['user'].append((lineno, ts, text.rstrip('\n')))
                    else:
                        stats['machine'] += 1
                        cur['ctx'].append(f'（上下文注入：{wrapper_label(text)}，源第 {lineno} 行，不显示为用户消息）')
                elif role == 'assistant':
                    stats['assistant'] += 1
                    cur['ai'].append((lineno, ts, text.rstrip('\n')))
                elif role == 'developer' and '<turn_aborted>' in text:
                    cur['aborted'] = True
            if t == 'event_msg' and p.get('type') == 'turn_aborted':
                cur['aborted'] = True
    flush()
    return turns, stats


def render_turn(out, idx, origin, turn):
    flags = ' 【该轮被中断】' if turn['aborted'] else ''
    head = f'## 第 {idx} 轮 · {origin}{flags}\n'
    out.append(head)
    for c in turn['ctx']:
        out.append(f'> {c}\n\n')
    for lineno, ts, text in turn['user']:
        out.append(f'### 用户（{ts}，源 {lineno} 行）\n\n')
        body = text if text.endswith('\n') else text + '\n'
        out.append(body + '\n')
    for lineno, ts, text in turn['ai']:
        out.append(f'### AI（{ts}，源 {lineno} 行）\n\n')
        body = text if text.endswith('\n') else text + '\n'
        out.append(body + '\n')
    out.append('\n---\n\n')


def fold_ai_only(turns):
    """把'无用户消息但有AI内容'的段折叠进前一轮（官方 App 不为其单开一轮）。"""
    merged = []
    for turn in turns:
        if turn['user'] or not turn['ai']:
            merged.append(turn)
        elif merged:
            merged[-1]['ctx'].append('（本轮后另有仅由上下文注入触发的 AI 输出，已并入本轮末尾）')
            merged[-1]['ai'].extend(turn['ai'])
            if turn['aborted']:
                merged[-1]['aborted'] = True
        else:
            merged.append(turn)
    return merged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, default=DIR)
    a = ap.parse_args()
    d = a.dir.resolve()
    now = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z')
    pt, ps = parse_turns(PARENT)
    pt = fold_ai_only(pt)
    rt, rs = parse_turns(ROOTF)
    rt = fold_ai_only(rt)
    mt, ms = parse_turns(MAIN)
    mt = fold_ai_only(mt)
    parent_user_turns = [x for x in pt if x['user']]
    main_user_turns = [x for x in mt if x['user']]
    out = []
    out.append('# Codex HoTT-2 线程 · 完整 38 轮对话（用户消息 + AI 回复）\n\n')
    out.append(f'- 结构＝官方 App 合并视图：父线程"🌟 HoTT"全部轮次（含被中断的"三问"轮）+ HoTT-2 主文件轮次；'
               f'fork 点在父线程 ordinal 7448（三问轮之前）。"三问"出现两次：父线程中断版 + HoTT-2 完成版。\n')
    out.append(f'- 父线程：`{PARENT}`（SHA-256 `{sha_file(Path(PARENT))}`）\n')
    out.append(f'- HoTT-2 主文件：`{MAIN}`（SHA-256 `{sha_file(Path(MAIN))}`）\n')
    out.append(f'- 轮次口径＝一条真实用户消息开起一轮（机器注入不算轮）；AI 回复＝response_item/role=assistant 全文。\n')
    total_parent = len(parent_user_turns)
    total_main = len(main_user_turns)
    out.append(f'- 轮数：父线程 {total_parent} + HoTT-2 主 {total_main} = **{total_parent + total_main} 轮**；'
               f'用户消息 {ps["user_real"]}+{ms["user_real"]}={ps["user_real"] + ms["user_real"]} 条；'
               f'AI 回复 {ps["assistant"]}+{ms["assistant"]}={ps["assistant"] + ms["assistant"]} 条；'
               f'机器注入 {ps["machine"]}+{ms["machine"]} 条（不计入）。\n')
    out.append(f'- 提取工具：`extract_merged_thread.py`；时间：{now}\n\n---\n\n')
    idx = 0
    for turn in pt:
        if not turn['user'] and not turn['ai']:
            continue
        idx += 1
        render_turn(out, idx, '父线程 🌟 HoTT', turn)
    for turn in mt:
        if not turn['user'] and not turn['ai']:
            continue
        idx += 1
        render_turn(out, idx, 'HoTT-2 主文件', turn)
    # 附录：root fork 文件的中断尝试（不计入38轮，谱系完整性保留）
    root_user = [x for x in rt if x['user']]
    if root_user:
        out.append('\n# 附录 · HoTT-2 根文件（fork 基干）的轮次（不计入 38 轮）\n\n')
        out.append(f'- 文件：`{ROOTF}`（SHA-256 `{sha_file(Path(ROOTF))}`）；用户消息 {rs["user_real"]} 条、AI 回复 {rs["assistant"]} 条。\n\n')
        for j, turn in enumerate(root_user, 1):
            render_turn(out, f'A{j}', 'HoTT-2 根文件', turn)
    (d / OUT).write_text(''.join(out), encoding='utf-8')
    summary = {'output': OUT, 'parent_turns': total_parent, 'main_turns': total_main,
               'total_turns': total_parent + total_main,
               'user_messages': ps['user_real'] + ms['user_real'],
               'ai_replies': ps['assistant'] + ms['assistant'],
               'machine_injections': ps['machine'] + ms['machine'],
               'root_appendix_turns': len(root_user),
               'bytes': (d / OUT).stat().st_size}
    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
