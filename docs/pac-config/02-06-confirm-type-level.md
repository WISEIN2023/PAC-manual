---
id: pac-config/02-06-confirm-type-level
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.6 Confirm Type Level
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.6 Confirm Type Level

### 2.6.1 XCONF_BUKRS — Company Level Control for Individual/Competition

**테이블-필드:** ZTPAC_CONFIG - XCONF_BUKRS

**운영 설정(LG전자 특화) :** REQ_BUKRS = X 모두 설정

#### 설정 설명

□ REQ_BUKRS = X인 경우 필드 활성화 됨

□ X 설정시 : Manual Confirm Type을 법인단위로 할 수 있도록 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC=>CHECK_INDIVIDUAL_FALG(CM003)/SELECT_SINGLE_NODE_INFO(CM01N), ZFPAC_CONFIRM_ITEM(LZPAC052U01),

ZFPAC_GET_MREADY_PID(LZPAC280U01), ZFPAC_CHK_ASSIGN_AUTH(LZPAC044U01), ZFPAC_PID_DETAIL_SEARCH(LZPAC018F01),

ZLPAC1000/1010/1011/1020(Participant), ZLPAC0140

#### 프로세스 관점 분석 (사용 로직)

Manual Confirm Type(Individual/Competition)을 법인코드 레벨로 통제할지 여부(REQ_BUKRS='X' 전제).

① ZCL_PAC=>CHECK_INDIVIDUAL_FALG: Activity의 Individual Confirm 여부 판정 시 'X'이면 법인코드 단위 설정을 우선 적용.

② ZFPAC_CONFIRM_ITEM: Manual Confirm 수행 시 Individual 여부 체크 경로에서 참조되어 유저별 개별 Confirm(ZTPAC_STATUS_IDV) 처리 분기.

③ Manual Ready 대상 조회(ZFPAC_GET_MREADY_PID), 권한 체크(ZFPAC_CHK_ASSIGN_AUTH), Participant 화면의 법인별 Confirm Type 컬럼 활성화에 사용.

#### 영향도 분석 (변경 시 영향)

설정 변경 시 법인별로 다르게 정의된 Confirm Type이 적용/무시되면서 Manual Confirm 동작 방식(개별 확인 vs 경쟁 확인)이 달라짐 — 결산 진행 중 변경 금지.

REQ_BUKRS 해제 시 이 설정도 함께 무효화됨.
