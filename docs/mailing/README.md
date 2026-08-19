---
id: mailing
title: 메일링 운영자 매뉴얼
category: 모니터링·알림
version: v1.0
updated: ""
source: 메일링 운영자 메뉴얼.docx
programs: [ZLPAC0010, ZLPAC0600, ZLPAC1000, ZLPAC7100, ZLPAC7191, ZLPAC7200, ZLPAC7200_F01, ZLPAC7210, ZLPACCSP0020, ZLPACSYS, ZLPACTODOS, ZLPAC_HTML]
tables: [ZTPACEXIT, ZTPACSYS, ZTPAC_CIS_CID, ZTPAC_CIS_MAIL, ZTPAC_CIS_USER, ZTPAC_HTML, ZTPAC_HTML_BODY, ZTPAC_LOG_MAIL, ZTPAC_MAIL_ADD, ZTPAC_MAIL_HIST, ZTPAC_MAIL_LOG, ZTPAC_MAIL_MENT, ZTPAC_MAIL_SCH_D, ZTPAC_PROC_AUTH, ZTPAC_SCH_ALARM, ZTPAC_SCH_CONFIG, ZTPAC_TODO_HIST, ZTPAC_TODO_STU]
functions: [ZFPAC_CONFIRM_ITEM, ZFPAC_CREATE_ALARM_BATCH, ZFPAC_CSP, ZFPAC_CSP_CLOSING_ALARM_HTML, ZFPAC_CSP_CLOSING_DIST_HTML, ZFPAC_CSP_COMPLETE_MAIL, ZFPAC_CSP_ERROR_HTML, ZFPAC_CSP_MREADY_HTML, ZFPAC_CSP_REWORK_HTML, ZFPAC_CSP_SEND_REWORK_MAIL, ZFPAC_GET_MAIL_RECEIVER, ZFPAC_GET_MREADY_PID, ZFPAC_MAILING, ZFPAC_OPEN_TODO, ZFPAC_SEND, ZFPAC_SEND_CIS_CONT, ZFPAC_SEND_CIS_MAIL, ZFPAC_SEND_COMPLETE_MAIL, ZFPAC_SEND_ERROR, ZFPAC_SEND_ERROR_MAIL, ZFPAC_SEND_MAIL, ZFPAC_SEND_MREADY_MAIL, ZCL_PAC, ZCL_PAC_FUNC, ZCL_PAC_LOG, ZCL_PAC_MAIL, ZCL_PAC_ORG, ZCL_PAC_TODO]
summary: PAC 메일 종류별 발송 구조와 관련 트랜잭션·함수·클래스, 운영자 발송 설정 절차, HTML 메일 양식 작성 원리, 트러블슈팅
---

# 메일링 운영자 매뉴얼

> PAC 메일 종류별 발송 구조와 관련 트랜잭션·함수·클래스, 운영자 발송 설정 절차, HTML 메일 양식 작성 원리, 트러블슈팅

버전 1.1 (초안) · 검증 기준일 2026-06 · SAP MCP(ADT) 소스 직접 검증

## 목차

1. [1. 문서 개요](01-munseo-gaeyo.md)
2. [2. PAC 메일링 개념 잡기](02-pac-meilring-gaenyeom-japgi.md)
3. [3. 메일 종류별 상세](03-meil-jongryubyeol-sangse.md)
4. [4. 주요 트랜잭션 · 프로그램 · 함수 · 클래스 (검증됨)](04-juyo-teuraenjaeksyeon-peurogeuraem-hamsu.md)
5. [5. 운영자 업무 절차 (단계별)](05-unyeongja-eopmu-jeolcha-dangyebyeol.md)
6. [6. HTML 메일 양식 작성 원리](06-html-meil-yangsik-jakseong-wonri.md)
7. [7. 트러블슈팅 & 디버깅 가이드](07-teureobeulsyuting-dibeoging-gaideu.md)
8. [8. 개발 후 검증 절차](08-gaebal-hu-geomjeung-jeolcha.md)
9. [9. 운영 주의사항 (확인 필요 항목)](09-unyeong-juuisahang-hwakin-pilyo-hangmok.md)
10. [10. LXI 메일링 특화 로직 정리](10-lxi-meilring-teukhwa-rojik-jeongri.md)
11. [부록 A. 관련 테이블 일람](11-burok-a-gwanryeon-teibeul-ilram.md)
12. [부록 B. 용어집 (Glossary)](12-burok-b-yongeojip-glossary.md)
13. [부록 C. 기반 분석 자료](13-burok-c-giban-bunseok-jaryo.md)
14. [부록 D. MCP 검증 기록](14-burok-d-mcp-geomjeung-girok.md)
