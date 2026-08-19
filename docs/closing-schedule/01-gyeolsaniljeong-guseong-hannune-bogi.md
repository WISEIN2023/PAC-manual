---
id: closing-schedule/01-gyeolsaniljeong-guseong-hannune-bogi
doc: closing-schedule
title: 1. 결산일정 구성 한눈에 보기
parent: docs/closing-schedule/README.md
---

# 1. 결산일정 구성 한눈에 보기

결산일정(Closing Schedule)은 결산 작업을 ‘언제, 어떤 순서로, 어떤 조직에서’ 수행할지를 정의·배포하고, 수행 상태를 관리·통제하는 PAC의 핵심 영역입니다. 결산일정은 정의 → 캘린더 → 배포의 순서로 준비되며, 운영 중에는 예외 처리(Super User), 일정 변경, 알람 설정 기능으로 보완됩니다.

## 1.1 결산일정 관련 프로그램

| T-Code | 화면명 | 역할 |
|---|---|---|
| ZLPAC7010 | Define Schedule ID | 통제가 필요한 업무별 Schedule ID와 통제 항목(시간/순서/Factor/조직)을 정의 |
| ZLPAC7030 | Monthly Closing Calendar Control | 결산 일정 배포에 사용할 월별 결산 일자(Calendar)를 지정 |
| ZLPAC7100 | Distribute Closing Schedule | 조직별 결산 일정을 생성·확정·배포하고 메일 공지 |
| ZLPAC7160 | Posting Super User Registration | Posting Block 상태에서 예외적으로 기표를 허용할 Super User를 등록 |
| ZLPAC7170 | Change Closing Schedule | 배포된 결산 일정을 조회하고 Open/Close 및 일정(시간)을 변경 |
| ZLPAC7180 | Change Closing Schedule Detail | 일정 변경 상세 — 변경 날짜/시간 입력 및 변경 사유 등록 |
| ZLPAC7200 | Set Closing Schedule Alarm | 결산 일정 도래 전 지정 사용자에게 알람을 발송하도록 설정 |

아래 프로그램은 결산일정 정의 과정에서 함께 참조됩니다.

| T-Code | 화면명 | 참조 위치 |
|---|---|---|
| ZLPAC7000 | Maintain Closing Schedule Config | Organization Type 등 공통 설정 관리 (Organization Assign 탭 활성화 결정) |
| ZLPAC7020 | Assign Schedule to Organization | Schedule ID를 Business Type 또는 조직 단위로 배정 |
| ZLPAC0020 | Define Activity Master | Schedule ID를 Activity Type C(Closing Schedule)에 매핑 |
| ZLPACEXIT | Maintain PAC User Exit | 스케줄 인터페이스 등 User Exit(Exit Function)을 등록·관리 (2.7 참조) |

> 시스템 확인 — SAP Repository<br>본 매뉴얼에 등장하는 프로그램은 운영 대상 시스템에 프로그램(Report) 및 트랜잭션으로 모두 등록되어 있으며, 모두 개발 패키지 ZPAC에 속합니다. 각 화면명(설명)은 시스템에 등록된 명칭과 일치합니다.<br>참고: ZLPAC7160의 프로그램 명칭은 ‘Super User Registration’, 트랜잭션 명칭은 ‘Posting Super User Registration’입니다.

## 1.2 결산일정 처리 흐름

결산일정은 다음 순서로 준비·운영됩니다. 앞 단계가 누락되면 다음 단계로 진행할 수 없습니다.

- ① Define Schedule ID (ZLPAC7010) — 통제할 업무 단위와 통제 방식(시간/순서/Factor)을 정의.
- ② Monthly Closing Calendar (ZLPAC7030) — 배포 대상 연·월의 결산 일자를 지정.
- ③ Schedule Distribute (ZLPAC7100) — 조직별 일정을 생성·확정·배포하고 메일을 공지.
- ④ (운영) Super User 등록(ZLPAC7160) · 일정 변경(ZLPAC7170/7180) · 알람 설정(ZLPAC7200)으로 예외 및 변경을 처리.

> 핵심 포인트<br>Calendar(②)가 지정되지 않은 연·월은 일정 배포(③)가 불가능합니다. 배포 시 ‘Calendar 미등록’ 오류가 발생하므로, 배포 전 해당 월의 Calendar 지정 여부를 먼저 확인해야 합니다.
