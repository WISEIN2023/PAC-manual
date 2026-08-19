---
id: closing-schedule/06-change-closing-schedule-zlpac7170-zlpac7180
doc: closing-schedule
title: 6. Change Closing Schedule (ZLPAC7170 · ZLPAC7180)
parent: docs/closing-schedule/README.md
---

# 6. Change Closing Schedule (ZLPAC7170 · ZLPAC7180)

## 6.1 개요 및 조회

**화면명** Change Closing Schedule    **T-Code** ZLPAC7170

결산 마감 일정을 조회·변경하는 프로그램입니다. 일정 도래 전이라도 Open/Close가 가능하며, 회사코드별 배포된 Schedule ID와 현재 수행 상태를 확인할 수 있습니다.

- Time Control을 적용받는 Schedule ID(Control by Time Schedule이 체크된 경우)에 한해 배포 시간을 변경할 수 있다.
조회 조건으로 Company Code, Closing Schedule ID, Fiscal Year/Period를 입력합니다.

![closing-schedule 화면](../../assets/closing-schedule/img32.png)

[ZLPAC7170] Change Closing Schedule — 조회 조건

## 6.2 일정 상태 및 Open / Close

| 항목 | 설명 |
|---|---|
| ① Status | Open : 결산 일정이 수행되지 않은 상태<br>On Time Closed : 배포한 결산 일정에 맞게 자동으로 수행된 상태<br>Manual Closed : 사용자가 수작업으로 Close 처리한 상태 (Monitoring Dashboard에서 node를 직접 실행) |
| ② Open / Close | Status에 따라 수행 여부를 아이콘으로 표시. 자물쇠 아이콘을 클릭하여 수작업 Open/Close 가능<br>Time Control이 설정되지 않은 Schedule은 Open/Close만 가능 |
| ③ Schedule ID | 모델링되어 배포까지 완료된 Schedule ID만 조회됨<br>Schedule ID 더블 클릭 시 Define Schedule ID 화면으로 이동 |
| ④ Schedule Simulation | 결산 일정이 Open되어 있는지 확인 (Open인 경우 메시지: All schedules are open)<br>모든 필드가 입력되어야 Simulation 가능 |

![closing-schedule 화면](../../assets/closing-schedule/img33.png)

[ZLPAC7170] 일정 상태(Open / On Time Closed) 및 Open/Close · Changeable? · Approval Status

![closing-schedule 화면](../../assets/closing-schedule/img34.png)

Schedule Simulation — 결산 일정 Open 여부 확인

## 6.3 변경 가능 여부 · 결재 · 변경 이력

| 항목 | 설명 |
|---|---|
| ① Changeable? | 변경 가능한 Schedule이면 ‘Yes’, 불가하면 ‘No’<br>Time Control이 설정되지 않은 Schedule은 ‘No’ |
| ② Approval Status | 결재 상태를 표시<br>Time Control이 설정되지 않은 Schedule은 공란 |
| ③ History Display | Schedule Change Type 및 변경 내용 확인. 조회 기간의 Schedule ID에 해당하는 변경이력·마감수행이력 표시<br>Schedule Change로 일정을 수정한 경우 기존/변경 후 날짜·시간, 승인 상태, 결재 본문, 요청자 정보 등 상세 이력 확인 가능 |
| ④ Schedule Change | 일정 변경을 하고 싶은 경우 선택 (상세 화면 ZLPAC7180으로 이동)<br>Time Control이 선택된 Schedule에 대해서만 변경 가능 |

![closing-schedule 화면](../../assets/closing-schedule/img35.png)

Display Closing Schedule Change History — 변경 유형 및 이력

> 시스템 확인 — Change Closing Schedule<br>ZLPAC7170(Change Closing Schedule)·ZLPAC7180(Change Closing Schedule Detail)은 모두 시스템에 등록되어 있습니다. 일정 계획은 ZTPAC_SCH_PLAN 테이블을 기준으로 조회·변경되며, 변경 시 결재 상태는 워크플로우 상태(WFSTATUS)로 관리됩니다.

## 6.4 결산 일정 변경 상세 (ZLPAC7180)

**화면명** Change Closing Schedule Detail    **T-Code** ZLPAC7180

| 항목 | 설명 |
|---|---|
| ① Date / Time after Change | 변경할 날짜와 시간을 입력<br>과거 날짜/시간으로는 변경 불가<br>Final Schedule로 지정된 Schedule의 날짜/시간보다 경과한 날짜/시간으로는 변경 불가 |
| ② Reason for Change | 변경 사유 입력 (필수 필드) |

![closing-schedule 화면](../../assets/closing-schedule/img36.png)

[ZLPAC7180] Change Closing Schedule Detail — 변경 날짜/시간 및 사유 입력
