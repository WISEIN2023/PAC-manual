# -*- coding: utf-8 -*-
import os, re, json, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from converter import anchor
from registry import DOCS, CATS, CAT_DESC

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(OUT + '/.manifest.json'))
BYSLUG = {m['slug']: m for m in M}
TITLE = {m['slug']: m['title'] for m in M}

PATTERNS = {
 'programs':  r'\bZ[LI]PAC[A-Z0-9_]*\b',
 'tables':    r'\bZTPAC[A-Z0-9_]*\b',
 'functions': r'\bZFPAC[A-Z0-9_]*\b',
 'classes':   r'\bZCL_[A-Z0-9_]*\b',
}
ALLPAT = re.compile('|'.join(f'(?:{p})' for p in PATTERNS.values()))
IDLIKE = re.compile(r'^[A-Z][A-Z0-9_]{3,}$')

def kind(x):
    for k, p in PATTERNS.items():
        if re.fullmatch(p, x):
            return k
    return None

def clean(t):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', t)
    t = re.sub(r'\*\*', '', t).strip()
    return re.sub(r'\s+', ' ', t)

occ = collections.defaultdict(list)
desc_cand = collections.defaultdict(collections.Counter)
gloss = {}
trouble = []
heading_ctx = {}

for m in M:
    slug = m['slug']
    for fmeta in m['files']:
        rel = fmeta['path']
        txt = open(os.path.join(OUT, rel)).read()
        cur_h, cur_a = m['title'], ''
        in_gloss = in_trouble = False
        seen_here = set()
        lines = txt.split('\n')
        if lines and lines[0] == '---':
            try:
                lines = lines[lines.index('---', 1) + 1:]
            except ValueError:
                pass
        for line in lines:
            hm = re.match(r'^(#{1,4}) (.+)$', line)
            if hm:
                cur_h = clean(hm.group(2))
                cur_a = anchor(hm.group(2).strip())
                in_gloss = bool(re.search(r'용어\s*집|Glossary', cur_h, re.I))
                in_trouble = bool(re.search(r'증상별|트러블슈팅|Troubleshooting|문의 대응|점검 가이드|FAQ|자주 묻는', cur_h, re.I))
                hm2 = re.match(r'^[\d\.\s]*([A-Z][A-Z0-9_]{4,})\s*[—\-–:]\s*(.+)$', cur_h)
                if hm2 and kind(hm2.group(1)):
                    desc_cand[hm2.group(1)][clean(hm2.group(2))] += 10
            if line.startswith('|') and not re.match(r'^\|[\s\-\|]+\|$', line):
                cells = [clean(c) for c in line.strip('|').split('|')]
                cells = [c for c in cells if c]
                if len(cells) >= 2:
                    if in_gloss and len(cells[0]) <= 40 and cells[0] not in ('용어', '구분', '약어'):
                        gloss.setdefault(cells[0], (cells[1], slug, rel, cur_a))
                    generic = (re.search(r'증상|현상|항목|질문|구분', cells[0]) and re.search(r'원인|설명|조치|확인 방법', cells[1]))
                    if in_trouble and not generic and len(cells[0]) > 4:
                        trouble.append((cells[0], ' → '.join(cells[1:])[:200], slug, rel, cur_a, cur_h))
                    for c in cells:
                        idm = re.fullmatch(r'([A-Z][A-Z0-9_]{4,})(\s*\(.*\))?', c)
                        if idm and kind(idm.group(1)):
                            tid = idm.group(1)
                            for x in cells:
                                if x == c or len(x) < 4 or IDLIKE.match(x):
                                    continue
                                if tid in x or x in tid:
                                    continue
                                desc_cand[tid][x[:100]] += 3
                                break
            for mm in ALLPAT.finditer(line):
                tok = mm.group(0).rstrip('_')
                if len(tok) <= 4 or not kind(tok) or tok in seen_here:
                    continue
                seen_here.add(tok)
                occ[tok].append((slug, rel, cur_a, cur_h))

def best_desc(tid):
    c = desc_cand.get(tid)
    if not c:
        return ''
    for cand, _ in c.most_common(5):
        cand = cand.strip(' .·')
        if len(cand) < 3 or IDLIKE.match(cand):
            continue
        if tid in cand and len(cand) < len(tid) + 6:
            continue
        return cand[:80]
    return ''

def links(tid, limit=2):
    out, seen = [], set()
    items = sorted(occ[tid], key=lambda x: (0 if tid in x[3] else (1 if tid in x[1] else 2)))
    for slug, rel, a, h in items:
        key = (slug, a)
        if key in seen:
            continue
        seen.add(key)
        p = '../' + rel + ('#' + a if a else '')
        out.append(f'[{slug}]({p})')
        if len(out) >= limit:
            break
    return ' · '.join(out)

