---
id: pac-config/03-22-world-map
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.22 World Map
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.22 World Map

### 3.22.1 PORTAL_BUPAK — Business Package for Portal World Map

**테이블-필드:** ZTPACSYS - PORTAL_BUPAK

**운영 설정(LG전자 설정) :** FI

#### 설정 설명

PAC Home의 World Map 조회화면에서 어떤 Business Package를 기준으로 조회할지를 정의

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_ZGWPAC_MONITOR_DPC_EXT=>REGION_SELSET_GET_ENTITY(CM00L)

#### 프로세스 관점 분석 (사용 로직)

PAC Home World Map 조회 기준 Business Package.

① OData REGION_SELSET Entity: World Map(지역별 결산 현황)을 어느 BusPkg 기준으로 집계·표시할지 결정하여 Fiori에 전달.

#### 영향도 분석 (변경 시 영향)

변경 시 포털 첫 화면 World Map의 집계 기준이 바뀜 — 표시 전용이나 전사 사용자가 보는 화면이므로 변경 시 공지 권장.
