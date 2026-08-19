---
id: log-management/03-log-jeokyong-bangbeop
doc: log-management
title: 3. Log 적용 방법
parent: docs/log-management/README.md
---

# 3. Log 적용 방법

PAC 대상 프로그램에 로그 기능을 적용하는 방법을 설명한다. 로그는 공통 Include(ZIPAC_COMMON)에 정의된 매크로를 프로그램에 삽입하여 적용하며, 매크로는 내부적으로 로그 클래스 ZCL_PAC_LOG를 호출한다.

## 3.1 공통 Include 적용

PAC 공통 Include 프로그램을 선언한다. 이 Include에는 로그 매크로, 공통 변수, 상수가 정의되어 있다.

INCLUDE ZIPAC_COMMON.

## 3.2 Screen Parameter 제어 및 T-Code 보정

파라미터 값을 수기로 변경하여 실행하는 것을 방지하기 위해 선택 화면 출력 시점에 화면 제어 매크로를 적용한다.

AT SELECTION-SCREEN OUTPUT.   _PAC_SET_SCREEN.

또한 프로그램 내에서 T-Code를 사용하는 변수는 SY-TCODE 대신 GV_PAC_TCODE를 사용할 것을 권장한다. PAC 자동 수행은 Batch Job을 생성하여 구동되는 구조여서 SY-TCODE에는 해당 프로그램의 T-Code가 입력되지 않기 때문이다.

**보완설명**  _PAC_SET_SCREEN은 내부적으로 PERFORM PAC_SET_SCREEN을 수행한다. GV_PAC_TCODE는 로그 시작 시 호출 파라미터(PS_PAC_INPUT_PARAM)의 T-Code 값으로 보정 입력되며, 일반 대화형 실행에서는 SY-TCODE 값이 그대로 사용된다.

## 3.3 PAC Log 매크로

로그는 시작 → 저장 → 종료 순서로 기록한다. 각 단계에 사용하는 매크로는 다음과 같다.

### 3.3.1 로그 시작

최초 한 번만 실행한다. Log ID가 생성되며 상태가 '진행 중'으로 반영된다.

_PAC_START_LOG.

### 3.3.2 Information 메시지 저장

Standard Message 뒤에 _PAC_SAVE_LOG 구문을 추가하여 직전 발생 메시지를 로그에 저장한다.

MESSAGE  S003(ZPAC01) WITH PARAM1. MESSAGE  I003(ZPAC01) WITH PARAM1.     _PAC_SAVE_LOG.

### 3.3.3 Warning / Error 메시지 저장

오류·경고 메시지는 INTO _MSG로 메시지를 받은 뒤 _PAC_SAVE_LOG로 저장한다.

MESSAGE  E003(ZPAC01) WITH PARAM1 INTO _MSG.     _PAC_SAVE_LOG. MESSAGE  W003(ZPAC01) WITH PARAM1 INTO _MSG.    _PAC_SAVE_LOG.

**보완설명**  _PAC_SAVE_LOG는 직전 메시지 유형(SY-MSGTY)을 감지하여 분류한다. 오류 유형(E·A·X)은 GV_PAC_ERROR를 설정하고 'K(Mass Error)'로, 정보 유형(I·S)은 'I(Information)'로 분류하여 저장한다. 메시지 ID(SY-MSGID)가 없으면 저장하지 않으므로 반드시 직전에 MESSAGE 구문이 있어야 한다.

### 3.3.4 로그 종료

저장된 로그를 바탕으로 최종 상태를 반영하며 비즈니스 로직을 종료한다.

_PAC_END_LOG.

**보완설명**  _PAC_END_LOG는 오류 누적 여부(GV_PAC_ERROR)에 따라 분기한다. 오류가 없으면 'C(Complete)'로, 오류가 있으면 내부적으로 _KEEP_ERROR_END를 호출하여 'F(Fail)' 상태와 함께 ZPAC01/032(Process Failed) 메시지를 기록한다.

### 3.3.5 로그 취소

로그 진행 중 프로그램 실행을 취소할 때 사용한다. Log Start 이후 실행 여부를 팝업으로 확인하여 사용자가 취소한 경우와 같은 특수 상황에서만 사용한다.

_PAC_CANCEL_LOG.

**보완설명**  _PAC_CANCEL_LOG는 로그를 직전 상태로 원복(revert)하며 ZPAC01/154 메시지를 기록한다. 일반적인 종료에는 _PAC_END_LOG를 사용하고, 사용자 취소 등 예외 상황에서만 본 매크로를 사용한다.

## 3.4 메시지 작성 유의사항

1. **유형별 Class/Number채번원칙.** 메시지는 유형별로 Class/Number를 채번하여 생성하는 것을 원칙으로 한다. '&'를 이용하여 여러 메시지를 하나의 Message 유형으로 개발하는 것은 지양한다. 에러 추적이 어려워지고 Error Help를 통한 에러 상세 조치사항 등록이 불가하기 때문이다.
2. **Collect 기본 동작.** PAC는 동일 Message Class/Number를 Collect하여 보여주는 것이 기본(default) 옵션이다. Collect 예외 처리를 할 수 있으나, '&'를 사용한 메시지는 여러 유형으로 사용될 수 있어 부적합하다.

## 3.5 수행 시간 측정

1. 로깅 시작부터 로깅 종료까지의 수행 시간이 자동으로 측정된다.
2. 시간 측정을 임의로 중단·재시작할 수 있다.
_LOG_TIME_SLEEP.   " 시간 측정 일시 정지 _LOG_TIME_START.   " 측정 정지 상태에서 시간 측정 재개

1. 시간 측정 일시정지 팝업을 제공한다. 팝업 호출 후 응답 전까지의 시간은 프로그램 수행 시간에서 제외되어야 한다.
PERFORM POP_TO_MSG  USING  'Title'  'TEXT1'  'TEXT2'. * 팝업 호출 전 시간 측정 중단, 팝업 종료 시 시간 측정 재개

**보완설명**  수행 시간 측정의 중단/재개는 ZCL_PAC_LOG의 HOLD_LOG_TIME 메소드로 제어된다(IV_HOLD = 'H' 중단 / 'S' 재개). 팝업 제공 메소드 PAC_POP_UP는 팝업 표시 직전 HOLD_LOG_TIME('H')로 시간을 멈추고, 팝업 종료 후 HOLD_LOG_TIME('S')로 재개하여 사용자 대기 시간이 수행 시간에 포함되지 않도록 한다.
