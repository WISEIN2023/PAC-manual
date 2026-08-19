---
id: pac-config/02-03-additional-activation
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.3 Additional Activation
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.3 Additional Activation

### 2.3.1 XPRE_USE — Closing Precheck Use?

**테이블-필드:** ZTPAC_CONFIG - XPRE_USE

**운영 설정(LG전자 특화) :** 미사용

#### 설정 설명

사전점검 필수체크 여부

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(사전점검 완료 체크), ZCL_PAC_SAIL=>IS_PRECHECK_COMPLETED(CM00K),

ZFPAC_CREATE_BUPAK_JOB/ZFPAC_CREATE_PCSGP_JOB(LZPAC050 U02/U03), ZLPAC0020_F01/F02, ZLPAC0010_F01/I01

#### 프로세스 관점 분석 (사용 로직)

결산 사전점검(Closing Precheck) 필수 여부.

① ZIPAC_COMMON: Actual 모드 + 비배치 + REPTY≠S(사전점검 자신 제외)일 때 ZCL_PAC_SAIL=>IS_PRECHECK_COMPLETED로 PRE_PID Activity의 상태를 조회, 완료('C'/'T')가 아니면 「Closing Precheck is not completed yet!」(ZPAC01-029)로 실행 차단.

② 배치 실행은 ZFPAC_CREATE_BUPAK_JOB/PCSGP_JOB의 START 시점에 동일 체크.

③ ZLPAC0010: 체크 시 PRE_PID 필수 입력(E092), 해제 시 PRE_PID 자동 클리어 및 화면 비활성.

#### 영향도 분석 (변경 시 영향)

활성화 시 사전점검 Activity 완료 전에는 모든 Activity 실행(포그라운드/배치)이 차단되므로 월초 운영 절차에 직접 영향.

해제 시 사전점검 없이 결산 Activity가 실행될 수 있어 데이터 준비 미비 상태의 조기 실행 위험.

### 2.3.2 PRE_PID — PAC  ID

**테이블-필드:** ZTPAC_CONFIG - PRE_PID

**운영 설정(LG전자 특화) :** 미사용

#### 설정 설명

사전점검 필수시 PID

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(미완료 메시지 표기), ZCL_PAC_SAIL=>IS_PRECHECK_COMPLETED(CM00K),

ZFPAC_CREATE_BUPAK_JOB/PCSGP_JOB(LZPAC050 U02/U03), ZLPAC0010_F01(CHECK_PRE_PID_110)/I01

#### 프로세스 관점 분석 (사용 로직)

XPRE_USE 활성 시 사전점검으로 지정할 Activity ID.

① ZCL_PAC_SAIL=>IS_PRECHECK_COMPLETED가 이 PID의 ZTPAC_STATUS 상태를 조회하여 완료 여부를 판정.

② ZIPAC_COMMON: 미완료 시 오류 메시지에 ZCL_PAC=>SELECT_PID_TEXT(PRE_PID)로 Activity명을 표기.

③ ZLPAC0010_F01 CHECK_PRE_PID_110: 입력값이 ZTPAC_PROC에 존재하는 유효 PID인지 검증(E121).

#### 영향도 분석 (변경 시 영향)

지정된 PID를 Activity Master에서 삭제/변경하면 사전점검 체크가 항상 미완료로 판정되어 BusPkg 전체 실행이 전면 차단될 위험.

Activity 마스터 변경 시 반드시 함께 점검해야 하는 필드.
