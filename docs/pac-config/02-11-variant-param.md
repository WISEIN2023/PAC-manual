---
id: pac-config/02-11-variant-param
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.11 Variant&Param
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.11 Variant&Param

### 2.11.1 PARNOMODI — Forbid modifying Screen parameters

**테이블-필드:** ZTPAC_CONFIG - PARNOMODI

**운영 설정(LG전자 특화) :** 운영은 모두 설정

#### 설정 설명

- 스크린 파라미터 수정 금지여부를 정의

- X 설정된 경우 PAC 로그가 정용된 겨우 스크린 Variant를 설정 할 수 없도록 한다.

- ZIPAC_COMMON 프로그램내 아래 위치에서 차단

AT SELECTION-SCREEN OUTPUT.

_PAC_SET_SCREEN.

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(FORM PARAMETER_INPUT_CHECK), ZCL_PAC_SAIL=>GET_PARAM_FOR_LOG(CM00H) 연계

#### 프로세스 관점 분석 (사용 로직)

자동화 대상 Activity의 스크린 파라미터 수정 금지 여부.

① ZIPAC_COMMON PARAMETER_INPUT_CHECK: 'X'이고 PAC 경유 CALL 실행이며 자동수행(XAUTO='X') Activity인 경우, GET_PARAM_FOR_LOG로 로그에 매핑된 파라미터를 조회하여 스크린 파라미터 입력을 차단(SIMUL 매핑 파라미터 예외, Relative 호출 제외).

② 목적: PAC가 세팅한 Variant/파라미터를 사용자가 포그라운드에서 임의 변경하여 다른 조건으로 수행되는 것을 방지.

#### 영향도 분석 (변경 시 영향)

해제 시 자동화 Activity를 포그라운드로 열어 파라미터를 임의 변경·실행할 수 있게 되어 실행 조건 무결성이 깨질 수 있음(잘못된 범위 기표 위험).

활성 시 예외적으로 조건 변경이 필요한 상황에서는 Variant 수정으로만 대응 가능.

### 2.11.2 VARONOFF — Std Variant Off

**테이블-필드:** ZTPAC_CONFIG - VARONOFF

**운영 설정(LG전자 특화) :** 운영은 모두 설정

#### 설정 설명

- Std Variant Off여부

- X설정된 경우 Activity 포그라운드 실행시 Standard Variant를 선택할 수 없도록 함으로 다른 Variant로 수행되는것을 차단한다.

- ZIPAC_COMMON 프로그램내 아래 위치에서 차단

AT SELECTION-SCREEN OUTPUT.

_PAC_SET_SCREEN.

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(FORM VARIANT_OFF_CHECK)

#### 프로세스 관점 분석 (사용 로직)

Standard Variant 기능 Off 여부.

① ZIPAC_COMMON VARIANT_OFF_CHECK: 'X'이면 Activity 포그라운드 실행 시 선택화면 PF-STATUS에서 'GET'(Get Variant)/'SPOS'(Save as Variant) 기능코드를 RS_SET_SELSCREEN_STATUS로 제거 → 저장된 Variant 불러오기/저장 차단.

② PARNOMODI와 함께 자동화 파라미터 무결성을 보장하는 장치.

#### 영향도 분석 (변경 시 영향)

해제 시 사용자가 개인 Variant를 불러와 PAC가 세팅한 조건을 덮어쓸 수 있음 — 자동화 파라미터 통제가 약화됨.

활성 시 사용자 편의(개인 Variant 활용)는 제한됨.
