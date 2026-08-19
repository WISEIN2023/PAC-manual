---
id: schedule-job
title: Schedule Job 운영자 매뉴얼
category: 마스터
version: v1.0
updated: ""
source: Schedule Job 운영자 매뉴얼(정리).docx
programs: [ZLPAC0020, ZLPAC0100, ZLPAC0101, ZLPAC0500, ZLPAC0510, ZLPAC0520, ZLPAC0530, ZLPAC0540]
tables: [ZTPAC_JOB, ZTPAC_JOB_DTL, ZTPAC_JOB_FUNC, ZTPAC_JOB_HIST, ZTPAC_JOB_ORG, ZTPAC_JOB_ORG_S, ZTPAC_JOB_SCH, ZTPAC_JOB_SCHORG, ZTPAC_JOB_TODO]
functions: [ZFPAC_CIS_RERUN_CONDITION, ZFPAC_CIS_SIMUL_RERUN, ZFPAC_CREATE_SCH_JOB, ZFPAC_JOB_SCH_DETAIL, ZFPAC_JOB_SCH_ORG_DETAIL]
summary: Job Schedule 정의(ZLPAC0500)·모니터링(ZLPAC0510)·월간 스케줄 관리(ZLPAC0520)·BP별 실행(ZLPAC0540)과 결산 시작 전 점검 항목
---

# Schedule Job 운영자 매뉴얼

> Job Schedule 정의(ZLPAC0500)·모니터링(ZLPAC0510)·월간 스케줄 관리(ZLPAC0520)·BP별 실행(ZLPAC0540)과 결산 시작 전 점검 항목

월 배치잡 자동 생성 · 스케줄 관리 프로그램군 (ZLPAC0500 ~ ZLPAC0540)

## 1. 개요

본 프로그램군은 PAC(Post-close / Accounting Closing) 솔루션에서 수행되는 결산 Activity를 매월 지정된 시간에 자동으로 수행되도록 배치잡(Batch Job)을 생성·관리하는 프로그램들의 집합이다. 운영자는 이 매뉴얼을 통해 각 프로그램의 역할, 배치잡 정의·생성·모니터링 절차, 그리고 관련 테이블 구조를 확인할 수 있다.

### 1.1 핵심 개념

- Job Type(BTYPE) 3가지에 대해 조직(법인)별·지정 시간별로 배치잡을 자동 수행하도록 Set-up 한다.
- 한 번 정의해두면 매월 예정 시점에 잡이 자동 수행되고, 정상 생성이 확인되면 차월(다음 달) 잡이 자동으로 생성되는 순환 구조를 가진다.
- 모든 연관 테이블은 ZTPAC_JOB_* 네이밍으로 시작한다.

### 1.2 Job Type (BTYPE) 종류

| BTYPE | 명칭 | 설명 |
|---|---|---|
| I | Closing Inspection | 결산점검 항목을 특정 시간에 자동 수행하도록 정의 |
| S | Specific Activity | 특정 Activity를 특정 시간에 자동 수행하도록 정의 |
| T | Automatic start of business Package | 특정 Business Package의 자동 시작 시점을 정의 |

**참고** 화면 라디오버튼 표기 순서(①Closing Inspection ②Specific Activity ③Automatic start of business Package)와 내부 코드값(I / S / T)의 매핑에 유의한다.

### 1.3 초기 프로그램 대비 주요 개선 사항

- Org Define 기능 추가 — 잡을 생성할 조직(법인) 목록을 정의.
- Job Define 개선.
- Next Month(Add Month) 필드 추가 — 시작 잡 일자를 지정하여, 익월 잡 생성 시 발생하던 오류 개선.
- ZLPAC0520 프로그램에서 날짜·시간 변경은 CWF 담당자만 가능하도록 권한 제한.

## 2. Job Schedule 운영담당자 주요 업무

Job Schedule 운영 중 운영담당자가 수행하는 대표적인 업무를 시나리오별로 정리한다. 각 업무는 뒤 장(3장 이후)의 프로그램별 상세 설명과 함께 참고한다.

