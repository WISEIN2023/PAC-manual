---
id: fiori-sapgui-call/01-piori-sap-gui-hochul-gaeyo
doc: fiori-sapgui-call
title: 1. 피오리 → SAP GUI 호출 개요
parent: docs/fiori-sapgui-call/README.md
---

# 1. 피오리 → SAP GUI 호출 개요

PAC의 결산 프로세스는 Fiori 화면(Closing Dashboard / Monitoring Dashboard)에서 조회·조작하지만, 개별 Activity의 실제 실행 화면은 SAP GUI 트랜잭션으로 제공되는 경우가 많습니다. Fiori에서 이러한 GUI 트랜잭션을 열어야 할 때, PAC는 단일 진입 프로그램 ZLPAC_FTCODE 를 경유하여 대상 트랜잭션·프로그램을 호출합니다. Fiori는 대상 T-Code를 직접 지정하지 않고 ZLPAC_FTCODE(T-Code)에 표준 파라미터만 전달하며, 실제 어떤 화면을 어떻게 띄울지는 ZLPAC_FTCODE 내부 분기 로직이 결정합니다.

> ■ 시스템 확인 — ZLPAC_FTCODE 오브젝트<br>프로그램 ZLPAC_FTCODE : 리포트(Type 1), 패키지 ZPAC, 설명 “Call SAP Transaction from Fiori”.<br>트랜잭션 ZLPAC_FTCODE : Fiori에서 호출하는 진입 T-Code, 설명 “Call TCODE from fiori”.<br>구성 인클루드 : ZLPAC_FTCODE_TOP / _SCR / _MAIN / _F01.

## 1.1 호출 구조 한눈에 보기

Fiori에서 발생한 호출은 다음 3단계 구조를 따릅니다. 진입점은 항상 ZLPAC_FTCODE 하나이며, 전달된 파라미터 조합에 따라 최종 호출 대상이 갈라집니다.

| 단계 | 구성 요소 | 역할 |
|---|---|---|
| ① 진입 | Fiori 화면 | 결산 프로세스/대시보드/To-Do 등에서 Activity·버튼 클릭 |
| ② 경유 | ZLPAC_FTCODE (T-Code) | 표준 파라미터(조직·기간·PID·TCODE 등)를 수신하여 호출 유형을 판정 |
| ③ 실행 | 대상 트랜잭션 / 프로그램 | SUBMIT 또는 CALL TRANSACTION으로 실제 GUI 화면을 실행 |

> 보완 설명 — 단일 진입 방식의 이점<br>대상 트랜잭션이 늘어나도 Fiori 측 호출 인터페이스는 ZLPAC_FTCODE 하나로 고정됩니다. 화면 추가·변경 시 Back-End 분기 로직만 조정하면 되므로 Fiori-GUI 연계의 유지보수 지점이 한 곳으로 모입니다.

## 1.2 ZLPAC_FTCODE 프로그램 구성

ZLPAC_FTCODE 는 표준 리포트 구조로 4개의 인클루드로 구성됩니다. 운영 점검 시 어느 인클루드를 봐야 하는지 아래를 기준으로 삼으십시오.

| 인클루드 | 내용 | 비고 |
|---|---|---|
| ZLPAC_FTCODE_TOP | 전역 데이터·상수 선언 | 타입/작업영역 정의 |
| ZLPAC_FTCODE_SCR | 셀렉션 화면(파라미터) 정의 | 호출 인터페이스 (2장) |
| ZLPAC_FTCODE_MAIN | START-OF-SELECTION 분기 로직 | 호출 유형 판정 (3장) |
| ZLPAC_FTCODE_F01 | 호출 유형별 FORM 구현 | 상세 동작 (4장) |

## 1.3 파생 프로그램 (참고)

동일한 호출 구조를 목적별로 파생한 프로그램이 함께 존재합니다. 본 문서는 표준 호출 프로그램 ZLPAC_FTCODE 를 기준으로 설명합니다.

| 프로그램 | 설명(시스템 등록값) | 용도 |
|---|---|---|
| ZLPAC_FTCODE | Call SAP Transaction from Fiori | 표준 호출(본 문서 대상) |
| ZLPAC_FTCODE_SIMUL | Call SAP Transaction for Simulation | 시뮬레이션 실행용 호출 |
| ZLPAC_FTCODE_SNID | Call SAP Transaction for Scenario | 시나리오 실행용 호출 |