def write(path, s):
    open(os.path.join(OUT, path), 'w').write(s)

HDR = "<!-- 이 파일은 docs/ 원본에서 자동 생성됩니다. 직접 수정하지 마세요. -->\n"

def id_table(title, keys, note):
    lines = [f'# {title}', '', note, '', f'총 **{len(keys)}건**', '',
             '| ID | 설명 | 상세 위치 |', '|---|---|---|']
    for k in sorted(keys):
        d = best_desc(k).replace('|', '\\|')
        lines.append(f'| `{k}` | {d} | {links(k)} |')
    return HDR + '\n'.join(lines) + '\n'

progs = sorted(x for x in occ if kind(x) == 'programs')
tabs  = sorted(x for x in occ if kind(x) == 'tables')
funcs = sorted(x for x in occ if kind(x) == 'functions')
cls   = sorted(x for x in occ if kind(x) == 'classes')

write('index/programs.md', id_table(
    '프로그램 · T-Code 인덱스', progs,
    '`ZLPAC*` / `ZIPAC*` 프로그램과 트랜잭션 코드 역인덱스입니다. 프로그램 번호로 담당 매뉴얼과 해당 섹션을 바로 찾을 수 있습니다.'))
write('index/tables.md', id_table(
    '테이블 인덱스', tabs,
    '`ZTPAC*` 테이블 역인덱스입니다. 테이블명으로 해당 테이블을 설명하는 매뉴얼 섹션을 찾을 수 있습니다.'))

fl = [HDR, '# 함수 · 클래스 인덱스', '',
      '`ZFPAC*` Function Module과 `ZCL_*` 클래스 역인덱스입니다.', '',
      f'## Function Module ({len(funcs)}건)', '',
      '| ID | 설명 | 상세 위치 |', '|---|---|---|']
for k in funcs:
    fl.append(f'| `{k}` | {best_desc(k)} | {links(k)} |')
fl += ['', f'## 클래스 ({len(cls)}건)', '', '| ID | 설명 | 상세 위치 |', '|---|---|---|']
for k in cls:
    fl.append(f'| `{k}` | {best_desc(k)} | {links(k)} |')
write('index/functions.md', '\n'.join(fl) + '\n')

gl = [HDR, '# 용어집 (통합)', '',
      '각 매뉴얼의 용어집 섹션을 통합했습니다. 동일 용어는 최초 정의 1건만 유지합니다.', '',
      f'총 **{len(gloss)}건**', '', '| 용어 | 설명 | 출처 |', '|---|---|---|']
for term in sorted(gloss, key=lambda x: (x.lower())):
    d, slug, rel, a = gloss[term]
    gl.append(f'| **{term}** | {d} | [{slug}](../{rel}{"#" + a if a else ""}) |')
write('index/glossary.md', '\n'.join(gl) + '\n')

tl = [HDR, '# 트러블슈팅 · 점검 라우팅표 (통합)', '',
      '각 매뉴얼의 "증상별 점검 가이드 / 트러블슈팅 / FAQ" 항목을 한 곳에 모았습니다.',
      '증상 키워드로 검색한 뒤 오른쪽 링크의 원문 섹션만 열어보세요.', '']
bydoc = collections.defaultdict(list)
for row in trouble:
    bydoc[row[2]].append(row)
tl.append(f'총 **{len(trouble)}건** / {len(bydoc)}개 문서\n')
for slug in [m['slug'] for m in M]:
    rows = bydoc.get(slug)
    if not rows:
        continue
    tl += [f'## {TITLE[slug]}', '', '| 증상 · 항목 | 원인 / 조치 | 원문 |', '|---|---|---|']
    seen = set()
    for sym, act, s, rel, a, h in rows:
        if (sym, act) in seen:
            continue
        seen.add((sym, act))
        tl.append(f'| {sym} | {act} | [{h}](../{rel}{"#" + a if a else ""}) |')
    tl.append('')
write('index/troubleshooting.md', '\n'.join(tl) + '\n')

json.dump({'progs': progs, 'tabs': tabs, 'funcs': funcs, 'cls': cls,
           'desc': {k: best_desc(k) for k in occ}},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ids.json'), 'w'), ensure_ascii=False)
print('programs', len(progs), 'tables', len(tabs), 'functions', len(funcs), 'classes', len(cls),
      'gloss', len(gloss), 'trouble', len(trouble))
for f in ['programs', 'tables', 'functions', 'glossary', 'troubleshooting']:
    print(f, os.path.getsize(f'{OUT}/index/{f}.md'))
