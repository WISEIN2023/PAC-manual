---
id: modeling/10-hyeonjang-unyeong-siseutem-geomjeungi
doc: modeling
title: 10. 현장(운영 시스템) 검증이 필요한 항목
parent: docs/modeling/README.md
---

# 10. 현장(운영 시스템) 검증이 필요한 항목

본 문서는 MCP(ABAP ADT)로 확인한 소스 사실을 기준으로 작성했습니다. 다음 항목은 시스템·데이터·릴리스에 따라 달라질 수 있어 운영 시스템에서 확인이 필요합니다.

- Business Type 레벨(BLEVEL)의 전체 코드 체계: 소스에서 A/C/B/K 값이 사용됨을 확인했으나(예: 'C'는 글로벌 전환 조건, 'K'는 조직 등록에서 패키지 특정 유형으로 우선 조회), 각 코드의 공식 명칭·정의는 도메인 값으로 확인 필요.
- 특정 CO Business Package의 조직 레벨/회사코드 필수 설정: ZTPAC_CONFIG 의 PACLVL·REQ_BUKRS 실제 값(6.5 현장확인 참조).
- 결산단위(CUNIT) 필드의 표시 라벨: 패키지별로 다르게 표시되므로(get_cunit_field_name) 대상 패키지에서 확인.
- 모델링 프로그램의 트랜잭션 코드/메뉴 진입 경로: ZLPAC0050은 동일명 트랜잭션 확인. ZLPAC0030/0031/0040/0041의 실제 메뉴 진입 경로는 운영 시스템 메뉴에서 확인.
- 각 오류 메시지(S112, S253~255, E003, E091, S429, E604 등)의 운영 시스템 실제 텍스트: 메시지 클래스 ZPAC01 기준으로 확인 가능.
