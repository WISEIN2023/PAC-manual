---
id: org-master/06-sangtae-donggihwa-baechi-peurogeuraem
doc: org-master
title: 6. 상태 동기화 배치 프로그램
parent: docs/org-master/README.md
---

# 6. 상태 동기화 배치 프로그램

조직 마스터나 결산 구조(Activity Group)를 변경하면, 이미 생성되어 있는 결산 상태 데이터(ZTPAC_STATUS)와 실제 구조가 어긋날 수 있습니다. 이 장의 두 배치 프로그램은 이러한 불일치를 다시 맞추는(동기화) 역할을 합니다. 두 프로그램 모두 **트랜잭션코드가없으므로** SE38 / SA38 또는 백그라운드 잡으로 실행합니다.

## 6.1 ZLPAC7192 — 마스터 변경 시 상태 동기화

| 구분 | 내용 |
|---|---|
| 프로그램 | ZLPAC7192 (트랜잭션 없음, SE38/SA38·배치 잡 실행) |
| 프로그램 설명 | Sync Status when Master Change - Batch Session |
| 주요 사용 테이블 | ZTPAC_CONFIG, ZTPAC_CLOSE, ZTPAC_COM_MAST/BA_MAST/CUNIT_MAST, ZTPAC_STATUS |
| 기능 | 조직 마스터(PID) 변경 후, 아직 마감(CLOSED)되지 않은 오픈 조직에 대해 결산 상태 계층을 다시 동기화합니다. |

선택 화면 파라미터:

| 파라미터 | 의미 | 설명 | 필수 |
|---|---|---|---|
| P_BUPAK | 비즈니스 패키지 | 필수. 동기화 대상 비즈니스 패키지 | ★ |
| P_BUKRS | 회사코드 | 선택. 특정 회사코드로 범위 제한 |  |
| P_GSBER | 사업영역 | 선택. 특정 사업영역으로 범위 제한 |  |
| P_CUNIT | 결산단위 | 선택. 특정 결산단위로 범위 제한 |  |
| P_PCSGP | 프로세스 그룹 | 선택. 특정 프로세스(그룹) 지정 |  |

처리 흐름(소스 기준): ①현재 결산월을 조회(ZCL_PAC_FUNC=>GET_LAST_CLOSING_PERIOD) → ②조직 레벨(C/B/U)에 따라 오픈일이 지났고 아직 마감되지 않은 조직을 추출 → ③변경 영향 노드를 조회(ZCL_PAC=>SELECT_PID_BY_CONDITION) → ④각 노드에 대해 상태 동기화 수행(ZCL_PAC=>SYNC_PCSGP_STATUS). 이미 마감(CLOSED='X')된 조직은 동기화 대상에서 제외됩니다.

## 6.2 ZLPAC7193 — Activity Group 이동 시 상태 동기화

| 구분 | 내용 |
|---|---|
| 프로그램 | ZLPAC7193 (트랜잭션 없음, SE38/SA38·배치 잡 실행) |
| 프로그램 설명 | Sync Status when Activity Group Move - Batch |
| 주요 사용 테이블 | ZTPAC_STATUS, ZTPAC_CLOSE |
| 기능 | Activity(결산 작업)를 다른 Activity Group으로 이동했을 때, 결산 상태 데이터를 이동 전/후 그룹에 맞게 옮기고 동기화합니다. |

선택 화면 파라미터:

| 파라미터 | 의미 | 설명 | 필수 |
|---|---|---|---|
| P_BUPAK | 비즈니스 패키지 | 필수. 대상 비즈니스 패키지 | ★ |
| P_PID | PID (프로세스 ID) | 필수. 대상 프로세스 식별자 | ★ |
| P_FPCSGP | 이동 전 그룹(From) | 필수. 이동 전 Activity Group | ★ |
| P_TPCSGP | 이동 후 그룹(To) | 필수. 이동 후 Activity Group | ★ |

처리 흐름(소스 기준): ①아직 마감되지 않은 상태(ZTPAC_STATUS, ZTPAC_CLOSE 미마감)를 조회 → ②해당 상태를 일괄 삭제 후 COMMIT → ③그룹 값을 이동 후 그룹(P_TPCSGP)으로 변경해 다시 입력 후 COMMIT → ④이동 전·후 그룹 모두에 대해 ZCL_PAC=>SYNC_PCSGP_STATUS 수행. 완료 시 처리 건수를 메시지로 표시합니다.

> ⚠ 주의<br>두 배치 프로그램은 결산 상태 테이블(ZTPAC_STATUS)을 직접 삭제·재입력하고 COMMIT WORK 을 수행합니다. 잘못된 파라미터로 실행하면 결산 상태가 어긋날 수 있으므로, 반드시 대상 비즈니스 패키지·기간을 확인하고, 가능하면 운영 반영 전 품질(Q) 시스템에서 검증한 뒤 실행하십시오. 이미 마감(CLOSED)된 데이터는 처리 대상에서 자동 제외됩니다.
