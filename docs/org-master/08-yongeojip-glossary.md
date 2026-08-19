---
id: org-master/08-yongeojip-glossary
doc: org-master
title: 8. 용어집 (Glossary)
parent: docs/org-master/README.md
---

# 8. 용어집 (Glossary)

본 문서에 등장하는 주요 용어·약어·프로그램·테이블을 정리합니다. SAP 표준 항목은 표준 정의를, PAC 고유 항목은 프로그램 소스·데이터 사전(DDIC) 확인 결과를 기준으로 정리했습니다.

| 용어 / 약어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. 본 문서의 대상인 SAP 결산자동화 솔루션. |
| 조직마스터 (Organization Master) | 결산을 수행하는 조직·분류 기준 정보. 회사코드·사업영역·결산단위·지역·국가·회사그룹·비즈니스 유형 등을 포함. |
| 비즈니스 패키지 (Business Package, BUPAK) | PAC의 결산 시나리오 단위. 조직 레벨(PACLVL)을 가지며 조직이 이 패키지에 배정됨. |
| 조직 레벨 (PACLVL) | 비즈니스 패키지가 결산을 관리하는 조직 단위. C=회사코드, B=사업영역, U=결산단위. (ZTPAC_CONFIG-PACLVL) |
| 비즈니스 유형 (Business Type, BUSTY) | 조직의 결산 업무 성격 분류 코드. ZLPAC0013에서 정의. 레벨(BLEVEL) A/C/B/K를 가짐. |
| 결산단위 / 기타조직 (Closing Unit, CUNIT) | 회사코드·사업영역으로 표현하기 어려운 별도의 결산 관리 단위. ZLPAC0200에서 정의(ZTPAC_CUNIT_MAST). |
| 회사그룹 (Company Group, COMGRP) | 여러 회사코드를 묶는 그룹. ZLPAC0093에서 정의(ZTPAC_COM_GRP). |
| 지역 (Region) | 결산 현황을 지도/그룹으로 표시하기 위한 지역 분류. ZLPAC0091에서 정의(ZTPAC_REGION). |
| Activity / Activity Group | PAC 결산 프로세스의 작업 단위(Activity)와 그 묶음(Group). 상태는 ZTPAC_STATUS로 관리됨. |
| PID | Process ID. 결산 프로세스(구조)를 식별하는 값. ZLPAC7193의 파라미터 P_PID. |
| PCSGP | 프로세스/Activity 그룹 식별자. ZLPAC7192/7193의 상태 동기화 대상 단위. |
| BUKRS | 회사코드(법인). SAP 표준 필드. |
| GSBER | 사업영역(Business Area). SAP 표준 필드. |
| LAND1 | 국가 키. SAP 표준 필드. |
| SPRAS | 언어 키. SAP 표준 필드. |
| TZONE | 시간대(Time Zone). SAP 표준 필드(TTZZ/TTZ5 참조). |
| BLEVEL | 비즈니스 유형 레벨. A / C(회사코드) / B(사업영역) / K(결산단위). (ZTPAC_BUSTY-BLEVEL) |
| REPFLAG | 대표조직 플래그. 대표 조직 여부 표시(소스 주석: 대표조직 FLAG). |
| OPENDT / OPENPH | 결산 오픈(개시) 일자 / 오픈 순서(차수). |
| ITMSEQ | 항목 시퀀스. 화면 표시(정렬) 순서. |
| LOEVM | 삭제 플래그(Deletion Flag). 논리 삭제 표시. |
| CLOSED | 결산 마감 여부(ZTPAC_CLOSE-CLOSED='X'). 마감된 조직/기간은 상태 동기화 대상에서 제외됨. |
| ZSPAC_TIMESTAMP | 생성자·생성일·최종변경자·변경일·변경시각을 담는 공통 인클루드 구조. 모든 조직마스터 테이블에 포함. |
| ALV (SAP List Viewer) | SAP의 표준 목록/편집 그리드. 본 문서의 유지보수 화면(화면번호 0100)이 사용. |
| SE38 / SA38 | ABAP 프로그램을 직접 실행/편집하는 표준 트랜잭션. 트랜잭션이 없는 배치 프로그램 실행에 사용. |
| SM12 | SAP 잠금(Lock) 항목을 조회·관리하는 표준 트랜잭션. |
| ZTPAC_STATUS | PAC Activity의 결산 상태를 보관하는 테이블. 동기화 배치가 갱신함. |
| ZCL_PAC / ZCL_PAC_FUNC | PAC 핵심 로직 클래스. 상태 동기화(SYNC_PCSGP_STATUS)·결산월 조회 등 제공. |
| ZTPAC_CONFIG_COM/BA/UNI | 비즈니스 패키지별 조직 배정(설정) 테이블. ZLPAC0050에서 유지보수. |

— 문서 끝 —
