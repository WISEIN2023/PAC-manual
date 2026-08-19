---
id: authorization/10-lgjeonja-teukhwa-jeongri
doc: authorization
title: 9. LG전자 특화 정리
parent: docs/authorization/README.md
---

# 9. LG전자 특화 정리

**📌 이 장의 위치** 여기부터는 LG전자 운영 환경에 특화된 내용입니다. 공통 개념(2~8장)을 먼저 이해한 뒤 읽으세요.

## 9.1 PAC Role 체계 (LG 기준)

Business Package별로 권한을 나누어 생성했습니다. 특히 Subsidiary Closing(개별결산)은 RAC 담당 / 일반 법인회계 담당 / HQ 담당으로 Role을 추가 세분화해 통제합니다.

**📷 화면** (엑셀 "PAC Role 체계"): GL CWF 권한 리스트, 운영환경 권한신청(GSOD) 화면

![authorization 화면](../../assets/authorization/img41.png)

![authorization 화면](../../assets/authorization/img42.png)

## 9.2 CWF 권한 체계 (Master/Variant Role)

LG전자 CWF의 주요 Master/Variant Role과 용도입니다(엑셀 "CWF권한" 시트).

| Master Role | Variant Role(대표) | VR수 | 용도 |
|---|---|---|---|
| ZM_FCW_IT | ZV_FCW_IT_ALL | 1 | IT Admin(SM) — IT 전체 권한(전체 프로세스) |
| ZM_FCW_HQ | ZV_FCW_HQ_SUBSIDIARY | 1 | 본사 회계담당. 연결회계/회계정책팀(개별결산) |
| ZM_FCW_RAC | ZV_FCW_RAC_SUBSIDIARY | 14 | 지역회계센터(개별결산), Region별 user 총괄 |
| ZM_FCW_ACC | ZV_FCW_ACC_SUBSIDIARY | 107 | 법인회계팀(GL_ACCOUNTING_GU에 추가). 회사코드 권한+Participant 등록 시 수행 |
| ZM_FCW_EXT | ZV_FCW_EXT_SUBSIDIARY | 1 | 유관시스템 IT담당자(임시유저 3일 사용) |
| ZM_FCW_FV | ZV_FCW_FV_ALL | 107 | 회계팀 아닌 FSV 각 Reviewer |
| ZM_FCW_ROYALTY | ZV_FCW_ROYALTY | 1 | 로열티 담당자, 각 사업부 기획담당 |
| ZM_FCW_CONS_PROF | ZV_FCW_CONS_PROF | 1 | 연결수익성 — 본사경영관리 |
| ZM_FCW_ENTITY_PROF | ZV_FCW_ENTITY_PROF | 1 | 개별수익성 — 법인 기획팀 |
| ZM_FCW_CONS_INV | ZV_FCW_CONS_INV | 1 | 연결수불(27년 1월 예정) |
| ZM_FCW_CONSOLIDATION | ZV_FCW_CONSOLIDATION | 1 | 연결회계팀 — HQ 권한 함께 부여(전법인 모니터링) |

업무 흐름: 개별결산 > 구분결산 > 연결결산 > 연결수익성

**📷 화면** (엑셀 "CWF권한"): Tcode 통제 묶음 / BUPAK별 통제 구분 / 모니터링 프로그램 수행 권한 화면

![authorization 화면](../../assets/authorization/img43.png)

## 9.3 ZPAC_BUPAK 값 구성 (Variant Role별 BUPAK 매핑)

각 Variant Role은 ZPAC_BUPAK Object에 담당 Business Package 값을 가집니다. 대표 예시(엑셀 "LG전자 권한특이사항" 시트):

| Variant Role | ZPAC_BUPAK 값(BUPAK) |
|---|---|
| ZV_FCW_ACC_SUBSIDIARY | CO, FI, FV, LC, NS |
| ZV_FCW_HQ_SUBSIDIARY | CO, FI, FV, LC, NS |
| ZV_FCW_RAC_SUBSIDIARY | CO, FI, FV, LC, NS |
| ZV_FCW_EXT_SUBSIDIARY | CO, FI |
| ZV_FCW_FV_ALL | FV |
| ZV_FCW_CONS_INV | CI |
| ZV_FCW_CONS_PROF | AC |
| ZV_FCW_ENTITY_PROF | AE |
| ZV_FCW_CONSOLIDATION | FC, IC |
| ZV_FCW_ROYALTY | AP, MP, RT |
| ZV_FCW_IT_ALL | * (전체) |

