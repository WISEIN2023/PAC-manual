---
id: log-management/06-gwanryeon-johoe-hamsu
doc: log-management
title: 6. 관련 조회 함수
parent: docs/log-management/README.md
---

# 6. 관련 조회 함수

로그 및 전기 문서 조회에 사용되는 함수 모듈은 다음과 같다. 모두 패키지 ZPAC에 속한다.

## 6.1 함수 목록

| 함수 모듈 | Function Group | 설명 |
|---|---|---|
| ZFPAC_LOG_DISPLAY | ZPAC110 | Display Activity Log — Activity 로그를 조회·표시한다. |
| ZFPAC_LOG_POSTDOC | ZPAC011 | Return Complete Document List — 완료된 문서 목록을 반환한다. |
| ZFPAC_DISPLAY_POST_DOC | ZPAC110 | Display Posted Document List — 전기된 문서 목록을 조회·표시한다. |
| ZFPAC_LOG_PARAM_INIT | ZPAC027 | Get Common Parameter Initial Value — 공통 파라미터 초기값을 조회한다. |

## 6.2 ZFPAC_LOG_DISPLAY — Display Activity Log

**기능 요약**

Fiori 및 Log History에서 Activity별 실행 상세 로그 메시지를 조회하는 핵심 함수이다. 특정 Log ID에 해당하는 Activity 실행 로그 메시지를 조회하여 Fiori 화면에 표시할 수 있도록 데이터를 반환한다. Time Zone 변환, 전기 문서 여부 표시, 중복 메시지 집계 등 로그 표시에 필요한 모든 후처리를 포함하며, 팝업 모드(IV_POPUP='X')인 경우 직접 ALV 화면을 호출한다(Log History에서 호출).

**프로세스 흐름**

| 단계 | 처리 | 내용 |
|---|---|---|
| ① | 초기화 | 입력 파라미터를 내부 공통 구조체(GS_PARAM)에 복사하고 내부 테이블(GT_LOG, GT_DETAIL 등)을 초기화한다. |
| ② | 로그 데이터 조회<br>(GET_DATA) | 1) ZTPAC_LOG_DTL에서 Log ID에 해당하는 로그 메시지 전체를 조회한다.<br>2) 연관 Error Help 정보(ZTPAC_HELP_USED)도 함께 읽어온다. |
| ③ | 수행 사용자 정보 추가<br>(CREATE_USERINFO_LOG) | Log Header(ZTPAC_LOG_HDR)에서 실행 사용자 정보를 읽어 로그 상단에 별도 행으로 추가한다. |
| ④ | 로그 집계<br>(MERGE_LOG_DETAIL) | 동일 메시지가 반복 발생한 경우 건수를 집계(LCNT)하여 하나의 행으로 합산한다. Message Class/ID, 파라미터(PARAM1~4) 기준으로 그룹화하며, ZTPAC_LOG_COLMSG를 읽어 예외처리된 Message Class/ID는 합산에서 제외한다. |
| ⑤ | 전기 문서 메시지 식별<br>(APPEND_GT_LOG_BLMSG) | ZTPAC_LOG_BLMSG 마스터와 비교하여 Message Class·ID가 동일한 로그는 'B(LCNT_TYPE)'로 표시한다. Fiori 노드에 Posting 아이콘으로 표시한다. |
| ⑥ | Time Zone 변환 | 조직의 기준 Time Zone(ZFPAC_TZONE_CONVERT 호출)으로 로그 발생 시각을 변환한다. IV_TZONE 미입력 시 조직의 첫 번째 Time Zone을 기본값으로 사용한다. |
| ⑦ | 메시지 유형 보정 | 1) Mass Error 종료 문구(ZPAC01/032)는 'S(정상)'로 재분류하여 에러 건수에서 제외한다.<br>2) STD 메시지 중 도움말(DOCU_INIT)이 등록된 경우 Help 아이콘을 표시한다.<br>3) Message ID에 따라 LCNT_TYPE의 유형을 입력한다. |
| ⑧ | 팝업 화면 호출<br>(옵션) | IV_POPUP='X'인 경우 로그 건수에 따라 크기를 조절한 팝업(Screen 0100)을 호출한다. |
| ⑨ | 파라미터 상세 반환<br>(옵션) | IV_LOGSEQ 또는 IV_MSGID/IV_MSGNR 필터가 입력된 경우 해당 메시지의 파라미터(PARAM1~4) 건별 상세를 ET_PARAM에 반환한다. |

**연관 테이블**

