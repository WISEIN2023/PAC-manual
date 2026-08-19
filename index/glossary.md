<!-- 이 파일은 docs/ 원본에서 자동 생성됩니다. 직접 수정하지 마세요. -->

# 용어집 (통합)

각 매뉴얼의 용어집 섹션을 통합했습니다. 동일 용어는 최초 정의 1건만 유지합니다.

총 **263건**

| 용어 | 설명 | 출처 |
|---|---|---|
| **Active Legacy I/F** | 스케줄 open/close 시 유관 시스템 인터페이스 여부. 필드 LEGIF(Active Legacy Interface). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Activities Not Exist** | Node에 표시되는 메시지. Closing ID가 모델링되지 않은 경우 발생. (8.4 참조) | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Activity (Closing ID)** | PAC 결산 작업의 한 단위. 실제로 수행되는 프로그램이 설정된 최하위 레벨. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Activity / Activity Group** | PAC 결산 프로세스의 작업 단위(Activity)와 그 묶음(Group). 상태는 ZTPAC_STATUS로 관리됨. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Activity Group / Sub-Group** | Activity의 묶음(상위) / Closing ID의 묶음(중간) 레벨. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Activity Type** | C=Closing Schedule, F=Confirmation, I=Closing Inspection, L=Legacy, M=Dummy, N=Function, T=Transaction, X=Auto Trigger. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Activity Type 'I'** | Activity가 Closing Inspection 유형임을 나타내는 마스터 값. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Activity(액티비티)** | PAC에서 결산 작업의 한 단위. 자동 실행되며 상태(준비/실행/완료/오류 등)가 변함. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **Alarm (Hour Before)** | 결산 일정 몇 시간 전에 알람을 발송할지 지정(1~9). 필드 SCH_ALARM. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Alarm Status (Active/Inactive/Disable)** | 알람 상태. 저장값 S=Saved, A=Active, Z=Inactive. Disable은 모델링 해제된 Schedule 분류. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ALV (ABAP List Viewer)** | SAP ABAP 표준 목록 출력 및 편집 컴포넌트. 데이터 확인·수정 화면. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ALV (SAP List Viewer)** | SAP의 표준 목록/편집 그리드. 본 문서의 유지보수 화면(화면번호 0100)이 사용. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **AMC (ABAP Messaging Channel)** | APC와 짝을 이루어 메시지를 채널에 실어 나르는 SAP 표준 기술. | [notice](../docs/notice.md#8-용어집-glossary) |
| **AND RETURN** | SUBMIT/호출 종료 후 제어를 호출 프로그램으로 반환하는 옵션. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **APC** | ABAP Push Channel. WebSocket 기반으로 To-Do를 포털 화면에 실시간 푸시. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **APC (ABAP Push Channel)** | ABAP 서버가 Fiori 화면으로 메시지를 Push하는 실시간 통신 기술. WebSocket 기반. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Approval Status** | 일정 변경 결재 상태. 워크플로우 상태(WFSTATUS)로 관리. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Assign Cut Off Group** | Cut Off Group을 지정해 카테고리 단위로 인터페이스를 연계하는 옵션. 필드 ACT_CSP(Active Cut Off Group). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Assign Level** | Schedule이 적용될 레벨. B=Business Type, O=Organization. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Assign Target Business Package** | 공지사항 생성·수정 화면의 우측 영역. 공지를 표시할 BP 및 조직을 지정. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Attach File (첨부 파일)** | 공지사항에 파일을 첨부하는 기능. 저장 완료 후에만 이용 가능. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Auto / Manual** | Auto=Start로 자동 수행, Manual=사용자가 직접 입력·Complete. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Auto Trigger** | 선행 Activity 완료 시 후행 Activity/BP를 자동으로 기동하는 PAC 메커니즘. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **AUTO_TYPE** | 자동수행 범위. A=Activity, B=Business Package, G=Activity Group. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **BATCHCWF001** | CWF 배치 실행 계정. Auto Trigger FM 수동 재실행 시 EXNAM 파라미터에 입력하는 배치 전용 계정. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **BCS** | Business Communication Services. SAP 표준 메일 발송 프레임워크. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **BLEVEL** | 비즈니스 유형 레벨. A / C(회사코드) / B(사업영역) / K(결산단위). (ZTPAC_BUSTY-BLEVEL) | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **BUKRS** | 회사코드(법인). SAP 표준 필드. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **BUKRS / GSBER / CUNIT** | 회사코드 / 사업영역 / 결산단위(조직 키). | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **BUPAK** | Business Package. PAC 설정의 최상위 묶음 단위. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **BUPAK / Business Package** | 결산 업무 묶음의 최상위 식별자. 마스터: ZTPAC_BUPAK. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Business Package (BP, BUPAK)** | PAC 결산 프로세스의 업무 단위(모듈). 공지사항에서 수신 대상 범위를 지정하는 키. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Business Package (BUPAK)** | PAC를 구성하는 기본 수행 단위(최상위 묶음). | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **BUSTY / Business Type** | 비즈니스 유형. 표준 맵 구분 키. 마스터: ZTPAC_BUSTY(BLEVEL 필드로 레벨 구분). | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **By Function (N)** | Function Module 호출로 수행되는 Activity 유형. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **CALL TRANSACTION** | 트랜잭션 코드를 실행하는 ABAP 표준 구문. 본 문서에서는 SET PARAMETER ID/BDCDATA와 함께 사용. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Call Type** | P=Program(표준·Auto 필수), T=Transaction(Manual 일부). | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **CALLTYP** | 호출 방식. 'P'=프로그램 SUBMIT, 그 외='T'=CALL TRANSACTION. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **CBO Table (Z/Y 테이블)** | Customer Build Object. SAP 표준이 아닌 고객사가 개발한 커스텀 테이블. Z 또는 Y로 시작. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Changeable?** | 일정 변경 가능 여부. Time Control 미설정 Schedule은 No. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **CID** | 결산점검 Category ID(데이터 타입 ZPAC_CID). Category 유형(CTYPE)으로 점검 트랜잭션을 결정. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **CIS** | Closing Inspection(결산점검). 결산 데이터의 재무 리스크를 시나리오로 검증. 제목 'Financial Risk Validation'. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **CIS / Closing Inspection** | 결산점검. 시나리오(Category ID)로 결산 데이터 검증. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **CLMON** | 결산 확정 스냅샷 테이블(ZTPAC_CLD_…)의 키인 결산월. 해당 월의 모델 상태를 구분. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **CLOSED** | 결산 마감 여부(ZTPAC_CLOSE-CLOSED='X'). 마감된 조직/기간은 상태 동기화 대상에서 제외됨. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Closing Calendar** | 월별 결산 일자를 지정하는 달력. ZLPAC7030에서 정의. 미설정 시 배포 불가. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Closing Dashboard** | PAC의 메인 Fiori 화면. 결산 현황 캘린더, 공지사항, My To-Do 등을 표시. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Closing ID** | 모델링 계층(Activity Group → Activity → Closing ID)의 최하위(최종) 레벨. Closing ID까지 모델링되어야 수행 가능. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Closing Inspection (CN/CC/CR/CS)** | 결산 점검 수행 중 오류 발생 시 발송되는 To-Do(일반/Controller/Reviewer/Simulation). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Closing Schedule** | 결산 마감 일정. 모델링과 연계해 특정 시점 자동 마감. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Closing Schedule Alarm** | 결산 일정 도래 전 알람 발송 설정. ZLPAC7200에서 등록. 테이블 ZTPAC_SCH_ALARM. 시간 통제 대상 일정만 설정 가능. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Control by Time Schedule** | 시간에 의한 통제 여부. 체크 시 시간 통제, 미체크 시 순서 통제. 필드 XTIME_CNTR. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Control HQ** | 본사 전용 관리 Schedule ID 여부. 필드 STDFLAG(HQ Control). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Create Schedule** | Saved 계획으로 각 법인별 결산 일정을 생성하는 동작. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **CUNIT** | 결산단위(Closing Unit). PAC 필드. 화면 라벨은 패키지별로 다를 수 있음. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Cut Off Group / Category Group (LG)** | Journal Accounting Rule의 카테고리 묶음. Cut Off Group 안에 Category Group·Category가 포함되며, CATEGRP·CATEGORY로 인터페이스 호출. 관리 소관은 GL 영역. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **CWF** | 운영 서버 모델링 변경 요청을 처리하는 담당(인원). 운영 서버는 CWF를 통해 요청 파일로 변경. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **CWF To-Do** | PAC가 직접 관리하는 To-Do. Closing Dashboard에서 확인. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **CWF 배치 유저** | PAC 배치잡 실행 전용 계정. 수동 재실행 시 EXNAM 파라미터에 입력. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Data Migration** | 데이터 이관. SAP 시스템 간 테이블 데이터를 전송하는 작업. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Day (D±n)** | 결산 기준일 대비 상대 일자. 부호 있는 정수로 저장(예: Distribute D-5~D+5, Calendar D-10~D+31). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Distribute in HQ Time Zone** | 결산 일정을 본사(UTC+9) 시간 기준으로 동시 실행하는 옵션. 필드 HQDIST. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Duration** | 감지 배치의 실행 주기(분). To-Do Duration(Manual Ready) / Rework Duration. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ENQUEUE / DEQUEUE** | SAP 표준 잠금 설정/해제 함수. 모델링은 EZ_ZSPAC_LOCK, 조직 등록은 EZ_ZTPAC_CONFCOM 사용. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **EP To-Do** | 전사 포털(EP)의 To-Do. Signal 시스템이 관할. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Error (E)** | Activity 수행 중 오류 발생 시 즉시 발송되는 To-Do. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **EVTNR / MSGGROUP** | 이벤트 번호 / 메시지 그룹. Signal 연계 이벤트 코드의 구성 요소. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Exception Reason** | Super User 예외 등록 사유. 필드 REASON. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Factor** | 전표유형·G/L 계정·기능 영역 단위 세부 통제 조건. 하나의 No.에 최대 3개, Factor 간 OR 조건. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **FI000 (삭제 에러)** | 'It cannot be deleted because there is status history data.' 상태 이력 데이터가 존재하여 모델링을 삭제할 수 없을 때 표시되는 메시지. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Final Schedule** | 결산 최종 Activity로 수행하는 Schedule ID. 시점 도래 시 해당 법인의 standard posting period가 Close됨. 필드 FINAL. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Fiori** | SAP의 웹 기반 사용자 인터페이스(UI). Closing Dashboard(zfrpac00020) 포함. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Function Type (Activity)** | PAC Activity Type 중 하나. RFC를 통해 외부 서버의 함수(Function)를 직접 실행하는 방식. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **GCRC Transaction Block** | Trigger 실행 후 자동으로 수행되는 후행 트랜잭션 묶음. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **GJAHR** | 회계 연도. SAP 표준 필드. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **GPID / Global Package ID** | 여러 Business Package를 묶는 글로벌 패키지 식별자. 마스터: ZTPAC_GPID_MAST. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **GSBER** | 사업영역(Business Area). SAP 표준 필드. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **HTML 템플릿($필드$)** | 메일 본문 양식. $필드명$ 자리에 발송 데이터가 치환되고, loop 마커로 표가 반복됨. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **Individual** | Manual Ready 중 개인 단위로 확인해야 하는 항목. IDV_FLAG='X'로 구분되어 별도 이벤트로 발생. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Inspection Category** | Closing Inspection Activity의 점검 분류(예: PRE_CHK). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Interface 모드** | ZLPACMIG030에서 RFC를 통해 원격 시스템 데이터를 읽어오는 모드. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **IS_DATA / IT_DATA1~9** | GET_HTML에 넘기는 데이터. IS_DATA=단건(헤더), IT_DATA1~9=여러 건(반복 표). | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **ITMSEQ** | 항목 시퀀스. 화면 표시(정렬) 순서. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **IV_AUTO_NEXT / AV_AUTO_NEXT** | ZCL_PAC_SAIL CONSTRUCTOR 파라미터 및 내부 변수. 'X'여야 자동수행 로직 활성화. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **LAND1** | 국가 키. SAP 표준 필드. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Legacy RFC / URL** | 트랜잭션 대신 연계되는 레거시 대상. 정의에 존재 시 CALL_URL로 처리. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Linked Activity** | 선후행 관계의 후행 Activity 묶음. Linked Rework / Reset Linked에 사용. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **LOEVM** | 삭제 플래그(Deletion Flag). 논리 삭제 표시. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **LOGKEY** | 한 번의 발송을 식별하는 키. PAC 로그와 발송 상세(ZTPAC_MAIL_LOG)를 연결. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **MAIN (대표 패키지)** | 글로벌 패키지에 연결된 Business Package 중 대표 패키지 표시. ZTPAC_GPID-MAIN='X'. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Maintain Level** | Activity Master 실행 Level. 모델링 Level(2/3)에 따라 표시 단계가 달라짐. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Manual Ready (M)** | 자동 수행이 불가하여 수동 완료가 필요한 항목의 To-Do. 배치로 감지. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Manual Ready(수동준비)** | 자동이 아니라 사람이 수동으로 처리하도록 준비된 단계. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **Map (Standard / Organization)** | Activity Sub-Group을 Node로 연결한 프로세스 흐름도(ZLPAC0030/0040). | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **MCP (ADT)** | SAP ABAP Development Tools 연동. 본 매뉴얼의 객체 검증(읽기 전용)에 사용. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **MEMORY ID** | EXPORT/IMPORT TO/FROM MEMORY로 프로그램 간 값을 전달하는 ABAP 메모리. 본 문서의 ZPAC0_INPUT_PARAM 해당. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Modify 모드** | ZLPACMIG030에서 현재 시스템의 테이블 데이터를 직접 조회·수정하는 모드. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **MONAT** | 회계 기간(월). SAP 표준 필드. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Notice (공지사항)** | PAC에서 운영 담당자가 결산 참여자에게 전달하는 공지. ZTPAC_NOTICE 테이블에 저장됨. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Notification 영역** | Closing Dashboard 상단에 표시되는 공지사항 목록 영역. 최대 3개까지 표시. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Open / On Time Closed / Manual Closed** | 결산 일정 수행 상태. 미수행(Open) / 일정에 맞춰 자동 수행(On Time Closed) / 수작업 Close(Manual Closed). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **OPENDT / OPENPH** | 결산 오픈(개시) 일자 / 오픈 순서(차수). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Organization Type** | 조직 배정 방식. M=By Modeling Assigned Organization, S=By Schedule Organization. 필드 ORGTYP. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **P_NOPID** | ZLPAC0140의 체크박스. 하위 Activity가 없는 노드만 조회. Level 1·2 선택 시에만 표시되며, 'Activities Not Exist' 노드 추적에 사용. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **PAC** | Process Automatic Channel. 본 문서의 대상인 SAP 결산자동화 솔루션. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **PACKETID** | To-Do 건을 식별하는 키(타임스탬프 기반). Signal-CWF 대사 시 사용. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **PACLVL (C/B/U)** | 조직 레벨. C=법인(Company), B=사업영역(Business Area), U=기타조직. 제목·본문·템플릿이 이 레벨에 따라 분기. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **PACLVL (조직 레벨)** | Business Package별 조직 기준 레벨. C=회사코드 / B=사업영역 / U=결산단위. ZTPAC_CONFIG에 저장. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **PCSGP** | 프로세스/Activity 그룹 식별자. ZLPAC7192/7193의 상태 동기화 대상 단위. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **PCSGP / Activity Group** | 액티비티 그룹. 모델을 그룹 단위로 구분. 값이 BUPAK와 같으면 최상위(1레벨)로 취급. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **PID** | Process ID. 결산 프로세스(구조)를 식별하는 값. ZLPAC7193의 파라미터 P_PID. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Plan Confirm** | 계획 일정을 확정하는 동작. 확정 후에는 Re-Planning으로만 수정 가능. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Re-Planning / Reschedule** | 배포된 일정을 다시 계획하는 동작. 기존 결산 이력이 Reset됨. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Receiver Selection** | 알람 수신자 선택 방식. From Activity Participants / Set Department / Add Receiver. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Relative** | Monitoring Dashboard에서 Activity와 함께 보여줄 연관 프로그램/URL. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **REPFLAG** | 대표조직 플래그. 대표 조직 여부 표시(소스 주석: 대표조직 FLAG). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **REPTY** | Activity 정의의 Report Type. 값이 'C'이면 결산일정 변경으로 분기. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **REQ_BUKRS** | 회사코드 필수 여부 플래그. 'X'이면 PACLVL이 B/U라도 회사코드 입력 필수. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Rework** | 이미 완료된 Activity를 다시 수행하는 재작업 기능. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Rework (R)** | 완료된 항목에 추가 전표 등이 감지되어 재작업이 필요할 때의 To-Do. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Rework Rule ID** | 재기표를 감지하는 규칙(G/L 계정 범위 등). ZLPAC3000/3010에서 정의. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Rework(재작업)** | 완료된 Activity에 추가 기표가 감지되어 재수행이 필요한 상태. Rework Rule ID로 감지. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **RFC (Remote Function Call)** | 원격 함수 호출. SAP 시스템 간 네트워크를 통해 함수를 호출하는 표준 방식. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **RFC Destination** | SM59에 등록된 원격 SAP 시스템 접속 정보. 이관 시 원본 시스템으로의 연결 경로. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **RS_IMPORT_DYNPRO** | 대상 화면(Dynpro)의 입력 필드 목록을 조회하는 표준 함수. 존재 필드에만 값 세팅에 사용. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **S4D / S4H** | 각각 SAP S/4HANA 개발 시스템 / 운영 시스템의 예시 SYSTEM ID. 실제 환경에 따라 다름. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SA38 / SE38** | ABAP 프로그램을 실행하는 SAP 표준 트랜잭션. | [notice](../docs/notice.md#8-용어집-glossary) |
| **SAMC** | AMC 채널 관리 트랜잭션. 채널 인가 프로그램(Authorized Program) 등록 시 사용. | [notice](../docs/notice.md#8-용어집-glossary) |
| **SAPconnect / RSCONN01** | SAP의 외부 통신(메일) 게이트웨이 / 발송 큐를 처리하는 표준 프로그램. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **Save without Screen** | ALV 확인 화면 없이 즉시 저장하는 옵션. 대량 이관 자동화 시 활용. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Schedule Change** | 일정 변경 동작. 상세 입력은 ZLPAC7180(Change Closing Schedule Detail). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Schedule ID** | 통제가 필요한 업무 단위로 정의하는 결산 일정 식별자. ZLPAC7010에서 정의. 마스터 테이블 ZTPAC_SCH_ID. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Schedule Type** | Schedule ID의 묶음. C=Closing Schedule, R=Closing Reporting, O=Other Schedule. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **SCHID** | Closing Schedule ID. 결산일정 변경 시 PID로부터 조회하여 전달. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SCU3** | SAP 표준 테이블 변경 로그 조회 트랜잭션. PAC 모델링은 전용 이력 테이블이 없어 변경 이력을 SCU3로 확인. (9.4 참조) | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **SE16N** | 테이블 데이터를 조회하는 SAP 표준 트랜잭션 (테이블 데이터 브라우저). | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SE37** | SAP Function Module 직접 실행 트랜잭션. 수동 재실행 시 사용. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **SE38 / SA38** | ABAP 프로그램을 직접 실행/편집하는 표준 트랜잭션. 트랜잭션이 없는 배치 프로그램 실행에 사용. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SENDTYPE** | 메일 발송 유형 코드. A=알람, D=배포, E=Activity계열, C=CIS컨트롤러, R=CIS리뷰어. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **SET PARAMETER ID** | SPA/GPA 파라미터 메모리에 값을 저장해 다음 화면 입력 필드에 기본값으로 전달하는 표준 구문. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SICF** | ICF 서비스 활성화 트랜잭션. APC WebSocket 서비스를 활성화할 때 사용. | [notice](../docs/notice.md#8-용어집-glossary) |
| **Signal** | EP To-Do를 관할하는 외부 시스템. PAC가 전달한 정보로 To-Do를 생성. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Signal(메신저)** | PAC 외부의 알림 플랫폼. 엘지(LXI)에서는 To-Do 알림을 Signal To-Do와 인터페이스해 함께 수신함. (PAC 자체 메신저 발송 기능은 미구현) | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **SM12** | SAP 잠금(Lock) 항목을 조회·관리하는 표준 트랜잭션. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SM21** | SAP 시스템 로그 조회 트랜잭션. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **SM37** | SAP 백그라운드 잡 모니터 트랜잭션. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **SM59** | RFC 연결 목적지를 관리하는 SAP 표준 트랜잭션. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SNID / CID** | CIS의 점검 시나리오 ID / 점검 카테고리 ID. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **SOST** | SAPconnect 발송 큐 모니터 트랜잭션. 메일 실제 전송 상태 확인·재전송. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **Special Role (M / O)** | ZLPAC1050에서 부여하는 모델링 수정 권한. M=Modeling-Std(표준 맵), O=Modeling-Org(조직 맵). (값은 운영 자료 기준, 현장확인) | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **SPRAS** | 언어 키. SAP 표준 필드. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **START ALL** | ZCL_PAC_SAIL의 기본 실행 모드. IV_START_FROM 미입력 시 수행 가능한 모든 Activity를 순차 수행. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **START FROM** | ZCL_PAC_SAIL의 IV_START_FROM 파라미터. 지정 PID부터 해당 라인만 선택적으로 실행하는 모드. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Status (Active/Closed)** | Active: 유효기간 내 공지(녹색). Closed: 만료 공지(빨간색). | [notice](../docs/notice.md#8-용어집-glossary) |
| **SUBMIT** | ABAP에서 다른 프로그램을 실행하는 구문. ZLPACMIG020은 ZLPACMIG030을 SUBMIT으로 호출. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **SUBMIT ... WITH SELECTION-TABLE** | 내부 파라미터 테이블(RSPARAMS)을 대상 리포트 셀렉션 화면에 전달하는 ABAP 표준 구문. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Super User** | Posting Block 상태에서 예외적으로 기표를 허용하는 사용자. ZLPAC7160에서 등록. 테이블 ZTPAC_SCH_EXCEPT. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Tcode vs 프로그램** | GetTransaction으로 구분. 본 화면 ZLPAC0020은 실제 Tcode. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **TDTYPE** | To-Do 유형 코드(데이터 엘리먼트 ZPAC_TODO_TYPE). E/M/R/CN/CC/CR/CS. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Time Rule (HQ / Local)** | 일정을 본사 시간(HQ)으로 적용할지 현지 시간(Local)으로 적용할지 구분하는 규칙. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **To-Do** | 결산 진행 중 담당자가 조치해야 할 항목을 알리는 '할 일' 알림. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **To-Do(할 일)** | PAC 전용 테이블에 기록되고 포털에 실시간 표시되는 알림 채널. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **TR (Transport Request)** | SAP 변경 전송 요청. 개발 → 품질 → 운영 순서로 Workbench/Customizing 변경을 이관. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **TRIG_TYPE** | Trigger 발생 유형. L=Legacy, B=BP간, S=타모듈, O=조직간. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Trigger Code** | 타 시스템/모듈/조직/Bus.Pkg 간 완료 정보를 I/F 받아 상태 반영하는 코드(ZLPAC0070). | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Trigger Code (CRSCODE)** | Auto Trigger 설정의 고유 식별자. ZTPAC_CROSS_IF 테이블의 키 값. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **Trigger Definition** | ZLPAC0020에서 Activity에 연결하는 Trigger Code. Inbound/Outbound 구분. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **TSTC** | 트랜잭션 코드-실행 프로그램 매핑을 보관하는 SAP 표준 테이블. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **TZONE** | 시간대(Time Zone). SAP 표준 필드(TTZZ/TTZ5 참조). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Valid to Date / Time** | Super User 예외 기표의 유효 기간/시간. 필드 VALIDTO / VALIDTM. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **Variant / Param** | 프로그램 실행 변형(Variant) / 호출 파라미터(Log Field·Screen Param·Constant). 합집합 수행. | [activity-master](../docs/activity-master/12-burok-a-yongeojip-glossary.md#부록-a-용어집-glossary) |
| **Web GUI 불가** | 모델링 화면은 ActiveX가 필요하여 Web GUI에서 실행 불가. SAP GUI 전용. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **Where Condition** | SQL WHERE 절에 해당하는 조회 조건. 특정 데이터 범위만 필터링할 때 사용. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **Where Used List** | 특정 Activity가 사용된 모든 모델링 목록. 전 법인 모델링 삭제 시 여기에 존재하는 모델링을 모두 삭제해야 함. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **XAUTO (Auto Next)** | ZTPAC_CROSS_IF의 자동수행 플래그. 'X'=자동, 공백=수동. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **XAUTO_START** | ZTPAC_CONFIG의 'Always auto start after completed' 필드. X 체크 시 AFTER_CONF/AFTER_CLSD/XAUTO_NEXT/CONFLVL이 자동 설정됨. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **XCOMP (조직지정여부)** | ZTPAC_NOTICE 테이블 필드. 공지 대상 조직이 지정된 경우 값이 설정됨. | [notice](../docs/notice.md#8-용어집-glossary) |
| **XMAIL_ERR / _MRD / _COM** | 사용자별 메일 수신 플래그(에러 / 수동준비 / 완료). | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **XSKIP** | 대상 화면 첫 셀렉션 화면 SKIP 여부 플래그. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZCL_PAC / ZCL_PAC_FUNC** | PAC 핵심 로직 클래스. 상태 동기화(SYNC_PCSGP_STATUS)·결산월 조회 등 제공. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZCL_PAC_AUTH** | PAC 권한 검사 클래스. CHECK_BUPAK_AUTH로 Business Package 관리 권한 확인. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZCL_PAC_NETGRAPH** | 표준 설명 'Process Automatic Channel - Network'. 모든 모델링 프로그램이 공통으로 사용하는 네트워크 그래프 엔진 클래스. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZCL_PAC_ORG** | PAC 조직 처리 클래스. CHECK_VALID_ORG(조직 유효성), get_cunit_field_name(결산단위 라벨) 등 제공. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZCL_PAC_SAIL** | PAC 자동화 실행 엔진 클래스. START_FROM_AUTO_TRIGGER 메서드로 Auto Trigger 수행. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZCL_PAC_SAIL=>CREATE_REWORK_BUPAK_JOB** | Rework 감지 배치를 생성하는 메소드. 실행 리포트 ZLPAC7191. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_AUTOTRIG_CHECK** | Auto Trigger 사전 유효성 검증 FM. Trigger Code 존재, 조직/Period 유효성, 수행 가능 여부를 일괄 검증. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_AUTOTRIG_CROSS_BUPAK** | TRIG_TYPE=B(BP간) Trigger 실행 FM. Outbound 완료 후 Inbound BP의 후행 Activity를 기동. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_AUTOTRIG_CROSS_ORG** | TRIG_TYPE=O(조직간) Trigger 실행 FM. 동일 BP 내 서로 다른 조직 간 Trigger 수행. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_AUTOTRIG_LEGACY** | Legacy 유형 Trigger의 수동 재실행에 사용하는 Function Module. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_AUTOTRIG_OTHERS** | TRIG_TYPE=S(타 모듈) Trigger 실행 FM. SAP 비PAC 업무(MM,SD 등)에서 호출 시 사용. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_CALL_APC_NOTICE** | 공지사항 저장 시 APC 메시지를 발송하는 PAC 함수. Function Group: ZPAC111. | [notice](../docs/notice.md#8-용어집-glossary) |
| **ZFPAC_CHECK_PRENODE** | AUTO_TYPE=B 시 선행 Activity 완료 여부를 추가 검증하는 FM. EV_SUBRC=0이어야 후행 기동. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_CLOSE_TODO** | To-Do 종료(Close) 함수. 함수 그룹 ZPAC260. CWF·Signal Close 동시 호출. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_CREATE_PCSGP_JOB** | 지정된 PCSGP를 백그라운드 잡으로 기동하는 Function Module. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_CSP_LEG_SCHIF / _EPS (LG)** | LG의 스케줄 인터페이스 Exit Function. 각각 GENERAL_EXPENSE_UAS·FA_ADDITION 스케줄의 open/close 시 호출되어 상태 정보를 API로 전송. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZFPAC_GET_CAN_START** | 후행 Activity 수행 가능 여부를 판단하는 Function Module. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_GET_MREADY_PID** | Manual Ready 대상 감지 함수(함수 그룹 ZPAC280). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZFPAC_LEGACY_LINK** | 레거시 URL 연계 함수모듈(함수그룹 ZPAC270). | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZFPAC_OPEN_TODO** | To-Do 발생(Open) 함수. 함수 그룹 ZPAC260. TDTYPE별 분기. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC0010** | Maintain Business Package Config. Business Package 전역 설정 트랜잭션. Auto Trigger 자동 수행을 위한 XAUTO_START 등 설정. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC0020** | Define Activity Master. Activity Group 번호·명칭을 정의/확인하는 프로그램(동일명 트랜잭션). 모델링 전 준비 단계. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0030** | Maintain Standard Map. 표준 모델링 프로그램. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0031** | Maintain Global Package Standard Map. 글로벌 표준 모델링 프로그램. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0040** | Maintain Organization Map. 조직 모델링 프로그램. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0041** | Maintain Global Package Organization Map. 글로벌 조직 모델링 프로그램(회사코드 레벨). | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0050** | Assign Organization to Business Package. Business Package에 조직(회사/사업영역/결산단위)을 등록하고 모델 매핑을 확인하는 프로그램(동일명 트랜잭션). | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0060** | PAC 공지사항 관리 프로그램 (Notice Management). 생성·변경·삭제 기능 제공. | [notice](../docs/notice.md#8-용어집-glossary) |
| **ZLPAC0140** | Display Modeling List. 모델링 결과를 레벨(1/2/3)별로 조회하는 프로그램(동일명 트랜잭션). 삭제 완료·최하위 모델링 확인에 사용. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC0600** | Display To Do. 개별 To-Do 조회. My To Do와 연결. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC1000** | Maintain Closing Activity Participants. Error·Manual Ready 수신자 설정. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC1050** | Maintain Special Role. 2·3 Level 모델링 수정 권한(Special Role)을 부여하는 프로그램(동일명 트랜잭션). | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZLPAC5080** | Maintain Closing Inspection Reviewer. Reviewer 수신자 설정. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC7100** | 결산 일정 배포 프로그램(Distribute Closing Schedule). 배포 시 감지 배치 생성. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC7191** | Rework 감지 배치 실행 리포트(Rework All Closing Check - Batch Session). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPAC_FTCODE** | Fiori에서 SAP GUI 트랜잭션을 호출하는 진입 프로그램/트랜잭션. 파라미터 조합으로 호출 유형을 분기. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZLPACCSP0020** | Signal Abnormal Monitoring. CWF-Signal 싱크 불일치 조회. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZLPACEXIT** | Maintain PAC User Exit. Exit Function(스케줄 인터페이스 등)을 등록·관리하는 프로그램. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZLPACTODOS** | To Do Abnormal Monitoring. 누락 등 비정상 To-Do 조회. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZPAC_NOTICE (APC명)** | 공지사항 실시간 반영을 위한 PAC 전용 APC. SICF 경로: /sap/bc/apc/sap/zpac_notice. | [notice](../docs/notice.md#8-용어집-glossary) |
| **ZPCM_TODO_COMPLETE_FEEDBACK** | Signal 측 To-Do 종료(피드백) 함수. Signal만 열린 경우 사용. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZPCMT0380** | Signal 측 To-Do 테이블. 강제 종료 파라미터 조회에 사용. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZSPAC_TIMESTAMP** | 생성자·생성일·최종변경자·변경일·변경시각을 담는 공통 인클루드 구조. 모든 조직마스터 테이블에 포함. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_BUPAK** | PAC Business Package 마스터 테이블. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_CIS_CID** | Closing Inspection Category Master. CID별 Category 유형(CTYPE) 보관. | [fiori-sapgui-call](../docs/fiori-sapgui-call/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_CLD_ONODE / ZTPAC_CLD_OLINK** | 결산 확정(마감) 시점의 조직 모델 노드/링크 스냅샷. 결산월(CLMON) 단위로 보관. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_CLD_SNODE / ZTPAC_CLD_SLINK** | 결산 확정(마감) 시점의 표준 모델 노드/링크 스냅샷. 결산월(CLMON) 단위로 보관. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_CONFIG** | PAC Global Config. Business Package별 PACLVL/REQ_BUKRS 등 설정 보관. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_CONFIG_COM/BA/UNI** | 비즈니스 패키지별 조직 배정(설정) 테이블. ZLPAC0050에서 유지보수. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_CROSS_IF** | Cross System Trigger Master 테이블. Trigger Code 속성 저장. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_CSP_0020** | To Do Event Code Master. Signal 연계 이벤트 코드 마스터. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_NOTICE** | 공지사항 마스터 테이블. 번호(ITMSEQ), 제목(NOTICEDESC), 본문(LTEXT), 유효기간(DATBI/TATBI) 저장. | [notice](../docs/notice.md#8-용어집-glossary) |
| **ZTPAC_NOTICE_ORG** | 공지사항 대상 조직 테이블. Business Package별 공지 대상 법인·조직 정보 저장. | [notice](../docs/notice.md#8-용어집-glossary) |
| **ZTPAC_ORG_NODE / ZTPAC_ORG_LINK** | 조직 모델의 노드/링크(맵) 정보 테이블. ZLPAC0050 LINK 조회에 사용. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_PROC** | Activity Definition Master 테이블. Activity의 모든 속성 저장. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_PROC_FUNC** | PAC Activity의 Function(함수) 실행 정의를 저장하는 PAC CBO 테이블. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_SCH_ALARM** | 결산 일정 알람 등록 테이블. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_SCH_CONFIG** | Closing Schedule Configuration. 결산일정 공통 설정 테이블. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_SCH_DISTM** | 결산 일정 배포 마스터 테이블. 배포 Status 보관. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_SCH_EXCEPT** | Super User(예외 기표) 등록 테이블. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_SCH_ID** | Closing Schedule ID Master. Schedule ID 및 통제 속성 보관 테이블. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_SCH_PLAN** | 결산 일정 계획 테이블. 일정 변경(ZLPAC7170/7180)의 기준. | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **ZTPAC_STATUS** | PAC Activity의 결산 상태를 보관하는 테이블. 동기화 배치가 갱신함. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **ZTPAC_STD_LINK** | 표준 모델의 노드 간 연결(링크) 테이블. 선행 노드(P_NODE) → 후행 노드(R_NODE). | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_STD_NODE** | 표준 모델 노드 테이블. ZLPAC0140 조회의 기준 테이블 중 하나. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **ZTPAC_TODO_HIST** | To Do History. 개별 수신 건 아이템 테이블(Key: TDKEY, SEQ, EMPNO, BNAME). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_TODO_STU** | To Do Status. To-Do 발송 헤더 테이블(Key: TDKEY, SEQ). | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_TRIG_LOG** | Trigger 실행 로그 테이블. Auto Trigger 실행 시각, 대상 조직, 실행 모드, 결과 메시지를 기록. SE16에서 오류 원인 파악 시 조회. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPAC_TRIG_ORG** | 조직간 Trigger 매핑 마스터 테이블. TRIG_TYPE='O'인 Trigger Code의 선행/후행 조직 및 Activity 연계 규칙을 정의. | [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| **ZTPACSYS** | PAC System Configuration. TODOIF(Signal 연계) 등 시스템 설정 보관. | [todo](../docs/todo/07-yongeojip-glossary.md#7-용어집-glossary) |
| **결산단위 / 기타조직 (Closing Unit, CUNIT)** | 회사코드·사업영역으로 표현하기 어려운 별도의 결산 관리 단위. ZLPAC0200에서 정의(ZTPAC_CUNIT_MAST). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **모델링(Modeling)** | 결산 작업(Activity)을 노드/링크로 연결해 프로세스 흐름을 정의하는 작업. PAC에서는 네트워크 그래프로 표현. | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **배치 잡(Batch Job)** | 지정 시각에 자동 실행되는 작업. 알람 메일은 예약 배치(ZLPAC7210)로 발송. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **배포 Status** | 일정 배포 단계. New → Saved → Planning Saved → Planning Confirmed → Distributed(Lock). 필드 STATUS(ZTPAC_SCH_DISTM). | [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| **비즈니스 유형 (Business Type, BUSTY)** | 조직의 결산 업무 성격 분류 코드. ZLPAC0013에서 정의. 레벨(BLEVEL) A/C/B/K를 가짐. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **비즈니스 패키지 (Business Package, BUPAK)** | PAC의 결산 시나리오 단위. 조직 레벨(PACLVL)을 가지며 조직이 이 패키지에 배정됨. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **상태 코드 F/W/M/C** | Activity 상태. F=실패, W=경고(재작업), M=수동준비(Manual Ready), C=완료. | [mailing](../docs/mailing/12-burok-b-yongeojip-glossary.md#부록-b-용어집-glossary) |
| **용어 / 약어** | 설명 | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **용어 / 오브젝트** | 설명 | [modeling](../docs/modeling/11-yongeojip-glossary.md#11-용어집-glossary) |
| **조직 레벨 (PACLVL)** | 비즈니스 패키지가 결산을 관리하는 조직 단위. C=회사코드, B=사업영역, U=결산단위. (ZTPAC_CONFIG-PACLVL) | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **조직마스터 (Organization Master)** | 결산을 수행하는 조직·분류 기준 정보. 회사코드·사업영역·결산단위·지역·국가·회사그룹·비즈니스 유형 등을 포함. | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **지역 (Region)** | 결산 현황을 지도/그룹으로 표시하기 위한 지역 분류. ZLPAC0091에서 정의(ZTPAC_REGION). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
| **헤더2라인** | ZLPACMIG010 다운로드 파일 형식. 파일 첫 2행이 테이블명과 필드명으로 구성됨. | [data-migration](../docs/data-migration/08-yongeojip-glossary.md#8-용어집-glossary) |
| **회사그룹 (Company Group, COMGRP)** | 여러 회사코드를 묶는 그룹. ZLPAC0093에서 정의(ZTPAC_COM_GRP). | [org-master](../docs/org-master/08-yongeojip-glossary.md#8-용어집-glossary) |
