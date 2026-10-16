#!/usr/bin/env python3
"""Private GUI transcript exporter for one ZCode Desktop session.

Reads the local ZCode session database (read-only) and writes a private
Markdown transcript containing only GUI-visible content:

  * the user's real typed messages (verbatim);
  * the assistant's visible text replies (verbatim, Markdown unchanged);
  * AskUserQuestion interactions (question, options, the user's selection).

A turn whose assistant reply failed (rate limit, cancellation, provider error)
renders the GUI-visible error notice as a marked blockquote capsule, so a
failed turn is never silently rendered as "no reply". Intermediate streaming
retry errors (StreamRecoveryDiscarded) are not user-visible failures and are
skipped with a receipt counter.

It deliberately omits reasoning, tool calls/results (other than the
AskUserQuestion capsule), system injections (todo reminders, agent listing
deltas), fork markers, context snapshots, and any credentials.

Modes:
  gui   (default) the GUI-visible transcript only;
  audit           gui content plus raw locators (message/part ids, timestamps,
                  fork origin breadcrumbs) for a bounded later audit.

Output goes only to the private ignored directory:
  ~/.zcode/trajectory-ref-exports/

stdout prints a small receipt only (paths, mode, status, counts, warnings);
never the transcript body. Exit codes: 0 ok, 2 usage/identity error.
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path.home() / ".zcode" / "cli" / "db" / "db.sqlite"
OUTPUT_DIR = Path.home() / ".zcode" / "trajectory-ref-exports"
OUTPUT_MODES = frozenset({"gui", "audit"})
TOOL_VERSION = "1.1.0"
ERROR_INTERMEDIATE_NAMES = frozenset({"StreamRecoveryDiscarded"})
ERROR_MESSAGE_MAX = 400


class ExportError(RuntimeError):
    pass


@dataclass
class MsgRow:
    id: str
    role: str
    time_created: int
    data: dict
    parts: list = field(default_factory=list)

    @property
    def is_synthetic(self) -> bool:
        meta = self.data.get("metadata") or {}
        if self.data.get("synthetic") or meta.get("synthetic"):
            return True
        return bool(meta.get("source") or self.data.get("source"))

    @property
    def source(self) -> str:
        meta = self.data.get("metadata") or {}
        return str(meta.get("source") or self.data.get("source") or "")

    def visibility(self) -> str:
        meta = self.data.get("metadata") or {}
        sem = meta.get("semantics") or self.data.get("semantics") or {}
        for cand in (
            meta.get("visibility"),
            sem.get("uiVisibility"),
            self.data.get("visibility"),
        ):
            if cand:
                return str(cand)
        return ""

    def fork_origin(self) -> dict:
        meta = self.data.get("metadata") or {}
        fo = meta.get("forkOrigin")
        return fo if isinstance(fo, dict) else {}

    @property
    def error_info(self) -> dict | None:
        err = self.data.get("error")
        if not isinstance(err, dict):
            return None
        d = err.get("data") or {}
        name = str(err.get("name") or "")
        if name in ERROR_INTERMEDIATE_NAMES:
            return None
        return {
            "name": name,
            "code": str(d.get("code") or ""),
            "message": str(d.get("message") or ""),
        }


def ts_to_local(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).astimezone().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def open_db_readonly() -> sqlite3.Connection:
    if not DB_PATH.is_file():
        raise ExportError(f"DB_NOT_FOUND:{DB_PATH}")
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def resolve_session(db: sqlite3.Connection, key: str) -> dict:
    rows = db.execute(
        "SELECT id, parent_id, project_id, workspace_id FROM session ORDER BY id"
    ).fetchall()
    by_id = {r[0]: r for r in rows}
    if key in by_id:
        hit = key
    else:
        prefix = [r[0] for r in rows if key in r[0]]
        if len(prefix) == 1:
            hit = prefix[0]
        elif not prefix:
            raise ExportError(f"SESSION_NOT_FOUND:{key}")
        else:
            raise ExportError(f"SESSION_AMBIGUOUS:{key}:{len(prefix)} matches")
    r = by_id[hit]
    return {
        "id": r[0],
        "parent_id": r[1] or "",
        "project_id": r[2] or "",
        "workspace_id": r[3] or "",
    }


def list_sessions(db: sqlite3.Connection) -> list[dict]:
    out = []
    for sid, pid, proj in db.execute(
        "SELECT id, parent_id, project_id FROM session ORDER BY id"
    ):
        n = db.execute(
            "SELECT count(*) FROM message WHERE session_id=?", (sid,)
        ).fetchone()[0]
        out.append({"id": sid, "parent_id": pid or "", "project": proj or "", "messages": n})
    return out


def load_messages(db: sqlite3.Connection, sid: str) -> list[MsgRow]:
    msgs = []
    for mid, tcre, data in db.execute(
        "SELECT id, time_created, data FROM message WHERE session_id=? "
        "ORDER BY time_created, id",
        (sid,),
    ):
        try:
            d = json.loads(data)
        except json.JSONDecodeError:
            d = {}
        msgs.append(MsgRow(id=mid, role=d.get("role") or "?", time_created=tcre, data=d))
    part_rows = db.execute(
        "SELECT message_id, id, time_created, data FROM part WHERE session_id=? "
        "ORDER BY time_created, id",
        (sid,),
    ).fetchall()
    by_msg: dict[str, list] = {}
    for message_id, pid, tcre, pdata in part_rows:
        try:
            pd = json.loads(pdata)
        except json.JSONDecodeError:
            continue
        by_msg.setdefault(message_id, []).append(
            {"id": pid, "time": tcre, "data": pd}
        )
    for m in msgs:
        m.parts = by_msg.get(m.id, [])
    return msgs


def user_visible_text(m: MsgRow) -> str:
    texts = []
    for p in m.parts:
        if p["data"].get("type") == "text":
            t = p["data"].get("text")
            if isinstance(t, str):
                texts.append(t)
    return "\n".join(texts).strip()


ANSWER_RE = re.compile(r'"(?P<q>[^"]+)"="(?P<a>[^"]*)"')


def askuser_capsules(m: MsgRow) -> list[dict]:
    out = []
    for p in m.parts:
        d = p["data"]
        if d.get("type") != "tool" or d.get("tool") != "AskUserQuestion":
            continue
        state = d.get("state") or {}
        questions = (state.get("input") or {}).get("questions") or []
        output = str(state.get("output") or "")
        clean_output = output.replace(
            "User has answered your questions:", ""
        ).strip()
        picks = {mq.group("q"): mq.group("a") for mq in ANSWER_RE.finditer(output)}
        for q in questions:
            qtext = q.get("question") or ""
            opts = [
                f"{o.get('label','')}（{o.get('description','')}）"
                for o in (q.get("options") or [])
            ]
            pick = ""
            for qn, ans in picks.items():
                if qn[:60] == qtext[:60]:
                    pick = ans
                    break
            if not pick and len(picks) == 1:
                pick = next(iter(picks.values()))
            answer = pick or clean_output[:160] or "（用户未作答：无输出记录）"
            out.append(
                {
                    "part_id": p["id"],
                    "question": qtext,
                    "options": opts,
                    "answer": answer,
                }
            )
        if not questions and output:
            out.append(
                {
                    "part_id": p["id"],
                    "question": "（问题体未记录）",
                    "options": [],
                    "answer": output.strip()[:300],
                }
            )
    return out


@dataclass
class Turn:
    index: int
    user_text: str = ""
    user_msg_id: str = ""
    user_time: int = 0
    assistant_texts: list = field(default_factory=list)  # (time, text, msg_id)
    askuser: list = field(default_factory=list)
    errors: list = field(default_factory=list)  # (time, error_info, msg_id)
    audit_user: dict = field(default_factory=dict)


def build_turns(msgs: list[MsgRow]) -> list[Turn]:
    turns: list[Turn] = []
    cur: Turn | None = None
    stats = {
        "user_real": 0,
        "user_injected": 0,
        "assistant": 0,
        "errors_intermediate_skipped": 0,
    }
    for m in msgs:
        if m.role == "user":
            if m.is_synthetic:
                stats["user_injected"] += 1
                continue
            cur = Turn(index=len(turns) + 1)
            cur.user_text = user_visible_text(m)
            cur.user_msg_id = m.id
            cur.user_time = m.time_created
            cur.audit_user = {
                "visibility": m.visibility(),
                "source": m.source,
                "fork_origin": m.fork_origin(),
            }
            turns.append(cur)
            stats["user_real"] += 1
        elif m.role == "assistant":
            if cur is None:
                cur = Turn(index=0)
                cur.user_text = "（会话开头，无用户消息）"
                turns.append(cur)
            stats["assistant"] += 1
            info = m.error_info
            if info is None:
                if isinstance(m.data.get("error"), dict):
                    stats["errors_intermediate_skipped"] += 1
            else:
                cur.errors.append((m.time_created, info, m.id))
            for p in m.parts:
                d = p["data"]
                if d.get("type") == "text":
                    t = d.get("text")
                    if isinstance(t, str) and t.strip():
                        cur.assistant_texts.append((p["time"], t, m.id))
                elif d.get("type") == "timeline":
                    continue
            caps = askuser_capsules(m)
            if caps:
                cur.askuser.extend(caps)
    for t in turns:
        t.assistant_texts.sort(key=lambda x: (x[0], x[2]))
    return turns, stats


def render_header(sess: dict, turns: list[Turn], mode: str, stats: dict) -> str:
    times = [t.user_time for t in turns if t.user_time] or [0]
    end_times = (
        [tt[0] for t in turns for tt in t.assistant_texts]
        + [te[0] for t in turns for te in t.errors]
    ) or times
    fork_note = ""
    if sess["parent_id"]:
        fork_note = f"\n> - **Fork 来源**：`{sess['parent_id']}`（本会话是该会话的 Fork）"
    failed = sum(1 for t in turns if t.errors)
    failed_note = f"，其中回复失败 {failed} 轮" if failed else ""
    lines = [
        f"# ZCode GUI 会话转录：{sess['id']}",
        "",
        "> **身份**：本文件是私有转录（Private transcript），由 `zcode-gui-session-export` 从本机 ZCode 会话库导出，仅含 GUI 可见内容；不含思考过程、工具调用细节、系统注入与任何凭据。",
        f"> - **会话**：`{sess['id']}`",
        f"> - **项目**：{sess['project_id'] or '-'}",
        f"> - **时间范围**：{ts_to_local(min(times))} 至 {ts_to_local(max(end_times))}（本地时区）",
        f"> - **轮次**：{len(turns)} 轮真实用户消息{failed_note}；assistant 消息 {stats['assistant']} 条（其中系统注入 {stats['user_injected']} 条已剔除）",
        f"> - **导出模式**：{mode}（gui＝仅 GUI 可见；audit＝附原始定位）",
        f"> - **导出时间/工具**：{datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')} / v{TOOL_VERSION}",
        fork_note,
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def render_turn(t: Turn, mode: str) -> str:
    out = [f"## 第 {t.index} 轮 · {ts_to_local(t.user_time)}", ""]
    out.append("### 研究发起人的提问")
    out.append("")
    out.append("~~~~text")
    out.append(t.user_text)
    out.append("~~~~")
    out.append("")
    if t.askuser:
        for cap in t.askuser:
            out.append("### 【界面问答】")
            out.append("")
            out.append(f"**问**：{cap['question']}")
            if cap["options"]:
                out.append("")
                out.append("选项：")
                for o in cap["options"]:
                    out.append(f"- {o}")
            out.append("")
            out.append(f"**→ 选择**：{cap['answer']}")
            out.append("")
    if t.assistant_texts:
        out.append("### 回复（GUI 可见全文，Markdown 原样）")
        out.append("")
        for _time, text, _mid in t.assistant_texts:
            out.append(text.rstrip())
            out.append("")
    if t.errors:
        out.append("### 回复失败（GUI 可见错误提示）")
        out.append("")
        for _time, info, mid in t.errors:
            label = info["code"] or info["name"] or "UNKNOWN_ERROR"
            msg = info["message"][:ERROR_MESSAGE_MAX]
            suffix = "…" if len(info["message"]) > ERROR_MESSAGE_MAX else ""
            out.append(f"> ⚠️ **{label}**：{msg}{suffix}")
            if mode == "audit":
                out.append(">")
                out.append(f"> assistant message: `{mid}`")
            out.append("")
    if mode == "audit":
        out.append("<details><summary>audit 定位</summary>")
        out.append("")
        out.append(f"- user message: `{t.user_msg_id}`")
        if t.audit_user.get("fork_origin"):
            fo = t.audit_user["fork_origin"]
            out.append(
                f"- fork origin: session `{fo.get('sessionId','?')}` message "
                f"`{fo.get('messageId','?')}`"
            )
        for cap in t.askuser:
            out.append(f"- askuser part: `{cap['part_id']}`")
        for _time, _text, mid in t.assistant_texts:
            out.append(f"- assistant text in message: `{mid}`")
        for _time, _info, mid in t.errors:
            out.append(f"- assistant error in message: `{mid}`")
        out.append("")
        out.append("</details>")
        out.append("")
    out.append("---")
    out.append("")
    return "\n".join(out)


def export(sess_key: str, mode: str) -> dict:
    db = open_db_readonly()
    sess = resolve_session(db, sess_key)
    msgs = load_messages(db, sess["id"])
    db.close()
    if not msgs:
        raise ExportError(f"SESSION_EMPTY:{sess['id']}")
    turns, stats = build_turns(msgs)
    if not turns:
        raise ExportError(f"NO_VISIBLE_USER_MESSAGES:{sess['id']}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    short = sess["id"].replace("sess_", "")[:8]
    out_path = OUTPUT_DIR / f"{stamp}-sess{short}-{mode}.md"
    body = [render_header(sess, turns, mode, stats)]
    body += [render_turn(t, mode) for t in turns]
    out_path.write_text("\n".join(body), encoding="utf-8")
    os_chmod = 0o600
    out_path.chmod(os_chmod)
    return {
        "path": str(out_path),
        "mode": mode,
        "status": "COMPLETE",
        "session": sess["id"],
        "forked_from": sess["parent_id"] or None,
        "turns": len(turns),
        "user_real": stats["user_real"],
        "user_injected_skipped": stats["user_injected"],
        "assistant_messages": stats["assistant"],
        "askuser_count": sum(len(t.askuser) for t in turns),
        "failed_turns": sum(1 for t in turns if t.errors),
        "error_capsules": sum(len(t.errors) for t in turns),
        "errors_intermediate_skipped": stats["errors_intermediate_skipped"],
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--mode", choices=sorted(OUTPUT_MODES), default="gui")
    ap.add_argument("--session", help="session id 或唯一前缀")
    ap.add_argument("--list", action="store_true", help="列出会话库中的 session")
    args = ap.parse_args(argv)
    try:
        if args.list:
            db = open_db_readonly()
            for s in list_sessions(db):
                fork = f" ← fork of {s['parent_id'][:16]}…" if s["parent_id"] else ""
                print(f"{s['id']}  msgs={s['messages']:>4}  {s['project']}{fork}")
            db.close()
            return 0
        if not args.session:
            ap.error("--session 或 --list 必须提供一个")
        receipt = export(args.session, args.mode)
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
        return 0
    except ExportError as e:
        print(f"zcode-gui-session-export: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
