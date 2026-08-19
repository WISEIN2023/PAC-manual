---
id: pac-config/02-02-authorization
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.2 Authorization
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.2 Authorization

### 2.2.1 XDIRECT — Direct TCODE Enable?

**테이블-필드:** ZTPAC_CONFIG - XDIRECT

**운영 설정(LG전자 특화) :** 운영은 모두 설정

#### 설정 설명

- PAC에서 자동으로 수행이 되야하는 Activity들은 TCODE 접속으로 수행되는것을 방지하고 있다

( PID가 정확히 입력이 된 경우만 수행이 되어야 로깅상에 문제가 없으므로)

- X가 설정된 경우는 TCODE 직접 수행을 허용하게 된다. (개발단계에서는 보통 허용을 하나 운영에서는 리스크 차단을 위해 허용하지 않는다)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON (TCODE Direct 실행 체크 로직)

#### 프로세스 관점 분석 (사용 로직)

자동수행 Activity의 TCODE 직접 실행 허용 여부.

① ZIPAC_COMMON: 사용자가 TCODE로 직접 접속하면, 해당 TCODE가 자동수행(XAUTO='X') Activity로 등록된 BusPkg 중 XDIRECT가 공백인 것이 하나라도 있으면 「Can't execute this TCODE directly. Please try by using Map」(ZPAC01-037) 메시지와 함께 실행 차단.

② 즉 X 설정 시 TCODE 직접 실행이 허용되고, 미설정 시 반드시 PAC Map을 통해서만 실행 가능.

#### 영향도 분석 (변경 시 영향)

해제(공백 전환) 시 해당 BusPkg에 등록된 자동수행 Activity의 TCODE 직접 사용이 일괄 차단됨 — 현업의 기존 TCODE 사용 업무가 즉시 막히므로 변경 시 사전 공지 필수.

반대로 X 설정 시 PAC 로그를 우회한 직접 실행이 허용되어 실행 통제가 약화됨.

### 2.2.2 XROLE_USE — Active Authorization Group?

**테이블-필드:** ZTPAC_CONFIG - XROLE_USE

**운영 설정(LG전자 특화) :** 미사용

#### 설정 설명

□ Activation : PAC의 Authorization Group에 설정된 권한을 통제할 수 있다.

- Authorization Group은 Standard Role 및 권한 Object 조합으로 구성된다.

- Activity 별로 Standard 권한을 통해 체킹하기 위한 용도로 사용된다.

□ Authorization Group 설정

1) ZLPAC1030 - Define Authorization Group 에서 Authorization Group 설정

2) Activity Master에 Authorization Group 필드가 활성화 된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC0020_F01/ZLPAC0020_ALV (Activity Master)

#### 프로세스 관점 분석 (사용 로직)

Activity Master(ZLPAC0020)에서 Authorization Group 컬럼의 표시/입력을 활성화.

① ZLPAC0020_F01/ALV: 'X'일 때 Activity별 Auth Group 필드가 ALV 필드카탈로그에 노출되어 Activity 단위 권한그룹을 지정 가능.

② 지정된 Auth Group은 Activity 실행 권한 통제(ZCL_PAC_AUTH 계열 체크)에 사용됨.

#### 영향도 분석 (변경 시 영향)

활성화 시 Activity 단위 권한그룹 통제가 추가되어 권한 미보유 유저의 실행이 제한될 수 있음.

해제 시 기존에 입력된 Auth Group 값은 남지만 화면에서 관리 불가 상태가 됨.