| 테이블 | 처리 | 용도 |
|---|---|---|
| ZTPAC_LOG_DTL | SELECT | 로그 상세 메시지 조회 |
| ZTPAC_LOG_HDR | SELECT | 로그 헤더 조회 — 실행 사용자·상태 |
| ZTPAC_LOG_BLMSG | SELECT | 전기 문서 메시지 기준 마스터 조회 |
| ZTPAC_HELP_USED | SELECT | Where Used 정보 조회 |
| I_JOURNALENTRY | SELECT | SAP 표준 전표 CDS — 전기 전표 조회 |

## 6.3 ZFPAC_LOG_POSTDOC — 전기 완료 전표 목록 반환

**기능 요약**

특정 PAC 프로세스(PID) 실행 결과로 생성된 회계 전표(전기 완료 문서) 목록을 반환한다. 로그 메시지에서 전표 번호와 회계연도를 추출한 뒤 SAP 표준 전표 CDS를 조회하여 최종 회사코드·전표번호·회계연도·기간 정보를 제공한다.

**입력 /출력 파라미터**

| 구분 | 항목 | 내용 |
|---|---|---|
| 입력 | 조직 / 기간 | IV_BUPAK(Business Package), IV_BUKRS(회사코드), IV_GSBER(사업영역), IV_CUNIT(기타조직), IV_GJAHR(회계연도), IV_MONAT(회계기간) — 전표 조회 범위 특정. |
|  | 프로세스 식별 | IV_PID(PAC ID) — 어떤 Activity의 전기 결과를 조회할지 특정. IV_LOGID(로그 ID), IV_LOGSEQ(로그 순번) — 특정 실행 건의 로그를 대상으로 조회. |
| 출력 | ET_LIST | 전기 완료 전표 목록(ZYPAC_POST_DOCLIST). 각 행에 회사코드(BUKRS), 전표번호(BELNR), 회계연도(GJAHR), 기간(MONAT) 포함. |
|  | ES_RETURN | 처리 결과 메시지(BAPIRET2). 오류 발생 시 유형 'E'와 메시지 내용 반환. |

**프로세스 흐름**

| 단계 | 처리 | 내용 |
|---|---|---|
| ① | 조직 유효성 검사 | ZCL_PAC_ORG=>CHECK_VALID_ORG를 호출하여 입력된 조직 정보가 PAC 시스템에 유효하게 등록되어 있는지 확인한다. 유효하지 않으면 처리를 중단하고 오류를 반환한다. |
| ② | 전기 문서 메시지 기준 조회 | ZTPAC_LOG_BLMSG 테이블에서 '전기 완료'를 의미하는 메시지 정의 목록을 전체 조회한다. 이 기준에 해당하는 메시지가 로그에 기록되어야 전표 번호를 추출할 수 있다. |
| ③ | 로그 메시지 조회<br>(ZFPAC_LOG_DISPLAY 호출) | ZFPAC_LOG_DISPLAY를 호출하여 해당 Log ID/Seq의 로그 파라미터 상세(ET_PARAM)를 받아온다. 파라미터에는 전표번호(BELNR)·회계연도(GJAHR)가 포함되어 있다. |
| ④ | 전표 번호 추출 | 반환된 파라미터 목록을 순회하면서 ZTPAC_LOG_BLMSG 정의와 매칭되는 행의 GJAHR_PARAM, BELNR_PARAM 필드명으로 실제 전표번호와 연도를 동적으로 읽어낸다. 선행 0 처리(CONVERSION_EXIT_ALPHA_INPUT)를 거쳐 표준 전표번호 형식으로 변환한다. |
| ⑤ | 중복 제거 | 추출된 전표 목록에서 동일한 회계연도·전표번호 쌍을 제거하여 중복 없는 리스트를 구성한다. |
| ⑥ | 전표 상세 조회<br>(SAP 표준 CDS) | I_JOURNALENTRY CDS 뷰를 FOR ALL ENTRIES 방식으로 조회하여 회사코드·전표번호·회계연도·기간 정보를 ET_LIST에 담아 최종 반환한다. |

**연관테이블 /함수**

| 객체 | 처리 | 용도 |
|---|---|---|
| ZTPAC_LOG_BLMSG | SELECT | 전기 문서 메시지 기준 마스터 — 어떤 메시지가 전기 완료를 의미하는지 정의 |
| I_JOURNALENTRY | SELECT | SAP 표준 전표 CDS 뷰 — 회계 전표 헤더 정보 조회 |
| ZFPAC_LOG_DISPLAY | 함수 호출 | 로그 파라미터 상세 조회를 내부적으로 위임(직접 테이블 접근 없음) |

## 6.4 ZFPAC_DISPLAY_POST_DOC — 전기 문서 내역 화면 표시

