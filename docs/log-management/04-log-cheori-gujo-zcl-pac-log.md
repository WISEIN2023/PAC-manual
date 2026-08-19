---
id: log-management/04-log-cheori-gujo-zcl-pac-log
doc: log-management
title: 4. Log 처리 구조 (ZCL_PAC_LOG)
parent: docs/log-management/README.md
---

# 4. Log 처리 구조 (ZCL_PAC_LOG)

로그의 실제 저장·상태 관리는 클래스 ZCL_PAC_LOG가 담당한다. 3장의 매크로(_PAC_START_LOG, _PAC_SAVE_LOG, _PAC_END_LOG)는 이 클래스의 메소드를 호출하는 진입점이다. 본 장은 운영·유지보수 시 로그가 어떤 흐름으로 처리되고 어떤 테이블에 저장되는지를 설명한다.

## 4.1 로그 상태값 정의

로그는 처리 진행에 따라 다음 상태값(IV_STATUS)을 갖는다. 운영 화면(맵)에서는 진행 중이면 노란색 등으로 상태가 표시된다.

| 상태코드 | 상태명 | 설명 |
|---|---|---|
| S | Start | 최초 Log Header 생성, Log ID 채번 |
| R | Running | 처리 중 — 개별 메시지 저장 |
| C | Complete | 정상 완료 |
| F | Fail | 오류로 인한 비정상 종료 |
| A | Abort / Cancel | 사용자 취소 또는 강제 종료 |
| K | Mass Error (Keep) | 오류 메시지 누적 저장 후 Fail 처리 |

## 4.2 로그 처리 흐름

### 4.2.1 [START] _PAC_START_LOG

로그 시작 시 ZCL_PAC_LOG 인스턴스를 생성하기 전에 다음 사전 검증을 순차적으로 수행한다. 어느 한 단계라도 통과하지 못하면 진행이 차단(Block)된다.

1. 호출 파라미터 메모리값 입력 — 년월, 조직, PID, T-Code 등 프로그램 호출 파라미터 메모리 정보를 Import한다.
2. Direct T-Code 접속 여부 — 자동(Auto) 대상 프로그램을 T-Code로 직접 수행한 경우, 비즈니스 패키지 Config(ZTPAC_CONFIG)의 Direct 허용 여부에 따라 차단한다.
3. GV_FORCED_PID 값이 입력된 경우 PID 값을 강제로 지정한다.
4. 스크린 파라미터 설정 — Activity Master Parameter에 설정된 값을 스크린 파라미터에 입력한다. ZTPACEXIT에 'LOG_ORG'로 EXIT가 등록된 경우 해당 함수를 호출하여 별도 값을 입력한다.
5. 필수 공통 파라미터 입력 여부 체크 — 비즈니스 패키지에 맞는 조직·기간 필수 필드가 누락되면 진행 불가. 단, Required Exception 처리된 파라미터는 오류 처리하지 않으며, Constant 지정 시 해당 값을, 그 외에는 메모리 값을 입력한다.
6. 비즈니스 패키지 마감 여부 체크 — ZTPAC_CLOSE의 마감 여부를 확인하여 마감된 경우 진행 불가.
7. 권한 체크 — 비즈니스 패키지 Config에 'Authorization check when log start' 설정 시 권한이 있는 경우만 진행(ZCL_PAC_AUTH=>CHECK_ORG_AUTH).
8. Final Activity 완료 체크 — 비즈니스 패키지 Config에 'Complete check when final activity execute' 설정 시 미완료이면 진행 불가.
9. 일정 마감 체크 — Actual 수행이면서 Activity Level 수행인 경우 일정 마감 여부를 확인(ZCL_PAC_CLOSING=>CHK_CLOSING_ALL)하여 마감 시 진행 불가.
10. 완료된 Activity 수행 여부 체크 — 비즈니스 패키지 Config에 'Block for execution when activity completed' 설정 시 완료 상태이면 진행 불가하며, Reset하여 상태를 초기화한 후 수행한다.
11. 위 로직을 모두 통과하면 ZCL_PAC_LOG 인스턴스(GRF_PAC_LOG)를 생성(CONSTRUCTOR)하고, ZPAC01/023(Activity is started) 메시지로 로그 시작을 기록한다(WRITE_LOG_MAIN, IV_STATUS = 'S').
Start 단계에서 WRITE_LOG_HEADER가 수행하는 주요 처리는 다음과 같다.

