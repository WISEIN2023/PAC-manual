---
id: pac-config/02-15-auto-exectution
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.15 Auto Exectution
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.15 Auto Exectution

### 2.15.1 XAUTO_START — Always auto start after completed

**테이블-필드:** ZTPAC_CONFIG - XAUTO_START

**운영 설정(LG전자 특화) :** 모두 활성

#### 설정 설명

□ X 설정된 경우 : 자동수행이 가능한 경우 자동수행으로 항상 실행된다

□ X 설정된 경우 : 아래가 함께 활성화 된다

- Auto Start After Manual Activity Confirm(AFTER_CONF) : X

- Auto Start After Schedule Closed(AFTER_CLSD) : X

- Auto Execution Level when manual confirm : X (The Next linked activity groups)

- Auto Execution Level when manual confirm :  J(Activities & Groups in BusPkg)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_NEXT_AUTO_START(LZPAC059U01), ZCL_PAC_SAIL=>CHECK_CAN_ALWAYAS_START(CM01D)/CHECK_CAN_START_NEXT_AUTO(CM006)/

MANUAL_COMPLETE(CM00M)/SAIL_PROCESS_GROUP 분기, ZFPAC_CONFIRM_ITEM(LZPAC052U01), ZFPAC_CREATE_PCSGP_JOB(LZPAC050U03),

ZFPAC_SCHID_CLOSE 연계(LZPAC131F01), ZCL_PAC=>UPDATE_PAC_STATUS(CM01X), ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

「완료 후 항상 자동시작(Always auto start after completed)」 — 자동수행 가능하면 무조건 자동 실행하는 최상위 자동화 모드.

① ZFPAC_NEXT_AUTO_START: 'X'이면 그룹 Job 생성 후 추가로 ZCL_PAC_SAIL=>CHECK_CAN_ALWAYAS_START로 전체 시작 가능 여부를 판단하여 ZFPAC_CREATE_BUPAK_JOB(BusPkg 전체) 또는 ZFPAC_CREATE_GPID_JOB(Global)을 기동.

② ZCL_PAC_SAIL: 공백일 때는 다른 Activity Line에 수행가능 노드가 있으면 자동시작을 보류하는 로직이 있어, 'X' 설정 시 이 제약 없이 항상 진행.

③ ZFPAC_CONFIRM_ITEM / MANUAL_COMPLETE: 공백이고 AFTER_CONF='X'일 때만 개별 NEXT_AUTO_START 호출 — 'X'면 개별 트리거 대신 상시 자동화 우선.

④ ZLPAC0010: 체크 시 AFTER_CONF/AFTER_CLSD/XAUTO_NEXT='X', CONFLVL='J' 강제 세팅 + 입력 잠금.

#### 영향도 분석 (변경 시 영향)

PAC 자동화 수준을 결정하는 최상위 스위치 — 활성 시 수행가능 노드가 생기는 즉시 배치가 연쇄 기동되므로 배치 부하(RATE_* 유휴율 설정)와 함께 관리 필요.

해제 시 Confirm/Close 이벤트 기반 자동화(AFTER_CONF/AFTER_CLSD)로만 동작하여 자동화 범위가 축소됨.

### 2.15.2 AFTER_CONF — Auto Start After Manual Activity Confirm

**테이블-필드:** ZTPAC_CONFIG - AFTER_CONF

**운영 설정(LG전자 특화) :** 모두 활성

#### 설정 설명

□ X 설정 : Manual Confirm 수행시 다음 Activity가 자동 수행가능하면 자동 수행된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CONFIRM_ITEM(LZPAC052U01), ZCL_PAC_SAIL=>MANUAL_COMPLETE(CM00M), 결산점검 Confirm(ZLPAC5100/5110/5200/5210/5300/5310_F01),

ZFPAC_AUTOTRIG_CROSS_BUPAK(LZPAC054U02), ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

Manual Confirm 수행 후 다음 Activity 자동 시작 여부.

① ZFPAC_CONFIRM_ITEM: Confirm 성공 → SYNC_PCSGP_STATUS 후 「XAUTO_START 공백 AND AFTER_CONF='X'」이면 ZFPAC_NEXT_AUTO_START 호출로 후속 Activity 자동 기동.

② ZCL_PAC_SAIL=>MANUAL_COMPLETE 등 다른 Confirm 경로에서도 동일 패턴.

③ 결산점검(ZLPAC5xxx) 시나리오 Confirm 후에도 동일 트리거.

④ ZLPAC0010: AFTER_CONF/AFTER_CLSD 모두 공백이면 XAUTO_NEXT·CONFLVL 필드 비활성, 체크 시 CONFLVL 기본값 'J'.

#### 영향도 분석 (변경 시 영향)

해제 시 Manual Confirm 후 후속 Activity가 자동으로 시작되지 않아 담당자가 수동으로 다음 단계를 실행해야 함 — 자동화 흐름 단절로 결산 소요시간 증가.

활성 시 Confirm 즉시 후속 배치가 기동되므로 Confirm 시점 관리가 곧 실행 시점 관리가 됨.

### 2.15.3 AFTER_CLSD — Auto Start After Schedule Closed

**테이블-필드:** ZTPAC_CONFIG - AFTER_CLSD

**운영 설정(LG전자 특화) :** 모두 활성

#### 설정 설명

