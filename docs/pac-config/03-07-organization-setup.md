---
id: pac-config/03-07-organization-setup
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.7 Organization Setup
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.7 Organization Setup

### 3.7.1 XCOMGRP — Active Company Group

**테이블-필드:** ZTPACSYS - XCOMGRP

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

□ X 활성화시 : Company 마스터에서 Company Group을 활성화 한다

□ Company Group : Company 별

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC0018_F01(Company Master), ZLPAC0050_F01(조직 할당), ZLPAC_MONITOR_ACT/BUPAK_F01(모니터링),

ZCL_ZGWPAC_MONITOR_DPC_EXT=>COMPANY_GRPSET_GET_ENTITYSET(CM005)

#### 프로세스 관점 분석 (사용 로직)

Company Group 활성화.

① ZLPAC0018: Company 마스터에 Company Group 필드 표시/입력 활성화(그룹 마스터는 ZLPAC0093).

② 모니터링(ZLPAC_MONITOR_*)과 Fiori 모니터 OData(COMPANY_GRPSET)에서 Company Group 단위 필터/집계 제공.

③ ZLPAC0050: 조직 할당 화면에서 그룹 기준 선택 지원.

#### 영향도 분석 (변경 시 영향)

해제 시 모니터링/조직 할당에서 그룹 단위 필터가 사라짐 — 그룹 기준으로 운영하던 조회 화면 사용 방식 변경.

기존 그룹 마스터 데이터(ZLPAC0093)는 유지되나 활용 불가 상태가 됨.

### 3.7.2 XBA_GROUP — Active Business Area Group

**테이블-필드:** ZTPACSYS - XBA_GROUP

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

□ X 활성화시 : Business Area Group을 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC1000_F01, ZLPAC1011_F01/F02/ALV(Participant/권한 관리)

#### 프로세스 관점 분석 (사용 로직)

Business Area Group 활성화.

① Participant·권한 관리 화면에서 Business Area Group 필드를 표시/입력 활성화하여 BA 그룹 단위 담당자 지정 지원.

#### 영향도 분석 (변경 시 영향)

해제 시 BA 그룹 단위 담당자 지정 입력이 불가해짐 — 기존 그룹 단위 등록 데이터는 유지되지만 신규/수정 관리 불가.

### 3.7.3 COMBUSTY — Enable To Change Business Type When Company Code Assign

**테이블-필드:** ZTPACSYS - COMBUSTY

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

□ X 활성화시 : 동일한 Company Code라도 BusPkg 할당시에 다른 Business Type으로 변경할 수 있도록 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC0018_F01(Company Master), ZLPAC0050_F01(조직 할당)

#### 프로세스 관점 분석 (사용 로직)

Company Code 할당 시 Business Type 변경 허용.

① ZLPAC0050: 동일 Company라도 BusPkg 할당 시 다른 Business Type 지정이 가능하도록 입력 필드 활성화. ZLPAC0018 Company 마스터에서도 동일 제어.

#### 영향도 분석 (변경 시 영향)

해제 시 BusPkg별로 다른 Business Type을 줄 수 없어 Company 마스터의 기본 Business Type이 일괄 적용됨 — Business Type 기반 분기(특화 로직)를 쓰는 조직 구성에 영향.

### 3.7.4 BABUSTY — Enable To Change Business Type When Business Area Assign

**테이블-필드:** ZTPACSYS - BABUSTY

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

□ X 활성화시 : 동일한 Business Area라도 BusPkg 할당시에 다른 Business Type으로 변경할 수 있도록 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC0019_F01(Business Area Master), ZLPAC0050_F01(조직 할당)

#### 프로세스 관점 분석 (사용 로직)

Business Area 할당 시 Business Type 변경 허용.

① COMBUSTY와 동일 로직의 BA 버전.

#### 영향도 분석 (변경 시 영향)

COMBUSTY와 동일 — BA 단위 Business Type 차등 지정 가능 여부가 바뀜.
