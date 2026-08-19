---
id: authorization/04-sap-gwonhan-gibongi
doc: authorization
title: 3. SAP 권한 기본기
parent: docs/authorization/README.md
---

# 3. SAP 권한 기본기

이 장은 PAC 권한 업무에 필요한 SAP 공통 지식을 다룹니다. SAP가 처음이라면 이 장을 먼저 숙지하세요.

## 3.1 PFCG와 Role의 구조

**PFCG**는 SAP에서 «권한(Role)을 만들고 편집하는» 핵심 Tcode입니다. Role은 권한의 묶음이라고 생각하면 됩니다. PAC에서는 Role을 두 단계로 나눠 관리합니다.

| 구분 | Master Role | Variant Role |
|---|---|---|
| 생성 단위 | T-code 단위 | T-code + 조직 단위 |
| 역할 | 권한 Object 설정의 «기준»이 되는 역할 | Master를 «상속»받아 실제 사용자에게 부여 |
| 여기에 담는 것 | 권한 줄 Tcode, Fiori Catalog 등 | 세부 Authorization Object로 권한 제어 |
| 사용자가 받는 것 | (직접 부여 안 함) | ✔ 실제 사용자가 부여받는 것은 Variant Role |
| 예시 | ZM_FCW_RAC_SUBSIDIARY | ZV_FCW_RAC_SUBSIDIARY_ASIA |

LG전자 PAC에서는 **ZPAC_BUPAK** 라는 Authorization Object로 Business Package별 권한을 제어합니다.

## 3.2 PFCG 네이밍룰 (LG 예시)

- **Master Role:** ZM_FCW_*
- **Variant Role:** ZV_FCW_*
**📌 LG 특이사항** 원래 Master : Variant = 1:1 구조였으나, 권한부여 2차 결재자가 법인별로 달라서, 권한별로 결재자를 다르게 세팅하기 위해 Variant Role을 법인 단위로 분리 생성했습니다. (예: ZV_FCW_RAC_SUBSIDIARY_ASIA, ZV_FCW_RAC_SUBSIDIARY_EUROPE)

## 3.3 꼭 알아야 할 주요 테이블

| 테이블 | 설명 | 주요 Key | 언제 쓰나 |
|---|---|---|---|
| AGR_DEFINE | Role 이름 + 설명 | AGR_NAME | Role 기본 정보 확인 |
| AGR_1251 | Role의 Authorization Object 정보 | AGR_NAME, OBJECT | Role에 어떤 권한 Object가 있나 |
| AGR_USERS | 사용자별 보유 Role 목록 | BNAME, AGR_NAME | 이 사람이 무슨 Role 갖고 있나 |
| AGR_TCODES | Role에 포함된 Tcode 목록 | AGR_NAME, TCODE | Role에 이 Tcode가 있나 |
| USR02 | SAP 로그온 사용자 | BNAME | 로그인 안 될 때 1순위 확인 |
| AGR_AGRS | Composite Role의 상·하위 관계 | AGR_NAME, CHILD_AGR | Role 구조 파악 |

## 3.4 꼭 알아야 할 주요 Tcode

| Tcode | 용도 | 대표 활용 |
|---|---|---|
| PFCG | Role 생성·수정, 권한 Object 부여 | 권한 관리의 핵심. Role 만들 때 제일 먼저 여는 화면 |
| SU01 | 사용자 생성·수정, 잠금해제, Role 배정 | 운영 중 가장 빈번하게 쓰는 Tcode |
| SU53 | 직전 권한오류의 원인 Object 확인 | 부족 Object 확인 → 해당 Object 가진 Role 찾기 → 추가 |
| SUIM | 권한 분석 통합 도구 | "이 Role을 누가 갖고 있나", "이 Object 가진 Role은" 즉답 |
| TSTC | 전체 Tcode 리스트 확인 | Tcode 존재 여부 조회 |
| PFCGMASSVAL | 여러 Role의 권한값 일괄 변경 | 신규 법인코드 추가 등 (5.7 참고) |
