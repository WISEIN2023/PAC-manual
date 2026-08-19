# -*- coding: utf-8 -*-
"""PAC 운영자 매뉴얼 DOCX -> Markdown 전용 컨버터"""
import os, re, io, json, hashlib
import docx
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
from PIL import Image

NS_A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
NS_R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'

# ---------- 공통 유틸 ----------
def norm(s):
    return re.sub(r'[ ​]', ' ', s or '').strip()

def esc_md(s):
    return (s or '').replace('](', ']\\(')


def anchor(heading):
    """GitHub 스타일 앵커 생성"""
    s = heading.strip().lower()
    s = re.sub(r'[^\w\s\-가-힣ㄱ-ㅎㅏ-ㅣ]', '', s, flags=re.UNICODE)
    s = s.replace(' ', '-')
    return s

def cell_text(cell, imgcb=None):
    parts = []
    for p in cell.paragraphs:
        if imgcb is not None:
            for bl in p._p.findall('.//{%s}blip' % NS_A):
                rid = bl.get('{%s}embed' % NS_R)
                nm = imgcb(rid)
                if nm:
                    parts.append('![img](%s/%s)' % ('{ASSETS}', nm))
        t = esc_md(norm(p.text))
        if t: parts.append(t)
    t = '<br>'.join(parts)
    t = re.sub(r'[ \t]+', ' ', t)
    return t.replace('|', '\\|')

def iter_blocks(doc):
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            yield Paragraph(child, doc)
        elif child.tag == qn('w:tbl'):
            yield Table(child, doc)

NUMFMT_CACHE = {}

def num_info(doc, p):
    """(is_list, is_ordered, level) 반환"""
    pPr = p._p.pPr
    if pPr is None:
        return (False, False, 0)
    numPr = pPr.find(qn('w:numPr'))
    if numPr is None:
        return (False, False, 0)
    ilvl_el = numPr.find(qn('w:ilvl'))
    numid_el = numPr.find(qn('w:numId'))
    lvl = int(ilvl_el.get(qn('w:val'))) if ilvl_el is not None else 0
    numid = numid_el.get(qn('w:val')) if numid_el is not None else None
    fmt = 'bullet'
    try:
        key = (id(doc), numid, lvl)
        if key in NUMFMT_CACHE:
            fmt = NUMFMT_CACHE[key]
        else:
            numbering = doc.part.numbering_part.element
            absid = None
            for n in numbering.findall(qn('w:num')):
                if n.get(qn('w:numId')) == numid:
                    a = n.find(qn('w:abstractNumId'))
                    absid = a.get(qn('w:val')) if a is not None else None
                    break
            if absid is not None:
                for an in numbering.findall(qn('w:abstractNum')):
                    if an.get(qn('w:abstractNumId')) == absid:
                        for l in an.findall(qn('w:lvl')):
                            if l.get(qn('w:ilvl')) == str(lvl):
                                f = l.find(qn('w:numFmt'))
                                if f is not None:
                                    fmt = f.get(qn('w:val'))
                                break
                        break
            NUMFMT_CACHE[key] = fmt
    except Exception:
        pass
    return (True, fmt not in ('bullet', 'none'), lvl)


def style_name(p):
    try:
        return p.style.name or ''
    except Exception:
        return ''

def para_md(p):
    """모든 하위 런(하이퍼링크 내부 포함)을 순회하며 굵게 처리"""
    out = []
    for r in p._p.iter(qn('w:r')):
        texts = []
        for t in r.iter():
            if t.tag == qn('w:t'):
                texts.append(t.text or '')
            elif t.tag == qn('w:tab'):
                texts.append(' ')
            elif t.tag in (qn('w:br'), qn('w:cr')):
                texts.append(' ')
        t = ''.join(texts).replace('\u00a0', ' ')
        if not t:
            continue
        rPr = r.find(qn('w:rPr'))
        bold = False
        if rPr is not None:
            b = rPr.find(qn('w:b'))
            if b is not None and b.get(qn('w:val')) not in ('0', 'false'):
                bold = True
        if bold and t.strip():
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            out.append(lead + '**' + t.strip() + '**' + trail)
        else:
            out.append(t)
    s = ''.join(out)
    s = re.sub(r'\*\*\s*\*\*', '', s)
    s = re.sub(r'\*\*\*\*', '', s)
    return esc_md(norm(s))


