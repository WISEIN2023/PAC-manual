---
id: fiori-sapgui-call/05-hochul-paramiteo-jeondal-mekeonijeum
doc: fiori-sapgui-call
title: 5. 호출 파라미터 전달 메커니즘
parent: docs/fiori-sapgui-call/README.md
---

# 5. 호출 파라미터 전달 메커니즘

호출 유형과 무관하게 공통으로 적용되는 값 전달·화면 제어 방식입니다. GUI 화면에 조직·기간이 제대로 채워지지 않는 증상을 점검할 때 근거가 됩니다.

## 5.1 SUBMIT WITH SELECTION-TABLE

대부분의 프로그램 호출은 RSPARAMS 내부 테이블(LT_PARAM)에 파라미터명·값을 채워 SUBMIT … WITH SELECTION-TABLE 로 전달합니다. 조직·기간·PID·SCHID 등이 이 방식으로 넘어갑니다.

## 5.2 CALL TRANSACTION + SET PARAMETER ID

트랜잭션형(CALLTYP≠'P') 호출에서는 대상 화면의 입력 필드를 RS_IMPORT_DYNPRO 로 먼저 확인한 뒤, 해당 화면에 실제 존재하는 필드에 한해 SET PARAMETER ID 로 SPA/GPA 파라미터를 채우고 CALL TRANSACTION 합니다.

| 입력 파라미터 | 세팅되는 Parameter ID |
|---|---|
| P_BUKRS | BUK |
| P_GSBER | GSB |
| P_GJAHR | GJA |
| P_MONAT | POPR |
| P_GJAHR + P_MONAT | SPMON (YYYYMM 결합) |

## 5.3 첫 화면 SKIP 제어

실행 시 대상 화면의 첫 셀렉션 화면을 건너뛸지 여부는 다음 규칙으로 결정됩니다.

- 결산점검 트랜잭션(ZLPAC5100 / 5200 / 5300)은 항상 첫 화면을 SKIP.
- 그 외에는 Activity 정의의 XSKIP 값에 따름.

## 5.4 MEMORY ID를 통한 호출 표식 전달

SUBMIT_PID 경로에서는 실행 직전에 PAC 입력 파라미터를 ABAP 메모리에 저장합니다. 이는 대상 화면이 ‘PAC에 의해 호출되었음’을 인지하고 결산 조직·기간 컨텍스트를 이어받게 하기 위한 것입니다.

> PS_PAC_INPUT_PARAM-PAC_CALLED = 'X'. " PAC 호출 표식<br>PS_PAC_INPUT_PARAM-TCODE = LV_TCODE.<br>EXPORT PS_PAC_INPUT_PARAM TO MEMORY ID ZPAC0_INPUT_PARAM.

[코드 5-1] MEMORY ID 전달 (시스템 소스 요약)