| 구분 | 업무 | 주 사용 프로그램 |
|---|---|---|
| 2.1 | 신규 배치잡 생성 | ZLPAC0500 → 0510 → 0520 |
| 2.2 | 신규 법인 추가 시 기존 배치잡에 법인 추가 | ZLPAC0500 → 0520 |
| 2.3 | 배치잡 착오 생성 시 강제 삭제 후 재수행 | SM37 → ZLPAC0520 |
| 2.4 | 배치잡 Cancel 시 재수행 | ZLPAC0520 / 단일 수행 |

### 2.1 신규 배치잡 생성

특정 결산점검 항목 · Activity · Business Package를 매월 지정 시간에 자동 수행하도록 새로 정의하는 절차이다.

1. (필요 시) ZLPAC0020에서 대상 Activity의 Activity Master를 생성한다.
2. ZLPAC0500에서 Job Type(I/S/T)을 선택한다.
3. Schedule Define(ZFPAC_JOB_SCH_DETAIL)에서 Schedule Type / Time Zone / 수행 날짜·시간을 지정한다.
4. Org Define(ZFPAC_JOB_SCH_ORG_DETAIL)에서 자동수행 대상 조직을 저장한다(예외 조직은 Inactive 체크).
5. ZLPAC0510에서 정의된 항목·대상 조직을 조회하여 확인한다.
6. ZLPAC0520에서 [CREATE]로 실제 배치잡을 생성한다.
**확인** CREATE 시 수행자(잡 소유자)가 각 서버 기준 '공통 유저'로 지정되었는지 반드시 확인한다. 초기 생성월 이후부터는 예정 시점에 자동 수행되고, 정상 생성이 확인되면 차월 잡이 자동 생성(Released)된다.

### 2.2 신규 법인 추가 시 기존 배치잡에 법인 추가

이미 운영 중인 Job Seq에 신규 법인(조직)을 대상으로 추가하는 절차이다.

1. ZLPAC0500에서 해당 Job Seq의 Org Define을 연다. 신규 추가된 법인은 [ + ] 로 표시된다.
2. 추가할 법인의 Inactive 체크를 해제(전체 수행 대상으로 포함)하고 저장한다 → 후행 화면에 반영된다.
3. ZLPAC0520로 이동하여 해당 신규 법인분의 배치잡을 [CREATE]로 생성한다.
- 실제로 Activity가 모델링되어 있는 조직만 목록에 표시된다. 모델링 여부는 ZLPAC0140에서 확인한다.
**참고** 기존에 이미 잡이 생성된 조직은 Block(파란 글씨·자물쇠 🔒) 처리되어 수정 불가하지만, 잡이 없는 신규 추가 법인은 정상적으로 추가·생성할 수 있다.

### 2.3 배치잡 착오 생성 시 강제 삭제 후 재수행

잘못된 날짜·시간 또는 잘못된 대상으로 잡을 착오 생성한 경우의 처리 절차이다.

1. SM37에서 해당 Job Name으로 검색한다.
2. 아직 수행 전(Released / Scheduled) 상태의 착오 생성 잡을 삭제한다.
3. ZLPAC0520에서 올바른 기준으로 배치잡을 다시 [CREATE] 한다.
**주의** 이미 수행 완료된 잡 이력은 삭제할 수 없다. 날짜·시간을 정의 기준과 다르게 강제로 바꿔 재생성해야 하는 경우, CWF 담당자만 ZLPAC0520의 [Change] 버튼으로 Plan Date/Time을 변경하여 생성할 수 있다.

### 2.4 배치잡 Cancel 시 재수행 방법

수행된 잡이 Cancel(취소·실패)된 경우, 이미 수행된 이력은 자동 재수행되지 않는다.

