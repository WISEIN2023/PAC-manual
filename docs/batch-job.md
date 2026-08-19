---
id: batch-job
title: PAC Batch Job 생성 프로세스 운영자 매뉴얼
category: 실행·자동화
version: v1.0
updated: ""
source: PAC_Batch_Job_생성_프로세스_운영자매뉴얼.docx
programs: [ZLPAC0100, ZLPAC0101, ZLPAC0150, ZLPAC0540, ZLPAC5110, ZLPAC5111, ZLPAC5210, ZLPAC5211, ZLPAC5310, ZLPAC5311, ZLPAC7111, ZLPAC7190, ZLPAC7191, ZLPAC7192, ZLPAC7193, ZLPAC7194, ZLPAC7195, ZLPAC7196, ZLPAC7210, ZLPAC7300]
tables: []
functions: [ZFPAC_GET_CAN_START, ZFPAC_GLOBAL_GET_CAN_START, ZCL_PAC, ZCL_PAC_CLOSING, ZCL_PAC_SAIL]
summary: PAC에서 배치 잡이 생성되는 경로별 프로세스 일람(Job 생성 함수와 호출 시점)
---

# PAC Batch Job 생성 프로세스 운영자 매뉴얼

> PAC에서 배치 잡이 생성되는 경로별 프로세스 일람(Job 생성 함수와 호출 시점)

## 1. 개요

본 문서는 SAP 결산자동화 솔루션인 PAC(Process Automatic Channel)의 유지보수를 위한 운영자 매뉴얼이다. PAC 운영 과정에서 자동/예약/데몬 형태로 생성되는 각종 Batch Job의 종류와 생성 시점, 실행 프로그램(Job Pgm), 실행 주기, 네이밍 규칙을 정리하여 장애 대응 및 운영 점검 시 참고할 수 있도록 한다.

**Batch Job 주기 구분:** 각 Job은 실행 주기에 따라 **실시간**(이벤트 발생 즉시 실행), **예약**(지정 시점 예약 실행), **데몬**(일정 종료 시까지 다음 예약 Job을 반복 생성) 형태로 구분된다.

**네이밍룰 표기:** 네이밍룰의 [PAC]는 Job 이름의 접두어이며, ‘년월/법인/조직정보/BUPAK/PCSGP/PID’ 등은 실행 대상에 따라 치환되는 변수 값이다. ★ 표기는 Business Config에 Active된 Package 단위로 정기 생성되는 핵심 감지 Job을 의미한다.

## 2. Batch Job 생성 프로세스 일람

아래 표는 PAC의 대분류별 Batch Job 생성 프로세스를 정리한 것이다.

