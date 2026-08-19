---
id: auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng
doc: auto-execution
title: 4. 프로그램 호출관계 · 선후행 · 영향도
parent: docs/auto-execution/README.md
---

# 4. 프로그램 호출관계 · 선후행 · 영향도

## 4.1 자동수행 호출 트리 (선행 → 후행)

**Fiori (OData: ZGWPAC_MAIN_SRV)**

**ZCL_ZGWPAC_MAIN_DPC_EXT → EXECUTE_ACTION  (action = PCSGP_START)**

· 사전: ON_CHECK_START_ENABLE(Exit) → ZFPAC_CHECK_JOB_BALANCING → 레벨 판정

ZFPAC_CREATE_GPID_JOB  ─ ZFPAC_GLOBAL_GET_CAN_START · CHK_CLOSING_ALL → ZFPAC_CREATE_BATCHJOB [ZLPAC0100]

ZFPAC_CREATE_BUPAK_JOB ─ ZFPAC_GET_RUNNING_JOB · IS_PRECHECK_COMPLETED · CHK_CLOSING_ALL → ZFPAC_CREATE_BATCHJOB [ZLPAC0100]

ZFPAC_CREATE_PCSGP_JOB ─ ZFPAC_GET_RUNNING_JOB · CHK_CLOSING_ALL · ZFPAC_CHECK_PRENODE → SAIL_PROCESS_ID(S) → [ZLPAC0100]

**ZLPAC0100 (Batch Job)  →  ZCL_PAC_SAIL → SAIL_START**

SAIL_GLOBAL_PROCESS ─ SYNC_GPID_STATUS · SELECT_NODE_EXECUTABLE · ZFPAC_GET_CAN_START / CHECK_CAN_RUN_MVID → SAIL_PROCESS_ID / CREATE_PCSGP_JOB

SAIL_BUSINESS_PACKAGE ─ START_REWORK_CHECK · SYNC_LINK_INFO · SELECT_NODE_EXECUTABLE · CHECK_CAN_RUN → SAIL_PROCESS_ID

SAIL_PROCESS_GROUP ★ ─ Rework · SYNC_LINK_INFO · SELECT_NODE_EXECUTABLE · IS_PRE_PCSGP_COMPLETED · ZFPAC_GET_RUNNING_JOB

└ 유형별: Period Skip · ZFPAC_CONFIRM_ITEM(REPTY=C) · CHECK_FINAL_COMPLETE · DUMMY_AUTO_CONFIRM · BUPAK_TRIGGER→ZFPAC_AUTOTRIG_CROSS_* · CREATE_PROCESS_GROUP_JOB

SAIL_PROCESS_ID ★ ─ SET_EXEC_PARAM · GET_BATCH_JOBNAMING · ZFPAC_USER_AUTH · CHECK_AUTH_BY_PID → ZFPAC_CREATE_BATCHJOB [ZLPAC0101]

**ZLPAC0101 (Batch Job)  →  SET_EXEC_PARAM(파라미터·Variant 발췌) → SUBMIT 실제 Activity 프로그램**

**실행 결과(상태 변화) → 상위 Group Job이 수행 가능 노드 Refresh → 다음 Job 생성 (자동 순환)**

## 4.2 동일 진입점(EXECUTE_ACTION)의 형제 오퍼레이션

| Action | 호출 함수/메소드 | 설명 |
|---|---|---|
| PCSGP_START | ZFPAC_CREATE_GPID/BUPAK/PCSGP_JOB | 그룹/패키지 레벨 자동수행 시작 (본 매뉴얼 주 대상) |
| PCSGP_STOP | ZFPAC_STOP_PCSGP_JOB | 실행 중인 그룹 배치잡을 중단 |
| PID_START | ZFPAC_CREATE_PID_JOB | 단일 Activity(PID)만 개별 실행 |
| CONFIRM_ITEM | ZFPAC_CONFIRM_ITEM | 수기 확정. 확정 후 AFTER_CONF 충족 시 ZFPAC_NEXT_AUTO_START로 후행 자동수행 |
| RESET_ITEM / RESET_FROM | ZCL_PAC_SAIL→RESET_ITEM / RESET_FROM_HERE | 완료 상태 초기화·특정 지점부터 재수행 (Rework 기반) |
| LINK_CHANGE | ZCL_PAC_SAIL→CHANGE_LINK_CONNECTION | 월별 노드 링크(선후행) 연결 변경 |
| AUTH_CHECK / AUTH_TCODE | ZFPAC_ORG_AUTH / CHECK_TCODE_AUTH | 조회·조직·트랜잭션 실행 권한 체크 |

## 4.3 변경 영향도 (핵심 오브젝트 수정 시 파급 범위)

| 오브젝트 | 영향 범위 | 위험도 |
|---|---|---|
| ZFPAC_CREATE_BATCHJOB | 모든 레벨(GPID/BUPAK/PCSGP/PID)의 Job 생성 공통 함수. JOB_OPEN/SUBMIT/JOB_CLOSE와 밸런싱·중복방지 포함 → 변경 시 전체 자동수행에 영향 | 높음 |
| ZLPAC0100 | 모든 그룹/패키지 Job의 실행 셸(SAIL_START 진입). 변경 시 전체 자동수행 엔진 구동에 영향 | 높음 |
| ZLPAC0101 | 모든 최하단 Activity 프로그램의 실행 셸(SUBMIT). 변경 시 모든 실제 프로그램 실행·파라미터 전달에 영향 | 높음 |
| ZCL_PAC_SAIL (PROCESS_GROUP/ID) | 자동수행 핵심 엔진. 선행완료→후행실행, 병렬·대기·재시도, 노드 유형별 처리 전반 → 변경 시 수행 순서·안정성 전반 영향 | 높음 |
| SET_EXEC_PARAM | 실행 프로그램의 파라미터/Variant 세팅 로직. 변경 시 모든 Activity 실행 파라미터에 영향 | 높음 |
| ZFPAC_CHECK_JOB_BALANCING / ZTPACSYS | 배치 생성량 조절. 값이 과하면 시스템 과부하, 과소하면 처리 지연 | 중간 |
| ZCL_PAC_CLOSING → CHK_CLOSING_ALL | 마감 판정. 오류 시 마감월에 실행되거나 정상월이 차단됨 | 중간 |
| ZTPAC_CONFIG | Business Package 동작 스위치(Precheck/Rework/Final/AutoStart/전기유저). 해당 패키지 거동 변경 | 중간(패키지) |
| ZTPAC_PROC | Activity 정의(파라미터/유형/트리거/Variant/Skip). 개별 Activity 실행 방식 변경 | 중간(Activity) |
| ZCL_PAC_AUTH → CHECK_AUTH_BY_PID | 최종 실행 권한 판정. 오류 시 정당 사용자 차단 또는 무권한 실행 | 중간 |
