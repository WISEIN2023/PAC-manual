---
id: modeling
title: 모델링 운영자 매뉴얼
category: 마스터
version: v1.0
updated: 2026-07-12
source: 모델링_운영자_메뉴얼.docx
programs: [ZLPAC0020, ZLPAC0030, ZLPAC0031, ZLPAC0040, ZLPAC0041, ZLPAC0050, ZLPAC0140, ZLPAC1050]
tables: [ZTPAC, ZTPAC_BUPAK, ZTPAC_BUSTY, ZTPAC_CLD, ZTPAC_CLD_OLINK, ZTPAC_CLD_ONODE, ZTPAC_CLD_SLINK, ZTPAC_CLD_SNODE, ZTPAC_CLO, ZTPAC_CONFCOM, ZTPAC_CONFIG, ZTPAC_CONFIG_BA, ZTPAC_CONFIG_COM, ZTPAC_CONFIG_UNI, ZTPAC_CUNIT_MAST, ZTPAC_GPID, ZTPAC_GPID_MAST, ZTPAC_MDLVLT, ZTPAC_NODE_HIST, ZTPAC_ORG_LINK, ZTPAC_ORG_NODE, ZTPAC_STATUS, ZTPAC_STD_LINK, ZTPAC_STD_NODE]
functions: [ZFPAC_SET_BUPAK, ZCL_PAC, ZCL_PAC_AUTH, ZCL_PAC_NETGRAPH, ZCL_PAC_ORG]
summary: 표준 모델링(ZLPAC0030)과 조직 모델링(ZLPAC0040)을 통한 결산 프로세스 구성, 노드 정의·상속·선후행 관계 설정
---

# 모델링 운영자 매뉴얼

> 표준 모델링(ZLPAC0030)과 조직 모델링(ZLPAC0040)을 통한 결산 프로세스 구성, 노드 정의·상속·선후행 관계 설정

| 문서명 | 모델링 운영자 메뉴얼 |
|---|---|
| 대상 솔루션 | PAC (Process Automatic Channel) |
| 대상 독자 | SAP 결산자동화 운영 · 유지보수 담당자 (SAP 초급 담당자 포함) |
| 대상 프로그램 | ZLPAC0030 / ZLPAC0031 / ZLPAC0040 / ZLPAC0041 / ZLPAC0050 (관련: ZLPAC0020 / ZLPAC1050 / ZLPAC0140) |
| 문서 버전 | v1.0 |
| 작성일 | 2026-07-12 |
| 근거 | MCP(ABAP ADT) 소스 검증 기반. 미검증 항목은 [현장확인] 으로 표기 |

## 목차

1. [1. 모델링 기본 개념](01-modelring-gibon-gaenyeom.md)
2. [2. 모델링 프로그램 한눈에 보기](02-modelring-peurogeuraem-hannune-bogi.md)
3. [3. 표준 모델링 — ZLPAC0030 (Standard Modeling)](03-pyojun-modelring-zlpac0030-standard-modeling.md)
4. [4. 조직 모델링 — ZLPAC0040 (Organization Modeling)](04-jojik-modelring-zlpac0040-organization.md)
5. [5. 글로벌 패키지 모델링 구조 — ZLPAC0031 / ZLPAC0041](05-geulrobeol-paekiji-modelring-gujo-zlpac0031.md)
6. [6. CO 모델링 및 조직 등록 — ZLPAC0050](06-co-modelring-mit-jojik-deungrok-zlpac0050.md)
7. [7. 실무 모델링 변경 절차](07-silmu-modelring-byeongyeong-jeolcha.md)
8. [8. 모델링 조회 · 삭제 및 자주 묻는 질문](08-modelring-johoe-sakje-mit-jaju-mutneun-jilmun.md)
9. [9. 운영 · 유지보수 점검 가이드](09-unyeong-yujibosu-jeomgeom-gaideu.md)
10. [10. 현장(운영 시스템) 검증이 필요한 항목](10-hyeonjang-unyeong-siseutem-geomjeungi.md)
11. [11. 용어집 (Glossary)](11-yongeojip-glossary.md)
