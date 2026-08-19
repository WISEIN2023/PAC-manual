---
id: auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu
doc: auto-execution
title: 3. 수행 단계별 상세 프로세스 (자동수행 관점)
parent: docs/auto-execution/README.md
---

# 3. 수행 단계별 상세 프로세스 (자동수행 관점)

## 단계 1. Fiori > Start 버튼

**● 자동수행 관점 프로세스**

담당자가 Fiori 앱에서 대상 Group의 [Start] 또는 [Start All] 버튼을 눌러 자동수행을 시작한다.

**● 보충 설명**

Start = 선택한 노드부터 수행 / Start All = 전체 노드를 대상으로 수행. Start All의 경우 각 노드의 선행 완료 여부를 함께 검증한다.

## 단계 2. ZGWPAC_MAIN › Action Import : PCSGP_START

**● 자동수행 관점 프로세스**

자동수행의 진입점이다. 시작 전 다음을 순서대로 점검하고 레벨에 맞는 생성 함수를 호출한다.

1) Business Package 마감여부 체킹(CHECK_BUPAK_CLOSE) — 마감된 경우 자동수행하지 않고 에러 종료

2) 수행권한 체킹(ZFPAC_USER_AUTH) — 해당 Group을 자동수행할 권한이 있는지 확인

3) Job 생성 가능 상태 체킹(ZFPAC_CHECK_JOB_BALANCING) — 배치 프로세스 유휴율만큼만 생성되도록 밸런싱, 가능한 경우만 진행

4) 자동수행 함수 호출 — 수행을 시작한 레벨에 따라 아래 3개 중 하나를 호출

· Global Package(GPID 존재) → ZFPAC_CREATE_GPID_JOB

· Business Package(1레벨) → ZFPAC_CREATE_BUPAK_JOB

· Activity Group → ZFPAC_CREATE_PCSGP_JOB

**● 보충 설명**

- PCSGP_START는 OData 서비스 ZGWPAC_MAIN_SRV의 Action이며, 실제 처리는 데이터 제공 클래스 ZCL_ZGWPAC_MAIN_DPC_EXT 의 EXECUTE_ACTION 메소드에서 이뤄진다.

① Start Enable 사용자 Exit(ZCL_PAC_SAIL→ON_CHECK_START_ENABLE) → ② 배치 밸런싱(ZFPAC_CHECK_JOB_BALANCING) → ③ 레벨 판정(GPID > Business Package = PCSGP > Activity Group) 후 생성함수를 호출한다. 마감·권한의 '실질 판정'은 진입점이 아니라 각 생성함수 내부 CHK_CLOSING_ALL)와 최종 SAIL_PROCESS_ID(CHECK_AUTH_BY_PID)에서 이뤄진다.

- EXECUTE_ACTION은 Start 외 여러 액션을 함께 처리한다

. PCSGP_STOP(중단 → ZFPAC_STOP_PCSGP_JOB)

. PID_START(단일 Activity 시작 → ZFPAC_CREATE_PID_JOB)

. CONFIRM_ITEM(수기 확정 → ZFPAC_CONFIRM_ITEM)

. RESET_ITEM·RESET_FROM(초기화·재수행)

. LINK_CHANGE(월별 링크 변경)

. AUTH_CHECK·AUTH_TCODE(조회·트랜잭션 권한 → ZFPAC_ORG_AUTH)

※ 본 매뉴얼은 PCSGP_START(자동수행) 경로를 중심으로 기술한다.

최상단(1레벨)이 아닌 Activity Group 및 Sub-Group에서도 자동수행을 시작할 수 있으며, 그 경우 해당 레벨만 자동 실행된다.

## 단계 3-a. ZFPAC_CREATE_GPID_JOB (Global Package 레벨)

**● 자동수행 관점 프로세스**

Global Package 레벨의 배치잡을 생성한다.

1) Start 가능여부 체킹(ZFPAC_GLOBAL_GET_CAN_START) — 수행 불가 시 종료

2) 일정 마감여부 체킹(CHK_CLOSING_ALL)

3) GPID 레벨 Job 생성 — ZLPAC0100 프로그램을 ZFPAC_CREATE_BATCHJOB으로 배치잡 생성

**● 보충 설명**

Global Package는 Company Code를 쓰는 Business Package들을 묶어 1레벨로 구성할 때 사용한다. (예: Company Code 기준 FI 와 Company Code+BA 기준 CO 를 하나의 Global Package로 구성)

## 단계 3-b. ZFPAC_CREATE_BUPAK_JOB (Business Package · 1레벨)

