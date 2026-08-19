---
id: closing-schedule/04-schedule-distribute-zlpac7100
doc: closing-schedule
title: 4. Schedule Distribute (ZLPAC7100)
parent: docs/closing-schedule/README.md
---

# 4. Schedule Distribute (ZLPAC7100)

## 4.1 개요

**화면명** Distribute Closing Schedule    **T-Code** ZLPAC7100

Define Schedule ID에서 세분화된 통제 항목을 정의했다면, Distribute Closing Schedule에서는 결산 조직별 일정 계획을 실제로 배포하고 공지합니다.

- 월별로 결산 일정의 일자/시간을 설정하여 조직별 시간대에 맞춰 배포한다.
- 최종 배포 전에는 특정 조직의 결산 일정에 대해 일자/시간 변경이 가능하다.
- 기존 배포된 월을 실행하여 현재 배포 상태를 확인할 수 있다.

## 4.2 조회 및 Closing Calendar 연계

| 항목 | 설명 |
|---|---|
| ① 조회 조건 | 결산 일정을 배포할 회계연도/월을 입력 후 조회 |
| ② 오류 메시지 | 입력한 회계연도/월이 Closing Calendar에 미등록된 경우 오류 메시지 발생 |
| ③ Closing Calendar | 실제 월별 결산 일자를 지정하는 프로그램(ZLPAC7030)<br>Calendar 누락 시 ②의 오류가 발생하며 배포 불가하므로 일자 지정 필수 |

![closing-schedule 화면](../../assets/closing-schedule/img19.png)

[ZLPAC7100] 회계연도/월 조회 — Closing Calendar 미등록 시 오류 메시지

## 4.3 일정 배포 Status 흐름

일정 배포는 단계별 Status로 관리되며, 다음 순서로 변경됩니다.

**New → Saved → Planning Saved → Planning Confirmed → Distributed**

> 시스템 확인 — 배포 Status 값<br>배포 Status는 배포 마스터(ZTPAC_SCH_DISTM)의 STATUS 필드로 관리되며, 시스템에 등록된 값은 다음과 같습니다.<br>(공백) = New, S = Saved, T = Planning Saved, P = Planning Confirmed, D = Distributed, L = Distributed (Lock), R = Reschedule Saved<br>최종 배포가 완료되면 Planning Confirmed → Distributed (Lock) 상태로 전환됩니다.

## 4.4 단계별 상세 동작

### 4.4.1 Status : New

Closing Calendar에서 날짜를 지정한 뒤 신규로 Closing Schedule을 배포하려 할 때 가장 처음 나타나는 화면으로, Status가 New로 표시됩니다.

| 항목 | 설명 |
|---|---|
| ① Plan Date, Plan Time | 각 Schedule ID에 등록된 Day/Time을 기준으로 Closing Calendar에 입력된 날짜로 변환된 계획일이며, 수정 가능 |
| ② Without Time Control | Schedule ID 리스트 중 시간에 의해 통제받지 않는 리스트를 표시<br>결산 순서가 도래하면 자동으로 수행될 Schedule |
| ③ Save | Save 버튼을 클릭하여 저장 |

![closing-schedule 화면](../../assets/closing-schedule/img20.png)

Status : New — Global Schedule 및 Without Time Control 표시

### 4.4.2 Status : Saved

New에서 Save하면 Status가 Saved로 변경됩니다.

| 항목 | 설명 |
|---|---|
| ① Status | New → Saved로 변경된 상태 |
| ② Create Schedule | Saved된 계획 일정으로 각 법인별 결산 일정을 생성<br>Plan Date/Time 수정도 가능 |
| ③ Reset all Changes | 입력한 모든 변경사항을 초기화<br>Status가 New 상태로 변경됨 |

![closing-schedule 화면](../../assets/closing-schedule/img21.png)

Status : Saved — Create Schedule / Reset all changes 버튼

### 4.4.3 Status : Planning Saved

Create Schedule을 수행하면 Status가 Planning Saved로 변경되고, 각 법인별 Schedule ID에 등록된 Time Rule이 적용된 리스트가 하단에 표시됩니다.

