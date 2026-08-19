---
id: pac-config/03-10-logging
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.10 Logging
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.10 Logging

### 3.10.1 USERTYPE — User Output Type

**테이블-필드:** ZTPACSYS - USERTYPE

**운영 설정(LG전자 설정) :** N : User Name

#### 설정 설명

□ Log 조회화면에서 수행유저의 표시방법을 설정

U : User ID

E : Employee Number

N : User Name

M : Mail ID

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_LOG=>GET_USER_OUPUT_TYPE(CM00F)

#### 프로세스 관점 분석 (사용 로직)

로그 조회 화면의 수행 유저 표시 방법(U:User ID/E:사번/N:이름/M:메일 ID).

① GET_USER_OUPUT_TYPE: 로그 표시 시 USERTYPE에 따라 User ID 그대로(U/공백), 사원마스터 조회 후 사번(E)·영문명(N)·메일 ID 앞부분(M)으로 변환하여 출력. 변환 실패 시 User ID로 폴백.

#### 영향도 분석 (변경 시 영향)

표시 전용 설정 — E/N/M 유형은 사원마스터(DISUSER 구성) 조회가 수반되므로 로그 조회 성능에 소폭 영향.

사원정보 미매핑 유저는 User ID로 표시됨.

### 3.10.2 LOGMXCNT — Number of logs can be created

**테이블-필드:** ZTPACSYS - LOGMXCNT

**운영 설정(LG전자 설정) :** 49999

#### 설정 설명

Log ID 당 생성할 수 있는 최대 로그 수를 제한 (장애 발생시를 대비)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_LOG=>WRITE_LOG_DETAIL(CM00M)

#### 프로세스 관점 분석 (사용 로직)

Log ID당 생성 가능한 최대 로그 건수(장애 시 로그 폭주 대비).

① WRITE_LOG_DETAIL: 로그 건수가 LOGMXCNT 초과 시 실제 메시지 대신 「Message Overflow」(ZPAC01-415, PARAM1=한도값) 1건만 기록하고 이후 기록 중단 → ZTPAC_LOG_DTL 폭주 방지.

#### 영향도 분석 (변경 시 영향)

값이 작으면 정상적인 대량 로그도 잘려 원인 분석 정보가 유실됨.

0/공백이면 한도 체크가 동작하지 않아 장애 시 로그 테이블 폭증(DB 용량/성능) 위험.
