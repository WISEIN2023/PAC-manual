---
id: auto-execution/05-haeksim-teibeul-seoljeong-seuwichi
doc: auto-execution
title: 5. 핵심 테이블 · 설정 스위치
parent: docs/auto-execution/README.md
---

# 5. 핵심 테이블 · 설정 스위치

## 5.1 핵심 테이블

| 테이블 | 설명 | 자동수행에서의 역할 |
|---|---|---|
| ZTPAC_PROC | Activity 정의 마스터 | 각 Activity(PID)의 실행 프로그램(TCODE), 유형(REPTY), 자동여부(XAUTO), Variant, 트리거(CRSCODE), Skip/Final 등 정의. 실행 방식의 원천. |
| ZTPAC_CONFIG | Business Package 글로벌 설정 | 패키지별 동작 스위치(조직레벨·Precheck·Rework·Final·AutoStart·전기유저 등). 자동수행 거동을 결정. |
| ZTPACSYS | 배치 밸런싱 설정 | 서버그룹(TARGET_GRP)과 레벨별 허용율(RATE_*), 대기시간(WAIT_TIME). 배치잡 생성량 조절의 기준. |
| ZTPAC_STATUS | Activity 실행 상태 | 조직·년월·PID별 현재 상태(R/C/T/P/O/E/W). 수행 가능 계산·완료 판정의 기준. |
| ZTPAC_LOG_HDR | 실행 로그 헤더 / Job 매핑 | LOGID와 실제 배치잡(BATCH_JOBNAM/JOBCOUNT)을 매핑. 실행 중 Job 추적에 사용. |
| ZTPACJOBS | 자동수행 Job 이력 | ZLPAC0100/0101 실행 시 생성되는 Running History. Job 생성 이력 관리. |
| ZTPAC_GPID | Global Package 구성 | GPID와 소속 Business Package(및 Main) 매핑. Global 레벨 수행 대상 산출. |
| ZTPAC_CLOSE | Business Package 마감 | 패키지 월마감 기록. CHECK_BUPAK_CLOSE의 판정 소스. |
| ZTPAC_CROSS_IF | 트리거 인터페이스 정의 | CRSCODE별 Inbound/Outbound·TRIG_TYPE(B/O)·대상 패키지. Auto Trigger 분기의 기준. |
| ZTPAC_PROC_RCLOS / ZTPAC_SCH_* | 결산일정 연계·일정 | Activity와 Closing Schedule(SCHID) 연결 및 일정 계획/확정. 마감 판정에 사용. |
| TBTCO / TBTCP | SAP 표준 배치잡 헤더/스텝 | 실제 배치잡의 상태(R/S/Y/A/F) 조회. 실행중·중복·중단 판단에 사용. |
| TSTC | 트랜잭션→프로그램 매핑 | TCODE에 할당된 실행 프로그램(PGMNA) 조회. ZLPAC0101이 실제 프로그램을 찾을 때 사용. |

## 5.2 ZTPAC_CONFIG 주요 스위치 (Business Package 동작 제어)

| 필드 | 의미 | 자동수행 영향 |
|---|---|---|
| PACLVL | 조직 레벨(C:회사 / B:회사+BA / U:기타) | JobName·조직 정규화·마감 기준 단위를 결정. |
| XPRE_USE / PRE_PID | Precheck 사용 여부 / 대상 Activity | 사용 시 사전점검 완료 전에는 자동수행 차단. |
| XSCH_USE | 결산일정(Schedule) 사용 여부 | 미사용 시 일정 마감 체크 일부를 생략. |
| XREWORK / RWTMOUT | Rework 사용 / 타임아웃 | 완료 후 재처리(Rework) 허용 및 감시 시간. |
| ACT_XFINAL / XFINAL_CHK | Final Activity 사용 / 완료 강제 체크 | Final 종료 전 타 Activity 완료를 강제(미완료 시 오류). |
| USER_TYPE / POST_USER | 전기유저 방식(A실행자/R역할/F고정) / 고정유저 | Posting User 결정 규칙. |
| XAUTO_START | Always Start(선행 무관 자동) | 설정 시 Auto Next를 자동 적용. |
| AFTER_CONF | 수기 확정 후 자동수행 | 확정 후 NEXT_AUTO_START로 후행 자동 진행. |
| XAUTO_NEXT / XSKIP_MIDDLE | 다음 자동 / 중간 Skip | 후행 자동 개시 및 중간 노드 건너뛰기 제어. |

## 5.3 ZTPAC_PROC 주요 필드 (Activity 정의)

| 필드 | 의미 | 비고 |
|---|---|---|
| REPTY | Activity 유형 | C:Closing Schedule, M:Dummy(자동확정), S:Group, X:Trigger, F/T:일반 등. 유형별 처리 분기. |
| XAUTO / AUTO_ONLY | 자동수행 대상 / 자동전용 | XAUTO 아닌 PID는 백그라운드 자동수행 불가(ZLPAC0101에서 차단). |
| TCODE / VARIANT / XVARIANT_EX | 실행 트랜잭션 / Variant / Variant Exit | 실제 실행 프로그램과 파라미터 원천(SET_EXEC_PARAM). |
| CRS_INOUT / CRSCODE / TG_CRSCODE | 트리거 In/Out / 코드 / 대상코드 | Auto Trigger 연계 정의(AUTOTRIG 분기 기준). |
| FINAL / XSKIP | Final 여부 / Period Skip | Final Activity·기간 Skip 처리 대상 여부. |
| ROOT_PCSGP / PCSGP | 최상위/소속 Activity Group | 노드 계층·JobName 구성에 사용. |

## 5.4 ZTPACSYS 밸런싱 파라미터

| 필드 | 의미 | 영향 |
|---|---|---|
| TARGET_GRP | 대상 서버 그룹 | 밸런싱 계산 대상 배치 서버 범위. |
| RATE_PCSGP / RATE_ACT / RATE_PID | 레벨별 허용율(%) | 유휴율이 이 값 미만이면 생성 대기/보류. 값이 낮을수록 더 공격적으로 생성. |
| WAIT_TIME | 대기 시간(초) | 여유 부족 시 재시도 간격. 배치잡 생성 시 과부하 방지. |
