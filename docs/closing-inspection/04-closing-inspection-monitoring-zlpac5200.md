---
id: closing-inspection/04-closing-inspection-monitoring-zlpac5200
doc: closing-inspection
title: 4. Closing Inspection Monitoring (ZLPAC5200)
parent: docs/closing-inspection/README.md
---

# 4. Closing Inspection Monitoring (ZLPAC5200)

## 4.1 실행 경로

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | Inspection Run — 실행 경로 |  |  |

Closing Inspection Monitoring은 다음 두 가지 경로로 실행할 수 있습니다.

- Monitoring Dashboard(Finance Closing) → Activity Group(Closing Pre-Inspection) → Activity(Pre-Check General) 노드를 통해 실행
- 메뉴트리에서 T-Code ZLPAC5200을 직접 실행
메뉴트리를 통해 접근하는 경우에만 Selection Screen을 통해 조회 조건을 입력하며, Monitoring Dashboard에서 접근하는 경우에는 Dashboard에서 조회한 회사코드와 월을 적용하여 조회 결과만 표시됩니다.

## 4.2 결산점검 조회

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | 결산점검 조회 — Selection Screen |  |  |

결산 항목 중 점검 항목에 대해 별도 시나리오를 정의하여 점검할 수 있으며, Inspection Type이 C(Closing Inspection)로 정의된 Closing Inspection Category만 조회할 수 있습니다. 조회 결과로는 해당 Category에 정의된 결산점검 시나리오가 조회됩니다.

- ① Business Package (필수 필드) : 조회할 Business Package를 선택합니다.
- ② Closing Inspection Category : Business Package별로 정의된 점검 카테고리를 선택합니다.
- ③ Company Code, Fiscal Year, Period : 조회할 회사코드와 결산 기간을 입력합니다.

> 사전 수행 항목<br>ZLPAC5060(Maintain Closing Inspection Scenario)에서 결산점검 시나리오가 먼저 등록되어 있어야 합니다.

## 4.3 조회 결과 화면

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | 결산점검 조회 결과 화면의 주요 항목 |  |  |

| 항목 | 설명 |
|---|---|
| ① Scenario | 결산점검으로 수행할 시나리오. 시나리오 수행 결과가 아이콘으로 표시됩니다. |
| ② Confirm | 시나리오 수행 여부와 관계없이 Confirm 체크박스를 선택하여 Manual로 점검 완료 처리할 수 있습니다. 단, Confirm Enable 속성에 따라 체크박스 활성화 여부가 결정되며, Need To Re-run으로 정의된 시나리오는 반드시 재수행을 통해 Success 되어야 점검 완료가 가능합니다. |
| ③ Count | 시나리오 점검 항목에 해당하는 레코드 개수가 표시됩니다. |
| ④ Result | 수행 결과를 확인할 수 있도록 구성한 시나리오의 경우, Result 필드의 아이콘을 클릭하여 결과 항목을 확인합니다. |
| ⑤ Finish Time | Inspection Run을 수행한 시점이 표시되며, Confirm 체크 시 해당 시점으로 업데이트됩니다. |

## 4.4 결산점검 수행 (Inspection Run)

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | Inspection Run — 시나리오 선택 및 실행 |  |  |

전체 시나리오 또는 원하는 시나리오만 선택하여 점검을 수행할 수 있습니다.

- ① Inspection Run 버튼 클릭 : 원하는 시나리오의 점검을 위해 버튼을 클릭하면 팝업이 실행됩니다.
- ② Selected Scenario 선택 : 조회된 리스트에서 특정 상태의 시나리오만 필터링하여 실행할 수 있습니다.
- ③ Inspection Run 수행될 시나리오 리스트 확인 : Monitoring 화면에서 조회한 시나리오가 표시되며, 해당 리스트에 표시된 항목 전체가 실행됩니다.
- ④ Exclude Scenario : 원하는 시나리오를 선택한 후 Exclude Scenario를 선택하면, 선택된 시나리오는 화면에서 삭제되고 그 외 나머지 시나리오만 화면에 출력됩니다. Run을 수행하면 화면에 남은 시나리오만 수행됩니다.
- ⑤ Set Scenario : 원하는 시나리오를 선택(단건 또는 다건)하면 선택된 시나리오 외의 시나리오는 화면에서 삭제되고, Run을 수행하면 화면에 남은 시나리오만 수행됩니다.
- ⑥ Run : 수행하고자 하는 시나리오 리스트를 실행합니다.

## 4.5 Job Status 확인 및 강제 종료

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | 수행 중인 Job Status 확인 |  |  |

결산점검 수행 화면에서 현재 수행 중인 Job Status를 확인할 수 있으며, 점검 중인 시나리오가 존재할 경우 Run 버튼은 비활성화됩니다.

- ① Job Status : 현재 점검 중인 시나리오가 있는 경우 리스트를 확인할 수 있습니다.
- ② Control - Stop : 버튼을 클릭하여 수행 중인 작업을 강제로 종료할 수 있습니다.

## 4.6 수행 결과 조회 — 상태별 시나리오 조회

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | 결산점검 수행 결과를 상태 기준으로 필터링하여 확인 |  |  |

Inspection Run을 수행한 후, 결산점검 수행 결과를 성공 · 실패 등 상태를 기준으로 필터링하여 확인할 수 있습니다.

| 상태 필터 | 설명 |
|---|---|
| ① 전체 | 전체 리스트를 표시합니다. |
| ② Failed | 점검 대상 항목이 존재하는 경우, 점검 대상 항목을 확인한 후 재수행 또는 Confirm 처리합니다. |
| ③ Success | 점검이 정상적으로 완료된 시나리오입니다. |
| ④ Confirm | Confirm 처리가 완료된 시나리오입니다. |
| ⑤ Need to Confirm | Manual 점검 항목인 경우 Inspection Run으로 수행하더라도 Status가 변동되지 않으므로 Need to Confirm 아이콘으로 별도 표시됩니다. Result 필드의 아이콘을 클릭한 후 Execute Program 버튼을 통해 연결된 프로그램을 수행하여 담당자가 Manual로 확인합니다. |
| ⑥ System Fail | 시나리오 수행 시 시스템 에러로 실행에 실패한 상태입니다. Review에 표시되는 아이콘을 클릭하여 시나리오 수행 Log를 확인할 수 있습니다. (Log는 프로그램에서 제공한 경우에만 표시됩니다.) |
| ⑦ Not Executed | 아직 수행되지 않은 시나리오입니다. |
| ⑧ Refresh | Inspection Run 수행 시 10초마다 자동 Refresh되며, 이와 별도로 Refresh 버튼을 통해 시나리오 실행 상태를 업데이트할 수 있습니다. |

## 4.7 수행 결과 조회 — Confirm 처리

| 화면명 | Closing Inspection Monitoring | T-Code | ZLPAC5200 |
|---|---|---|---|
| 설명 | 결산점검 수행 결과 — Confirm 일괄 처리 |  |  |

점검 수행 후, 특정 시나리오에 대해서는 Confirm 체크박스를 통해 점검자의 확인 처리가 가능합니다.

- ① All Check 버튼 클릭 : Confirm 수행이 필요한 시나리오들을 일괄 Confirm 처리합니다.
- ② Confirm 일괄 체크 : 개별 체크 없이 한 번에 Confirm이 체크됩니다.