**📌 검증 방법** BUPAK으로 조회해 검증. Master Role의 ZPAC_BUPAK은 «.», Variant Role은 각 BUPAK 값을 가집니다(검증 필드: ZBUPAK). Role 27개 기준.

## 9.4 운영서버 권한신청 (GSOD)

**❗ 중요** 운영서버에서는 사용자가 «직접» GSOD에서 권한을 신청합니다. CWF 담당이 대신 처리해 주는 업무가 아닙니다.

- **IT 권한:** GSOD - Mass Registration (권한 IM에게 요청). CWF IT ALL 권한요청은 담당 선임을 통해 Mass Registration 요청
**⚠️ 확인 필요** Mass Registration 절차는 2026-07-07 작성 기준으로, 현재는 프로세스가 변경되었을 수 있습니다. 신청 전 최신 절차를 확인하세요.

- **일반 권한(IT 외):** GSOD에서 신청. 가이드 파일: NERP Authority_GL, CWF_v1.0
- **GSOD 결재자 변경:** 일배치로 반영되므로 즉시 반영 안 됨

### GSOD 표시 설정 — ZPCMR1405

ZPCMR1405 프로그램의 Visible 필드 설정으로 GSOD에 신청 권한 표시 여부를 설정합니다.

- 수작업으로 하나씩 바꾸면 담당자 정보가 reset되므로 «엑셀 템플릿 업로드» 사용
- GSOD 반영은 익일 03시에 인터페이스되어 반영됨
- ZM_FCW_IT, ZM_FCW_EXT는 GSOD에서 안 보이는 항목
- **GSOD 전환 대상('27.1월~):** ZV_FCW_FV_ALL(재무위험검증 FV), ZV_FCW_CONF_INV(연결수불 CI)
**📌 검증 메모** ZPCMR1405는 ZPCM 네임스페이스로 현재 검증 시스템에서 조회되지 않았습니다(LG 별도 시스템 추정). 운영 시스템에서 확인 필요.

**📷 화면** (엑셀 "운영 권한신청방법"): GSOD Mass Registration / 일반 권한 신청 화면

![authorization 화면](../../assets/authorization/img44.png)

![authorization 화면](../../assets/authorization/img45.png)

![authorization 화면](../../assets/authorization/img46.png)

![authorization 화면](../../assets/authorization/img47.png)

![authorization 화면](../../assets/authorization/img48.png)

![authorization 화면](../../assets/authorization/img49.png)

![authorization 화면](../../assets/authorization/img50.png)

![authorization 화면](../../assets/authorization/img51.png)

**📷 화면** (엑셀 "GSOD"): ZPCMR1405 Visible 설정 / 엑셀 업로드 화면

![authorization 화면](../../assets/authorization/img52.png)

![authorization 화면](../../assets/authorization/img53.png)

![authorization 화면](../../assets/authorization/img54.png)

![authorization 화면](../../assets/authorization/img55.png)

## 9.5 GSOD 2차 결재자 셋업

권한 신청 시 2차 승인자를 Role별로 세팅합니다. 주요 GL/CWF Role의 2차 승인자 기준(엑셀 "GSOD 2차결재자 셋업" 시트):

| Master Role | 설명 | 2차 승인자 |
|---|---|---|
| ZM_FGL_ACCOUNTING_SU | FIN Accounting RAC | 각 RAC 팀장 |
| ZM_FGL_ACCOUNTING_GU | FIN Accounting General | 각 법인 CFO |
| ZM_FCW_RAC | CWF Accounting RAC User | FIN Accounting RAC와 동일 승인자 |
| ZM_FCW_ACC | CWF Accounting General User | FIN Accounting General과 동일 승인자 |
| ZM_FCW_HQ | CWF Accounting HQ Admin | GL Account Super와 동일 승인자 |
| ZM_FCW_IT / ZM_FCW_EXT | IT / I/F User | GSOD에서 신청 안 함 |

**📌 신규 법인 추가 시** 신규 Variant Role도 GL Role과 동일한 결재자로 셋업합니다(5.8 참고). 셋업은 GL Role 참고.

## 9.6 System User 생성 프로세스 (INTCWFPO001)

CWF 결산 담당자가 SAP ID가 없을 때, I/F 유저(INTCWFPO001)가 임시로 유저를 생성하고 CWF 권한을 부여하는 프로세스입니다(User Type: System).

- **대상:** IT 유지보수 인원 등 유관 담당자(SAP ID 없이 X사번만 보유)
- **처리:** SAP ID를 생성하고 수행 권한을 임시로 «3일간» 부여 (Function으로 유저 확인·생성·권한부여, 별도 Activity로 구성)
- **보유 Role:** ZBC_ITSM_SLIM, ZBC_PI_ALL, ZBC_ITSM_CWF_ROLE
- **유관담당자 CWF Post user 권한:** ACC로 받지 않고 ZV_FCW_EXT(→ '26.1.20부터 ZV_FCW_EXT_SUBSIDIARY)로 분리 관리
**⚠️ 변경 시 주의** 유관담당자에게 부여할 권한이 바뀌면 함수 체크로직 수정이 필요합니다. 체크 함수: ZPCM_SAVE_CWF_ROLE (담당자에게 알려야 함).

**📷 화면** (엑셀 "CWF INTCWFPO001"): System User 권한 구성 화면

![authorization 화면](../../assets/authorization/img56.png)

![authorization 화면](../../assets/authorization/img57.png)

## 9.7 결산 CWF 보유 권한 점검 메일링

CWF에 등록된 Tcode를 수행하려면 각 모듈별 결산담당자 Role에 Tcode 수행권한이 등록돼 있어야 합니다. 도메인별 Pair Role에 CWF Tcode가 등록됐는지 점검하고, 누락 시 담당자에게 메일을 보냅니다.

- **점검 주체:** CWF 담당
- **점검 함수:** ZFCL_CWF_ROLE_CHECK (권한 누락 시 Role별 담당자·이메일 반환)
- **기준 데이터:** ZPCMT0060 (common code master), 등록 프로그램 ZPCMR0030 — 28개 개발클래스↔도메인 Role 매핑
- **메일 로직 참고:** ZLPAC7200 / ZFPAC_CREATE_ALARM_BATCH → ZLPAC7210 배치잡(메일 발송 실제 로직)
**📌 검증 메모** ZFCL_CWF_ROLE_CHECK, ZPCMR0030, ZPCMT0060은 ZPCM/ZFCL 네임스페이스로 현재 검증 시스템에서 조회되지 않았습니다(별도 시스템/제공 함수 추정). 운영 시스템에서 확인 필요. BW 대상은 다른 서버라 RFC destination 사용.

**📷 화면** (엑셀 "결산CWF권한점검_전체내용"): Common Code 등록(ZPCMR0030) / 배치잡 생성 화면

![authorization 화면](../../assets/authorization/img58.png)

![authorization 화면](../../assets/authorization/img59.png)

![authorization 화면](../../assets/authorization/img60.png)

![authorization 화면](../../assets/authorization/img61.png)

![authorization 화면](../../assets/authorization/img62.png)

![authorization 화면](../../assets/authorization/img63.png)

![authorization 화면](../../assets/authorization/img64.png)

## 9.8 개발클래스 ↔ 도메인 Role 매핑 (관리파일)

결산 CWF 권한 점검의 기준이 되는 매핑입니다(엑셀 "관리파일" 시트, 대표 발췌).

| 개발Class | 도메인 | 모듈 | 결산 Master Role |
|---|---|---|---|
| ZFGLD/ZFCLD/ZFFCD | 재경 | 회계 | ZM_FGL_ACCOUNTING_SU |
| ZFAPD/ZFFBD | 재경 | 금융 | ZM_FAP_FIN_CLOSING |
| ZFARD/ZFIVD | 재경 | 채권 | ZM_FAR_CLOSING_GENERAL |
| ZCPCD/ZCSCD | 재경 | 원가 | ZM_FPC_SPV |
| ZCSCD | 재경 | 구분회계 | ZM_FSC_*CLOSING |
| ZFTXD | 재경 | 세무 | ZM_FTX_FIN_CLOSING |
| ZMCMD | 생산 | 관세 | ZM_MCM_FIN_CLOSING |
| ZSLED | 영업 | 물류 | ZM_SLE_FIN_CLOSING |
| ZSSDD | 영업 | 주문 | ZM_SSD_FIN_CLOSING |

**📌 전체 매핑** 관리파일 시트에는 약 28개 개발클래스 매핑과 도메인별 담당자·이메일이 있습니다. 전체는 엑셀 원본을 참조하세요(본문 9.9에 담당자 요약).

**📷 [캡처 삽입 위치]** 엑셀 "관리파일" 시트의 행11 그림 → Common Code 등록 화면

## 9.9 고객사별 CWF 권한 담당자

| BUPAK | 한글명 | 담당자 |
|---|---|---|
| FI / CO / FV / LC / NS | 개별결산/원가/재무위험검증/로컬결산/경험율 | 정수진 |
| RT / MP / AP | 로열티 / Moving Plan / Annual Plan | 박민우 |
| AC / AE | 연결수익성 / 판관비배부 | 주원돈, 고윤기 |
| CI | 연결수불 | 정상호, 허우태(PI) |
| FC / IC | 연결회계 / 연결회계(임시) | 박예찬, 김홍석(PI) |

## 9.10 권한 관련 History / 의사결정

- Activity Master·Modeling·Inspection scenario master는 IT용·HQ용 권한에서만 허용하기로 결정
- HQ_SUBSIDIARY 권한을 받으면 모든 조직의 접근권한을 허용
- CI(연결수불)는 권한만 우선 생성해 둠('27.1월 사용 예정)
**📷 화면** (엑셀 "history"): 권한 의사결정 이력 화면

![authorization 화면](../../assets/authorization/img65.png)

![authorization 화면](../../assets/authorization/img66.png)

![authorization 화면](../../assets/authorization/img67.png)

![authorization 화면](../../assets/authorization/img68.png)

**📷 화면** (엑셀 "LG전자 권한특이사항"): Role 메뉴트리 변경 / 배치 권한오브젝트 / 권한반영 검증 화면

![authorization 화면](../../assets/authorization/img69.png)

![authorization 화면](../../assets/authorization/img70.png)

![authorization 화면](../../assets/authorization/img71.png)

![authorization 화면](../../assets/authorization/img72.png)

![authorization 화면](../../assets/authorization/img73.png)

![authorization 화면](../../assets/authorization/img74.png)

![authorization 화면](../../assets/authorization/img75.png)

![authorization 화면](../../assets/authorization/img76.png)

![authorization 화면](../../assets/authorization/img77.png)

![authorization 화면](../../assets/authorization/img78.png)

## 9.11 고객사 특화 권한 체크 로직 (화면)

LG전자 전용 커스텀 권한 체크 로직(예: Business Package별 별도 Authorization Object 보유 여부를 추가로 체크) 관련 화면입니다. 참조 메서드 ZFPAC_CSP_CHECK_BUKRS_AUTH (현재 MCP 미확인 — 운영 시스템에서 확인 필요).

**📷 화면** (엑셀 "고객사 특화 로직"): LGE 전용 권한 체크 로직 화면

![authorization 화면](../../assets/authorization/img79.png)

![authorization 화면](../../assets/authorization/img80.png)

![authorization 화면](../../assets/authorization/img81.png)

![authorization 화면](../../assets/authorization/img82.png)

![authorization 화면](../../assets/authorization/img83.png)

![authorization 화면](../../assets/authorization/img84.png)

![authorization 화면](../../assets/authorization/img85.png)

![authorization 화면](../../assets/authorization/img86.png)

![authorization 화면](../../assets/authorization/img87.png)