**● 자동수행 관점 프로세스**

Business Package(1레벨) 배치잡을 생성한다.

1) Start 가능여부 체킹(ZFPAC_GET_RUNNING_JOB) — 1레벨 배치잡이 이미 실행 중이면 종료

2) 일정 마감여부 체킹(CHK_CLOSING_ALL)

3) BUPAK 레벨 Job 생성 — ZLPAC0100을 ZFPAC_CREATE_BATCHJOB으로 배치잡 생성

**● 보충 설명**

BusPkg Config 설정에 따라 Precheck(사전점검) 체크 선택시, 사전점검의 완료 여부도 함께 확인하며, 미완료 시 실행하지 않는다.

- Precheck(사전점검) 사용 여부 : ZTPAC_CONFIG-XPRE_USE로 제어

- IS_PRECHECK_COMPLETED 결과가 완료('C'/'T')가 아니면 오류(ZPAC01/029)로 자동수행을 중단

- 사전점검 대상 Activity는 ZTPAC_CONFIG-PRE_PID로 지정

※ LG전자등 현재 PAC 적용 고객중 설정 없음

## 단계 3-c. ZFPAC_CREATE_PCSGP_JOB (Activity Group 레벨)

**● 자동수행 관점 프로세스**

Activity Group 레벨의 배치잡을 생성한다.

1) Start 가능여부 체킹(ZFPAC_GET_RUNNING_JOB) — 대상 Group 배치잡이 이미 실행 중이면 종료

2) 일정 마감여부 체킹(CHK_CLOSING_ALL)

3) 선행 완료여부 체킹 — Start All(IV_HERE 미지정)로 수행된 경우, 대상 Activity Group의 이전 노드가 모두 완료된 경우에만 수행

- Activity Sub Group인 경우, Sub-Group의 선행 노드와 그 부모 Activity Group 노드의 선행까지 모두 완료되었는지 확인한다.

4) Activity Group Job 생성 — ZLPAC0100을 배치잡으로 생성

**● 보충 설명**

IV_HERE = 'X' 수행 : 특정한 PID 위치로 부터 이후의 연결된 Activity 노드들만 수행하는 기능

-> 이때, START_FROM에 해당 특정위치의 PID 를 입력한다

## 단계 4. ZLPAC0100 (Batch Job 셸 프로그램)

**● 자동수행 관점 프로세스**

실제 배치잡으로 수행되는 기본 프로그램이다. (SAP 배치잡 생성에 필수)

· 수행 데이터·Lock 점검

· Running History 생성 — 자동수행 Job 이력 관리를 위해 ZTPACJOBS 테이블에 등록(MAKE_JOB_HISTORY)

· 실제 자동수행 로직 ZCL_PAC_SAIL → SAIL_START 호출

**● 보충 설명**

이 프로그램 자체에는 결산 로직이 없다. 배치잡이라는 '실행 껍데기' 역할을 하며 내부에서 자동수행 클래스를 호출한다.

## 단계 5. ZCL_PAC_SAIL → SAIL_START

**● 자동수행 관점 프로세스**

수행 레벨에 따라 세부 실행 로직으로 다시 분기한다.

1) Global Package → SAIL_GLOBAL_PROCESS

2) Business Package → SAIL_BUSINESS_PACKAGE

3) Activity Group / Sub-Group → SAIL_PROCESS_GROUP

· 실행에 필요한 NODE·LINK 정보를 조회한 뒤 위 로직을 호출하고, Job 종료 시 상태 반영(APC) 및 Rework 점검을 수행한다.

**● 보충 설명**

SAIL = PAC 자동수행 엔진의 핵심 클래스. 이후 단계(5-1~6)는 SAIL_START가 호출하는 하위 로직이다.

## 단계 5-1. SAIL_GLOBAL_PROCESS

**● 자동수행 관점 프로세스**

Global Package 레벨에서 수행 가능한 Activity Group을 찾아 실행한다.

1) GPID 레벨 상태 동기화(SYNC_GPID_STATUS)

2) NODE·LINK 조회

3) 수행 가능 여부 계산(SELECT_NODE_EXECUTABLE)

4) 수행 가능한 Activity Group 실행

· MVID 없음: ZFPAC_GET_CAN_START로 가능 확인 후, 실행 중 Job이 없으면 SAIL_PROCESS_ID(그룹 Job) 생성

· MVID 있음: 하위 BA를 모두 실행해야 하므로 ZFPAC_CREATE_PCSGP_JOB 호출

**● 보충 설명**

