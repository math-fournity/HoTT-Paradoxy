#!/usr/bin/env python3
"""Build or verify a dated bibliographic discovery snapshot for LIT-DENOMINATOR-001.

Crossref and OpenAlex are discovery metadata sources, not theorem evidence.  Every
candidate selected for the research corpus must later be qualified against its
primary paper, proceedings page, publisher record, or official source repository.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


SCHEMA = "hott-literature-discovery/v1"
CUTOFF = "2026-09-14"
MAX_RESULTS = 100
USER_AGENT = "HoTT-machine-overview-literature-audit/1.0 (local academic research)"

QUERIES = [
    ("Q-COMP-HOTT", '"homotopy type theory" computability'),
    ("Q-PARTIAL-UNIVALENT", '"univalent type theory" partiality recursion dominance'),
    ("Q-CUBICAL-META", '"cubical type theory" normalization canonicity decidability'),
    ("Q-SYNTHETIC-INCOMP", '"synthetic computability" incompleteness'),
    ("Q-MECH-GODEL", 'Gödel incompleteness proof assistant Coq Lean Agda Isabelle'),
    ("Q-TT-UNDECIDABILITY", '"type theory" undecidability proof search'),
    ("Q-GUARDED", '"guarded recursion" dependent type theory clocked productivity'),
    ("Q-2LTT-META", '"two-level type theory" metatheory syntax reflection'),
    ("Q-ORACLE-HOTT", '"homotopy type theory" oracle modality Turing reducibility'),
    ("Q-CUBICAL-SYNTAX", '"cubical type theory" syntax coherence decision procedure'),
    ("Q-PROOF-SEARCH", '"proof search" typeclass termination Coq Agda Lean'),
    ("Q-CT-CUBICAL", '"Church thesis" cubical assemblies homotopy type theory'),
    ("Q-TURING-REDUCIBILITY", '"Turing reducibility" constructive type theory'),
    ("Q-PARTIAL-ELEMENTS", '"partial elements" univalent type theory'),
    ("Q-AGDA-GODEL", 'Gödel theorem Agda formalization'),
    ("Q-INCOMP-HOTT", 'incompleteness "homotopy type theory"'),
    ("Q-EXTENSION-2LTT", '"extension types" "two-level type theory"'),
    ("Q-DECIDABILITY-HOTT", 'decidability "homotopy type theory" Brouwer'),
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def normalized_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def year_from_parts(parts: Any) -> int | None:
    try:
        return int(parts[0][0])
    except (TypeError, ValueError, IndexError):
        return None


def fetch_json(url: str, retries: int = 3) -> tuple[bytes, dict[str, Any]]:
    last: Exception | None = None
    for attempt in range(1, retries + 1):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                raw = response.read()
                return raw, {
                    "http_status": response.status,
                    "content_type": response.headers.get("content-type"),
                    "resolved_url": response.geturl(),
                    "attempt": attempt,
                }
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code != 429 or attempt == retries:
                break
            retry_after = exc.headers.get("Retry-After", "2")
            try:
                delay = min(max(float(retry_after), 0.5), 10.0)
            except ValueError:
                delay = 2.0
            time.sleep(delay)
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt == retries:
                break
            time.sleep(float(attempt))
    assert last is not None
    raise last


def crossref_url(query: str) -> str:
    params = {
        "query.bibliographic": query,
        "rows": str(MAX_RESULTS),
        "filter": f"from-pub-date:1931-01-01,until-pub-date:{CUTOFF}",
        "select": "DOI,title,author,published,container-title,type,URL,subject,abstract",
    }
    return "https://api.crossref.org/works?" + urllib.parse.urlencode(params)


def openalex_url(query: str) -> str:
    params = {
        "search": query,
        "filter": "from_publication_date:1931-01-01,to_publication_date:" + CUTOFF,
        "per-page": str(MAX_RESULTS),
        "mailto": "research@example.invalid",
    }
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def crossref_rows(payload: dict[str, Any], query_id: str) -> list[dict[str, Any]]:
    rows = []
    for item in payload.get("message", {}).get("items", []):
        title_values = item.get("title") or []
        title = str(title_values[0]).strip() if title_values else ""
        if not title:
            continue
        published = item.get("published", {}).get("date-parts")
        year = year_from_parts(published)
        authors = []
        for author in item.get("author") or []:
            name = " ".join(str(author.get(part, "")).strip() for part in ("given", "family")).strip()
            if name:
                authors.append(name)
        doi = str(item.get("DOI", "")).lower() or None
        rows.append({
            "title": title,
            "year": year,
            "authors": authors,
            "venue": "; ".join(item.get("container-title") or []),
            "doi": doi,
            "url": item.get("URL"),
            "type": item.get("type"),
            "abstract_available": bool(item.get("abstract")),
            "discovery_sources": ["crossref"],
            "query_ids": [query_id],
            "review_status": "DISCOVERY_UNREVIEWED",
        })
    return rows


def openalex_rows(payload: dict[str, Any], query_id: str) -> list[dict[str, Any]]:
    rows = []
    for item in payload.get("results", []):
        title = str(item.get("display_name") or "").strip()
        if not title:
            continue
        authors = [
            str(entry.get("author", {}).get("display_name", "")).strip()
            for entry in item.get("authorships") or []
        ]
        authors = [name for name in authors if name]
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        doi_value = item.get("doi")
        doi = str(doi_value).removeprefix("https://doi.org/").lower() if doi_value else None
        rows.append({
            "title": title,
            "year": item.get("publication_year"),
            "authors": authors,
            "venue": source.get("display_name") or "",
            "doi": doi,
            "url": primary.get("landing_page_url") or item.get("id"),
            "type": item.get("type"),
            "abstract_available": bool(item.get("abstract_inverted_index")),
            "openalex_id": item.get("id"),
            "cited_by_count": item.get("cited_by_count"),
            "discovery_sources": ["openalex"],
            "query_ids": [query_id],
            "review_status": "DISCOVERY_UNREVIEWED",
        })
    return rows


def candidate_key(row: dict[str, Any]) -> str:
    if row.get("doi"):
        return "doi:" + str(row["doi"])
    return "title:" + normalized_title(str(row["title"]))


def merge_candidate(target: dict[str, Any], incoming: dict[str, Any]) -> None:
    target["discovery_sources"] = sorted(set(target["discovery_sources"] + incoming["discovery_sources"]))
    target["query_ids"] = sorted(set(target["query_ids"] + incoming["query_ids"]))
    for field in ("year", "venue", "doi", "url", "type", "openalex_id", "cited_by_count"):
        if not target.get(field) and incoming.get(field):
            target[field] = incoming[field]
    if len(incoming.get("authors", [])) > len(target.get("authors", [])):
        target["authors"] = incoming["authors"]
    target["abstract_available"] = bool(target.get("abstract_available") or incoming.get("abstract_available"))


def build(output: Path) -> int:
    if output.exists() and any(output.iterdir()):
        raise SystemExit("OUTPUT_NOT_EMPTY")
    raw_dir = output / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    fetches: list[dict[str, Any]] = []
    merged: dict[str, dict[str, Any]] = {}
    errors: list[dict[str, Any]] = []
    for query_id, query in QUERIES:
        for provider, url_builder, parser in (
            ("crossref", crossref_url, crossref_rows),
            ("openalex", openalex_url, openalex_rows),
        ):
            url = url_builder(query)
            try:
                raw, response = fetch_json(url)
                payload = json.loads(raw)
                rows = parser(payload, query_id)
                compressed = gzip.compress(raw, compresslevel=9, mtime=0)
                rel = f"raw/{query_id}-{provider}.json.gz"
                (output / rel).write_bytes(compressed)
                fetches.append({
                    "query_id": query_id,
                    "query": query,
                    "provider": provider,
                    "request_url": url,
                    "raw_path": rel,
                    "raw_bytes": len(raw),
                    "raw_sha256": sha(raw),
                    "gzip_bytes": len(compressed),
                    "gzip_sha256": sha(compressed),
                    "parsed_rows": len(rows),
                    **response,
                })
                for row in rows:
                    key = candidate_key(row)
                    if key in merged:
                        merge_candidate(merged[key], row)
                    else:
                        row["candidate_key"] = key
                        merged[key] = row
            except Exception as exc:  # evidence captures exact provider failure
                errors.append({
                    "query_id": query_id,
                    "query": query,
                    "provider": provider,
                    "request_url": url,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                })
    candidates = sorted(merged.values(), key=lambda row: (row.get("year") or 9999, normalized_title(row["title"])))
    candidate_doc = {
        "schema_version": SCHEMA,
        "asset_class": "MACHINE_GENERATED_DISCOVERY_SNAPSHOT",
        "cutoff_date": CUTOFF,
        "evidence_boundary": "DISCOVERY_METADATA_NOT_PRIMARY_SOURCE_QUALIFICATION",
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    candidate_raw = (json.dumps(candidate_doc, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    (output / "DISCOVERY-CANDIDATES.json").write_bytes(candidate_raw)
    manifest = {
        "schema_version": SCHEMA,
        "asset_class": "MACHINE_GENERATED_DISCOVERY_RECEIPT",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "cutoff_date": CUTOFF,
        "query_count": len(QUERIES),
        "provider_count": 2,
        "expected_fetches": len(QUERIES) * 2,
        "successful_fetches": len(fetches),
        "failed_fetches": len(errors),
        "candidate_count": len(candidates),
        "candidate_path": "DISCOVERY-CANDIDATES.json",
        "candidate_bytes": len(candidate_raw),
        "candidate_sha256": sha(candidate_raw),
        "queries": [{"id": query_id, "query": query} for query_id, query in QUERIES],
        "fetches": fetches,
        "errors": errors,
        "primary_source_status": "NOT_QUALIFIED_BY_THIS_TOOL",
    }
    (output / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "DISCOVERY_SNAPSHOT_CREATED",
        "output": str(output.resolve()),
        "queries": len(QUERIES),
        "successful_fetches": len(fetches),
        "failed_fetches": len(errors),
        "candidates": len(candidates),
    }, ensure_ascii=False))
    return 0 if not errors else 2


def verify(output: Path) -> int:
    manifest = json.loads((output / "MANIFEST.json").read_text(encoding="utf-8"))
    candidate_raw = (output / manifest["candidate_path"]).read_bytes()
    errors: list[str] = []
    if manifest.get("schema_version") != SCHEMA:
        errors.append("SCHEMA")
    if sha(candidate_raw) != manifest.get("candidate_sha256"):
        errors.append("CANDIDATE_HASH")
    if len(candidate_raw) != manifest.get("candidate_bytes"):
        errors.append("CANDIDATE_BYTES")
    candidates = json.loads(candidate_raw)["candidates"]
    keys = [row["candidate_key"] for row in candidates]
    if len(keys) != len(set(keys)):
        errors.append("DUPLICATE_KEYS")
    if len(candidates) != manifest.get("candidate_count"):
        errors.append("CANDIDATE_COUNT")
    query_ids = {row["id"] for row in manifest.get("queries", [])}
    if query_ids != {query_id for query_id, _ in QUERIES}:
        errors.append("QUERY_SET")
    for row in manifest.get("fetches", []):
        compressed = (output / row["raw_path"]).read_bytes()
        if sha(compressed) != row["gzip_sha256"] or len(compressed) != row["gzip_bytes"]:
            errors.append("GZIP_IDENTITY:" + row["raw_path"])
            continue
        raw = gzip.decompress(compressed)
        if sha(raw) != row["raw_sha256"] or len(raw) != row["raw_bytes"]:
            errors.append("RAW_IDENTITY:" + row["raw_path"])
    status = "VALID" if not errors else "INVALID"
    print(json.dumps({"status": status, "errors": errors, "queries": len(query_ids), "fetches": len(manifest.get("fetches", [])), "candidates": len(candidates)}, ensure_ascii=False))
    return 0 if not errors else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    build_parser = sub.add_parser("build")
    build_parser.add_argument("--output", type=Path, required=True)
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    return build(args.output) if args.command == "build" else verify(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
