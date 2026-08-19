---
id: data-migration/07-unyeong-yujibosu-jeomgeom-gaideu
doc: data-migration
title: 7. 운영 · 유지보수 점검 가이드
parent: docs/data-migration/README.md
---

# 7. 운영 · 유지보수 점검 가이드

## 7.1 이관 전 사전 점검 체크리스트

| 점검 항목 | 확인 방법 | 정상 기준 |
|---|---|---|
| RFC Destination 등록 확인 | T-Code SM59에서 목적지명 검색 | 목적지 존재 및 연결 테스트 성공 |
| 이관 대상 테이블 확인 | SE16N 또는 SE11에서 테이블명 조회 | Z/Y 시작 테이블만 이관 가능 |
| 테이블 구조 동일 여부 | ZLPACMIG020의 테이블 구조 체크(P_DBCHK) 기능 활용 | "DB structure is identical" 메시지 확인 |
| 개발 시스템 여부 확인 | SY-SYSID 값 확인 (프로그램 내부에서 자동 체크) | 운영/품질 시스템에서만 삭제 기능 활성 |
| Business Package 유효성 | ZTPAC_BUPAK 테이블에서 BP코드 확인 | 이관 대상 BP가 테이블에 존재 |

## 7.2 증상별 점검 가이드

| 증상 | 우선 점검 사항 | 조치 방법 |
|---|---|---|
| "Destination XXX does not exist" 오류 | SM59에서 RFC 목적지 등록 여부 확인 | 목적지 등록 후 재시도 |
| "Z로 시작하는 테이블명만 사용가능" 오류 | 입력한 테이블명이 Z/Y 시작인지 확인 | 올바른 CBO 테이블명으로 수정 |
| "Table layout does not match" 오류 | 원본/목적 시스템 간 테이블 구조 불일치 | TR로 테이블 구조 먼저 이관 후 재시도 |
| 이관 후 데이터가 없음 | Business Package 조건, Where Condition 확인 | BP 또는 조건 값 재확인 후 이관 |
| ALV 화면에서 저장 안 됨 | Lock 잔류 여부 확인 (SM12) | SM12에서 Lock 항목 확인 후 해제 |
| RFC Destination 설정 오류 (Function) | ZTPAC_PROC_FUNC 테이블의 RFC Destination 값 확인 | ZLPACMIG030 Modify 모드로 일괄 수정 |

## 7.3 데이터 삭제 시 주의사항

> ⚠ 데이터 삭제 관련 중요 안내<br>• 데이터 삭제(Table Data Delete) 기능은 개발 시스템(S4D)에서는 비활성화됩니다. 개발 시스템에서 실행 시 삭제가 수행되지 않습니다.<br>• Business Package를 지정하지 않으면 테이블의 모든 데이터가 삭제됩니다. 반드시 이관 범위를 확인 후 실행하십시오.<br>• 삭제 후 복구는 어렵습니다. 이관 전 필요에 따라 ZLPACMIG010의 Download 기능으로 기존 데이터를 백업하십시오.
