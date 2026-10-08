#!/usr/bin/env python3
"""CG-006: find prior GPT work in the eight GUI conversation records.

Sources, first available wins:
  1. QA-tree export  audit/GUI-SYNTH-REDO/qa/<branch>/NNNN.md   (one doc per user turn; each branch
     folder holds only that line's own turns, i.e. post-fork; dev-08 is the trunk)
  2. Verbatim digests  .claude/goals/CG-006-zfc-complete-formalization/gui-digests/*.md
     (post-fork user turns + final answers, cut from source 1 on 2026-10-08)
  3. GUI exports  git-worktree对话录/*.md  (committed; whole conversations incl. shared prefix)

Usage:
  gui_find.py KEYWORD [KEYWORD ...] [--branch dev-03] [--roles USER,FINAL] [--max 6] [--context 1]
      every keyword must occur in the turn (case-insensitive); prints branch/turn, role and matching lines
  gui_find.py --show dev-08/0112            print the user turn and the final answer of one turn
  gui_find.py --list dev-03                 one line per turn: number, user text head, final head

Roles: USER = research initiator's words; FINAL = GPT's last answer of the turn; MID = progress notes.
GPT's answers are self-reports, not evidence: check the cited files with `git show <ref>:<path>`.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(PKG, '..', '..', '..'))
QA = os.path.join(ROOT, 'audit', 'GUI-SYNTH-REDO', 'qa')
DIG = os.path.join(PKG, 'gui-digests')
GUI = os.path.join(ROOT, 'git-worktree对话录')
MARK = re.compile(r'(?m)^(## User|## Codex|### Files changed in this reply)\s*$')


def split_blocks(text):
    body = text.split('\n---\n', 1)[1] if text.startswith('---') else text
    out, cur = [], None
    for part in MARK.split(body):
        if part in ('## User', '## Codex', '### Files changed in this reply'):
            cur = [part, '']
            out.append(cur)
        elif cur is not None:
            cur[1] += part
    codex = [i for i, b in enumerate(out) if b[0] == '## Codex']
    roles = []
    for i, b in enumerate(out):
        if b[0] == '## User':
            roles.append(('USER', b[1]))
        elif b[0] == '## Codex':
            roles.append(('FINAL' if codex and i == codex[-1] else 'MID', b[1]))
        else:
            roles.append(('FILES', b[1]))
    return roles


def qa_turns(branch):
    for br in sorted(os.listdir(QA)):
        d = os.path.join(QA, br)
        if br.startswith('_') or not os.path.isdir(d) or (branch and br != branch):
            continue
        for f in sorted(os.listdir(d)):
            if re.fullmatch(r'\d{4}\.md', f):
                with open(os.path.join(d, f), encoding='utf-8') as h:
                    yield br, f[:4], split_blocks(h.read())


def digest_turns(branch):
    for f in sorted(os.listdir(DIG)):
        if not f.endswith('.md') or f == 'README.md':
            continue
        with open(os.path.join(DIG, f), encoding='utf-8') as h:
            text = h.read()
        for chunk in re.split(r'(?m)^========== ', text)[1:]:
            m = re.match(r'(\S+)/(\d{4})\.md', chunk)
            if not m or (branch and m.group(1) != branch):
                continue
            u = re.search(r'### USER\n(.*?)\n### FINAL', chunk, flags=re.S)
            fin = re.search(r'### FINAL\n(.*?)(?=\n## 附录|\Z)', chunk, flags=re.S)
            yield m.group(1), m.group(2), [('USER', u.group(1) if u else ''), ('FINAL', fin.group(1) if fin else '')]


def turns(branch):
    if os.path.isdir(QA):
        return 'qa', qa_turns(branch)
    if os.path.isdir(DIG):
        return 'digests', digest_turns(branch)
    return 'gui', None


def grep_gui(keys, ctx, maxn):
    for f in sorted(os.listdir(GUI)):
        if not f.endswith('.md') or f == 'README.md':
            continue
        lines = open(os.path.join(GUI, f), encoding='utf-8').read().split('\n')
        hits = [i for i, l in enumerate(lines) if all(k.lower() in l.lower() for k in keys)]
        for i in hits[:maxn]:
            print(f'{f[:6]} L{i + 1}: ' + ' / '.join(lines[max(0, i - ctx):i + ctx + 1])[:400])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('keys', nargs='*')
    ap.add_argument('--branch')
    ap.add_argument('--roles', default='USER,FINAL,MID')
    ap.add_argument('--max', type=int, default=6, help='matching lines shown per turn')
    ap.add_argument('--context', type=int, default=0)
    ap.add_argument('--show')
    ap.add_argument('--list')
    a = ap.parse_args()
    if a.show:
        br, num = a.show.split('/')
        src, it = turns(br)
        for b, n, roles in it or []:
            if n == num.zfill(4):
                for role, text in roles:
                    if role in ('USER', 'FINAL'):
                        print(f'===== {b}/{n} {role} =====\n{text.strip()}\n')
        return
    if a.list:
        src, it = turns(a.list)
        for b, n, roles in it or []:
            u = next((t for r, t in roles if r == 'USER'), '').strip().replace('\n', ' ')
            u = re.sub(r'<codex_internal_context.*', '[goal 续跑]', u)
            f = next((t for r, t in roles if r == 'FINAL'), '').strip().replace('\n', ' ')
            print(f'{b}/{n}  U: {u[:90]}  |  F: {f[:90]}')
        return
    if not a.keys:
        ap.error('give keywords, --show or --list')
    keys = [k.lower() for k in a.keys]
    want = set(a.roles.split(','))
    src, it = turns(a.branch)
    print(f'[source: {src}]')
    if it is None:
        grep_gui(a.keys, a.context, a.max)
        return
    for b, n, roles in it:
        whole = '\n'.join(t for r, t in roles if r != 'FILES').lower()
        if not all(k in whole for k in keys):
            continue
        shown = 0
        for role, text in roles:
            if role not in want:
                continue
            lines = text.split('\n')
            for i, l in enumerate(lines):
                if any(k in l.lower() for k in keys) and shown < a.max:
                    seg = ' / '.join(x.strip() for x in lines[max(0, i - a.context):i + a.context + 1] if x.strip())
                    print(f'{b}/{n} [{role}] {seg[:300]}')
                    shown += 1
        if shown:
            print()


if __name__ == '__main__':
    sys.exit(main())
