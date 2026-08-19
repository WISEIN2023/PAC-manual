---
id: pac-config/02-04-posting
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.4 Posting
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.4 Posting

### 2.4.1 USER_TYPE — Posting User Type

**테이블-필드:** ZTPAC_CONFIG - USER_TYPE

**운영 설정(LG전자 특화) :** LG전자는 모두 Fixed User로 설정

#### 설정 설명

□ Batch Job을 수행하는 User 유형을 정의한다

- A : By Actual Execution User -> Start 수행 버튼을 누른 User로 지정

- R : By Participants -> Participant에 지정된 Posting User로 지정 (R 설정된 경우 Participant 화면에 Posing 유저 설정 필드가 활성화 된다)

- F : By Fixed User -> 지정된 고정 유저로 설정

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_USER_AUTH(LZPAC040U01), ZCL_PAC_LOG=>WRITE_LOG_HEADER(CM00N),

ZLPAC1000/1011(Participant 관리), ZLPAC0010_F01(CONFIRM_SAVE_DATA/SCREEN_PBO_0110)

#### 프로세스 관점 분석 (사용 로직)

배치 Job 수행 유저 유형(A:실제 실행유저 / R:Role별 지정유저 / F:고정유저).

① ZFPAC_USER_AUTH: PAC 실행 시 Posting User 결정 분기 — A면 SY-UNAME, R이면 Participant에 등록된 Posting User(우선순위 Activity>Group>Org, 미지정 시 POST_USER가 Default), F면 POST_USER 고정.

② ZCL_PAC_LOG=>WRITE_LOG_HEADER: 배치 + 'A'이면 로그 헤더의 수행자(PSNAM)를 실제 실행자(EXNAM)로 기록.

③ ZLPAC1000/1011: R 유형일 때 Participant 화면에 Posting User 지정 컬럼 활성화.

④ ZLPAC0010: 필수값(S191). 'A' 선택 시 POST_USER 숨김/클리어, R·F 선택 시 POST_USER 필수.

#### 영향도 분석 (변경 시 영향)

배치 Job의 실행(기표) 권한 주체가 바뀌는 설정 — 변경 시 대상 유저의 권한(Role) 보유 여부를 반드시 확인해야 하며, 미비 시 자동 기표가 권한 오류로 실패.

로그의 수행자 기록 기준도 함께 바뀌어 감사 추적에 영향.

### 2.4.2 POST_USER — Posting User

**테이블-필드:** ZTPAC_CONFIG - POST_USER

**운영 설정(LG전자 특화) :** INTCWFPO001

#### 설정 설명

1) R로 설정된 경우 : Default Posting User로 사용이 되며 Participannt 화면에 Post User를 설정하지 않은 경우 여기 입력된 유저로 사용된다

2) F로 설정된 경우 : Fixed User ID로 활용

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_USER_AUTH(LZPAC040 U01/F01), ZFPAC_CREATE_SCH_JOB(LZPAC050U11), ZLPAC1010/1020(Participant)

#### 프로세스 관점 분석 (사용 로직)

Posting(배치 실행) 유저 ID.

① USER_TYPE='F'(Fixed): 모든 배치 Job이 이 유저로 생성·기표됨(ZFPAC_USER_AUTH가 EV_POST_USER로 반환 → Job 생성 시 실행 유저로 사용).

② USER_TYPE='R'(Role): Participant에 Posting User 미지정 조직의 Default 유저로 동작.

③ ZFPAC_CREATE_SCH_JOB(결산일정 Job 생성)에서도 실행 유저로 참조.

#### 영향도 분석 (변경 시 영향)

이 유저가 잠금/삭제/권한 회수되면 자동 기표 전체가 장애 — 유저 유효성(잠금 여부, Role 유지)을 정기 점검해야 하는 최우선 운영 항목.

변경 시 신규 유저의 권한 검증 후 반영 필요.