**기능 요약**

특정 Log ID로 발생한 회계 전기 내역을 화면(Screen 500)에 표시한다. 계정별 집계(ALV 상단)와 전표 라인 상세(ALV 하단) 두 개의 ALV로 구성된 팝업을 제공하며, 전체화면(IV_FULL='X') 모드와 팝업 모드를 지원한다.

**입력 /출력 파라미터**

| 항목 | 내용 |
|---|---|
| IV_BUPAK | Business Package — 조회 대상 업무 패키지. |
| IV_LOGID | 로그 ID — 전기 내역을 조회할 실행 로그의 고유 식별자. |
| IV_LOGSEQ | 로그 순번 — 특정 메시지 순번을 기준으로 전기 문서를 필터링. |
| IV_FULL | 'X' 입력 시 전체화면 모드(Screen 500 직접 호출), 미입력 시 팝업 모드. |
| ES_RETURN | 처리 결과 메시지(BAPIRET2). 유효성 검사 실패 또는 데이터 없을 때 오류 정보 반환. |

**프로세스 흐름**

| 단계 | 처리 | 내용 |
|---|---|---|
| ① | 초기화 | 내부 ALV 테이블(GT_ALV5, GT_ALV6, GT_LOG_LIST) 및 제어 변수를 초기화하고 화면 제어 변수(GV_FULL, GV_LOGSEQ)를 설정한다. |
| ② | BusPkg 유효성 검사<br>(CHECK_BUPAK) | 입력된 IV_BUPAK가 PAC 시스템에 등록된 유효한 Business Package인지 확인한다. 오류 발생 시 ES_RETURN에 오류 메시지를 담고 처리를 중단한다. |
| ③ | 로그 헤더 존재 여부 확인<br>(CHECK_LOG_HDR) | IV_LOGID에 해당하는 로그 헤더(ZTPAC_LOG_HDR)가 실제로 존재하는지 검증한다. 존재하지 않으면 오류 처리 후 중단한다. |
| ④ | 전기 문서 목록 조회<br>(READ_LOG_POSTDOC) | ZFPAC_LOG_POSTDOC을 내부적으로 활용하여 해당 로그에서 생성된 회계 전표 목록을 조회하고 내부 테이블(GT_LOG_LIST)에 저장한다. |
| ⑤ | 전표 라인 상세 조회<br>(APPEND_GT_ALV6_FROM_BKPF) | 조회된 전표번호를 기준으로 BKPF/BSEG 또는 ACDOCA에서 전표 라인 상세 정보를 읽어 ALV 하단 테이블(GT_ALV6)에 추가한다. |
| ⑥ | 계정별 집계<br>(APPEND_GT_ALV5_FROM_ACDOCA) | ACDOCA(Universal Journal)에서 계정별 금액을 집계하여 ALV 상단 테이블(GT_ALV5)에 추가한다. |
| ⑦ | 계정명 표시<br>(MODIFY_GT_ALV5) | 계정 코드에 해당하는 계정명을 조회하여 ALV5 테이블에 반영한다. |
| ⑧ | 화면 호출 | IV_FULL='X'이면 Screen 500을 전체화면으로 호출. 미입력 시 STARTING AT / ENDING AT 좌표를 지정한 팝업 형태로 Screen 500을 호출한다. |

**연관테이블 /함수**

| 객체 | 처리 | 용도 |
|---|---|---|
| ZTPAC_LOG_HDR | SELECT | 로그 헤더 존재 여부 및 조직 정보 확인 |
| ZTPAC_LOG_BLMSG | SELECT | 전기 문서 메시지 기준 마스터(READ_LOG_POSTDOC 내부 사용) |
| ACDOCA | SELECT | SAP 표준 Universal Journal — 계정별 집계 및 전표 라인 조회 |
| BKPF / BSEG | SELECT | SAP 표준 전표 헤더/라인 — 전표 상세 정보 조회 |
| ZFPAC_LOG_POSTDOC | 함수 호출 | 전기 완료 전표 번호 목록 조회를 위임(내부 호출) |
| ZFPAC_LOG_DISPLAY | 함수 호출 | 로그 메시지 조회 및 파라미터 추출을 위임(간접 호출) |

**화면 구성**

| 구성 | 표시 항목 |
|---|---|
| ALV 상단 (GT_ALV5) | 계정별 집계 뷰: 계정코드, 계정명, 차변금액, 대변금액, 통화 등 표시. |
| ALV 하단 (GT_ALV6) | 전표 라인 상세 뷰: 전표번호, 항목번호, 전기키, 금액, 텍스트 등 표시. |
