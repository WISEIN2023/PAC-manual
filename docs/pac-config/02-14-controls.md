---
id: pac-config/02-14-controls
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.14 Controls
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.14 Controls

### 2.14.1 XSCH_USE — Closing Schedule Exception?

**테이블-필드:** ZTPAC_CONFIG - XSCH_USE

**운영 설정(LG전자 특화) :** FI만 사용

#### 설정 설명

- PAC의 결산일정 시스템 사용여부를 지정

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_CLOSING=>CHK_CLOSING_ALL(CM003), ZLPAC7000_F01(일정 배포), ZLPAC0010_F01(CONFIRM_SAVE_DATA/CHECK_LEVEL)

#### 프로세스 관점 분석 (사용 로직)

PAC 결산일정(Closing Schedule) 시스템 사용 여부.

① ZCL_PAC_CLOSING=>CHK_CLOSING_ALL: Activity 실행/Confirm 시 일정 마감 여부 체크 수행 여부의 스위치 — 미사용 BusPkg는 일정 체크 없이 진행.

② ZLPAC7000: 결산일정 배포 대상 BusPkg 판정.

③ ZLPAC0010: ZTPAC_PROC_RCLOS(일정 할당) 존재 시 해제 불가(S470), ZTPAC_SCH_CONFIG-SCH_LEVEL과 PACLVL 불일치 시 활성화 불가.

#### 영향도 분석 (변경 시 영향)

활성화 시 일정 Close 이후 Confirm 통제 등 일정 기반 제약이 실행 프로세스에 추가됨.

해제하려면 일정 할당(ZTPAC_PROC_RCLOS) 선삭제가 필요하며, 해제 시 일정 마감 통제가 전면 사라짐.

### 2.14.2 NODE_LINK — Exectution block for completed activity

**테이블-필드:** ZTPAC_CONFIG - NODE_LINK

**운영 설정(LG전자 특화) :** 모두 설정

#### 설정 설명

□ X설정 : Activity가 완료된 경우  Reset을 통해 상태를 초기화 한 경우만 실행이 되도록 한다

□ 차단위치

1) _PAC_LOG_START시 완료상태는 차단된다

2) Map의 Activity를 더블클릭 이동시 'Skip Firtst Screen'이 적용된 경우 링크가 차단된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(완료 Activity 재실행 차단), ZCL_PAC=>CHECK_LINK_TO_TCODE(CM004)

#### 프로세스 관점 분석 (사용 로직)

완료된 Activity의 실행 차단(Execution block for completed activity).

① ZIPAC_COMMON: Actual 모드에서 설정 시 ZTPAC_STATUS 상태가 'C','T','P','O'(완료 계열)이면 「Can't execute because it is completed. Please reset it first.」(ZPAC01-516)로 실행 차단 → Reset 후에만 재실행 가능.

② ZCL_PAC=>CHECK_LINK_TO_TCODE: 맵에서 TCODE 링크 실행 시 동일 개념 체크.

#### 영향도 분석 (변경 시 영향)

중복 기표 방지의 핵심 안전장치 — 해제 시 완료된 Activity를 Reset 없이 재실행할 수 있어 이중 기표/중복 처리 위험.

활성 시 정당한 재실행도 Reset 절차를 거쳐야 하므로 운영 절차 숙지 필요.

### 2.14.3 ACT_XFINAL — Active Monthly Closing

**테이블-필드:** ZTPAC_CONFIG - ACT_XFINAL

**운영 설정(LG전자 특화) :** FI 필수. 나머지 모듈 확인 필요 (Final Activity 찍어야함)

#### 설정 설명

□ X설정 : Business Package Monthly Closing을 적용한다

- Activation된 경우 Activity Master에 Final 필드가 활성화 되며 Final이 적용된 Acvitiy가 완료된 경우 해당 Business Package 마감을 적용한다

- Global Package로 설정된 경우는 Main BusPkg에 적용된 기준으로 일괄 적용된다

□ 마감적용된 경우 Final Activity가 종료된 경우

- 마감 시점에 BusPkg / 조직 / 기간의 프로세스를 스냅샷으로 저장한다 (ZTPAC_CLD_SNODE, ZTPAC_CLD_ONODE, ZTPAC_CLD_SLINK, ZTPAC_CLD_OLINK)

- 마감된 월은 조회 모드로만 수행되며, 스냅샷 된 내역으로 조회하도록 하여 월별 관리가 가능하다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC=>CHECK_BUPAK_CLOSE(CM002)/CLOSE_BUPAK_FINAL(CM007)/SELECT_PID_BY_CONDITION(CM01G),

ZLPAC0170(Monthly Final Closing Monitoring), ZLPAC0020_F02, ZLPAC0010_F01(ACT_XFINAL_CHECKBOX_WHEN_130)

#### 프로세스 관점 분석 (사용 로직)

Business Package Monthly Closing(월마감) 적용 여부.

① ZCL_PAC=>CHECK_BUPAK_CLOSE / CLOSE_BUPAK_FINAL: Final Activity(ZTPAC_PROC-FINAL='X') 완료 시 BusPkg의 해당 월을 마감 처리하고 마감된 월의 Activity 실행을 통제.

② ZLPAC0170: 월마감 현황 모니터링/해제 관리.

③ ZLPAC0020_F02: Activity Master의 Final Activity 지정 필드 활성화.

