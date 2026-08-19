---
id: authorization/13-peuroseseu-gaeyo-participant-process-overview
doc: authorization
title: 프로세스 개요 — Participant (Process Overview)
parent: docs/authorization/README.md
---

# 프로세스 개요 — Participant (Process Overview)

**📌 병합 메모** 이 장은 별도 문서였던 «PAC_프로세스매뉴얼_Participant.docx»(작성: 정유림, v1.0, 2026-06-16)를 이 매뉴얼로 통합한 것입니다. (2026-07-06 병합) 프로세스 관점의 요약이며, 상세 절차·검증 결과는 4·5·12장을 함께 참고하세요.

## 개요

PAC 솔루션 수행을 위한 두 가지 권한(PAC Role + Participant) 등록 및 관리 프로세스입니다.

| 구분 | 설명 |
|---|---|
| PAC Role | PAC Fiori 화면(Fiori Catalog) 및 PAC 프로그램 TCode 실행을 위한 SAP PFCG 권한 |
| Participant | 각 Business Package에 모델링된 Activity별 실제 수행 담당자 지정. Activity → Sub-Group → Activity Group → Business Package(Controller) 레벨로 권한 상속. Controller 등록 시 해당 BUPAK 내 모든 Activity 수행 가능 |
| Reviewer | (참고) Closing Inspection(결산 점검)의 시나리오별 담당자. Participant와 구분되며 ZLPAC5080에서 별도 등록 |
| Special Role | 프로젝트/IT 인원에게 Participant 등록 없이 모든 Activity 수행 권한 부여. CWF 담당자가 ZLPAC1050에서 부여 — 모든 BUPAK/조직 Activity에 적용 |

## 전제조건 (Prerequisites)

- Business Package(BUPAK) 및 Activity 모델링 완료
- SAP PFCG Role 생성 완료
- 조직마스터(회사코드, Business Area 등) 등록 완료

## 수행 주체 및 시점

| 수행 주체 | 수행 시점 |
|---|---|
| PAC 시스템 관리자(CWF 담당자) / 운영환경 지정 담당자 | • 신규 법인(BUPAK) 추가 시
• 담당자 변경 시
• 초기 시스템 구성 시 |

## 프로세스 흐름 (단계별)

| 단계 | 단계명 | 수행 내용 | 관련 프로그램 |
|---|---|---|---|
| Step 1 | PAC Role 부여 | SAP PFCG에서 PAC 전용 Role 생성·부여. BUPAK별 Role 분리 시 ZPAC_BUPAK Authorization Object를 Role에 포함. ⚠ Role 없이는 PAC Fiori 화면 접근 자체 불가 | PFCG (SAP 표준) |
| Step 2 | Participant 등록 | ZLPAC1000에서 Activity별 수행 담당자 지정. 대량은 ZLPAC1011(Excel Upload). 레벨: Activity > Sub-Group > Group > BUPAK(Controller). ⚠ 미등록 시 PAC Map에서 수행 버튼 비활성화 | ZLPAC1000 / ZLPAC1011 |
| Step 3 | Special Role 등록(필요 시) | 전체 수행 권한이 필요한 프로젝트/IT 인원을 ZLPAC1050에서 등록. ⚠ 모든 BUPAK/조직 Activity 수행 가능 → 남용 주의, CWF 담당자만 등록 | ZLPAC1050 |
| Step 4 | System Config 설정(초기 1회) | ZLPACSYS > Authorization 탭에서 Special Auth Check 방식 설정(S/O/A). Auth Group 사용 시 ZLPAC1030에서 Role-AuthGroup 매핑 | ZLPACSYS / ZLPAC1030 |
| Step 5 | 등록 결과 확인 | ZLPAC1010에서 등록 Participant 목록 점검. 이력은 ZLPAC1020(History) | ZLPAC1010 / ZLPAC1020 |

## 관련 프로그램 LIST

| 프로그램 ID | 프로그램 명 | 기능 요약 | 비고 |
|---|---|---|---|
| ZLPAC1000 | Maintain Closing Activity Participants | Activity별 Participant 등록/수정/삭제. Controller 레벨 포함 | 필수 |
| ZLPAC1001 | Copy Business Area for User Role | 사용자 Role 기반 Business Area 복사 등록 |  |
| ZLPAC1010 | Display Closing Activity Participants | 등록 Participant 목록 조회·점검 | 필수 |
| ZLPAC1011 | Excel Upload For Closing Activity Participants | 조직별 대량 Participant 일괄 등록 | 대량등록 |
| ZLPAC1020 | Display Closing Activity Participants History | Participant 등록/변경 이력 조회 |  |
| ZLPAC1030 | Maintain Authorization Group | Auth Group 정의·Role 매핑. ZLPACSYS 연동 | 초기설정 |
| ZLPAC1050 | Maintain Special Role | 프로젝트/IT 전체 수행 권한 부여. CWF 전용 | CWF 전용 |
| ZLPACSYS | PAC System Setting | Authorization 탭: Special Auth Check 방식(S/O/A) | 초기설정 |

## 관련 오브젝트 (테이블 / 클래스 / OData)

| 오브젝트 | 유형 | 활용 목적 |
|---|---|---|
| ZPAC_PART | 테이블 | Participant 등록 정보 저장 (Key: BUPAK, BUKRS, GSBER, UNAME) |
| ZPAC_SPECAUTH | 테이블 | Special Role 부여 정보 저장 (Key: UNAME, BUPAK) |
| ZPAC_AUTHGRP | 테이블 | Authorization Group ↔ Role 매핑 |
| ZCL_PAC_AUTH | 클래스 | 각 프로그램 공통 권한 체크(CHECK_ORG_AUTH / CHECK_AUTH_HQ / CHECK_SPECIAL_AUTH / CHECK_AUTH_BY_AUTHGROUP) |
| ZGWPAC_MONITOR | OData | Dashboard World Map / My Company Progress 조직 표시(Participant 등록 기반) |
| ZCL_ZGWPAC_MAIN_DPC_EXT | 클래스 | Fiori 참여자 OData 처리(목록 조회·상태) |

