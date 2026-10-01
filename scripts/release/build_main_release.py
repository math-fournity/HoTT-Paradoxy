#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the curated tree of the `main` branch from a commit of the `dev` branch.

The main branch holds only what supports the conclusions (researcher, 2026-09-30: "把当前这个repo的main分支整理好，
然后改名为dev分支，然后把main分支腾出来。专门放支撑结论的关键性内容。").  Everything is read from one source
commit, never from the working tree, so the result is determined by (commit, spec):

* docs, proof packages, toolchain records and run receipts listed in scripts/release/main-release-spec.json;
* a closure check: every source file named in an included receipt's source-manifest.json must be included and
  must have the recorded SHA-256 at the source commit, or the build fails;
* CLAIMS.md, copied verbatim from three places on dev (two sections of HoTT/CLAIM_EVIDENCE_MATRIX.md, the
  goal-local relay rows and the claim one-liners of the Claude master index), plus a generated run table;
  CLAIMS-ZH.md is the same file; CLAIMS-RU/DE/FR/EN.md come from translation templates, each of which records the
  SHA-256 of the Chinese sections it translates, and the build fails when that hash no longer matches;
* translations of the community audit papers (`<name>-RU.md` etc. next to the Chinese original on dev), each with
  a header that records the SHA-256 of the Chinese original it translates; a stale translation fails the build.
  On main the Chinese originals get the same language bar as their translations; on dev they stay as they are;
* README.md and README-ZH/RU/DE/FR/EN.md from the templates listed in the spec, tools/replay.py from scripts/release/replay.py;
* RELEASE-MANIFEST.json: every file with its SHA-256 and role, the runs, the units, the translations and the
  paths that the documents mention but that stay on dev.

Usage:
  python3 -B scripts/release/build_main_release.py --source <commit-ish> --out <empty directory>
The output directory may already contain a `.git` entry (a worktree of the main branch); nothing else.
Exit 0 on success; any closure, hash or extraction problem aborts with a message.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
SPEC = "scripts/release/main-release-spec.json"
TABLE_LABELS = {
    "zh": ("路径", "在 `dev` 上", "打开"),
    "ru": ("Путь", "В `dev`", "открыть"),
    "en": ("Path", "On `dev`", "open"),
    "fr": ("Chemin", "Sur `dev`", "ouvrir"),
    "de": ("Pfad", "In `dev`", "öffnen"),
}
# run table of CLAIMS: header row, "accepted", "rejected as expected", list separator, comma
RUN_TABLE_LABELS = {
    "zh": ("| 运行 | 证明 | 命题 | 证明器 | 记录的结局 | 单元 |", "接受", "被拒（预期）", "、", "，"),
    "ru": ("| Запуск | Доказательство | Утверждения | Система | Записанный результат | Блок |", "принято", "отклонено (ожидаемо)", ", ", ", "),
    "de": ("| Lauf | Beweis | Aussagen | Beweisassistent | Aufgezeichnetes Ergebnis | Einheit |", "akzeptiert", "abgelehnt (erwartet)", ", ", ", "),
    "fr": ("| Exécution | Preuve | Énoncés | Assistant de preuve | Résultat enregistré | Unité |", "accepté", "rejeté (attendu)", ", ", ", "),
    "en": ("| Run | Proof | Claims | Proof assistant | Recorded outcome | Unit |", "accepted", "rejected (expected)", ", ", ", "),
}
REPLAY = "scripts/release/replay.py"
GITIGNORE = "_build/\n*.agdai\n*.olean\n__pycache__/\n"


def translation_header(text: str) -> dict:
    """Fields of the `<!-- translation:v1 ... -->` block that opens a translation (empty dict if absent)."""
    m = re.match(r"<!-- translation:v1\n(.*?)\n-->\n", text, re.S)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).split("\n"):
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip()
    return fields


def language_bar(order: list[str], labels: dict, current: str, target) -> str:
    """`中文 · Русский · …` with the current language in bold and the others linked to target(lang)."""
    return " · ".join(f"**{labels[l]}**" if l == current else f"[{labels[l]}]({target(l)})" for l in order)


