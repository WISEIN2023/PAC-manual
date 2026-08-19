---
id: monitoring/01-moniteoring-peurogeuraem-gaeyo
doc: monitoring
title: 1. 모니터링 프로그램 개요
parent: docs/monitoring/README.md
---

# 1. 모니터링 프로그램 개요

## 1.1 이 문서가 다루는 프로그램

본 메뉴얼은 PAC 결산 자동화 솔루션에서 결산 진행 상황을 모니터링하고 상태를 관리하는 7개 ABAP 프로그램의 운영·유지보수 방법을 설명합니다. 각 프로그램의 설명·화면 항목·처리 흐름은 SAP 운영 시스템의 실제 소스를 확인하여 작성했습니다.

7개 프로그램은 용도에 따라 크게 세 부류로 나뉩니다.

- **결산 진행현황 모니터링(집계·트리) :** ZLPAC_MONITOR_ BUPAK / COM / GPID — 조직·기간별로 액티비티의 완료·실패·진행 건수를 집계해 트리 형태로 보여줍니다.
- **특수 목적 모니터링 :** ZLPAC_OVERTIME_PID(장시간 수행 액티비티 감시), ZLPAC0170(월 최종결산 완료 현황).
- **관리자용 상태 관리 :** ZLPACSTATUSM — 액티비티 상태값 직접 변경, 스케줄 계획 관리, SAP 잠금(Lock) 조회·삭제.

## 1.2 7개 프로그램 한눈에 보기

| 프로그램 | 프로그램 설명(소스 헤더) | 구분 | 화면 형태 |
|---|---|---|---|
| ZLPAC_MONITOR_BUPAK | Monitoring by Business Package | 진행현황 | ALV 트리 |
| ZLPAC_MONITOR_COM | Monitoring By Company Code | 진행현황 | ALV 트리 |
| ZLPAC_MONITOR_GPID | Global Process Monitoring (글로벌) | 진행현황 | ALV 트리 + Excel |
| ZLPAC_OVERTIME_PID | Activity OverTime Monitoring | 특수 | ALV 그리드 |
| ZLPAC0170 | Monthly Final Closing Monitoring | 특수 | ALV 그리드 |
| ZLPACSTATUSM | Status Management for Admin | 관리자 | ALV(상태/스케줄/잠금) |

> 보완 설명 — '프로그램 설명'의 근거<br>위 표의 프로그램 설명은 각 프로그램 소스 첫머리의 주석(Description) 값을 그대로 옮긴 것입니다.<br>ZLPAC_MONITOR_ACT / BUPAK / COM / GPID 는 INCLUDE 구조가 동일한 계열 프로그램으로, TOP·SCR·ALV·MAIN·O01·I01·F01 의 7개 INCLUDE로 구성됩니다. 일부 INCLUDE 주석에는 원본(ZLPAC_MONITOR_GPID)에서 복사된 흔적이 남아 있으나, 동작에는 영향이 없습니다.

## 1.3 공통 개념 — 조직 레벨과 계층

PAC는 비즈니스 패키지(BUPAK)마다 결산 조직 단위를 다르게 정의합니다. 이 조직 레벨을 PACLVL 이라 하며, 모니터링 화면에 표시되는 조직 컬럼과 트리 구성이 이 값에 따라 달라집니다.

| PACLVL | 의미 | 핵심 조직 필드 |
|---|---|---|
| C | 회사코드(Company Code) 단위 결산 | BUKRS |
| B | 사업영역(Business Area) 단위 결산 | BUKRS + GSBER |
| U | 결산단위(Closing Unit) 단위 결산 | BUKRS + CUNIT |

진행현황 모니터링 트리는 아래 계층으로 구성됩니다. 화면·조회옵션에 따라 상위 레벨(회사그룹·지역·차수)이 추가되거나 하위 레벨(서브그룹·액티비티)이 생략됩니다.

| 계층(예: GPID) | 노드 | 설명 |
|---|---|---|
| 상위 | 회사그룹(Company Group) / 지역(Region) / 차수(Open Phase) | 글로벌 조회 시 집계 상위 노드 |
| 조직 | 회사코드(Company Code) | PACLVL에 따라 사업영역·결산단위로 대체 |
| 1레벨 | 액티비티 그룹(Activity Group) | PID 3번째 자리 = 'G' |
| 2레벨 | 액티비티 서브그룹(Activity) | PID 3번째 자리 = 'S' |
| 3레벨 | 액티비티(Closing ID / PID) | 실제 수행 프로그램 단위 |
