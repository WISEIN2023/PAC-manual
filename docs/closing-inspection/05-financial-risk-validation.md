---
id: closing-inspection/05-financial-risk-validation
doc: closing-inspection
title: 5. Financial Risk Validation
parent: docs/closing-inspection/README.md
---

# 5. Financial Risk Validation

## 5.1 개요

Financial Risk Validation은 재무 위험 검증을 위한 결산점검 기능으로, Closing Inspection Category(ZLPAC5050)에서 Inspection Type을 R(Financial Risk Validation)로 정의한 Category를 대상으로 합니다. (2.3 참조)

- GERP에서 GFVS라고 칭하던 기능을 NERP에서는 Financial Risk Validation으로 칭합니다.
Financial Risk Validation은 다음 2개 프로그램으로 운영됩니다.

| 프로그램 | 프로그램명 (시스템 등록 내역) | 용도 |
|---|---|---|
| ZLPAC5100 | Financial Risk Validation Monitoring | 법인 단위 점검 수행 · 모니터링 |
| ZLPAC5400 | Financial Risk Validation Dashboard | 전 법인 수행 현황 조회 |

## 5.2 Financial Risk Validation Monitoring (ZLPAC5100)

| 화면명 | Financial Risk Validation Monitoring | T-Code | ZLPAC5100 |
|---|---|---|---|
| 설명 | Financial Risk Validation 점검 수행 · 모니터링 |  |  |

Financial Risk Validation의 점검 수행은 ZLPAC5100에서 진행하며, 화면 구성과 사용 방법은 Closing Inspection Monitoring(ZLPAC5200)과 크게 다르지 않습니다. 조회 · Inspection Run · 상태별 결과 조회 · Confirm 처리 방법은 4장의 내용을 동일하게 참고하십시오.

## 5.3 Financial Risk Validation Dashboard (ZLPAC5400)

| 화면명 | Financial Risk Validation Dashboard | T-Code | ZLPAC5400 |
|---|---|---|---|
| 설명 | 전 법인의 Financial Risk Validation 수행 현황을 한 화면에서 조회 |  |  |

Financial Risk Validation을 사용하는 전 법인에 대해 시나리오 수행 현황을 조회할 수 있는 신규 프로그램입니다. 조회 Type은 Region과 Company Code 2가지가 있으며, 각 Type별로 검색할 수 있습니다.

### 5.3.1 Status 표시 기준 — Type : Company Code

각 Company Code의 Scenario 수행 상태를 기준으로 다음과 같이 표시됩니다.

| 상태 | 표시 |
|---|---|
| Complete 상태 | 초록불 |
| Fail 상태 | 빨간불 |
| 미수행 상태, Confirm하지 않은 상태 | 마름모 |
| 해당 Company Code에서 사용하지 않는 Scenario | 'X' |

### 5.3.2 Status 표시 기준 — Type : Region

Region 하위 Company Code의 수행 상태를 종합하여 다음과 같이 표시됩니다.

| 상태 | 표시 |
|---|---|
| 하위 법인 중 수행된 법인이 1개 이상 존재하고, 전체가 Complete 상태는 아니면서 Fail이 없는 경우 | 노란불 |
| 하위 법인 중 Fail 상태인 법인이 있는 경우 | 빨간불 |
| 하위 법인이 모두 Complete인 경우 | 초록불 |
| 하위 법인이 모두 미수행인 경우 | 마름모 |

하위 법인 중 일부 법인만 수행이 완료된 경우 Region의 Status는 진행중(노란불)으로 표시되며, 하위 전체 법인의 시나리오가 완료되면 Region의 시나리오도 완료로 변경됩니다.

### 5.3.3 Scenario 사용 여부가 혼재하는 경우 (Type : Region)

Region 조회 시 하위 Company Code별 Scenario 사용 여부가 혼재하는 경우를 고려하여 다음 기준이 함께 반영됩니다.

- 해당 Scenario를 사용하는 법인 : 각 법인의 수행 상태에 따라 Status를 표시합니다.
- 해당 Scenario를 사용하지 않는 법인 : Status를 'X'로 표시합니다.
- Region 내 전체 법인이 해당 Scenario를 사용하지 않는 경우 : 해당 Scenario는 표시되지 않습니다.
Type을 Region으로 선택한 후 Expand Company Code를 실행하면 하위 법인별 Status를 함께 확인할 수 있으며, 시나리오를 Assign하지 않은 법인에는 'X'가 표시됩니다. 해당 법인을 단독으로(Company Code로) 조회하면 그 시나리오는 조회되지 않습니다.

### 5.3.4 Currency 및 환율

- Type이 Region인 경우 Currency는 USD로 고정됩니다. Currency를 선택할 수 있는 것은 Type이 Company Code인 경우뿐입니다. 지역(Region)으로 조회하면 지역에 속한 법인들의 통화가 서로 다를 가능성이 높기 때문입니다.
- 이 프로그램에 적용되는 환율은 조회월 말일자 환율입니다.

### 5.3.5 Manual 시나리오의 Confirm

Manual 점검 항목(예: 가수금 - 발생일 기준 30일 초과 점검)은 Inspection Run으로 수행하더라도 Status가 변동되지 않으므로, 담당자가 직접 Confirm 처리해야 합니다. 하위 법인의 Manual 항목이 모두 Confirm되면 Region의 Status에도 반영됩니다. (4.6의 Need to Confirm 처리 방법 참조)

> 보완 설명 — 시스템 검증 내역<br>· ZLPAC5100(Financial Risk Validation Monitoring)은 프로그램과 트랜잭션 코드가 모두 시스템에 등록되어 있습니다. (패키지 ZPAC_CIS)<br>· ZLPAC5400(Financial Risk Validation Dashboard)은 신규 개발 프로그램으로 시스템에 프로그램으로 등록되어 있습니다. (패키지 ZPAC_CIS)<br>· ZLPAC5400 소스 확인 결과, 조회 Type 구분값은 R(Region) / C(Region + Company Code)로 정의되어 있으며, Business Package는 'FV'로 고정되어 조회됩니다. 조회 조건으로 기준월(SPMON), Currency Type, Region 범위, Company Code 범위, Scenario 범위를 사용합니다.

— 문서 끝 —
