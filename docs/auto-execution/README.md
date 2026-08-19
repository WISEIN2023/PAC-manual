---
id: auto-execution
title: PAC 자동수행 운영자 매뉴얼
category: 실행·자동화
version: v1.0
updated: ""
source: PAC_자동수행_운영자매뉴얼.docx
programs: [ZLPAC0100, ZLPAC0101]
tables: [ZTPACJOBS, ZTPACSYS, ZTPAC_CLOSE, ZTPAC_CONFIG, ZTPAC_CROSS_IF, ZTPAC_GPID, ZTPAC_LOG_HDR, ZTPAC_PROC, ZTPAC_PROC_RCLOS, ZTPAC_SCH, ZTPAC_SCH_CONFIG, ZTPAC_SCH_PLAN, ZTPAC_STATUS]
functions: [ZFPAC_AUTOTRIG_CROSS, ZFPAC_AUTOTRIG_CROSS_BUPAK, ZFPAC_CHECK_JOB_BALANCING, ZFPAC_CHECK_PRENODE, ZFPAC_CLOSING_SCHID, ZFPAC_CONFIRM_ITEM, ZFPAC_CREATE_BATCHJOB, ZFPAC_CREATE_BUPAK_JOB, ZFPAC_CREATE_GPID, ZFPAC_CREATE_GPID_JOB, ZFPAC_CREATE_PCSGP_JOB, ZFPAC_CREATE_PID_JOB, ZFPAC_GET_CAN_START, ZFPAC_GET_RUNNING_JOB, ZFPAC_GLOBAL_GET_CAN_START, ZFPAC_NEXT_AUTO_START, ZFPAC_ORG_AUTH, ZFPAC_STOP_PCSGP_JOB, ZFPAC_USER_AUTH, ZCL_PAC, ZCL_PAC_AUTH, ZCL_PAC_CLOSING, ZCL_PAC_ORG, ZCL_PAC_SAIL, ZCL_ZGWPAC_MAIN_DPC_EXT]
summary: 자동수행(XAUTO) 개념과 자동실행 흐름도, 수행 단계별 상세 프로세스, 프로그램 호출관계·선후행·영향도, 핵심 테이블과 설정 스위치
---

# PAC 자동수행 운영자 매뉴얼

> 자동수행(XAUTO) 개념과 자동실행 흐름도, 수행 단계별 상세 프로세스, 프로그램 호출관계·선후행·영향도, 핵심 테이블과 설정 스위치

SAP 결산 자동화 솔루션 · 자동수행 프로세스 / 프로그램 관계 / 영향도 / 참조 정보

## 목차

1. [1. 자동수행 개념](01-jadongsuhaeng-gaenyeom.md)
2. [2. 자동실행 흐름도](02-jadongsilhaeng-heureumdo.md)
3. [3. 수행 단계별 상세 프로세스 (자동수행 관점)](03-suhaeng-dangyebyeol-sangse-peuroseseu.md)
4. [4. 프로그램 호출관계 · 선후행 · 영향도](04-peurogeuraem-hochulgwangye-seonhuhaeng.md)
5. [5. 핵심 테이블 · 설정 스위치](05-haeksim-teibeul-seoljeong-seuwichi.md)
6. [6. 연계 함수 · 메소드 상세 (프로세스 관점)](06-yeongye-hamsu-mesodeu-sangse-peuroseseu.md)
