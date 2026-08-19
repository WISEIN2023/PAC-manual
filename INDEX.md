# PAC 운영자 매뉴얼 마스터 인덱스

SAP 결산자동화 솔루션 **PAC(Process Automatic Channel)** 운영자 매뉴얼 21종의 진입점입니다.
먼저 이 파일에서 대상 문서를 특정한 뒤, **필요한 문서(또는 장) 파일만** 열어보세요.

## 조회 순서

1. 질문에 **프로그램/테이블/함수명**(`ZLPAC*`, `ZTPAC*`, `ZFPAC*`, `ZCL_*`)이 있으면 → 아래 **역인덱스**부터 조회
2. **증상·오류**에 대한 질문이면 → [트러블슈팅 라우팅표](index/troubleshooting.md)
3. **용어 정의**를 묻는 질문이면 → [용어집](index/glossary.md)
4. 그 외에는 아래 **키워드 라우팅** 또는 **문서 목록**에서 문서를 특정

## 역인덱스

| 인덱스 | 대상 | 건수 |
|---|---|---|
| [프로그램 · T-Code](index/programs.md) | `ZLPAC*` `ZIPAC*` | 136 |
| [테이블](index/tables.md) | `ZTPAC*` | 107 |
| [함수 · 클래스](index/functions.md) | `ZFPAC*` `ZCL_*` | 122 |
| [용어집](index/glossary.md) | 통합 용어 | 263 |
| [트러블슈팅](index/troubleshooting.md) | 증상 → 조치 | 114 |

## 키워드 라우팅

| 키워드 | 문서 |
|---|---|
| 권한, 조직권한, Role, SU01, 접근 불가, 법인 안 보임 | [권한 운영자 매뉴얼](docs/authorization/README.md) |
| Config, 설정키, 스위치, ZTPAC_CONFIG, ZTPACSYS | [PAC Config 운영자 매뉴얼](docs/pac-config/README.md) |
| 조직, 회사코드, 사업영역, 지역, 국가, Business Type | [조직마스터 운영자 매뉴얼](docs/org-master/README.md) |
| 로그, Log, 에러 메시지 저장, 좀비 로그, ZCL_PAC_LOG | [Log 관리 프로세스 매뉴얼](docs/log-management/README.md) |
| Activity 정의, 액티비티 마스터, Activity Type, Call Type | [Activity Master 운영자 매뉴얼](docs/activity-master/README.md) |
| 모델링, 표준 모델링, 조직 모델링, 노드, 선후행 | [모델링 운영자 매뉴얼](docs/modeling/README.md) |
| 결산일정, 마감일, 캘린더, Schedule ID, 일정 배포, 알람 | [결산일정 운영자 매뉴얼](docs/closing-schedule/README.md) |
| Job Schedule, 잡 스케줄, 월간 스케줄, 배치 실행 계획 | [Schedule Job 운영자 매뉴얼](docs/schedule-job.md) |
| 자동수행, XAUTO, 자동 실행 흐름 | [PAC 자동수행 운영자 매뉴얼](docs/auto-execution/README.md) |
| Auto Trigger, Trigger Code, CRS Code, 조직간 연계 기동 | [Auto Trigger 운영자 매뉴얼](docs/auto-trigger/README.md) |
| Batch Job 생성, 잡 생성 함수 | [PAC Batch Job 생성 프로세스 운영자 매뉴얼](docs/batch-job.md) |
| REWORK, 재작업, 재수행 감지, Linked Activity | [REWORK 운영자 매뉴얼](docs/rework.md) |
| 결산점검, Closing Inspection, Financial Risk Validation | [Closing Inspection 운영자 매뉴얼](docs/closing-inspection/README.md) |
| 모니터링, 진행현황, 실행시간 초과, 상태 관리 | [모니터링 운영자 매뉴얼](docs/monitoring/README.md) |
| To-Do, 할 일, 미완료 To-Do | [PAC To-Do 운영자 매뉴얼](docs/todo/README.md) |
| 메일, 메일링, HTML 메일 양식, 발송 안 됨 | [메일링 운영자 매뉴얼](docs/mailing/README.md) |
| 공지사항, 첨부파일, 게시 | [공지사항 운영자 매뉴얼](docs/notice.md) |
| APC, 실시간 Refresh, Push Channel, AMC | [APC 운영자 매뉴얼](docs/apc.md) |
| Fiori 버튼, Start, Reset, Confirm, Action 오류 | [Fiori Action 호출 로직 운영자 매뉴얼](docs/fiori-action.md) |
| Fiori에서 SAP GUI 호출, T-Code 호출, 화면 안 뜸 | [피오리 연계 SAP GUI 호출 운영자 매뉴얼](docs/fiori-sapgui-call/README.md) |
| 데이터 이관, Migration, RFC Destination 일괄 변경 | [Data Migration 운영자 매뉴얼](docs/data-migration/README.md) |

