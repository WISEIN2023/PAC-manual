---
id: pac-config/03-13-user-output-field
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.13 User Output FIeld
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.13 User Output FIeld

### 3.13.1 USRID_S — User ID Display

**테이블-필드:** ZTPACSYS - USRID_S

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

X 활성화시 : User ID를 조회가능하도록 활성화한다 (PAC의 유저관련 정보에 SAP ID 필드 출력)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ 유저 관련 전 화면 약 25개 Include: ZLPAC1000/1010/1011/1020/1050(Participant·권한), ZLPAC0080(Skip), ZLPAC0600,

ZLPAC5080/5090(CIS), ZLPAC7140/7160(일정 알람), LZPAC042(ZFPAC_AUTH_CHG_MASS), LZPAC043(ZFPAC_PID_AUTHLIST),

LZPAC057(ZFPAC_DIS_TRIG_STATUS), LZPAC136/137(SCH_ALARM), LZPAC201(ZFPAC_GET_MAIL_RECEIVER), LZPAC221/223, LZPACCIS0015

#### 프로세스 관점 분석 (사용 로직)

PAC 유저 관련 화면에서 SAP User ID 컬럼의 조회 표시 여부.

① 각 화면의 ALV 필드카탈로그 구성(F01/ALV Include)에서 공백이면 해당 컬럼 NO_OUT(숨김) 처리.

② _S/_E 계열 8개 필드(USRID/EMPNO/UNAME/EMAIL)는 동일 패턴으로 유저 식별 정보의 표시/편집 정책을 시스템 전역에서 통일 관리.

#### 영향도 분석 (변경 시 영향)

시스템 전역의 유저 관련 화면(약 25개)에 일괄 적용되므로 개별 화면 단위 예외가 불가 — 표시 정책 변경 시 전 화면 영향.

개인정보 표시 정책(User ID 노출 여부)과 연관.

### 3.13.2 USRID_E — User ID Editable

**테이블-필드:** ZTPACSYS - USRID_E

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

X 활성화시 : User ID를 수정가능한 필드로 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군 + ZCL_PAC_ORG=>ON_GET_USERINFO(CM00I)

#### 프로세스 관점 분석 (사용 로직)

User ID 컬럼의 수정(입력) 허용 여부.

① ALV EDIT 속성 제어: 'X'이면 Participant 등록 등에서 User ID 직접 입력 가능, 공백이면 조회 전용(사번 등 다른 키로만 입력).

② DISUSER(사원마스터) 구성과 조합하여 입력 기준 필드를 결정.

#### 영향도 분석 (변경 시 영향)

해제 시 User ID 직접 입력이 전 화면에서 막혀 사번/이름 기반 입력만 가능 — 담당자 등록 절차가 바뀜.

DISUSER 구성과 불일치하면 입력 가능한 키가 없어지는 조합이 될 수 있으므로 세트로 검토.

### 3.13.3 EMPNO_S — Employee Number Display

**테이블-필드:** ZTPACSYS - EMPNO_S

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

X 활성화시 : 사원번호를 조회가능하도록 활성화한다 (PAC의 유저관련 정보에 SAP ID 필드 출력)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군

#### 프로세스 관점 분석 (사용 로직)

사원번호 컬럼의 조회 표시 여부.

① 각 유저 관련 화면 ALV에서 사번 컬럼 표시/숨김 제어.

#### 영향도 분석 (변경 시 영향)

전역 일괄 적용 — 사번 노출 정책(개인정보) 관점에서 관리.

### 3.13.4 EMPNO_E — Employee Number Editable

**테이블-필드:** ZTPACSYS - EMPNO_E

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

X 활성화시 : 사원번호를 수정가능한 필드로 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군 + ZCL_PAC_ORG=>ON_GET_USERINFO(CM00I)

#### 프로세스 관점 분석 (사용 로직)

사원번호 컬럼의 수정 허용 여부.

① 'X'이면 사번으로 담당자 입력 가능(입력 시 ON_GET_USERINFO로 사원마스터에서 나머지 정보 자동 보완).

#### 영향도 분석 (변경 시 영향)

해제 시 사번 기반 담당자 등록 불가 — DISUSER(사원마스터) 활성 환경에서는 주요 입력 수단이므로 신중히.

### 3.13.5 UNAME_S — User Name Display

**테이블-필드:** ZTPACSYS - UNAME_S

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : 사용자 이름을 조회가능하도록 활성화한다 (PAC의 유저관련 정보에 SAP ID 필드 출력)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군

#### 프로세스 관점 분석 (사용 로직)

사용자 이름 컬럼의 조회 표시 여부.

#### 영향도 분석 (변경 시 영향)

전역 일괄 적용 — 표시 전용.

### 3.13.6 UNAME_E — User Name Editable

**테이블-필드:** ZTPACSYS - UNAME_E

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : 사용자 이름을 수정가능한 필드로 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군

#### 프로세스 관점 분석 (사용 로직)

사용자 이름 컬럼의 수정 허용 여부.

#### 영향도 분석 (변경 시 영향)

해제 시 이름 직접 입력/수정 불가 — 표시 정보는 사원마스터 자동 보완에 의존하게 됨.

### 3.13.7 EMAIL_S — Email Display

**테이블-필드:** ZTPACSYS - EMAIL_S

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : 이메일을 조회가능하도록 활성화한다 (PAC의 유저관련 정보에 SAP ID 필드 출력)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군

#### 프로세스 관점 분석 (사용 로직)

이메일 컬럼의 조회 표시 여부.

① 메일 수신자 조회(ZFPAC_GET_MAIL_RECEIVER, LZPAC201) 및 알람 수신자 화면에서 표시 제어.

#### 영향도 분석 (변경 시 영향)

전역 일괄 적용 — 메일 주소 노출 정책 관점에서 관리.

### 3.13.8 EMAIL_E — Email Editable

**테이블-필드:** ZTPACSYS - EMAIL_E

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : 이메일을 수정가능한 필드로 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ USRID_S와 동일 화면군 + ZCL_PAC_ORG=>ON_GET_USERINFO(CM00I)

#### 프로세스 관점 분석 (사용 로직)

이메일 컬럼의 수정 허용 여부.

① 'X'이면 수신자 메일 주소를 직접 입력/수정 가능 — 사원마스터에 메일이 없는 외부 인원 등록 시 활용.

#### 영향도 분석 (변경 시 영향)

해제 시 사원마스터에 메일이 없는 인원(외부 인력 등)의 알람 수신 등록이 불가해짐.

### 3.13.9 USERINFO — Additional Info for User Auth

**테이블-필드:** ZTPACSYS - USERINFO

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

X 활성화시 : 유저 Additional Field를 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC1000_F01, ZLPAC1010F01, ZLPAC1011_F01, ZLPAC1020F01, LZPAC043U01(ZFPAC_PID_AUTHLIST)

#### 프로세스 관점 분석 (사용 로직)

유저 Additional Info 필드 활성화.

① Participant/권한 화면에서 추가 정보 컬럼(부서 등 부가 필드)을 표시하도록 활성화.

#### 영향도 분석 (변경 시 영향)

표시 전용 — 해제 시 부가 정보 컬럼만 숨겨지고 데이터는 유지.
