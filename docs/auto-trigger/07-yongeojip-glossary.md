---
id: auto-trigger/07-yongeojip-glossary
doc: auto-trigger
title: 7. 용어집 (Glossary)
parent: docs/auto-trigger/README.md
---

# 7. 용어집 (Glossary)

본 문서에서 사용한 주요 용어를 정리합니다.

| 용어 / 약어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. SAP 결산자동화 솔루션. |
| Auto Trigger | 선행 Activity 완료 시 후행 Activity/BP를 자동으로 기동하는 PAC 메커니즘. |
| Trigger Code (CRSCODE) | Auto Trigger 설정의 고유 식별자. ZTPAC_CROSS_IF 테이블의 키 값. |
| Trigger Definition | ZLPAC0020에서 Activity에 연결하는 Trigger Code. Inbound/Outbound 구분. |
| XAUTO (Auto Next) | ZTPAC_CROSS_IF의 자동수행 플래그. 'X'=자동, 공백=수동. |
| AUTO_TYPE | 자동수행 범위. A=Activity, B=Business Package, G=Activity Group. |
| TRIG_TYPE | Trigger 발생 유형. L=Legacy, B=BP간, S=타모듈, O=조직간. |
| Business Package (BUPAK) | PAC의 최상위 업무 단위. 복수의 Activity Group과 Activity로 구성. |
| PCSGP | Process Sub-Group. PAC에서 Activity들이 속하는 프로세스 그룹 단위. |
| ZTPAC_PROC | Activity Definition Master 테이블. Activity의 모든 속성 저장. |
| ZTPAC_CROSS_IF | Cross System Trigger Master 테이블. Trigger Code 속성 저장. |
| ZCL_PAC_SAIL | PAC 자동화 실행 엔진 클래스. START_FROM_AUTO_TRIGGER 메서드로 Auto Trigger 수행. |
| ZFPAC_GET_CAN_START | 후행 Activity 수행 가능 여부를 판단하는 Function Module. |
| ZFPAC_CREATE_PCSGP_JOB | 지정된 PCSGP를 백그라운드 잡으로 기동하는 Function Module. |
| ZFPAC_AUTOTRIG_LEGACY | Legacy 유형 Trigger의 수동 재실행에 사용하는 Function Module. |
| IV_AUTO_NEXT / AV_AUTO_NEXT | ZCL_PAC_SAIL CONSTRUCTOR 파라미터 및 내부 변수. 'X'여야 자동수행 로직 활성화. |
| BUKRS | 회사 코드(법인). SAP 표준 필드. |
| GJAHR | 회계 연도. SAP 표준 필드. |
| MONAT | 회계 기간(월). SAP 표준 필드. |
| SE37 | SAP Function Module 직접 실행 트랜잭션. 수동 재실행 시 사용. |
| SM37 | SAP 백그라운드 잡 모니터 트랜잭션. |
| SM21 | SAP 시스템 로그 조회 트랜잭션. |
| CWF 배치 유저 | PAC 배치잡 실행 전용 계정. 수동 재실행 시 EXNAM 파라미터에 입력. |
| GCRC Transaction Block | Trigger 실행 후 자동으로 수행되는 후행 트랜잭션 묶음. |
| Rework | 이미 완료된 Activity를 다시 수행하는 재작업 기능. |
| ZTPAC_TRIG_LOG | Trigger 실행 로그 테이블. Auto Trigger 실행 시각, 대상 조직, 실행 모드, 결과 메시지를 기록. SE16에서 오류 원인 파악 시 조회. |
| ZTPAC_TRIG_ORG | 조직간 Trigger 매핑 마스터 테이블. TRIG_TYPE='O'인 Trigger Code의 선행/후행 조직 및 Activity 연계 규칙을 정의. |
| ZLPAC0010 | Maintain Business Package Config. Business Package 전역 설정 트랜잭션. Auto Trigger 자동 수행을 위한 XAUTO_START 등 설정. |
| XAUTO_START | ZTPAC_CONFIG의 'Always auto start after completed' 필드. X 체크 시 AFTER_CONF/AFTER_CLSD/XAUTO_NEXT/CONFLVL이 자동 설정됨. |
| ZFPAC_AUTOTRIG_CHECK | Auto Trigger 사전 유효성 검증 FM. Trigger Code 존재, 조직/Period 유효성, 수행 가능 여부를 일괄 검증. |
| ZFPAC_AUTOTRIG_CROSS_BUPAK | TRIG_TYPE=B(BP간) Trigger 실행 FM. Outbound 완료 후 Inbound BP의 후행 Activity를 기동. |
| ZFPAC_AUTOTRIG_CROSS_ORG | TRIG_TYPE=O(조직간) Trigger 실행 FM. 동일 BP 내 서로 다른 조직 간 Trigger 수행. |
| ZFPAC_AUTOTRIG_OTHERS | TRIG_TYPE=S(타 모듈) Trigger 실행 FM. SAP 비PAC 업무(MM,SD 등)에서 호출 시 사용. |
| START FROM | ZCL_PAC_SAIL의 IV_START_FROM 파라미터. 지정 PID부터 해당 라인만 선택적으로 실행하는 모드. |
| START ALL | ZCL_PAC_SAIL의 기본 실행 모드. IV_START_FROM 미입력 시 수행 가능한 모든 Activity를 순차 수행. |
| BATCHCWF001 | CWF 배치 실행 계정. Auto Trigger FM 수동 재실행 시 EXNAM 파라미터에 입력하는 배치 전용 계정. |
| ZFPAC_CHECK_PRENODE | AUTO_TYPE=B 시 선행 Activity 완료 여부를 추가 검증하는 FM. EV_SUBRC=0이어야 후행 기동. |

--- 문서 끝 ---
