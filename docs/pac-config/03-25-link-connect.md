---
id: pac-config/03-25-link-connect
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.25 Link Connect
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.25 Link Connect

### 3.25.1 LINK_CONNECT — Active Connect/Disconnect in Fiori Link

**테이블-필드:** ZTPACSYS - LINK_CONNECT

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

PAC Map 화면에서 링크를 클릭하여 Connect/Disconnect 여부를 설정할 수 있다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC=>SELECT_LINK(CM017)/SELECT_GPID_LINK(CM014), ZCL_PAC_MTM=>SELECT_LINK_MTM(CM01H)

→ ZFPAC_LINK_CONNECT_CHANGE(SAPLZPAC091)와 연계

#### 프로세스 관점 분석 (사용 로직)

Fiori Map에서 링크 클릭으로 Connect/Disconnect 설정 허용 여부.

① ZCL_PAC=>SELECT_LINK 계열: 링크 조회 시 이 설정을 링크 속성으로 전달 → Fiori Map에서 링크 클릭 시 연결/해제 토글 UI 활성화, 실제 변경은 ZFPAC_LINK_CONNECT_CHANGE가 처리.

② 선후행 관계를 화면에서 임시 차단/연결하는 운영 기능.

#### 영향도 분석 (변경 시 영향)

활성 시 사용자가 Map에서 선후행 링크를 직접 끊거나 연결할 수 있게 됨 — 자동수행의 진행 경로가 화면 조작으로 바뀔 수 있으므로 권한 있는 인원만 사용하도록 운영 지침 필요.

해제 시 링크 변경은 모델링 화면에서만 가능.
