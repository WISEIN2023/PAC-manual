---
id: auto-trigger/04-auto-trigger-dongjak-jogeon-mit-enjin-dongjak
doc: auto-trigger
title: 4. Auto Trigger 동작 조건 및 엔진 동작 원리
parent: docs/auto-trigger/README.md
---

# 4. Auto Trigger 동작 조건 및 엔진 동작 원리

## 4.1 자동 수행을 위한 필수 조건

Auto Trigger가 정상 동작하려면 다음 세 가지 조건이 모두 충족되어야 합니다.

| 조건 | 내용 | 확인 방법 |
|---|---|---|
| ① Trigger Code 설정 | ZTPAC_CROSS_IF에 CRS Code가 등록되고 XAUTO=X로 설정 | ZLPAC0070 조회 |
| ② Activity 연결 | ZTPAC_PROC의 CRSCODE 또는 TG_CRSCODE에 해당 CRS Code 연결 | ZLPAC0020 조회 |
| ③ PAC 엔진 AUTO_NEXT 플래그 | ZCL_PAC_SAIL 생성 시 IV_AUTO_NEXT='X' 파라미터가 전달되어야 자동 수행 로직 활성화 | PAC 시스템 CONFIG 확인 |

> 📌 중요 : AUTO_NEXT 플래그 (MCP ZCL_PAC_SAIL 소스 확인)
> ZCL_PAC_SAIL 클래스는 CONSTRUCTOR 파라미터 IV_AUTO_NEXT를 받아 내부 변수 AV_AUTO_NEXT에 저장합니다.
> 이 값이 'X'여야만 Auto Trigger 로직이 실행됩니다.
> 이 파라미터는 PAC 배치잡 또는 자동수행 호출 시 PAC 시스템 CONFIG에서 제어합니다.

## 4.2 START_FROM_AUTO_TRIGGER 메서드 실행 흐름

ZCL_PAC_SAIL > START_FROM_AUTO_TRIGGER 메서드(MCP로 소스 확인)의 실제 동작 순서는 다음과 같습니다.

| 단계 | 내용 |
|---|---|
| 1. PCSGP 조회 | IV_PID로 해당 Activity의 PCSGP(프로세스 그룹) 조회 |
| 2. 수행 가능 여부 1차 체크 | ZFPAC_GET_CAN_START 호출 : 선행 Activity 완료 여부 확인 → EV_CANSTART=X여야 계속 진행 |
| 3. AUTO_TYPE=B 추가 체크 | Auto Execution Type이 'Business Package(B)'인 경우, 상위 PCSGP에 대해 ZFPAC_GET_CAN_START를 한번 더 호출 |
| 4. 후행 Activity 기동 | ZFPAC_CREATE_PCSGP_JOB 호출 : 백그라운드 잡으로 후행 Activity/Group 기동 |

## 4.3 후행이 일부 미완료 상태에서도 실행되는 이유

기초 자료에서 '앞부분이 다 실행되지 않았는데도 Trigger 실행 후 후행이 실행되는 이유'에 대한 설명입니다.

이는 AUTO_TYPE이 'A(Activity)'로 설정되어 있기 때문입니다. Activity 단위 Trigger는 특정 하나의 Activity가 완료되면 그것만으로 후행을 기동합니다. 전체 선행 Activity의 완료를 대기하지 않습니다.

| AUTO_TYPE | 후행 실행 조건 |
|---|---|
| A (Activity) | Trigger가 연결된 해당 Activity 하나가 완료되면 즉시 후행 기동 |
| B (Business Package) | 상위 PCSGP(BP 레벨)가 완료 가능 상태여야 후행 기동 |
| G (Activity Group) | 해당 Activity Group 단위로 수행 가능 여부를 판단하여 기동 |

**4.4 Trigger실행조건(Auto Execution Type별동작)**

Auto Next가 체크된 전제 하에, Trigger 실행 후 후행 Activity가 실제로 수행되는 조건은 ZLPAC0070에서 설정한 Auto Execution Type(AUTO_TYPE)에 따라 다르게 적용됩니다.

관련 소스 : ZCL_PAC_SAIL > START_FROM_AUTO_TRIGGER, ZFPAC_CHECK_PRENODE (MCP 확인)

| 구분 | AUTO_TYPE = A (Activity) | AUTO_TYPE = B (Business Package) |
|---|---|---|
| 수행 기준 | 트리거와 연결된 특정 Activity가 완료되면 즉시 후행 기동 | Activity Group(1레벨) 기준으로 트리거 앞에 있는 모든 선행이 완료되어야 후행 기동 |
| 링크(선행 연결) 있는 경우 | Activity Group 내에서 자신보다 선행 Activity의 완료 여부를 확인
(서브그룹 체크) | ZFPAC_CHECK_PRENODE 호출로 선행 Activity까지 완료 여부를 추가 검증.
트리거를 먼저 받더라도 선행이 미완료이면 후행 수행 불가 |
| 트리거 수신 → 선행 미완료 시 | 해당 Activity만 체크 — 서브그룹 내 선행 미완료이면 수행 안함 | 선행이 수행되지 않았으면 후행 Activity가 수행되지 않음
선행 Activity 완료 후에야 후행 Activity 수행됨 |
| 핵심 함수 | ZFPAC_GET_CAN_START → EV_CANSTART=X 여야 계속 진행 | ZFPAC_GET_CAN_START(1차) → ZFPAC_CHECK_PRENODE(2차 추가 검증) 모두 통과해야 수행 |

