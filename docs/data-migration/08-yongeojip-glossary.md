---
id: data-migration/08-yongeojip-glossary
doc: data-migration
title: 8. 용어집 (Glossary)
parent: docs/data-migration/README.md
---

# 8. 용어집 (Glossary)

본 문서에 등장하는 주요 용어와 약어를 정리합니다.

| 용어 / 약어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. 본 문서의 대상인 SAP 결산자동화 솔루션. |
| Data Migration | 데이터 이관. SAP 시스템 간 테이블 데이터를 전송하는 작업. |
| Business Package (BP, BUPAK) | PAC 결산 프로세스의 업무 단위. 법인·결산 범위를 묶는 식별자. |
| RFC (Remote Function Call) | 원격 함수 호출. SAP 시스템 간 네트워크를 통해 함수를 호출하는 표준 방식. |
| RFC Destination | SM59에 등록된 원격 SAP 시스템 접속 정보. 이관 시 원본 시스템으로의 연결 경로. |
| SM59 | RFC 연결 목적지를 관리하는 SAP 표준 트랜잭션. |
| Interface 모드 | ZLPACMIG030에서 RFC를 통해 원격 시스템 데이터를 읽어오는 모드. |
| Modify 모드 | ZLPACMIG030에서 현재 시스템의 테이블 데이터를 직접 조회·수정하는 모드. |
| CBO Table (Z/Y 테이블) | Customer Build Object. SAP 표준이 아닌 고객사가 개발한 커스텀 테이블. Z 또는 Y로 시작. |
| ZTPAC_PROC_FUNC | PAC Activity의 Function(함수) 실행 정의를 저장하는 PAC CBO 테이블. |
| ZTPAC_BUPAK | PAC Business Package 마스터 테이블. |
| ALV (ABAP List Viewer) | SAP ABAP 표준 목록 출력 및 편집 컴포넌트. 데이터 확인·수정 화면. |
| SE16N | 테이블 데이터를 조회하는 SAP 표준 트랜잭션 (테이블 데이터 브라우저). |
| SE38 / SA38 | ABAP 프로그램을 실행하는 SAP 표준 트랜잭션. |
| SM12 | SAP 잠금(Lock) 항목을 조회·관리하는 표준 트랜잭션. |
| S4D / S4H | 각각 SAP S/4HANA 개발 시스템 / 운영 시스템의 예시 SYSTEM ID. 실제 환경에 따라 다름. |
| Where Condition | SQL WHERE 절에 해당하는 조회 조건. 특정 데이터 범위만 필터링할 때 사용. |
| Save without Screen | ALV 확인 화면 없이 즉시 저장하는 옵션. 대량 이관 자동화 시 활용. |
| SUBMIT | ABAP에서 다른 프로그램을 실행하는 구문. ZLPACMIG020은 ZLPACMIG030을 SUBMIT으로 호출. |
| TR (Transport Request) | SAP 변경 전송 요청. 개발 → 품질 → 운영 순서로 Workbench/Customizing 변경을 이관. |
| Function Type (Activity) | PAC Activity Type 중 하나. RFC를 통해 외부 서버의 함수(Function)를 직접 실행하는 방식. |
| 헤더2라인 | ZLPACMIG010 다운로드 파일 형식. 파일 첫 2행이 테이블명과 필드명으로 구성됨. |

— 문서 끝 —
