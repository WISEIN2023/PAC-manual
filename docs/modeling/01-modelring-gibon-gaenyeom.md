---
id: modeling/01-modelring-gibon-gaenyeom
doc: modeling
title: 1. 모델링 기본 개념
parent: docs/modeling/README.md
---

# 1. 모델링 기본 개념

## 1.1 PAC에서 '모델링'이란

PAC는 결산 업무를 여러 개의 작은 작업 단위(Activity)로 나누고, 이 작업들을 순서(선·후행 관계)에 따라 연결하여 자동으로 수행합니다. 이때 '어떤 작업들이 어떤 순서로 연결되는가'를 시각적인 그림(네트워크 그래프)으로 정의하는 작업을 모델링(Modeling)이라고 합니다.

모델링 화면에서는 작업(**Node**)을 배치하고 작업 사이를 선(**Link**)으로 이어 결산 프로세스의 흐름을 만듭니다. 이렇게 만들어진 모델(맵)을 기준으로 실제 결산이 자동 수행됩니다.

## 1.2모델링 방법

- 좌측 메뉴 Tree의 Activity를 더블 클릭으로 우측 화면에 Node생성
- (모델링 된 Activity는 노란색으로 바뀜)
- Node와 Node 사이를 Link로 연결 하고 저장
- Node위에서 마우스 우클릭 후 ‘Maintain Activity Group’ 클릭 하면 하위 Activity 모델링 가능
- 삭제시 해당 Node 클릭 후 ‘Delete’ key

> 보완 설명 — 공통 모델링 엔진<br>모든 PAC 모델링 프로그램은 공통 클래스 ZCL_PAC_NETGRAPH (표준 설명: "Process Automatic Channel - Network")를 사용합니다. 각 프로그램은 이 클래스로 네트워크 그래프 객체(GRF_NETGRAPH)를 생성한 뒤 화면 0100에 그래프를 표시합니다.<br>즉 화면에 보이는 모델링 편집 방식(노드 배치·링크 연결·저장)은 다섯 개 프로그램 모두 동일하며, 프로그램마다 다른 것은 '무엇을 기준으로(조직·글로벌 여부) 모델을 여는가' 뿐입니다.

모델링은 **Activity Group → Activity → ClosingID** 의 3단계 계층 순서로 이루어집니다. 이 계층은 조회 프로그램 ZLPAC0140의 레벨 선택(Level 1/2/3, 기본값 Level 3)에서도 확인됩니다. 여기서 **Closing ID** 가 가장 하위(최종) 레벨입니다.

> 핵심 포인트 — 최종 레벨(Closing ID) 필수<br>최종 레벨인 Closing ID까지 모델링되어 있지 않으면 해당 프로세스는 수행이 불가합니다. 따라서 모델링 시 반드시 최하위 Closing ID를 Setup해야 합니다.<br>표준 맵(Standard Map)에서 먼저 모델링한 뒤, 조직 맵(Organization Map)에서 조직별로 모델링하는 순서로 진행합니다.

## 1.3 모델링을 여는 기준 값

모델링 프로그램은 실행 시 선택 화면에서 '어떤 모델을 열 것인지'를 결정하는 기준 값을 입력받습니다. 문서 전반에 반복 등장하는 핵심 기준 값은 다음과 같습니다.

| 기준 값 | 필드 | 의미 |
|---|---|---|
| Business Package | PA_BUPAK / BUPAK | 결산 업무 묶음의 최상위 식별자. 대부분의 모델링이 이 값을 기준으로 시작한다. |
| Business Type | PA_BUSTY / BUSTY | 비즈니스 유형. 표준 맵을 구분하는 키. 마스터: ZTPAC_BUSTY. |
| Activity Group | PA_PCSGP / PCSGP | 액티비티 그룹. 모델을 그룹 단위로 구분. 값이 Business Package와 같으면 최상위(1레벨) 취급. |
| 조직 레벨(PACLVL) | ZTPAC_CONFIG-PACLVL | Business Package별 조직 기준 레벨. C=회사코드 / B=사업영역 / U=결산단위. |
| Global Package ID | PA_GPID / GPID | 여러 Business Package를 하나로 묶는 글로벌 패키지 식별자. 마스터: ZTPAC_GPID_MAST. |

## 1.4 표준 모델 vs 조직 모델

PAC 모델링은 크게 '표준(Standard)'과 '조직(Organization)' 두 계열로 나뉩니다. 표준 모델은 조직과 무관한 기준 프로세스를 정의하고, 조직 모델은 특정 조직(회사코드·사업영역·결산단위)에 실제로 적용되는 프로세스를 정의합니다.

| 구분 | 표준 모델 (Standard Map) | 조직 모델 (Organization Map) |
|---|---|---|
| 일반 패키지 | ZLPAC0030 | ZLPAC0040 |
| 글로벌 패키지 | ZLPAC0031 | ZLPAC0041 |
| 기준 값 | Business Package + Business Type | Business Package + 조직(회사/BA/결산단위) |
| 용도 | 조직과 무관한 표준 프로세스 정의 | 조직별 실제 수행 프로세스 정의 |

## 1.4 모델링 프로그램의 공통 동작 특성

검증 결과, 다섯 개 모델링 프로그램은 다음과 같은 공통 특성을 가집니다. 운영 시 이 특성을 알고 있으면 대부분의 문의를 빠르게 해석할 수 있습니다.

- SAP GUI 전용(Web GUI 수행 불가): CL_GUI_OBJECT=>ACTIVEX / WWW_ACTIVE 를 검사하여 Web GUI에서 실행하면 메시지(S112)를 표시하고 중단합니다. 반드시 SAP GUI(ActiveX 사용 가능 환경)에서 수행해야 합니다. (ZLPAC0050 제외 — 4개 모델링 프로그램에 해당)
- 권한 체크: 실행·저장 시 ZCL_PAC_AUTH=>CHECK_BUPAK_AUTH 로 해당 Business Package 관리 권한을 확인합니다. 권한이 없으면 조회 모드(READONLY)로 전환됩니다.
- 잠금(Lock): 편집 충돌을 막기 위해 표준 잠금 함수 ENQUEUE_EZ_ZSPAC_LOCK (모드 'E', 배타적)로 잠급니다. 다른 사용자가 잠근 경우 조회 모드로 열립니다.
- 변경 후 종료 시 확인: 저장하지 않은 변경 사항이 있는 상태에서 나가려 하면 GET_SAVE_STATUS 결과에 따라 '변경 내용이 사라집니다' 확인 팝업을 표시합니다.
