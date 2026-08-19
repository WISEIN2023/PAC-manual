---
id: monitoring/03-aektibitibyeol-moniteoring-zlpac-monitor-act
doc: monitoring
title: 3. 액티비티별 모니터링 — ZLPAC_MONITOR_ACT(LG제외)
parent: docs/monitoring/README.md
---

# 3. 액티비티별 모니터링 — ZLPAC_MONITOR_ACT(LG제외)

**소스 설명 :** Monitoring by Activity. 하나의 비즈니스 패키지 안에서 액티비티(PID) 단위까지 진행 상황을 트리로 상세하게 보여주는 프로그램입니다. 조회 레벨 기본값이 '액티비티(A)'로 설정되어 있어 가장 상세한 단위까지 펼쳐 보는 데 적합합니다.

## 3.1 선택화면 항목

| 구분 | 필드 | 설명 |
|---|---|---|
| 기본검색 | P_BUPAK | 비즈니스 패키지 (필수) |
|  | S_COMGRP / S_REGION | 회사그룹 / 지역 |
|  | S_BUKRS / S_GSBER / S_CUNIT | 회사코드 / 사업영역 / 결산단위 |
|  | P_GJAHR / P_MONAT | 회계연도 / 회계기간(월) |
| 조회옵션 | P_D_ACT | Display Activity (기본 체크). 액티비티 레벨 표시 여부 |
|  | P_LVL | 조회 레벨 리스트박스 (G 그룹 / S 서브그룹 / A 액티비티, 기본 A) |
|  | S_PCSGP / S_PCSUB / S_PID | 액티비티 그룹 / 서브그룹 / 액티비티 (각 단일 값만 입력) |
|  | P_TIMER / P_MINUTE / P_MAXTM | 자동 새로고침 사용 / 주기(분) / 종료(분) |
|  | P_D_STXT | Display Status Text (상태 텍스트 표시) |

> 보완 설명 (MCP 검증)<br>S_PCSGP / S_PCSUB / S_PID 는 INITIALIZATION 단계에서 SELECT_OPTIONS_RESTRICT 함수로 '단일 값(EQ)'만 허용하도록 제한됩니다. 범위·구간 입력은 불가합니다.<br>P_D_COMG(Display Company Group), P_D_REG(Display Region) 항목은 소스 주석상 이 프로그램에서는 미사용(‘미사용’) 표기되어 있습니다.<br>회계연도·월이 비어 있으면 ZCL_PAC_FUNC=>GET_DEFAULT_PERIOD 로 기본 결산 기간이 자동 설정됩니다.

## 3.2 처리 흐름

실행(START-OF-SELECTION) 시 다음 순서로 동작합니다.

- ① GET_AUTH_ORG_MAST — 권한 있는 조직 마스터 읽기
- ② READ_TEXT_TABLE — 상태 도메인 등 텍스트 테이블 읽기
- ③ READ_DATA — ZFPAC_PAC_MONITOR 호출 결과로 트리용 기준 데이터(GT_ALV9) 구성
- ④ START_TIMER — P_TIMER 체크 시 자동 새로고침 타이머 시작
- ⑤ CALL SCREEN 100 — ALV 트리(CL_GUI_ALV_TREE) 표시

## 3.3 운영 시 참고

- 트리 아이콘·색상·상태 버튼·건수 더블클릭 동작은 2장 공통 기반과 동일합니다.
- 자동 새로고침 시에는 변경된 노드만 갱신되며 화면 하단에 'The data has been refreshed.' 메시지가 표시됩니다.
