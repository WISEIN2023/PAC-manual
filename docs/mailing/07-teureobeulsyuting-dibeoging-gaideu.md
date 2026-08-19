---
id: mailing/07-teureobeulsyuting-dibeoging-gaideu
doc: mailing
title: 7. 트러블슈팅 & 디버깅 가이드
parent: docs/mailing/README.md
---

# 7. 트러블슈팅 & 디버깅 가이드

## 7.1 문의 대응 케이스

| 증상 | 점검 순서 / 원인 | 확인 위치 |
|---|---|---|
| 메일이 안 왔다 | ① PAC 로그에 발송기록 있나? 없으면 수신자/트리거 문제 → ② 있으면 SOST 상태(대기/오류/완료) 확인 | PAC 로그 → SOST |
| 특정 사람만 못 받는다 | 플래그(XMAIL_*) 체크 여부, 이메일(SMTP_ADDR) 존재, 삭제플래그(LOEVM), 대상 PID 등록 확인 | SE16N: ZTPAC_PROC_AUTH |
| 수동준비 메일이 에러 받는 사람한테만 | 수동준비가 XMAIL_ERR로 수신자 조회(현재 사양). 의도와 다르면 개발팀 확인 | 3.3절 주의 |
| 완료 메일이 안 온다 | ZLPACSYS의 XMAIL_COM ON 여부, ZTPAC_PROC_AUTH의 XMAIL_COM='X', Activity가 실제 완료(C)인지 | ZLPACSYS / SE16N |
| 본문에 $필드$가 그대로 나온다 | HTML 마커가 발송 메서드 전달 필드와 불일치. 철자/대소문자 확인 | ZLPAC_HTML / 6장 |
| 알람 메일이 안 온다 | ZTPAC_SCH_ALARM(ASTATUS='A')·N시간, 일정 배포 여부, SM37의 ZLPAC7210 잡 상태, 수신자 존재 | SE16N / SM37 |
| CIS 메일이 안 간다 | ZTPAC_CIS_CID의 XMAIL='X', 담당자 등록, ZTPACEXIT 트리거 설정 | SE16N |
| 메신저가 안 온다 | 메신저 발송 기능은 현재 미구현(플래그 XMSGR_*만 선택 가능). 고객사 요청 시 인터페이스 CSP 로직 개발 필요 | SE16N: ZTPAC_PROC_AUTH(XMSGR_*) |

## 7.2 디버깅 포인트 (중단점 위치)

문제 원인을 코드 레벨에서 확인해야 할 때, 아래 위치에 중단점(Breakpoint)을 걸어 값을 확인합니다. 디버깅은 개발/품질 시스템에서 수행하는 것을 원칙으로 합니다.

| 증상 / 목적 | 중단점 대상 | 확인할 값 |
|---|---|---|
| 상태변화 메일이 안 나감 | ZCL_PAC => UPDATE_PAC_STATUS (메일 IF 블록) | AS_PAC_CONFIG-XMAIL, LV_STATUS(F/W/C 여부) |
| 수신자가 비어 발송 안 됨 | ZFPAC_SEND_ERROR_MAIL / _COMPLETE_MAIL (ZTPAC_PROC_AUTH SELECT) | LT_USERID 건수, 이메일 변환 결과 |
| 발송 자체 실패 | ZFPAC_SEND_MAIL 의 PERFORM SEND_MAIL | E_RESULT('S'/'E'), EV_LOGKEY |
| 본문 변수($필드$)가 안 채워짐 | ZCL_PAC_FUNC => GET_HTML / CONVERT_VAR | 필드명 매칭(ASSIGN COMPONENT 결과) |
| 알람 예약이 안 걸림 | ZLPAC7200_F01 → CREATE_MAIL_BATCH → ZFPAC_CREATE_ALARM_BATCH | 알람시각 계산, 배포 교차검증, 미래시각 여부 |
| 알람 발송이 안 됨 | ZLPAC7210 START-OF-SELECTION (CHECK_USER / EXECUTE_MAILING) | 수신자(GT_USER), 스케줄(GT_SCH_PLAN) 존재 여부 |

> [ 디버깅 포인트 ]<br>디버깅 시작 방법(예): SE38/SE24에서 대상 소스를 열고 줄에 중단점 설정 → 해당 기능 실행. 백그라운드(배치) 발송은 외부 중단점(External Breakpoint)을 사용해야 잡힙니다.<br>백그라운드 잡(알람 ZLPAC7210, ZFPAC_SEND_MAIL의 백그라운드 발송)은 SM37에서 잡을 찾아 디버깅하거나, 외부 중단점 + SM50으로 프로세스를 확인합니다.<br>덤프(단기 종료)가 의심되면 ST22에서 시각·사용자로 검색해 원인을 확인합니다.

## 7.3 빠른 점검 흐름

> 메일 안 옴 문의<br>└─ PAC 로그(HIST / SCH_D / CIS_MAIL)에 기록 있나?<br>├─ 없음 → 수신자/트리거 문제<br>│ ├─ 수신자 0명? → ZTPAC_PROC_AUTH 플래그/이메일/LOEVM 확인<br>│ ├─ 알람? → ZTPAC_SCH_ALARM(ASTATUS)·배포여부·SM37(ZLPAC7210)<br>│ └─ CIS? → ZTPAC_CIS_CID(XMAIL)·담당자·ZTPACEXIT<br>└─ 있음(STATUS=S) → SOST 상태 확인<br>├─ 대기 → SAPconnect 발송잡(RSCONN01) 가동 확인<br>├─ 오류 → 사유 확인 후 재전송<br>└─ 완료 → 수신측(스팸/메일게이트웨이) 안내
