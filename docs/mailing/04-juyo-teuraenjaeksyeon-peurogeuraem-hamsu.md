---
id: mailing/04-juyo-teuraenjaeksyeon-peurogeuraem-hamsu
doc: mailing
title: 4. 주요 트랜잭션 · 프로그램 · 함수 · 클래스 (검증됨)
parent: docs/mailing/README.md
---

# 4. 주요 트랜잭션 · 프로그램 · 함수 · 클래스 (검증됨)

아래 목록은 SAP MCP(ADT)로 객체의 실재와 설명을 직접 확인한 것입니다. 영문 설명은 SAP에 등록된 객체 설명(verified), 우측은 운영 관점의 역할입니다.

## 4.1 운영자가 직접 사용하는 트랜잭션 / 프로그램

| 객체 / 호출 | 유형 | SAP 설명 | 운영 관점 역할 |
|---|---|---|---|
| ZLPACSYS | 프로그램(SE38) | PAC System Setting | 메일 종류 시스템 ON/OFF 설정 (관리자) |
| ZLPAC1000 | 트랜잭션 | Maintain Activity Participants | 사용자별 수신자/권한 등록 |
| ZLPAC_HTML | 트랜잭션 | PAC HTML Manager | HTML 메일 양식 등록/수정 |
| ZLPAC7200 | 트랜잭션 | Set Closing Schedule Alarm | 마감 알람 설정(저장 시 배치 예약) |
| ZLPAC7210 | 트랜잭션 | Closing Schedule Alarm Mailing | 예약 실행되는 알람 메일 발송 리포트 |
| SOST | 표준 트랜잭션 | SAPconnect Send Requests | 메일 실제 전송 상태 확인·재전송 |

## 4.2 핵심 함수(Function Module)

| 함수 | 함수그룹 | SAP 설명 | 역할 |
|---|---|---|---|
| ZFPAC_MAILING | ZPAC200 | PAC - Mailling Process | 상태→메일 라우터(F/W/M/C 분기) |
| ZFPAC_SEND_MAIL | ZPAC203 | Send Mail | 최종 발송 엔진(단일 출구) |
| ZFPAC_SEND_ERROR_MAIL | ZPAC202 | Activity Error Mailing | 에러=재작업 메일 |
| ZFPAC_SEND_COMPLETE_MAIL | ZPAC202 | Activity Complete Mailing | 완료 메일 |
| ZFPAC_SEND_MREADY_MAIL | ZPAC202 | Activity Error Mailing(라벨) | 수동준비 메일 |
| ZFPAC_GET_MAIL_RECEIVER | ZPAC201 | Closing Schedule Distribution Mail | 배포메일 화면/발송 |
| ZFPAC_CREATE_ALARM_BATCH | ZPAC172 | Create Alarm Batch | 알람 배치 예약/취소 |
| ZFPAC_SEND_CIS_MAIL | ZPACCIS0220 | Closing Inspection Error Mailing By Reviewer | CIS 리뷰어 메일 |
| ZFPAC_OPEN_TODO / CLOSE_TODO | ZPAC260 | (To Do Open/Close) | To-Do 생성/종료 |

**ZFPAC_MAILING의 IV_STATUS 분기 — 로그(IT_LOG) 필수 여부**

ZFPAC_MAILING은 직접 메일을 만들지 않습니다. IV_STATUS 값을 보고 아래 3개 펑션 중 하나를 대신 호출해 주는 교통정리(라우터) 역할만 합니다. 이때 메일 본문에 로그 내용이 들어가느냐에 따라 로그 파라미터(IT_LOG)의 필수 여부가 달라집니다.

| IV_STATUS | 호출되는 펑션 | 보내는 메일 | 로그 내용(IT_LOG) |
|---|---|---|---|
| F / W (실패·경고) | ZFPAC_SEND_ERROR_MAIL | 에러 메일 | 필수 — 로그가 없으면 발송하지 않고 에러 종료 |
| M (수동준비) | ZFPAC_SEND_MREADY_MAIL | 수동준비 알림 메일 | 불필요 — OPTIONAL 선언, 실제로 넘기지 않음 |
| C (완료) | ZFPAC_SEND_COMPLETE_MAIL | 완료 알림 메일 | 불필요 — OPTIONAL 선언, 실제로 넘기지 않음 |

> [ 왜 에러 메일만 로그가 필수인가요? ]<br>에러 메일은 “무엇이 실패했는지”를 보여주는 것이 목적이라, 로그 내역 자체가 메일의 본문 내용입니다. 그래서 ZFPAC_SEND_ERROR_MAIL은 ZTPAC_STATUS에서 실패(F/W) 로그 ID를 찾아 ZFPAC_LOG_DISPLAY로 로그를 추출한 뒤, 발송 메서드 ZCL_PAC_MAIL=>SEND_MAIL_ERROR의 IT_LOG(필수 파라미터)로 전달합니다. 로그가 비어 있으면 메일을 보내지 않고 에러로 종료합니다.<br>반면 수동준비(M)·완료(C) 메일은 “수동 작업 차례가 되었다 / 결산이 끝났다”만 알리는 단순 알림이라 로그 내용이 필요 없습니다. 두 펑션은 로그 추출 로직이 주석 처리되어 있고, 발송 메서드(SEND_MAIL_MREADY / SEND_MAIL_COMPLETE)의 IT_LOG도 OPTIONAL로 선언되어 있어 아예 전달하지 않습니다. (소스 주석 근거: “260311 — Manual ready는 로그 내용 불필요”)

## 4.3 핵심 클래스(Class)

| 클래스 · 메서드 | 역할 |
|---|---|
| ZCL_PAC_MAIL | 메일 엔진 — 수신자 구성·제목·HTML 본문·발송·로그 (SEND_MAIL_xxx 9종) |
| ZCL_PAC => UPDATE_PAC_STATUS | 상태 변경 시 메일/To-Do를 발화시키는 트리거 지점 |
| ZCL_PAC_FUNC => GET_HTML | HTML 양식을 읽어 변수($필드$)와 반복(loop)을 채움 |
| ZCL_PAC_TODO | To-Do 생성/종료/수신자 결정 |
| ZCL_PAC_ORG => ON_GET_USERINFO | 사용자ID → 이메일 등 사용자정보 조회 |