## 문서 목록

### 기반설정 — PAC 동작의 토대가 되는 설정·권한·조직·로그 체계

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [PAC Config 운영자 매뉴얼](docs/pac-config/README.md) | Business Package Config(ZTPAC_CONFIG)와 System Config(ZTPACSYS)의 전 설정키를 키별로 설명·참조 프로그램·영향도까지 정리한 설정 사전 | `ZIPAC_COMMON`, `ZIPAC_SYSSCREEN`, `ZLPAC0010`, `ZLPAC0010_F01` |
| [권한 운영자 매뉴얼](docs/authorization/README.md) | PAC 권한 체계 전반. SAP 권한 기본기, PAC 권한 체크 구조, 조직권한, Fiori 화면 권한, 실행/Posting User 개념과 트러블슈팅 | `ZLPAC0010`, `ZLPAC0080`, `ZLPAC0160`, `ZLPAC1000` |
| [조직마스터 운영자 매뉴얼](docs/org-master/README.md) | 지역·국가·회사그룹 등 기초 조직 분류, Business Type 정의, 회사코드/사업영역 조직 마스터, 비즈니스 패키지 조직 배정과 상태 동기화 배치 | `ZLPAC0013`, `ZLPAC0017`, `ZLPAC0018`, `ZLPAC0019` |
| [Log 관리 프로세스 매뉴얼](docs/log-management/README.md) | PAC 로그 설계 원칙, 공통 파라미터, PAC Log 매크로 적용법, ZCL_PAC_LOG 처리 구조, 로그 테이블과 조회 함수, 좀비 로그 정리 | `ZIPAC_COMMON`, `ZLPAC0020`, `ZLPAC0072` |

### 마스터 — 결산 프로세스를 정의하는 마스터 데이터와 일정 구성

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [Activity Master 운영자 매뉴얼](docs/activity-master/README.md) | Activity 3-Level 구조와 Activity Type별 정의 방법, 단계별 셋업 절차(STEP 1~6), 항목별 호출 Function 매핑, 트러블슈팅 | `ZLPAC0010`, `ZLPAC0020`, `ZLPAC0030`, `ZLPAC0040` |
| [모델링 운영자 매뉴얼](docs/modeling/README.md) | 표준 모델링(ZLPAC0030)과 조직 모델링(ZLPAC0040)을 통한 결산 프로세스 구성, 노드 정의·상속·선후행 관계 설정 | `ZLPAC0020`, `ZLPAC0030`, `ZLPAC0031`, `ZLPAC0040` |
| [결산일정 운영자 매뉴얼](docs/closing-schedule/README.md) | Schedule ID 정의(ZLPAC7010), 월별 결산 캘린더(ZLPAC7030), 일정 배포(ZLPAC7100), Super User 등록, 일정 변경 및 알람 설정 | `ZLPAC0020`, `ZLPAC7000`, `ZLPAC7010`, `ZLPAC7020` |
| [Schedule Job 운영자 매뉴얼](docs/schedule-job.md) | Job Schedule 정의(ZLPAC0500)·모니터링(ZLPAC0510)·월간 스케줄 관리(ZLPAC0520)·BP별 실행(ZLPAC0540)과 결산 시작 전 점검 항목 | `ZLPAC0020`, `ZLPAC0100`, `ZLPAC0101`, `ZLPAC0500` |

