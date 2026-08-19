---
id: pac-config/02-13-modeling
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.13 Modeling
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.13 Modeling

### 2.13.1 XDEL_REASON — Deletion Reason in Modeling?

**테이블-필드:** ZTPAC_CONFIG - XDEL_REASON

**운영 설정(LG전자 특화) :** 비활성

#### 설정 설명

모델링 삭제시 사유관리 활성화

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_NETGRAPH=>EVT_NODE_CTMENU_REQ(CM00S) 삭제 처리 경로

#### 프로세스 관점 분석 (사용 로직)

모델링에서 노드 삭제 시 사유 관리 활성화.

① ZCL_PAC_NETGRAPH(모델링 맵)의 노드 삭제 이벤트에서 'X'이면 삭제 사유 입력 팝업(ZFPAC_CHGNODE_REASON 연계)을 강제하고 사유를 이력으로 저장.

#### 영향도 분석 (변경 시 영향)

활성화 시 모델링 삭제마다 사유 입력이 강제되어 변경 이력 추적성이 확보되는 대신 작업 단계가 늘어남.

해제 시 삭제 사유 이력이 남지 않아 감사 대응 시 추적 불가.
