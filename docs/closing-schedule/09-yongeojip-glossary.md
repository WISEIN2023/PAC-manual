---
id: closing-schedule/09-yongeojip-glossary
doc: closing-schedule
title: 9. 용어집 (Glossary)
parent: docs/closing-schedule/README.md
---

# 9. 용어집 (Glossary)

본 문서에 등장하는 주요 용어와 약어를 정리합니다. ‘(LG)’ 표기는 LG 환경에 특화된 항목입니다.

| 용어 / 약어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. SAP 결산자동화 솔루션. |
| Schedule ID | 통제가 필요한 업무 단위로 정의하는 결산 일정 식별자. ZLPAC7010에서 정의. 마스터 테이블 ZTPAC_SCH_ID. |
| Schedule Type | Schedule ID의 묶음. C=Closing Schedule, R=Closing Reporting, O=Other Schedule. |
| Final Schedule | 결산 최종 Activity로 수행하는 Schedule ID. 시점 도래 시 해당 법인의 standard posting period가 Close됨. 필드 FINAL. |
| Control by Time Schedule | 시간에 의한 통제 여부. 체크 시 시간 통제, 미체크 시 순서 통제. 필드 XTIME_CNTR. |
| Control HQ | 본사 전용 관리 Schedule ID 여부. 필드 STDFLAG(HQ Control). |
| Active Legacy I/F | 스케줄 open/close 시 유관 시스템 인터페이스 여부. 필드 LEGIF(Active Legacy Interface). |
| Assign Cut Off Group | Cut Off Group을 지정해 카테고리 단위로 인터페이스를 연계하는 옵션. 필드 ACT_CSP(Active Cut Off Group). |
| Cut Off Group / Category Group (LG) | Journal Accounting Rule의 카테고리 묶음. Cut Off Group 안에 Category Group·Category가 포함되며, CATEGRP·CATEGORY로 인터페이스 호출. 관리 소관은 GL 영역. |
| ZLPACEXIT | Maintain PAC User Exit. Exit Function(스케줄 인터페이스 등)을 등록·관리하는 프로그램. |
| ZFPAC_CSP_LEG_SCHIF / _EPS (LG) | LG의 스케줄 인터페이스 Exit Function. 각각 GENERAL_EXPENSE_UAS·FA_ADDITION 스케줄의 open/close 시 호출되어 상태 정보를 API로 전송. |
| Factor | 전표유형·G/L 계정·기능 영역 단위 세부 통제 조건. 하나의 No.에 최대 3개, Factor 간 OR 조건. |
| Assign Level | Schedule이 적용될 레벨. B=Business Type, O=Organization. |
| Organization Type | 조직 배정 방식. M=By Modeling Assigned Organization, S=By Schedule Organization. 필드 ORGTYP. |
| Distribute in HQ Time Zone | 결산 일정을 본사(UTC+9) 시간 기준으로 동시 실행하는 옵션. 필드 HQDIST. |
| Time Rule (HQ / Local) | 일정을 본사 시간(HQ)으로 적용할지 현지 시간(Local)으로 적용할지 구분하는 규칙. |
| Closing Calendar | 월별 결산 일자를 지정하는 달력. ZLPAC7030에서 정의. 미설정 시 배포 불가. |
| Day (D±n) | 결산 기준일 대비 상대 일자. 부호 있는 정수로 저장(예: Distribute D-5~D+5, Calendar D-10~D+31). |
| 배포 Status | 일정 배포 단계. New → Saved → Planning Saved → Planning Confirmed → Distributed(Lock). 필드 STATUS(ZTPAC_SCH_DISTM). |
| Create Schedule | Saved 계획으로 각 법인별 결산 일정을 생성하는 동작. |
| Plan Confirm | 계획 일정을 확정하는 동작. 확정 후에는 Re-Planning으로만 수정 가능. |
| Re-Planning / Reschedule | 배포된 일정을 다시 계획하는 동작. 기존 결산 이력이 Reset됨. |
| Super User | Posting Block 상태에서 예외적으로 기표를 허용하는 사용자. ZLPAC7160에서 등록. 테이블 ZTPAC_SCH_EXCEPT. |
| Exception Reason | Super User 예외 등록 사유. 필드 REASON. |
| Valid to Date / Time | Super User 예외 기표의 유효 기간/시간. 필드 VALIDTO / VALIDTM. |
| Open / On Time Closed / Manual Closed | 결산 일정 수행 상태. 미수행(Open) / 일정에 맞춰 자동 수행(On Time Closed) / 수작업 Close(Manual Closed). |
| Changeable? | 일정 변경 가능 여부. Time Control 미설정 Schedule은 No. |
| Approval Status | 일정 변경 결재 상태. 워크플로우 상태(WFSTATUS)로 관리. |
| Schedule Change | 일정 변경 동작. 상세 입력은 ZLPAC7180(Change Closing Schedule Detail). |
| Closing Schedule Alarm | 결산 일정 도래 전 알람 발송 설정. ZLPAC7200에서 등록. 테이블 ZTPAC_SCH_ALARM. 시간 통제 대상 일정만 설정 가능. |
| Alarm (Hour Before) | 결산 일정 몇 시간 전에 알람을 발송할지 지정(1~9). 필드 SCH_ALARM. |
| Alarm Status (Active/Inactive/Disable) | 알람 상태. 저장값 S=Saved, A=Active, Z=Inactive. Disable은 모델링 해제된 Schedule 분류. |
| Receiver Selection | 알람 수신자 선택 방식. From Activity Participants / Set Department / Add Receiver. |
| ZTPAC_SCH_ID | Closing Schedule ID Master. Schedule ID 및 통제 속성 보관 테이블. |
| ZTPAC_SCH_CONFIG | Closing Schedule Configuration. 결산일정 공통 설정 테이블. |
| ZTPAC_SCH_DISTM | 결산 일정 배포 마스터 테이블. 배포 Status 보관. |
| ZTPAC_SCH_EXCEPT | Super User(예외 기표) 등록 테이블. |
| ZTPAC_SCH_ALARM | 결산 일정 알람 등록 테이블. |
| ZTPAC_SCH_PLAN | 결산 일정 계획 테이블. 일정 변경(ZLPAC7170/7180)의 기준. |

— 문서 끝 —