- Log ID 채번 — Number Range 오브젝트 ZPAC0_LOG_NROBJ에서 고유 Log ID를 생성한다.
- 헤더 구조체 구성 — Batch 수행 정보, 수행 유저(Execute User) 정보를 수집하여 ZTPAC_LOG_HDR에 입력한다.
- PAC Lock Object 생성 — Lock Key(조직·년월·PID 등)로 ENQUEUE_EZPACLCK_QUEUE를 수행한다. Lock이 이미 잡힌 경우 오류 처리 후 종료(WRITE_LOG_MAIN, IV_STATUS = 'E').
- 스크린 파라미터 값 입력(ZTPAC_LOG_SCREEN), 수행 프로그램 입력(ZTPAC_RUNNING).
- 좀비(Zombie) 로그 정리(DELETE_DUMMY_LOG).

### 4.2.2 [SAVE] _PAC_SAVE_LOG

1. SY-MSGID/MSGNO/MSGTY를 감지하여 오류(E·A·X)는 K(Mass Error)로, 정보(I·S)는 I(Information)로 분류한다.
2. _SET_LOG_PARAM을 호출하여 화면 하단에 메시지를 출력한다(GV_PAC_MSGOFF = X이면 미출력). PID가 없으면 로그가 테이블에 저장되지 않으므로 GT_FORE_LOG 인터널 테이블에 저장한다.
3. WRITE_LOG_MAIN(IV_STATUS = 'R')을 호출하여 WRITE_LOG_DETAIL을 수행한다.
WRITE_LOG_DETAIL의 주요 처리는 다음과 같다.

- Log Detail 입력(ZTPAC_LOG_DTL) — Log Sequence(AV_LOGSEQ)를 증가시킨다.
- 최대 로그 건수 초과 체크 — System Config 'Max number that logs can be created'(LOGMXCNT)에 설정된 수를 초과할 수 없다.
- 중복 메시지 체크 — 비즈니스 패키지 Config 'Delete Duplicated Log'(LOGDUPDEL) 설정 시, Message Class/ID와 Parameter 1~4가 동일하면 제거한다.
- 전기 문서 여부 체크 — ZTPAC_LOG_BLMSG에 등록된 Message Class/ID는 기표 관련으로 인식하여 Log Header의 STYPE을 'P'로 저장한다.
- Where Used 정보 저장(ZTPAC_HELP_USED).

### 4.2.3 [END] _PAC_END_LOG

1. _SET_LOG를 호출하여 화면 하단에 메시지를 출력한다(GV_PAC_MSGOFF = X이면 미출력).
2. GV_PAC_ERROR가 없으면 Complete(C), 있으면 Fail(F)로 WRITE_LOG_MAIN을 호출한다.
종료 단계의 주요 처리는 다음과 같다.

- 수행 종료 시간 계산 및 총 수행 시간(EXETM) UPDATE.
- Running 프로그램 목록 삭제(ZTPAC_RUNNING) 및 PAC Lock Object 해제(DEQUEUE).
- 최종 상태를 ZTPAC_STATUS에 반영하고, 하위 Activity 상태 변경 시 상위 상태를 Refresh(ZCL_PAC=>SYNC_PCSGP_STATUS)한다.
- 상태 변경 시 Fiori 화면으로 APC를 호출한다.
- Final Activity인 경우 비즈니스 패키지 종료 처리(CLOSE_BUPAK_FINAL) — 수행 조직/기간 마감(ZTPAC_CLOSE) 및 모델링 이력 저장(SAVE_HIST_AT_CLOSE).

## 4.3 ZCL_PAC_LOG 주요 메소드

운영·유지보수 시 자주 참조하는 ZCL_PAC_LOG의 메소드와 역할은 다음과 같다.

