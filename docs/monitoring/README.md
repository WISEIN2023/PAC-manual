---
id: monitoring
title: 모니터링 운영자 매뉴얼
category: 모니터링·알림
version: v1.0
updated: 2026-07-16
source: 모니터링_운영자_메뉴얼.docx
programs: [ZLPAC0160, ZLPAC0170, ZLPAC7010, ZLPACSTATUSM, ZLPAC_MONITOR, ZLPAC_MONITOR_ACT, ZLPAC_MONITOR_BUPAK, ZLPAC_MONITOR_COM, ZLPAC_MONITOR_GPID, ZLPAC_OVERTIME_PID]
tables: [ZTPACSYS, ZTPAC_BA_MAST, ZTPAC_CLOSE, ZTPAC_COM_GRP, ZTPAC_COM_MAST, ZTPAC_CONFIG, ZTPAC_CONFIG_COM, ZTPAC_CUNIT_MAST, ZTPAC_GPID, ZTPAC_GPID_MAST, ZTPAC_LOG_HDR, ZTPAC_PROC, ZTPAC_SCH_DISTM, ZTPAC_SCH_PLAN, ZTPAC_STATUS]
functions: [ZFPAC_LOG_DISPLAY, ZFPAC_PAC_MONITOR, ZCL_PAC, ZCL_PAC_AUTH, ZCL_PAC_FIORI, ZCL_PAC_FUNC]
summary: 액티비티별·BP별·회사코드별·글로벌 프로세스별 진행현황 모니터링 프로그램, 실행시간 초과 모니터링, 관리자용 상태 관리(ZLPACSTATUSM)
---

# 모니터링 운영자 매뉴얼

> 액티비티별·BP별·회사코드별·글로벌 프로세스별 진행현황 모니터링 프로그램, 실행시간 초과 모니터링, 관리자용 상태 관리(ZLPACSTATUSM)

| 문서 정보 | 내용 |
|---|---|
| 문서명 | 모니터링 운영자 메뉴얼 |
| 대상 솔루션 | PAC (Process Automatic Channel) |
| 대상 독자 | SAP 결산자동화 운영 · 유지보수 담당자 (SAP 초급 포함) |
| 대상 프로그램 | ZLPAC_MONITOR_ACT, ZLPAC_MONITOR_BUPAK, ZLPAC_MONITOR_COM,<br>ZLPAC_MONITOR_GPID, ZLPAC_OVERTIME_PID, ZLPAC0170, ZLPACSTATUSM |
| 문서 버전 | v1.0 |
| 작성일 | 2026-07-16 |
| 근거 | SAP 운영 시스템 소스(MCP 검증) 기반. 추론 없이 소스 확인 사실만 기술 |

## 목차

1. [1. 모니터링 프로그램 개요](01-moniteoring-peurogeuraem-gaeyo.md)
2. [2. 공통 기반 요소 (진행현황 모니터링 계열)](02-gongtong-giban-yoso-jinhaenghyeonhwang.md)
3. [3. 액티비티별 모니터링 — ZLPAC_MONITOR_ACT(LG제외)](03-aektibitibyeol-moniteoring-zlpac-monitor-act.md)
4. [4. 비즈니스 패키지별 모니터링 — ZLPAC_MONITOR_BUPAK](04-bijeuniseu-paekijibyeol-moniteoring-zlpac.md)
5. [5. 회사코드별 모니터링 — ZLPAC_MONITOR_COM](05-hoesakodeubyeol-moniteoring-zlpac-monitor-com.md)
6. [6. 글로벌 프로세스 모니터링 — ZLPAC_MONITOR_GPID](06-geulrobeol-peuroseseu-moniteoring-zlpac.md)
7. [7. 액티비티 실행시간 초과 모니터링 — ZLPAC_OVERTIME_PID](07-aektibiti-silhaengsigan-chogwa-moniteoring.md)
8. [8. 월 최종결산 완료 모니터링 — ZLPAC0170](08-wol-choejonggyeolsan-wanryo-moniteoring.md)
9. [9. 관리자용 상태 관리 — ZLPACSTATUSM](09-gwanrijayong-sangtae-gwanri-zlpacstatusm.md)
10. [10. 운영 · 유지보수 점검 가이드](10-unyeong-yujibosu-jeomgeom-gaideu.md)
11. [11. 현장(운영 시스템) 검증이 필요한 항목](11-hyeonjang-unyeong-siseutem-geomjeungi.md)
12. [12. 용어집 (Glossary)](12-yongeojip-glossary.md)
