---
id: authorization/14-burok-peurogeuraem-teibeul-keulraeseu-sap
doc: authorization
title: 12. 부록 — 프로그램·테이블·클래스 (SAP 검증 결과)
parent: docs/authorization/README.md
---

# 12. 부록 — 프로그램·테이블·클래스 (SAP 검증 결과)

본문에 등장한 객체를 SAP ADT(MCP)로 조회한 결과입니다. «상태»가 검증완료인 항목은 현재 연결 시스템에 실재함을 확인했습니다.

## 12.1 프로그램 / 트랜잭션

| 객체 | 설명(SAP 등록명) | 상태 |
|---|---|---|
| ZLPAC0010 | Maintain Business Package Config | ✔ 검증완료 |
| ZLPAC0080 | Define Confirm(Skip) Enable Activity By Organization | ✔ 검증완료 |
| ZLPAC0160 | Display Log History (실행/기표 유저 조회) | ✔ 검증완료 |
| ZLPAC1000 | Maintain Closing Activity Participants | ✔ 검증완료 |
| ZLPAC1011 | Excel Upload For Closing Activity Participants | ✔ 검증완료 |
| ZLPAC1030 | Define Authorization Group | ✔ 검증완료 |
| ZLPAC1050 | Maintain Special Role | ✔ 검증완료 |
| ZLPAC5080 | Maintain Closing Inspection Reviewer | ✔ 검증완료 |
| ZLPAC7160 | Super User Registration (Posting) | ✔ 검증완료 |
| ZLPACSYS | PAC System Setting | ✔ 검증완료 |
| ZLPACEXIT | Maintain PAC User Exit (프로그램+트랜잭션) | ✔ 검증완료 |
| ZPCMR1405 | GSOD 표시 설정 (LG) | 미확인(별도 시스템 추정) |
| ZPCMR0030 | Common Code Management (LG) | 미확인(별도 시스템 추정) |
| ZPCMR1409 | 신규 Role 권한신청 등록 (LG) | 미확인(별도 시스템 추정) |

## 12.2 테이블

| 테이블 | 설명 | 상태 |
|---|---|---|
| ZTPAC_SUPER_CONF | Activity Manual Confirm Exception (ZLPAC0080 저장) | ✔ 검증완료 |
| ZTPAC_SPAUTH | Special Role 사용자 등록 (코드 참조) | 코드 인용 |
| ZTPACSYS | Special Auth 검사방식 설정 (코드 참조) | 코드 인용 |
| ZTPAC_PROC_AUTH | 수행/Controller/Participant 권한 (코드 참조) | 코드 인용 |
| ZTPAC_AUTH_ROLE | Auth Group ↔ Role/Object 매핑 (코드 참조) | 코드 인용 |
| ZTPAC_LOG_HDR | Log Header (EXNAM 실행/PSNAM 기표 유저) | ✔ 검증완료 |
| ZTPAC_LOG_DTL | Log Detail | ✔ 검증완료 |
| ZTPAC_CONFIG | BUPAK Config (USER_TYPE A/R/F·POST_USER) | ✔ 검증완료 |
| ZTPACEXIT | PAC User Exit Program (Exit 함수 등록 저장) | ✔ 검증완료 |
| ZTPAC_USERINFO | PAC User Default Information — 개인 기본값(사원마스터 아님, 7.5 주의박스) | ✔ 검증완료 |
| ZSPAC_USER_INFO | Customer Specific INFO — 사원정보 반환 구조 | ✔ 검증완료 |
| ZPCMT0060 | Common Code Master (LG) | 미확인(별도) |
| ZPCMT0063 | LG전자 사원마스터 테이블 | 미확인(고객사 시스템) |
| ZCOAT1004 | LXI 사원마스터 테이블 | 미확인(고객사 시스템) |

## 12.3 클래스 / 함수 / OData

