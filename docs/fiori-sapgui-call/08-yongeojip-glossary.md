---
id: fiori-sapgui-call/08-yongeojip-glossary
doc: fiori-sapgui-call
title: 8. 용어집 (Glossary)
parent: docs/fiori-sapgui-call/README.md
---

# 8. 용어집 (Glossary)

본 문서에 등장하는 주요 용어·약어를 정리합니다. SAP 표준 항목은 표준 정의를 기준으로 합니다.

| 용어 / 약어 | 설명 |
|---|---|
| ZLPAC_FTCODE | Fiori에서 SAP GUI 트랜잭션을 호출하는 진입 프로그램/트랜잭션. 파라미터 조합으로 호출 유형을 분기. |
| Business Package (BUPAK) | PAC 결산 비즈니스 패키지 식별자. 데이터 타입 ZPAC_BUPAK. |
| PID | Activity(Process) ID. ZTPAC_PROC 조회 키(데이터 타입 ZPAC_PID). |
| CID | 결산점검 Category ID(데이터 타입 ZPAC_CID). Category 유형(CTYPE)으로 점검 트랜잭션을 결정. |
| REPTY | Activity 정의의 Report Type. 값이 'C'이면 결산일정 변경으로 분기. |
| CALLTYP | 호출 방식. 'P'=프로그램 SUBMIT, 그 외='T'=CALL TRANSACTION. |
| Relative | 연관 Activity 실행. P_RTYPE(ZPAC_REL_TYPE) 값 존재 시 CALL_RELATIVE로 처리. |
| To-Do | 담당자에게 할당된 처리 항목. P_TDTYPE(ZPAC_TODO_TYPE)로 조회 유형을 지정. |
| SCHID | Closing Schedule ID. 결산일정 변경 시 PID로부터 조회하여 전달. |
| Legacy RFC / URL | 트랜잭션 대신 연계되는 레거시 대상. 정의에 존재 시 CALL_URL로 처리. |
| XSKIP | 대상 화면 첫 셀렉션 화면 SKIP 여부 플래그. |
| SUBMIT ... WITH SELECTION-TABLE | 내부 파라미터 테이블(RSPARAMS)을 대상 리포트 셀렉션 화면에 전달하는 ABAP 표준 구문. |
| CALL TRANSACTION | 트랜잭션 코드를 실행하는 ABAP 표준 구문. 본 문서에서는 SET PARAMETER ID/BDCDATA와 함께 사용. |
| SET PARAMETER ID | SPA/GPA 파라미터 메모리에 값을 저장해 다음 화면 입력 필드에 기본값으로 전달하는 표준 구문. |
| RS_IMPORT_DYNPRO | 대상 화면(Dynpro)의 입력 필드 목록을 조회하는 표준 함수. 존재 필드에만 값 세팅에 사용. |
| MEMORY ID | EXPORT/IMPORT TO/FROM MEMORY로 프로그램 간 값을 전달하는 ABAP 메모리. 본 문서의 ZPAC0_INPUT_PARAM 해당. |
| AND RETURN | SUBMIT/호출 종료 후 제어를 호출 프로그램으로 반환하는 옵션. |
| TSTC | 트랜잭션 코드-실행 프로그램 매핑을 보관하는 SAP 표준 테이블. |
| ZTPAC_PROC | Activity Definition Master. Activity별 호출 정의(TCODE·CALLTYP·REPTY·CID·XSKIP·LEGACY_* 등)를 보관. |
| ZTPAC_CIS_CID | Closing Inspection Category Master. CID별 Category 유형(CTYPE) 보관. |
| ZCL_PAC_NETGRAPH | PAC 네트워크(연관 관계) 처리 클래스. CALL_RELATIVE 메소드 제공. |
| ZFPAC_LEGACY_LINK | 레거시 URL 연계 함수모듈(함수그룹 ZPAC270). |

— 문서 끝 —
