---
id: authorization
title: 권한 운영자 매뉴얼
category: 기반설정
version: v1.0
updated: ""
source: 권한 운영자 메뉴얼.docx
programs: [ZLPAC0010, ZLPAC0080, ZLPAC0160, ZLPAC1000, ZLPAC1001, ZLPAC1010, ZLPAC1011, ZLPAC1020, ZLPAC1030, ZLPAC1050, ZLPAC5080, ZLPAC7160, ZLPAC7200, ZLPAC7210, ZLPACEXIT, ZLPACSYS]
tables: [ZTPACEXIT, ZTPACSYS, ZTPAC_AUTH_GROUP, ZTPAC_AUTH_ROLE, ZTPAC_BUPAK, ZTPAC_CONFIG, ZTPAC_CONFIG_COM, ZTPAC_LOG_DTL, ZTPAC_LOG_HDR, ZTPAC_PROC_AUTH, ZTPAC_SPAUTH, ZTPAC_SUPER_CONF, ZTPAC_USERINFO]
functions: [ZFPAC_CREATE_ALARM_BATCH, ZFPAC_CREATE_BATCHJOB, ZFPAC_CREATE_PID_JOB, ZFPAC_CSP_CHECK_BUKRS_AUTH, ZFPAC_EMP_INFO_SH_EXIT, ZFPAC_STD_AUTH, ZFPAC_USER_AUTH, ZFPAC_USRID_INFO_SH_EXIT, ZCL_PAC, ZCL_PAC_AUTH, ZCL_PAC_CLOSING, ZCL_PAC_ORG, ZCL_PAC_SAIL, ZCL_ZGWPAC_MAIN_DPC_EXT]
summary: PAC 권한 체계 전반. SAP 권한 기본기, PAC 권한 체크 구조, 조직권한, Fiori 화면 권한, 실행/Posting User 개념과 트러블슈팅
---

# 권한 운영자 매뉴얼

> PAC 권한 체계 전반. SAP 권한 기본기, PAC 권한 체크 구조, 조직권한, Fiori 화면 권한, 실행/Posting User 개념과 트러블슈팅

버전 v1.5 · 최종수정 2026-07-12

※ 본문의 프로그램·테이블·클래스는 SAP ADT(MCP)로 실재 여부를 검증함

## 목차

1. [개정 이력](01-gaejeong-iryeok.md)
2. [1. 문서 개요 및 학습 가이드](02-munseo-gaeyo-mit-hakseup-gaideu.md)
3. [2. PAC 권한의 큰 그림](03-pac-gwonhanui-keun-geurim.md)
4. [3. SAP 권한 기본기](04-sap-gwonhan-gibongi.md)
5. [4. PAC 권한 체크 구조](05-pac-gwonhan-chekeu-gujo.md)
6. [5. 권한 관리 실무 절차](06-gwonhan-gwanri-silmu-jeolcha.md)
7. [6. Fiori 화면과 권한](07-fiori-hwamyeongwa-gwonhan.md)
8. **7. 실행 유저 / Posting User 개념**
    - [7.1 Activity 실행 유저 표시 방식](08-01-activity-silhaeng-yujeo-pyosi-bangsik.md)
    - [7.2 Posting User 셋팅 (ZLPAC0010)](08-02-posting-user-setting-zlpac0010.md)
    - [7.3 Posting User(기표유저) vs Execute User(실행유저)](08-03-posting-user-gipyoyujeo-vs-execute-user.md)
    - [7.4 CWF 배치유저 (System User) — LG: BATCHCWF001](08-04-cwf-baechiyujeo-system-user-lg-batchcwf001.md)
    - [7.5 사원마스터(인사마스터) 연계와 Exit ON_GET_USERINFO — 화면의 사용자 정보는 어디서 오나](08-05-sawonmaseuteo-insamaseuteo-yeongyewa-exit.md)
9. [8. 관련 OData (참고)](09-gwanryeon-odata-chamgo.md)
10. [9. LG전자 특화 정리](10-lgjeonja-teukhwa-jeongri.md)
11. [10. 트러블슈팅 (증상 → 원인 → 조치)](11-teureobeulsyuting-jeungsang-wonin-jochi.md)
12. [11. 셀프 확인](12-selpeu-hwakin.md)
13. [프로세스 개요 — Participant (Process Overview)](13-peuroseseu-gaeyo-participant-process-overview.md)
14. [12. 부록 — 프로그램·테이블·클래스 (SAP 검증 결과)](14-burok-peurogeuraem-teibeul-keulraeseu-sap.md)
15. [13. 용어집](15-yongeojip.md)
