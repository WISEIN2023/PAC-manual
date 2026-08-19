---
id: log-management/02-gongtong-paramiteo
doc: log-management
title: 2. 공통 파라미터
parent: docs/log-management/README.md
---

# 2. 공통 파라미터

로그를 적용하려면 자동 수행에 필요한 조직 정보와 기간 정보가 반드시 입력되어야 한다. 이를 '필수 공통 파라미터'라 부른다. 공통 파라미터는 사전 정의된 스크린 파라미터에 입력되며, 이 값이 모두 입력된 경우에만 로그 수행이 가능하다.

## 2.1 필수 공통 파라미터

결산에 필요한 파라미터는 약속된 파라미터 이름을 사용하는 것이 권장 사항이나, 다른 파라미터 명을 사용하더라도 Activity Master의 파라미터 Set-up을 통해 예외처리가 가능하다. 비즈니스 패키지별로 사용하는 조직 파라미터는 상이할 수 있다.

| 구분 | 파라미터 (Type) | 설명 |
|---|---|---|
| 조직정보 | P_BUKRS TYPE BUKRS | Company Code(회사 코드) |
| 기간정보 | P_GJAHR TYPE GJAHR | Fiscal Year(회계연도) |
|  | P_MONAT TYPE MONAT | Month(월, 2자리) |
|  | P_SPMON TYPE SPMON | Period(회계연도+월, 6자리) |
| 시뮬레이션 | P_SIMUL TYPE ZPAC_SIMUL<br>(AS CHECKBOX) | X : Simulation, 공란 : Actual Run |

## 2.2 공통 파라미터 설정 방법

1. **Global /비즈니스 패키지 공통 설정 —** ZLPAC0072 (Define Common Log Parameter)에서 설정한다. Business Package가 비어 있으면 Global로 전체 업무에 공통 적용되고, Business Package는 등록되었으나 PAC ID·Program이 등록되지 않으면 해당 비즈니스 패키지에 공통 적용된다.
2. **PID·Program별 특화 설정 —** Global 및 비즈니스 패키지 공통으로 적용이 어려운 경우, ZLPAC0020 (Activity Master) 우측 화면에서 'Parameter'를 호출하여 PID별로 입력한다.
등록된 스크린 파라미터가 프로그램에 존재하면 Log Field의 의미에 따라 파라미터 값이 입력된다. Log Field별 의미는 다음과 같다.

| Log Field | 의미 | Log Field | 의미 |
|---|---|---|---|
| BUKRS | Company Code | GJAHR | Fiscal Year |
| BUPAK | Business Package | MONAT | Month |
| GSBER | Business Area | SPMON | Fiscal Year + Month |
| CUNIT | Other Organization | PID | PAC ID |
| SIMUL | Simulation |  |  |

## 2.3 공통 파라미터 적용 순서

공통 파라미터는 다음 우선순위로 적용된다. 가장 구체적인 설정(PAC ID)이 우선하며, 해당 설정이 없으면 상위 범위로 거슬러 올라가 찾는다.

**PACID  →Program  →BusinessPackage  →Global**

예를 들어 Company Code, Fiscal Year, Month가 필수인 업무에서 Log Field가 BUKRS, GJAHR, MONAT인 스크린 파라미터를 각각 위 적용 순서에 따라 존재하는지 찾아 값을 채운다.
