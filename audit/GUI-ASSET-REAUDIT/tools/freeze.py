# -*- coding: utf-8 -*-
"""P0 身份冻结（SOP 002 §2）：写 manifest2.json。

用法：python3 -B -I tools/freeze.py            （首次冻结）
      python3 -B -I tools/freeze.py --refreeze  （语料身份未变时的重新冻结；旧 manifest 改名保留）
须先通过 selftest（002 §7）。身份不符一律 BLOCKED。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (CORPUS_DIR, LONG_LINE_BYTES, MANIFEST, ROOT, Blocked, corpus_paths,  # noqa: E402
                    git, now_utc, read_bytes, sha256_hex, split_lines, write_json,
                    load_json, seal_append)


def main(argv):
    refreeze = '--refreeze' in argv
    if os.path.exists(MANIFEST) and not refreeze:
        raise Blocked('manifest2.json 已存在；如确需重新冻结，使用 --refreeze（旧文件将改名保留）')
    rc, out, _ = git('rev-parse', 'HEAD')
    if rc != 0:
        raise Blocked('rev-parse HEAD 失败')
    head = out.decode('utf-8').strip()
    rc, out, _ = git('status', '--porcelain', '--', CORPUS_DIR)
    if rc != 0 or out.strip():
        raise Blocked('语料目录有未提交改动，或 status 失败（002 §2 第 4 步）')
    corpus = corpus_paths()
    files = []
    for tag, path in corpus:
        rc1, o1, _ = git('rev-parse', 'HEAD:' + path)
        rc2, o2, _ = git('hash-object', path)
        blob = o1.decode('utf-8').strip()
        work = o2.decode('utf-8').strip()
        if rc1 != 0 or rc2 != 0 or blob != work:
            raise Blocked('HEAD blob 与工作树不一致：%s' % tag)
        data = read_bytes(os.path.join(ROOT, path))
        lines = split_lines(data)
        lens = [len(x[1]) for x in lines]
        longs = [i + 1 for i, n in enumerate(lens) if n > LONG_LINE_BYTES]
        try:
            data.decode('utf-8')
            enc = 'UTF-8 OK'
        except UnicodeDecodeError as ex:
            enc = 'ENCODING_ANOMALY at byte %d' % ex.start
        files.append({
            'tag': tag, 'path': path, 'blob': blob, 'sha256': sha256_hex(data),
            'bytes': len(data), 'lines': len(lines),
            'ends_with_lf': data.endswith(b'\n'), 'cr_bytes': data.count(b'\r'),
            'max_line_bytes': max(lens) if lens else 0,
            'long_lines_over_%d' % LONG_LINE_BYTES: longs,
            'encoding': enc,
        })
    order = [f['tag'] for f in files]
    total = sum(f['lines'] for f in files)
    fp_src = ''.join('%s:%s\n' % (f['tag'], f['sha256']) for f in sorted(files, key=lambda x: x['tag']))
    manifest = {
        'schema': 'gui-asset-reaudit/manifest/v1',
        'frozen_at': now_utc(),
        'head': head,
        'corpus_dir': CORPUS_DIR,
        'status_porcelain_corpus': 'EMPTY',
        'files': files,
        'order': order,
        'T': total,
        'fingerprint': sha256_hex(fp_src.encode('utf-8')),
        'fingerprint_method': "SHA-256 of concatenated 'tag:sha256' lines (each ending LF) in lexicographic tag order",
        'tool': 'tools/freeze.py',
    }
    if refreeze and os.path.exists(MANIFEST):
        old = load_json(MANIFEST)
        keep = MANIFEST.replace('manifest2.json', 'manifest2.prev-%s.json' % manifest['frozen_at'].replace(':', ''))
        os.replace(MANIFEST, keep)
        seal_append('NOTE_FREEZE', detail='manifest2 重新冻结；旧文件改名保留', old_head=old.get('head'))
    write_json(MANIFEST, manifest)
    print('FREEZE_OK head=%s files=%d T=%d fingerprint=%s' % (head, len(files), total, manifest['fingerprint']))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
