---
id: fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu
doc: fiori-sapgui-call
title: 6. 운영 · 유지보수 점검 가이드
parent: docs/fiori-sapgui-call/README.md
---

# 6. 운영 · 유지보수 점검 가이드

Fiori에서 GUI 화면이 열리지 않거나 값이 잘못 전달되는 증상이 보고될 때, 아래 순서로 점검하면 원인 범위를 좁힐 수 있습니다.

## 6.1 정상 동작 확인 체크리스트

| 점검 항목 | 확인 방법 | 정상 기준 |
|---|---|---|
| 진입 트랜잭션 | SE93에서 ZLPAC_FTCODE 존재·활성 확인 | T-Code가 프로그램 ZLPAC_FTCODE에 연결 |
| Activity 정의 | ZTPAC_PROC 에서 해당 BUPAK·PID 행 조회 | TCODE/CALLTYP/REPTY 등 정의값 존재 |
| 대상 트랜잭션 유효성 | SE93 / TSTC에서 대상 T-Code의 실행 프로그램 확인 | PGMNA·DYPNO 정상 등록 |
| 권한 | 대상 트랜잭션 실행 권한(S_TCODE 등) 확인 | 호출 사용자에게 실행 권한 부여 |

## 6.2 증상별 점검 가이드

| 증상 | 우선 점검 사항 |
|---|---|
| Fiori에서 아무 화면도 열리지 않음 | ① 진입 T-Code ZLPAC_FTCODE 연결/권한 ② ZTPAC_PROC 정의행 존재 ③ 전달 파라미터(BUPAK·PID) 값 여부 |
| 엉뚱한 화면이 열림(분기 오판) | 입력 파라미터 조합 확인 : P_RTYPE·P_TDTYPE·P_TCODE·P_PID·P_CID 우선순위(3.1)에 따른 분기 결과 점검 |
| 결산일정 변경이 안 열림 | ① 정의의 REPTY='C' 여부 ② GET_SCHID_BY_PID 반환 일정 ID 존재 ③ ZLPAC7170 유효성 |
| To-Do가 안 열림 | ① P_TDTYPE 전달값 ② ZLPAC0600 유효성 |
| 화면은 열리나 조직·기간이 비어 있음 | ① SET PARAMETER ID 매핑(5.2) ② 대상 화면에 해당 입력 필드 존재 ③ MEMORY ID ZPAC0_INPUT_PARAM 전달 |
| 레거시 링크가 안 열림 | ① 정의의 LEGACY_RFC/URL 값 ② ZFPAC_LEGACY_LINK 정상 여부 |
| 첫 화면이 예상과 다르게 뜨거나 건너뜀 | Activity 정의의 XSKIP 값 및 결산점검 트랜잭션 여부(5.3) 확인 |

> ⚠ 주의 — Activity 정의 변경<br>ZTPAC_PROC의 REPTY·CALLTYP·TCODE·LEGACY_* 값은 호출 분기를 직접 결정합니다. 정의값을 변경하면 동일한 Fiori 조작이라도 다른 화면·다른 방식으로 호출될 수 있으므로, 운영계 반영 전 반드시 품질계에서 호출 결과를 검증하십시오.
