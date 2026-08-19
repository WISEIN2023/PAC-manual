---
id: pac-config/02-07-logging
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.7 Logging
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.7 Logging

### 2.7.1 LOGDUPDEL — Delete Duplicated Log

**테이블-필드:** ZTPAC_CONFIG - LOGDUPDEL

**운영 설정(LG전자 특화) :** 운영은 모두 설정

#### 설정 설명

- Log 중복 삭제 여부 정의

- 설정시 : ZTPAC_LOG_DTL에 쌓이는 로그에 대해 Message Class, Number, Parameter 1 ~ 4 의 값이 모두 같은 경우는 테이블 저장을 하지 않는다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_LOG=>WRITE_LOG_DETAIL(CM00M), ZIPAC_COMMON(포그라운드 로그 dedup)

#### 프로세스 관점 분석 (사용 로직)

로그 중복 기록 방지 여부.

① ZCL_PAC_LOG=>WRITE_LOG_DETAIL: 'X'이면 ZTPAC_LOG_DTL에 동일 LOGID+MSGID+MSGNR+PARAM1~4 조합이 이미 존재하면 기록 skip.

② ZIPAC_COMMON: 포그라운드 로그(GT_FORE_LOG)도 동일 기준으로 중복 메시지 제거.

#### 영향도 분석 (변경 시 영향)

해제 시 반복 오류 상황에서 동일 메시지가 무제한 기록되어 로그 폭증 → LOGMXCNT 한도 조기 도달, 로그 조회 성능 저하 및 DB 용량 증가.

활성 시에는 중복 메시지의 발생 횟수 정보가 남지 않는 트레이드오프 존재.

### 2.7.2 XLOG_AUTH — Authorization check when log start?

**테이블-필드:** ZTPAC_CONFIG - XLOG_AUTH

**운영 설정(LG전자 특화) :** Subsidiary Closing만 활성화

#### 설정 설명

□ X설정 : 로그 시작시 모듈권한 체킹여부

- PAC로그가 심어진 경우 '_PAC_LOG_START' 수행시에 권한을 체킹하고 문제 없는 경우만 진행이 가능하다

- ZCL_PAC_AUTH=>CHECK_ORG_AUTH을 통해 권한을 점검

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(_PAC_LOG_START 권한 체크), ZCL_PAC_AUTH=>CHECK_ORG_AUTH(CM006)/CHECK_AUTH_WHEN_LOG_START(CM004)

#### 프로세스 관점 분석 (사용 로직)

PAC 로그 시작 시 모듈(조직) 권한 체크 여부.

① ZIPAC_COMMON: 'X'이면 로그 시작 시점에 ZCL_PAC_AUTH=>CHECK_ORG_AUTH(BUPAK/BUKRS/GSBER/CUNIT, ACTVT='01')를 호출하여 실행 권한을 검증, 오류(E) 시 실행 차단.

② PAC 로그가 심어진 프로그램('_PAC_LOG_START' 매크로 사용 프로그램) 전체가 대상.

#### 영향도 분석 (변경 시 영향)

활성화 시 권한 미비 유저의 실행이 로그 시작 단계에서 차단됨 — 활성 전환 시 전 수행 인원의 조직 권한 등록 상태 사전 점검 필수.

해제 시 조직 권한 없는 유저도 Activity 실행 가능해져 통제 약화.
