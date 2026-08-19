---
id: closing-inspection/02-closing-inspection-category-zlpac5050
doc: closing-inspection
title: 2. Closing Inspection Category (ZLPAC5050)
parent: docs/closing-inspection/README.md
---

# 2. Closing Inspection Category (ZLPAC5050)

## 2.1 초기 화면 — Category 조회

| 화면명 | Define Closing Inspection Category | T-Code | ZLPAC5050 |
|---|---|---|---|
| 설명 | 결산점검 Category 초기 화면 |  |  |

Activity Master(ZLPAC0020)에서 Activity Type이 I(Closing Inspection)인 경우, 점검 항목을 정의하기 위해 Inspection Category를 세팅합니다. 이 화면에서 Category를 생성 · 변경 · 삭제할 수 있습니다.

- ① 생성된 Category는 Activity Master의 Inspection Category에 매핑하여 사용됩니다.
- ② Business Package : 조회할 Business Package를 입력한 후 Search 버튼을 클릭하면 기 생성된 Category List를 확인할 수 있습니다.

## 2.2 Category 수정 · 조회 · 삭제

| 화면명 | Define Closing Inspection Category | T-Code | ZLPAC5050 |
|---|---|---|---|
| 설명 | 기 생성된 Category 수정 · 조회 · 삭제 |  |  |

조회된 목록에서 Category ID를 클릭하면 해당 Category의 정보를 확인할 수 있습니다.

- ① Change / Display / Delete : 수정 / 조회 / 삭제 모드를 전환합니다.
- Business Package와 Category ID는 최초 생성 후에는 변경할 수 없습니다.

## 2.3 Category 신규 생성

| 화면명 | Define Closing Inspection Category | T-Code | ZLPAC5050 |
|---|---|---|---|
| 설명 | Category 신규 생성 및 기본 정보 입력 |  |  |

**① New 버튼으로 Category를 생성하고 다음 정보를 입력합니다.**

- Business Package 선택
- SeqNo : 기존 Seq. +1로 자동 채번됩니다. (변경 가능)
- Category ID / Category Name / Category Info 입력
**② InspectionType :점검 유형을 선택합니다.**

| 값 | 유형 | 설명 |
|---|---|---|
| S | Simulation Run | 실제 결산에서 수행할 Activity를 미리 수행해 보고 이상이 있는지 체크해야 할 경우 선택 |
| C | Closing Inspection | Simulation Run 이외의 일반 결산점검 항목일 경우 선택 |
| R | Financial Risk Validation | 재무 위험 검증 항목일 경우 선택 |

> 보완 설명 — Inspection Type 코드값 (시스템 검증)<br>Inspection Type은 데이터 사전 도메인 ZPAC_CIS_TYPE(Closing Inspection Type)으로 관리되며, 시스템에 정의된 고정값은 S(Simulation Run), C(Closing Inspection), R(Financial Risk Validation) 3가지입니다.<br>Closing Inspection Monitoring(ZLPAC5200)에서는 Inspection Type이 C로 정의된 Category만 조회 대상이 됩니다. (4.2 참조)

## 2.4 Inspection Setting / Mailing & To-Do

| 화면명 | Define Closing Inspection Category | T-Code | ZLPAC5050 |
|---|---|---|---|
| 설명 | Category 속성(Inspection Setting, Mailing & To-Do) 입력 |  |  |

**① Inspection Setting**

| 항목 | 설명 |
|---|---|
| Save each Scenario detail data | Simulation Run 수행 후 Detail Table(세부사항)을 저장할 것인지 결정합니다. |
| Complete Check | 전체 Complete 체크. 수행하지 않고 넘어가거나, 에러가 발생하더라도 무시하고 넘기고 싶은 경우 Complete 버튼을 눌러 넘어가도록 합니다. 체크만 하면 저장되지 않으므로 반드시 Complete + Start를 함께 수행해야 합니다. |
| External Sequence | Closing Inspection Scenario(ZLPAC5060)에서 시나리오 생성 시 Seq.가 자동 채번되는데, 기존에 사용했던 Seq.를 사용하기 위해 직접 입력하도록 허용하는 옵션입니다. |

**② Mailing & To-Do**

- Mailing Active : Mailing 기능의 활성화 여부를 체크합니다.
- To-Do Active : To-Do 기능의 활성화 여부를 체크합니다.

## 2.5 Organization ID Setting (Inspection Type R)

| 화면명 | Define Closing Inspection Category | T-Code | ZLPAC5050 |
|---|---|---|---|
| 설명 | Inspection Type이 R(Financial Risk Validation)일 때 Organization ID 설정 |  |  |

**① Inspection Type이 R일 때는 Organization ID Setting 항목을 추가로 입력합니다.**

- Organization ID Active for Scenario / Organization Name
- Field / Data Element / Table / Search Help
**② 입력 완료 후 Save 버튼으로 저장합니다.**

> 보완 설명 — Organization ID Setting 저장 위치 (시스템 검증)<br>Organization ID Setting 입력값은 Category Master 테이블 ZTPAC_CIS_CID의 조직 관련 필드(XORG: 활성화 여부, CORG_TEXT: Organization Name, OFIELD: Field, ODOMAIN: Data Element, DBTABNAME: Table, SHMA_VAL: Search Help)에 저장됩니다.
