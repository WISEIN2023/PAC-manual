---
id: pac-config/03-18-skip-auth-check-rule
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.18 Skip Auth Check Rule
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.18 Skip Auth Check Rule

### 3.18.1 SKIP_AUTH — Skip Auth

**테이블-필드:** ZTPACSYS - SKIP_AUTH

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

□ Manual Skip화면(ZLPAC0080)에서의 권한제어

1) S : By Standard Role

=> Standard Role로 권한을 체킹 / 해당 법인의 권한이 있는 경우 수정가능

2) C : By HQ+IT+Controller

=> HQ, IT는 전체 조직 수정가능, Controller는 해당 조직 수정가능하도록 권한 체킹

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC0080_F01(Manual Skip 화면)

#### 프로세스 관점 분석 (사용 로직)

Manual Skip 화면(ZLPAC0080)의 권한 제어 유형(S: Standard Role / O: Object / P: Participant).

① ZLPAC0080_F01: Skip 처리 실행 전 이 유형에 따라 표준 Role, 권한 오브젝트, Participant 등록 여부 중 하나로 권한 체크 → 권한 없는 유저의 임의 Skip 방지.

#### 영향도 분석 (변경 시 영향)

Skip은 프로세스를 건너뛰는 민감 기능 — 판정 기준을 느슨한 유형으로 바꾸면 임의 Skip으로 인한 결산 누락 위험, 엄격하게 바꾸면 정당한 Skip 처리자가 차단될 수 있음.
