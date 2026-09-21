#!/usr/bin/env python3
"""Append the bounded reality-identity correction from canonical visible events.

This renderer never parses a rollout directly.  It asks the canonical session
trajectory reader for the three specified turns, then asks the same reader to
inspect every selected message without truncation.  Only user messages and
assistant commentary/final messages are copied; tool output, system/developer
instructions, and hidden reasoning are excluded.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

from export_visible_dialogue import HOME_DIR, READER, SOURCE, THREAD, command, jbytes, sha, write_new


TURN_IDS = (
    "01a0c25f-7b06-7202-b171-ab8c6f1b0e14",  # semantic/specification role of RealitySame
    "01a0c269-21f0-7b73-b006-cec601fd0e1a",  # original A/B/X process
    "01a0c281-3db5-7ea1-9b74-1f35569c0a04",  # integration plan
)
SHARD_ID = 11
TITLE = "数学现实同一性、原X与第三弹校正"
SHARD = Path("对话原文") / f"{SHARD_ID:03d} - {TITLE}.md"
DELTA = Path("evidence/对话归档增量-004.json")
VERIFY = Path("evidence/对话逐字核验-004.json")


def visible_turn(turn_id: str) -> list[dict]:
    raw = command(
        [
            "tail",
            "--host",
            "codex",
            "--source",
            str(SOURCE),
            "--turn",
            turn_id,
            "--count",
            "500",
            "--json",
            "--full-text",
        ]
    )
    events = [json.loads(line) for line in raw.splitlines() if line.strip()]
    selected = [
        event
        for event in events
        if event.get("schema_version") == "agent-session-trajectory/v1"
        and (
            event.get("role") == "user"
            or event.get("data", {}).get("phase") in ("commentary", "final_answer")
        )
    ]
    assert selected and selected[0]["turn_id"] == turn_id
    assert sum(event.get("role") == "user" for event in selected) == 1
    assert sum(event.get("data", {}).get("phase") == "final_answer" for event in selected) == 1
    return sorted(selected, key=lambda event: event["sequence"])


def inspected(event: dict) -> dict:
    result = json.loads(
        command(
            [
                "inspect",
                "--host",
                "codex",
                "--source",
                str(SOURCE),
                event["locator"],
                "--no-truncate",
            ]
        )
    )
    assert result["session_id"] == THREAD
    assert not result.get("text_truncated")
    assert result["name"] == event["name"]
    return result


def kind(event: dict) -> str:
    if event["role"] == "user":
        return "user"
    return "assistant-final" if event["data"]["phase"] == "final_answer" else "assistant-commentary"


def load_prior() -> tuple[list[dict], list[Path]]:
    paths = [
        HOME_DIR / "evidence/对话归档清单.json",
        HOME_DIR / "evidence/对话归档增量-002.json",
        HOME_DIR / "evidence/对话归档增量-003.json",
    ]
    manifests = [json.loads(path.read_text()) for path in paths]
    rows: list[dict] = []
    for manifest in manifests:
        rows.extend(manifest["messages"])
    assert [row["ordinal"] for row in rows] == list(range(1, len(rows) + 1))
    assert len({row["id"] for row in rows}) == len(rows)
    return rows, paths


def verify_increment(rows: list[dict]) -> list[str]:
    failures: list[str] = []
    for row in rows:
        data = (HOME_DIR / row["text_file"]).read_bytes()
        shard = (HOME_DIR / row["shard"]).read_bytes()
        start, end = row["shard_byte_range"]
        current = json.loads(
            command(
                [
                    "inspect",
                    "--host",
                    "codex",
                    "--source",
                    str(SOURCE),
                    row["locator"],
                    "--no-truncate",
                ]
            )
        )
        if (
            current.get("text_truncated")
            or current.get("text", "").encode() != data
            or sha(data) != row["sha256"]
            or shard[start:end] != data
        ):
            failures.append(row["id"])
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    prior, prior_paths = load_prior()

    if args.verify:
        delta = json.loads((HOME_DIR / DELTA).read_text())
        rows = delta["messages"]
        failures = verify_increment(rows)
        expected_ids = [event["name"] for turn in TURN_IDS for event in visible_turn(turn)]
        actual_ids = [row["id"] for row in rows]
        index = (HOME_DIR / "对话原文.md").read_text()
        result = {
            "status": "PASS" if not failures and expected_ids == actual_ids else "FAIL",
            "increment_messages": len(rows),
            "cumulative_messages": len(prior) + len(rows),
            "expected_ids_match": expected_ids == actual_ids,
            "failures": failures,
            "reader": str(READER),
            "reader_sha256": sha(READER.read_bytes()),
            "comparison": "canonical inspect, independent text file, and embedded shard bytes; UTF-8 exact",
            "index_mentions_shard": str(SHARD) in index,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return int(result["status"] != "PASS" or not result["index_mentions_shard"])

    assert not (HOME_DIR / SHARD).exists()
    assert not (HOME_DIR / DELTA).exists()
    assert not (HOME_DIR / VERIFY).exists()
    selected = [event for turn in TURN_IDS for event in visible_turn(turn)]
    assert [event["sequence"] for event in selected] == sorted(event["sequence"] for event in selected)
    assert not {event["name"] for event in selected} & {row["id"] for row in prior}

    expanded = [inspected(event) for event in selected]
    body = (
        f"<!-- governance-shard:v2\nlogical_id: ASTRA-BREAKPOINT-DIALOGUE\nshard_id: {SHARD_ID:03d}\nindex: ../对话原文.md\n-->\n\n"
        f"# {TITLE}\n\n"
        "本片逐字保存三轮可见问答：数学现实同一性的语义地位、原 A/B/X 所观察的过程、以及这些澄清应如何进入当前策略。它是历史原文，不把其中任一判断自动提升为数学结论。\n\n"
    ).encode()
    rows: list[dict] = []
    for item in expanded:
        message_kind = kind(item)
        ordinal = len(prior) + len(rows) + 1
        text_file = Path("原始消息") / f"{ordinal:03d}-{message_kind}.txt"
        data = item["text"].encode()
        body += (
            f"## 消息 {ordinal:03d}｜{message_kind}\n\n时间：{item['timestamp']}；消息ID：{item['name']}。\n\n"
            f"<!-- message-original:{item['name']}:start -->\n"
        ).encode()
        start = len(body)
        body += data
        end = len(body)
        body += f"\n<!-- message-original:{item['name']}:end -->\n\n".encode()
        write_new(HOME_DIR / text_file, data)
        rows.append(
            {
                "ordinal": ordinal,
                "id": item["name"],
                "role": item["role"],
                "phase": item.get("data", {}).get("phase"),
                "turn_id": item["turn_id"],
                "timestamp": item["timestamp"],
                "locator": item["locator"],
                "utf8_bytes": len(data),
                "characters": len(item["text"]),
                "sha256": sha(data),
                "text_file": str(text_file),
                "shard": str(SHARD),
                "shard_byte_range": [start, end],
            }
        )
    write_new(HOME_DIR / SHARD, body)

    all_rows = prior + rows
    counts = {
        "user": sum(row["role"] == "user" for row in all_rows),
        "assistant_final": sum(row.get("phase") == "final_answer" for row in all_rows),
        "assistant_commentary": sum(row.get("phase") == "commentary" for row in all_rows),
    }
    manifest = {
        "schema_version": "astra-visible-dialogue-increment/v1",
        "previous_manifests": [str(path.relative_to(HOME_DIR)) for path in prior_paths],
        "previous_manifest_sha256": {str(path.relative_to(HOME_DIR)): sha(path.read_bytes()) for path in prior_paths},
        "thread_id": THREAD,
        "turn_ids": list(TURN_IDS),
        "reader": str(READER),
        "reader_sha256": sha(READER.read_bytes()),
        "source_path": str(SOURCE),
        "source_sha256_at_export": sha(SOURCE.read_bytes()),
        "messages": rows,
        "shard": str(SHARD),
        "cumulative_messages": len(all_rows),
        "counts": counts,
        "scope": "Three requested visible Q&A turns only; no system/developer/tool/hidden-reasoning export.",
    }
    write_new(HOME_DIR / DELTA, jbytes(manifest))

    index_path = HOME_DIR / "对话原文.md"
    index = index_path.read_text()
    old_last = "last_shard: 对话原文/010 - 继续尝试与先修复检查点的指令.md"
    assert old_last in index
    assert "下方 10 个分片" in index
    index = index.replace(old_last, f"last_shard: {SHARD}", 1)
    index = index.replace("下方 10 个分片", "下方 11 个分片", 1)
    index = index.replace(
        "<!-- governance-shard-table:end -->",
        f"| {SHARD_ID:03d} | [{TITLE}](<{SHARD}>) | 数学现实同一性、原过程和策略整合的三轮完整问答 | archived-source |\n<!-- governance-shard-table:end -->",
        1,
    )
    prior_sentence = (
        "当前归档44条：11条用户、8条AI最终答复、25条可见过程消息，截止用户明确要求“先修复全项目加载与检查点，再执行”。"
        "初始21条及两次增量均保留原字节；本轮尚未发送的最终答复不伪装成已交付历史。"
    )
    replacement = (
        f"当前归档{len(all_rows)}条：{counts['user']}条用户、{counts['assistant_final']}条AI最终答复、"
        f"{counts['assistant_commentary']}条可见过程消息。初始快照和前三次增量均保留原字节；"
        "本次只补入三轮已经交付的问答，不把正在进行的工作伪装成历史最终答复。"
    )
    assert prior_sentence in index
    index = index.replace(prior_sentence, replacement, 1)
    index += (
        f"\n本次增量：[004清单]({DELTA})；使用 canonical reader 的逐字核验可执行为"
        f" `python3 -B tools/append_reality_identity_corrigendum.py --verify`。\n"
    )
    index_path.write_text(index)

    failures = verify_increment(rows)
    verify = {
        "status": "PASS" if not failures else "FAIL",
        "increment_messages": len(rows),
        "cumulative_messages": len(all_rows),
        "failures": failures,
        "reader": str(READER),
        "reader_sha256": sha(READER.read_bytes()),
        "comparison": "canonical inspect, independent text file, and embedded shard bytes; UTF-8 exact",
    }
    write_new(HOME_DIR / VERIFY, jbytes(verify))
    print(json.dumps(verify, ensure_ascii=False, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
