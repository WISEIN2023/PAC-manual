---
id: closing-inspection/03-closing-inspection-scenario-zlpac5060
doc: closing-inspection
title: 3. Closing Inspection Scenario (ZLPAC5060)
parent: docs/closing-inspection/README.md
---

# 3. Closing Inspection Scenario (ZLPAC5060)

## 3.1 초기 화면

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 결산점검 시나리오 등록 — 초기 화면 |  |  |

Map을 통해 수행되는 Activity 중 결산 사전점검 항목으로 수행되는 상세 시나리오를 정의하는 화면입니다. Closing Inspection Scenario는 Closing Inspection Category 단위로 세팅되며, 등록된 시나리오는 Closing Dashboard의 각 Node를 통해 실행되거나 Closing Inspection Monitoring(ZLPAC5200) 프로그램에서 실행됩니다.

- Closing Inspection Scenario : Closing Inspection Category 단위로 정의되며, 결산 시 점검할 시나리오의 묶음입니다.
- ① Selection Condition : 결산점검 시나리오를 조회하기 위해 Business Package, Closing Inspection Category를 입력합니다.
- ② Execute : 실행하여 조회 화면으로 이동합니다.

## 3.2 조회 화면 — Tree Menu와 Detail View

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 결산점검 시나리오 조회 화면 |  |  |

**① Tree Menu**

- Closing Inspection Scenario로 구성한 항목을 Tree 구조로 조회합니다.
- Closing Inspection Category > Folder > Scenario 순서로 구성됩니다.
- 최하위 Scenario에 실제 수행할 결산점검 정보를 셋업할 수 있습니다.
**② Detail View**

- 좌측 Tree Menu의 각 항목을 더블클릭하여 Detail View에서 확인합니다.
- Folder 레벨 더블클릭 → Folder ID와 Name이 표시됩니다.
- Scenario 레벨 더블클릭 → Scenario ID, Name 및 실제 수행할 결산점검 정보가 표시됩니다.
**③Change /Display :수정 /조회 모드를 전환합니다.**

## 3.3 Folder / Scenario 생성 · 복사 · 이동

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 결산점검 시나리오 등록 — 신규 생성 |  |  |

Tree Menu에서 마우스 우클릭을 통해 결산점검 시나리오를 생성할 수 있습니다.

- ① Folder 레벨에서 우클릭 : Folder 생성 · 삭제가 가능하며, 폴더 하위에 폴더를 추가할 수 있습니다.
- ② Scenario 레벨에서 우클릭 : Scenario 생성 · 삭제가 가능합니다.
- Scenario 복사 : 상위 Folder 및 복사할 이름을 설정하여 복사합니다.
- Scenario 이동 : 상위 Folder를 지정하여 이동합니다.
시나리오 신규 생성 순서는 다음과 같습니다.

- ① Create Scenario 실행
- ② Scenario Name 입력
- ③ 상세 정보 입력 — Scenario ID는 자동 채번(변경 불가)되며, Scenario Name은 생성 시 초기 입력한 이름(변경 가능)입니다.
- ④ User Manual : Scenario별 결산점검 방법을 기술한 매뉴얼을 등록합니다. 추후 담당자가 이를 참고하여 업무를 진행합니다.
- ⑤ Scenario 실행 정보 입력 : General / Organization / Period / Relative 4가지 탭에 입력합니다. (3.4 ~ 3.7 참조)

| 탭 | 입력 내용 |
|---|---|
| General | 시나리오 Error 발생 시 Control 방법, 결산점검 타입(Function / CDS View / Manual) 지정 |
| Organization | 시나리오를 수행할 조직 단위 결정 (All, By Business Type, By Organization) |
| Period | 수행 주기 결정 (Monthly, Period Assign) |
| Relative | 시나리오 마우스 우클릭 시 사용자가 추가 확인할 정보 제공. Transaction, Report, Master, Etc, URL Link에 실행할 T-Code 또는 프로그램 매핑 |

## 3.4 General 탭 — Error Control

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 시나리오 상세 정보 입력 (General 탭) — Error Control |  |  |

**① ErrorControl :결산점검 시나리오 수행 결과 에러(Failed) 발생 시의 후행 프로세스를 정의합니다.**

| 값 | 유형 | 설명 |
|---|---|---|
| R | Need Re-run | Confirm 체크박스가 비활성화되며, 반드시 재수행이 필요합니다. |
| C | Need to Comment | Failed 발생 시 반드시 Comment 아이콘을 클릭하여 Confirm 시 사유를 입력해야 합니다. 파일 첨부 시 'User Manual' 버튼을 클릭합니다. |
| T | Can be Confirm | Failed 발생 시에도 Confirm이 가능합니다. |

> 보완 설명 — Error Control 코드값 (시스템 검증)<br>Error Control은 도메인 ZPAC_CIS_ECTRL로 관리되며, 시스템에 정의된 고정값은 R(Need to Re-run), C(Need to Comment), T(Can be Confirm) 3가지입니다. 입력값은 시나리오 마스터 테이블 ZTPAC_CIS의 ECTRL 필드에 저장됩니다.<br>Inspection Type이 F(By Function)인 경우 Error Control R(Need Re-run)은 사용할 수 없습니다.

## 3.5 General 탭 — Inspection Type

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 시나리오 상세 정보 입력 (General 탭) — Inspection Type |  |  |

**① InspectionType :결산점검을 수행할 점검 타입을 입력합니다. 타입에 따라 필수 입력 정보가 다릅니다.**

