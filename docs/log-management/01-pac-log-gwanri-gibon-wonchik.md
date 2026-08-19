---
id: log-management/01-pac-log-gwanri-gibon-wonchik
doc: log-management
title: 1. PAC Log 관리 기본 원칙
parent: docs/log-management/README.md
---

# 1. PAC Log 관리 기본 원칙

PAC는 SAP 결산 업무를 자동으로 수행하고 그 수행 결과(로그)를 저장·관리하는 솔루션이다. 로그 관리는 PAC 운영의 핵심으로, 각 결산 작업(Activity)이 언제·누구에 의해·어떤 결과로 수행되었는지를 일관된 규칙으로 기록한다. 본 장은 로그가 정상적으로 기록되도록 하기 위해 PAC 대상 프로그램이 따라야 하는 기본 설계 원칙을 설명한다.

## 1.1 T-Code 분리 및 오류 설계 원칙

- **업무 및 기능 단위 T-Code 분리(권고).** 수행/조회 등 권한을 분리하기 위해 T-Code를 나누는 것을 권고하나 필수는 아니다. 동일 T-Code를 여러 Activity에서 Variant 및 Parameter 설정으로 구분할 수 있다.
- **발생 가능한 오류를 한 번에 담는 설계.** 오류 정보를 한 번에 확인하여 조치함으로써 재조치율을 줄인다. 예를 들어 Cost Center 만료 오류가 하나만 발생하고 종료하면, 해당 건을 조치해도 다른 Cost Center에 문제가 있을 경우 오류가 계속 발생한다. 따라서 가능한 모든 오류를 수집하여 표시하도록 설계한다.

## 1.2 자동 수행 제어

- **Direct T-Code 접속 차단.** PAC 자동 수행 대상 프로그램은 T-Code를 직접 실행하여 접속할 수 없다. 직접 수행 시 이중 수행 등의 이슈를 막기 위해 PAC에서 수행을 차단하며, Configuration을 통해 On/Off가 가능하고 예외가 필요한 Activity는 예외처리할 수 있다.
- **중요 파라미터 변경 제어.** Activity 수행에 중요한 파라미터는 Actual Run의 경우 변경이 불가하도록 제어된다. 파라미터를 변경하여 일부만 수행되는 이슈를 차단하기 위함이다.
**보완설명**  Direct T-Code 차단 여부는 비즈니스 패키지 설정 테이블(ZTPAC_CONFIG)의 Direct 허용 설정에 따라 로그 시작(_PAC_START_LOG) 시점에 판별된다. Batch Job으로 수행되면 SY-TCODE에 해당 프로그램의 T-Code가 입력되지 않으므로, PAC는 별도 변수 GV_PAC_TCODE에 T-Code를 보정 입력한다.

## 1.3 자동 실행 프로그램 개발 원칙 및 Simulation

- **자동 실행에 맞는 개발.** Batch Job의 경우 별도 화면 표시 없이 Posting 등이 수행되도록 구현하고, 버튼을 이용한 Manual 수행 로직은 최소화한다. 화면이 존재하는 경우 SY-BATCH를 통해 포그라운드에서만 스크린이 호출되도록 분기한다.
- **Simulation Run.** Posting/Save가 이루어지지 않는 결산 사전 점검(Test Run) 개념이다. Pre-run은 상세 에러 검증과 Posting Simulation을 포함하여, 실제 전기(Posting) 시 예상 가능한 오류까지 사전에 점검한다. 시뮬레이션이 적용된 Activity는 사전 결산 점검 항목 중 Activity Simulation에 포함될 수 있다.
