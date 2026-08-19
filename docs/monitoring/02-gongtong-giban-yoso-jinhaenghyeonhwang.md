---
id: monitoring/02-gongtong-giban-yoso-jinhaenghyeonhwang
doc: monitoring
title: 2. 공통 기반 요소 (진행현황 모니터링 계열)
parent: docs/monitoring/README.md
---

# 2. 공통 기반 요소 (진행현황 모니터링 계열)

ZLPAC_MONITOR_ACT / BUPAK / COM / GPID 는 데이터 소스·상태 표현·새로고침·로그 연계·권한 처리를 공유합니다. 개별 프로그램 장을 읽기 전에 이 장을 먼저 이해하면 나머지 장을 빠르게 파악할 수 있습니다.

## 2.1 데이터 소스 — 함수 ZFPAC_PAC_MONITOR

네 개의 진행현황 프로그램은 모두 표준 SELECT 대신 공통 함수 ZFPAC_PAC_MONITOR 를 호출하여 조직·액티비티별 상태 건수를 받아옵니다. 화면은 이 함수가 돌려준 집계 결과를 트리로 그리는 역할만 합니다.

**호출 형태(소스 확인):**

CALL FUNCTION 'ZFPAC_PAC_MONITOR'

EXPORTING IV_BUPAK  IV_PCSGP(선택)  IV_GJAHR  IV_MONAT

IV_MLEVEL = 'C'   IT_BUKRS   IV_SUM

IMPORTING ET_RESULT TYPE ZYPAC_HQ_MONITOR.

결과 라인 구조 **ZSPAC_HQ_MONITOR** 의 주요 필드는 다음과 같습니다.

| 필드 | 의미 |
|---|---|
| TOT_CNT | 총 건수(대상 액티비티 수) |
| COMPLETE | 완료(Complete) 건수 |
| FAIL | 실패(Fail) 건수 |
| RUN | 진행(Running) 건수 |
| REWORK | 재작업 필요(Rework) 건수 |
| DEACTIVE | 미수행(Not Executed) 건수 |
| RATE | 진행률(%) = COMPLETE ÷ TOT_CNT × 100 (정수) |
| STATUS / PID / PCSGP / BUKRS 등 | 상태 코드 및 조직·액티비티 키, 프로그램명(TTEXT), 로그 키(LOGID) |

> 보완 설명 (MCP 검증)<br>IV_MLEVEL 파라미터는 네 프로그램 모두 'C'(회사코드 기준 집계)로 호출합니다.<br>ZLPAC_MONITOR_COM 은 요약 조회(P_DETAIL 미체크) 시 IV_SUM='X' 로 호출하여 비즈니스 패키지 1건 요약만 받고, 상세 조회 시 액티비티 그룹/서브그룹/PID 레벨까지 받아 트리를 구성합니다.<br>진행률(RATE)은 완료 건수 ÷ 총 건수의 정수 백분율입니다. 진행 중(RUN) 건수는 진행률에 가산하지 않습니다(소스에서 run_rate 가산 로직은 주석 처리됨).

## 2.2 상태(Status) 값과 색상·버튼

액티비티 상태는 도메인 **ZPAC_STATUS** 로 관리되며, 모니터링 화면의 아이콘 색상과 툴바 버튼이 이 값을 기준으로 표시됩니다. 소스 상수(C_STATUS_*)에서 확인한 값은 다음과 같습니다.

| 코드 | 의미 | 화면 색상(트리 아이콘) |
|---|---|---|
| C | 완료 (Complete) | 초록 LED (파랑 강조) |
| T | 수동 확정 (Manual Confirm) | 초록 LED |
| P | 기간 스킵 (Period Skip) | 초록 LED |
| F | 실패 (Fail) | 빨강 LED (빨강 강조) |
| W | 재작업 필요 (Need to Rework) | 실패 아이콘 (빨강 강조) |
| R | 진행 중 (Running) | 노랑 LED |
| S | 시작 (Start) | 노랑 LED |
| H | 보류 (Pending / Hold) | 노랑 LED |
| A | 종료/취소 (End / Cancel) | 마이너스 아이콘 |
| (공백) | 미수행 (Not Executed) | 마이너스 아이콘 |

