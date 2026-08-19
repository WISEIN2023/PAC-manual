---
id: activity-master/05-05-step-4-linked-activity-deungrok-seonhuhaeng
doc: activity-master
title: 5. 초기 운영자 셋업 절차 (단계별) > 5.5 STEP 4 — Linked Activity 등록 (선후행 연결)
parent: docs/activity-master/README.md
---

# 5. 초기 운영자 셋업 절차 (단계별)

## 5.5 STEP 4 — Linked Activity 등록 (선후행 연결)

선행 Activity 재수행 시 후행 Activity에 일괄 Rework(Linked Rework)을 발생시키고, 선행 Reset 시 후행도 일괄 Reset(Reset Linked)할 수 있도록 후행 Activity를 등록합니다.

1,2,3번 순차 수행 Activiyt가 완료 후, 1번Activity를 다시 수행시킨 경우 2,3번에 대해서 Rework Occurred로 발생시킬수 있다.

1. Not Assigned에서 Activity Group/Activity 입력 → 등록할 Closing ID 검색.
2. ← 버튼으로 선택한 Closing ID를 Assign.
3. Assigned에 등록 확인 후 저장.
- **Linked Rework:** 선행 재수행 시 후행에 Rework 발생 (원인 Closing ID·사용자·시점 로그 제공).
- **Reset Linked:** 후행 Activity 일괄 Reset (다른 Group 하위 Closing ID도 가능).

> [ ✔ 검증 ]<br>[Link]\(LINK_ICON) → ZFPAC_LINKED_PID_ASSIGN (FG ZPAC022, 'Assign Linked Acitivty ID'). 테이블 ZTPAC_REWORK_LKD.
