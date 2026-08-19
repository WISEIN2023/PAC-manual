---
id: pac-config/02-05-display-level
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.5 Display Level
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.5 Display Level

### 2.5.1 ISSU1 — Activity Group

**테이블-필드:** ZTPAC_CONFIG - ISSU1

**운영 설정(LG전자 특화) :** 전체 지정

#### 설정 설명

이슈등록 관리 레벨

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_BUTTONS(LZPAC220U02), ZFPAC_GET_GLOBAL_NODE(LZPAC701U01)

#### 프로세스 관점 분석 (사용 로직)

이슈 등록을 허용할 레벨 중 Activity Group 레벨 활성화 여부.

① ZFPAC_GET_NODE_FIORI: 노드의 PID_LEVEL이 'PCSGP'(Group)이고 ISSU1='X'이면 해당 노드에 이슈 등록/조회 기능(LV_ISSU_USE) 활성화.

② ZFPAC_GET_BUTTONS: Fiori 노드 클릭 시 이슈 버튼 노출 제어. Global Map(LZPAC701U01)도 동일.

※ ISSU1/2/3는 하나의 SELECT로 함께 조회되어 레벨별 OR 조건으로 판정.

#### 영향도 분석 (변경 시 영향)

변경 시 Fiori Map에서 이슈 버튼이 노출되는 레벨이 바뀜 — 기존에 등록된 이슈 데이터는 유지되나 해당 레벨에서의 신규 등록/조회 진입점이 사라짐.

### 2.5.2 ISSU2 — Activity

**테이블-필드:** ZTPAC_CONFIG - ISSU2

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_BUTTONS(LZPAC220U02), ZFPAC_GET_GLOBAL_NODE(LZPAC701U01)

#### 프로세스 관점 분석 (사용 로직)

이슈 등록 허용 레벨 중 Activity(Sub Group) 레벨.

① PID_LEVEL='PCSUB'이고 ISSU2='X'이면 이슈 기능 활성화. 나머지 로직은 ISSU1과 동일.

#### 영향도 분석 (변경 시 영향)

ISSU1과 동일 — Sub Group 레벨의 이슈 버튼 노출 여부가 바뀜.

### 2.5.3 ISSU3 — Closing ID

**테이블-필드:** ZTPAC_CONFIG - ISSU3

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_BUTTONS(LZPAC220U02), ZFPAC_GET_GLOBAL_NODE(LZPAC701U01)

#### 프로세스 관점 분석 (사용 로직)

이슈 등록 허용 레벨 중 Closing ID(개별 Activity) 레벨.

① PID_LEVEL='PID'이고 ISSU3='X'이면 이슈 기능 활성화. 나머지 로직은 ISSU1과 동일.

#### 영향도 분석 (변경 시 영향)

ISSU1과 동일 — 개별 Activity 레벨의 이슈 버튼 노출 여부가 바뀜.

### 2.5.4 AUTH1 — Activity Group

**테이블-필드:** ZTPAC_CONFIG - AUTH1

**운영 설정(LG전자 특화) :** Closing ID

#### 설정 설명

Participant List 조회레벨

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01)의 'PALIST' 버튼 처리, ZFPAC_GET_PROPERTIES(LZPAC050U07)

#### 프로세스 관점 분석 (사용 로직)

Participant List 조회를 허용할 레벨 중 Activity Group 레벨.

① ZFPAC_GET_NODE_FIORI의 버튼 구성('PALIST')에서 PID_LEVEL='PCSGP'이고 AUTH1='X'인 경우에만 Participant List 버튼 노출(그 외 CONTINUE로 제외).

② ZFPAC_GET_PROPERTIES: 노드 속성 조회 시 동일 레벨 판정.

※ Confirm Type이 Individual인 노드는 레벨과 무관하게 제외됨.

#### 영향도 분석 (변경 시 영향)

변경 시 Fiori Map에서 담당자 목록(Participant List) 버튼이 노출되는 레벨이 바뀜 — 담당자 정보 노출 범위 정책과 연관되므로 개인정보 노출 관점 검토 필요.

### 2.5.5 AUTH2 — Activity

**테이블-필드:** ZTPAC_CONFIG - AUTH2

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_PROPERTIES(LZPAC050U07)

#### 프로세스 관점 분석 (사용 로직)

Participant List 조회 허용 레벨 중 Activity(Sub Group) 레벨.

① PID_LEVEL='PCSUB'이고 AUTH2='X'이면 Participant List 버튼 노출. 로직은 AUTH1과 동일.

#### 영향도 분석 (변경 시 영향)

AUTH1과 동일 — Sub Group 레벨의 담당자 목록 노출 여부가 바뀜.

### 2.5.6 AUTH3 — Closing ID

**테이블-필드:** ZTPAC_CONFIG - AUTH3

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_GET_NODE_FIORI(LZPAC220U01), ZFPAC_GET_PROPERTIES(LZPAC050U07)

#### 프로세스 관점 분석 (사용 로직)

Participant List 조회 허용 레벨 중 Closing ID 레벨.

① PID_LEVEL='PID'이고 AUTH3='X'이면 Participant List 버튼 노출. 로직은 AUTH1과 동일.

#### 영향도 분석 (변경 시 영향)

AUTH1과 동일 — 개별 Activity 레벨의 담당자 목록 노출 여부가 바뀜.
