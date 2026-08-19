---
id: pac-config/03-16-special-auth-check
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.16 Special Auth Check
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.16 Special Auth Check

### 3.16.1 ADMIN_AUTH — Authorization Check Type

**테이블-필드:** ZTPACSYS - ADMIN_AUTH

**운영 설정(LG전자 설정) :** S : By Special Role

#### 설정 설명

□ Admin 권한을 체크하는 유형을 정의

S : By Special Role -> Special Role에 Admin 유형에 등록된 유저를 Admin으로 인식

O : By Authorization Object -> Admin Auth Group으로 등록된 유저를 Admin으로 인식

A : By Special Role + Object -> S, O 둘중 하나를 가진경우 Admin으로 인식

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

Admin 권한 체크 유형(S: Special Role / O: Auth Object / A: 둘 다).

① CHECK_SPECIAL_AUTH(IV_AUTH_TYPE='A'): S이면 ZTPAC_SPAUTH(Special Role 등록 테이블)에서 유저 조회, O이면 ADMIN_OBJ의 권한그룹으로 Authorization Object 체크, A이면 둘 중 하나라도 충족 시 Admin 인정.

② Admin 권한은 관리 화면 접근/Reset/강제 처리 등 특수 기능의 게이트로 시스템 전역에서 사용.

#### 영향도 분석 (변경 시 영향)

관리자 판정 방식 자체가 바뀌는 설정 — S→O 전환 시 ZTPAC_SPAUTH 등록자가 아닌 권한그룹 보유자로 Admin이 재정의되므로, 전환 전 대상자 매핑을 완료하지 않으면 관리자 접근 공백/과다 부여 발생.

### 3.16.2 ADMIN_OBJ — PAC Authorization Group

**테이블-필드:** ZTPACSYS - ADMIN_OBJ

#### 설정 설명

□ Admin Authorization Check Type(ADMIN_AUTH)를 O, A로 설정한 경우 활성화 된다

□ Admin으로 지정할 Authorization Group을 입력한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008), ZLPACSYS_F01/I01

#### 프로세스 관점 분석 (사용 로직)

Admin용 PAC Authorization Group.

① ADMIN_AUTH가 O/A일 때 권한 오브젝트 체크에 사용할 Auth Group 값. ZLPACSYS 화면에서 유형이 O/A일 때만 입력 활성(I01에서 필수 체크).

#### 영향도 분석 (변경 시 영향)

오입력 시 Admin 판정이 전원 실패(관리 기능 접근 불가) 또는 의도치 않은 그룹에 Admin 부여 — 권한 Role 설계와 일치 필수.

### 3.16.3 TF_AUTH — Authorization Check Type

**테이블-필드:** ZTPACSYS - TF_AUTH

**운영 설정(LG전자 설정) :** O : By Authorization Object

#### 설정 설명

□ TF 권한을 체크하는 유형을 정의

S : By Special Role -> Special Role에 TF 유형에 등록된 유저를 HQ으로 인식

O : By Authorization Object -> TF Auth Group으로 등록된 유저를 HQ 인식

A : By Special Role + Object -> S, O 둘중 하나를 가진경우 HQ으로 인식

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

TF(Task Force) 권한 체크 유형(S/O/A).

① CHECK_SPECIAL_AUTH(IV_AUTH_TYPE='T'): Admin과 동일 로직으로 TF 권한 판정 — 결산 TF 인원에게 부여되는 중간 수준 권한 게이트.

#### 영향도 분석 (변경 시 영향)

ADMIN_AUTH와 동일한 주의사항 — TF 권한자의 판정 기준이 바뀌므로 전환 시 대상자 매핑 선행.

### 3.16.4 TF_OBJ — PAC Authorization Group

**테이블-필드:** ZTPACSYS - TF_OBJ

**운영 설정(LG전자 설정) :** IT

#### 설정 설명

□ TF Authorization Check Type(TF_AUTH)를 O, A로 설정한 경우 활성화 된다

□ TF으로 지정할 Authorization Group을 입력한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008), ZLPACSYS_F01/I01

#### 프로세스 관점 분석 (사용 로직)

TF용 PAC Authorization Group.

① TF_AUTH가 O/A일 때 사용할 Auth Group.

#### 영향도 분석 (변경 시 영향)

ADMIN_OBJ와 동일 — 오입력 시 TF 권한 판정 실패/오부여.

### 3.16.5 HQ_AUTH — Authorization Check Type

**테이블-필드:** ZTPACSYS - HQ_AUTH

**운영 설정(LG전자 설정) :** O : By Authorization Object

#### 설정 설명

□ HQ 권한을 체크하는 유형을 정의

S : By Special Role -> Special Role에 HQ 유형에 등록된 유저를 HQ으로 인식

O : By Authorization Object -> HQ Auth Group으로 등록된 유저를 HQ 인식

A : By Special Role + Object -> S, O 둘중 하나를 가진경우 HQ으로 인식

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008)/CHECK_AUTH_HQ(CM003), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

HQ(본사) 권한 체크 유형(S/O/A).

① CHECK_SPECIAL_AUTH(IV_AUTH_TYPE='H') → CHECK_AUTH_HQ가 래핑. HQ 권한자는 ZFPAC_USER_AUTH에서 전체 실행/조회 권한(ALL) 부여, ZFPAC_PORTAL_NOTICE_LIST에서 전체 공지 조회 등 조직 제한 없는 접근의 기준.

#### 영향도 분석 (변경 시 영향)

HQ 권한은 조직 제한을 우회하는 최고 수준 조회/실행 권한 — 판정 기준 변경 시 전 조직 데이터 접근 범위가 바뀌므로 보안 관점 검토 필수.

### 3.16.6 HQ_OBJ — PAC Authorization Group

**테이블-필드:** ZTPACSYS - HQ_OBJ

**운영 설정(LG전자 설정) :** HQ

#### 설정 설명

□ HQ Authorization Check Type(ADMIN_AUTH)를 O, A로 설정한 경우 활성화 된다

□ HQ으로 지정할 Authorization Group을 입력한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH(CM008), ZLPACSYS_F01/I01

#### 프로세스 관점 분석 (사용 로직)

HQ용 PAC Authorization Group.

① HQ_AUTH가 O/A일 때 사용할 Auth Group.

#### 영향도 분석 (변경 시 영향)

ADMIN_OBJ와 동일 — 오입력 시 HQ 권한 판정 실패/오부여.
