# 매뉴얼 갱신 운영 가이드

이 저장소를 **어떻게 최신 상태로 유지할 것인가**에 대한 문서입니다.
Git이 처음인 담당자도 그대로 따라 할 수 있도록 명령어 단위로 적었습니다.

- 대상 저장소: `pac-manual`
- 원본 위치: `E:\700. PAC 메뉴얼관리\PAC Manual(DOCX)`
- 실행 환경: 담당자 로컬 PC (Windows 기준)

---

## 0. 3분 요약

가장 흔한 작업인 **"기존 매뉴얼 내용을 고쳤다"** 의 전체 흐름입니다.

```
① Word로 DOCX 수정 후 저장
      ↓
② update.bat 더블클릭  (변환 + 인덱스 + 검증이 한 번에 실행)
      ↓
③ CONVERSION_REPORT.md 에서 커버리지 / 링크 오류 확인
      ↓
④ git add . → git commit → git push
      ↓
⑤ 인덱스가 바뀌었으면 Claude Project 지식 파일 교체
```

---

## 1. 반드시 지켜야 할 3가지 원칙

### 원칙 1 — 원본은 DOCX입니다

내용 수정은 **항상 DOCX에서** 합니다. `docs/` 안의 `.md` 파일을 직접 고치지 마세요.

> `tools/build.py`는 실행할 때마다 `docs/`와 `assets/` 폴더를 **통째로 지우고 다시 만듭니다.**
> md를 직접 고치면 다음 갱신 때 **아무 경고 없이 사라집니다.**

md를 직접 고쳐도 되는 예외는 다음 4개뿐입니다. 이 파일들은 변환 대상이 아닙니다.

| 파일 | 성격 |
|---|---|
| `README.md` | 저장소 안내 |
| `CLAUDE.md` | AI 조회 규약 |
| `MAINTENANCE.md` | 이 문서 |
| `tools/README.md` | 도구 설명 |

### 원칙 2 — 인덱스는 손으로 만들지 않습니다

`INDEX.md`와 `index/` 5개 파일은 **전부 자동 생성물**입니다.
프로그램·테이블·함수 목록은 문서 본문을 스캔해서 만들어지므로, DOCX에 `ZLPAC0080`을 새로 쓰면
갱신 실행만으로 `index/programs.md`에 자동으로 나타납니다. 직접 추가할 필요가 없습니다.

### 원칙 3 — 검증 통과 후에 push 합니다

`CONVERSION_REPORT.md`에서 아래 두 가지를 확인하기 전에는 push 하지 마세요.

- 깨진 파일 링크 **0건**, 깨진 앵커 **0건**
- 전체 커버리지 **99% 이상**

---

## 2. 최초 1회만 하는 환경 준비

### 2-1. Python 설치 확인

PowerShell을 열고:

```powershell
python --version
```

`Python 3.9` 이상이 나오면 됩니다. 없다면 https://www.python.org/downloads/ 에서 설치하고,
설치 화면에서 **"Add Python to PATH"** 를 반드시 체크하세요.

### 2-2. 필요한 패키지 설치

```powershell
pip install python-docx pillow
```

### 2-3. Git 설치 확인

```powershell
git --version
```

없다면 https://git-scm.com/download/win 에서 설치합니다.

### 2-4. 저장소 내려받기

