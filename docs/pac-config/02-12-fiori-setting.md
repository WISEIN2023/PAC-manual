---
id: pac-config/02-12-fiori-setting
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.12 Fiori Setting
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.12 Fiori Setting

### 2.12.1 FIORI_TILE — Fiori Tile

**테이블-필드:** ZTPAC_CONFIG - FIORI_TILE

#### 설정 설명

Portal 의 Business Package 피오리 타일 주소

※ 업무별로 타일을 각기 만들어 해당 업무별로 접근되도록 할 수 있다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_PORTAL_LINK(LZPAC271U01), ZCL_PAC_MAIL=>SEND_MAIL_* 전 메소드(CM008/009/00B/00H/00I/00J),

To Do 링크(LZPAC260F01), CIS 모니터(LZPACCIS0300U01)

#### 프로세스 관점 분석 (사용 로직)

Portal(PAC Home)의 BusPkg Fiori 타일 주소.

① ZFPAC_GET_PORTAL_LINK: Direct Link 목록 구성 시 FIORI_TILE을 ZCL_PAC_FUNC=>GET_URL(/UI2/CL_START_URL 기반 FLP URL 생성)에 전달하여 클릭 시 이동할 URL 생성.

② ZCL_PAC_MAIL: 메일 본문 링크를 「#<FIORI_TILE 앞부분>-func_link?PA_BUKRS=...&PA_PID=...」 형태로 조립 — 타일 ID가 메일/To Do 딥링크의 prefix.

#### 영향도 분석 (변경 시 영향)

Fiori 카탈로그/타일 ID 변경 시 이 필드를 함께 변경하지 않으면 포털 Direct Link·메일·To Do의 모든 딥링크가 깨짐 — Fiori 배포와 연동 관리 필수 항목.

### 2.12.2 ACT_LINK — Active as main link in Portal

**테이블-필드:** ZTPAC_CONFIG - ACT_LINK

**운영 설정(LG전자 특화) :** Subsidiary : FI만 연결 : IC -> FC 전환 그외 : 모두 활성화

#### 설정 설명

□ X설정 : PAC Home 화면의 Direct Link에 활성화된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_PORTAL_LINK(LZPAC271U01), ZLPAC0010_F01(ACT_LINK_WHEN_130)

#### 프로세스 관점 분석 (사용 로직)

PAC Home 화면의 Direct Link 활성화 여부.

① ZFPAC_GET_PORTAL_LINK: 「WHERE ACT_LINK NE SPACE」인 BusPkg만 Link 후보가 되고, ZTPAC_BUPAK과 JOIN하여 PAC Home Direct Link 목록으로 반환(ITMSEQ 순).

② ZLPAC0010: 미설정 시 LINK_ROLE 필드 숨김.

#### 영향도 분석 (변경 시 영향)

해제 시 해당 BusPkg가 포털 첫 화면(PAC Home) 링크에서 즉시 사라져 사용자의 접근 경로가 없어짐 — 사용자 공지와 함께 변경.

### 2.12.3 LINK_ROLE — Auth Group in Direct Link

**테이블-필드:** ZTPAC_CONFIG - LINK_ROLE

**운영 설정(LG전자 특화) :** BusPkg별 Auth Group을 만들어 연결 (해당 업무 권한만 보이도록)

#### 설정 설명

□ Active as main link in Portal가 설정된 경우 필드가 활성화 된다

□ Authorization Group을 입력. 입력된 경우 해당 권한이 존재하는 경우만 활성화 된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_PORTAL_LINK(LZPAC271U01)

#### 프로세스 관점 분석 (사용 로직)

Direct Link의 Auth Group 지정.

① ZFPAC_GET_PORTAL_LINK: LINK_ROLE 지정 시 ZCL_PAC_AUTH=>CHECK_AUTH_BY_AUTHGROUP으로 접속 유저의 권한그룹 보유 여부를 체크하여 권한자에게만 링크 노출. 미지정 시 전체 노출.

#### 영향도 분석 (변경 시 영향)

권한그룹 오지정 시 정당한 사용자에게도 링크가 숨겨짐(또는 반대로 전체 노출) — 권한 Role 변경/이관 시 함께 점검 필요.

### 2.12.4 XGRP_LVL — Active Group Leveling

**테이블-필드:** ZTPAC_CONFIG - XGRP_LVL

**운영 설정(LG전자 특화) :** Subsidiary,LC,NS 사용

#### 설정 설명

Group Leveling 사용여부

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZLPAC0020_F02(Activity Master)

#### 프로세스 관점 분석 (사용 로직)

Group Leveling(맵에서 그룹 단위 정렬 표시) 사용 여부.

① ZFPAC_GET_NODE_FIORI: Config 'X' + Activity Master(ZTPAC_PROC)의 해당 Group에도 XGRP_LVL='X'이고, 모든 노드가 Group 값을 갖고 Group 간 직접 링크가 없는 경우에만 노드셋에 플래그를 세팅 → Fiori Map이 그룹 레벨링 레이아웃으로 렌더링.

② ZLPAC0020_F02: Activity Master의 그룹 레벨링 필드 입력 활성화.

#### 영향도 분석 (변경 시 영향)

표시(레이아웃) 전용 설정으로 실행 로직에는 영향 없음.

단, 활성화하려면 모델링 데이터가 전제조건(전체 Grouping, 그룹 간 링크 없음)을 충족해야 하며 미충족 시 설정해도 적용되지 않음.

### 2.12.5 XSWIM — Swim Lane Active?

**테이블-필드:** ZTPAC_CONFIG - XSWIM

**운영 설정(LG전자 특화) :** 미사용

#### 설정 설명

Swim Lane 사용여부

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_ZGWPAC_MAIN_DPC_EXT=>SEL_FIELDSET_GET_ENTITY(CM00M), ZLPAC0020_F01, ZLPAC0010_F01(SWIM_LANE_CHECKBOX_WHEN_130)

#### 프로세스 관점 분석 (사용 로직)

Fiori Map의 Swim Lane 표시 사용 여부.

① OData 서비스 ZGWPAC_MAIN의 SEL_FIELDSET(화면 필드 구성 Entity)에서 XSWIM 값을 Fiori 앱에 전달 → Map 렌더링 방식 결정.

② ZLPAC0020: Activity Master의 Swim Lane 관련 필드 활성화.

③ ZLPAC0010: 모델링 데이터(ZTPAC_STD_NODE/ORG_NODE) 존재 시 활성화 확인 팝업.

#### 영향도 분석 (변경 시 영향)

기존 모델링이 있는 상태에서 활성화하면 Map 레이아웃이 재배치되어 사용자 화면이 크게 달라짐(설정 시 확인 팝업이 뜨는 이유).

실행 로직 무관, 표시 전용.
