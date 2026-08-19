---
id: pac-config/03-12-auto-refresh
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.12 Auto Refresh
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.12 Auto Refresh

### 3.12.1 REFRESH_TIME — Closing Insepction Refresh Duration

**테이블-필드:** ZTPACSYS - REFRESH_TIME

**운영 설정(LG전자 설정) :** 10

#### 설정 설명

□ 결산점검에서 자동 Refresh의 수행 단위(초)를 입력

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC5100_F01, ZLPAC5200_F01, ZLPAC5300_F01(결산점검 화면)

#### 프로세스 관점 분석 (사용 로직)

결산점검(Closing Inspection) 화면의 자동 Refresh 주기(초).

① 결산점검 진행 현황 화면들이 이 주기로 상태를 자동 재조회 — 시나리오 배치 진행 상황 모니터링용.

#### 영향도 분석 (변경 시 영향)

주기를 줄이면 갱신은 빨라지나 다수 사용자가 동시 조회 시 시스템 부하 증가.

공백이면 자동 갱신 없음.

### 3.12.2 REFRESH_MIN — Monitoring Refresh Duration

**테이블-필드:** ZTPACSYS - REFRESH_MIN

**운영 설정(LG전자 설정) :** 10

#### 설정 설명

PAC 모니터링에서 'Auto Refresh'가 활성화 된 경우 Refresh 주기(분)를 입력(Default)

- 모니터링 화면에서 수정 가능하다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC_MONITOR_ACT/BUPAK/GPID_F01(PAC 모니터링)

#### 프로세스 관점 분석 (사용 로직)

PAC 모니터링 화면의 Auto Refresh 주기(분).

① 모니터링 프로그램에서 'Auto Refresh' 활성화 시 이 주기로 재조회(Default 1분).

#### 영향도 분석 (변경 시 영향)

주기 축소 시 조회 부하 증가. 모니터링 사용 인원수와 함께 검토.

### 3.12.3 REFRESH_MAX — Monitoring Max Running Time

**테이블-필드:** ZTPACSYS - REFRESH_MAX

**운영 설정(LG전자 설정) :** 60

#### 설정 설명

PAC 모니터링에서 'Auto Refresh'를 활성화 한 경우 최대 수행되는 시간(분)을 입력

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC_MONITOR_ACT/BUPAK/GPID_F01(PAC 모니터링)

#### 프로세스 관점 분석 (사용 로직)

PAC 모니터링 Auto Refresh의 최대 수행 시간(분).

① Auto Refresh가 이 시간을 초과하면 자동 중단 — 무한 세션 점유 방지.

#### 영향도 분석 (변경 시 영향)

값을 키우면 방치된 모니터링 세션이 장시간 주기 조회를 지속하여 불필요한 부하 발생.

너무 작으면 정상 모니터링 중 자동 중단이 잦아짐.

### 3.12.4 XREFRESH_FIORI — Active Auto Refresh on Portal?

**테이블-필드:** ZTPACSYS - XREFRESH_FIORI

**운영 설정(LG전자 설정) :** 활성화

#### 설정 설명

X 활성화시 : PAC Home에서 World Map View의 자동 Refresh를 가능하게 한다

- World Map View의 Refresh 버튼에서 마우스 우클릭시 'Auto Refresh' On/Off 가능

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_ZGWPAC_MONITOR_DPC_EXT=>PORTAL_REFRESHSE_GET_ENTITY(CM00I)

#### 프로세스 관점 분석 (사용 로직)

PAC Home(Portal) World Map View의 자동 Refresh 허용 여부.

① OData PORTAL_REFRESHSE Entity로 Fiori 앱에 전달되어 World Map 화면의 자동 갱신 기능 on/off.

#### 영향도 분석 (변경 시 영향)

활성 시 포털 접속자 수만큼 주기적 OData 호출이 발생 — 접속자가 많은 결산기에는 백엔드 부하 요소.

해제 시 수동 Reload로만 갱신.

### 3.12.5 FREFRESH_MIN — Refresh Duration

**테이블-필드:** ZTPACSYS - FREFRESH_MIN

**운영 설정(LG전자 설정) :** 10

#### 설정 설명

World Map View의 자동 Refresh 활성화시 Refresh 주기(분)를 입력

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_ZGWPAC_MONITOR_DPC_EXT=>PORTAL_REFRESHSE_GET_ENTITY(CM00I)

#### 프로세스 관점 분석 (사용 로직)

World Map View 자동 Refresh 주기(분).

① XREFRESH_FIORI 활성 시 Fiori World Map의 갱신 주기로 전달.

#### 영향도 분석 (변경 시 영향)

주기 축소 시 포털발 OData 호출 빈도 증가 — XREFRESH_FIORI와 세트로 부하 관점 관리.
