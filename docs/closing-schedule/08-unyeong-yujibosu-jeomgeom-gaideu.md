---
id: closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu
doc: closing-schedule
title: 8. 운영 · 유지보수 점검 가이드
parent: docs/closing-schedule/README.md
---

# 8. 운영 · 유지보수 점검 가이드

결산일정 관련 이상이 보고될 때, 아래 순서로 점검하면 원인 범위를 빠르게 좁힐 수 있습니다.

## 8.1 정상 동작 확인 체크리스트

| 점검 항목 | 확인 방법 | 정상 기준 |
|---|---|---|
| 프로그램/트랜잭션 존재 | SE93/SE38에서 ZLPAC7010·7030·7100·7160·7170·7180·7200 조회 | 프로그램·트랜잭션이 모두 존재 (패키지 ZPAC) |
| Calendar 등록 | ZLPAC7030에서 배포 대상 연·월 조회 | 해당 월의 Day에 결산 일자가 지정됨 |
| 조직 배정 | ZLPAC7020에서 대상 조직 조회 | Schedule ID가 Assigned Schedule로 표시됨 |
| 배포 상태 | ZLPAC7100에서 해당 연·월 실행 | Status가 의도한 단계(예: Distributed/Lock) |
| 알람 스케줄 | ZLPAC7200에서 알람 History 확인 | Background Job이 예정 시각에 스케줄링/발송됨 |

## 8.2 증상별 점검 가이드

| 증상 | 우선 점검 사항 |
|---|---|
| 특정 월의 일정 배포가 불가 / 오류 | ZLPAC7030에서 해당 회계연도·월의 Calendar(결산 일자) 지정 여부 확인 (미등록 시 배포 불가) |
| 특정 조직만 일정이 보이지 않음 | ZLPAC7020에서 해당 조직에 Schedule ID 배정 여부 확인<br>Config의 Organization Type(M/S)과 Schedule ID의 Assign Level(B/O)이 의도와 일치하는지 확인 |
| 시간이 지나도 자동 통제가 안 됨 | Schedule ID의 Control by Time Schedule(XTIME_CNTR) 체크 여부 확인<br>Distribute 구간의 Day/Time 입력 여부 확인 |
| 배포 일정 수정 불가 | Status가 Planning Confirmed 이상인지 확인. 확정 후에는 Re-Planning으로만 수정 가능 (기존 이력 Reset 주의) |
| 일정을 변경하려는데 ‘No’로 표시 | 해당 Schedule ID가 Time Control(Control by Time Schedule) 대상인지 확인. Time Control 미설정 Schedule은 Changeable? = No |
| Posting Block인데 특정 사용자 기표 필요 | ZLPAC7160에서 전표 생성/승인 시점 사용자를 G/L·조직·기간과 함께 Super User로 등록 (Valid to Date/Time 확인) |
| Legacy 인터페이스가 호출되지 않음 (LG) | 해당 Schedule의 LEGIF='X' 여부, ZLPACEXIT(Exit Group SCH_IF)에 Exit Function 등록 여부, 인터페이스 API 연결 상태 확인 |
| 알람이 발송되지 않음 | 대상 Schedule이 ‘시간에 의한 통제’ 대상이며 해당 법인에 모델링되어 있는지 확인<br>알람 상태가 Active이며 Inactive 체크가 아닌지, Receiver가 1개 이상 설정되어 있는지 확인<br>ZLPAC7200 History에서 Background Job 스케줄/실행 상태 확인 |
