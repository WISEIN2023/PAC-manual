---
id: data-migration/01-data-migration-gaeyo
doc: data-migration
title: 1. Data Migration 개요
parent: docs/data-migration/README.md
---

# 1. Data Migration 개요

## 1.1 Data Migration이란

Data Migration(데이터 이관)은 PAC 솔루션의 설정 데이터, 마스터 데이터, 결산 프로세스 정의 데이터를 한 SAP 시스템(예: 개발 서버)에서 다른 SAP 시스템(예: 운영 서버)으로 이전하는 작업입니다.

PAC는 독자적인 Migration 전용 프로그램 세트(ZLPACMIG010 ~ ZLPACMIG050)를 제공합니다. 이 프로그램들을 통해 SAP 표준 Transport Request 없이도 Z 테이블의 데이터를 RFC를 통해 시스템 간 직접 이관할 수 있습니다.

> 💡 핵심 포인트<br>• PAC Migration 프로그램은 이름이 Z 또는 Y로 시작하는 커스텀(Z/Y) 테이블의 데이터만 대상으로 합니다.<br>• 이관은 RFC Destination(SM59 등록 목적지)을 통해 원격 시스템에서 데이터를 읽어와 현재 시스템에 저장하는 방식으로 동작합니다.<br>• 개발 시스템(S4D 등)에서는 데이터 삭제 기능이 제한되어 실수로 인한 데이터 손실을 방지합니다.

## 1.2 Migration 프로그램 구성

PAC는 이관 목적에 따라 5개의 Migration 프로그램을 제공합니다.

| 프로그램명 | 설명 | 주요 용도 |
|---|---|---|
| ZLPACMIG010 | TABLE Data Upload/Download | 단일 테이블 데이터를 엑셀/텍스트 파일로 다운로드하거나 파일로부터 업로드 |
| ZLPACMIG020 | Transport Table Data by Business Package | Business Package 단위로 여러 테이블 데이터를 RFC를 통해 타 시스템으로 전송 |
| ZLPACMIG030 | Migration Data for CBO Table | 단일 CBO 테이블 데이터를 RFC로 읽어 현재 시스템에 저장 (ZLPACMIG020에서 내부 호출) |
| ZLPACMIG040 | Migration Data for Multi Table | 여러 테이블을 한 번에 이관 (ZLPACMIG030이 32건 초과 시 자동 호출) |
| ZLPACMIG050 | Migration Data for Business Package | Business Package 범위(다수)를 지정하여 대량 이관 |

## 1.3 이관 프로세스 흐름

일반적인 PAC 데이터 이관 순서는 다음과 같습니다.

1. RFC Destination 확인 (T-Code: SM59) — 원본 시스템으로의 RFC 목적지가 등록되어 있는지 확인합니다.
2. 이관 대상 테이블 및 Business Package 목록 확인 — 주요 프로그램 및 테이블 LIST 시트를 참고합니다.
3. ZLPACMIG020 또는 ZLPACMIG050 실행 — Business Package 단위로 이관을 수행합니다.
4. 이관 결과 확인 — ALV 화면에서 이관된 건수를 확인하거나, 목적 테이블을 SE16N으로 직접 조회합니다.
5. RFC Destination 설정 필요 시 ZLPACMIG030 활용 — ZTPAC_PROC_FUNC 테이블의 RFC Destination 필드를 일괄 수정합니다.
