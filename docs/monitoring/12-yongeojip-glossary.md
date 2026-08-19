---
id: monitoring/12-yongeojip-glossary
doc: monitoring
title: 12. 용어집 (Glossary)
parent: docs/monitoring/README.md
---

# 12. 용어집 (Glossary)

본 문서에 등장하는 주요 용어·프로그램·테이블·클래스를 정리합니다. SAP 표준 항목은 표준 정의를, PAC 고유 항목은 소스 확인 내용을 기준으로 정리했습니다.

## 12.1 개념 · 코드

| 용어 / 약어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. 본 문서의 대상인 SAP 결산자동화 솔루션. |
| BUPAK / Business Package | 비즈니스 패키지. 결산 프로세스를 묶는 PAC 최상위 단위. |
| PACLVL | 비즈니스 패키지의 조직 레벨. C=회사코드, B=사업영역, U=결산단위. |
| Activity / Activity Group / Sub-Group | 결산 작업 단위(Activity=PID)와 그 상위 묶음(그룹·서브그룹). PID 3번째 자리 G/S로 구분. |
| PID | Program/Process ID. 액티비티 식별자(수행 단위). |
| Status (ZPAC_STATUS) | 액티비티 상태 코드. C 완료, T 수동확정, P 기간스킵, F 실패, W 재작업, R 진행, S 시작, H 보류, A 종료/취소, 공백 미수행. |
| GPID / Global Package ID | 여러 법인·지역을 아우르는 글로벌 패키지 식별자. |
| Open Phase (오픈 차수) | 글로벌 조회 시 사용하는 오픈 차수. GPID 모니터의 상위 집계 레벨(OPENPH). |
| Company Group / Region | 회사그룹(COMGRP) / 지역(REGION). 글로벌 조회의 상위 집계 노드. |
| Progress Rate | 진행률(%). 완료 건수 ÷ 총 건수 × 100(정수). 진행 중 건은 미가산. |
| ACT_XFINAL | 월 최종결산 활성 플래그(ZTPAC_CONFIG). ZLPAC0170 조회 대상 판정에 사용. |
| REQ_BUKRS | 비즈니스 패키지의 회사코드 필수 여부(ZTPAC_CONFIG). |
| XAUTO | 액티비티 자동 수행 대상 여부(ZTPAC_PROC). OverTime 판정에 사용. |

## 12.2 프로그램 · 함수 · 클래스

| 명칭 | 설명 |
|---|---|
| ZLPAC_MONITOR_ACT / BUPAK / COM / GPID | 진행현황 모니터링 프로그램(각각 액티비티·패키지·회사코드·글로벌 기준). |
| ZLPAC_OVERTIME_PID | 실행시간 초과(장시간 수행) 액티비티 감시 프로그램. |
| ZLPAC0170 | 월 최종결산 완료 현황 모니터링 프로그램. |
| ZLPACSTATUSM | 관리자용 상태/스케줄/잠금 관리 프로그램. |
| ZFPAC_PAC_MONITOR | 조직·액티비티별 상태 건수를 집계해 돌려주는 공통 함수(진행현황 계열의 데이터 소스). |
| ZFPAC_LOG_DISPLAY / ZLPAC0160 | 실행 로그 조회 함수 / 프로그램. 건수 더블클릭 시 연계. |
| ZLPAC7010 | 결산 스케줄 프로그램. 스케줄 관리 모드에서 스케줄 ID 더블클릭 시 연계. |
| ZCL_PAC_FUNC=>GET_DEFAULT_PERIOD | 기본 결산 기간(연/월)을 반환. |
| ZCL_PAC=>GET_COMPLETE_ORG_LIST | 조직별 월 최종결산 완료 정보 반환(ZLPAC0170). |
| ZCL_PAC=>SYNC_PCSGP_STATUS | 액티비티 상태 변경 시 상위 그룹 상태 동기화. |
| ZCL_PAC_AUTH | 조직·HQ 권한 판정 클래스(GET_AUTH_BUKRS/GSBER/CUNIT_LIST, CHECK_AUTH_HQ 등). |
| ZCL_PAC_FIORI=>CALL_APC | Fiori 화면 실시간 갱신(APC) 호출. |

## 12.3 테이블 · 구조

| 명칭 | 설명 |
|---|---|
| ZTPAC_STATUS | 액티비티 상태 보관 테이블. |
| ZTPAC_PROC | 액티비티 정의 마스터(유형 REPTY, TCODE, XAUTO, 삭제 LOEVM 등). |
| ZTPAC_CONFIG | 비즈니스 패키지 설정(PACLVL, REQ_BUKRS, ACT_XFINAL, PERTYPE, FIORI_TILE 등). |
| ZTPAC_CLOSE | 월 결산 완료 정보 테이블(ZLPAC0170). |
| ZTPAC_LOG_HDR | 실행 로그 헤더(시작일시 ERDAT/ERZET, 소요 EXETM, 배치잡, LOGID). |
| ZTPAC_SCH_PLAN | 결산 스케줄 계획 테이블. |
| ZTPAC_SCH_DISTM | 스케줄 배포 상태 테이블(STATUS L/D). OverTime 기본 조회월 산정에 사용. |
| ZTPAC_GPID / ZTPAC_GPID_MAST | 글로벌 패키지 구성 / 마스터. |
| ZTPAC_COM_MAST / ZTPAC_COM_GRP | 회사 마스터(지역·회사그룹·차수·타임존) / 회사그룹 마스터. |
| ZTPAC_CUNIT_MAST / ZTPAC_BA_MAST | 결산단위 마스터 / 사업영역 마스터. |
| ZTPACSYS | 시스템 설정(자동 새로고침 기본값 REFRESH_MIN/REFRESH_MAX). |
| ZSPAC_HQ_MONITOR / ZYPAC_HQ_MONITOR | 모니터링 집계 결과 구조 / 테이블 타입. |

## 12.4 SAP 표준 / UI

| 용어 / 약어 | 설명 |
|---|---|
| ALV Tree (CL_GUI_ALV_TREE) | 계층형 목록 표시용 표준 UI 컨트롤. 진행현황 모니터의 트리 화면. |
| ALV Grid (CL_GUI_ALV_GRID) | 표 형태 목록 표시용 표준 UI 컨트롤. OverTime·ZLPAC0170·상태관리 화면. |
| CL_GUI_TIMER | 화면 타이머 표준 클래스. 자동 새로고침 주기 제어. |
| CL_SALV_TABLE | 간편 ALV 표준 클래스. GPID 모니터의 XLSX 다운로드에 사용. |
| ENQUEUE / DEQUEUE | SAP 표준 잠금 설정/해제. 상태·스케줄 편집 시 동시 편집 방지에 사용. |
| SM12 | SAP 잠금(Lock) 조회·관리 표준 트랜잭션. 잠금 관리 모드가 이와 유사. |
| ENQUE_READ / ENQUE_DELETE | 잠금 조회 / 삭제 표준 함수(잠금 관리 모드에서 사용). |
| BUKRS / GSBER / GJAHR / MONAT / SPMON | 회사코드 / 사업영역 / 회계연도 / 회계기간(월) / 연월(YYYYMM). SAP 표준 필드. |
| EXETM | 실행 소요 시간(초). OverTime의 지난달·평균 소요 계산에 사용. |
| OData / Fiori | Fiori 화면의 데이터 조회 프로토콜 / SAP 웹 UI. OverTime의 Link가 Fiori로 이동. |

— 문서 끝 —
