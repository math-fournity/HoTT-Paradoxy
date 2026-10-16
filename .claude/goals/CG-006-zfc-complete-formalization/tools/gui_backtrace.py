#!/usr/bin/env python3
"""Backward skeleton of one GUI conversation line, from its last own turn back to its fork.

usage: python3 gui_backtrace.py <branch> [--from N] [--to M] [--head 260] [--user 320]

Reads the QA tree (audit/GUI-SYNTH-REDO/qa/<branch>/NNNN.md, a machine export of the raw
rollouts with GUI-visible content only).  Per turn it prints, newest first:
  U  the user's request (response-annotation boilerplate reduced to the request and the
     selected snippets; /goal continuation and app/environment blocks marked, not expanded);
  F  the opening of GPT's last answer in that turn (whitespace collapsed);
  T  SOP / goal names, verdict tokens and claim IDs that occur in that last answer.
Text is cut, never rewritten.  GPT's answers are self-reports, not evidence.
CG-006 (session d58e0c0d), 2026-10-08.
"""
import argparse
import json
import os
import re

QA = os.path.join(os.path.dirname(__file__), "../../../../audit/GUI-SYNTH-REDO/qa")
SOP_RE = re.compile(r"\b[A-Z][A-Z0-9]+(?:-[A-Z0-9]+){2,}\b")
VERDICT_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+){2,}\b")
CLAIM_RE = re.compile(r"\b(?:CG001-)?C-\d{2,3}\b|\bF-0\d\d\b")


def blocks(text):
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    parts = re.split(r"(?m)^(## User|## Codex|### Files changed in this reply)\s*$", body)
    out, cur = [], None
    for p in parts:
        if p in ("## User", "## Codex", "### Files changed in this reply"):
            cur = [p, ""]
            out.append(cur)
        elif cur is not None:
            cur[1] += p
    return out


def flat(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + "…"


def user_request(u, n):
    u = re.sub(r"<external_codex_apps_open_page>.*?</external_codex_apps_open_page>", "", u, flags=re.S)
    u = re.sub(r"<environment_context>.*?</environment_context>", "", u, flags=re.S)
    tags = []
    g = re.search(r'<codex_internal_context source="goal">(.*?)(?:</codex_internal_context>|\Z)', u, re.S)
    if g:
        obj = re.search(r"(?:objective|Objective|目标)[^\n:：]*[:：]\s*(.+)", g.group(1))
        tags.append("[goal 续跑]" + (" 目标：" + flat(obj.group(1), 140) if obj else ""))
        u = u.replace(g.group(0), "")
    if "<response-annotations>" in u:
        sel = re.findall(r'"text":"(.*?)","source"', u, re.S)
        req = u.split("## My request:", 1)[1] if "## My request:" in u else ""
        tags.append("[批注 " + str(len(sel)) + "] " + " / ".join(flat(x, 70) for x in sel[:3]))
        u = req
    u = flat(u, n)
    return (" ".join(tags) + " " + u).strip() or "(空)"


def tokens(final):
    seen = []
    for rx in (SOP_RE, VERDICT_RE, CLAIM_RE):
        for m in rx.findall(final):
            if m not in seen and not m.startswith(("HTTP", "UTF-8", "SHA-256")):
                seen.append(m)
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("branch")
    ap.add_argument("--from", dest="lo", type=int, default=1)
    ap.add_argument("--to", dest="hi", type=int, default=10**6)
    ap.add_argument("--head", type=int, default=260)
    ap.add_argument("--user", type=int, default=320)
    ap.add_argument("--max-tokens", type=int, default=14)
    a = ap.parse_args()
    d = os.path.join(QA, a.branch)
    fork = json.load(open(os.path.join(d, "_branch.json"), encoding="utf-8")).get("fork")
    docs = sorted((f for f in os.listdir(d) if re.fullmatch(r"\d{4}\.md", f)), reverse=True)
    print(f"# {a.branch} backward skeleton ({len(docs)} own turns); fork: "
          + (f"{fork['parent_branch']}#{fork['parent_doc']}" if fork else "root"))
    for f in docs:
        n = int(f[:4])
        if not (a.lo <= n <= a.hi):
            continue
        bl = blocks(open(os.path.join(d, f), encoding="utf-8").read())
        users = "\n".join(b[1] for b in bl if b[0] == "## User")
        codex = [b[1] for b in bl if b[0] == "## Codex"]
        final = codex[-1] if codex else ""
        print(f"\n#{n:04d} U: {user_request(users, a.user)}")
        print(f"  F: {flat(final, a.head)}")
        t = tokens(final)
        if t:
            print("  T: " + ", ".join(t[: a.max_tokens]) + (f" (+{len(t) - a.max_tokens})" if len(t) > a.max_tokens else ""))


if __name__ == "__main__":
    main()