| 값 | 유형 | 시나리오 실행 방식 |
|---|---|---|
| F | By Function | (주로 사용) Closing Inspection 수행 시 지정한 Function이 실행되며, 실행 결과를 ALV로 표시할 수 있고 Screen Layout 지정이 가능합니다. Function 실행 시 적용될 Variant 설정이 가능하며, 실행 결과는 아이콘을 클릭하여 확인합니다. |
| C | By CDS View | Closing Inspection 수행 시 CDS View가 실행됩니다. |
| M | By Manual | Closing Inspection을 Manual로 수행합니다. 점검자가 시나리오를 직접 수행할 수 있도록 하며, T-Code 또는 Program으로 연결된 프로그램을 실행시켜 점검사항을 확인한 후 직접 Confirm 체크박스를 선택합니다. |

> 보완 설명 — Inspection Type(시나리오) 코드값 (시스템 검증)<br>시나리오 레벨의 점검유형은 도메인 ZPAC_CIS_EXTYP로 관리되며, 시스템에 정의된 고정값은 F(By Function), C(By CDS View), M(By Manual) 3가지입니다. 입력값은 ZTPAC_CIS의 EXTYP 필드에 저장되며, Function명은 SFUNC, CDS View명은 SCDS 필드에 저장됩니다.<br>2장의 Category 레벨 Inspection Type(S/C/R, 도메인 ZPAC_CIS_TYPE)과는 서로 다른 항목이므로 혼동하지 않도록 주의하십시오.

### 3.5.1 Inspection Type : By Function 상세

Inspection Type을 F(By Function)로 지정한 경우 다음 정보를 입력합니다.

- Function : 실행할 Function을 입력하고 체크(검증)합니다.
- Screen Layout : 결과를 출력할 테이블 ALV의 레이아웃을 설정합니다.
- Activate Variant Management 체크박스 : 점검을 위해 Function 실행 시 Variant를 사용할 경우 체크하여 파라미터와 파라미터 값을 입력합니다. Function에 정의된 Parameter에 Default Value를 설정합니다.

### 3.5.2 Inspection Type : By Manual 상세

Inspection Type을 M(By Manual)로 지정한 경우 다음 정보를 입력합니다.

- Activate Program Management 체크박스 : 점검을 위해 활용할 프로그램 화면으로 링크하고자 하는 경우 체크합니다.
- Call Type : T-Code 또는 Program 중 호출 방식을 선택합니다.
- Variant : 필요 시 기 생성된 Variant를 사용할 수 있습니다.
- Skip First Screen : Selection Screen을 자동 실행시킬 경우 체크합니다.
- Parameter : Selection Screen에 자동 입력될 Parameter Value를 지정합니다.
- By Manual 시나리오의 Result 필드에는 아이콘(Execute Program)이 표시되며, T-Code 또는 Program으로 연결된 프로그램으로 이동하여 점검사항을 확인한 후 직접 Confirm을 체크합니다.

> 보완 설명 — Call Type 코드값 (시스템 검증)<br>Call Type은 도메인 ZPAC_CALL_TYPE으로 관리되며, 시스템에 정의된 고정값은 T(T-CODE), P(Program) 2가지입니다. 입력값은 ZTPAC_CIS의 CALLTYP 필드에, Skip First Screen 여부는 XSKIP 필드에 저장됩니다.

## 3.6 Organization 탭

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 시나리오 상세 정보 입력 (Organization 탭) |  |  |

결산점검을 수행할 조직 유형을 지정합니다.

| 값 | 유형 | 설명 |
|---|---|---|
| A | All | 모든 조직에서 해당 결산점검 시나리오를 수행합니다. |
| O | By Organization | 특정 법인만 결산점검 시나리오를 실행시키고자 할 경우 목록에 추가합니다. |
| B | By Business Type | 특정 사업 유형만 결산점검 시나리오를 실행시키고자 할 경우 목록에 추가합니다. |

> 보완 설명 — 조직유형 · 기간유형 코드값 (시스템 검증)<br>조직유형은 도메인 ZPAC_CIS_ORG로 관리되며 고정값은 A(All), B(By Business Type), O(By Organization)입니다. 입력값은 ZTPAC_CIS의 ORGTYPE 필드에 저장되고, 개별 조직 지정 내역은 부속 테이블 ZTPAC_CIS_ORG에 저장됩니다.<br>Period 탭의 기간유형은 도메인 ZPAC_CIS_PER로 관리되며 고정값은 A(Monthly), M(Period Assign)입니다. 입력값은 ZTPAC_CIS의 PERTYPE 필드에 저장됩니다.

## 3.7 Relative 탭

| 화면명 | Maintain Closing Inspection Scenario | T-Code | ZLPAC5060 |
|---|---|---|---|
| 설명 | 시나리오 상세 정보 입력 (Relative 탭) |  |  |

결산점검 화면에서 각 시나리오와 연관된 프로그램을 Relative로 등록하면, 신규 화면에서 경로를 따라 접속할 필요 없이 마우스 우클릭으로 이동할 수 있도록 표시됩니다.

- ① Relative Type 선택 후 원하는 항목을 연결합니다.
- ② Transaction Code를 입력합니다.
- ③ Shown Sequence를 입력합니다. Relative 등록이 여러 건인 경우 Sequence를 통해 Display 순서를 지정합니다.
- ④ Relative Text를 입력합니다.
- ⑤ Call Type을 입력합니다.

> 보완 설명 — Relative Type 코드값 (시스템 검증)<br>Relative Type은 도메인 ZPAC_REL_TYPE으로 관리되며, 시스템에 정의된 고정값은 T(Transaction), R(Report), M(Master), E(Etc), U(URL Link) 5가지입니다. 등록 내역은 부속 테이블 ZTPAC_CIS_REL에 저장됩니다.
