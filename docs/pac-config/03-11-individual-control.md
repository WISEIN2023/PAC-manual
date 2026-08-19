---
id: pac-config/03-11-individual-control
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.11 Individual Control
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.11 Individual Control

### 3.11.1 IDV_RESET — Individual Reset Type

**테이블-필드:** ZTPACSYS - IDV_RESET

**운영 설정(LG전자 설정) :** I : User By User

#### 설정 설명

□ Reset을 수행한 경우의 Reset 단위

A : All Users -> 모든 유저가 Reset 된다

I : User By User → 해당 유저만 Reset 된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_SAIL=>RESET_ITEM_INDIVIDUAL(CM00U)

#### 프로세스 관점 분석 (사용 로직)

Individual Activity Reset 단위(A: All Users / I: User by User).

① RESET_ITEM_INDIVIDUAL: 'A'(또는 Confirm 권한자)이면 ZTPAC_STATUS_IDV에서 해당 Activity의 모든 유저 상태를 DELETE(전체 리셋), 'I'면 본인(SY-UNAME) 건만 삭제.

#### 영향도 분석 (변경 시 영향)

'A' 전환 시 한 명의 Reset이 다른 유저들의 Individual 확인 상태까지 초기화함 — 여러 담당자가 개별 확인하는 운영에서는 작업 유실 위험.

'I' 전환 시 전체 초기화가 필요한 상황에서 권한자 개입이 필요.