# ---------- 이미지 ----------
def collect_images(doc):
    """rId -> image part"""
    m = {}
    for rid, rel in doc.part.rels.items():
        if "image" in rel.reltype:
            m[rid] = rel
    return m

def save_image(rel, outdir, idx, slug):
    blob = rel.target_part.blob
    ext = os.path.splitext(rel.target_part.partname)[1].lower() or '.png'
    if ext in ('.emf', '.wmf'):
        ext = '.png'  # 그대로 저장(변환 불가시 원본)
    name = f"img{idx:02d}{ext}"
    path = os.path.join(outdir, name)
    os.makedirs(outdir, exist_ok=True)
    orig = len(blob)
    saved = False
    try:
        im = Image.open(io.BytesIO(blob))
        im.load()
        if im.width > 1600:
            ratio = 1600 / im.width
            im = im.resize((1600, int(im.height * ratio)), Image.LANCZOS)
        buf = io.BytesIO()
        if im.mode in ('RGBA', 'LA'):
            im2 = im.convert('RGBA').quantize(colors=256, method=Image.FASTOCTREE)
        else:
            im2 = im.convert('RGB').quantize(colors=256, method=Image.MEDIANCUT)
        im2.save(buf, format='PNG', optimize=True)
        data = buf.getvalue()
        if len(data) < orig:
            name = f"img{idx:02d}.png"
            path = os.path.join(outdir, name)
            open(path, 'wb').write(data)
            saved = True
    except Exception:
        pass
    if not saved:
        open(path, 'wb').write(blob)
    return name, orig, os.path.getsize(path)

# ---------- 표 ----------
def table_md(tbl, imgcb=None):
    rows = []
    for r in tbl.rows:
        cells = []
        seen = []
        for c in r.cells:
            key = c._tc
            if key in seen:   # 가로 병합 중복 제거
                continue
            seen.append(key)
            cells.append(cell_text(c, imgcb))
        rows.append(cells)
    rows = [r for r in rows if any(x for x in r)]
    if not rows:
        return []
    w = max(len(r) for r in rows)
    rows = [r + [''] * (w - len(r)) for r in rows]
    # 1열짜리 표(콜아웃 박스) -> 인용문으로
    if w == 1:
        out = []
        for r in rows:
            out.append('> ' + r[0].replace('\\|', '|'))
        return out
    out = ['| ' + ' | '.join(rows[0]) + ' |', '|' + '---|' * w]
    for r in rows[1:]:
        out.append('| ' + ' | '.join(r) + ' |')
    return out

COVER_DROP = re.compile(r'필드 업데이트|목차를 (표시|업데이트)|Process Automatic Channel|결산자동화|운영자\s*(메|매)뉴얼|운영\s*·\s*유지보수 가이드')

META_KEYS = {'문서명': 'doc_name', '대상 솔루션': 'solution', '대상 독자': 'audience',
             '문서 버전': 'version', '작성일': 'date', '작성자': 'author',
             '버전': 'version', '개정일': 'date', '문서 명': 'doc_name'}

def parse_meta_table(tbl):
    meta = {}
    for r in tbl.rows:
        cs = [cell_text(c) for c in r.cells]
        if len(cs) >= 2 and cs[0] in META_KEYS:
            meta[META_KEYS[cs[0]]] = cs[1]
    return meta

