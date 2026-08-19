---
id: todo/01-to-do-gibon-gaenyeom
doc: todo
title: 1. To-Do 기본 개념
parent: docs/todo/README.md
---

# 1. To-Do 기본 개념

## 1.1 To-Do란 무엇인가

To-Do는 결산 진행 중 담당자가 조치해야 할 항목이 발생했을 때, 해당 담당자에게 전달되는 '할 일' 알림입니다. PAC는 현재 다음 네 가지 상황에 대해 To-Do를 발생시킵니다.

- Error : 결산 Activity 수행 중 오류가 발생한 경우
- Manual Ready : 자동 수행이 불가하여 담당자의 수동 조치(수동 완료)가 필요한 경우
- Rework : 이미 완료된 항목에 추가 전표 등이 감지되어 재작업이 필요한 경우
- Closing Inspection : 결산 점검(Inspection) 수행 중 오류가 발생한 경우

## 1.2 발생 방식 — 즉시 발송과 배치 감지

To-Do는 발생 시점에 따라 두 가지 방식으로 전달됩니다.

- 즉시 발송 : 상태 변경이 일어나는 그 시점에 바로 To-Do가 발송됩니다. Error가 대표적입니다.
- 배치 감지 후 발송 : 배치(Batch)가 일정 주기로 돌면서 대상을 감지한 뒤 발송합니다. Manual Ready와 Rework가 이 방식으로 처리됩니다.

## 1.3 To-Do 수신자 설정

To-Do를 누구에게 보낼지는 유형에 따라 별도의 마스터 프로그램에서 설정합니다.

- Error · Manual Ready 수신자 : ZLPAC1000(Participants) 등록 시 Option으로 설정합니다.
- Reviewer(Closing Inspection) 수신자 : ZLPAC5080(Reviewer) 등록 시 설정합니다.

> ✔ 시스템 확인<br>ZLPAC1000 = 'Maintain Closing Activity Participants' (결산 참여자 등록).<br>ZLPAC5080 = 'Maintain Closing Inspection Reviewer' (Reviewer 등록, 패키지 ZPAC_CIS).<br>두 프로그램 모두 라이브 SAP 시스템에서 등록 정보·설명을 확인했습니다.

## 1.4 To-Do 확인 경로와 Signal 연계

발생한 To-Do는 Closing Dashboard와 EP(전사 포털) To-Do 두 곳에서 확인할 수 있습니다. 다만 두 화면이 바라보는 관점은 서로 다릅니다.

- Closing Dashboard : PAC가 직접 관리하는 To-Do(CWF To-Do)를 결산 관점에서 표시합니다.
- EP To-Do : 'Signal'이라는 외부 시스템이 관할합니다. PAC가 전달한 정보를 토대로 To-Do가 생성되지만, 개별 인원의 EP To-Do 자체를 PAC에서 직접 조회할 수는 없습니다.

> ✔ 시스템 확인<br>PAC To-Do의 외부 연계(Signal) 활성 여부는 시스템 설정 테이블 ZTPACSYS 의 TODOIF 필드로 제어됩니다.<br>이 필드가 'X'이면 To-Do 발생/종료 시 Signal 연계 로직이 함께 동작합니다. (ZFPAC_OPEN_TODO / ZFPAC_CLOSE_TODO 소스에서 확인)
