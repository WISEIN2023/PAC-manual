# 변환 도구

원본 DOCX에서 이 저장소를 재생성하는 스크립트입니다.

## 사전 준비

```bash
pip install python-docx pillow
export PAC_DOCX_SRC="/path/to/PAC Manual(DOCX)"   # 원본 DOCX 폴더
```

## 실행 순서

```bash
python3 tools/build.py        # DOCX -> docs/, assets/, .manifest.json
python3 tools/gen_index.py    # index/ 5종 생성
python3 tools/gen_root.py     # INDEX.md 생성
python3 tools/validate.py     # CONVERSION_REPORT.md 생성 + 링크/앵커 검사
```

## 파일

| 파일 | 역할 |
|---|---|
| `registry.py` | 문서 목록(슬러그·카테고리·요약)과 분할 임계값. **신규 매뉴얼 추가 시 여기에 등록** |
| `converter.py` | DOCX → Markdown 변환 (헤딩·표·이미지·리스트·굵게) |
| `romanize.py` | 한글 제목 → ASCII 파일명 슬러그 |
| `build.py` | 문서별 변환 및 장 단위 분할 |
| `gen_index.py` | 프로그램/테이블/함수/용어/트러블슈팅 역인덱스 생성 |
| `gen_root.py` | 마스터 인덱스(INDEX.md) 생성 |
| `validate.py` | 원본 대비 커버리지·링크·앵커 검증 |

## 분할 기준

- 문서 본문 12,000자 초과 → H1(장) 단위 분할
- 장 본문 9,000자 초과 → H2(절) 단위 추가 분할
- `registry.py`의 `SPLIT_THRESHOLD`, `build.py`의 `SUB_SPLIT`에서 조정