# ---------- 본체 ----------
def convert(path, slug, assets_dir):
    doc = docx.Document(path)
    rels = collect_images(doc)
    img_idx = 0
    img_stats = []
    body = []
    meta = {}
    blocks = list(iter_blocks(doc))
    first_heading_seen = False
    meta_table_done = False
    skip_toc = False
    n_tables = 0

    counters = {}
    state = {'idx': 0}
    def imgcb(rid):
        if not rid or rid not in rels:
            return None
        state['idx'] += 1
        name, o, n = save_image(rels[rid], assets_dir, state['idx'], slug)
        img_stats.append((name, o, n))
        return name

    for bi, b in enumerate(blocks):
        if isinstance(b, Table):
            if not first_heading_seen and not meta_table_done:
                m = parse_meta_table(b)
                if m:
                    meta.update(m)
                    meta_table_done = True
            if skip_toc:
                continue
            n_tables += 1
            md = table_md(b, imgcb)
            if md:
                body.append('')
                body.extend(md)
                body.append('')
            continue

        p = b
        st = style_name(p)
        txt = norm(p.text)
        blips = p._p.findall('.//{%s}blip' % NS_A)

        # 이미지
        imgs_here = []
        for bl in blips:
            rid = bl.get('{%s}embed' % NS_R)
            name = imgcb(rid)
            if name:
                imgs_here.append(name)

        hm = re.match(r'Heading (\d)', st)
        if hm:
            lvl = int(hm.group(1))
            if not txt:
                continue                      # 빈 H1/H2 제거
            if re.fullmatch(r'목\s*차|목차|Table of Contents', txt):
                skip_toc = True               # 자동 목차 구간 진입
                continue
            skip_toc = False
            first_heading_seen = True
            body.append('')
            body.append('#' * min(lvl, 6) + ' ' + txt)
            body.append('')
            continue

        if skip_toc:
            # 목차 본문(번호 나열)은 버림. 단 다음 Heading 만나면 해제됨
            if imgs_here:
                skip_toc = False
            else:
                continue

        if imgs_here:
            for name in imgs_here:
                body.append('')
                body.append(f'![{slug} 화면]({{ASSETS}}/{name})')
                body.append('')

        if not txt:
            continue

        if not first_heading_seen:
            meta.setdefault('cover', []).append(txt)
            if COVER_DROP.search(txt) or (len(txt) < 25 and not txt.startswith(('-', '·'))):
                continue
            body.append(para_md(p))
            body.append('')
            continue

        md = para_md(p)
        if st.lower().startswith('toc '):
            continue
        is_list, ordered, lvl = num_info(doc, p)
        if st.startswith('List Bullet'):
            is_list, ordered = True, False
            lvl = max(lvl, (int(st[-1]) - 1) if st[-1].isdigit() else 0)
        elif st.startswith('List Number'):
            is_list, ordered = True, True
            lvl = max(lvl, (int(st[-1]) - 1) if st[-1].isdigit() else 0)
        elif not is_list and st in ('List Paragraph', '목록 단락'):
            is_list, ordered, lvl = True, False, 0
        if is_list:
            lvl = min(lvl, 3)
            ind = '  ' * lvl
            prev = body[-1] if body else ''
            prev2 = body[-2] if len(body) > 1 else ''
            cont = bool(re.match(r'^\s*(\d+\.|-) ', prev)) or (prev == '' and re.match(r'^\s*(\d+\.|-) ', prev2))
            if not cont:
                counters.clear()
                if body and body[-1] != '':
                    body.append('')
            elif body and body[-1] == '':
                body.pop()
            if ordered:
                counters[lvl] = counters.get(lvl, 0) + 1
                for k in list(counters):
                    if k > lvl:
                        del counters[k]
                marker = f'{counters[lvl]}. '
            else:
                marker = '- '
            body.append(ind + marker + md)
        elif st.startswith('Caption') or re.match(r'^\[(그림|표)\]', txt):
            body.append('*' + md + '*')
            body.append('')
        else:
            body.append(md)
            body.append('')

    text = '\n'.join(body)
    text = re.sub(r'\n{3,}', '\n\n', text).strip() + '\n'
    return text, meta, img_stats, n_tables
