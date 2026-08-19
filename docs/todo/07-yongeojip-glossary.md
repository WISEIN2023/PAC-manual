---
id: todo/07-yongeojip-glossary
doc: todo
title: 7. 용어집 (Glossary)
parent: docs/todo/README.md
---

# 7. 용어집 (Glossary)

본 문서에 등장하는 주요 용어와 약어를 정리합니다.

| 용어 / 약어 | 설명 |
|---|---|
| To-Do | 결산 진행 중 담당자가 조치해야 할 항목을 알리는 '할 일' 알림. |
| TDTYPE | To-Do 유형 코드(데이터 엘리먼트 ZPAC_TODO_TYPE). E/M/R/CN/CC/CR/CS. |
| Error (E) | Activity 수행 중 오류 발생 시 즉시 발송되는 To-Do. |
| Manual Ready (M) | 자동 수행이 불가하여 수동 완료가 필요한 항목의 To-Do. 배치로 감지. |
| Rework (R) | 완료된 항목에 추가 전표 등이 감지되어 재작업이 필요할 때의 To-Do. |
| Closing Inspection (CN/CC/CR/CS) | 결산 점검 수행 중 오류 발생 시 발송되는 To-Do(일반/Controller/Reviewer/Simulation). |
| Individual | Manual Ready 중 개인 단위로 확인해야 하는 항목. IDV_FLAG='X'로 구분되어 별도 이벤트로 발생. |
| CWF To-Do | PAC가 직접 관리하는 To-Do. Closing Dashboard에서 확인. |
| EP To-Do | 전사 포털(EP)의 To-Do. Signal 시스템이 관할. |
| Signal | EP To-Do를 관할하는 외부 시스템. PAC가 전달한 정보로 To-Do를 생성. |
| ZFPAC_OPEN_TODO | To-Do 발생(Open) 함수. 함수 그룹 ZPAC260. TDTYPE별 분기. |
| ZFPAC_CLOSE_TODO | To-Do 종료(Close) 함수. 함수 그룹 ZPAC260. CWF·Signal Close 동시 호출. |
| ZFPAC_GET_MREADY_PID | Manual Ready 대상 감지 함수(함수 그룹 ZPAC280). |
| ZPCM_TODO_COMPLETE_FEEDBACK | Signal 측 To-Do 종료(피드백) 함수. Signal만 열린 경우 사용. |
| ZCL_PAC_SAIL=>CREATE_REWORK_BUPAK_JOB | Rework 감지 배치를 생성하는 메소드. 실행 리포트 ZLPAC7191. |
| ZLPAC7100 | 결산 일정 배포 프로그램(Distribute Closing Schedule). 배포 시 감지 배치 생성. |
| ZLPAC7191 | Rework 감지 배치 실행 리포트(Rework All Closing Check - Batch Session). |
| ZLPAC0010 | Business Package Config 유지보수 프로그램. To-Do/Rework Duration 설정. |
| ZLPAC0600 | Display To Do. 개별 To-Do 조회. My To Do와 연결. |
| ZLPACTODOS | To Do Abnormal Monitoring. 누락 등 비정상 To-Do 조회. |
| ZLPACCSP0020 | Signal Abnormal Monitoring. CWF-Signal 싱크 불일치 조회. |
| ZLPAC1000 | Maintain Closing Activity Participants. Error·Manual Ready 수신자 설정. |
| ZLPAC5080 | Maintain Closing Inspection Reviewer. Reviewer 수신자 설정. |
| ZTPAC_TODO_STU | To Do Status. To-Do 발송 헤더 테이블(Key: TDKEY, SEQ). |
| ZTPAC_TODO_HIST | To Do History. 개별 수신 건 아이템 테이블(Key: TDKEY, SEQ, EMPNO, BNAME). |
| ZTPAC_CSP_0020 | To Do Event Code Master. Signal 연계 이벤트 코드 마스터. |
| ZPCMT0380 | Signal 측 To-Do 테이블. 강제 종료 파라미터 조회에 사용. |
| ZTPACSYS | PAC System Configuration. TODOIF(Signal 연계) 등 시스템 설정 보관. |
| ZTPAC_CONFIG | Business Package Config 테이블. XTODO(To-Do 사용)/XREWORK/RWTMOUT 등 보관. |
| Duration | 감지 배치의 실행 주기(분). To-Do Duration(Manual Ready) / Rework Duration. |
| EVTNR / MSGGROUP | 이벤트 번호 / 메시지 그룹. Signal 연계 이벤트 코드의 구성 요소. |
| PACKETID | To-Do 건을 식별하는 키(타임스탬프 기반). Signal-CWF 대사 시 사용. |
| Activity Type 'I' | Activity가 Closing Inspection 유형임을 나타내는 마스터 값. |
| Inspection Category | Closing Inspection Activity의 점검 분류(예: PRE_CHK). |

— 문서 끝 —
