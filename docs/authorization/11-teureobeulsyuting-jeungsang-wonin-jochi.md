---
id: authorization/11-teureobeulsyuting-jeungsang-wonin-jochi
doc: authorization
title: 10. 트러블슈팅 (증상 → 원인 → 조치)
parent: docs/authorization/README.md
---

# 10. 트러블슈팅 (증상 → 원인 → 조치)

실제 문의가 들어왔을 때 보는 장입니다. 2.3의 1차 체크리스트와 함께 사용하세요.

## 10.1 화면 접근 단계

| 증상 | 원인 | 조치 |
|---|---|---|
| Fiori 접속 즉시 오류 | PAC Role(Fiori Catalog) 없음 | SU01에서 PAC Role 배정 / 사용자 잠금 여부도 확인(USR02) |
| 타일(앱)이 아예 안 보임 | Catalog이 Role에 없음 | PFCG에서 해당 Catalog ID 포함 확인 |
| 대시보드는 보이나 법인 없음 | Participant 미등록 | ZLPAC1000에서 담당 법인/조직 등록 |
| Direct Link에 BUPAK 미표시 | Auth Group 등록 Role 미보유 | ZLPAC1030 매핑·ZLPAC0010 설정 확인 |
| World Map 클릭 시 권한 오류 | Participant 미등록 | ZLPAC1000 등록 |
| 사용자명·부서가 안 보이거나 이상함 | 사원마스터 데이터 누락 또는 Exit/표시 설정 문제 | 사원마스터 테이블(LG: ZPCMT0063, LXI: ZCOAT1004) 데이터 확인 → ZLPACEXIT 등록·ZLPACSYS DISUSER 설정 확인 (7.5) |

## 10.2 Activity 수행 단계

| 증상 | 원인 | 조치 |
|---|---|---|
| Authorization 오류로 수행 불가 | Tcode 실행 권한 부족 | SU53로 부족 Object 확인 → 해당 Object 가진 Role 찾아 추가 |
| 기표가 자동 수행 안 됨 | 수행 유저 권한 부족 | 배치유저(BATCHCWF001) 수행 여부/Posting User 설정 확인 |
| 마감 후 예외 기표 필요 | Posting Block 상태 | ZLPAC7160에 기표 주체를 Super User로 등록(5.5) |
| Auto Activity Skip 필요 | Manual Skip 비활성 | ZLPAC0080에 예외자 등록(5.4) |

## 10.3 Derive(파생) 후 권한값 깨짐

Master Role Derive 후 Variant Role의 ZPAC_BUPAK / 배치 Object 값이 «.»으로 초기화되는 현상(Master Role과 동일한 값으로 변경됨) → PFCGMASSVAL로 일괄 복원(5.7). 배치 관련은 P_PROGNAM을 «*»로 재설정.

## 10.4 업무별 디버깅 진입점 빠른 참조

"이 업무가 안 될 때 어디에 중단점(/h)을 걸어야 하나"를 한눈에 보는 표입니다. 메서드는 SE24, 함수는 SE37에서 열어 해당 위치에 중단점을 걸고 실행하세요. (각 항목의 상세 추적법은 4.2 / 7.3.2 / 7.3.3 참고)

| 업무 상황 | 디버깅 진입점 | 확인 포인트 |
|---|---|---|
| BUPAK 권한 오류 | ZCL_PAC_AUTH=>CHECK_BUPAK_AUTH | Special Role/Role/Object 통과 여부 |
| Tcode 실행권한 오류 | ZCL_PAC_AUTH=>CHECK_TCODE_AUTH | S_TCODE 권한, SY-SUBRC |
| 조직 권한 오류 | ZCL_PAC_AUTH=>CHECK_ORG_AUTH | BUKRS/GSBER/CUNIT 권한 |
| 활동(PID) 수행권한 | ZCL_PAC_AUTH=>CHECK_AUTH_BY_PID | EV_SUBRC (1:PAC, 2:Tcode, 3:Role) |
| Special Role 인정 여부 | ZCL_PAC_AUTH=>CHECK_SPECIAL_AUTH | A/T/H, ZTPAC_SPAUTH 등록 |
| HQ 권한 | ZCL_PAC_AUTH=>CHECK_AUTH_HQ | HQ 통과 여부 |
| Manual Skip 안 됨 | ZCL_PAC=>CHECK_MANUAL_ENABLE | ZTPAC_SUPER_CONF 예외 등록 |
| 실행유저(EXNAM) 결정 | ZFPAC_CREATE_PID_JOB | IV_EXNAM / SY-UNAME 분기 |
| 기표유저(PSNAM) 결정 | ZFPAC_USER_AUTH | ZTPAC_CONFIG USER_TYPE A/R/F |
| Activity Job 실행 | ZCL_PAC_SAIL=>SAIL_PROCESS_ID | LV_JOBUSER 값 |
| 마감 후 기표 막힘 | ZCL_PAC_CLOSING=>CHK_CLOSING_ALL | EV_CLOSED='X' 여부 |
| 조직/기간 유효성 | ZCL_PAC_ORG=>CHECK_VALID_ORG / _PERIOD | ES_RETURN 오류 여부 |
| 사용자 정보 조회(F4/이름 표시) | ZCL_PAC_ORG=>ON_GET_USERINFO | LV_FUNC(Exit 등록 여부), LS_SYS-DISUSER='E' 분기 |

**💡 디버깅 팁** 클래스 메서드는 SE24에서 해당 메서드를 더블클릭해 열고 줄에 중단점을 건 뒤 화면을 실행하면 멈춥니다. 권한 오류는 4.2의 «SU53 → 메서드 진입» 경로와 함께 쓰면 빠릅니다. 어느 메서드가 호출되는지 모를 때는 SE24/SE37에서 메서드·함수에 «외부 중단점(External Breakpoint)»을 걸고 Fiori/화면을 다시 실행하면 멈추는 지점으로 진입점을 찾을 수 있습니다.
