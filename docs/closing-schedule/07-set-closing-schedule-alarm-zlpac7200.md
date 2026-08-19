---
id: closing-schedule/07-set-closing-schedule-alarm-zlpac7200
doc: closing-schedule
title: 7. Set Closing Schedule Alarm (ZLPAC7200)
parent: docs/closing-schedule/README.md
---

# 7. Set Closing Schedule Alarm (ZLPAC7200)

## 7.1 개요

**화면명** Set Closing Schedule Alarm    **T-Code** ZLPAC7200

결산 일정이 도래하기 전에, 결산 일정별로 등록된 사용자에게 알람을 발송하도록 설정하는 프로그램입니다.

- 알람이 등록된 경우 기본적으로 결산 일정 배포 시점에 스케줄링된다.
- 배포 시점 이후 추가되는 알람은, 추가 시점을 기준으로 가장 최근 배포된 연월의 Closing Schedule이 경과하지 않은 경우에만 스케줄링된다.
- 모델링되어 있는 Company Code, Schedule ID에 대해서만 등록 가능하다.
- Closing Schedule Alarm은 ‘시간에 의한 통제를 받는 결산 일정’에 대해서만 설정할 수 있다.

> 주의<br>등록하려는 Schedule이 해당 법인에 모델링되어 있지 않은 경우 등록이 불가합니다. (예: ‘TREASURY’ is not a schedule assigned to ‘ZA01’.)

## 7.2 알람 등록

| 항목 | 설명 |
|---|---|
| ① Active / Inactive / Disable | 조회 시 체크한 내역만 표시되며, 기본값은 ‘Active’만 체크됨<br>Disable : 기존 등록 Schedule이 모델링 목록에서 해제되는 경우 ‘Disable’로 분류되며 알람 발송 불가 |
| ② Company code, Schedule ID | 등록하려는 Company Code, Schedule ID 입력 (필수)<br>정상 Schedule ID 입력 시 해당 Schedule의 이름·Day·Time Rule이 표기됨 |
| ③ Alarm (Hour Before) | 몇 시간 전에 알람을 받을지 설정 (1~9)<br>예: ‘3’으로 설정 시 해당 법인 해당 스케줄의 결산 일정 3시간 전에 알람 발송 |
| ④ Receiver | 알람 수신자 설정 (알람 등록 시 필수) |
| ⑤ Planned Start Date / Time | 해당 스케줄의 알람 예정 날짜/시간<br>현재 계획된 알람이 있는 경우에만 표시되며, 없으면 공란 |
| ⑥ History | 해당 알람이 등록된 이후 발송된 내역이 있는 경우 확인 가능 |
| ⑦ Inactive | 체크된 경우 알람 발송 불가 |

> 시스템 확인 — Alarm 저장 및 스케줄링<br>알람 등록 내역은 테이블 ZTPAC_SCH_ALARM(Set Closing Schedule Alarm)에 저장됩니다. 알람 시간은 SCH_ALARM 필드(CHAR 1자리)로, 단일 숫자(1~9)를 보관하며 범위는 프로그램에서 제어됩니다.<br>알람 상태(ASTATUS)의 시스템 등록값은 S = Saved, A = Active, Z = Inactive입니다. ‘Disable’은 모델링에서 해제된 Schedule을 가리키는 분류입니다.<br>알람은 SAP 백그라운드 잡(Background Job)으로 스케줄링되어 예정 시각에 발송됩니다.

![closing-schedule 화면](../../assets/closing-schedule/img37.png)

[ZLPAC7200] Set Closing Schedule Alarm — 알람 등록 화면

![closing-schedule 화면](../../assets/closing-schedule/img38.png)

모델링되지 않은 Schedule 등록 시 오류 메시지

![closing-schedule 화면](../../assets/closing-schedule/img39.png)

Set Alarm History — 알람 발송 이력(Background Job)

## 7.3 Receiver 설정

알람 메일 수신자를 설정하는 화면으로, Receiver Selection 선택에 따라 수신자가 달라집니다. 알람 등록을 위해 Receiver Selection을 최소 1개 이상 선택해야 합니다.

| 항목 | 설명 |
|---|---|
| ① From Activity Participants | 회사코드에 등록된 Controller, Participant를 리시버로 설정 |
| ② Set Department | 특정 부서별 리시버 설정. 부서코드 설정 시 부서에 등록된 인원 전부에게 발송 |
| ③ Add Receiver | ①, ② 이외 특정 사용자를 리시버로 설정 |
| ④ Receiver List | 선택한 Receiver Selection에 따라 설정된 리시버 리스트를 확인 |

![closing-schedule 화면](../../assets/closing-schedule/img40.png)

Maintain Closing Schedule Alarm Receiver — Receiver Selection

![closing-schedule 화면](../../assets/closing-schedule/img41.png)

Closing Schedule Alarm Receiver List — 수신자 리스트