### 실행·자동화 — 정의된 프로세스를 실행하고 자동으로 이어가는 엔진

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [PAC 자동수행 운영자 매뉴얼](docs/auto-execution/README.md) | 자동수행(XAUTO) 개념과 자동실행 흐름도, 수행 단계별 상세 프로세스, 프로그램 호출관계·선후행·영향도, 핵심 테이블과 설정 스위치 | `ZLPAC0100`, `ZLPAC0101` |
| [Auto Trigger 운영자 매뉴얼](docs/auto-trigger/README.md) | 선행 Activity 완료 시 다른 BP·조직의 후행 작업을 자동 기동하는 Auto Trigger의 설정(ZLPAC0070), 엔진 동작 원리, 수동 재실행 절차 | `ZLPAC0010`, `ZLPAC0010_F01`, `ZLPAC0020`, `ZLPAC0070` |
| [PAC Batch Job 생성 프로세스 운영자 매뉴얼](docs/batch-job.md) | PAC에서 배치 잡이 생성되는 경로별 프로세스 일람(Job 생성 함수와 호출 시점) | `ZLPAC0100`, `ZLPAC0101`, `ZLPAC0150`, `ZLPAC0540` |
| [REWORK 운영자 매뉴얼](docs/rework.md) | 완료된 Activity의 재작업 발생 감지 체계, REWORK Rule 활성화와 점검 주기, Linked Activity 동작, 모니터링 화면 기준 시나리오 | `ZLPAC0020`, `ZLPAC3000`, `ZLPAC3010`, `ZLPAC7191` |
| [Closing Inspection 운영자 매뉴얼](docs/closing-inspection/README.md) | 결산점검 Category(ZLPAC5050)·Scenario(ZLPAC5060) 설정과 점검 수행·모니터링(ZLPAC5200), Financial Risk Validation 대시보드 | `ZLPAC0020`, `ZLPAC5050`, `ZLPAC5060`, `ZLPAC5070` |

### 모니터링·알림 — 수행 현황 조회와 사용자 알림(메일·To-Do·공지)

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [모니터링 운영자 매뉴얼](docs/monitoring/README.md) | 액티비티별·BP별·회사코드별·글로벌 프로세스별 진행현황 모니터링 프로그램, 실행시간 초과 모니터링, 관리자용 상태 관리(ZLPACSTATUSM) | `ZLPAC0160`, `ZLPAC0170`, `ZLPAC7010`, `ZLPACSTATUSM` |
| [PAC To-Do 운영자 매뉴얼](docs/todo/README.md) | To-Do 생성·완료 처리 개념과 유형별 프로세스, 관련 테이블·프로그램, 미완료 To-Do 처리 방법 | `ZLPAC0010`, `ZLPAC0600`, `ZLPAC1000`, `ZLPAC5080` |
| [메일링 운영자 매뉴얼](docs/mailing/README.md) | PAC 메일 종류별 발송 구조와 관련 트랜잭션·함수·클래스, 운영자 발송 설정 절차, HTML 메일 양식 작성 원리, 트러블슈팅 | `ZLPAC0010`, `ZLPAC0600`, `ZLPAC1000`, `ZLPAC7100` |
| [공지사항 운영자 매뉴얼](docs/notice.md) | 공지사항 관리 프로그램(ZLPAC0060)에서의 생성·수정·삭제와 첨부 파일 등록, APC를 통한 Fiori 실시간 반영 구조 | `ZLPAC00020`, `ZLPAC0060` |

### 연계 — Fiori 화면 및 실시간 푸시(APC) 연계 구조

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [APC 운영자 매뉴얼](docs/apc.md) | ABAP Push Channel 기본 개념과 PAC이 사용하는 3개 APC(ZPAC/ZPAC_TODO/ZPAC_NOTICE)의 생성·환경 구성·상세 동작·점검 가이드 | `ZLPAC5100` |
| [Fiori Action 호출 로직 운영자 매뉴얼](docs/fiori-action.md) | Fiori 화면에서 호출되는 Action(권한체크·Start·Reset·Reset From Here·Confirm)의 처리 위치, 파라미터, 내부 로직과 오류 메시지 | - |
| [피오리 연계 SAP GUI 호출 운영자 매뉴얼](docs/fiori-sapgui-call/README.md) | Fiori에서 SAP GUI 트랜잭션을 호출하는 인터페이스(ZLPAC_FTCODE_MAIN)의 셀렉션 파라미터, 분기 로직, 호출 유형별 동작 | `ZLPAC0600`, `ZLPAC5100`, `ZLPAC5200`, `ZLPAC5300` |

### 이관·운영 — 설정·데이터 이관 및 운영 지원 도구

| 문서 | 내용 | 핵심 프로그램 |
|---|---|---|
| [Data Migration 운영자 매뉴얼](docs/data-migration/README.md) | ZLPACMIG010~050 이관 프로그램별 개요·화면·사용법, RFC Destination 일괄 수정 등 운영 주요 작업과 사전 점검 체크리스트 | `ZLPACMIG010`, `ZLPACMIG020`, `ZLPACMIG030`, `ZLPACMIG040` |

## 저장소 통계

- 원본 문서 **21건** → Markdown **200개 파일** (장 단위 분할)
- 본문 489,215자 · 표 538개 · 화면 캡처 295개
- 식별자: 프로그램 136 · 테이블 107 · 함수 106 · 클래스 16