- 재수행이 필요하면 단일·일회성으로 직접 잡을 생성하거나 해당 Activity를 직접 수행한다.
- 이미 수행된 잡 이력 자체는 삭제 불가하다(2.3의 삭제는 '수행 전' 잡에만 해당).
**검토 필요** Schedule Calendar 방식(SCH_DTL_TYPE = Schedule Calendar date)으로 설정하고 다음 달의 캘린더를 등록하지 않으면, 차월 잡 날짜 계산 시 기준일이 없어 자동 차월 생성을 막을 수 있을 것으로 보인다. 이 방식으로 재수행 시점을 통제할 수 있는지는 실제 동작 확인이 필요하다.

## 3. 프로그램 구성 및 관계

전체 흐름은 [정의 → 모니터링 → 생성 → 실행 → 이력조회]의 단계로 이루어지며, 각 단계를 담당하는 프로그램은 다음과 같다.

| 프로그램 | 명칭 | 역할 | 주요 테이블 |
|---|---|---|---|
| ZLPAC0500 | Define Job Schedule | Job Type 3종에 대해 조직·시간별 자동 배치 수행 Set-up | ZTPAC_JOB_SCH / ZTPAC_JOB_SCHORG |
| ZLPAC0510 | Monitoring By Job Schedule | 지정 조직별 배치잡 생성 상태별 건수 조회 | ZTPAC_JOB_SCHORG, TBTCO/TBTCP |
| ZLPAC0520 | Maintain Monthly Job Schedule by Organization | Period별 배치잡 생성 이력 상세 조회 / 실제 배치잡 생성 | ZTPAC_JOB_ORG_S, ZTPAC_JOB_HIST |
| ZLPAC0530 | Display Job Schedule History | 생성된 배치잡 수행 이력 조회 | ZTPAC_JOB_HIST |
| ZLPAC0540 | Execute Schedule Job by Background | 0520 생성 잡이 실제 Activity 수행 / 차월 잡 자동 생성 | ZTPAC_JOB_HIST |

### 3.1 처리 흐름 요약

1. ZLPAC0500 — 잡 스케줄 정의(Job Type / Time Zone / 대상 조직 / 날짜·시간).
2. ZLPAC0520 — 정의된 스케줄을 기준으로 특정 시점에 수행될 실제 배치잡을 CREATE.
3. 예정 시점 도래 → ZLPAC0540가 백그라운드로 실행되어 실제 Activity 잡을 수행.
4. 정상 생성이 확인되면 ZLPAC0540 내부 로직이 차월(다음 달) 잡을 자동 생성(Released 상태).
5. ZLPAC0510(현황 모니터링) / ZLPAC0530(수행 이력)으로 상태를 확인.

## 4. ZLPAC0500 — Define Job Schedule (잡 스케줄 정의)

**목적:** Job Type별 배치잡을 정의하기 위한 프로그램. Schedule Define을 통해 Schedule Type / Time Zone을 지정하고, 어느 조직의 자동수행 잡을 만들 것인지 저장한다.

**연관 테이블:** ZTPAC_JOB_SCH (JOBSEQ별 수행 상세 정보), ZTPAC_JOB_SCHORG (JOBSEQ별 수행 법인 저장)

### 4.1 정의 절차

1. Job Type(BTYPE) 선택 — I(Closing Inspection) / S(Specific Activity) / T(Business Package).
2. Schedule Define(ZFPAC_JOB_SCH_DETAIL) — Schedule Type / Time Zone 지정.
3. Org Define(ZFPAC_JOB_SCH_ORG_DETAIL) — 자동수행 잡을 생성할 대상 조직 저장.
4. 수행될 날짜·시간 입력 — 팝업에서 저장한 date/time이 ZLPAC0500 레코드에 반영된다.

### 4.2 주요 필드

| 필드 | 설명 |
|---|---|
| From ~ To Period | 더블클릭 시 해당 Job Seq의 월별 잡 생성 현황(ZLPAC0510)으로 이동. |
| Add Month | 잡 생성월의 '다음 달'부터 수행해야 할 때 사용(시작 시점 지정). |
| Time Zone / Time | 수행 기준 시간대(Local 등)와 시각을 지정. |
| Inactive(조직) | 예외 처리할 조직에 체크하면 후행 화면에서 해당 조직이 제외된다. |

### 4.3 조직(Org) 목록 표시 규칙

