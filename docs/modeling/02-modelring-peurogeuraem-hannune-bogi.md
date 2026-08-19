---
id: modeling/02-modelring-peurogeuraem-hannune-bogi
doc: modeling
title: 2. 모델링 프로그램 한눈에 보기
parent: docs/modeling/README.md
---

# 2. 모델링 프로그램 한눈에 보기

## 2.1 프로그램 목록

본 메뉴얼에서 다루는 모델링 관련 프로그램은 다음과 같습니다. 표준 설명(Description)은 MCP를 통해 실제 소스에서 확인한 값입니다.

| 프로그램 | 표준 설명 | 역할 | 본문 |
|---|---|---|---|
| ZLPAC0030 | Maintain Standard Map | 표준 모델링 | 3장 |
| ZLPAC0040 | Maintain Organization Map | 조직 모델링 | 4장 |
| ZLPAC0031 | Maintain Global Package Standard Map | 글로벌 표준 모델링 | 5장 |
| ZLPAC0041 | Maintain Global Package Organization Map | 글로벌 조직 모델링 | 5장 |
| ZLPAC0050 | Assign Organization to Business Package | CO 등 조직 등록/모델 확인 | 6장 |
| 보완 설명 — ZLPAC0030 / ZLPAC0040 의 include 구성<br>두 프로그램은 표준 모듈풀(module pool) 구조로, _TOP(전역선언) · _SCR(선택화면) · _MAIN(수행) · _O01(PBO) · _I01(PAI) · _F01(폼루틴) include로 구성됩니다. 유지보수 시 로직은 대부분 _F01 에 있습니다.<br>글로벌 버전(ZLPAC0031/0041)의 include 최상단 주석에는 원본인 ZLPAC0030/0040 이름이 남아 있으나, 이는 복제 후 파생된 흔적으로 실제 프로그램은 각각 독립적으로 동작합니다. |  |  |  |

## 2.2 조직 레벨(PACLVL) — 조직 모델링의 핵심 개념

조직 모델링(ZLPAC0040)과 조직 등록(ZLPAC0050)의 동작은 Business Package별 '조직 레벨'에 따라 달라집니다. 조직 레벨은 설정 테이블 ZTPAC_CONFIG 의 PACLVL 필드에 저장되며, 다음 세 값 중 하나를 가집니다.

| PACLVL | 조직 레벨 | 저장 테이블 | 키(식별) 조합 |
|---|---|---|---|
| C | 회사코드 (Company Code) | ZTPAC_CONFIG_COM | 회사코드(BUKRS) |
| B | 사업영역 (Business Area) | ZTPAC_CONFIG_BA | 회사코드 + 사업영역(GSBER) |
| U | 결산단위 (Closing Unit) | ZTPAC_CONFIG_UNI | 회사코드 + 결산단위(CUNIT) |
| 핵심 포인트<br>조직 레벨(PACLVL)은 Business Package마다 하나로 고정됩니다. 즉 같은 Business Package 안에서는 회사코드/사업영역/결산단위 중 한 가지 기준으로만 조직이 관리됩니다.<br>회사코드 필수 여부는 별도 플래그 REQ_BUKRS 로 제어됩니다. PACLVL이 B 또는 U라도 REQ_BUKRS='X' 이면 회사코드도 함께 입력해야 합니다. |  |  |  |

## 2.3 모델링과 함께 사용하는 관련 프로그램

모델링 작업 전·후에 함께 사용하는 프로그램입니다. 표준 설명은 MCP로 확인한 실제 값입니다.

| 프로그램 | 표준 설명 | 모델링에서의 역할 |
|---|---|---|
| ZLPAC0020 | Define Activity Master | Activity Group 번호·명칭을 확인/정의. 모델링 전 준비 단계. |
| ZLPAC1050 | Maintain Special Role | 2·3 Level 모델링 수정 권한(Special Role) 부여. |
| ZLPAC0140 | Display Modeling List | 모델링 결과(레벨별)를 조회. 삭제 완료·최하위 모델링 확인. |

