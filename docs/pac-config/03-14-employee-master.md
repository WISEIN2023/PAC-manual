---
id: pac-config/03-14-employee-master
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.14 Employee Master
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.14 Employee Master

### 3.14.1 DISUSER — Active Employee Master

**테이블-필드:** ZTPACSYS - DISUSER

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : 별도 CBO 사원마스터를 활성화 한다 (비활성화시 STD User ID의 정보를 활용)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_ORG=>ON_GET_USERINFO(CM00I) + 유저 관련 전 화면 약 30개 Include(USRID_S 화면군 + LZPAC044, LZPACCIS0014)

#### 프로세스 관점 분석 (사용 로직)

별도 CBO 사원마스터 활성화 여부.

① ZCL_PAC_ORG=>ON_GET_USERINFO: 유저 정보 조회의 단일 창구로, 'X'이면 CBO 사원마스터에서, 공백이면 SAP 표준 User(USR21/ADRP 계열)에서 이름·사번·메일을 조회.

② Participant, 알람 수신자, CIS Reviewer, Skip 권한 등 유저 정보를 다루는 모든 화면이 이 설정에 따라 조회 소스를 전환.

#### 영향도 분석 (변경 시 영향)

조회 소스 전환 설정이므로 변경 시 기존 등록 데이터의 사번/ID 매핑 정합성을 전수 점검해야 함 — 매핑 불일치 시 담당자 이름/메일이 표시되지 않거나 알람 수신자 결정 실패.

CBO 사원마스터 I/F 중단 시 유저 정보 표시 전반 장애로 파급.
