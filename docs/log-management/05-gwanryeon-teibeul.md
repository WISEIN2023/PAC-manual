---
id: log-management/05-gwanryeon-teibeul
doc: log-management
title: 5. 관련 테이블
parent: docs/log-management/README.md
---

# 5. 관련 테이블

로그 처리 과정에서 데이터가 저장·조회되는 주요 테이블은 다음과 같다.

## 5.1 로그 테이블 목록

| 테이블명 | 설명 | 처리 유형 | 용도 |
|---|---|---|---|
| ZTPAC_LOG_HDR | Log Header (로그 헤더) | S/I/U/D | 로그 1건당 헤더 저장. Log ID, 수행자, 상태, 시작/종료 시간, Batch Job, IP, 프로그램 ID 관리 (핵심 테이블) |
| ZTPAC_LOG_DTL | Log Detail (로그 본문) | S/I | 개별 로그 메시지 저장. Log Sequence, 메시지 Class/번호/텍스트, 파라미터(PARAM1~4), 타임스탬프 (핵심 테이블) |
| ZTPAC_LOG_STACK | Log Stack (호출 스택) | S/I | 오류 발생 시 ABAP Call Stack 저장. 오류 발생 위치 추적 (디버깅 용도) |
| ZTPAC_LOG_SCREEN | Execution Screen Parameter Log | I | 실행 시 입력된 Selection Screen 파라미터값을 로그 단위로 저장. 재실행·이력 확인에 활용 |
| ZTPAC_RUNNING | Running Program List | I/D | 현재 실행 중인 PAC 프로그램 실시간 관리. 좀비 판별 기준이며 정상 종료 시 삭제 |
| ZTPAC_STATUS | PAC Activity Status | S/U | Activity별 현재 진행 상태와 진행 중 Log ID 관리. 운영 맵 상태 표시의 기준 |
| ZTPAC_CONFIG_LCK | Lock Definition | S | 비즈니스 패키지별 Lock Key 구성 규칙(필드·순서) 정의 |
| ZTPAC_LOG_BLMSG | Success Doc Message Master | S | 전기 문서 생성을 의미하는 메시지(MSGID/MSGNR) 기준. 발생 시 헤더 STYPE을 'P'로 표시 |
| ZTPAC_HELP_USED | Error Help - Where Used List | M | 어떤 프로그램에서 어떤 메시지를 사용했는지 누적 기록. 메시지별 사용 현황 분석 |

처리 유형 약어 : S(SELECT), I(INSERT), U(UPDATE), D(DELETE), M(MODIFY)

## 5.2 핵심 테이블 주요 필드

### 5.2.1 ZTPAC_LOG_HDR (Log Header)

| 필드 | Data Element | 설명 |
|---|---|---|
| LOGID | ZPAC_LOG_ID | Log ID (Key) |
| BUPAK | ZPAC_BUPAK | Business Package |
| GJAHR / MONAT | GJAHR / MONAT | 회계연도 / 월 |
| BUKRS / GSBER | BUKRS / GSBER | 회사 코드 / 사업영역 |
| EXEMODE | ZPAC_EXE_MODE | 수행 모드 (A: Actual 등) |
| TCODE / PID | TCODE / ZPAC_PID | T-Code / PAC ID |
| STATUS | ZPAC_STATUS | 로그 상태 (S/R/C/F/A/K) |
| STYPE | CHAR01 | 전기 문서 여부 등 유형 (P: 전기 관련) |
| EXETM | /SDF/CMO_SEC | 총 수행 시간(초) |
| BATCH_JOBNAM / JOBCOUNT | BTCJOB / BTCJOBCNT | Batch Job 명 / Job 카운트 |
| HOSTIP | ZPAC_LOG_HOSTIP | 수행 Host IP |
| EXNAM | ZPAC_EXNAM | 수행 사용자 |
| ERDAT_L / ERZET_L | ERDAT / ERZET | 로그 생성 일자 / 시각 |

### 5.2.2 ZTPAC_LOG_DTL (Log Detail)

| 필드 | Data Element | 설명 |
|---|---|---|
| LOGID | ZPAC_LOG_ID | Log ID (Key) |
| LOGSEQ | ZPAC_LOG_SEQ | Log Sequence (Key) |
| LOGCASE | ZPAC_LOG_CASE | 로그 케이스 (I/W/C/F/K 등) |
| MSGTYP | ZPAC_MSG_TYPE | 메시지 유형 |
| MSGID / MSGNR | MSGID / MSGNR | 메시지 Class / 번호 |
| LOGMSGTXT | ZPAC_LOG_MSGTXT | 로그 메시지 본문 텍스트 |
| PARAM1 ~ PARAM4 | SYST_MSGV | 메시지 파라미터 값 |
| ERDAT_L / ERZET_L | ERDAT / ERZET | 메시지 생성 일자 / 시각 |
