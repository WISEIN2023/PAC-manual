---
id: pac-config/03-24-calendar
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.24 Calendar
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.24 Calendar

### 3.24.1 PORTAL_CBUKRS — Active portal calendar company code

**테이블-필드:** ZTPACSYS - PORTAL_CBUKRS

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

PAC Home의 Calendar 화면에서 법인코드 사용을 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_ZGWPAC_MONITOR_DPC_EXT=>CALENDAR_ORGSET_GET_ENTITY(CM003)

#### 프로세스 관점 분석 (사용 로직)

PAC Home Calendar 화면의 법인코드 사용 활성화.

① OData CALENDAR_ORGSET Entity: Calendar 조회 시 법인코드 선택 필드 활성화 여부 전달.

#### 영향도 분석 (변경 시 영향)

해제 시 포털 Calendar에서 법인 단위 일정 조회 불가 — 법인별 일정을 운영하는 경우 필수 유지.
