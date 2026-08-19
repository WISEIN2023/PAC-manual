---
id: monitoring/11-hyeonjang-unyeong-siseutem-geomjeungi
doc: monitoring
title: 11. 현장(운영 시스템) 검증이 필요한 항목
parent: docs/monitoring/README.md
---

# 11. 현장(운영 시스템) 검증이 필요한 항목

본 메뉴얼은 소스 확인 사실만 기술했습니다. 다음 항목은 화면 텍스트 요소(TEXT-symbol)·시스템 설정·권한 롤 등에 따라 달라질 수 있으므로, 운영 시스템에서 최종 확인하시기 바랍니다.

- 각 선택화면 항목의 실제 화면 라벨(TEXT-001 등 텍스트 요소로 정의됨)과 리스트박스 표기.
- ZLPAC0170 의 라디오 버튼(P_RAD1 / P_RAD2)이 화면에 표시하는 정확한 명칭과 각 옵션의 조회 범위 차이.
- 자동 새로고침 기본값(ZTPACSYS-REFRESH_MIN / REFRESH_MAX)의 실제 설정 값.
- HQ 권한(글로벌 GPID) 및 각 조직 권한 롤(ZCL_PAC_AUTH)의 실제 부여 정책.
- 트랜잭션 코드로 각 프로그램을 실행하는 경우의 T-Code 매핑(운영 시스템의 SE93 기준).