- 일반적으로 예외 조직 없이 전체 조직을 대상으로 수행한다. 제외할 조직이 있으면 Inactive 체크.
- 신규 추가된 법인이 있을 경우 [ + ] 로 표시된다.
- 실제로 Activity가 모델링되어 있는 조직 리스트만 표시된다.
**중요** 해당 Job Seq에 이미 생성된 잡이 하나라도 있으면 그 조직은 수정 불가하도록 Block 처리되며 파란색 글씨로 표시된다. ZLPAC0520에서 생성한 잡이 있는 조직은 자물쇠(🔒) 모양으로 표시된다.

## 5. ZLPAC0510 — Monitoring By Job Schedule (잡 스케줄 모니터링)

**목적:** 지정된 조직별 배치잡의 생성 상태별 건수를 조회한다. Job Seq의 세부정보로서 Period별 실제 잡 생성 개수와 상태를 표시한다.

**데이터 산정 기준:** ZTPAC_JOB_SCHORG를 Total 기준으로 잡고, ZTPAC_JOB_ORG_S에 저장된 실제 생성 잡에 대해서는 조회 시점 기준 TBTCO / TBTCP에서 실제 잡 상태를 읽어와 상태별로 Summary(collect)한다.

### 5.1 상태 컬럼 정의

| 컬럼 | 의미 | 산정 기준 |
|---|---|---|
| Total Cnt | 이 스케줄에서 해당 월에 잡이 있어야 할 조직 수 | ZTPAC_JOB_SCHORG |
| P / S / R / F / A | 실제 생성된 잡들이 현재 어떤 상태인지 (Completed / Scheduled / Released / Failed·Cancelled / Active 등) | ZTPAC_JOB_ORG_S + 조회시점 TBTCO |
| Not Created | 아직 잡이 만들어지지 않은 조직 수 (= Total − 생성분) | 계산값 |

**동작** 전월 잡이 완료되는 순간 익월 수행될 잡이 생성되어 Released 상태로 추가되는 구조다. 실제 잡 생성을 수행하려면 Maintain Job의 [ ⇒ ] 화살표 버튼을 더블클릭하여 ZLPAC0520으로 이동한다.

## 6. ZLPAC0520 — Maintain Monthly Job Schedule by Organization (월별 잡 생성·유지관리)

**목적:** ZLPAC0500에서 정의한 Job Seq별 조직·시간에 대한 실제 배치잡을 생성하는 화면. Period별 배치잡 생성 이력을 상세 조회한다.

**연관 테이블:** ZTPAC_JOB_ORG_S (Create된 잡 리스트 — ZLPAC0540이 다음 달 잡을 자동 생성할 때도 이 테이블에 저장), ZTPAC_JOB_HIST.

### 6.1 배치잡 생성 절차

1. 앞 단계(ZLPAC0500)에서 정의한 잡 정보의 날짜·시간이 자동으로 채워진다.
2. 사용자는 정의된 날짜·시간으로만 생성 가능하다(임의 변경 불가 — 예외는 6.3 참조).
3. [ CREATE ] 버튼 클릭 → 내부적으로 FORM CALL_ZFPAC_CREATE_BATCHJOB 퍼폼이 수행된다.
**운영 주의** CALL_ZFPAC_CREATE_BATCHJOB 퍼폼 실행 시 수행자(잡 소유자)를 지정하는데, 이때 반드시 각 서버 기준으로 수행할 '공통 유저'로 변경해 주어야 한다.

### 6.2 Plan Date / Plan Time 표기

- Plan Date, Plan Time은 Job Seq에 정의한 Local 시간 기준이며, 화면에는 이를 본사 시간으로 몇 시인지 환산하여 표시한다.
- 초기 생성월 다음부터는 예정된 일정에 자동으로 수행되며, 정상 수행되면 다음 달 잡이 자동 생성되어 Released 상태로 표시된다.

### 6.3 Change 버튼 (CWF 담당자 전용)

