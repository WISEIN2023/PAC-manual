---
id: pac-config/02-01-oranization-setting
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.1 Oranization Setting
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

Business Package 단위로 관리되는 Config이다. 관리 트랜잭션은 ZLPAC0010(Maintain Business Package Config)이며, 테이블 키는 BUPAK(Business Package)이다. BusPkg별 조직 구조, 자동화 정책, 알람, 권한, 마감 통제 등을 정의한다.

## 2.1 Oranization Setting

### 2.1.1 BUPAK — BusPkg

**테이블-필드:** ZTPAC_CONFIG - BUPAK

#### 설정 설명

적용할 Bus Pkg

#### 참조 프로그램 / 오브젝트 (Where-used)

[전체 PAC 오브젝트 약 180여 개 Include에서 참조 - 테이블 키]

■ 대표: ZCL_PAC=>SELECT_CONFIG / GET_BUPAK_DEFAULT / SELECT_PACLVL, ZIPAC_COMMON(공통 Include),

ZLPAC0010(Config 관리), ZLPAC0011(BusPkg Master), ZLPAC0120(Execute Map), 모든 SAPLZPAC* 펑션그룹

#### 프로세스 관점 분석 (사용 로직)

ZTPAC_CONFIG의 유일한 키 필드로, PAC의 모든 런타임/마스터 프로그램이 「SELECT SINGLE ... FROM ZTPAC_CONFIG WHERE BUPAK = ...」 형태로 Config를 읽는 진입 키.

① ZCL_PAC=>SELECT_CONFIG( IV_BUPAK )가 표준 Config 조회 API로 전 프로세스에서 호출됨.

② ZLPAC0010에서 BusPkg 선택 시 GET_BUPAK_INFO가 해당 키로 Config 전체를 읽어 화면에 표시하고, 저장 시 ENQUEUE_EZ_ZTPAC_CONFIG의 잠금 키로 사용.

③ ZIPAC_COMMON(_PAC_LOG_START)에서 실행 대상 Activity의 BUPAK으로 Config를 읽어 이후 모든 체크(기간/권한/사전점검 등)의 기준이 됨.

#### 영향도 분석 (변경 시 영향)

BusPkg 추가/삭제 시 Config 1건이 반드시 존재해야 하며, 미존재 시 해당 BusPkg의 모든 실행이 기본값(대부분 비활성)으로 동작.

신규 BusPkg 오픈 시 최우선 등록 항목이며, 삭제 시 해당 BusPkg의 모델링·상태·로그 데이터 전체가 고아 데이터가 됨.

### 2.1.2 PACLVL — org Level

**테이블-필드:** ZTPAC_CONFIG - PACLVL

#### 설정 설명

Organization Level을 선택

□ Org Level

C : Company Code

B : Business Area

U : Other Organization

→ Other Organization은 필드명을뿐이며, ZTPAC_CUNIT_C에서 조직 이름을 직접 정의해서 사용한다

#### 참조 프로그램 / 오브젝트 (Where-used)

[약 190여 개 Include에서 참조]

■ 표준 API: ZCL_PAC=>SELECT_PACLVL(CM01C)

■ 핵심: ZIPAC_COMMON(필수 조직 체크), ZLPAC0010_F01(CHECK_PACLVL_CHANGE_ABLE/CHECK_LEVEL),

ZLPAC0050(조직 할당), ZFPAC_*_SEARCH_HELP(SAPLZPAC240), 실행/모니터링 전 화면(TOP Include 화면 제어)

#### 프로세스 관점 분석 (사용 로직)

조직 레벨(C:Company/B:Business Area/U:Closing Unit)을 결정하는 PAC의 최상위 구조 설정.

① 런타임: ZIPAC_COMMON에서 로그 시작 시 PACLVL에 따라 필수 조직 필드를 체크(C→BUKRS 필수 E013, B→GSBER 필수 E014, U→CUNIT 필수 E092). 미입력 시 실행 차단.

② 전 조회/실행 화면(ZLPAC0120, ZLPAC0140, 모니터링, 결산점검 ZLPAC5xxx 등)의 TOP/F01에서 PACLVL에 따라 조직 입력 필드를 동적으로 활성/비활성.

③ ZLPAC0050의 조직 할당 대상 테이블(ZTPAC_CONFIG_COM/BA/UNI) 결정.

④ 결산일정(XSCH_USE) 사용 시 ZTPAC_SCH_CONFIG-SCH_LEVEL과 일치해야만 저장 허용(CHECK_LEVEL).

#### 영향도 분석 (변경 시 영향)

