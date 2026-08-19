---
id: authorization/08-05-sawonmaseuteo-insamaseuteo-yeongyewa-exit
doc: authorization
title: 7. 실행 유저 / Posting User 개념 > 7.5 사원마스터(인사마스터) 연계와 Exit ON_GET_USERINFO — 화면의 사용자 정보는 어디서 오나
parent: docs/authorization/README.md
---

# 7. 실행 유저 / Posting User 개념

## 7.5 사원마스터(인사마스터) 연계와 Exit ON_GET_USERINFO — 화면의 사용자 정보는 어디서 오나

**📌 수정 이력** (2026-07-06 추가) 고객사 사원마스터 테이블 연계와 Exit ON_GET_USERINFO 동작·활용범위를 신설했습니다.

고객사에는 보통 **사원 마스터 테이블(인사마스터)**이 있고, 여기에 사원별 SAP ID·사번·성명·부서명·이메일 등 관리 대상 사원정보가 담겨 있습니다. PAC은 참여자 등록(ZLPAC1000) 화면 등 각종 화면에서 이 정보를 가져다 쓰는데, 그 표준 통로가 ZCL_PAC_ORG=>ON_GET_USERINFO 와 여기에 연결되는 **Exit(고객사 함수)** 입니다. 어느 고객사에 가더라도 «고객사의 인사마스터 테이블을 PAC에 적용하는 일»은 반드시 수행하는 표준 구축 작업입니다.

| 고객사 | 사원마스터 테이블 | 비고 |
|---|---|---|
| LG전자 | ZPCMT0063 | 미확인(고객사 시스템) — 현재 검증 시스템에서 조회 불가 |
| LXI | ZCOAT1004 | 미확인(고객사 시스템) — 현재 검증 시스템에서 조회 불가 |

**⚠️ 데이터 출처(확인 필요)** 사원마스터 데이터는 고객사 인사시스템 또는 권한신청 관련 프로세스와의 인터페이스로 적재·갱신되는 것으로 추정됩니다(운영 경험 기준, 미확정). 신규 고객사에서는 «누가/어떤 주기로 이 테이블을 채우는지»를 반드시 확인하세요.

### 7.5.1 동작 구조 — Exit가 있으면 사원마스터, 없으면 SU01 기준

**✔ SAP 검증 완료:** ZCL_PAC_ORG=>ON_GET_USERINFO 소스 확인("Get User Information"). 파라미터: IT_USERID·IT_ORG·IV_MAXROW → ET_USERIF(ZYPAC_USER_INFO). 내부에서 ZTPACSYS(DISUSER 등)와 ZTPACEXIT(EXIT_GROUP=ZPAC0_EXIT_EMP_MAST 상수, SUBGRP='USER')를 읽어 분기함

**결정 규칙 (실제 코드 인용):**

METHOD ON_GET_USERINFO.   " ZCL_PAC_ORG   " ① User Master 조회 기준 (ZLPACSYS 설정)   SELECT SINGLE DISUSER, USRID_E, EMPNO_E, EMAIL_E ... FROM ZTPACSYS.    " ② EXIT 적용 Check — ZLPACEXIT에서 등록한 고객사 함수   SELECT SINGLE EXITFUNC INTO @DATA(LV_FUNC) FROM ZTPACEXIT    WHERE EXIT_GROUP EQ @ZPAC0_EXIT_EMP_MAST AND SUBGRP EQ 'USER'.    " ③ 사번마스터 EXIT 활성화 된 경우 (원 주석)   IF SY-SUBRC EQ 0 AND LS_SYS-DISUSER EQ 'E'.     CALL FUNCTION LV_FUNC          " 고객사 Exit 함수 동적 호출       EXPORTING IT_USERID = ... IT_ORG = ... IV_MAXROW = ...       IMPORTING ET_USERIF = ET_USERIF.  " ← 사원마스터에서 조회한 결과   ELSE.     " ④ EXIT 미존재 : STANDARD User Info (SU01 기준)     SELECT ... FROM USR21 JOIN USER_ADDR LEFT JOIN ADR6                LEFT OUTER JOIN I_COSTCENTERTEXT ...   ENDIF. ENDMETHOD.

- **Exit 활성 조건 2가지:** ① ZTPACEXIT에 사번마스터 Exit 함수가 등록되어 있고(EXIT_GROUP=사번마스터·SUBGRP='USER') ② ZTPACSYS의 DISUSER 값이 'E'일 것. 하나라도 아니면 SAP 표준 사용자마스터(SU01: USR21·USER_ADDR·ADR6·코스트센터 텍스트)에서 조회합니다.
- **Exit 함수의 역할:** 고객사 사원마스터 테이블(LG: ZPCMT0063, LXI: ZCOAT1004)을 조회해 표준 반환 구조로 매핑해 돌려주는 것. 함수 인터페이스는 IT_USERID / IT_ORG / IV_MAXROW → ET_USERIF 로 고정입니다.
- **Exit 등록 위치:** ZLPACEXIT ("Maintain PAC User Exit") 프로그램·트랜잭션에서 등록하며, 저장 테이블은 ZTPACEXIT (BUPAK·EXIT_GROUP·SUBGRP 키, EXITFUNC=함수명) 입니다.
**✔ SAP 검증 완료:** ZLPACEXIT = "Maintain PAC User Exit" (프로그램+트랜잭션 실재 확인), ZTPACEXIT = "PAC User Exit Program" (테이블 실재 확인). EXIT_GROUP 상수 ZPAC0_EXIT_EMP_MAST의 실제 값은 타입그룹(ZPAC0) 소스 미열람 제약으로 미확인 — 운영 SE16(ZTPACEXIT)에서 확인