| 메소드명 | 구분 | 역할 (프로세스 관점) |
|---|---|---|
| CONSTRUCTOR | Public | 로깅 객체 초기화. 상위 클래스(ZCL_PAC) 생성자를 호출하여 조직정보(BUPAK/BUKRS/PID 등)를 주입하고, Lock 문자열과 Batch Job 정보를 설정한다. |
| WRITE_LOG_MAIN | Public | 로그 저장의 핵심 진입 메소드. 상태값(IV_STATUS)과 로그 케이스에 따라 처리 흐름을 분기한다. Start(S)는 WRITE_LOG_HEADER를, 이후에는 WRITE_RUNNING_TIME → WRITE_LOG_DETAIL을 수행한다. |
| WRITE_LOG_HEADER | Private | 로그 헤더를 최초 1회 생성. Log ID 채번, 수행자·IP·Batch Job·프로그램 ID 수집, PAC Lock 생성, 선택화면 파라미터 저장, 좀비 로그 정리를 수행한다. |
| WRITE_LOG_DETAIL | Private | 실제 로그 메시지 1건을 ZTPAC_LOG_DTL에 저장. Log Sequence 증가, 메시지 텍스트(T100) 구성, 최대 건수·중복 체크, 종료 상태 시 ZTPAC_STATUS 최종 업데이트를 수행한다. |
| WRITE_RUNNING_TIME | Private | 수행 시간 측정·기록. Start 시 시작 시간, End 시 종료 시간과 총 수행 시간(EXETM)을 계산하며, HOLD 기능으로 팝업 대기 시간을 제외한다. |
| CHECK_PAC_LOCKING | Public | 동일 프로세스 중복 실행 방지를 위한 Lock 설정. Actual 모드(EXEMODE='A')에서만 실제 Lock을 수행한다. |
| CREATE_LOGID | Class | Number Range 오브젝트(ZPAC0_LOG_NROBJ)에서 유니크한 Log ID를 채번한다. |
| DELETE_DUMMY_LOG | Private | 비정상 종료된 좀비 로그를 정리. Work Process 목록과 비교하여 실행 중이 아닌 항목을 Abort(A) 처리 후 삭제한다. |
| GET_LOCK_KEY | Class | 비즈니스 패키지별 Lock Key 문자열 생성. ZTPAC_CONFIG_LCK 설정이 있으면 정의된 필드 순서로, 없으면 기본 규칙으로 구성한다. |
| GET_SCREEN_PARAM | Public | 프로그램 선택화면의 입력값을 추출. ABAP Call Stack으로 최상위 실행 프로그램을 식별하여 저장 가능한 형태로 변환한다. |
| BUILD_MSG_TEXT | Class | 메시지 클래스/번호로 실제 메시지 텍스트 생성. 파라미터 치환 또는 T100 직접 조회로 문장을 만든다. |
| ON_LOG_START | Public | Log Start 시점에 사용자 정의 Exit Function을 호출하는 업무 확장 포인트(ZTPAC_PROC 정의). |
| SELECT_LOG_ID_FROM_PID | Public | PID와 조직정보로 현재 실행 중인 Log ID를 ZTPAC_STATUS에서 조회한다. |
| CHANGE_LOG_ID | Public | 외부에서 강제로 Log ID를 변경. 이전 상태를 저장하여 원복이 가능하게 한다. |
| HOLD_LOG_TIME | Public | 수행 시간 측정을 중단(H)/재개(S)한다. 팝업 대기 시간을 수행 시간에서 제외하는 데 사용한다. |
| PAC_POP_UP | Public | 사용자 확인/취소 팝업 제공. 팝업 표시 중 수행 시간 측정을 Hold한다. |

## 4.4 PAC Lock Checking

동일 조직/기간에 Activity가 이중 수행되는 것을 방지하기 위해 Lock Checking을 수행한다. Lock Checking은 로그 시작 시 자동으로 수행된다.

**Lock Key 기본규칙 :** T-Code + 조직정보 + Fiscal Year + Period

**보완설명**  Lock은 Actual 모드(EXEMODE='A')에서만 실제로 수행된다. 동일 세션의 본인 Lock은 허용되지만, 다른 세션의 본인 Lock 또는 다른 사용자의 Lock은 오류로 처리된다. Lock Key 구성은 ZTPAC_CONFIG_LCK 설정이 있으면 정의된 필드 순서를 따르고, 없으면 기본 규칙(BUKRS/GSBER/PID 등)으로 구성된다.

## 4.5 좀비(Zombie) 로그 정리

비정상 종료로 인해 ZTPAC_RUNNING에는 등록되어 있으나 실제로는 실행 중이 아닌 로그를 좀비 로그라 한다. 로그 시작 시 DELETE_DUMMY_LOG가 현재 서버의 Work Process 목록을 조회하여, 실행 중이 아닌 항목을 좀비로 판단하고 해당 로그의 상태를 'A(Abort)'로 업데이트한 후 삭제하여 시스템 정합성을 유지한다.