④ ZLPAC0010: Final Activity가 이미 지정되어 있으면 해제 불가(I391), 해제 시 XFINAL_CHK도 함께 클리어.

#### 영향도 분석 (변경 시 영향)

활성화하려면 Activity Master에 Final Activity 지정이 선행되어야 함.

해제 시 월마감 개념이 사라져 마감된 월에도 Activity 실행이 허용됨 — 마감 후 소급 처리 통제가 무력화되므로 결산 거버넌스 관점에서 신중히 결정.

### 2.14.4 XFINAL_CHK — Completed Check when Final Activity execute

**테이블-필드:** ZTPAC_CONFIG - XFINAL_CHK

**운영 설정(LG전자 특화) :** 검토필요

#### 설정 설명

□ Active Monthly Closing(ACT_XFINAL)이 활성화 된 경우에 필드가 활성화 된다

□ X 설정 : Final Activity 마감시 미완료 프로세스 체킹하여 미완료 내역이 존재하는 경우 완료불가 처리

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZIPAC_COMMON(Final Activity Complete Check), ZFPAC_CONFIRM_ITEM(LZPAC052U01),

ZCL_PAC_SAIL=>SAIL_PROCESS_GROUP(CM00X)/CHECK_FINAL_COMPLETE(CM007), ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

Final Activity 실행 시 전체 완료 체크 여부(ACT_XFINAL 활성 시에만 입력 가능).

① ZIPAC_COMMON: Actual 모드에서 Final Activity 실행 시 ZCL_PAC_SAIL=>CHECK_FINAL_COMPLETE로 BusPkg 내 모든 Activity 완료 여부 확인, 미완료 존재 시 「All process have to be completed!」(ZPAC01-101)로 실행 차단.

② ZFPAC_CONFIRM_ITEM: Final Activity Manual Confirm 시 동일 체크.

③ ZCL_PAC_SAIL=>SAIL_PROCESS_GROUP: 배치 자동수행 중 Final 노드 도달 시 동일 체크 후 미완료면 에러 로그(101) 기록하고 skip.

#### 영향도 분석 (변경 시 영향)

미완료 Activity가 있는 상태의 조기 월마감을 막는 안전장치 — 해제 시 일부 Activity 미완료 상태에서도 Final(마감) 실행이 가능해져 불완전 마감 위험.

활성 시 예외적 조기 마감이 필요한 경우 미완료 Activity를 Skip/Confirm 처리 후 진행해야 함.

### 2.14.5 ORG_SKIP — Active Organization skip in Activity Master

**테이블-필드:** ZTPAC_CONFIG - ORG_SKIP

**운영 설정(LG전자 특화) :** 미사용

#### 설정 설명

Organization Skip 기능 사용여부

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_FUNC=>CHECK_ORG_SKIP_ENABLE(CM002), ZCL_PAC=>SELECT_NODE(CM01A), ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZLPAC0020_F02

#### 프로세스 관점 분석 (사용 로직)

Activity Master의 Organization Skip 기능 사용 여부.

① ZCL_PAC_FUNC=>CHECK_ORG_SKIP_ENABLE: 특정 조직에서 제외(Skip) 지정된 Activity인지 판정.

② ZCL_PAC=>SELECT_NODE / ZFPAC_GET_NODE_FIORI: 맵 노드 조회 시 Skip 조직의 노드를 제외/표시 처리.

③ ZLPAC0020_F02: Activity Master에서 조직 Skip 지정 필드 활성화.

#### 영향도 분석 (변경 시 영향)

활성화 시 조직별로 Activity를 프로세스에서 제외할 수 있게 됨 — Skip된 노드는 완료 체크(선행 체크, Final 체크)에서도 제외되므로 프로세스 흐름 판정에 영향.

해제 시 기존 Skip 지정이 무시되어 해당 조직에서 다시 수행 대상이 됨.

### 2.14.6 XSKIP_MIDDLE — Active skip only one sub group on Map

**테이블-필드:** ZTPAC_CONFIG - XSKIP_MIDDLE

**운영 설정(LG전자 특화) :** 모두 활성(2레벨 제외) ※ Sub group에 Relative or Closing Category가 설정된 경우에는 점프하지 않음

#### 설정 설명

□ Modeling Level(MDLVL)이 3레벨인경우 필드가 활성화된다

□ X 설정시 : 중간레벨이 하나만 존재하는 경우 마지막 레벨로 점프되도록 하여 사용자 편의성 개선

예) 1레벨의 노드 더블 클릭시

. 2레벨 1개 -> 3레벨로 점프

. 2레벨 2개 -> 2레벨로 점프

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_GLOBAL_TREE(LZPAC701U03)

#### 프로세스 관점 분석 (사용 로직)

3레벨 모델링에서 중간 레벨(Sub Group) 단독 Skip 허용 여부(MDLVL=3일 때만 화면 활성).

① ZFPAC_GET_NODE_FIORI/GLOBAL_TREE: 트리 구성 시 'X'이면 중간 Sub Group 하나만 Skip하는 동작을 허용하도록 노드 구성 로직 분기.

② Sub Group에 Relative/Closing Category를 구성하는 경우 활용.

#### 영향도 분석 (변경 시 영향)

변경 시 Fiori 트리/맵에서 Sub Group 단위 Skip 동작 가능 여부가 바뀜 — 중간 레벨을 건너뛰는 운영을 하던 조직은 해제 시 프로세스 진행이 막힐 수 있음.