> 📌 MCP 소스 확인 — START_FROM_AUTO_TRIGGER의 AUTO_TYPE=B 처리 흐름
> 1. ZFPAC_GET_CAN_START 호출 : EV_CANSTART = X 여야 계속 진행
> 2. AUTO_TYPE = B인 경우 ZFPAC_CHECK_PRENODE 추가 호출
> → IV_PID(트리거 연결 Activity)보다 선행인 Activity가 모두 완료(C)여야 EV_SUBRC=0 반환
> 3. EV_SUBRC ≠ 0이면 CHECK LV_SUBRC EQ 0 조건에 의해 ZFPAC_CREATE_PCSGP_JOB 호출하지 않음
> 4. 선행 완료 후 다음 Trigger 또는 SAIL 루프에서 다시 조건 충족 시 후행이 수행됨

**4.5 Auto Trigger관련Function Module상세**

Auto Trigger 수행에 관여하는 핵심 Function Module들입니다. BUPAK_TRIGGER 메서드(ZCL_PAC_SAIL)에서 TRIG_TYPE에 따라 적합한 FM을 호출합니다.

| FM명 | Function Group | 역할 및 호출 조건 |
|---|---|---|
| ZFPAC_AUTOTRIG_CHECK | ZPAC111 | Legacy / Other Module에서 들어오는 Trigger의 사전 유효성 검증 전용.
Trigger Code 존재 여부, 조직 유효성, Period 유효성, 이미 완료/수행중 여부를 순차 체크.
BUPAK은 ZTPAC_CROSS_IF의 TG_BUPAK에서 자동 조회 |
| ZFPAC_AUTOTRIG_CROSS_BUPAK | ZPAC111 | TRIG_TYPE = B (Between Business Package)인 경우 호출.
Outbound Activity 완료를 기록하고, Inbound BP의 후행 Activity를 기동.
Outbound 조직 N : Inbound 조직 N 설정 가능. Outbound 조직이 모두 완료되어야 Inbound 기동 |
| ZFPAC_AUTOTRIG_CROSS_ORG | ZPAC111 | TRIG_TYPE = O (Between Organization)인 경우 호출.
동일 Business Package 내 서로 다른 조직(법인) 간 Trigger.
ZTPAC_TRIG_ORG 테이블의 조직 매핑을 기준으로 Outbound 조직 완료 후 Inbound 조직 기동 |
| ZFPAC_AUTOTRIG_LEGACY | ZPAC111 | TRIG_TYPE = L (From Legacy)인 경우 호출.
Legacy 시스템(SAP 외부)과의 연계에 사용. MODE=E(실행)/C(취소)/R(Running)/F(실패) 지원.
MODE=F 사용 시 IS_MSG(오류 메시지) 파라미터 필수 |
| ZFPAC_AUTOTRIG_OTHERS | ZPAC111 | TRIG_TYPE = S (From Other Module)인 경우 호출.
PAC을 사용하지 않는 SAP 타 업무(MM, SD 등)와의 연계에 사용.
PAC 내부 BP 간 Trigger에는 사용하지 않음 |

> 📌 FM 호출 분기 로직 (MCP ZCL_PAC_SAIL > BUPAK_TRIGGER 소스 확인)
> ZTPAC_CROSS_IF에서 TRIG_TYPE 조회 후:
> TRIG_TYPE = 'B' → ZFPAC_AUTOTRIG_CROSS_BUPAK 호출
> TRIG_TYPE = 'O' → ZFPAC_AUTOTRIG_CROSS_ORG 호출
> (TRIG_TYPE = 'L' / 'S'는 외부 시스템이 직접 FM을 호출하는 방식으로 동작)

**4.6 STARTFROM /START ALL기능설명**

PAC 실행 엔진(ZCL_PAC_SAIL)에는 특정 Activity부터 시작하거나 전체를 재시작하는 두 가지 실행 모드가 있습니다.

| 구분 | START FROM (IV_START_FROM) | START ALL |
|---|---|---|
| 개념 | 지정한 특정 Activity(PID)부터 해당 라인만 수행 | 해당 Activity Group(PCSGP) 내 수행 가능한 모든 Activity를 순차 수행 |
| 파라미터 | CONSTRUCTOR의 IV_START_FROM에 대상 PID 입력 | IV_START_FROM 미입력(공백) 상태로 실행 |
| 동작 방식 | 지정 PID의 Child Node(하위)와 Parent Node(상위 라인)만 추출하여 해당 라인 외 Activity는
수행 불가 상태(EXEC=공백, CANRUN=공백)로 처리 후 실행 | SELECT_NODE_EXECUTABLE로 수행 가능한 모든 노드를 계산하여 순차 기동 |
| 사용 목적 | 특정 Activity만 재실행이 필요하거나, 오류 발생 후 해당 라인만 재수행할 때 | 일반적인 PAC 자동수행 시 사용 |
| 소스 근거 | SAIL_BUSINESS_PACKAGE / SAIL_PROCESS_GROUP 내
IF AV_START_FROM IS NOT INITIAL 분기 처리 (MCP 확인) | 동일 메서드 내 AV_START_FROM IS INITIAL 상태에서의 기본 수행 경로 |

> 📌 START FROM 상세 동작 (MCP SAIL_BUSINESS_PACKAGE / SAIL_PROCESS_GROUP 소스 확인)
> 1. SELECT_CHILD_NODE_LIST : 지정 PID의 하위 노드 목록 조회
> 2. SELECT_PARENT_NODE_LIST : 지정 PID의 상위(같은 라인) 노드 목록 조회
> 3. 두 목록 합산 후 중복 제거
> 4. 해당 목록 외의 Activity는 EXEC/CANRUN을 공백으로 세팅 → 수행 불가 처리
> 5. SELECT_NODE_EXECUTABLE로 수행 가능 노드 재계산 후 해당 라인만 실행
