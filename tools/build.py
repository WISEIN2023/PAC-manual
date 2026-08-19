# -*- coding: utf-8 -*-
import os, re, sys, json, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from converter import convert, anchor
from romanize import slugify
from registry import DOCS, CATS, CAT_DESC, SPLIT_THRESHOLD
SUB_SPLIT = 9000

SRC = os.environ.get("PAC_DOCX_SRC", os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_source_docx"))
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERNS = {
 'programs':  r'\bZ[LI]PAC[A-Z0-9_]*\b',
 'tables':    r'\bZTPAC[A-Z0-9_]*\b',
 'functions': r'\bZFPAC[A-Z0-9_]*\b',
 'classes':   r'\bZCL_[A-Z0-9_]*\b',
}

def ids_in(text):
    r = {}
    for k, p in PATTERNS.items():
        vals = set()
        for m in re.findall(p, text):
            m = m.rstrip('_')
            if len(m) > 4:
                vals.add(m)
        r[k] = sorted(vals)
    return r

def yaml_list(v):
    return '[' + ', '.join(v) + ']' if v else '[]'

def fm(d):
    lines = ['---']
    for k, v in d.items():
        if isinstance(v, list):
            lines.append(f'{k}: {yaml_list(v)}')
        else:
            s = str(v)
            if any(c in s for c in ':#\'"[]{}') or s == '':
                s = '"' + s.replace('"', "'") + '"'
            lines.append(f'{k}: {s}')
    lines.append('---')
    return '\n'.join(lines) + '\n'

def split_by(text, level):
    mark = '#' * level + ' '
    parts = []
    cur_h, cur, pre = None, [], []
    for line in text.split('\n'):
        if line.startswith(mark):
            if cur_h is not None:
                parts.append((cur_h, '\n'.join(cur).strip()))
            elif cur:
                pre = cur
            cur_h = line[len(mark):].strip()
            cur = []
        else:
            cur.append(line)
    if cur_h is not None:
        parts.append((cur_h, '\n'.join(cur).strip()))
    else:
        pre = cur
    return '\n'.join(pre).strip(), parts


def split_h1(text):
    """(heading, body) 리스트로 H1 분할. 첫 H1 이전 서두는 preamble."""
    parts = []
    cur_h, cur = None, []
    pre = []
    for line in text.split('\n'):
        if line.startswith('# '):
            if cur_h is not None:
                parts.append((cur_h, '\n'.join(cur).strip()))
            elif cur:
                pre = cur
            cur_h = line[2:].strip()
            cur = []
        else:
            cur.append(line)
    if cur_h is not None:
        parts.append((cur_h, '\n'.join(cur).strip()))
    else:
        pre = cur
    return '\n'.join(pre).strip(), parts

def headings_of(text):
    out = []
    for line in text.split('\n'):
        m = re.match(r'^(#{1,4}) (.+)$', line)
        if m:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out

def main():
    for sub in ('docs', 'assets'):
        d = os.path.join(OUT, sub)
        if os.path.exists(d):
            shutil.rmtree(d)
    os.makedirs(OUT + '/docs', exist_ok=True)
    os.makedirs(OUT + '/assets', exist_ok=True)
    os.makedirs(OUT + '/index', exist_ok=True)

    manifest = []
    for i, d in enumerate(DOCS, 1):
        path = os.path.join(SRC, d['file'])
        slug = d['slug']
        assets_dir = os.path.join(OUT, 'assets', slug)
        text, meta, imgs, ntab = convert(path, slug, assets_dir)
        ids = ids_in(text)
        pre, parts = split_h1(text)
        split = len(text) > SPLIT_THRESHOLD and len(parts) >= 3

        base_fm = dict(
            id=slug, title=d['title'], category=d['cat'],
            version=meta.get('version', 'v1.0'),
            updated=meta.get('date', ''),
            source=d['file'],
            programs=ids['programs'][:40],
            tables=ids['tables'][:40],
            functions=(ids['functions'] + ids['classes'])[:40],
            summary=d['summary'],
        )

        files = []
        toc_lines = []
        if not split:
            rel = f'docs/{slug}.md'
            assets_rel = f'../assets/{slug}'
            content = fm(base_fm) + '\n# ' + d['title'] + '\n\n> ' + d['summary'] + '\n\n' + demote(text, pre)
            content = content.replace('{ASSETS}', assets_rel)
            open(os.path.join(OUT, rel), 'w').write(content)
            files.append((rel, headings_of(content)))
        else:
            os.makedirs(os.path.join(OUT, 'docs', slug), exist_ok=True)
            assets_rel = f'../../assets/{slug}'
            used = set()

            def write_unit(name, title, bodymd, parent_title=None):
                nm = name
                while nm in used:
                    nm += 'x'
                used.add(nm)
                rel = f'docs/{slug}/{nm}.md'
                cfm = dict(id=f'{slug}/{nm}', doc=slug, title=title,
                           parent=f'docs/{slug}/README.md')
                c = fm(cfm) + '\n' + bodymd.strip() + '\n'
                c = c.replace('{ASSETS}', assets_rel)
                open(os.path.join(OUT, rel), 'w').write(c)
                files.append((rel, headings_of(c)))
                return nm

            for ci, (h, body) in enumerate(parts, 1):
                base = re.sub(r'^\d+-', '', slugify(h))
                pre2, subs = split_by(body, 2)
                if len(body) > SUB_SPLIT and len(subs) >= 2:
                    toc_lines.append(f'{ci}. **{h}**')
                    for si, (sh, sbody) in enumerate(subs, 1):
                        sbase = re.sub(r'^\d+(-\d+)*-', '', slugify(sh))
                        head = f'# {h}\n\n'
                        if si == 1 and pre2:
                            head += pre2 + '\n\n'
                        md = head + f'## {sh}\n\n' + sbody
                        nm = write_unit(f'{ci:02d}-{si:02d}-{sbase}', f'{h} > {sh}', md, h)
                        toc_lines.append(f'    - [{sh}]({nm}.md)')
                else:
                    md = f'# {h}\n\n' + body
                    nm = write_unit(f'{ci:02d}-{base}', h, md)
                    toc_lines.append(f'{ci}. [{h}]({nm}.md)')

            rd = fm(base_fm) + '\n# ' + d['title'] + '\n\n> ' + d['summary'] + '\n\n'
            if pre:
                rd += pre.replace('{ASSETS}', assets_rel) + '\n\n'
            rd += '## 목차\n\n' + '\n'.join(toc_lines) + '\n'
            rel = f'docs/{slug}/README.md'
            open(os.path.join(OUT, rel), 'w').write(rd)
            files.insert(0, (rel, headings_of(rd)))

        manifest.append(dict(
            order=i, slug=slug, title=d['title'], cat=d['cat'], summary=d['summary'],
            source=d['file'], split=split, chars=len(text), tables=ntab,
            images=len(imgs), img_bytes=[list(x[1:]) for x in imgs],
            ids=ids, entry=(f'docs/{slug}/README.md' if split else f'docs/{slug}.md'),
            files=[dict(path=p, headings=h) for p, h in files],
        ))
        mx = max((os.path.getsize(os.path.join(OUT, p)) for p, _ in files), default=0)
        print(f'{slug:20s} chars={len(text):6d} tbl={ntab:3d} img={len(imgs):3d} files={len(files):3d} max={mx:6d} split={split}')

    json.dump(manifest, open(OUT + '/.manifest.json', 'w'), ensure_ascii=False, indent=1)


def demote(text, pre):
    """단일 파일: 최상단에 문서 제목 H1을 넣었으므로 본문 헤딩을 1단계 내림"""
    out = []
    for line in text.split('\n'):
        m = re.match(r'^(#{1,5}) (.+)$', line)
        if m:
            out.append('#' + m.group(1) + ' ' + m.group(2))
        else:
            out.append(line)
    return '\n'.join(out).strip() + '\n'

if __name__ == '__main__':
    main()