def insert_after_title(text: str, line: str) -> str:
    """Insert `line` as its own paragraph right after the first level-1 heading."""
    lines = text.split("\n")
    for i, row in enumerate(lines):
        if row.startswith("# "):
            return "\n".join(lines[:i + 1] + ["", line] + lines[i + 1:])
    raise SystemExit("NO_TITLE_FOR_LANGUAGE_BAR")


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def blob(commit: str, path: str) -> bytes:
    try:
        return git("show", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        raise SystemExit(f"MISSING_AT_SOURCE:{path}")


def tracked(commit: str, prefix: str) -> list[str]:
    out = git("ls-tree", "-r", "-z", "--name-only", commit, "--", prefix).decode("utf-8")
    return sorted(p for p in out.split("\0") if p)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section(text: str, heading: str) -> str:
    """Body of a level-2 section: the lines after `heading` up to the next level-2 heading."""
    lines = text.split("\n")
    starts = [i for i, line in enumerate(lines) if line.strip() == heading]
    if len(starts) != 1:
        raise SystemExit(f"SECTION_NOT_UNIQUE:{heading}:{len(starts)}")
    body = []
    for line in lines[starts[0] + 1:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body).strip("\n")


def table_rows(text: str, first_cells: list[str]) -> list[str]:
    rows = []
    for cell in first_cells:
        hits = [line for line in text.split("\n") if line.startswith(f"| `{cell}` |") or line.startswith(f"| {cell} |")]
        if len(hits) != 1:
            raise SystemExit(f"ROW_NOT_UNIQUE:{cell}:{len(hits)}")
        rows.append(hits[0])
    return rows


def path_mentions(text: str) -> set[str]:
    found = set()
    for m in re.finditer(r"`([^`\n]+)`", text):
        found.add(re.sub(r"[:：]\d[\d,–\-]*$", "", m.group(1).strip()).rstrip("/"))
    for m in re.finditer(r"\]\(([^)\n]+)\)", text):
        target = m.group(1).strip().strip("<>").split("#")[0]
        if target and not re.match(r"[a-z]+://", target):
            found.add(target)
    return found


def claims_body(commit: str, cs: dict) -> str:
    """Sections 1-3 of CLAIMS.md: copied verbatim from dev; the CLAIMS translations translate exactly this text."""
    body = []
    titles = ["## 1. 罗素线与 UR：追问程序、邻近对照与截断对照", "## 2. Cloud-Opus 的审计与补完：宇宙塔的一般 n、高阶归纳类型证书、GLM 线与跨平台重放"]
    order_idx = [1, 0]  # the Claude section first, then the Cloud-Opus section
    sections = cs["matrix_sections"]
    for title, idx in zip(titles, order_idx):
        src = sections[idx]
        body += [title, "", f"> 来源：`dev` 上 `{src['file']}` 的“{src['heading'][3:]}”一节。", "",
                 section(blob(commit, src["file"]).decode("utf-8"), src["heading"]), ""]
    relay = cs["relay_rows"]
    relay_text = blob(commit, relay["file"]).decode("utf-8")
    one = cs["claim_one_liners"]
    one_text = blob(commit, one["file"]).decode("utf-8")
    body += [
        "## 3. 芝诺线、Delay 语义与共用对照",
        "",
        "> 这些命题的行在 `dev` 上的目标内索引里（`.claude/goals/CG-001-targeted-overview/relay.md` 的 R1 草稿），尚未登记进共享矩阵；"
        "每个运行另有逐字节重放的输出，在 `dev` 上的 `.claude/goals/CG-001-targeted-overview/verification/`。命题全文与禁止外推以各包的 `CLAIM.md` 为准。",
        "",
        "### 3.1 证明包与运行（逐字）",
        "",
        "| Package ID | Claim IDs | 源码 | 证据 | 判词 |",
        "|---|---|---|---|---|",
        *table_rows(relay_text, relay["proof_ids"]),
        "",
        "### 3.2 命题一句话（逐字）",
        "",
        "| 命题 | 一句话 | 包 |",
        "|---|---|---|",
        *table_rows(one_text, one["claims"]),
    ]
    return "\n".join(body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="commit-ish on dev to build from")
    ap.add_argument("--out", help="empty output directory (required unless --claims-body-sha)")
    ap.add_argument("--claims-body-sha", action="store_true",
                    help="print the SHA-256 of sections 1-3 of CLAIMS.md at --source (the value a CLAIMS translation records) and exit")
    args = ap.parse_args()

    commit = git("rev-parse", "--verify", f"{args.source}^{{commit}}").decode().strip()
    commit_date = git("show", "-s", "--format=%cI", commit).decode().strip()
    spec = json.loads(blob(commit, SPEC))
    repo = spec["repository"]
    if args.claims_body_sha:
        print(sha(claims_body(commit, spec["claims_sources"]).encode("utf-8")))
        return 0
    if not args.out:
        raise SystemExit("--out is required")

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    leftovers = [p.name for p in out.iterdir() if p.name != ".git"]
    if leftovers:
        raise SystemExit(f"OUTPUT_NOT_EMPTY:{leftovers[:5]}")

    files: dict[str, dict] = {}

    def add(path: str, role: str) -> None:
        if path in files:
            return
        data = blob(commit, path)
        files[path] = {"role": role, "data": data}

    for path in spec["docs"]:
        add(path, "CONCLUSION_DOCUMENT")

    # translations of conclusion documents: `<name>-RU.md` etc. next to the Chinese original
    bar = spec["language_bar"]
    order, labels, suffix = bar["order"], bar["labels"], bar["suffix"]
    translations = []
    doc_paths = list(spec["docs"])
    for source in spec["doc_translations"]["sources"]:
        if source not in files:
            raise SystemExit(f"TRANSLATED_SOURCE_NOT_A_DOC:{source}")
        stem = source[:-3]
        name = os.path.basename(stem)

        def target(lang: str, name: str = name) -> str:
            return f"{name}.md" if lang == "zh" else f"{name}{suffix[lang]}.md"

        source_sha = sha(files[source]["data"])
        for lang in order:
            if lang == "zh":
                continue
            path = f"{stem}{suffix[lang]}.md"
            add(path, "CONCLUSION_DOCUMENT_TRANSLATION")
            doc_paths.append(path)
            text = files[path]["data"].decode("utf-8")
            head = translation_header(text)
            if head.get("source") != source or head.get("language") != lang:
                raise SystemExit(f"TRANSLATION_HEADER_INVALID:{path}")
            if head.get("source_sha256") != source_sha:
                raise SystemExit(f"TRANSLATION_STALE:{path}:records {head.get('source_sha256')} but {source} is {source_sha}")
            if language_bar(order, labels, lang, target) not in text.split("\n"):
                raise SystemExit(f"TRANSLATION_LANGUAGE_BAR_MISSING:{path}")
            translations.append({"path": path, "language": lang, "source": source, "source_sha256": source_sha,
                                 "translator": head.get("translator"), "status": "CURRENT"})
        files[source]["language_bar"] = language_bar(order, labels, "zh", target)
        files[source]["source_sha256"] = source_sha

    for package in spec["packages"]:
        members = tracked(commit, package)
        if not members:
            raise SystemExit(f"EMPTY_PACKAGE:{package}")
        for path in members:
            add(path, "PROOF_PACKAGE")
    for path in spec["files"]:
        add(path, "TOOLCHAIN_RECORD")

    on_dev_closure = {row["path"]: row["reason"] for row in spec.get("closure_on_dev", [])}
    on_dev_seen: dict[str, dict] = {}
    runs = []
    for run_id in spec["runs"]:
        prefix = f"HoTT/verification/runs/{run_id}"
        members = tracked(commit, prefix)
        if not members:
            raise SystemExit(f"MISSING_RUN:{run_id}")
        for path in members:
            add(path, "RUN_RECEIPT")
        record = json.loads(blob(commit, f"{prefix}/RUN.json"))
        manifest = json.loads(blob(commit, f"{prefix}/source-manifest.json"))
        for row in manifest.get("files", []):
            path = row["path"]
            if path not in files and path in on_dev_closure:
                if sha(blob(commit, path)) != row["sha256"]:
                    raise SystemExit(f"SOURCE_HASH_MISMATCH:{run_id}:{path}")
                entry = on_dev_seen.setdefault(path, {"path": path, "sha256": row["sha256"], "reason": on_dev_closure[path],
                                                      "dev_url": f"{repo}/blob/dev/{quote(path, safe='/')}", "named_by_runs": []})
                entry["named_by_runs"].append(run_id)
                continue
            if path not in files:
                if spec.get("auto_closure"):
                    add(path, "AUXILIARY_DEPENDENCY")
                else:
                    raise SystemExit(f"CLOSURE_MISSING:{run_id}:{path}")
            if sha(files[path]["data"]) != row["sha256"]:
                raise SystemExit(f"SOURCE_HASH_MISMATCH:{run_id}:{path}")
        exit_code = record.get("exit_code")
        if not isinstance(exit_code, int):
            raise SystemExit(f"RUN_WITHOUT_EXIT_CODE:{run_id}")
        claims = record.get("claim_ids") or []
        if isinstance(claims, str):
            claims = [claims]
        runs.append({
            "run_id": run_id, "proof_id": record.get("proof_id"), "claim_ids": claims,
            "proof_assistant": record.get("proof_assistant"), "recorded_status": record.get("status"),
            "recorded_exit": exit_code, "expected": "accepted" if exit_code == 0 else "rejected",
            "captured_cwd": record.get("cwd"),
        })

    # units: a run belongs to a unit when one of its claim ids matches one of the unit's patterns
    units = {}
    for key, unit in spec["units"].items():
        members = [r["run_id"] for r in runs
                   if any(fnmatch.fnmatch(c.replace("`", ""), pat) for c in r["claim_ids"] for pat in unit["claims"])]
        units[key] = {"title": unit["title"], "claims": unit["claims"], "runs": members}
    unassigned = [r["run_id"] for r in runs if not any(r["run_id"] in u["runs"] for u in units.values())]

    # CLAIMS.md: sections 1-3 are copied verbatim from dev (the part the translations translate), section 4 is generated
    body_text = claims_body(commit, spec["claims_sources"])
    body_sha = sha(body_text.encode("utf-8"))

    def run_table(lang: str) -> str:
        head, yes, no, list_sep, comma = RUN_TABLE_LABELS[lang]
        rows = [head, "|---|---|---|---|---|---|"]
        for r in runs:
            member_of = list_sep.join(k for k, u in units.items() if r["run_id"] in u["runs"]) or "—"
            claims = list_sep.join(c.replace("`", "") for c in r["claim_ids"]) or "—"
            outcome = yes if r["expected"] == "accepted" else no
            rows.append(f"| `{r['run_id']}` | `{r['proof_id']}` | {claims} | {r['proof_assistant']} | "
                        f"{outcome}{comma}exit {r['recorded_exit']}{comma}`{r['recorded_status']}` | {member_of} |")
        return "\n".join(rows)

    claims_outputs: dict[str, bytes] = {}
    claims_translations = []
    for t in spec["claims_templates"]:
        lang = t["lang"]

        def claims_target(l: str) -> str:
            return "CLAIMS-ZH.md" if l == "zh" else f"CLAIMS{suffix[l]}.md"

        expected_bar = language_bar(order, labels, lang, claims_target)
        if lang == "zh":
            text = "\n".join([
                "# 命题与证据",
                "",
                expected_bar,
                "",
                f"> 本文件由 `dev` 上的 `scripts/release/build_main_release.py` 从提交 `{commit[:8]}` 生成，不在本分支修改。第 1、2 节逐字取自 `dev` 上共享证据矩阵 "
                "`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的两节（不含原标题行）；第 3 节逐字取自 `dev` 上的目标内索引草稿与 Claude 总索引；第 4 节由各运行的收据生成。"
                "文中 `formal/…`、`verification/runs/…` 指本分支 `HoTT/` 下的同名路径；其余过程文件的路径在 `dev` 上（见 README 第 6 节）。"
                "另有俄、德、法、英文译本（AI 翻译，以本中文版为准）；`CLAIMS.md` 与 `CLAIMS-ZH.md` 相同。",
                "",
                body_text,
                "",
                "## 4. 运行清单",
                "",
                run_table("zh"),
            ])
        else:
            text = blob(commit, t["template"]).decode("utf-8")
            head = translation_header(text)
            if head.get("source") != "CLAIMS.md" or head.get("language") != lang:
                raise SystemExit(f"CLAIMS_TRANSLATION_HEADER_INVALID:{t['template']}")
            if head.get("source_body_sha256") != body_sha:
                raise SystemExit(f"CLAIMS_TRANSLATION_STALE:{t['template']}:records {head.get('source_body_sha256')} but sections 1-3 are {body_sha}")
            if expected_bar not in text.split("\n"):
                raise SystemExit(f"CLAIMS_TRANSLATION_LANGUAGE_BAR_MISSING:{t['template']}")
            for key, value in {"REPO": repo, "SOURCE_COMMIT": commit, "SOURCE_SHORT": commit[:8], "RUN_TABLE": run_table(lang)}.items():
                text = text.replace("{{" + key + "}}", value)
            if "{{" in text:
                raise SystemExit(f"CLAIMS_PLACEHOLDER_LEFT:{t['template']}")
            claims_translations.append({"language": lang, "template": t["template"], "outputs": t["outputs"],
                                        "source_body_sha256": body_sha, "translator": head.get("translator"), "status": "CURRENT"})
        data = (text.rstrip("\n") + "\n").encode("utf-8")
        for out_name in t["outputs"]:
            claims_outputs[out_name] = data
    if "CLAIMS.md" not in claims_outputs:
        raise SystemExit("CLAIMS_MD_MISSING")

    # paths that the documents mention but that stay on dev
    included = set(files)
    mentioned = set()
    for path in doc_paths:
        text = files[path]["data"].decode("utf-8")
        base = os.path.dirname(path)
        for token in path_mentions(text):
            for candidate in (token, os.path.join(base, token)):
                norm = os.path.normpath(candidate)
                if norm in (".", "") or norm.startswith(".."):
                    continue
                if git("ls-tree", commit, "--", norm).strip():
                    mentioned.add(norm)
                    break
    def in_release(path: str) -> bool:
        return path in included or any(p.startswith(path.rstrip("/") + "/") for p in included)
    on_dev = sorted(p for p in mentioned if not in_release(p) and git("ls-tree", commit, "--", p).strip())
    dev_links = []
    for p in on_dev:
        kind = "tree" if git("ls-tree", commit, "--", p).decode().split()[1] == "tree" else "blob"
        dev_links.append((p, f"{repo}/{kind}/dev/{quote(p, safe='/')}"))

    def dev_table(lang: str) -> str:
        head, where, label = TABLE_LABELS[lang]
        rows = [f"| {head} | {where} |", "|---|---|"]
        rows += [f"| `{p}` | [{label}]({url}) |" for p, url in dev_links]
        return "\n".join(rows)

    link_rewrites: dict[str, list] = {}
    for path in doc_paths:
        text = files[path]["data"].decode("utf-8")
        base = os.path.dirname(path)
        changed = []

        def fix(m: "re.Match[str]") -> str:
            raw = m.group(2)
            target = raw.strip()
            bracketed = target.startswith("<") and target.endswith(">")
            bare = target[1:-1] if bracketed else target
            if re.match(r"[a-z]+://", bare) or bare.startswith("#"):
                return m.group(0)
            file_part, _, anchor = bare.partition("#")
            norm = os.path.normpath(os.path.join(base, file_part))
            if in_release(norm) or not git("ls-tree", commit, "--", norm).strip():
                return m.group(0)
            kind = "tree" if git("ls-tree", commit, "--", norm).decode().split()[1] == "tree" else "blob"
            url = f"{repo}/{kind}/dev/{quote(norm, safe='/')}" + (f"#{anchor}" if anchor else "")
            changed.append({"from": bare, "to": url})
            return f"{m.group(1)}({url})"

        new_text = re.sub(r"(\[[^\]\n]*\])\(([^)\n]+)\)", fix, text)
        if changed:
            files[path]["data"] = new_text.encode("utf-8")
            files[path]["role"] += "_LINKS_TO_DEV"
            link_rewrites[path] = changed

    # on main the Chinese originals carry the same language bar as their translations
    for source in spec["doc_translations"]["sources"]:
        entry = files[source]
        entry["data"] = insert_after_title(entry["data"].decode("utf-8"), entry["language_bar"]).encode("utf-8")
        entry["role"] += "_WITH_LANGUAGE_BAR"

    replay_py = blob(commit, REPLAY)
    accepted = sum(1 for r in runs if r["expected"] == "accepted")
    generated = {
        **claims_outputs,
        "tools/replay.py": replay_py,
        ".gitignore": GITIGNORE.encode("utf-8"),
    }
    templates = spec["readme_templates"]
    readme_outputs = [out for t in templates for out in t["outputs"]]
    if "README.md" not in readme_outputs or len(set(readme_outputs)) != len(readme_outputs):
        raise SystemExit(f"README_OUTPUTS_INVALID:{readme_outputs}")
    file_total = len(files) + len(generated) + len(readme_outputs) + 1  # + RELEASE-MANIFEST.json
    for t in templates:
        readme = blob(commit, t["template"]).decode("utf-8")
        for key, value in {"REPO": repo, "SOURCE_COMMIT": commit, "SOURCE_SHORT": commit[:8], "RUN_TOTAL": str(len(runs)),
                           "RUN_ACCEPTED": str(accepted), "RUN_REJECTED": str(len(runs) - accepted),
                           "FILE_TOTAL": str(file_total), "DEV_PATHS_TABLE": dev_table(t["lang"])}.items():
            readme = readme.replace("{{" + key + "}}", value)
        if "{{" in readme:
            raise SystemExit(f"README_PLACEHOLDER_LEFT:{t['template']}")
        for out_name in t["outputs"]:
            generated[out_name] = readme.encode("utf-8")

    manifest = {
        "schema_version": "hott-paradoxy-main-release/v1",
        "release_id": spec["release_id"],
        "repository": repo,
        "source": {"branch": spec["dev_branch"], "commit": commit, "commit_date": commit_date, "spec": SPEC,
                   "spec_sha256": sha(blob(commit, SPEC))},
        "purpose": spec["purpose"],
        "authorization": spec["authorization"],
        "principle": spec["principle"],
        "counts": {"files": file_total, "runs": len(runs), "runs_accepted": accepted, "runs_rejected_as_expected": len(runs) - accepted},
        "units": units,
        "runs_without_unit": unassigned,
        "runs": runs,
        "paths_mentioned_but_on_dev": on_dev,
        "receipt_sources_kept_on_dev": sorted(on_dev_seen.values(), key=lambda e: e["path"]),
        "document_links_rewritten_to_dev": link_rewrites,
        "translations": {
            "note": "AI translations; the Chinese originals are authoritative. Each translation records the SHA-256 of the "
                    "Chinese text it translates, and the build fails when that hash no longer matches.",
            "documents": translations,
            "claims": {"source": "CLAIMS.md sections 1-3", "source_body_sha256": body_sha, "templates": claims_translations},
        },
        "files": [{"path": p, "role": v["role"], "bytes": len(v["data"]), "sha256": sha(v["data"]), "source": "dev:" + commit[:8],
                   **({"dev_sha256": v["source_sha256"]} if "source_sha256" in v else {})}
                  for p, v in sorted(files.items())]
                 + [{"path": p, "role": "GENERATED", "bytes": len(d), "sha256": sha(d)} for p, d in sorted(generated.items())],
    }
    generated["RELEASE-MANIFEST.json"] = (json.dumps(manifest, ensure_ascii=False, indent=1) + "\n").encode("utf-8")

    for path, entry in files.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(entry["data"])
    for path, data in generated.items():
        target = out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    (out / "tools/replay.py").chmod(0o755)
    print(json.dumps({"status": "BUILT", "source": commit, "files": file_total, "runs": len(runs), "accepted": accepted,
                      "units": {k: len(u["runs"]) for k, u in units.items()}, "runs_without_unit": unassigned,
                      "paths_on_dev": len(on_dev)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