작업할 폴더에서 (예: `E:\700. PAC 메뉴얼관리\`)

```powershell
cd "E:\700. PAC 메뉴얼관리"
git clone https://github.com/<계정>/pac-manual.git
cd pac-manual
```

### 2-5. Git 사용자 정보 등록 (최초 1회)

```powershell
git config --global user.name "홍길동"
git config --global user.email "hong@wiseinsoft.com"
```

### 2-6. update.bat 경로 확인

저장소 루트의 `update.bat`을 메모장으로 열어 첫 부분 경로가 실제 원본 폴더와 같은지 확인합니다.

```bat
set PAC_DOCX_SRC=E:\700. PAC 메뉴얼관리\PAC Manual(DOCX)
```

---

## 3. 시나리오별 절차

### 시나리오 A — 기존 매뉴얼 내용을 수정했다 (가장 흔함)

가장 단순한 경우입니다. **registry 수정 없이** 변환만 다시 돌리면 됩니다.

1. Word에서 해당 DOCX를 수정하고 저장합니다. 파일명은 바꾸지 마세요.
2. Word를 **완전히 닫습니다.** (열려 있으면 임시 파일 때문에 변환이 실패할 수 있습니다.)
3. 저장소 루트의 `update.bat`을 더블클릭합니다.
4. 마지막에 출력되는 변경 파일 목록을 확인합니다.
5. `CONVERSION_REPORT.md`를 열어 검증 결과를 확인합니다. (→ 4장)
6. 커밋하고 push 합니다.

```powershell
cd "E:\700. PAC 메뉴얼관리\pac-manual"
git add .
git commit -m "Auto Trigger 매뉴얼 3.2절 Trigger Code 필드 설명 보완"
git push
```

### 시나리오 B — 신규 매뉴얼을 추가한다

새 DOCX가 하나 늘어난 경우입니다. **`tools/registry.py`에 한 항목을 추가**하는 단계가 추가됩니다.

1. 새 DOCX를 `PAC Manual(DOCX)` 폴더에 넣습니다.
2. `tools/registry.py`를 메모장이나 VS Code로 열고, `DOCS = [` 목록 안에 아래 형태로 추가합니다.

```python
 dict(file="배치모니터링_운영자_메뉴얼.docx", slug="batch-monitoring", cat="모니터링·알림",
      title="배치 모니터링 운영자 매뉴얼",
      summary="배치 잡 실행 현황 조회와 실패 잡 재기동 절차"),
```

| 항목 | 규칙 |
|---|---|
| `file` | **DOCX 파일명과 정확히 일치**해야 합니다. 확장자 포함, 공백·언더스코어까지 동일하게 |
| `slug` | 영문 소문자·하이픈만. 파일 경로가 되므로 한글·공백 금지. 다른 문서와 중복 금지 |
| `cat` | 기존 6개 중 하나: `기반설정` `마스터` `실행·자동화` `모니터링·알림` `연계` `이관·운영` |
| `title` | 화면에 보이는 문서 제목. `매뉴얼` 표기로 통일 |
| `summary` | 한 문장. **이 문장이 `INDEX.md`에 그대로 실려 AI가 문서를 고르는 근거가 됩니다.** 어떤 프로그램·업무를 다루는지 구체적으로 |

3. (권장) `tools/gen_root.py` 상단 `ROUTE` 목록에도 키워드 한 줄을 추가합니다.
   이건 자동 생성되지 않는 유일한 부분입니다. 없어도 문서 목록에는 나오지만, 키워드 라우팅이 더 정확해집니다.

```python
 ("배치 모니터링, 실패 잡, 재기동", "batch-monitoring"),
```

4. `update.bat` 실행 → 검증 확인 → 커밋/push. (시나리오 A의 3~6단계와 동일)

### 시나리오 C — 매뉴얼을 삭제하거나 파일명을 바꿨다

1. **삭제**: `tools/registry.py`에서 해당 `dict(...)` 항목을 지웁니다.
   `docs/`는 매번 새로 만들어지므로 남은 파일을 손으로 지울 필요는 없습니다.
2. **파일명 변경**: `registry.py`의 `file` 값을 새 파일명으로 고칩니다.
   - `slug`은 **가능하면 바꾸지 마세요.** slug을 바꾸면 파일 경로가 바뀌고,
     Claude Project에 등록해 둔 인덱스나 외부에 공유한 링크가 전부 깨집니다.
3. `update.bat` 실행 → 커밋/push.

> 파일명만 바꾸고 registry를 안 고치면 실행 시 아래 오류가 납니다. 안내대로 `file` 값을 고치면 됩니다.
> `[오류] tools/registry.py 에 등록된 DOCX 파일이 폴더에 없습니다.`

### 시나리오 D — 요약문·카테고리·키워드만 손보고 싶다

DOCX는 그대로 두고 `registry.py`의 `summary` / `cat` / `title` 이나
`gen_root.py`의 `ROUTE`만 고친 경우입니다. 전체 변환은 필요 없습니다.

```powershell
$env:PAC_DOCX_SRC = "E:\700. PAC 메뉴얼관리\PAC Manual(DOCX)"
python tools\build.py
python tools\gen_root.py
```

> `summary`·`title`은 각 문서 md의 front-matter에도 들어가므로 `build.py`를 함께 돌려야 합니다.
> `ROUTE`만 고쳤다면 `gen_root.py` 하나만 돌려도 됩니다.

### 시나리오 E — 이미지(화면 캡처)만 교체했다

DOCX 안의 캡처를 새로 붙였다면 시나리오 A와 동일합니다.
`assets/` 폴더는 매번 새로 만들어지므로 옛 이미지는 자동으로 정리됩니다.

---

## 4. 검증 결과 읽는 법

`update.bat` 실행이 끝나면 `CONVERSION_REPORT.md`가 새로 만들어집니다. 아래 3곳만 보면 됩니다.

### ① 최상단 요약

```
- 원본 DOCX 21건 (36.2 MB) → Markdown 200개 파일 (1016 KB) + 이미지 287장 (11.6 MB)
- 내부 링크 1483개 검사: 깨진 파일 링크 0건, 깨진 앵커 0건
```

**깨진 링크·앵커는 반드시 0건이어야 합니다.** 0이 아니면 아래 "링크 오류" 절에 목록이 나옵니다.

### ② 문서별 텍스트 커버리지 표

원본 DOCX의 문단·표 셀을 하나씩 변환 결과와 대조한 비율입니다.

| 커버리지 | 판단 |
|---|---|
| 98% 이상 | 정상. 누락분은 Word 자동목차·표지 문구입니다 |
| 95~98% | 확인 권장. "누락 항목 분류"의 잔여 목록을 보세요 |
| 95% 미만 | **push 하지 말고 원인 확인.** 특수 서식(도형, 텍스트 상자, SmartArt)이 원인일 가능성이 큽니다 |

### ③ 누락 항목 분류

```
누락 59건 중 49건은 의도적으로 제거한 요소입니다.
분류되지 않은 잔여 항목: 1건
```

**"분류되지 않은 잔여 항목"** 에 실제 본문 문장이 올라와 있다면 변환에서 빠진 것입니다.
해당 문장이 Word에서 어떤 서식인지 확인하세요. 도형·텍스트 상자 안의 글자는 변환되지 않으므로,
**일반 문단이나 표로 옮겨 적은 뒤** 다시 변환하면 해결됩니다.

---

## 5. Git 명령어 최소 세트

| 하고 싶은 것 | 명령어 |
|---|---|
| 내가 뭘 바꿨는지 보기 | `git status` |
| 무엇이 어떻게 바뀌었는지 보기 | `git diff` |
| 변경 전체를 커밋 대상에 올리기 | `git add .` |
| 커밋 (설명 남기기) | `git commit -m "설명"` |
| 서버로 올리기 | `git push` |
| 다른 사람 변경분 받아오기 | `git pull` |
| 최근 커밋 목록 보기 | `git log --oneline` |

### 커밋 메시지 쓰는 법

무엇을 왜 바꿨는지 한 줄로 씁니다. 나중에 "언제 이 내용이 바뀌었지?"를 찾는 단서가 됩니다.

```
좋음   결산일정 매뉴얼 v1.2 반영 — Super User 등록 절차 변경
좋음   Auto Trigger 신규 매뉴얼 추가
좋음   권한 매뉴얼 트러블슈팅 3개 케이스 추가

나쁨   수정
나쁨   update
나쁨   ㅁㄴㅇㄹ
```

### 작업 시작 전에는 항상 pull

여러 명이 같은 저장소를 쓴다면, 작업 전에 최신 상태를 받아 두세요.

```powershell
git pull
```

---

## 6. 자주 하는 실수와 해결

| 증상 | 원인 | 해결 |
|---|---|---|
| `[오류] 원본 DOCX 폴더를 찾을 수 없습니다` | `PAC_DOCX_SRC` 경로가 틀림 | `update.bat` 안의 경로를 실제 폴더와 맞춤 |
| `[오류] registry.py 에 등록된 DOCX 파일이 폴더에 없습니다` | 파일명 변경 또는 오타 | `registry.py`의 `file` 값을 실제 파일명과 일치시킴 |
| `PackageNotFoundError` | Word에서 파일이 열려 있음 (`~$` 임시 파일) | Word를 완전히 닫고 재실행 |
| `ModuleNotFoundError: No module named 'docx'` | 패키지 미설치 | `pip install python-docx pillow` |
| `python: command not found` | Python이 PATH에 없음 | Python 재설치 시 "Add Python to PATH" 체크 |
| md를 고쳤는데 다음 갱신에서 사라짐 | 원칙 1 위반 | DOCX에서 수정 후 재변환 |
| push 했는데 GitHub에 이미지가 안 보임 | `assets/`가 커밋되지 않음 | `git add .` 로 전체를 올렸는지 확인 |
| `Updates were rejected` | 다른 사람이 먼저 push함 | `git pull` 후 다시 `git push` |

---

## 7. 되돌리기 (롤백)

### 아직 커밋하지 않았다면 — 변경 전부 버리기

```powershell
git checkout -- .
```

### 이미 커밋했지만 push 전이라면 — 마지막 커밋 취소

```powershell
git reset --soft HEAD~1
```

`--soft`는 파일 내용은 그대로 두고 커밋만 취소합니다.

### 이미 push까지 했다면 — 되돌리는 커밋을 새로 만들기

```powershell
git log --oneline          # 되돌릴 커밋 ID 확인 (예: a1b2c3d)
git revert a1b2c3d
git push
```

> `git reset --hard`는 작업 내용이 복구 불가능하게 사라질 수 있으므로 사용하지 마세요.
> 어떤 경우든 원본 DOCX만 있으면 저장소는 언제든 다시 만들 수 있습니다.

---

## 8. Claude 연계 갱신

저장소를 push했다고 Claude가 바로 최신 내용을 보는 것은 아닙니다.
연계 방식에 따라 갱신 시점이 다릅니다.

| 연계 방식 | 갱신 시점 |
|---|---|
| GitHub MCP로 저장소를 직접 조회 | push 즉시 반영. 별도 작업 없음 |
| `INDEX.md`·`index/`를 Claude Project 지식에 등록 | **수동 교체 필요** |

Project 지식에 인덱스를 올려 두셨다면, 아래 경우에 파일을 다시 올려야 합니다.

- 문서가 추가·삭제된 경우 → `INDEX.md` 교체
- 프로그램·테이블·함수가 새로 등장한 경우 → `index/programs.md`, `index/tables.md`, `index/functions.md` 교체
- 용어집·트러블슈팅 항목이 늘어난 경우 → `index/glossary.md`, `index/troubleshooting.md` 교체

> 판단이 애매하면 `git diff --stat` 결과에 `INDEX.md`나 `index/`가 보이는지로 결정하세요.
> 목록에 있으면 그 파일만 교체하면 됩니다.

### 갱신 후 확인 질의

인덱스를 교체한 뒤 아래 4가지 유형을 한 번씩 물어보고 정상 응답하는지 확인하세요.

1. 프로그램 번호 — "ZLPAC0070은 무슨 프로그램인가요?"
2. 증상 — "Fiori에서 법인이 안 보입니다"
3. 용어 — "PAC에서 BUPAK이 뭔가요?"
4. 업무 주제 — "Auto Trigger를 새로 설정하는 절차 알려주세요"

응답에 **근거 파일 경로가 함께 표기되는지** 확인하는 것이 핵심입니다.
경로가 없거나 엉뚱한 문서를 참조하면 `CLAUDE.md`의 조회 규약이 적용되지 않은 것입니다.

---

## 9. 갱신 체크리스트

작업할 때 그대로 복사해서 쓰세요.

```
[ ] 1. git pull 로 최신 상태 받기
[ ] 2. DOCX 수정 후 Word 완전히 닫기
[ ] 3. 신규/삭제/파일명 변경이면 tools/registry.py 수정
[ ] 4. update.bat 실행
[ ] 5. CONVERSION_REPORT.md — 깨진 링크·앵커 0건 확인
[ ] 6. CONVERSION_REPORT.md — 커버리지 98% 이상 확인
[ ] 7. git status 로 변경 파일 확인
[ ] 8. git add . / git commit -m "설명" / git push
[ ] 9. INDEX.md·index/ 가 바뀌었으면 Claude Project 지식 교체
[ ] 10. 확인 질의 4종 실행
```

---

## 10. 참고 — 스크립트 구성

`update.bat`은 아래 4개를 순서대로 실행합니다. 개별 실행이 필요할 때 참고하세요.

| 순서 | 스크립트 | 하는 일 | 만드는 것 |
|---|---|---|---|
| 1 | `tools/build.py` | DOCX를 Markdown으로 변환하고 장 단위로 분할 | `docs/`, `assets/`, `.manifest.json` |
| 2 | `tools/gen_index.py` | 본문을 스캔해 역인덱스 생성 | `index/` 5종 |
| 3 | `tools/gen_root.py` | 문서 목록과 키워드 라우팅 구성 | `INDEX.md` |
| 4 | `tools/validate.py` | 원본 대조·링크 검사·고아 이미지 정리 | `CONVERSION_REPORT.md` |

분할 기준을 바꾸고 싶다면:

- 문서 분할 임계값 — `tools/registry.py`의 `SPLIT_THRESHOLD` (기본 12,000자)
- 장 추가 분할 임계값 — `tools/build.py`의 `SUB_SPLIT` (기본 9,000자)

값을 줄이면 파일이 더 잘게 쪼개져 1회 조회 토큰이 줄지만, 파일 수가 늘어 라우팅이 복잡해집니다.
현재 값은 파일당 3~9천 자(조회 시 약 5~8K 토큰)를 목표로 맞춘 것입니다.
