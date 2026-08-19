---
id: authorization/15-yongeojip
doc: authorization
title: 13. 용어집
parent: docs/authorization/README.md
---

# 13. 용어집

**Activity**

PAC 결산 프로세스를 구성하는 기본 작업 단위. Sub-Group → Group → Business Package로 묶임.

**Authorization Object**

SAP에서 특정 기능 사용 권한을 제어하는 기본 단위. 예: ZPAC_BUPAK, S_TCODE.

**Auth Group(Authorization Group)**

Special Auth를 Object 방식으로 검사할 때, 어떤 Role 보유로 판정할지 매핑하는 키값(ZLPAC1030).

**Business Package(BUPAK)**

결산 프로세스를 묶은 단위. FI(개별결산), CO(원가), FC(연결회계) 등. Controller 레벨.

**BATCHCWF001**

LG의 CWF 배치(System) 유저. 자동 수행용 풀 권한 유저.

**Catalog(Fiori Catalog)**

Fiori 앱(타일)을 묶은 권한 집합. Role에 할당해야 타일이 보임.

**Controller**

Business Package 레벨 담당자. 해당 BUPAK 법인별 모든 Activity 수행 가능.

**CWF(Closing Work Flow)**

결산 워크플로우. CWF 담당자가 권한을 부여·점검.

**Derive(파생)**

Master Role을 상속해 Variant Role을 만드는 작업. 파생 후 권한값 reset에 주의.

**Execute User**

Activity를 실제로 수행한 유저. Posting User와 다를 수 있음.

**Fiori**

SAP의 웹 기반 UI. PAC은 Fiori 기반으로 동작.

**GSOD**

LG전자 운영서버 권한신청 환경. 사용자가 직접 신청. 표시설정은 ZPCMR1405.

**INTCWFPO001**

LG의 I/F System User. SAP ID 없는 유관담당자에게 임시(3일) 유저·권한 부여.

**Master Role**

권한 Object 설정의 기준 Role. Tcode 단위 생성. 예: ZM_FCW_*.

**ON_GET_USERINFO**

ZCL_PAC_ORG의 사용자 정보 조회 메서드. ZLPACEXIT에 등록된 고객사 Exit 함수(사원마스터 조회)를 호출하고, 없으면 SU01 표준 정보를 반환(7.5).

**Participant**

각 Activity의 담당자 등록(ZLPAC1000). BUPAK·조직 단위.

**PAC(Process Automatic Channel)**

SAP 기반 결산자동화 솔루션.

**PFCG**

SAP 표준 권한(Role) 생성·편집 Tcode.

**PFCGMASSVAL**

여러 Role의 권한 Object 값을 일괄 변경하는 Tcode.

**Posting User**

기표 시 표시되는 유저. ZLPAC0010 BUPAK Config 설정(A/R/F)에 따름.

**Reviewer**

Closing Inspection(결산 점검) 시나리오별 담당자(ZLPAC5080).

**SE43**

Area Menu(영역 메뉴) 유지보수 Tcode.

**Special Auth / Special Role**

Participant 없이 Activity 수행 가능한 특수 권한(ZLPAC1050). A=Admin, T=TF 등.

**SSO**

단일 ID/PW로 여러 시스템 통합 로그인(LG: EP↔SAP). 계정 매핑에 사원마스터 활용 가능(7.5).

**SU01**

사용자 생성·수정·잠금해제·Role 배정 Tcode.

**SU20 / SU21 / SU24**

권한 필드 생성 / Authorization Object 생성·조회 / Tcode별 권한 제안값(Default Data) 관리 Tcode (5.9).

**SU53**

직전 권한오류의 원인 Authorization Object 확인 Tcode.

**SUIM**

권한 분석 통합 도구(User Information System).

**Variant Role**

Master를 상속해 실제 사용자에게 부여되는 Role. Tcode+조직 단위. 예: ZV_FCW_*.

**World Map**

Closing Dashboard의 지도 화면. Participant 등록 기준으로 법인 표시.

**ZPAC_BUPAK**

Business Package(BUPAK)별 권한을 제어하는 Authorization Object.

**ZLPACEXIT**

PAC User Exit 등록·관리 프로그램(트랜잭션). 등록 내용은 ZTPACEXIT 테이블에 저장.

**ZLPACSYS**

PAC 시스템 설정 프로그램. Authorization·User Management 등 탭 보유.

**사원마스터(인사마스터)**

고객사별 사원정보(SAP ID·사번·성명·부서·이메일 등) 테이블. LG전자 ZPCMT0063, LXI ZCOAT1004. PAC은 Exit ON_GET_USERINFO로 연계(7.5).

**— 문서 끝 —**

본 메뉴얼은 엑셀 기초자료 + SAP ADT(MCP) 검증을 기반으로 작성되었습니다. 캡처(📷)·미확인 객체는 운영 시스템에서 보완하세요.
