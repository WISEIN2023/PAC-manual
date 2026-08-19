---
id: pac-config/03-01-data-editable-setting
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.1 Data Editable Setting
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

시스템(클라이언트) 전역으로 1건 관리되는 Config이다. 관리 트랜잭션은 ZLPACSYS(Maintain Business Package Config - System)이며, 화면 표시 정책, 유저 정보 소스, 특수 권한 체계, 배치 부하 제어, 포털(PAC Home) 구성 등을 정의한다.

## 3.1 Data Editable Setting

### 3.1.1 HTML_EDIT — HTML Manager

**테이블-필드:** ZTPACSYS - HTML_EDIT

**운영 설정(LG전자 설정) :** 개발만 설정

#### 설정 설명

□ X 활성화시 : HTML Editor(ZLPAC_HTML)에서 수정가능하도록 한다 (운영은 되도록 조회모드로 설정)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC_HTML_F01(HTML Editor), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

HTML Manager(ZLPAC_HTML)에서 HTML 템플릿(메일 양식 등) 수정 가능 여부.

① ZLPAC_HTML_F01: 'X'일 때만 편집 모드 진입 허용 → 운영기는 해제하여 직접 수정을 막고 CTS로만 반영하도록 통제.

#### 영향도 분석 (변경 시 영향)

운영기에서 활성화하면 이관 절차 없이 메일 양식 등이 직접 수정될 수 있어 형상관리 통제가 깨짐 — 운영기는 해제 유지 권장.

### 3.1.2 HTML_CTS — Active HTML CTS

**테이블-필드:** ZTPACSYS - HTML_CTS

**운영 설정(LG전자 설정) :** 개발만 설정

#### 설정 설명

□ X 활성화시 : HTML Editor(ZLPAC_HTML)에서 CTS하도록 활성화 (개발에서 설정)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPACSYS_F01(관리 화면), HTML 저장 로직에서 플래그 조건으로 동작

#### 프로세스 관점 분석 (사용 로직)

HTML Editor에서 CTS(Transport) 연결 활성화.

① 'X'이면 ZLPAC_HTML에서 HTML 콘텐츠 저장 시 트랜스포트 요청에 담아 이관 가능(개발기에서 설정).

#### 영향도 분석 (변경 시 영향)

개발기 전용 설정 — 운영기에서 활성화할 이유가 없으며, 개발기에서 해제 시 HTML 수정분이 CTS에 담기지 않아 이관 누락 발생.

### 3.1.3 ALV_EDIT — ALV Manager

**테이블-필드:** ZTPACSYS - ALV_EDIT

**운영 설정(LG전자 설정) :** 개발만 설정

#### 설정 설명

□ X 활성화시 : ALV Manager(ZLPAC_ALV)에서 수정가능하도록 한다 (운영은 되도록 조회모드로 설정)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC_ALV_F01(ALV Manager), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

ALV Manager(ZLPAC_ALV)에서 ALV 레이아웃 정의 수정 가능 여부.

① ZLPAC_ALV_F01: 'X'일 때만 편집 허용. 운영기는 조회 전용으로 통제.

#### 영향도 분석 (변경 시 영향)

HTML_EDIT과 동일 — 운영기 활성화 시 화면 레이아웃 정의가 무통제 수정될 수 있음. 운영기는 해제 유지 권장.

### 3.1.4 ALV_CTS — Active ALV CTS

**테이블-필드:** ZTPACSYS - ALV_CTS

**운영 설정(LG전자 설정) :** 개발만 설정

#### 설정 설명

□ X 활성화시 : ALV Manager(ZLPAC_ALV)에서 CTS하도록 활성화 (개발에서 설정)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC_ALV_F01, ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

ALV Manager에서 CTS(Transport) 활성화.

① 'X'이면 ZLPAC_ALV에서 레이아웃 저장 시 트랜스포트 연결(개발기 설정).

#### 영향도 분석 (변경 시 영향)

HTML_CTS와 동일 — 개발기 전용. 해제 시 레이아웃 수정분 이관 누락.
