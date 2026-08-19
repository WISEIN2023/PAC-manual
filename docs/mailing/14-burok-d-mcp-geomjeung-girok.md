---
id: mailing/14-burok-d-mcp-geomjeung-girok
doc: mailing
title: 부록 D. MCP 검증 기록
parent: docs/mailing/README.md
---

# 부록 D. MCP 검증 기록

본문의 객체 단정은 아래 검증을 근거로 합니다. (검증 기준일: 2026-06, SAP ADT/MCP) 못 읽은 항목은 «미확인»으로 남깁니다.

| 객체 | 결과 | 근거 |
|---|---|---|
| ZLPAC1000 | ✔ Tcode | "Maintain Activity Participants" |
| ZLPAC_HTML | ✔ Tcode | "PAC HTML Manager" |
| ZLPAC7200 | ✔ Tcode | "Set Closing Schedule Alarm" |
| ZLPAC7210 | ✔ Tcode | "Closing Schedule Alarm Mailing" |
| ZLPACSYS | ✔ (Tcode 아님, 프로그램) | PROG/P only, TRAN 없음 → SE38 실행 |
| ZFPAC_MAILING | ✔ FM | FG ZPAC200, "PAC - Mailling Process" |
| ZFPAC_SEND_MAIL | ✔ FM | FG ZPAC203, "Send Mail" |
| ZFPAC_SEND_ERROR/COMPLETE/MREADY_MAIL | ✔ FM | FG ZPAC202 (MREADY 라벨은 'Error'로 오기 — ⚠️) |
| ZFPAC_GET_MAIL_RECEIVER | ✔ FM | FG ZPAC201, 배포메일 화면 |
| ZCL_PAC_MAIL | ✔ Class | "Mail Class" (메일 엔진) |
| ZCL_PAC=>UPDATE_PAC_STATUS | ✔ (소스확인) | 상태변화 시 메일/To-Do 발화 지점 |
| ZTPACEXIT (CIS/메신저 트리거) | ⚠ 구조✔·데이터 미확인 | GetTableContents 404 → 운영 SE16 확인 |
| 타입그룹 ZPAC0 (HTML 마커 리터럴) | 미확인(환경 제약) | 타입그룹 소스 열람 불가 → 기존 양식 복사 권장 |
