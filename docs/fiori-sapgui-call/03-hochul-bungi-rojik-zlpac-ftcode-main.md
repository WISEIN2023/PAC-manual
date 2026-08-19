---
id: fiori-sapgui-call/03-hochul-bungi-rojik-zlpac-ftcode-main
doc: fiori-sapgui-call
title: 3. 호출 분기 로직 (ZLPAC_FTCODE_MAIN)
parent: docs/fiori-sapgui-call/README.md
---

# 3. 호출 분기 로직 (ZLPAC_FTCODE_MAIN)

ZLPAC_FTCODE 는 START-OF-SELECTION 시점에 파라미터를 평가하여 호출 유형을 하나로 결정합니다. 판정은 위에서부터 순차적으로 이루어지며, 먼저 일치하는 조건의 분기만 실행됩니다.

## 3.1 전체 분기 흐름

| 순서 | 판정 조건 | 실행 | 호출 유형 |
|---|---|---|---|
| ① | P_RTYPE 값 존재 | CALL_RELATIVE | Relative 실행 |
| ② | P_TDTYPE 값 존재 | CALL_TODO_DISPLAY | To-Do 조회 |
| ③-a | REPTY = 'C' | SUBMIT_SCHEDULE_CHANGE | 결산일정 변경 |
| ③-b | TCODE 없음 + Legacy RFC/URL 존재 | CALL_URL | 레거시 URL 연계 |
| ③-c | P_TCODE 존재 + P_PID 없음 | CALL_DIRECT_TCODE | 직접 트랜잭션 호출 |
| ③-d | P_CID 존재 | SUBMIT_CID | Category 기반 실행 |
| ③-e | 그 외(기본) | SUBMIT_PID | Activity 직접 실행 |

③ 항목(a~e)은 P_RTYPE·P_TDTYPE가 모두 비어 있는 ‘Activity Link’ 경로에서만 평가됩니다. 이 경로에서는 먼저 Activity 정의 마스터(ZTPAC_PROC)를 P_BUPAK·P_PID로 조회한 뒤, 조회된 정의값(REPTY·TCODE·LEGACY_* 등)과 입력 파라미터를 함께 사용하여 a~e를 순서대로 판정합니다.

> ■ 시스템 확인 — 분기 원천<br>인클루드 ZLPAC_FTCODE_MAIN의 START-OF-SELECTION 소스에서 위 분기 순서를 확인함.<br>③ 경로의 마스터 조회 : SELECT SINGLE * FROM ZTPAC_PROC WHERE BUPAK = P_BUPAK AND PID = P_PID.

> START-OF-SELECTION.<br>IF P_RTYPE IS NOT INITIAL. " ① Relative<br>ZCL_PAC_NETGRAPH=>CALL_RELATIVE( ... ).<br>ELSEIF P_TDTYPE IS NOT INITIAL. " ② To-Do<br>PERFORM CALL_TODO_DISPLAY.<br>ELSE. " ③ Activity Link<br>SELECT SINGLE * INTO CORRESPONDING FIELDS OF @GS_PROC<br>FROM ZTPAC_PROC WHERE BUPAK = @P_BUPAK AND PID = @P_PID.<br>IF GS_PROC-REPTY EQ 'C'. PERFORM SUBMIT_SCHEDULE_CHANGE. " a<br>ELSEIF GS_PROC-TCODE IS INITIAL AND<br>( GS_PROC-LEGACY_RFC IS NOT INITIAL OR<br>GS_PROC-LEGACY_URL IS NOT INITIAL ). PERFORM CALL_URL. " b<br>ELSEIF P_TCODE IS NOT INITIAL AND P_PID IS INITIAL.<br>PERFORM CALL_DIRECT_TCODE. " c<br>ELSEIF P_CID IS NOT INITIAL. PERFORM SUBMIT_CID. " d<br>ELSE. PERFORM SUBMIT_PID. " e<br>ENDIF.<br>ENDIF.

[코드 3-1] ZLPAC_FTCODE_MAIN 분기 로직 (시스템 소스 요약)

## 3.2 분기 판정에 사용되는 마스터 필드

③ 경로의 판정 기준이 되는 ZTPAC_PROC(Activity Definition Master)의 주요 필드입니다.

| 필드 | 의미 | 분기에서의 역할 |
|---|---|---|
| REPTY | Report Type | 값이 'C' 이면 결산일정 변경(③-a)으로 분기 |
| TCODE | Activity 실행 트랜잭션 | 비어 있고 Legacy 값이 있으면 URL 연계(③-b) |
| LEGACY_RFC / LEGACY_URL | 레거시 연계 대상 | 존재 시 CALL_URL 대상 판정(③-b) |
| CALLTYP | 호출 방식 | 'P'=프로그램 SUBMIT, 그 외='T'=CALL TRANSACTION(4.1) |
| CID | 결산점검 Category | SUBMIT_CID 경로에서 대상 산정에 사용 |
| XSKIP | 첫 화면 SKIP 여부 | 실행 시 첫 화면 생략 제어(5.3) |

> ■ 시스템 확인 — ZTPAC_PROC<br>테이블 ZTPAC_PROC : 설명 “Activity Definition Master”, 키 = MANDT·BUPAK·PID. 위 필드(REPTY·TCODE·CALLTYP·CID·XSKIP·LEGACY_RFC·LEGACY_URL) 존재 확인됨.