**⚠️ 검증 메모 (병합 시 정정)** 위 테이블명 ZPAC_PART / ZPAC_SPECAUTH / ZPAC_AUTHGRP는 원 프로세스 문서의 간략 표기입니다. MCP로 검증된 실제 저장 테이블은 12.2의 ZTPAC_PROC_AUTH(수행/Controller/Participant) / ZTPAC_SPAUTH(Special Role) / ZTPAC_AUTH_ROLE(Auth Group 매핑) 입니다. 또한 클래스 메서드는 CHECK_HQ_AUTH가 아니라 «CHECK_AUTH_HQ»로 확인되었습니다. 정확한 검증 결과는 12장 부록을 기준으로 하세요.

## 운영 노하우 / 주의사항

- **자주 하는 실수:** PAC Role 없이 Participant만 등록 → Fiori 접근 불가 / BUPAK 미지정 등록 → Dashboard 조직 미표시 / Controller 등록 시 BUPAK 전체 수행권한 → 과다 부여 주의
- **반드시 알아야 할 점:** Special Role은 CWF 담당자만 부여(운영 요청 시 CWF 경유) / BUPAK별 Role 분리 시 ZPAC_BUPAK Object 포함 필수 / Participant여도 해당 Activity TCode의 SAP 실행 권한 없으면 수행 불가 — SAP Role + Participant 둘 다 확인
- **영향도:** ZLPAC1000 등록/변경 → Dashboard World Map·My Company Progress 즉시 반영 / ZLPACSYS Auth Check 방식 변경 → ZCL_PAC_AUTH 전체 권한 체크 동작 변경(전사 영향)
- **배치 의존성:** 특별한 선행 Batch 의존성 없음. ZLPAC1011은 ZLPAC1000과 동일 저장 로직

## 디버깅 포인트

| 증상 / 에러 | 확인 위치 | 원인 | 조치 |
|---|---|---|---|
| PAC Fiori 화면 접근 불가(권한 오류) | PFCG 사용자 할당 / SU53 | SAP PAC Role 미부여 | PFCG에서 PAC Role 부여 후 권한 재생성 |
| Activity 수행 버튼 비활성화 | ZLPAC1000 등록 여부 / CHECK_ORG_AUTH B.P | Participant 미등록 또는 권한 레벨 불일치 | ZLPAC1000에서 Activity/Group/Controller 등록 확인 |
| World Map에 법인 미표시 | ZLPAC1000 등록 / ORG_PROGRESSET | 해당 법인에 Participant 0명 | 해당 BUKRS에 최소 1명 Participant 등록 |
| Special Role 부여했는데 수행 불가 | ZLPACSYS Authorization 탭 / CHECK_SPECIAL_AUTH | Auth Check가 O(Object Only)로 설정됨 | ZLPACSYS 설정을 S 또는 A로 변경, 또는 Object 추가 부여 |

## 고객사 특화 (LGE)

- **도메인별 권한 체크 로직 별도 존재:** BUPAK별 별도 Authorization Object 보유 여부를 추가 체크(LGE 전용 커스텀, 표준 권한 체크와 별개). 참조 메서드 ZFPAC_CSP_CHECK_BUKRS_AUTH
- **World Map 자회사 구분 선택 기능:** 각 자회사 구분(Company Group)을 선택해 Map을 보는 기능(표준에는 없는 LGE 전용). 참조 ZGWPAC_MONITOR=>COMPANY_GRPSET
**📌 검증 메모** ZFPAC_CSP_CHECK_BUKRS_AUTH 등 LGE 전용 로직은 현재 MCP 연결 시스템에서 미확인입니다(별도 시스템/커스텀 추정). 운영 시스템에서 확인 필요.

## FAQ

**Q1. PAC Fiori 화면이 보이지 않는다.**

PAC Role(PFCG) 부여 여부를 확인한다. SU53으로 권한 오류 내역을 보고, 없으면 PFCG에서 부여 요청.

**Q2. Participant로 등록했는데 Activity 수행 버튼이 비활성화된다.**

① PAC Role(PFCG) 부여, ② ZLPAC1000 Participant 등록을 동시에 확인. Activity에 연결된 TCode의 SAP 실행 권한도 있어야 수행 가능.

**Q3. 운영 환경에서 누가 Participant를 등록하는가?**

운영 환경은 지정된 운영 담당자가 일괄/개별 등록. 운영 외(개발/품질)는 상황에 따라 PAC 담당자가 직접 등록 가능.

**Q4. 프로젝트 인원에게 임시 전체 권한을 주고 싶다.**

ZLPAC1050(Maintain Special Role)에서 등록. 단 CWF 담당자만 가능하며, 부여 시 모든 BUPAK/조직 Activity 수행이 가능해지므로 주의.

**Q5. World Map에 특정 법인이 표시되지 않는다.**

ZLPAC1000에서 해당 법인(BUKRS)에 Participant가 최소 1명 이상 등록돼야 표시된다. 등록 후 즉시 반영.

**Q6. ZLPACSYS Authorization 탭 S/O/A의 차이는?**

S=Special Role만 있으면 인정, O=Authorization Object만 있으면 인정, A=둘 중 하나라도 있으면 인정. 보통 A로 유연하게 운영.