| 항목 | 설명 |
|---|---|
| ① Status | Saved → Planning Saved로 변경된 상태. 법인별 Time Rule 적용 리스트가 하단에 표시됨 |
| ② Plan Confirm | Saved된 계획 일정으로 결산 일정을 생성(확정) |
| ③ Change By HQ Time /
Change By Local Time | 선택에 따라 Plan Date/Plan Time 필드가 활성화되어 수정 가능<br>Time Rule이 HQ인 Schedule ID는 Local Time을 변경해도 HQ 일정으로 배포되므로, 적용되는 Time Rule에 해당하는 Plan Date/Time을 변경해야 함<br>Time Rule HQ → Change By HQ Time 클릭 → Plan Date(HQ) 변경<br>Time Rule Local → Change By Local Time 클릭 → Plan Date(Local) 변경 |

> 주의<br>이 단계에서 Confirm한 후에는 더 이상 수정이 불가합니다. 수정이 필요하면 다음 단계(Planning Confirmed)의 Re-Planning을 사용해야 합니다.

![closing-schedule 화면](../../assets/closing-schedule/img22.png)

Status : Planning Saved — 법인별 Plan Date/Time (HQ·Local) 표시

![closing-schedule 화면](../../assets/closing-schedule/img23.png)

Change By HQ Time / Change By Local Time 선택

![closing-schedule 화면](../../assets/closing-schedule/img24.png)

Without Time Schedule — 시간 통제 없이 순서로 수행되는 일정

### 4.4.4 Status : Planning Confirmed

Plan Confirm을 수행하면 Status가 Planning Confirmed로 변경됩니다.

| 항목 | 설명 |
|---|---|
| ① Status | Planning Saved → Planning Confirmed로 변경 |
| ② Display Schedule Plan | 확정한 법인별·Schedule ID별 Plan Date/Plan Time을 확인하는 화면으로 이동 |
| ③ Distribute | 배포 버튼을 클릭하면 최종 결산 일정 배포가 완료되며, 계획한 일자에 일정이 수행됨 |
| ④ Re-Planning | 배포한 일정의 수정이 필요한 경우 클릭하여 Schedule Plan을 수정한 뒤 다시 Plan Confirm → Distribute |

> 주의<br>Re-Planning / Reschedule 시 기존 결산 이력은 모두 Reset되므로 주의가 필요합니다.

![closing-schedule 화면](../../assets/closing-schedule/img25.png)

Status : Planning Confirmed — Display Schedule Plan / Distribute / Re-Planning

![closing-schedule 화면](../../assets/closing-schedule/img26.png)

Distribute 실행 시 확인 팝업

### 4.4.5 Status : Distributed

Distribute를 수행하면 최종 배포가 완료되어 Status가 Distributed (Lock)으로 변경됩니다.

| 항목 | 설명 |
|---|---|
| ① Status | Planning Confirmed → Distributed (Lock)으로 변경 |
| ② Send Mail | Closing Participant, Inspection Reviewer, 추가 지정 사용자에게 결산 배포 일정 메일을 실시간 발송 |

![closing-schedule 화면](../../assets/closing-schedule/img27.png)

Status : Distributed (Lock) — Unlock / Display Schedule Plan / Send Mail

## 4.5 일정 배포 메일링

결산 일정 배포 후 관련 담당자에게 실시간으로 메일을 발송할 수 있습니다.

| 항목 | 설명 |
|---|---|
| ① Receiver (By Company) Selection | Closing Participant, Inspection Reviewer, Add Receiver(w. HQ Time)를 지정하여 원하는 사용자에게 발송 |
| ② Add Receiver | Closing Participant·Inspection Reviewer 이외에 메일을 보낼 사용자를 직접 등록하여 추가 |
| ③ 메일 작성 | 메일 내용 작성 및 첨부파일 추가 |
| ④ Save | 단순히 내역을 저장할 경우 사용 |
| ⑤ Preview | 메일 내용 미리보기<br>Schedule List에는 Schedule Type이 Closing Schedule인 Schedule ID가 모두 포함됨<br>그 외 Schedule Type은 정의 시 ‘Include mailing when schedule distribution’을 체크한 Schedule ID만 포함됨<br>Preview 내용은 본사 기준으로 확인 가능함 |
| ⑥ Send | Send 버튼 클릭 시 메일 발송 |

![closing-schedule 화면](../../assets/closing-schedule/img28.png)

[ZLPAC7100] 일정 배포 메일 — 수신자 선택 / Comment / 첨부

![closing-schedule 화면](../../assets/closing-schedule/img29.png)

Add Receiver — 추가 수신자 등록

![closing-schedule 화면](../../assets/closing-schedule/img30.png)

Preview — 메일 미리보기 (Closing Info / Schedule List / Closing Guide)
