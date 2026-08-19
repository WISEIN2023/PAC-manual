---
id: closing-inspection/01-closing-inspection-gaeyo
doc: closing-inspection
title: 1. Closing Inspection 개요
parent: docs/closing-inspection/README.md
---

# 1. Closing Inspection 개요

## 1.1 Closing Inspection이란

Closing Inspection(결산 사전점검)은 PAC 결산 프로세스에서 실제 결산 Activity를 수행하기 전에, 미리 정의한 점검 시나리오를 실행하여 결산 데이터와 프로세스에 이상이 없는지 확인하는 기능입니다. Activity Master(ZLPAC0020)에서 Activity Type이 I(Closing Inspection)인 Activity에 대해 점검 항목을 정의하고, 정의된 시나리오를 실행·모니터링하는 구조로 동작합니다.

Closing Inspection은 다음 3단계 구조로 설정·운영됩니다.

| 단계 | T-Code | 역할 |
|---|---|---|
| ① Category 정의 | ZLPAC5050 | 점검 항목의 묶음 단위인 Closing Inspection Category를 생성 · 관리 |
| ② Scenario 등록 | ZLPAC5060 | Category 하위에 실제 수행할 점검 시나리오(Folder / Scenario)를 등록 |
| ③ Monitoring / 수행 | ZLPAC5200 | 등록된 시나리오를 실행(Inspection Run)하고 결과를 확인 · Confirm |

생성된 Category는 Activity Master(ZLPAC0020)의 Inspection Category 항목에 매핑하여 사용되며, 등록된 시나리오는 Closing Dashboard의 각 Node를 통해 실행되거나 Closing Inspection Monitoring(ZLPAC5200) 프로그램에서 실행됩니다.

## 1.2 관련 프로그램 목록

Closing Inspection 기능과 관련된 프로그램(트랜잭션)은 다음과 같습니다. 아래 목록은 운영 시스템(개발 패키지 ZPAC / ZPAC_CIS)에서 실제 확인한 내역입니다.

| T-Code | 프로그램명 (시스템 등록 내역) | 패키지 |
|---|---|---|
| ZLPAC0020 | Define Activity Master | ZPAC |
| ZLPAC5050 | Define Closing Inspection Category | ZPAC_CIS |
| ZLPAC5060 | Maintain Closing Inspection Scenario | ZPAC_CIS |
| ZLPAC5070 | Maintain Error Control for Closing Inspection Simulation | ZPAC_CIS |
| ZLPAC5080 | Maintain Closing Inspection Reviewer | ZPAC_CIS |
| ZLPAC5090 | Display Closing Inspection Reviewer | ZPAC |
| ZLPAC5100 | Financial Risk Validation Monitoring | ZPAC_CIS |
| ZLPAC5110 | Auto Execution Closing Inspection Category by Reviewer | ZPAC_CIS |
| ZLPAC5111 | Auto Execution for Closing Inspection Reviewer By Scenario | ZPAC_CIS |
| ZLPAC5200 | Closing Inspection Monitoring | ZPAC_CIS |
| ZLPAC5210 | Auto Execution for Closing Inspection By Category | ZPAC_CIS |
| ZLPAC5211 | Auto Execution for Closing Inspection By Scenario | ZPAC_CIS |
| ZLPAC5400 | Financial Risk Validation Dashboard | ZPAC_CIS |

> 보완 설명 — 주요 저장 테이블 (시스템 검증)<br>· ZTPAC_CIS_CID (Closing Inspection Category Master) : Category 기본 정보가 저장되는 테이블. Business Package(BUPAK) + Category ID(CID)가 키로 구성됩니다.<br>· ZTPAC_CIS (Closing Inspection Scenario Master) : Folder / Scenario 계층과 시나리오 실행 정보(Error Control, 점검유형, Function, CDS View, 조직유형, 기간유형 등)가 저장되는 테이블. BUPAK + CID + Scenario ID(SNID)가 키로 구성됩니다.<br>· 이 외에 Function Variant 파라미터(ZTPAC_CIS_VPARAM), 조직 지정(ZTPAC_CIS_ORG), Relative 등록(ZTPAC_CIS_REL) 등의 부속 테이블이 시나리오 상세 정보를 나누어 저장합니다.
