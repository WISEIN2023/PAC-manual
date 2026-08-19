---
id: auto-trigger/05-trigger-sudong-jaesilhaeng-reset-bangbeop
doc: auto-trigger
title: 5. Trigger 수동 재실행 (Reset) 방법
parent: docs/auto-trigger/README.md
---

# 5. Trigger 수동 재실행 (Reset) 방법

## 5.1 언제 수동 재실행이 필요한가

- Auto Trigger가 오류로 중단되어 후행 Activity가 기동되지 않은 경우
- 일부 조직 데이터 재작업(Rework) 후 해당 Trigger만 선택적으로 재실행해야 하는 경우
- 테스트 목적으로 특정 Trigger를 수동으로 기동해야 하는 경우

## 5.2 수동 재실행 절차

1. ZLPAC0070 또는 ZLPAC0020에서 재실행할 Trigger 정보 확인    → 확인 항목 : CRSCODE, BUKRS(회사코드), GJAHR(회계연도), MONAT(회계기간)
2. Activity Type 확인 : 'Auto Trigger From Legacy' 여부 확인    → ZLPAC0020에서 해당 Activity의 REPTY(Activity Type) 필드 확인
3. SE37 (Function Module 실행 화면) 실행
4. FM 선택 (아래 표 참조)
5. 파라미터 입력 (아래 표 참조)
6. [실행(F8)] 클릭 → Trigger 기동 후 GCRC Transaction Block까지 자동 수행

| Activity Type | 사용 FM |
|---|---|
| Auto Trigger From Legacy 인 경우 | ZFPAC_AUTOTRIG_LEGACY |
| 그 외 일반 Auto Trigger 인 경우 | ZFPAC_AUTOTRIG_* (유형에 맞는 FM 선택) |

| 파라미터 | 입력 값 | 설명 |
|---|---|---|
| BUKRS | 회사 코드 | 예: 1000 |
| GJAHR | 회계 연도 | 예: 2026 |
| MONAT | 회계 기간(월) | 예: 06 |
| CRSCODE | Trigger Code | ZLPAC0070의 Trigger Definition에서 확인한 CRSCODE |
| MODE | 'E' | E = Execute(실행) 모드. 반드시 대문자 E 입력 |
| EXNAM | CWF 배치 유저 ID | PAC 배치잡 실행 계정 입력 (일반 사용자 ID 사용 불가) |

> 📌 주의 사항
> MODE 파라미터는 반드시 'E'(Execute)로 입력하십시오.
> EXNAM은 CWF 배치 실행 계정을 사용해야 합니다. 잘못된 계정 사용 시 권한 오류가 발생합니다.
> 수동 재실행 전 SM37에서 동일 Trigger의 잡이 실행 중이지 않은지 반드시 확인하십시오.

**5.2.1 Trigger리셋요청시CWF수동재실행상세**

Auto Trigger는 보통 외부 시스템(Legacy 등)에서 자동으로 FM을 호출하여 실행됩니다. 그러나 외부 시스템에서 재호출이 불가능한 상황(시스템 장애, 운영 이슈 등)이면, CWF 배치 계정으로 SE37에서 해당 Function Module을 수동 실행(Reset 재실행)하여야 합니다.

아래 절차에 따라 Trigger 정보를 먼저 확인한 후 해당 FM을 실행합니다.

**① Trigger정보확인**

ZLPAC0070 또는 ZLPAC0020에서 아래 정보를 먼저 확인합니다.

| 확인 항목 | 확인 방법 | 용도 |
|---|---|---|
| Trigger Source Type | ZLPAC0070 조회 → TRIG_TYPE 컬럼 확인 | L/B/S/O 중 어떤 유형인지 파악 → 실행할 FM 결정에 사용 |
| Trigger Define (CRSCODE) | ZLPAC0020 Activity 행의 CRSCODE 또는 TG_CRSCODE 확인 | FM 파라미터 CRSCODE에 입력 |
| BUKRS (회사코드) | Trigger가 발생한 법인의 회사코드 | FM 파라미터 BUKRS에 입력 |
| GJAHR / MONAT | 재실행 대상 회계연도 / 회계기간 | FM 파라미터 GJAHR, MONAT에 입력 |
| Activity Type | ZLPAC0020 > REPTY 필드 | Auto Trigger From Legacy이면 ZFPAC_AUTOTRIG_LEGACY 선택 |

**② Function Module선택및실행**

TRIG_TYPE에 따라 아래 FM을 선택하여 SE37에서 실행합니다.

| TRIG_TYPE | 선택 FM | 비고 |
|---|---|---|
| L (From Legacy) | ZFPAC_AUTOTRIG_LEGACY | Activity Type = Auto Trigger From Legacy인 경우 사용 |
| S (From Other Module) | ZFPAC_AUTOTRIG_OTHERS | SAP 타 모듈 연계 Trigger 재실행 |
| B (Between Business Package) | ZFPAC_AUTOTRIG_CROSS_BUPAK | BP 간 Trigger 재실행 |
| O (Between Organization) | ZFPAC_AUTOTRIG_CROSS_ORG | 조직간 Trigger 재실행 |

SE37 실행 시 아래 파라미터를 입력합니다.

| 파라미터 | 입력 값 | 설명 |
|---|---|---|
| IV_BUKRS | 회사코드 | 예: 1000. Trigger가 발생한 법인의 회사코드 |
| IV_GJAHR | 회계연도 | 예: 2026 |
| IV_MONAT | 회계기간(월) | 예: 06 |
| IV_CRSCODE | Trigger Code | ZLPAC0070/ZLPAC0020에서 확인한 Trigger Define (CRSCODE) 값 |
| IV_MODE | 'E' | 실행 모드. E=Execute(실행). 반드시 대문자 E 입력 |
| IV_EXNAM | CWF 배치 유저 ID | 실행자 계정. 반드시 CWF 배치 유저(예: BATCHCWF001) 입력. 일반 사용자 ID 사용 불가 |

> 📌 주의 사항 (CWF 배치 유저 사용 이유)
> Auto Trigger FM은 백그라운드 잡(배치잡)을 생성하므로, 일반 대화형 계정으로 실행 시 권한 오류가 발생합니다.
> EXNAM에는 반드시 CWF 배치 실행 계정(BATCHCWF001 등)을 입력해야 합니다.
> 수동 실행 전 SM37에서 동일 Trigger의 잡이 이미 실행 중이지 않은지 반드시 확인하십시오.
> FM 실행 후 GCRC Transaction Block까지 자동 연쇄 수행되므로 중간 개입 불필요합니다.

## 5.3 수동 재실행 후 확인 방법

- SM37 (백그라운드 잡 모니터) : 해당 Trigger로 생성된 잡이 정상 완료(Finished) 상태인지 확인
- PAC 모니터 화면 : 후행 Activity의 상태가 수행 중 또는 완료로 변경되었는지 확인
- SM21 (시스템 로그) : 실행 오류 여부 확인