- Change 버튼은 CWF 담당자에게만 활성화되어 보인다.
- Plan Date와 Time을 강제로 변경하여 생성할 수 있다(CWF 담당자만).
- 일반적으로는 ZLPAC0500에서 정의한 기준 그대로 표시·생성하도록 가이드한다.

### 6.4 잡 삭제 / 재수행

**삭제** Create 후 잡을 삭제하려면 SM37에서 직접 해당 Job Name으로 검색하여 삭제해야 한다.

**재수행** 이미 수행된 잡 이력은 삭제 불가하다. 재수행이 필요하면 단일·일회성으로 직접 생성하거나 직접 수행하도록 가이드한다.

### 6.5 ZLPAC0530 — Display Job Schedule History (수행 이력 조회)

생성된 배치잡의 수행 이력을 조회하는 화면. ZLPAC0540 수행이 완료되면서 ZTPAC_JOB_HIST 테이블에 이력이 저장된다.

## 7. ZLPAC0540 — Execute Schedule Job by Background (백그라운드 실행)

**목적:** ZLPAC0520에서 배치잡 생성 시 실행되는 프로그램으로, 예정된 시점에 실제 Activity 잡을 생성·수행하고 차월 잡을 자동 생성한다.

### 7.1 동작 구조

1. ZLPAC0520에서 CREATE 시, 수행 프로그램이 ZLPAC0540인 잡이 생성된다(생성자는 배치 유저로 고정).
2. 예정 시점 도래 → ZLPAC0540가 실행되어 [ 예정된 잡 수행 + 다음 달 잡 생성 ]을 함께 처리한다.
BTYPE별로 백그라운드 잡 생성 로직만 다르고, '다음 달 잡 생성' 부분은 모두 동일하다.

### 7.2 실제 Activity 수행에 사용되는 Function

| BTYPE | 사용 Function / 동작 |
|---|---|
| I | ZFPAC_CIS_RERUN_CONDITION / ZFPAC_CIS_SIMUL_RERUN |
| T | ZFPAC_CREATE_SCH_JOB → ZLPAC0100 수행. PID 조회 없이 BUPAK 값을 넣어 최상위 패키지를 수행(ZFPAC_CREATE_BATCHJOB에서 ZLPAC0100 실행). |
| S | ZFPAC_CREATE_SCH_JOB → ZLPAC0101 수행. ZTPAC_JOB_SCH에서 JOBSEQ로 PID를 읽고 해당 PID의 PCSGP까지 활용하여 수행. |

### 7.3 차월(다음 달) 잡 자동 생성 로직

- 이번 달 수행 잡이 '정상적으로 생성'되었으면(수행 결과가 아니라 정상 생성 여부만 확인) 차월 잡을 생성한다.
- 차월 잡의 생성 날짜·시간은 ZTPAC_JOB_ORG의 정보를 기준으로 계산한다.
- SCH_DTL_TYPE에 따라 계산 방식이 달라진다 — Fixed date(고정일) 또는 Schedule Calendar date(스케줄 캘린더일).
- 잡 생성은 ZFPAC_CREATE_BATCHJOB를 통해 이루어진다.
**참고** 차월 잡 생성 시 다음 달 Time Zone(타임존) 설정이 함께 반영된다.

## 8. 관련 테이블

### 8.1 PAC 잡 스케줄 테이블 (ZTPAC_JOB_*)

| 테이블 | 설명 | 사용 |
|---|---|---|
| ZTPAC_JOB_SCH | PAC – Job Schedule | 사용 |
| ZTPAC_JOB_SCHORG | PAC – Job Schedule Base by Organization | 사용 |
| ZTPAC_JOB_ORG_S | PAC – Job Schedule by Organization (Saved) | 사용 |
| ZTPAC_JOB_HIST | PAC – Job Schedule History | 사용 |
| ZTPAC_JOB_DTL | PAC – Batch Job Schedule Detail | 미사용 |
| ZTPAC_JOB_FUNC | PAC – Job Schedule | 미사용 |
| ZTPAC_JOB_ORG | PAC – Job Schedule by Organization | 미사용 |
| ZTPAC_JOB_TODO | PAC – To-Do List Schedule | 미사용 |