MVID는 Global Package에서 Company Code+BA를 쓰는 Business Package를 처리하기 위한 구분값이다. 1레벨은 Company Code로 정의되어 있으나 하위 BA를 모두 전개하여 실행한다.

## 단계 5-2. SAIL_BUSINESS_PACKAGE

**● 자동수행 관점 프로세스**

Business Package 안의 Activity Group들을 실행한다.

1) Rework 점검(START_REWORK_CHECK)

2) 상태 Refresh(SYNC_LINK_INFO)

3) 수행 가능 여부 계산(SELECT_NODE_EXECUTABLE)

4) 수행 가능한 Activity Group에 대해 CHECK_CAN_RUN으로 재확인하고, 실행 중 Job이 없으면 SAIL_PROCESS_ID(그룹 Job) 생성

**● 보충 설명**

Start From(특정 PID부터 시작) 지정 시, 해당 노드의 선행·후행 라인만 대상으로 하고 관련 없는 노드는 제외한다.

## 단계 5-3. SAIL_PROCESS_GROUP  ★핵심

**● 자동수행 관점 프로세스**

Activity Group 레벨의 핵심 실행 로직. 조회된 노드를 반복(DO~ENDDO)하며 수행 가능한 노드를 자동 실행한다.

① Rework 여부 점검 — 발생 시 상태 반영하여 후행 실행 차단

② LINK SYNC(SYNC_LINK_INFO) — 상태·링크를 실시간 재조회

③ Start From 라인이 아닌 항목은 에러 처리하여 실행대상에서 제외

④ 노드 수행 가능 여부 계산(SELECT_NODE_EXECUTABLE)

⑤ 전체 레벨 수행 시 상위 Group 선행 완료 여부 체킹(IS_PRE_PCSGP_COMPLETED) — 미완료 시 종료

⑥/⑦ 수행 가능 노드가 없으면 ZFPAC_GET_RUNNING_JOB으로 실행 중 Activity 확인 → 있으면 5초 단위 대기, 없으면 상태 재계산 및 강제 중단된 배치잡을 오류 처리

⑧ 수행 가능 노드 자동 실행

수행 가능 노드에 대해 유형별로 처리한다.

⑨ Period Skip — Activity Master에 Skip 처리된 월이면 상태를 완료로 변경

⑩ Closing Schedule(REPTY=C)이 자동수행된 경우 — 결산일정을 자동 CLOSE(ZFPAC_CONFIRM_ITEM)

- 수기 Confirm(ZFPAC_CONFIRM_ITEM) :  실행중 Job·Lock·마감·Final 완료 등을 점검한 뒤 Activity 상태를 완료로 확정한다. 확정 후 ZTPAC_CONFIG-AFTER_CONF='X'이면 ZFPAC_NEXT_AUTO_START로 후행 자동수행이 이어진다

⑪ Final Activity — 종료 전 미완료 Activity 존재 여부 체킹(CHECK_FINAL_COMPLETE)

⑫ Dummy 유형(REPTY=M) — 자동 Confirm(DUMMY_AUTO_CONFIRM)

⑬ Out-bound Trigger(REPTY=X & CRS_INOUT=O)

- Out-bound Trigger(REPTY=X, CRS_INOUT=O)는 ZTPAC_CROSS_IF의 TRIG_TYPE에 따라 분기한다

. 'B'=CROSS_BUPAK(Business Package 간), 'O'=CROSS_ORG(조직 간).

. Outbound 조직이 모두 완료되는 시점에 Inbound Activity를 완료처리 하고, Inbound가 XAUTO='X'이면 후속 자동 수행

( ZCL_PAC_SAIL→START_FROM_AUTO_TRIGGER로 후속 자동수행을 개시)

. Rework 불가(XREWORK=' ') 트리거는 이미 완료된 Inbound가 있으면 재수행을 차단

⑭ 노드가 Activity Sub-Group이면 Sub-Group Job 생성(CREATE_PROCESS_GROUP_JOB)

⑮ 최하단 프로그램 레벨 Job 생성 — SAIL_PROCESS_ID(IV_TYPE=T)

**● 보충 설명**

이 단계가 '선행 완료 → 후행 실행' 규칙과 병렬 처리, 대기/재시도를 실제로 담당하는 부분이다.

강제 중단(Cancel)된 배치잡은 상태가 '진행 중'으로 남을 수 있어, Job 상태를 조회해 강제로 에러 처리한다.

노드는 '실행할 프로그램'일 수도, '하위 그룹'일 수도, '자동 확정 대상'일 수도 있다. 유형에 따라 실제 처리가 달라진다.

