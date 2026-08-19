---
id: auto-trigger/06-unyeong-yujibosu-jeomgeom-gaideu
doc: auto-trigger
title: 6. 운영 · 유지보수 점검 가이드
parent: docs/auto-trigger/README.md
---

# 6. 운영 · 유지보수 점검 가이드

## 6.1 정상 동작 확인 체크리스트

| 점검 항목 | 확인 방법 | 정상 기준 |
|---|---|---|
| Trigger Code 등록 여부 | ZLPAC0070에서 CRSCODE 조회 | 해당 CRSCODE 행 존재, XAUTO='X' |
| Activity 연결 여부 | ZLPAC0020에서 해당 Activity의 CRSCODE/TG_CRSCODE 확인 | CRSCODE 또는 TG_CRSCODE 입력됨 |
| Trigger 아이콘 표시 | ZLPAC0070 조회 결과에서 ICON 컬럼 확인 | 아이콘이 표시되면 ZTPAC_PROC와 연결됨 |
| 배치잡 상태 확인 | SM37에서 PAC 관련 잡 조회 | 오류(Aborted) 잡이 없음 |

## 6.2 증상별 점검 가이드

| 증상 | 우선 점검 사항 |
|---|---|
| Auto Trigger가 전혀 동작하지 않음 | ① ZTPAC_CROSS_IF에 CRS Code 등록 여부 (ZLPAC0070 조회)
② ZTPAC_PROC에 CRSCODE 연결 여부 (ZLPAC0020 조회)
③ PAC 엔진 실행 시 IV_AUTO_NEXT=X 전달 여부 (시스템 CONFIG 확인) |
| 특정 Trigger만 동작하지 않음 | ① ZLPAC0070에서 해당 CRSCODE의 XAUTO 체크 여부
② AUTO_TYPE 입력 여부 (XAUTO=X인데 AUTO_TYPE 공백이면 동작 안함)
③ ZFPAC_GET_CAN_START 체크 실패 여부 : 선행 Activity 완료 상태 확인 |
| Auto Trigger 후 후행이 오류로 중단됨 | ① SM37에서 오류 잡의 로그 확인
② SM21 시스템 로그 확인
③ 5장 절차에 따라 Trigger 수동 재실행 |
| 잘못된 조직/법인으로 Trigger가 발동됨 | ① ZTPAC_CROSS_IF의 TG_BUPAK 값 확인
② ZTPAC_PROC의 CRSCODE 연결 Activity 확인 (ZLPAC0070 아이콘 클릭) |
