---
id: mailing/11-burok-a-gwanryeon-teibeul-ilram
doc: mailing
title: 부록 A. 관련 테이블 일람
parent: docs/mailing/README.md
---

# 부록 A. 관련 테이블 일람

| 테이블 | 용도 |
|---|---|
| ZTPAC_PROC_AUTH | 사용자별 메일/To-Do/메신저 수신 플래그(XMAIL_*/XTODO_*/XMSGR_*) + 이메일(SMTP_ADDR) |
| ZTPACSYS | 메일 종류 시스템 토글(시스템당 1행) |
| ZTPAC_HTML / ZTPAC_HTML_BODY | HTML 양식 헤더 / 본문(HTML 텍스트) |
| ZTPAC_SCH_ALARM | 마감 알람 N시간(SCH_ALARM) · 활성상태(ASTATUS) |
| ZTPAC_SCH_CONFIG | 스케줄 공통 설정(발신자 SENDER, 본사법인 HQ_BUKRS 등) |
| ZTPAC_MAIL_HIST | Activity 계열 메일 발송 이력(완료/에러/수동준비) |
| ZTPAC_MAIL_SCH_D | 배포/알람 메일 발송 이력(SENDTYPE D/A) |
| ZTPAC_CIS_MAIL | 결산점검 메일 발송 이력(SENDTYPE C/R) |
| ZTPAC_MAIL_LOG | 발송 상세(발신/수신/제목/본문/상태, LOGKEY로 연결) |
| ZTPAC_MAIL_ADD / ZTPAC_MAIL_MENT | 배포메일 추가 수신자 / 코멘트 |
| ZTPAC_TODO_STU / ZTPAC_TODO_HIST | To-Do 상태(헤더) / 수신자별 이력 |
| ZTPACEXIT | CIS/메신저 외부연동 EXIT 함수 등록(EXIT_GROUP→EXITFUNC) [확인 필요: 메신저 실제 연동 여부] |
| ZTPAC_CIS_CID | 결산점검 카테고리 마스터(메일 ON/OFF: XMAIL) |
