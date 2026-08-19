---
id: pac-config/03-17-notice-auth-check
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.17 Notice Auth Check
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.17 Notice Auth Check

### 3.17.1 NOTICE_AUTH — Notice Auth Check Type

**테이블-필드:** ZTPACSYS - NOTICE_AUTH

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

□ 결산일정 공지시에 접속가능한 권한을 정의

1) A : By Auth Role => Auth Role로 권한제어

2) P : By Participant => Participant로 권한제어

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_PORTAL_NOTICE_LIST(LZPAC063U01)

#### 프로세스 관점 분석 (사용 로직)

결산일정 공지(Notice) 접근 권한 유형(A: By Auth Role / P: By Participant).

① ZFPAC_PORTAL_NOTICE_LIST: HQ 권한자는 전체 공지 조회. 그 외 유저는 'A'이면 공지에 연결된 BusPkg에 대해 ZCL_PAC_AUTH=>CHECK_BUPAK_AUTH(권한 Role)로, 'P'이면 ZTPAC_PROC_AUTH(Participant 등록 여부)로 필터링하여 권한 있는 BusPkg의 공지만 표시.

② 조회된 공지는 ZTPAC_NOTICE_RD에 읽음 여부 기록.

#### 영향도 분석 (변경 시 영향)

A↔P 전환 시 공지가 보이는 사용자 집합이 바뀜 — Participant 등록이 안 된 Role 보유자(또는 그 반대)는 공지를 못 보게 되어 공지 전달 누락 가능.