운영 중 변경은 사실상 불가 — ZLPAC0050에서 조직이 이미 할당(ZTPAC_CONFIG_COM/BA/UNI 존재)된 경우 ZLPAC0010이 필드를 잠금(CHECK_PACLVL_CHANGE_ABLE).

변경이 필요하면 조직 할당 선삭제 후 모델링/상태 데이터 정합성 전면 재검증 필요. 실행 필수값 체크 기준이 바뀌므로 전 실행 프로세스에 영향.

### 2.1.3 REQ_BUKRS — Activate Company Code

**테이블-필드:** ZTPAC_CONFIG - REQ_BUKRS

#### 설정 설명

PACLVL 이 B, U인 경우 추가로 법인코드를 활성화 할지를 지정한다

예) PACLVL = B & REQ_BUKRS = 'X' 인 경우 법인코드, BA를 동시에 사용

#### 참조 프로그램 / 오브젝트 (Where-used)

[약 160여 개 Include에서 참조]

■ 핵심: ZIPAC_COMMON(GET_COMMON_ORG/필수체크), ZFPAC_GET_REQBUKRS_NODE/LINK/TREE(SAPLZPAC220),

ZLPAC0018/0019(조직 Master), ZLPAC0050(조직 할당), ZLPAC1000/1011(Participant), 각 실행·모니터링 화면 TOP

#### 프로세스 관점 분석 (사용 로직)

PACLVL이 B/U일 때 법인코드(BUKRS)를 추가 활성화하는 설정.

① ZIPAC_COMMON: 'X'이면 BUKRS 필수 체크가 추가되고, Company 레벨 Activity 실행 시 GET_COMMON_ORG로 Common Org(GSBER/CUNIT)를 자동 결정.

② ZFPAC_GET_REQBUKRS_NODE/LINK/TREE: Fiori Map을 법인코드 기준으로 조회하는 전용 FM 세트가 이 설정으로 동작.

③ 조회·실행·참가자·모니터링 화면 전반에서 법인코드 필드 표시를 제어.

④ ZLPAC0010: PACLVL='C'이면 필드가 숨겨지고 저장 시 강제 클리어. 조직 할당 존재 시 변경 잠금.

#### 영향도 분석 (변경 시 영향)

XCONF_BUKRS(법인별 Confirm Type)의 전제 조건 — 해제 시 함께 무효화됨.

설정 변경 시 실행 필수값(BUKRS)과 Map 조회 기준이 바뀌어 법인 단위 조회/권한/Confirm 로직 전체에 영향. 조직 할당 존재 시 변경 자체가 잠김.

### 2.1.4 MDLVL — Modeling Level

**테이블-필드:** ZTPAC_CONFIG - MDLVL

**운영 설정(LG전자 특화) :** CI, FV, NS 2레벨사용

#### 설정 설명

□ PAC 모델링 레벨을 지정

3 : Activity Group > Activity > Cloisng ID

2:  Activity Group > Cloisng ID

#### 참조 프로그램 / 오브젝트 (Where-used)

[약 36개 Include에서 참조]

■ 표준 API: ZCL_PAC=>SELECT_MDLVL(CM018), ZCL_PAC_MTM=>SELECT_MDLVL(CM01I)

■ 핵심: ZLPAC0020(Activity Master), ZLPAC0140(Modeling List), ZFPAC_GET_GLOBAL_TREE(LZPAC701U03),

ZLPAC0010_F01(CHECK_MDLVL_CHANGE_ABLE), 모니터링 화면 TOP

#### 프로세스 관점 분석 (사용 로직)

모델링 계층(3: Group>Sub Group>Activity, 2: Group>Activity)을 결정.

① ZCL_PAC=>SELECT_MDLVL이 표준 API로, Activity Master(ZLPAC0020)의 입력 컬럼 구성, 모델링 리스트(ZLPAC0140), Fiori 트리 구성(ZFPAC_GET_NODE_FIORI/GLOBAL_TREE)에서 2/3레벨 분기.

② ZLPAC0010_F01 SET_LIST_BOX_FOR_MDLVL: BusPkg별 레벨 명칭으로 리스트박스 구성.

③ XSKIP_MIDDLE 필드는 MDLVL=3일 때만 화면 활성(SCREEN_PBO_0130).

#### 영향도 분석 (변경 시 영향)

운영 중 변경 불가 항목 — ZTPAC_PROC에 노드가 등록되면 ZLPAC0010이 잠금(CHECK_MDLVL_CHANGE_ABLE).

변경 시 모델링 구조 전체(트리/맵/모니터링 집계 레벨)가 바뀌므로 모델링 데이터 재구축이 전제됨.

