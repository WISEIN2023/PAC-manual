---
id: pac-config/03-21-minimum-allowance-rate
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.21 Minimum Allowance Rate
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.21 Minimum Allowance Rate

### 3.21.1 RATE_PCSGP — Allowance rate by Activity Group

**테이블-필드:** ZTPACSYS - RATE_PCSGP

**운영 설정(LG전자 설정) :** 10

#### 설정 설명

□ Activity Group의 배치잡을 생성할때의 유휴율을 관리 한다(해당 유휴율 이하의 경우 배치잡 생성 불가)

- ZFPAC_CHECK_JOB_BALANCING 에서 유휴율을 조회하여 JOB 생성여부를 정한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CHECK_JOB_BALANCING(LZPAC290U01), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

Activity Group 레벨 배치 Job 생성 최소 유휴율(%).

① ZFPAC_CHECK_JOB_BALANCING: 배치 WP 유휴율(FREE/TOTAL×100)을 계산하여 Group/BUPAK 레벨 Job인 경우 이 값 미만이면 Job 생성 보류(IV_WAIT='X'면 WAIT_TIME초 대기 후 재시도, 아니면 미생성).

② 대량 자동수행 시 배치 WP 고갈로 인한 타 업무 장애를 방지하는 부하 제어 장치.

#### 영향도 분석 (변경 시 영향)

값을 높이면 PAC 배치가 보수적으로 생성되어 타 업무 보호는 강해지나 결산 자동수행이 지연될 수 있음.

0/공백이면 부하 제어 없이 Job이 생성되어 WP 고갈 위험.

### 3.21.2 RATE_ACT — Allowance rate by Activity Sub Group

**테이블-필드:** ZTPACSYS - RATE_ACT

**운영 설정(LG전자 설정) :** 8

#### 설정 설명

□ Activity Sub Group의 배치잡을 생성할때의 유휴율을 관리 한다(해당 유휴율 이하의 경우 배치잡 생성 불가)

- ZFPAC_CHECK_JOB_BALANCING 에서 유휴율을 조회하여 JOB 생성여부를 정한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CHECK_JOB_BALANCING(LZPAC290U01), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

Activity Sub Group 레벨 배치 Job 생성 최소 유휴율(%).

① PID_LEVEL='PCSUB' Job에 적용. 로직은 RATE_PCSGP와 동일.

#### 영향도 분석 (변경 시 영향)

RATE_PCSGP와 동일 — Sub Group 레벨 Job의 생성 조건.

### 3.21.3 RATE_PID — Allowance rate by Activity

**테이블-필드:** ZTPACSYS - RATE_PID

**운영 설정(LG전자 설정) :** 5

#### 설정 설명

□ Activity의 배치잡을 생성할때의 유휴율을 관리 한다(해당 유휴율 이하의 경우 배치잡 생성 불가)

- ZFPAC_CHECK_JOB_BALANCING 에서 유휴율을 조회하여 JOB 생성여부를 정한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CHECK_JOB_BALANCING(LZPAC290U01), ZLPACSYS_F01

#### 프로세스 관점 분석 (사용 로직)

Activity(개별) 레벨 배치 Job 생성 최소 유휴율(%).

① PID_LEVEL='PID' Job에 적용. 로직은 RATE_PCSGP와 동일.

#### 영향도 분석 (변경 시 영향)

RATE_PCSGP와 동일 — 개별 Activity Job의 생성 조건. 통상 레벨이 낮을수록 Job 수가 많으므로 기준을 낮게(관대하게) 설정하는 편.

### 3.21.4 WAIT_TIME — Background Job Wait-up Time

**테이블-필드:** ZTPACSYS - WAIT_TIME

**운영 설정(LG전자 설정) :** 5

#### 설정 설명

위 유휴율에 해당하는 경우 대기시간을 정의

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CHECK_JOB_BALANCING(LZPAC290U01)

#### 프로세스 관점 분석 (사용 로직)

유휴율 미달 시 대기 시간(초).

① IV_WAIT='X'로 호출된 경우 유휴율 미달이면 WAIT UP TO WAIT_TIME SECONDS 후 재측정하는 루프 수행 — 미설정 시 대기 모드 자체가 동작하지 않음(CHECK로 종료).

#### 영향도 분석 (변경 시 영향)

공백이면 대기-재시도 없이 즉시 포기되어 유휴율 미달 시점의 Job이 생성되지 않음.

과도하게 크면 대기 루프가 길어져 호출측 세션이 장시간 점유됨.