## 2.4 모델링 데이터가 저장되는 테이블

모델링 화면에서 그린 네트워크 그래프는 **노드(Node)** 와 **링크(Link)** 두 종류의 테이블로 나뉘어 저장됩니다. 여기에 **표준(Standard) /조직(Organization)** 구분과 **운영데이터 /결산 확정 스냅샷** 구분이 더해져 아래 8개 테이블이 사용됩니다.

| 테이블 | 구분 | 용도 |
|---|---|---|
| ZTPAC_STD_NODE | 표준 · 노드 | 표준 모델(ZLPAC0030 / ZLPAC0031)의 노드(Activity) 정보. ZLPAC0140 Standard Map 조회의 기준 테이블. |
| ZTPAC_STD_LINK | 표준 · 링크 | 표준 모델의 노드 간 연결선(선행 노드 → 후행 노드) 정보. |
| ZTPAC_ORG_NODE | 조직 · 노드 | 조직 모델(ZLPAC0040 / ZLPAC0041)의 조직별 노드 정보. ZLPAC0050의 LINK 조회, ZLPAC0140 Organization Map 조회에 사용. |
| ZTPAC_ORG_LINK | 조직 · 링크 | 조직 모델의 노드 간 연결선 정보. |
| ZTPAC_CLD_SNODE | 확정 · 표준 · 노드 | 결산 마감(Closed) 시점의 표준 모델 노드 스냅샷. 결산월(CLMON) 단위로 보관. |
| ZTPAC_CLD_SLINK | 확정 · 표준 · 링크 | 결산 마감 시점의 표준 모델 링크 스냅샷. |
| ZTPAC_CLD_ONODE | 확정 · 조직 · 노드 | 결산 마감 시점의 조직 모델 노드 스냅샷. |
| ZTPAC_CLD_OLINK | 확정 · 조직 · 링크 | 결산 마감 시점의 조직 모델 링크 스냅샷. |

> 보완 설명 — 테이블 이름 읽는 법<br>테이블 이름은 ZTPAC_ + 대상(STD 표준 / ORG 조직 / CLD 결산 확정) + 종류(NODE 노드 / LINK 링크) 규칙으로 되어 있습니다. 확정 테이블은 조직 여부를 앞 글자로 다시 구분합니다 — CLD_S…(Standard) / CLD_O…(Organization).<br>운영 · 확정 테이블의 차이는 키에 결산월(`CLMON`) 이 있는지 여부입니다. 운영 테이블은 현재 시점의 모델 1벌만 보관하고, CLD_ 테이블은 결산월별로 그 시점의 모델을 남깁니다. "지난달에는 어떤 모습이었나"는 CLD_ 테이블에서 확인합니다.<br>조직 테이블(ORG_, CLD_O…)은 키에 회사코드 · 사업영역 · 결산단위(BUKRS / GSBER / CUNIT)를 가지며, 표준 테이블(STD_, CLD_S…)은 대신 Business Type(BUSTY)을 가집니다.<br>모든 테이블은 삭제 플래그 LOEVM 을 사용하는 논리 삭제 방식입니다. 화면에서 지운 노드도 LOEVM = 'X' 로 남아 있을 수 있으므로, 테이블을 직접 조회할 때는 LOEVM 조건을 반드시 확인합니다.<br>※ 운영 현장에서 확정 테이블을 ZTPAC_CLO_… 로 부르는 경우가 있으나, 실제 DDIC 오브젝트명은 ZTPAC_CLD_… 입니다(SE11 조회 시 CLD 로 입력).<br>※ 위 테이블은 반드시 모델링 프로그램을 통해서만 변경해야 합니다. SE16 등으로 직접 수정하면 노드와 링크의 정합성이 깨져 그래프가 열리지 않을 수 있습니다.
