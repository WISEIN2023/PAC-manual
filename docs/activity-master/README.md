---
id: activity-master
title: Activity Master 운영자 매뉴얼
category: 마스터
version: v1.0
updated: ""
source: Activity Master 운영자 메뉴얼.docx
programs: [ZLPAC0010, ZLPAC0020, ZLPAC0030, ZLPAC0040, ZLPAC0070, ZLPAC0130, ZLPAC3000, ZLPAC3010, ZLPACSYS]
tables: [ZTPAC0074, ZTPAC_CIS_CID, ZTPAC_CONFIG, ZTPAC_CROSS_IF, ZTPAC_LOG_BLMSG, ZTPAC_LOG_DTL, ZTPAC_LOG_HDR, ZTPAC_LOG_PARAM, ZTPAC_PROC, ZTPAC_PROCT, ZTPAC_PROC_AUTH, ZTPAC_PROC_FUNC, ZTPAC_PROC_MEMO, ZTPAC_PROC_PER, ZTPAC_PROC_RCLOS, ZTPAC_PROC_SKIP, ZTPAC_RELATIVE, ZTPAC_RELATIVET, ZTPAC_REL_PARAM, ZTPAC_REWORK_LKD, ZTPAC_RW_RULEID, ZTPAC_STATUS, ZTPAC_STD_NODE]
functions: [ZFPAC, ZFPAC_CLOSING_ASSIGN, ZFPAC_CSP_AC_IF, ZFPAC_GOS_DELETE, ZFPAC_LINKED_PID_ASSIGN, ZFPAC_PID_BY_FUNCTION, ZFPAC_PID_DETAIL_SEARCH, ZFPAC_PID_INFO, ZFPAC_PID_PERIOD, ZFPAC_REL_PARAM, ZFPAC_REP_PARAM, ZFPAC_RULE_TO_ACTIVITY, ZFPAC_SET_BUPAK, ZFPAC_SET_LEGACY_URL, ZFPAC_SET_TRIGINFO, ZFPAC_SKIP_PID_ASSIGN, ZCL_PAC_LOG]
summary: Activity 3-Level 구조와 Activity Type별 정의 방법, 단계별 셋업 절차(STEP 1~6), 항목별 호출 Function 매핑, 트러블슈팅
---

# Activity Master 운영자 매뉴얼

> Activity 3-Level 구조와 Activity Type별 정의 방법, 단계별 셋업 절차(STEP 1~6), 항목별 호출 Function 매핑, 트러블슈팅

Define Activity Master (ZLPAC0020) — 결산 액티비티 정의·셋업

버전 1.0 (초안) · 검증 기준일 2026-06 · SAP MCP(ADT) 소스 직접 검증

## 목차

1. [1. 문서 개요](01-munseo-gaeyo.md)
2. [2. 큰 그림 — PAC 구조 한눈에](02-keun-geurim-pac-gujo-hannune.md)
3. [3. 관련 트랜잭션 · 함수 · 테이블 (검증됨)](03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md)
4. [4. 화면 구성 및 진입](04-hwamyeon-guseong-mit-jinip.md)
5. **5. 초기 운영자 셋업 절차 (단계별)**
    - [5.1 STEP 1 — Activity Group / Sub-Group 정의 (General 탭)](05-01-step-1-activity-group-sub-group-jeongui.md)
    - [5.2 STEP 2 — Activity 정의 (Activity Type / Call Type)](05-02-step-2-activity-jeongui-activity-type-call.md)
    - [5.3 (위 STEP 2 보조) 항목→버튼→Function 한눈 정리](05-03-wi-step-2-bojo-hangmok-beoteun-function.md)
    - [5.4 STEP 3 — Rework Rule ID 등록 (재작업 감지)](05-04-step-3-rework-rule-id-deungrok-jaejakeop.md)
    - [5.5 STEP 4 — Linked Activity 등록 (선후행 연결)](05-05-step-4-linked-activity-deungrok-seonhuhaeng.md)
    - [5.6 STEP 5 — Relative(연관 프로그램) 등록 (Relative 탭)](05-06-step-5-relative-yeongwan-peurogeuraem.md)
    - [5.7 STEP 6 — 저장](05-07-step-6-jeojang.md)
6. [6. 항목별 호출 Function 매핑표 (핵심 요약)](06-hangmokbyeol-hochul-function-maepingpyo.md)
7. [7. 연계 작업 (사전 · 후속)](07-yeongye-jakeop-sajeon-husok.md)
8. [8. 트러블슈팅 & 디버깅 가이드](08-teureobeulsyuting-dibeoging-gaideu.md)
9. [9. 직접 해보기 실습](09-jikjeop-haebogi-silseup.md)
10. [10. 운영 주의사항 (확인 필요 항목)](10-unyeong-juuisahang-hwakin-pilyo-hangmok.md)
11. [11. 신규구축시 Activity Master 관련 업무(LXI 예시)](11-singyuguchuksi-activity-master-gwanryeon.md)
12. [부록 A. 용어집 (Glossary)](12-burok-a-yongeojip-glossary.md)