**반환 구조** ZSPAC_USER_INFO **("Customer Specific INFO") 주요 필드:**

| 필드 | 의미 |
|---|---|
| USER_ID | SAP User ID (BNAME) |
| EMPNO / PERNR | 사번 / 인사 사원번호 |
| NAME_LOCAL / NAME_ENG | 성명(현지어/영문) |
| ORGANIZATION_ID / ORGANIZATION_NAME(_ENG) | 부서(조직) ID·명 |
| EMAIL_ID | 이메일 |
| BUKRS / GSBER / KOSTL(KTEXT) | 회사코드 / 사업영역 / 코스트센터(명) |
| RESIGNATION_FLAG / RESIGNATION_DATE | 퇴사 여부 / 퇴사일 |

**✔ SAP 검증 완료:** ZSPAC_USER_INFO 구조 실재 확인(위 필드 전부). 같은 계열 Exit로 조직마스터용 ON_GET_ORG_MAST_EXIT·ON_GET_BUKRS_MAST_EXIT·ON_GET_BA_MAST_EXIT·ON_GET_CUNIT_MAST_EXIT·ON_GET_DEPT_MAST_EXIT도 ZCL_PAC_ORG에 동일 패턴(ZTPACEXIT 조회→동적 CALL)으로 존재함

### 7.5.2 활용범위 — 어디서 이 정보를 쓰나

- **① 사원정보 F4 검색 도움말:** 참여자 등록(ZLPAC1000) 등에서 User ID 입력 필드의 F4를 누르면 Search Help Exit 함수 ZFPAC_EMP_INFO_SH_EXIT / ZFPAC_USRID_INFO_SH_EXIT (함수그룹 ZPAC241, "[PAC] Employee Info Search help Exit")가 ON_GET_USERINFO를 호출해 ID·사번·성명·부서·이메일로 검색한 사원 리스트를 보여줍니다(최대 500건).
- **② 화면의 사용자명·부서·이메일 표시:** DISUSER='E'면 화면에 표시되는 사용자 정보가 사원마스터 기준이 됩니다. ZLPACSYS(User Management 탭)의 USRID/EMPNO/UNAME/EMAIL 표시 설정 필드(ZTPACSYS의 USRID_S·USRID_E·EMPNO_S·EMPNO_E·UNAME_S·UNAME_E·EMAIL_S·EMAIL_E)와 연동됩니다.
- **③ SSO 연계:** 사원마스터를 기준으로 포탈 계정↔SAP ID 매핑을 구성해 SSO(6.5)를 적용할 수 있습니다. LG전자는 EP 포탈↔SAP 통합 로그인에 활용.
- **④ 퇴사자 관리:** RESIGNATION_FLAG·RESIGNATION_DATE 필드로 퇴사자를 식별할 수 있어, 참여자 정리·권한 회수 점검의 기준 데이터가 됩니다.
**✔ SAP 검증 완료:** ①·②는 소스에서 직접 확인(Search Help Exit의 ON_GET_USERINFO 호출, ZTPACSYS 설정 판독). ③·④는 구조 필드·운영 경험 기준 — 적용 방식은 고객사별 상이

### 7.5.3 신규 고객사 적용 체크리스트 (표준 구축 작업)

1. 고객사 인사마스터 테이블과 적재 경로(인사시스템/권한신청 인터페이스, 갱신 주기) 확인
2. Exit 함수 개발 — 인사마스터를 조회해 ZSPAC_USER_INFO 구조(ET_USERIF)로 매핑. 인터페이스는 IT_USERID/IT_ORG/IV_MAXROW → ET_USERIF 준수
3. ZLPACEXIT 에서 사번마스터 Exit 그룹(SUBGRP='USER')에 함수 등록 (ZTPACEXIT 저장 확인)
4. ZLPACSYS에서 DISUSER 등 User Management 표시 기준을 사원마스터(E) 기준으로 설정
5. 참여자 등록 화면(ZLPAC1000)에서 F4 검색·사용자명 표시가 사원마스터 기준으로 나오는지 테스트
**⚠️ 이름이 비슷한 테이블 혼동 주의** ZTPAC_USERINFO("PAC User Default Information")는 사원마스터가 아니라 «사용자별 기본값(Default BUPAK·조직, Network Graph 화면 설정)» 저장 테이블입니다. 사원정보(성명·부서·이메일)는 ZSPAC_USER_INFO 구조로 반환되는 사원마스터/SU01 데이터를 보세요.

**💡 운영 팁** 화면에서 «사용자명이 안 보인다/이상하다» 문의가 오면 먼저 사원마스터 테이블에 해당 사번·SAP ID 데이터가 올바르게 존재하는지(SE16), 그리고 ZTPACEXIT 등록·ZLPACSYS DISUSER 설정을 확인하세요. 트러블슈팅 표는 10.1 참고.