| 객체 | 설명 | 상태 |
|---|---|---|
| ZCL_PAC | Process Automatic Channel Main | ✔ 검증완료 |
| ZCL_PAC_AUTH | Authorization Class (26개 메서드) | ✔ 검증완료(소스확인) |
| ZCL_PAC=>CHECK_MANUAL_ENABLE | Manual Skip 권한 체크 | 엑셀 인용 |
| ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH | Special Role 권한 체크 | ✔ 코드확인 |
| ZFPAC_CREATE_PID_JOB | Create Job by PID (실행유저 EXNAM 결정) | ✔ 검증완료(소스확인) |
| ZFPAC_USER_AUTH | 기표유저(EV_POST_USER) A/R/F 결정 | ✔ 검증완료(소스확인) |
| ZCL_PAC_SAIL=>SAIL_PROCESS_ID | PID Batch Job 실행·유저 전달 | ✔ 검증완료(소스확인) |
| ZCL_PAC_ORG=>ON_GET_USERINFO | 사용자 정보 조회 — Exit(사원마스터)/SU01 분기 | ✔ 검증완료(소스확인) |
| ZFPAC_EMP_INFO_SH_EXIT | [PAC] Employee Info Search help Exit (그룹 ZPAC241) | ✔ 검증완료(소스확인) |
| ZFPAC_USRID_INFO_SH_EXIT | [PAC] Employee Info Search help Exit (그룹 ZPAC241) | ✔ 검증완료(소스확인) |
| ZCL_ZGWPAC_MAIN_DPC_EXT | 참여자 관련 OData (DPC) | 엑셀 인용 |
| ZGWPAC_MONITOR | 대시보드 OData(PortalLink 등) | 엑셀 인용 |
| ZFCL_CWF_ROLE_CHECK | CWF Role 점검 함수 (LG 제공) | 미확인(별도) |
| ZPCM_SAVE_CWF_ROLE | 유관담당자 CWF 권한 체크 함수 (LG) | 미확인(별도) |

**📌 미확인 객체 안내** «미확인»은 현재 MCP가 연결된 SAP 시스템에서 조회되지 않은 객체로, 대부분 ZPCM/ZFCL 등 LG 별도 네임스페이스입니다. 존재하지 않는다는 뜻이 아니라, 운영 시스템에서 별도 확인이 필요하다는 의미입니다.

## 12.4 ZCL_PAC_AUTH 권한 체크 메서드 상세 (용도·호출관계)

4.3 표의 9개 메서드가 «실제로 무엇을 검사하고, 클래스 내부에서 서로 어떻게 호출되는지»를 **ZCL_PAC_AUTH 소스(ADT) 직접 확인** 기준으로 정리한 것입니다. 아래 «호출관계»는 클래스 내부 기준으로 확정된 내용이며, 외부 프로그램·화면·Fiori에서의 호출부는 필요 시 SE80 where-used로 별도 확인하세요.

**✔ SAP 검증 완료:** ZCL_PAC_AUTH 소스 확인. 아래 3계층 구조(부품 → 조합 → 진입점)와 내부 호출관계는 코드에서 검증됨.

### ① 기반(부품) 메서드 — 다른 메서드들이 갖다 쓰는 최종 실행부

| 메서드 | 실제 동작 (코드 검증) | 호출관계 · 성격 |
|---|---|---|
| CHECK_AUTH_BY_AUTHGROUP | ZTPAC_AUTH_ROLE에서 해당 Auth Group의 Role/Object 목록을 읽어 ①AGR_USERS로 Role 보유(유효기간 포함) ②AUTHORITY-CHECK로 Object 보유 ③ZPAC_BUPAK Object(*=ALL 포함)를 순차 검사 | CHECK_AUTH_BY_PID·CHECK_SPECIAL_AUTH가 호출. 대부분 권한 체크의 최종 실행부(부품) |
| CHECK_SPECIAL_AUTH | ZTPACSYS 설정(A/T/H별 S/O/A)을 읽어 S=ZTPAC_SPAUTH 조회, O=CHECK_AUTH_BY_AUTHGROUP 호출, A=둘 중 하나. → 4.4절 S/O/A 표가 곧 이 로직 | CHECK_AUTH_HQ·CHECK_BUPAK_AUTH·GET_AUTH_BUPAK_BY_USER가 호출. Admin/TF 특권 판정 공통 관문 |
| CHECK_TCODE_AUTH | AUTHORITY-CHECK OBJECT 'S_TCODE' ID 'TCD' FIELD Tcode 단 한 줄(표준 Tcode 권한) | 클래스 내부 미사용 → S_TCODE 직접 체크용 공개 유틸리티 |

### ② 조직 · HQ 체크 메서드

