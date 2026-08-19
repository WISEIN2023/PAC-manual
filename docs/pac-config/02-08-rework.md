---
id: pac-config/02-08-rework
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.8 Rework
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.8 Rework

### 2.8.1 XREWORK — Rework Activate?

**테이블-필드:** ZTPAC_CONFIG - XREWORK

**운영 설정(LG전자 특화) :** Subsidiary만 활성화

#### 설정 설명

□ Rework Check 활성화 여부

- 기표된 FI 전표를 바탕으로 Rework 여부를 점검할지 설정한다 (FI전표를 발생하지 않는 프로세스는 설정 불필요)

- Active 된 경우 Activity Master의 Rework Setting을 바탕으로 점검된다

□ Rework Concept

- 추가 기표가 발생한 경우 해당 전표의 정보가 Rework 대상인지를 점검하고 대상인 경우 수행 Activity의 상태를 'Rework Ocurred'로 변경하고 해당 Activity와 연관된 라인의 자동수행을 중단한다

- ZTPAC_STATUS의 RWDT, RWTM에 Rework 점검 수행 시각이 기록되며, 해당 시간 이후에 발생된 내역만 점검하도록 하여 중복점검을 회피한다

□ Rework 점검대상 판단

1) Rework Rule ID

G/L Account, 차/대변지시자, Functional Area, 외화여부 등으로 판단

2) Rework Function

발생 전표 정보를 바탕으로 Rework이 발생하였는지를 상세 확인하는 EXIT 개념의 점검 방식

□ 점검 주기

- 자동 수행이 되는 경우 수시 점검이 수행된다

- 결산 일정이 Close 되는 경우 Rework 점검이 Active된 Business Package에 대해 일괄 수행된다

- Map을 조회시 'ZFPAC_GET_CAN_START'를 통해 수행된다

- 일정 배포시 Rework 점검이 Active 된 Business Package에 대해 주기 체킹을 수행하는 Batch Job을 생성한다(ZLPAC7191)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_SAIL=>START_REWORK_CHECK(CM01A)/CREATE_REWORK_BUPAK_JOB(CM00D), ZFPAC_SCHID_CLOSE(LZPAC131U01),

ZFPAC_REWORK_START(LZPAC020U01), ZLPAC7191(Rework 배치 생성), ZLPAC0150(조직별 Rework Job), ZLPAC7100, ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

Rework Check(기표 FI 전표 기반 재작업 점검) 활성화 여부.

① ZCL_PAC_SAIL=>START_REWORK_CHECK: 진입부에서 「CHECK XREWORK EQ ABAP_TRUE」로 비활성 BusPkg는 즉시 종료 → Rework 점검 전체의 마스터 스위치.

② ZFPAC_SCHID_CLOSE: 결산일정 Close 시 XREWORK='X'인 모든 BusPkg를 SELECT하여 START_REWORK_CHECK를 기동.

③ ZLPAC7191/ZLPAC0150: Rework 점검용 주기 배치 Job 생성.

④ ZLPAC0010: 해제 시 RWTMOUT 자동 클리어, 화면 필드(REK 그룹) 비활성.

#### 영향도 분석 (변경 시 영향)

활성화 시 일정 Close마다 Rework 점검 배치가 주기적으로 기동되어 배치 부하 증가 — 배치 WP 여유와 함께 검토.

해제 시 마감 후 발생한 FI 전표(재작업 대상)가 감지되지 않아 재결산 누락 위험.

### 2.8.2 RWTMOUT — Rework Duration (Minutes)

**테이블-필드:** ZTPAC_CONFIG - RWTMOUT

**운영 설정(LG전자 특화) :** 활성화된 경우 10분단위

#### 설정 설명

- Rework 점검 주기. ZLPAC7191을 통해 Batch Job이 생성된 경우 몇분단위로 점검을 할지를 지정하게된다

. 해당 프로그램에서 다음 Job을 스케쥴로 생성하는 컨셉

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_SAIL=>CREATE_REWORK_BUPAK_JOB(CM00D), ZLPAC0010_F01

#### 프로세스 관점 분석 (사용 로직)

Rework 점검 주기(분).

① ZCL_PAC_SAIL=>CREATE_REWORK_BUPAK_JOB: 즉시시작이 아닌 경우 RWTMOUT을 읽어 TZTF_ADD_MINUTE로 현재시각+RWTMOUT분을 다음 배치 Job 시작시각으로 지정 → 주기적 Rework 점검 스케줄링.

② ZLPAC0010: XREWORK 미체크 시 클리어되고 입력 불가.

#### 영향도 분석 (변경 시 영향)

값이 작을수록 점검 주기가 짧아져 Rework 감지는 빨라지나 배치 Job 수가 증가.

0/공백으로 두면 주기 계산이 되지 않아 반복 점검이 동작하지 않으므로 XREWORK 활성 시 필수 입력.
