---
id: pac-config/03-20-target-group
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.20 Target Group
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.20 Target Group

### 3.20.1 TARGET_GRP — Target Group

**테이블-필드:** ZTPACSYS - TARGET_GRP

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

Job 생성시 특정 Target Group으로 배치잡을 생성하도록 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CHECK_JOB_BALANCING(LZPAC290U01)

#### 프로세스 관점 분석 (사용 로직)

배치 Job 생성 대상 Server Group.

① ZFPAC_CHECK_JOB_BALANCING: 지정 시 RSBATCH_GET_SERVER_AND_GROUP으로 해당 그룹의 서버 목록을 조회하여 그 서버들의 배치 WP만 유휴율 계산 대상으로 삼음(미지정 시 전체 활성 서버). Job 생성 시 대상 서버 그룹 지정과 연동.

#### 영향도 분석 (변경 시 영향)

서버 그룹명이 Basis에서 변경/삭제되면 유휴율 계산 대상이 없어져 Job 밸런싱이 오동작 — Basis 서버그룹 변경 시 함께 갱신 필수.

PAC 배치를 특정 서버군에 격리하고 싶을 때 사용.