**툴바의 상태 버튼** : Total / Fail / Complete / Rework / Running / Not Executed 버튼이 있으며, 각 버튼을 누르면 해당 상태 건수가 0인 노드를 트리에서 제외하여 그 상태만 골라 볼 수 있습니다. 전체 건수 표시는 최초 조회 기준으로 유지됩니다.

## 2.3 자동 새로고침(Auto Refresh) 타이머

ACT / BUPAK / GPID 화면에는 자동 새로고침 기능이 있습니다(COM 제외). 선택화면에서 'Active Auto Refresh'(P_TIMER)를 체크하면 지정 간격마다 화면이 스스로 최신 상태로 갱신됩니다.

- **Every N Minute (P_MINUTE) :** 새로고침 주기(분). 내부적으로 타이머 간격 = P_MINUTE × 60초로 설정됩니다(표준 클래스 CL_GUI_TIMER 사용).
- **Turn off in N Minute (P_MAXTM) :** 자동 새로고침을 종료할 총 시간(분). 최대 수행 횟수 = P_MAXTM ÷ P_MINUTE (나머지가 있으면 +1회).
- **기본값 :** P_MINUTE·P_MAXTM 가 비어 있으면 시스템 설정 테이블 ZTPACSYS 의 REFRESH_MIN / REFRESH_MAX 값을 기본으로 사용합니다.
- **갱신 방식 :** 새로고침 시 전체를 다시 그리지 않고, 건수·상태가 변경된 노드만 찾아 갱신(FRONTEND_UPDATE)하므로 화면 깜빡임을 최소화합니다.

> 핵심 포인트<br>자동 새로고침은 결산 자동수행 중 진행 상황을 사람이 직접 새로고침하지 않아도 반영하기 위한 기능입니다. 주기를 너무 짧게(예: 1분) 설정하고 대상 조직·기간이 넓으면 함수 호출 부하가 커질 수 있으므로, 운영에서는 조직 범위와 주기를 함께 고려해 설정하십시오.

## 2.4 건수 더블클릭 → 로그 연계

트리에서 상태 건수(예: Fail, Complete, Rework, Running 컬럼)나 노드를 더블클릭하면 해당 조건의 실행 로그 조회로 연결됩니다.

- 로그 키(LOGID)가 있고 Fail/Complete/Rework/Running 컬럼을 더블클릭한 경우 → 함수 **ZFPAC_LOG_DISPLAY** 를 팝업으로 호출.
- 그 외의 경우 → 로그 조회 프로그램 **ZLPAC0160** 을 상태 조건과 함께 SUBMIT(호출).
더블클릭한 컬럼과 SUBMIT 시 전달되는 상태 조건의 대응은 다음과 같습니다.

| 더블클릭 컬럼 | 전달 상태 코드 |
|---|---|
| Fail | F |
| Complete | C, T, P |
| Rework | W |
| Running (Run) | S, R, H |
| Not Executed (Deactive) | (공백), A |
| Status(상태 컬럼) | 전체 상태 |

## 2.5 권한 체크

모니터링 대상 조직은 사용자 권한으로 걸러집니다. 권한 판정은 클래스 **ZCL_PAC_AUTH** 의 조직 목록 조회 메소드(GET_AUTH_BUKRS_LIST / GET_AUTH_GSBER_LIST / GET_AUTH_CUNIT_LIST)로 이뤄지며, 권한 없는 조직은 결과에서 제거됩니다.

> 보완 설명 — GPID(글로벌)의 HQ 권한<br>ZLPAC_MONITOR_GPID 는 본사(HQ) 권한을 가진 사용자의 경우 회사코드 권한 체크를 건너뛰어 전체 회사코드를 조회할 수 있습니다(ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH, CHECK_AUTH_HQ).<br>이는 소스 주석상 특정 고객(CWF HQ) 환경을 위한 처리입니다. 권한 정책은 시스템 롤 설정에 따라 달라질 수 있으므로 운영 시스템 기준으로 확인하십시오.
