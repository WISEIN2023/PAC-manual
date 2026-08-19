---
id: todo/06-unyeong-yujibosu-jeomgeom-gaideu
doc: todo
title: 6. 운영 · 유지보수 점검 가이드
parent: docs/todo/README.md
---

# 6. 운영 · 유지보수 점검 가이드

To-Do 관련 이상이 보고될 때, 아래 순서로 점검하면 원인 범위를 빠르게 좁힐 수 있습니다.

## 6.1 증상별 점검 가이드

| 증상 | 우선 점검 사항 |
|---|---|
| 특정 Business Package의 To-Do가 전혀 발생하지 않음 | ZTPAC_CONFIG-XTODO(To-Do 사용) 값이 'X'인지 확인 (ZLPAC0010) |
| Manual Ready To-Do가 지연되어 표시됨 | ① ZLPAC0010의 To-Do Duration(감지 주기) 확인 ② Manual Ready 감지 함수(ZFPAC_GET_MREADY_PID) 대상 여부 ③ 수신자(ZLPAC1000 Participants) 등록 확인 |
| Rework To-Do가 발생하지 않음 | ① 대상 BusPkg의 XREWORK='X' 여부 ② Rework 감지 배치([PAC]REWORK…, ZLPAC7191) 수행 여부(SM37) ③ ZLPAC0010의 Rework Duration |
| Error To-Do가 발생하지 않음 | 상태 변경 지점(ZCL_PAC=>UPDATE_PAC_STATUS)에서 To-Do 발송 대상인지, 수신자(Participants Option) 등록 여부 확인 |
| Closing Inspection To-Do가 발생하지 않음 | Activity Master의 Activity Type='I' 및 Inspection Category 등록 여부, Reviewer(ZLPAC5080) 등록 확인 |
| 발생했어야 할 To-Do가 누락됨 | ZLPACTODOS에서 비정상 To-Do 조회 후 검토 → 검토 완료 시에만 Open/Close 또는 Data Sync 수행 |
| CWF와 Signal To-Do가 서로 어긋남 | ZLPACCSP0020에서 싱크 불일치 건 조회 → CWF만 닫힌 경우 ZFPAC_CLOSE_TODO, Signal만 열린 경우 ZPCM_TODO_COMPLETE_FEEDBACK 사용 |
| EP(포털) To-Do가 표시되지 않음 | EP To-Do는 Signal이 관할하므로 PAC에서 직접 조회 불가. Signal 연계(ZTPACSYS-TODOIF) 및 Signal 담당 확인 |

## 6.2 정상 동작 확인 체크리스트

| 점검 항목 | 확인 방법 |
|---|---|
| To-Do 사용 설정 | ZLPAC0010에서 대상 BusPkg의 To-Do Active 및 Duration 확인 |
| 수신자 등록 | ZLPAC1000(Participants) / ZLPAC5080(Reviewer) 등록 확인 |
| 감지 배치 수행 | SM37에서 [PAC]REWORK(…) 등 감지 배치의 정상 수행 여부 확인 |
| 개별 To-Do 조회 | ZLPAC0600(Display To Do)에서 대상 조직/기간/User로 조회 |
| 비정상 To-Do 확인 | ZLPACTODOS(누락 등) / ZLPACCSP0020(Signal 싱크) 조회 |
