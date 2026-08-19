# -*- coding: utf-8 -*-
import os, json, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry import DOCS, CATS, CAT_DESC
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(OUT + '/.manifest.json'))
BY = {m['slug']: m for m in M}
IDS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ids.json')))

ROUTE = [
 ("권한, 조직권한, Role, SU01, 접근 불가, 법인 안 보임", "authorization"),
 ("Config, 설정키, 스위치, ZTPAC_CONFIG, ZTPACSYS", "pac-config"),
 ("조직, 회사코드, 사업영역, 지역, 국가, Business Type", "org-master"),
 ("로그, Log, 에러 메시지 저장, 좀비 로그, ZCL_PAC_LOG", "log-management"),
 ("Activity 정의, 액티비티 마스터, Activity Type, Call Type", "activity-master"),
 ("모델링, 표준 모델링, 조직 모델링, 노드, 선후행", "modeling"),
 ("결산일정, 마감일, 캘린더, Schedule ID, 일정 배포, 알람", "closing-schedule"),
 ("Job Schedule, 잡 스케줄, 월간 스케줄, 배치 실행 계획", "schedule-job"),
 ("자동수행, XAUTO, 자동 실행 흐름", "auto-execution"),
 ("Auto Trigger, Trigger Code, CRS Code, 조직간 연계 기동", "auto-trigger"),
 ("Batch Job 생성, 잡 생성 함수", "batch-job"),
 ("REWORK, 재작업, 재수행 감지, Linked Activity", "rework"),
 ("결산점검, Closing Inspection, Financial Risk Validation", "closing-inspection"),
 ("모니터링, 진행현황, 실행시간 초과, 상태 관리", "monitoring"),
 ("To-Do, 할 일, 미완료 To-Do", "todo"),
 ("메일, 메일링, HTML 메일 양식, 발송 안 됨", "mailing"),
 ("공지사항, 첨부파일, 게시", "notice"),
 ("APC, 실시간 Refresh, Push Channel, AMC", "apc"),
 ("Fiori 버튼, Start, Reset, Confirm, Action 오류", "fiori-action"),
 ("Fiori에서 SAP GUI 호출, T-Code 호출, 화면 안 뜸", "fiori-sapgui-call"),
 ("데이터 이관, Migration, RFC Destination 일괄 변경", "data-migration"),
]

tot_files = sum(len(m['files']) for m in M)
tot_chars = sum(m['chars'] for m in M)
tot_img = sum(m['images'] for m in M)
tot_tbl = sum(m['tables'] for m in M)

L = []
L.append('# PAC 운영자 매뉴얼 마스터 인덱스')
L.append('')
L.append('SAP 결산자동화 솔루션 **PAC(Process Automatic Channel)** 운영자 매뉴얼 21종의 진입점입니다.')
L.append('먼저 이 파일에서 대상 문서를 특정한 뒤, **필요한 문서(또는 장) 파일만** 열어보세요.')
L.append('')
L.append('## 조회 순서')
L.append('')
L.append('1. 질문에 **프로그램/테이블/함수명**(`ZLPAC*`, `ZTPAC*`, `ZFPAC*`, `ZCL_*`)이 있으면 → 아래 **역인덱스**부터 조회')
L.append('2. **증상·오류**에 대한 질문이면 → [트러블슈팅 라우팅표](index/troubleshooting.md)')
L.append('3. **용어 정의**를 묻는 질문이면 → [용어집](index/glossary.md)')
L.append('4. 그 외에는 아래 **키워드 라우팅** 또는 **문서 목록**에서 문서를 특정')
L.append('')
L.append('## 역인덱스')
L.append('')
L.append('| 인덱스 | 대상 | 건수 |')
L.append('|---|---|---|')
L.append(f'| [프로그램 · T-Code](index/programs.md) | `ZLPAC*` `ZIPAC*` | {len(IDS["progs"])} |')
L.append(f'| [테이블](index/tables.md) | `ZTPAC*` | {len(IDS["tabs"])} |')
L.append(f'| [함수 · 클래스](index/functions.md) | `ZFPAC*` `ZCL_*` | {len(IDS["funcs"]) + len(IDS["cls"])} |')
L.append(f'| [용어집](index/glossary.md) | 통합 용어 | 263 |')
L.append(f'| [트러블슈팅](index/troubleshooting.md) | 증상 → 조치 | 114 |')
L.append('')
L.append('## 키워드 라우팅')
L.append('')
L.append('| 키워드 | 문서 |')
L.append('|---|---|')
for kw, slug in ROUTE:
    m = BY[slug]
    L.append(f'| {kw} | [{m["title"]}]({m["entry"]}) |')
L.append('')
L.append('## 문서 목록')
L.append('')
for cat in CATS:
    L.append(f'### {cat} — {CAT_DESC[cat]}')
    L.append('')
    L.append('| 문서 | 내용 | 핵심 프로그램 |')
    L.append('|---|---|---|')
    for m in M:
        if m['cat'] != cat:
            continue
        keyp = ', '.join(f'`{x}`' for x in m['ids']['programs'][:4]) or '-'
        L.append(f'| [{m["title"]}]({m["entry"]}) | {m["summary"]} | {keyp} |')
    L.append('')
L.append('## 저장소 통계')
L.append('')
L.append(f'- 원본 문서 **{len(M)}건** → Markdown **{tot_files}개 파일** (장 단위 분할)')
L.append(f'- 본문 {tot_chars:,}자 · 표 {tot_tbl}개 · 화면 캡처 {tot_img}개')
L.append(f'- 식별자: 프로그램 {len(IDS["progs"])} · 테이블 {len(IDS["tabs"])} · 함수 {len(IDS["funcs"])} · 클래스 {len(IDS["cls"])}')
open(OUT + '/INDEX.md', 'w').write('\n'.join(L) + '\n')
print('INDEX.md', os.path.getsize(OUT + '/INDEX.md'))