□ X 설정 : 결산 일정 Closed 시 다음 Activity가 자동 수행가능하면 자동 수행된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_SCHID_CLOSE/SCH_DELAY_CLOSE의 후속 처리(LZPAC131F01 - PID_STATUS_CHANGE), ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

결산일정 Close 시 다음 Activity 자동 시작 여부.

① ZFPAC_SCHID_CLOSE(수동/Overdue 자동 Close 공통): 일정 Close 후 PID_STATUS_CHANGE(LZPAC131F01)에서 해당 일정에 연결된 Schedule Activity 상태를 완료 처리하고, AFTER_CLSD='X'인 BusPkg는 ZFPAC_NEXT_AUTO_START로 후속 Activity를 자동 기동.

② 일정 기반 자동화(마감시각 도래 → 자동 실행 개시)의 트리거.

#### 영향도 분석 (변경 시 영향)

해제 시 일정 Close 이후의 자동 실행 개시가 중단되어 시각 기반 자동화가 끊김 — 야간 마감 자동 진행에 의존하는 운영이라면 치명적.

활성 시 Overdue 자동 Close에 의해서도 후속 실행이 기동되므로 일정 시각 설정의 정확성이 중요해짐.

### 2.15.4 CONFLVL — Check previous linked activities completed by

**테이블-필드:** ZTPAC_CONFIG - CONFLVL

**운영 설정(LG전자 특화) :** 모두 J로 설정

#### 설정 설명

□ Next Auto로 자동 수행시 이전 Activity 상태 체킹 기준을 설정한다

1) J : Activities & Groups in the Business Packag

- Activity 및 Group의 상태를 다 체킹하여 수행한다

- Next Execution Level이 'The next linked activity group'으로 설정된 경우는 이 설정만 적용할 수 있다

2) A : Activities only in the started group

- 이벤트가 일어난 최하단 레벨의 상태만 체킹하여 해당 레벨이 수행가능하면 실행한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_NEXT_AUTO_START(LZPAC059U01) → ZFPAC_CHECK_PRENODE(SAPLZPAC051), ZLPAC0010_F01(SET_LIST_BOX_FOR_CONFLVL)

#### 프로세스 관점 분석 (사용 로직)

Next Auto 자동수행 시 이전 Activity 완료 체킹 기준(J: BusPkg 내 전체 그룹 / A: 시작된 그룹 내 Activity만).

① ZFPAC_NEXT_AUTO_START: 'A'이면 ZFPAC_CHECK_PRENODE 호출 시 IV_HERE='X'로 전달되어 해당 Group 범위만 완료 체크, 'J'면 부모 Node의 Group까지 모두 완료되어야 후속 자동시작 진행.

② ZLPAC0010: XAUTO_NEXT='X'이면 'J'만 선택 가능(리스트박스 제한 + 강제 세팅).

#### 영향도 분석 (변경 시 영향)

J→A 변경 시 선행 그룹이 미완료여도 그룹 내 조건만 충족하면 후속이 자동 시작됨 — 자동화는 빨라지나 선행 프로세스 미완료 상태의 조기 실행 위험.

A→J 변경 시 반대로 자동 시작 조건이 엄격해져 진행이 늦어질 수 있음.

### 2.15.5 XAUTO_NEXT — Next Execution Level

**테이블-필드:** ZTPAC_CONFIG - XAUTO_NEXT

**운영 설정(LG전자 특화) :** 모두 X로 설정

#### 설정 설명

□ Manual Confirm 혹인 Schedule Close 이후 자동 수행시의 수행 레벨을 정의

1) ' ' : Only This activity level : 이벤트가 발생된 최하단의 Level 단계에서만 자동 수행 된다 (Auto

2) X : The next linked activity groups : 최하단이 발생되면 해당 Group을 자동 수행하고 다음 레벨들도 수행된다

(Auto Next 적용)

※ Auto Start가 적용된 경우

Activity Group 배치잡을 생성한다 : IV_HERE = 'X', IV_AUTO_NEXT = 적용여부, IV_START_FROM = 발생 PID

IV_START_FROM을 통해 이벤트가 발생된 Line만 수행되도록 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_NEXT_AUTO_START(LZPAC059U01) → ZFPAC_CREATE_PCSGP_JOB의 IV_AUTO_NEXT, ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

Manual Confirm/Schedule Close 이후 자동수행의 수행 레벨(공백: 해당 그룹 라인만 / X: 다음 그룹까지 연쇄).

① ZFPAC_NEXT_AUTO_START: 공백이면 해당 Group의 노드/링크를 조회(SELECT_NODE/LINK/NODE_EXECUTABLE)하여 Confirm된 PID의 후행 라인에 수행가능 노드가 있을 때만 그룹 Job 생성. 'X'이면 이 사전 체크를 생략하고 ZFPAC_CREATE_PCSGP_JOB에 IV_AUTO_NEXT='X'로 전달되어 그룹 완료 시 다음 그룹까지 자동 연쇄 수행.

② ZLPAC0010: 'X' 선택 시 CONFLVL='J' 고정.

#### 영향도 분석 (변경 시 영향)

'X' 설정 시 그룹 경계를 넘어 자동화가 연쇄되므로 한 번의 Confirm으로 여러 그룹의 배치가 이어질 수 있음 — 배치 부하와 실행 순서 모니터링 강화 필요.

해제 시 그룹마다 수동 개입(Confirm)이 필요해져 자동화 범위 축소.
