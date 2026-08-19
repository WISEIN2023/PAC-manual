<!-- 이 파일은 docs/ 원본에서 자동 생성됩니다. 직접 수정하지 마세요. -->

# 트러블슈팅 · 점검 라우팅표 (통합)

각 매뉴얼의 "증상별 점검 가이드 / 트러블슈팅 / FAQ" 항목을 한 곳에 모았습니다.
증상 키워드로 검색한 뒤 오른쪽 링크의 원문 섹션만 열어보세요.

총 **113건** / 15개 문서

## 권한 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| Fiori 접속하자마자 오류 | PAC Role(Fiori Catalog) 없음 → SU01 → Role 목록 | [2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)](../docs/authorization/03-pac-gwonhanui-keun-geurim.md#23-증상별-1차-체크리스트-가장-많이-쓰는-표) |
| 대시보드는 보이는데 법인이 안 뜸 | Participant 미등록 → ZLPAC1000 등록 현황 | [2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)](../docs/authorization/03-pac-gwonhanui-keun-geurim.md#23-증상별-1차-체크리스트-가장-많이-쓰는-표) |
| Direct Link에 Business Package가 안 보임 | Auth Group에 등록된 Role 미보유 → ZLPAC0010 / ZLPAC1030 | [2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)](../docs/authorization/03-pac-gwonhanui-keun-geurim.md#23-증상별-1차-체크리스트-가장-많이-쓰는-표) |
| World Map에서 법인 클릭 시 권한 오류 | Participant 미등록 → ZLPAC1000 등록 현황 | [2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)](../docs/authorization/03-pac-gwonhanui-keun-geurim.md#23-증상별-1차-체크리스트-가장-많이-쓰는-표) |
| 화면은 되는데 Activity 수행이 안 됨 | Tcode 실행 권한 부족 → SU53로 부족 Object 확인 | [2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)](../docs/authorization/03-pac-gwonhanui-keun-geurim.md#23-증상별-1차-체크리스트-가장-많이-쓰는-표) |

## 조직마스터 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 마스터 저장 시 오류/저장 안 됨 | ① 필수 키 값 누락 여부 ② 중복 키 여부(행에 오류 아이콘·메시지 표시) ③ 편집(변경) 모드 여부 ④ 잠금(Lock) 충돌 — SM12 확인 | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| 조직 삭제가 안 됨 | 해당 조직이 배정(ZLPAC0050)·결산에 사용 중인지 확인. 사용 중이면 소스의 ORG_MAP_EXIST 로 삭제가 제한됨 | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| 회사/사업영역 명이 안 보임 | SAP 표준 테이블(T001, TGSBT) 및 언어(SPRAS) 확인 | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| 비즈니스 유형이 선택 안 됨 | 상위 마스터 ZLPAC0013 등록 여부 및 유형 레벨(BLEVEL)이 대상 조직 레벨과 맞는지 확인 | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| 구조 변경 후 결산 상태가 안 맞음 | 변경 유형에 맞는 배치 실행 — 마스터 변경은 ZLPAC7192, Activity Group 이동은 ZLPAC7193 | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| ZLPAC0017 사용 관련 혼선 | 테이블 ZTPAC_COM_BUSTY DDIC 라벨이 ‘미사용’으로 표기됨 — 운영 사용 여부 확인 필요(3.2 참조) | [7.2 증상별 점검 가이드](../docs/org-master/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |

## Activity Master 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 이런 질문일 때 | 짧은 답 / 볼 곳 | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| Activity 코드를 바꾸고 싶어요 | Group/Sub/Activity 코드는 자동 채번이라 변경 불가. (5장 STEP1·STEP2) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 스케줄을 Activity에 연결하려면? | General tab의 Activity Master 속성 지정 . Activity type : Schedule 로 지정한 뒤, Schedule 필드를 통해 맵핑 → ZFPAC_CLOSING_ASSIGN. (5.2, 6장) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 연관 프로그램(T-Code)을 붙이려면? | Relative 탭에서 등록. (5.6) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| Rework(재작업) 감지를 설정하려면? | Rework 버튼 → ZFPAC_RULE_TO_ACTIVITY. 사전: ZLPAC3000/3010. (5.4, 7장) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| Trigger(자동수행)를 설정하려면? | 사전 ZLPAC0070에서 Trigger Code 정의 후 Trigger Define. (5장 Type X, 7장) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 어떤 항목이 어떤 Function을 부르나? | 6장 『항목별 호출 Function 매핑표』. | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 버튼 클릭 시 'Save first' | 신규 행은 PID 채번 전이라 버튼 동작 불가 → 먼저 저장 후 버튼 사용 | [8.1 문의 대응 케이스 (증상 → 원인 → 조치)](../docs/activity-master/08-teureobeulsyuting-dibeoging-gaideu.md#81-문의-대응-케이스-증상--원인--조치) |
| 코드를 못 바꿈 | Group/Sub/Activity 코드는 자동 채번(설계상 변경 불가) → 5장 STEP1/STEP2 | [8.1 문의 대응 케이스 (증상 → 원인 → 조치)](../docs/activity-master/08-teureobeulsyuting-dibeoging-gaideu.md#81-문의-대응-케이스-증상--원인--조치) |
| 삭제·Move To가 안 됨 | Map 등록(STD/ORG_NODE·LINK) 또는 수행 이력(ZTPAC_STATUS) 존재 → SE16N: 해당 테이블 | [8.1 문의 대응 케이스 (증상 → 원인 → 조치)](../docs/activity-master/08-teureobeulsyuting-dibeoging-gaideu.md#81-문의-대응-케이스-증상--원인--조치) |
| Rework 미발생 | Rule ID·G/L 계정 범위 또는 Rework Function 조건 → ZLPAC3010 / ZTPAC_RW_RULEID | [8.1 문의 대응 케이스 (증상 → 원인 → 조치)](../docs/activity-master/08-teureobeulsyuting-dibeoging-gaideu.md#81-문의-대응-케이스-증상--원인--조치) |

## 모델링 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 프로그램 실행 즉시 메시지 후 종료 | ① Web GUI에서 실행 여부(S112) ② SAP GUI로 재실행 | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| 편집이 안 되고 조회 모드로만 열림 | ① Business Package 관리 권한 ② 다른 사용자의 잠금(SM12에서 EZ_ZSPAC_LOCK/ZTPAC_CONFCOM 확인) | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| '조직이 할당되지 않았습니다' 오류(S253/254/255) | ZLPAC0050에서 해당 회사코드/사업영역/결산단위 조직 등록 여부 확인 | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| Business Type 미정의 오류(E003/E091) | ZTPAC_BUSTY에 해당 Business Type 정의 여부, Business Package와의 연결 확인 | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| 표준으로 열어야 하는데 글로벌로 전환됨 | PCSGP=BUPAK 여부, GPID 존재 여부, BLEVEL='C' 여부 확인(3.4) | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| ZLPAC0050에서 Business Type 입력 불가 | 해당 조직에 이미 모델 매핑 존재 여부(LINK 아이콘), SPECIFIC BUSTY/결산단위 레벨 여부(6.4) | [9.2 증상별 점검 가이드](../docs/modeling/09-unyeong-yujibosu-jeomgeom-gaideu.md#92-증상별-점검-가이드) |
| 모델링했는데 ZLPAC0140에서 보이지 않음 | 최하위인 Closing ID까지 모델링되어 있는지 확인. (ZLPAC0140 기본 조회 레벨이 최하위이므로 Closing ID 미모델링 시 조회되지 않음) | [자주 묻는 질문 (FAQ)](../docs/modeling/11-yongeojip-glossary.md#자주-묻는-질문-faq) |
| Node에 'Activities Not Exist' 메시지가 나옴 | Closing ID가 모델링되지 않은 경우. 최종 레벨(Closing ID)을 Setup해야 함. (8.3 참조) | [자주 묻는 질문 (FAQ)](../docs/modeling/11-yongeojip-glossary.md#자주-묻는-질문-faq) |
| 모델링 삭제가 안 됨 (FI000) | 상태 이력 데이터가 존재하는 경우. 해당 Activity의 Where Used List에 있는 모든 모델링을 먼저 삭제. (8.2 참조) | [자주 묻는 질문 (FAQ)](../docs/modeling/11-yongeojip-glossary.md#자주-묻는-질문-faq) |
| 2·3 Level 모델링이 수정권한 없음 | ZLPAC1050에서 해당 권한(Standard=M / Organization=O)이 부여되어 있는지 확인. (7.2 참조) | [자주 묻는 질문 (FAQ)](../docs/modeling/11-yongeojip-glossary.md#자주-묻는-질문-faq) |
| CO에서 해당 법인 결산 마감 되었는데 Monitoring 화면에 COG004 Activity가 진행이 되지 않은 상태로 보임 | Company Level Map에는 없지만 BA에는 모델링이 되어 있어서 생긴 문제. BA 모델링 1레벨 삭제 필요. 이미 결산이 마감된 시점에는 ZTPAC_CLD_ONODE 테이블에 데이터 입력해줘야 함. (운영X) | [자주 묻는 질문 (FAQ)](../docs/modeling/11-yongeojip-glossary.md#자주-묻는-질문-faq) |

## 결산일정 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 특정 월의 일정 배포가 불가 / 오류 | ZLPAC7030에서 해당 회계연도·월의 Calendar(결산 일자) 지정 여부 확인 (미등록 시 배포 불가) | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| 특정 조직만 일정이 보이지 않음 | ZLPAC7020에서 해당 조직에 Schedule ID 배정 여부 확인<br>Config의 Organization Type(M/S)과 Schedule ID의 Assign Level(B/O)이 의도와 일치하는지 확인 | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| 시간이 지나도 자동 통제가 안 됨 | Schedule ID의 Control by Time Schedule(XTIME_CNTR) 체크 여부 확인<br>Distribute 구간의 Day/Time 입력 여부 확인 | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| 배포 일정 수정 불가 | Status가 Planning Confirmed 이상인지 확인. 확정 후에는 Re-Planning으로만 수정 가능 (기존 이력 Reset 주의) | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| 일정을 변경하려는데 ‘No’로 표시 | 해당 Schedule ID가 Time Control(Control by Time Schedule) 대상인지 확인. Time Control 미설정 Schedule은 Changeable? = No | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| Posting Block인데 특정 사용자 기표 필요 | ZLPAC7160에서 전표 생성/승인 시점 사용자를 G/L·조직·기간과 함께 Super User로 등록 (Valid to Date/Time 확인) | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| Legacy 인터페이스가 호출되지 않음 (LG) | 해당 Schedule의 LEGIF='X' 여부, ZLPACEXIT(Exit Group SCH_IF)에 Exit Function 등록 여부, 인터페이스 API 연결 상태 확인 | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |
| 알람이 발송되지 않음 | 대상 Schedule이 ‘시간에 의한 통제’ 대상이며 해당 법인에 모델링되어 있는지 확인<br>알람 상태가 Active이며 Inactive 체크가 아닌지, Receiver가 1개 이상 설정되어 있는지 확인<br>ZLPAC7200 History에서 Background Job 스케줄/실행 상태 확인 | [8.2 증상별 점검 가이드](../docs/closing-schedule/08-unyeong-yujibosu-jeomgeom-gaideu.md#82-증상별-점검-가이드) |

## Schedule Job 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 잡 상태 건수가 맞지 않는다 | Total은 ZTPAC_JOB_SCHORG 기준, 실제 상태는 조회 시점 TBTCO 기준이다. 전월 잡 완료 시점에 익월 잡이 Released로 추가되므로 조회 시점에 따라 건수가 달라질 수 있다. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |
| 조직이 수정 불가(파란 글씨·자물쇠)로 보인다 | 해당 Job Seq에 이미 생성된 잡이 있는 조직이다. ZLPAC0520에서 생성한 잡이 존재하면 Block 처리된다. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |
| Plan Date/Time을 바꿔야 한다 | CWF 담당자만 ZLPAC0520의 Change 버튼으로 변경 가능하다. 일반 운영자는 ZLPAC0500 정의 기준을 사용한다. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |
| 생성한 잡을 삭제하고 싶다 | SM37에서 해당 Job Name으로 검색하여 삭제한다. 이미 수행된 잡 이력은 삭제 불가. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |
| 이미 수행된 잡을 재수행하고 싶다 | 단일·일회성으로 직접 생성하거나 직접 수행한다. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |
| 잡 소유자(수행자)가 서버와 맞지 않는다 | ZLPAC0520 CREATE 시 각 서버 기준 공통 유저로 지정되었는지 확인한다. | [11. 운영 FAQ / 트러블슈팅](../docs/schedule-job.md#11-운영-faq--트러블슈팅) |

## Auto Trigger 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| Auto Trigger가 전혀 동작하지 않음 | ① ZTPAC_CROSS_IF에 CRS Code 등록 여부 (ZLPAC0070 조회) | [6.2 증상별 점검 가이드](../docs/auto-trigger/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 특정 Trigger만 동작하지 않음 | ① ZLPAC0070에서 해당 CRSCODE의 XAUTO 체크 여부 | [6.2 증상별 점검 가이드](../docs/auto-trigger/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| Auto Trigger 후 후행이 오류로 중단됨 | ① SM37에서 오류 잡의 로그 확인 | [6.2 증상별 점검 가이드](../docs/auto-trigger/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 잘못된 조직/법인으로 Trigger가 발동됨 | ① ZTPAC_CROSS_IF의 TG_BUPAK 값 확인 | [6.2 증상별 점검 가이드](../docs/auto-trigger/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |

## REWORK 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 추가 기표를 해도 Rework가 발생하지 않음 | ① XREWORK 활성 여부 ② Rule ID/상세 조건이 해당 계정을 포함하는지 ③ 대상 Activity에 Rework Rule ID가 지정되었는지 | [6.2 증상별 점검 가이드](../docs/rework.md#62-증상별-점검-가이드) |
| 특정 계정만 Rework로 안 잡힘 | ZLPAC3010의 G/L 계정 범위·차/대변·Functional Area·외화 여부 조건 일치 확인 | [6.2 증상별 점검 가이드](../docs/rework.md#62-증상별-점검-가이드) |
| 연관 라인이 함께 중단되지 않음 | ZLPAC0020의 Linked Activity 등록 내역 확인(기준 Closing ID에 대상 라인이 연결되어 있는지) | [6.2 증상별 점검 가이드](../docs/rework.md#62-증상별-점검-가이드) |
| 주기 점검이 동작하지 않음 | ① XREWORK 활성 ② RWTMOUT(주기, 분) 값 ③ [PAC]REWORK... 배치 잡 등록/스케줄 상태(SM37) | [6.2 증상별 점검 가이드](../docs/rework.md#62-증상별-점검-가이드) |
| 같은 전표가 반복 점검되는 듯함 | ZTPAC_STATUS의 RWDT/RWTM(점검 시각) 기록 여부 확인 — 해당 시각 이후 내역만 점검됨 | [6.2 증상별 점검 가이드](../docs/rework.md#62-증상별-점검-가이드) |

## 모니터링 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 건수/상태가 실제와 다르게 보임 | ① 조회한 회계연도·월(기간)이 맞는지 ② 조직 조건(회사코드/사업영역/결산단위)이 맞는지 ③ ZFPAC_PAC_MONITOR 집계 결과 자체를 로그(ZLPAC0160)로 대조 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| 특정 조직만 안 보임 | 권한 문제일 수 있음 — ZCL_PAC_AUTH 조직 권한(회사코드/사업영역/결산단위) 보유 여부 확인 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| 자동 새로고침이 동작하지 않음 | ① Active Auto Refresh(P_TIMER) 체크 여부 ② 주기(P_MINUTE) 입력 여부 ③ 종료 시간(P_MAXTM) 도달로 자동 종료되었는지 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| 화면이 과도하게 자주/느리게 갱신 | 새로고침 주기(P_MINUTE)와 조회 조직 범위 재검토 — 범위가 넓고 주기가 짧으면 부하 증가 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| OverTime 목록이 비어 있음 | 정상일 수 있음(기준 시간 초과 진행 건이 없음). 초과 기준(P_OVER)·조회월(P_SPMON)·상태(R/S) 조건 확인 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| 월 최종결산 완료가 표시 안 됨 | ① 대상 패키지가 ACT_XFINAL='X' 인지 ② 결산 월이 미래가 아닌지 ③ 완료일자(COMP_DATE) 존재 여부 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |
| 상태/스케줄을 변경할 수 없음 | 다른 사용자가 편집 잠금(ENQUEUE_EZ_ZSPAC_LOCK)을 보유 중일 수 있음 — 잠금 사용자 확인 | [10.1 증상별 점검](../docs/monitoring/10-unyeong-yujibosu-jeomgeom-gaideu.md#101-증상별-점검) |

## PAC To-Do 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 특정 Business Package의 To-Do가 전혀 발생하지 않음 | ZTPAC_CONFIG-XTODO(To-Do 사용) 값이 'X'인지 확인 (ZLPAC0010) | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| Manual Ready To-Do가 지연되어 표시됨 | ① ZLPAC0010의 To-Do Duration(감지 주기) 확인 ② Manual Ready 감지 함수(ZFPAC_GET_MREADY_PID) 대상 여부 ③ 수신자(ZLPAC1000 Participants) 등록 확인 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| Rework To-Do가 발생하지 않음 | ① 대상 BusPkg의 XREWORK='X' 여부 ② Rework 감지 배치([PAC]REWORK…, ZLPAC7191) 수행 여부(SM37) ③ ZLPAC0010의 Rework Duration | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| Error To-Do가 발생하지 않음 | 상태 변경 지점(ZCL_PAC=>UPDATE_PAC_STATUS)에서 To-Do 발송 대상인지, 수신자(Participants Option) 등록 여부 확인 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| Closing Inspection To-Do가 발생하지 않음 | Activity Master의 Activity Type='I' 및 Inspection Category 등록 여부, Reviewer(ZLPAC5080) 등록 확인 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| 발생했어야 할 To-Do가 누락됨 | ZLPACTODOS에서 비정상 To-Do 조회 후 검토 → 검토 완료 시에만 Open/Close 또는 Data Sync 수행 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| CWF와 Signal To-Do가 서로 어긋남 | ZLPACCSP0020에서 싱크 불일치 건 조회 → CWF만 닫힌 경우 ZFPAC_CLOSE_TODO, Signal만 열린 경우 ZPCM_TODO_COMPLETE_FEEDBACK 사용 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |
| EP(포털) To-Do가 표시되지 않음 | EP To-Do는 Signal이 관할하므로 PAC에서 직접 조회 불가. Signal 연계(ZTPACSYS-TODOIF) 및 Signal 담당 확인 | [6.1 증상별 점검 가이드](../docs/todo/06-unyeong-yujibosu-jeomgeom-gaideu.md#61-증상별-점검-가이드) |

## 메일링 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 이런 질문일 때 | 짧은 답 / 볼 곳 | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 메일이 안 왔다는데? | PAC 로그(ZTPAC_LOG_MAIL)에 발송기록 있는지 → 있으면 SOST에서 실제 전송 상태 확인. (7.1 케이스 A, 5.6) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 특정 사람만 메일을 못 받아요 | ZTPAC_PROC_AUTH의 수신 플래그(XMAIL_*)·이메일(SMTP_ADDR) 확인. (7.1 케이스 B) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 수신자를 추가하려면? | ZLPAC1000에서 원하는 메일 수신항목에 대한 사용자 등록 + 메일 종류 체크박스. (5.2) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 고객사별 메일 수신옵션을 통제하려면? | ZLPACSYS | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 마감 알람은 어떻게 설정? | ZLPAC7200에서 알람시간·수신자 저장 → 배치 자동 예약. (5.4) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 메일 본문(양식)을 바꾸려면? | ZLPAC_HTML에서 HTML 양식 수정. 새 데이터는 ABAP 수정 필요. (5.5, 6장) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 메일이 실제로 나갔는지 확인? | SOST(SAPconnect 발송 큐). PAC 로그 성공 ≠ 실제 전송. (5.6, 7.1 케이스 A) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 본문에 $필드명$이 그대로 나와요 | 양식 마커가 발송 데이터 필드명과 불일치. (7.1 케이스 E, 6장) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 문제 원인을 코드로 봐야 할 때(디버깅) | 증상별 중단점 위치 표. (7.2) | [1.1 자주 묻는 질문(FAQ) — 빠른 찾기](../docs/mailing/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) |
| 메일이 안 왔다 | ① PAC 로그에 발송기록 있나? 없으면 수신자/트리거 문제 → ② 있으면 SOST 상태(대기/오류/완료) 확인 → PAC 로그 → SOST | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 특정 사람만 못 받는다 | 플래그(XMAIL_*) 체크 여부, 이메일(SMTP_ADDR) 존재, 삭제플래그(LOEVM), 대상 PID 등록 확인 → SE16N: ZTPAC_PROC_AUTH | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 수동준비 메일이 에러 받는 사람한테만 | 수동준비가 XMAIL_ERR로 수신자 조회(현재 사양). 의도와 다르면 개발팀 확인 → 3.3절 주의 | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 완료 메일이 안 온다 | ZLPACSYS의 XMAIL_COM ON 여부, ZTPAC_PROC_AUTH의 XMAIL_COM='X', Activity가 실제 완료(C)인지 → ZLPACSYS / SE16N | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 본문에 $필드$가 그대로 나온다 | HTML 마커가 발송 메서드 전달 필드와 불일치. 철자/대소문자 확인 → ZLPAC_HTML / 6장 | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 알람 메일이 안 온다 | ZTPAC_SCH_ALARM(ASTATUS='A')·N시간, 일정 배포 여부, SM37의 ZLPAC7210 잡 상태, 수신자 존재 → SE16N / SM37 | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| CIS 메일이 안 간다 | ZTPAC_CIS_CID의 XMAIL='X', 담당자 등록, ZTPACEXIT 트리거 설정 → SE16N | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |
| 메신저가 안 온다 | 메신저 발송 기능은 현재 미구현(플래그 XMSGR_*만 선택 가능). 고객사 요청 시 인터페이스 CSP 로직 개발 필요 → SE16N: ZTPAC_PROC_AUTH(XMSGR_*) | [7.1 문의 대응 케이스](../docs/mailing/07-teureobeulsyuting-dibeoging-gaideu.md#71-문의-대응-케이스) |

## 공지사항 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 공지사항 저장 후 대시보드에 미표시 | ① SICF 서비스 활성화 여부 ② Valid to Date가 현재 날짜 이후인지 확인 → SICF 활성화 또는 유효기간 재설정 | [7.2 증상별 점검 가이드](../docs/notice.md#72-증상별-점검-가이드) |
| 특정 사용자에게만 공지 미표시 | Assign Target Business Package에서 해당 사용자의 BP가 등록되어 있는지 확인 → 대상 BP를 추가하거나 전체 공개(BP 미지정)로 변경 | [7.2 증상별 점검 가이드](../docs/notice.md#72-증상별-점검-가이드) |
| 공지사항이 전혀 실시간 반영 안 됨 | APC 운영자 메뉴얼 5.2절 "공지사항(Notice) 실시간 표시 안 됨" 항목 확인 → SICF, SAMC, APC SAPC Test Run 순서로 점검 | [7.2 증상별 점검 가이드](../docs/notice.md#72-증상별-점검-가이드) |
| Notification 영역에 4개 이상 표시 안 됨 | 최대 3개까지 표시되는 PAC 설계 스펙 확인 → 설계 스펙 정상 동작. 오래된 공지 만료일 조정 권장 | [7.2 증상별 점검 가이드](../docs/notice.md#72-증상별-점검-가이드) |
| 첨부 파일이 팝업에 표시 안 됨 | 공지사항 저장 후 Attach File을 통해 파일 업로드 완료 여부 확인 → 파일 업로드 재시도 또는 세션 재로그인 | [7.2 증상별 점검 가이드](../docs/notice.md#72-증상별-점검-가이드) |

## APC 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| 모든 화면이 전혀 자동 갱신되지 않음 | ① SICF 서비스 활성 여부 ② SAPC Test Run으로 APC 자체 송수신 ③ 네트워크/프록시의 WebSocket 차단 여부(wss) | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |
| 프로세스 화면(ZPAC)만 갱신 안 됨 | ① 상태 변경 지점(ZCL_PAC > UPDATE_PAC_STATUS / SYNC_PCSGP_STATUS 등)에서 ZFPAC_CALL_APC 호출 여부 ② Extension ID(조직/기간) 일치 여부 ③ OData(ZGWPAC_MAIN) 정상 여부 | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |
| 특정 조직만 갱신 안 됨 | Extension ID 조합(법인·BA·기타조직·년월)이 화면 세션과 일치하는지 확인 | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |
| My To Do가 실시간 표시 안 됨 | ① 해당 사용자가 Participant List에 To Do 수신인으로 등록되어 있는지 ② ZFPAC_OPEN_TODO/CLOSE_TODO 호출 여부 ③ Extension ID(Client-User) 확인 | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |
| 공지사항(Notice)이 실시간 표시 안 됨 | [확인 필요] ZFPAC_CALL_APC_NOTICE 호출부 주석 처리 여부 확인 (4.3 참조) | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |
| 같은 화면이 과도하게 중복 갱신/지연 | APC LOCK(EZPACLCK_APC) 잔류 잠금 여부를 SM12에서 확인 | [5.2 증상별 점검 가이드](../docs/apc.md#52-증상별-점검-가이드) |

## 피오리 연계 SAP GUI 호출 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| Fiori에서 아무 화면도 열리지 않음 | ① 진입 T-Code ZLPAC_FTCODE 연결/권한 ② ZTPAC_PROC 정의행 존재 ③ 전달 파라미터(BUPAK·PID) 값 여부 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 엉뚱한 화면이 열림(분기 오판) | 입력 파라미터 조합 확인 : P_RTYPE·P_TDTYPE·P_TCODE·P_PID·P_CID 우선순위(3.1)에 따른 분기 결과 점검 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 결산일정 변경이 안 열림 | ① 정의의 REPTY='C' 여부 ② GET_SCHID_BY_PID 반환 일정 ID 존재 ③ ZLPAC7170 유효성 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| To-Do가 안 열림 | ① P_TDTYPE 전달값 ② ZLPAC0600 유효성 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 화면은 열리나 조직·기간이 비어 있음 | ① SET PARAMETER ID 매핑(5.2) ② 대상 화면에 해당 입력 필드 존재 ③ MEMORY ID ZPAC0_INPUT_PARAM 전달 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 레거시 링크가 안 열림 | ① 정의의 LEGACY_RFC/URL 값 ② ZFPAC_LEGACY_LINK 정상 여부 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| 첫 화면이 예상과 다르게 뜨거나 건너뜀 | Activity 정의의 XSKIP 값 및 결산점검 트랜잭션 여부(5.3) 확인 | [6.2 증상별 점검 가이드](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |

## Data Migration 운영자 매뉴얼

| 증상 · 항목 | 원인 / 조치 | 원문 |
|---|---|---|
| "Destination XXX does not exist" 오류 | SM59에서 RFC 목적지 등록 여부 확인 → 목적지 등록 후 재시도 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| "Z로 시작하는 테이블명만 사용가능" 오류 | 입력한 테이블명이 Z/Y 시작인지 확인 → 올바른 CBO 테이블명으로 수정 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| "Table layout does not match" 오류 | 원본/목적 시스템 간 테이블 구조 불일치 → TR로 테이블 구조 먼저 이관 후 재시도 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| 이관 후 데이터가 없음 | Business Package 조건, Where Condition 확인 → BP 또는 조건 값 재확인 후 이관 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| ALV 화면에서 저장 안 됨 | Lock 잔류 여부 확인 (SM12) → SM12에서 Lock 항목 확인 후 해제 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |
| RFC Destination 설정 오류 (Function) | ZTPAC_PROC_FUNC 테이블의 RFC Destination 값 확인 → ZLPACMIG030 Modify 모드로 일괄 수정 | [7.2 증상별 점검 가이드](../docs/data-migration/07-unyeong-yujibosu-jeomgeom-gaideu.md#72-증상별-점검-가이드) |