| 메서드 | 실제 동작 (코드 검증) | 호출관계 · 성격 |
|---|---|---|
| CHECK_ORG_AUTH | 입력된 조직값에 따라 ON_CHECK_BUKRS_AUTH_EXIT(회사코드)/ON_CHECK_GSBER_AUTH_EXIT(사업영역)/ON_CHECK_CUNIT_AUTH_EXIT(기타조직)를 순차 호출, 하나라도 'E'면 중단 | GET_AUTH_BUKRS/CUNIT/GSBER/REGGRP_LIST가 호출. «권한 있는 조직 목록» 계열의 핵심 필터 |
| CHECK_AUTH_HQ | CHECK_SPECIAL_AUTH('T'=Global) 먼저, 없으면 CHECK_SPECIAL_AUTH('A'=System Admin). 즉 HQ 판정 = Global 또는 Admin 특권 보유 | GET_AUTH_COMGRP_LIST가 호출. (CHECK_SCROFF_EXP의 호출부는 현재 주석 처리) |
| GET_AUTH_BUKRS_LIST | PAC 레벨(C/B/U)에 맞는 config(ZTPAC_CONFIG_COM/BA/UNI)에서 회사코드 후보를 뽑고, 각 건에 CHECK_ORG_AUTH(PAC 권한만)를 돌려 'E'인 것을 제거 후 반환 | 내부 미사용 → 화면/F4/OData에 «선택 가능한 회사코드»를 채워주는 공개 조회 진입점 |

### ③ 최상위 진입점 메서드 — 실제 처리 직전의 관문

| 메서드 | 실제 동작 (코드 검증) | 호출관계 · 성격 |
|---|---|---|
| CHECK_AUTH_BY_PID | ①FM ZFPAC_USER_AUTH로 PAC 수행권한 확인→없으면 EV_SUBRC=1 ②PID Level이면 FM ZFPAC_STD_AUTH로 Tcode 권한→없으면 =2 ③HQ 권한자가 아니면 ZTPAC_PROC의 Auth Group을 찾아 CHECK_AUTH_BY_AUTHGROUP→없으면 =3 | 내부 미사용 → 프로세스 실행 직전 최상위 게이트. EV_SUBRC(1/2/3)로 막힌 단계 구분 |
| CHECK_BUPAK_AUTH | Admin/TF면 통과. 아니면 ZTPAC_BUPAK+AUTH_GROUP+AUTH_ROLE JOIN으로 Role/Object를 얻어 AGR_USERS(Role) 또는 AUTHORITY-CHECK ID 'ZBUPAK'(Object) 검사. 결과를 ES_RETURN(BAPIRET2)로 반환 | 내부 미사용 → Business Package 변경/저장 시 공개 진입점 |
| CHECK_CONTROLLER_AUTH | ZTPAC_CONFIG의 PACLVL(C/B/U)에 따라 ZTPAC_PROC_AUTH(USRID·조직·PID=SPACE·CORG=SPACE)를 조회해 담당(Controller) 여부 판정. REQ_BUKRS 유무로 조직 조합 분기 | 내부 미사용 → GET_CONTROLLER_AUTH_LIST와 짝을 이루는 공개 판정 메서드 |

### 내부 호출관계 요약 (소스 확정)

CHECK_AUTH_BY_PID    -> CHECK_AUTH_BY_AUTHGROUP   (+FM ZFPAC_USER_AUTH, ZFPAC_STD_AUTH) CHECK_AUTH_HQ        -> CHECK_SPECIAL_AUTH(T->A)  -> CHECK_AUTH_BY_AUTHGROUP CHECK_BUPAK_AUTH     -> CHECK_SPECIAL_AUTH(A->T) CHECK_SPECIAL_AUTH   -> CHECK_AUTH_BY_AUTHGROUP CHECK_ORG_AUTH       -> ON_CHECK_BUKRS/GSBER/CUNIT_AUTH_EXIT GET_AUTH_BUKRS_LIST  -> CHECK_ORG_AUTH  [내부호출 없는 공개 진입점]   CHECK_AUTH_BY_PID · CHECK_BUPAK_AUTH · CHECK_CONTROLLER_AUTH · CHECK_TCODE_AUTH · GET_AUTH_BUKRS_LIST

**📌 4.3 표와의 미세 차이 (반영 시 유의)** ① CHECK_TCODE_AUTH는 클래스 내부에서 호출되지 않는 공개 유틸리티입니다 — CHECK_AUTH_BY_PID의 Tcode 체크는 이 메서드가 아니라 FM ZFPAC_STD_AUTH가 담당합니다. ② CHECK_AUTH_HQ의 «HQ» 판정은 실제로 Global('T') 또는 System Admin('A') 특권 보유 여부를 봅니다(HQ 전용 타입 'H'를 직접 보지 않음). ③ CHECK_SPECIAL_AUTH의 S/O/A 분기가 곧 4.4절 표의 로직이므로 두 절을 함께 보세요.
