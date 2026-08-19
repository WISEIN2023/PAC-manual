---
id: pac-config/03-19-job-grouping
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.19 Job Grouping
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.19 Job Grouping

### 3.19.1 JCRULE — Grouping Count when Job Creation

**테이블-필드:** ZTPACSYS - JCRULE

**운영 설정(LG전자 설정) :** 1

#### 설정 설명

결산점검의 시나리오별 잡을 생성시에 건별로 배치를 만들지 그룹으로 만들지를 정의한다

예) 1 : 시나리오 건별생성, 5 : 5개 시나리오를 묶어서 생성

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC5110_F01, ZLPAC5210_F01(결산점검 Job 생성), ZFPAC_CIS_SIMUL_RERUN(LZPACCIS0041F01)

#### 프로세스 관점 분석 (사용 로직)

결산점검 시나리오 Job 생성 시 그룹핑 건수(1: 건별 배치 / n: n건 묶음 배치).

① 결산점검 실행 화면(ZLPAC5110/5210)과 시뮬레이션 재수행(ZFPAC_CIS_SIMUL_RERUN)에서 시나리오들을 JCRULE 건수 단위로 묶어 배치 Job 생성 → Job 개수와 병렬도 조절.

#### 영향도 분석 (변경 시 영향)

값이 작을수록 병렬도·Job 수 증가(빠르지만 WP 소모 큼), 클수록 순차 처리 증가(느리지만 안정적) — 배치 WP 규모와 결산점검 시나리오 수에 맞춰 튜닝.