### 8.2 SAP 표준 배치잡 테이블

잡 상태를 조회할 때는 헤더 테이블인 TBTCO를 기준으로 조회해야 한다.

| 구분 | TBTCO | TBTCP |
|---|---|---|
| 의미 | 잡 헤더 (Job Overview) | 잡 스텝 (Job Step) |
| Key | JOBNAME + JOBCOUNT | JOBNAME + JOBCOUNT + STEPCOUNT |
| 건수 | 1건 | 스텝 수만큼 발생 |
| STATUS 의미 | 잡 전체의 최종 상태 | 해당 스텝 하나의 상태 |

**중요** 잡 전체의 최종 상태를 보려면 반드시 TBTCO로 조회해야 한다(TBTCP는 스텝 단위 상태이므로 잡 전체 상태와 다를 수 있음).

## 9. 운영 확인사항 (결산 시작 전 점검)

ZLPAC0500 결산 시작 전 점검이 필요한 매월 수행 배치잡 목록. (LG팀즈 – CWF 결산 관련 To-Do List를 함께 확인할 것)

| Job Type | BUPAK | 항목 | Time Zone | Time | Org / 특이사항 |
|---|---|---|---|---|---|
| Inspection | FI | PRE_CHK | Local | D-1 09시 | Pre-chk simulation은 '26.2월부터 제거 |
| Inspection | FV | V_FIN | Local | D-5, D+5 오전 9시 | 파일럿·모델링 법인 (ZLPAC0140에서 확인 — 불필요 org 제거) |
| Inspection | FV | C_COST | Local | D-5, D+5 오전 9시 | 파일럿·모델링 법인 (ZLPAC0140에서 확인 — 불필요 org 제거) |
| Inspection | LC | LC_PRCHK | Local | D+5 오전 9시 | — |
| Activity | FI | FI0756 Create Closing FI Doc IF Check list | Local | D-1 18시 | 파일럿 오픈 법인 대상만 생성 |

## 10. Set-up 절차 예시

예시 — 특정 Activity를 특정 시간에 자동 수행하도록 정의하는 경우:

1. ZLPAC0020 — Activity Master 생성.
2. ZLPAC0500 — Define Job Schedule: 특정 Activity에 대해 지정한 시간에 자동 배치 수행되도록 정의.
3. ZLPAC0510 — Monitoring By Job Schedule: 정의된 배치잡 항목 조회 및 생성.
**주의** ZLPAC0500에서 정의한 후, 반드시 ZLPAC0510(및 ZLPAC0520) 화면에서 항목 조회 및 배치잡 생성까지 이루어져야 실제 잡이 동작한다.

## 11. 운영 FAQ / 트러블슈팅

| 증상 / 질문 | 확인 및 조치 |
|---|---|
| 잡 상태 건수가 맞지 않는다 | Total은 ZTPAC_JOB_SCHORG 기준, 실제 상태는 조회 시점 TBTCO 기준이다. 전월 잡 완료 시점에 익월 잡이 Released로 추가되므로 조회 시점에 따라 건수가 달라질 수 있다. |
| 조직이 수정 불가(파란 글씨·자물쇠)로 보인다 | 해당 Job Seq에 이미 생성된 잡이 있는 조직이다. ZLPAC0520에서 생성한 잡이 존재하면 Block 처리된다. |
| Plan Date/Time을 바꿔야 한다 | CWF 담당자만 ZLPAC0520의 Change 버튼으로 변경 가능하다. 일반 운영자는 ZLPAC0500 정의 기준을 사용한다. |
| 생성한 잡을 삭제하고 싶다 | SM37에서 해당 Job Name으로 검색하여 삭제한다. 이미 수행된 잡 이력은 삭제 불가. |
| 이미 수행된 잡을 재수행하고 싶다 | 단일·일회성으로 직접 생성하거나 직접 수행한다. |
| 잡 소유자(수행자)가 서버와 맞지 않는다 | ZLPAC0520 CREATE 시 각 서버 기준 공통 유저로 지정되었는지 확인한다. |