## 단계 6. SAIL_PROCESS_ID  ★핵심

**● 자동수행 관점 프로세스**

최하단 프로그램 레벨의 배치잡을 생성한다.

1) 실행 파라미터 설정(SET_EXEC_PARAM) — ZLPAC0101에 호출할 BusPkg, PID, 조직, 년월정보, Simulation 정보 등의 파라미터 호출

2) Job Naming 조회(GET_BATCH_JOBNAMING)

3) 수행 유저 조회

· 최하단 프로그램(Transaction) 수행: ZFPAC_USER_AUTH로 Posting User 설정

· 그룹 Job(IV_TYPE=S) 수행: 지정 유저가 있으면 그 값, 없으면 실행자(SY-UNAME)

4) 수행 권한 체크 — 프로그램이 ZLPAC0100이 아닌 경우 ZCL_PAC_AUTH → CHECK_AUTH_BY_PID로 확인, 권한 없으면 오류

5) Batch Job 생성(ZFPAC_CREATE_BATCHJOB)

. Activity Master에 등록된 프로그램이 아닌 ZLPAC0101을 실행한다

**● 보충 설명**

. Posting User(전기 유저) 설정 우선순위: Activity ID > Activity Group > Organization.

. ZLPAC0100은 그룹 Job을 수행하는 프로그램이므로 개별 권한 체크 대상에서 제외된다.

. IV_TYPE='S'(그룹 Job)이면 ZLPAC0100을,

IV_TYPE≠'S'(최하단 프로그램)이면 ZLPAC0101을 배치잡 실행 프로그램으로 지정

※ ZLPAC0100 = 자동수행 엔진 셸(SAIL_START 호출)

ZLPAC0101 = 실제 대상 프로그램 SUBMIT 셸(파라미터·Variant 발췌 + 상위 Job 보호)

=> 두 프로그램 모두 결산 로직은 없는 '실행 껍데기'다

## 단계 7. ZLPAC0101  ★핵심 (Batch Job 셸 프로그램)

**● 자동수행 관점 프로세스**

최하단 프로그램 레벨 Job의 실행 프로그램으로, 실제 대상 프로그램을 직접 돌리지 않고 ZLPAC0101을 거쳐 실행한다.

1) Activity(PID) 마스터(ZTPAC_PROC) 조회 — TCODE로 실제 실행 프로그램(TSTC-PGMNA)을 확인

(TCODE/프로그램 미존재, 자동수행 대상(XAUTO) 아님이면 오류 로그 남기고 종료)

2) 파라미터·Variant 발췌 — Activity Master에 등록된 파라미터/Variant를 SET_EXEC_PARAM으로 실행 파라미터(LT_PARAM)에 반영

3) 필수 공통 파라미터(기간·조직) 점검 — 누락 시 오류 로그를 남기고 정상 종료(EXIT)

4) 입력 정보를 메모리에 EXPORT 후 실제 프로그램을 SUBMIT(WITH SELECTION-TABLE)하여 실행

**● 보충 설명**

[상위 Job 보호 목적으로의 분리]

- 배치잡은 실행 중 런타임 오류나 selection-screen 필수 파라미터 누락 등으로 프로그램이 비정상 종료되면 Job 상태가 취소(Aborted)로 처리된다.

- Activity Group Job이 하위 프로그램을 직접 SUBMIT하면, 그 SUBMIT 시점의 오류가 SUBMIT을 수행하던 상위 Job까지 함께 중단시킬 수 있다.

- 이를 막기 위해 최하단 프로그램은 ZLPAC0101이라는 별도 셸의 독립 배치잡으로 분리한다. 파라미터 검증·오류는 ZLPAC0101 내부에서 처리(누락 시 로그 후 정상 종료)되고 실제 프로그램의 오류도 ZLPAC0101 Job(프로그램 레벨)에만 국한되므로, 상위의 Activity Group·Business Package Job은 중단되지 않고 나머지 노드를 계속 관리한다.

## 전체 · 상태 코드 참고

**● 자동수행 관점 프로세스**

완료 계열로 취급되는 Activity 상태: C(완료), T(수기완료), P(기간 Skip 완료), O(기타 완료). 진행 상태: R(진행중), W(대기), E(오류). Batch Job 상태(TBTCO): R(실행중)/S(Released)/Y(Ready)/A(중단)/F(완료). 자동수행 로직은 R/S/Y를 '실행중'으로 판단해 중복 생성을 막고, A(중단)는 강제 오류 처리한다.