### 2.1.5 PERTYPE — Period Type

**테이블-필드:** ZTPAC_CONFIG - PERTYPE

**운영 설정(LG전자 특화) :** 모두 P로 사용

#### 설정 설명

□ Period 유형설정으로 지정된 유형에 따라 기간이 활성화 된다

Y : Fiscal Year

P : Period(Fiscal Year + Month)

N : Not Use

#### 참조 프로그램 / 오브젝트 (Where-used)

[약 30개 Include에서 참조]

■ 핵심: ZIPAC_COMMON(기간 필수 체크), ZCL_PAC_ORG=>CHECK_VALID_PERIOD(CM004)/CHECK_ORG_OPEN(CM002),

ZFPAC_GET_VARIANT(LZPAC100U01), ZLPAC0120/0160/2100/5200/5300, 모니터링 화면 TOP

#### 프로세스 관점 분석 (사용 로직)

기간 유형(Y:회계연도/P:기간/N:없음)에 따라 기간 필드 활성화와 필수 여부를 제어.

① ZIPAC_COMMON: 로그 시작 시 'P'면 GJAHR+MONAT 필수, 'Y'면 GJAHR만 필수(E092). 미충족 시 실행 차단.

② ZCL_PAC_ORG=>CHECK_VALID_PERIOD: ZFPAC_NEXT_AUTO_START, ZFPAC_CONFIRM_ITEM 등 모든 실행성 FM 진입부의 기간 유효성 검증.

③ 실행맵/로그조회/모니터링/결산점검 화면의 연·월 입력 필드 표시 제어.

④ ZFPAC_GET_VARIANT: Variant 파라미터 치환 시 기간 유형에 따라 연/월 값 매핑.

#### 영향도 분석 (변경 시 영향)

상태테이블(ZTPAC_STATUS)의 기간 키 사용 방식과 직결 — 운영 중 변경 시 기존 상태/로그 데이터와 기간 단위 불일치 발생.

월 결산 운영 중 변경 금지. 변경 시 Variant 기간 매핑(ZFPAC_GET_VARIANT)도 함께 재검증 필요.

### 2.1.6 GPID — Global Package ID

**테이블-필드:** ZTPAC_GPID - GPID

#### 설정 설명

□ Business Package를 엮어 Global Package로 수행되는 경우 조회된다

□ Global Package ID 관리 : ZLPAC8011 - Assign Global Pkg to Modeling ID 에 등록된다

- Main Package : Global Package의 엮인 Business Package의 중심 Package로 ZTPAC_GPID-MAIN = X 인 경우

- Sub Package : Global Package에 엮인 Business Package 중 Main이 아닌 경우

#### 참조 프로그램 / 오브젝트 (Where-used)

[ZTPAC_GPID 테이블 - 별도 저장]

■ 핵심: ZFPAC_GET_GLOBAL_NODE/LINK/TREE(SAPLZPAC701), ZFPAC_CREATE_GPID_JOB(LZPAC050 U08),

ZCL_PAC=>SELECT_GPID_NODE(CM015)/SELECT_GPID_LINK(CM014)/SYNC_GPID_STATUS(CM01S),

ZLPAC0010_F01(CHECK_MAIN_PACKAGE), ZLPAC0031/0041(Global Map), ZLPAC_MONITOR_GPID

#### 프로세스 관점 분석 (사용 로직)

복수 BusPkg를 하나의 Global Package로 묶어 수행하는 경우의 그룹 ID(ZTPAC_GPID에 저장, Config 화면에서 조회/입력).

① ZFPAC_NEXT_AUTO_START/CHECK_CAN_ALWAYAS_START: GPID 존재 시 자동수행이 ZFPAC_CREATE_GPID_JOB(Global 단위 Job)으로 분기.

② SAPLZPAC701: Global Map의 노드/링크/트리 조회. ZCL_PAC=>SYNC_GPID_STATUS로 BusPkg 상태를 Global 상태로 집계.

③ ZLPAC0010_F01 CHECK_MAIN_PACKAGE: 동일 GPID 내 MAIN='X' 패키지에서만 GPID 편집 가능.

#### 영향도 분석 (변경 시 영향)

GPID 연결/해제 시 자동수행 Job 생성 단위(BusPkg↔Global)가 바뀌고, Global Map 모델링(ZLPAC0031/0041)과 Global 모니터링(ZLPAC_MONITOR_GPID)의 집계 대상이 변경됨.

Main Package 지정과 함께 관리해야 하며, 해제 시 Global 단위 상태 동기화가 중단됨.
