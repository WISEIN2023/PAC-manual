---
id: pac-config/03-03-map-control
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.3 Map Control
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.3 Map Control

### 3.3.1 BTN_NAVI — Active Navigation Button in SAP Gui?

**테이블-필드:** ZTPACSYS - BTN_NAVI

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

□ X 활성화시 : SAP GUI 버전의 PAC 실행화면에서 Nagivation 버튼 활성화

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_NETGRAPH=>SET_TOOLBAR(CM01Y), ZCL_PAC_MTM=>SET_TOOLBAR(CM01V)

#### 프로세스 관점 분석 (사용 로직)

SAP GUI 버전 PAC 실행맵의 Navigation 버튼 활성화.

① ZCL_PAC_NETGRAPH/MTM의 SET_TOOLBAR: 'X'이면 넷그래프 툴바에 Navigation 버튼을 추가 구성.

#### 영향도 분석 (변경 시 영향)

GUI 맵 화면의 툴바 구성만 변경되는 표시 전용 설정 — 실행 로직 영향 없음.

### 3.3.2 RFSHTM — Auto Refresh Time Setting in SAP Gui

**테이블-필드:** ZTPACSYS - RFSHTM

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

SAP GUI 버전의 PAC 실행화면에서 자동 Refresh 타임을 설정(SAP GUI는 자동 Refresh가 되지 않아 주기적으로 Refresh Time 설정이 필요하다)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_MTM=>CONSTRUCTOR(CM007), ZCL_PAC_SAIL=>CONSTRUCTOR(CM00B), ZLPAC0110_F01(Execute PAC By Company)

#### 프로세스 관점 분석 (사용 로직)

SAP GUI 실행화면의 자동 Refresh 주기(초) 설정.

① ZCL_PAC_SAIL/MTM CONSTRUCTOR: AV_RFSHTM = (입력값이 있고 시스템값 이하이면 입력값, 아니면 ZTPACSYS-RFSHTM) — 시스템 설정이 Refresh 주기의 상한으로 동작.

② ZLPAC0110: 회사별 실행 화면의 주기적 상태 갱신 타이머.

#### 영향도 분석 (변경 시 영향)

값을 줄이면 GUI 맵의 상태 갱신이 빨라지는 대신 조회 부하 증가.

0/공백이면 자동 갱신이 사실상 동작하지 않아 사용자가 수동 Refresh 해야 함.

### 3.3.3 LINK_COLOR — Active Link Line Color

**테이블-필드:** ZTPACSYS - LINK_COLOR

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

□ X 활성화시 : Line의 Color 색상을 활성화 (선후행의 상태, 순서에 따라 색상이 변함)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC=>SELECT_LINK(CM017)/SELECT_GPID_LINK(CM014), ZCL_PAC_MTM=>SELECT_LINK_MTM(CM01H)

#### 프로세스 관점 분석 (사용 로직)

맵 링크(Line) 색상 활성화.

① ZCL_PAC=>SELECT_LINK 계열: 링크 조회 시 'X'이면 선·후행 Activity의 상태/순서에 따라 라인 색상 속성을 세팅하여 Map(GUI/Fiori)에 전달.

#### 영향도 분석 (변경 시 영향)

표시 전용 설정 — 색상으로 상태를 판단하던 사용자 경험만 변화, 실행 로직 영향 없음.
