# PAC 운영자 매뉴얼 저장소 — AI 조회 규약

이 저장소는 SAP 결산자동화 솔루션 **PAC(Process Automatic Channel)** 운영자 매뉴얼 21종을
Markdown으로 변환하고, 토큰 효율을 위해 **3단 인덱스 구조**로 재구성한 것입니다.

## 절대 규칙

1. **문서 전체를 읽지 마세요.** 항상 인덱스로 대상 파일을 특정한 뒤, 그 파일 하나만 읽습니다.
2. `docs/` 아래 파일은 장(chapter) 단위로 분할되어 있습니다. `README.md`는 해당 문서의 목차입니다.
3. 매뉴얼에 없는 내용은 추측하지 말고 **"매뉴얼에 기재되어 있지 않습니다"** 라고 답하세요.
   PAC은 고객사별 커스터마이징이 있는 솔루션이므로 일반적인 SAP 지식으로 보완 추정하면 안 됩니다.
4. 답변 끝에 **근거 파일 경로와 섹션**을 반드시 표기하세요. 예: `docs/auto-trigger/03-...md#3.2`

## 조회 순서

| 질문 유형 | 첫 조회 대상 |
|---|---|
| 프로그램/T-Code 번호가 있음 (`ZLPAC0070` 등) | `index/programs.md` |
| 테이블명이 있음 (`ZTPAC_*`) | `index/tables.md` |
| 함수/클래스명이 있음 (`ZFPAC_*`, `ZCL_*`) | `index/functions.md` |
| 오류·증상·"안 돼요" 유형 | `index/troubleshooting.md` |
| 용어 정의 | `index/glossary.md` |
| 그 외 업무 주제 | `INDEX.md` (키워드 라우팅 → 문서 목록) |

인덱스에서 얻은 링크(`docs/...#앵커`)의 **파일 1개만** 읽고 답변합니다.
부족하면 같은 문서의 `README.md` 목차를 보고 **필요한 장만 추가로** 읽습니다.

## 디렉터리 구조

```
INDEX.md              마스터 인덱스 (여기서 시작)
index/                역인덱스 5종 (프로그램·테이블·함수·용어·트러블슈팅)
docs/<slug>.md        단일 파일 문서
docs/<slug>/          분할 문서 (README.md = 목차, NN-*.md = 장)
assets/<slug>/        화면 캡처 이미지
tools/                DOCX → Markdown 재변환 스크립트
```

## 문서 메타데이터

각 문서 최상단 YAML front-matter에 `category`, `programs`, `tables`, `functions`, `summary`가 있습니다.
문서를 특정할 때 이 필드를 활용하세요.

## 용어 주의

- **Activity** = 결산 작업 1단위(Closing ID). SAP 표준 용어가 아닌 PAC 고유 개념입니다.
- **BusPkg(BUPAK)** = Business Package. PAC 설정의 최상위 키입니다.
- `ZLPAC*` = 프로그램/트랜잭션, `ZTPAC*` = 테이블, `ZFPAC*` = Function Module, `ZCL_PAC*` = 클래스