| 대분류 | 소분류 | 업무 설명 | Job 생성 시점 | Job Pgm | 주기 | 네이밍룰 | 비고 |
|---|---|---|---|---|---|---|---|
| Activity<br>자동실행 | Global Pkg 수행 | Global Package의 경우 Bus Pkg 레벨 자동 실행 | Global Package를 Root에서 'Start' 수행 시 | ZLPAC0100 | 실시간 | [PAC]P_GPID_년월_법인 |  |
| Activity<br>자동실행 | BusPkg 수행 | BusPkg의 전체 프로세스를 자동 실행 | Root에서 'Start' 수행 시 | ZLPAC0100 | 실시간 | [PAC]B_년월+조직정보_BUPAK |  |
| Activity<br>자동실행 | Actvitiy Group 수행 | Actvitiy Group 내 프로세스를 자동실행 | 1) BusPkg Level에서 'Start' 실행<br>2) 상위 Level에서 실행됨 | ZLPAC0100 | 실시간 | [PAC]G_년월+조직정보_PCSGP |  |
| Activity<br>자동실행 | Activity 수행 | Actvitiy 내 프로세스를 자동실행 | 1) Activity Group Level 에서 'Start' 실행<br>2) 상위 Level에서 실행됨 | ZLPAC0100 | 실시간 | [PAC]S_년월+조직정보_PCSGP |  |
| Activity<br>자동실행 | Closing ID수행 | 특정 프로세스만 자동실행 | 1) Activity Level 에서 'Start' 실행<br>2) 상위 Level에서 실행됨 | ZLPAC0101 | 실시간 | [PAC]A_년월+조직정보_PID | ZLPAC0101에서 실제 PGM을 SUBMIT 수행 |
| Schedule Job | Closing Inspection 수행 | 특정 Category 별로 수행한다 | Schedule Job Create 버튼 클릭 시 | ZLPAC0540 | 예약 | [PAC]Btype+jobseq+(BUPAK/년월/조직정보) | Btype = I (Closing Inspection) |
| Schedule Job | Closing ID 수행 | 특정 프로세스만 자동실행 | Schedule Job Create 버튼 클릭 시 | ZLPAC0540 | 예약 | [PAC]Btype+jobseq+(BUPAK/년월/조직정보) | Btype = S (Specific Activity) |
| Schedule Job | Global / Bus Pkg 수행 | Global / BusPkg의 전체 프로세스를 자동 실행 | Schedule Job Create 버튼 클릭 시 | ZLPAC0540 | 예약 | [PAC]Btype+jobseq+(BUPAK/년월/조직정보) | Btype = T (Automatic start of business Package) |
| Rework 감지 | 정기감지 ★ | Config설정된 단위로 Rework 발생을 점검한다<br>- Business Config에 Active된 Package 별로 생성 | 일정배포시 생성됨<br>- ZCL_PAC_SAIL=>CREATE_REWORK_BUPAK_JOB | ZLPAC7191 | 데몬 | [PAC]REWORK(BUPAK)_년/월 | - 비정상 종료 점검도 같이 수행됨<br>( Auto 대상이나 종료 후에도 진행중으로 뜬 경우 에러처리)<br>- Mismatch 상태 Sync<br>( Group 내 상태와 불일치시 상태값 동기화 )<br>※ Final 일정시까지 다음 예약잡을 생성하는 구조로 실행됨<br>- 5분단위 (Config 설정) |
| Rework 감지 | 수시감지 | Activity Group 단위로 Rework을 수시 점검한다 | 1) Activity 자동실행시 생성<br>2) 일정 마감시 생성<br>3) Can Run 체크시 생성 | ZLPAC0150 | 실시간 | [PAC]년월_PCSGP_RW |  |
| To-Do | 정기감지 ★ | Config설정된 단위로 Manual Todo 발생을 점검한다<br>- Business Config에 Active된 Package 별로 생성 | 일정배포시 생성됨<br>- ZCL_PAC_SAIL=>CREATE_MANUAL_TODO_JOB | ZLPAC7195 | 데몬 | [PAC]MTODO(BUPAK)_년/월 | - Manual Ready To Do 항목 중 미발송 내역을 발송<br>※ Final 일정시까지 다음 예약잡을 생성하는 구조로 실행됨<br>- 1분단위 (Config 설정) |
| To-Do | 정기감지 ★ | Config설정된 단위로 Abnormal Todo 발생을 점검한다<br>- Business Config에 Active된 Package 별로 생성 | 일정배포시 생성됨<br>- ZCL_PAC_SAIL=>CREATE_ABN_TODO_JOB | ZLPAC7196 | 데몬 | [PAC]ABTODO(BUPAK)_년/월 | - 정상 발송되지 않은 To Do 항목을 체크된 내역을 발송<br>※ Final 일정시까지 다음 예약잡을 생성하는 구조로 실행됨<br>- 1분단위 (Config 설정) |
| 일정 마감체킹 | 정기감지 ★ | 마감일정이 도래한 경우 상태를 반영 (On Time Closed 처리)<br>- 스케쥴 Conifg : Overdue Job Creation이 활성화 된 경우만 | 일정배포시 생성됨<br>- ZCL_PAC_CLOSING=>CREATE_OVERDUE_JOB | ZLPAC7190 | 데몬 | [PAC]OVERDUE(년/월) | ※ Final 일정시까지 다음 예약잡을 생성하는 구조로 실행됨<br>- 5분단위 (Config 설정) |
| 일정 알람 | 결산일정 마감전 사전 알람 | 일정배포시 생성됨 | ZLPAC7210 | 예약 | SA/법인+년+월+일정ID | - 일정배포시 설정된 시간을 기준으로 예약 Job 생성됨<br>- 일정 배포후 변경내역 참고못함 |  |
| 일정마감정보 I/F | 일정 Open/Close 정보 Legacy I/F<br>. Schedule Master에 Legacy Active + Exit 등록 되어야함 | 일정 Open/Close | ZLPAC7194 | 실시간 | [PAC]SCHIF_ + 스케쥴ID + (조직/년월) |  |  |
| 차월 STD Period 오픈 | 차월의 Standard Posting Period를 자동으로 Open한다<br>- 일정 Config에 Active된 경우 생성<br>- 법인별 1일 00시에 맞추어 생성됨 | 일정배포시 생성됨<br>- ZCL_PAC_CLOSING=>CREATE_NEXT_PERIOD_OPEN_JOB | ZLPAC7300 | 예약 | [PAC]Next Period(년+월+법인) | System Config에 설정되어야 함 |  |
| Global Package - Sync | Activity Group의 Can Run등의 정보를 미리 생성한다<br>- Can Run 점검시의 성능향상을 위해 | 1) 일정배포시 생성됨<br>2) ZFPAC_GLOBAL_GET_CAN_START 수행시 | ZLPAC7111 | 실시간 | [PAC]GPID_SYNC(년/월/조직) |  |  |
| BusPkg - Sync | BusPkg의 전체 프로세스의 Can Run을 수행한다<br>- Can Run 점검시의 성능향상을 위해 | 1) 일정배포시 생성됨<br>2) ZFPAC_GET_CAN_START 수행시 | ZLPAC7111 | 실시간 | [PAC]BUPAK_SYNC(년/월/조직) |  |  |
| BusPkg - Sync | 변경이 발생된 Activity Group을 사용하는 조직으로 Sync 수행 | Standard Map 변경시<br>- ZCL_PAC > CREATE_SYNC_JOB_BY_MAST | ZLPAC7192 | 실시간 | [PAC]MASTER SYNC(조직) | 변경된 PCSGP로 영향받는 OPEN 법인에게 모두 SYNC 수행 |  |
| BusPkg - Sync | 변경이 발생된 Activity Group을 사용하는 조직으로 Sync 수행 | Activity Master의 Move To 수행시<br>- ZCL_PAC > CREATE_SYNC_JOB_BY_MAST | ZLPAC7193 | 실시간 | [PAC]MOVE SYNC(PID) | STATUS가 존재하는 OPEN 법인의 영향 PCSGP로 SYNC 수행 |  |
| 결산 Simulation 점검 | Category별 수행 | Simulation 점검 Category 별로 수행한다 | 1) 결산점검 자동 예약 실행시<br>2) 결과화면에서 Inspection Run 수행시 | ZLPAC5310 | 예약<br>실시간 | C_BUPAK+CATEGORY+년월+Seq |  |
| 결산 Simulation 점검 | Activity 별 수행 | Activity Master에 등록된 Simulation 대상 프로그램 점검을 수행 | 결과화면에서 Inspection Run 수행시 | ZLPAC5311 | 실시간 | S_BUPAK+CATEGORY+년월+Scenraio+Seq |  |
| 결산 Reviewer 점검 | Category별 수행 | Reviewer 점검 Category 별로 수행한다 | 1) 결산점검 자동 예약 실행시<br>2) 결과화면에서 Inspection Run 수행시 | ZLPAC5110 | 예약<br>실시간 | C_BUPAK+CATEGORY+년월+Seq |  |
| 결산 Reviewer 점검 | Scenario별 수행 | 시나리오에 등록된 점검 로직을 수행하여 결과 반영 | 1) 결과화면에서 Inspection Run 수행시<br>2) Detail 화면에서 재수행시 | ZLPAC5111 | 실시간 | S_BUPAK+CATEGORY+년월+Scenraio+Seq |  |
| 결산점검(일반) | Category별 수행 | 일반 점검 Category 별로 수행한다 | 1) 결산점검 자동 예약 실행시<br>2) 결과화면에서 Inspection Run 수행시 | ZLPAC5210 | 예약<br>실시간 | C_BUPAK+CATEGORY+년월+Seq |  |
| 결산점검(일반) | Scenario별 수행 | 시나리오에 등록된 점검 로직을 수행하여 결과 반영 | 1) 결과화면에서 Inspection Run 수행시<br>2) Detail 화면에서 재수행시 | ZLPAC5211 | 실시간 | S_BUPAK+CATEGORY+년월+Scenraio+Seq |  |
