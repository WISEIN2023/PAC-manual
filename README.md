# PAC 운영자 매뉴얼 (Markdown)

SAP 결산자동화 솔루션 **PAC (Process Automatic Channel)** 운영자 매뉴얼 21종의 Markdown 저장소입니다.
원본 DOCX를 변환하고, AI 질의응답 시 토큰 소모를 최소화하도록 인덱스를 붙였습니다.

## 시작하기

**→ [INDEX.md](INDEX.md) 에서 시작하세요.**

| 찾는 것 | 바로 가기 |
|---|---|
| 프로그램 · T-Code 번호로 찾기 | [index/programs.md](index/programs.md) |
| 테이블명으로 찾기 | [index/tables.md](index/tables.md) |
| 함수 · 클래스명으로 찾기 | [index/functions.md](index/functions.md) |
| 오류 · 증상으로 찾기 | [index/troubleshooting.md](index/troubleshooting.md) |
| 용어 뜻 찾기 | [index/glossary.md](index/glossary.md) |

## 구성

```
INDEX.md               마스터 인덱스
CLAUDE.md              AI 조회 규약 (Claude 연계 시 자동 참조)
index/                 역인덱스 5종
docs/                  매뉴얼 본문 (대형 문서는 장 단위 분할)
assets/                화면 캡처 이미지
tools/                 DOCX → Markdown 재변환 스크립트
CONVERSION_REPORT.md   변환 검증 리포트
```

## Claude 연계

1. GitHub MCP 서버를 Claude에 연결하고 이 저장소를 대상으로 지정합니다.
2. `INDEX.md`와 `index/` 파일을 Claude Project 지식에 등록하면 라우팅 단계의 토큰 소모가 사라집니다.
3. `CLAUDE.md`의 조회 규약에 따라 필요한 파일만 읽도록 동작합니다.

## 갱신 방법

원본 DOCX가 Source of Truth입니다. 원본 수정 후 아래를 실행하면 본문·인덱스가 모두 재생성됩니다.

```bash
pip install python-docx pillow
export PAC_DOCX_SRC="/path/to/PAC Manual(DOCX)"

python3 tools/build.py        # DOCX -> docs/, assets/
python3 tools/gen_index.py    # index/ 5종 재생성
python3 tools/gen_root.py     # INDEX.md 재생성
python3 tools/validate.py     # 검증 리포트
```

`tools/registry.py`의 `DOCS` 목록에 항목을 추가하면 신규 매뉴얼도 동일하게 편입됩니다.

## 주의

내부 시스템의 프로그램·테이블 구조가 포함되어 있습니다. **비공개(Private) 저장소로 운영**하세요.
