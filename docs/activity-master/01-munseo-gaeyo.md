---
id: activity-master/01-munseo-gaeyo
doc: activity-master
title: 1. 문서 개요
parent: docs/activity-master/README.md
---

# 1. 문서 개요

> [ 안내 ]<br>대부분의 Activity Master 및 Modeling 관련 내용은 고객사별 교육 자료를 참고할 수 있습니다.

## 1.1 자주 묻는 질문(FAQ) — 빠른 찾기

| 이런 질문일 때 | 짧은 답 / 볼 곳 |
|---|---|
| Activity 코드를 바꾸고 싶어요 | Group/Sub/Activity 코드는 자동 채번이라 변경 불가. (5장 STEP1·STEP2) |
| 스케줄을 Activity에 연결하려면? | General tab의 Activity Master 속성 지정 . Activity type : Schedule 로 지정한 뒤, Schedule 필드를 통해 맵핑 → ZFPAC_CLOSING_ASSIGN. (5.2, 6장) |
| 연관 프로그램(T-Code)을 붙이려면? | Relative 탭에서 등록. (5.6) |
| Rework(재작업) 감지를 설정하려면? | Rework 버튼 → ZFPAC_RULE_TO_ACTIVITY. 사전: ZLPAC3000/3010. (5.4, 7장) |
| 선후행 Activity를 묶으려면?
Linked Activity 가 뭔가요? | Link 버튼(Linked Activity) → ZFPAC_LINKED_PID_ASSIGN. (5.5)
모두 수행된 상태에서 선행작업이 재수행되었을 때 반드시 후행액티비티의 재작업이 필요한 경우 지정. |
| Trigger(자동수행)를 설정하려면? | 사전 ZLPAC0070에서 Trigger Code 정의 후 Trigger Define. (5장 Type X, 7장) |
| 어떤 항목이 어떤 Function을 부르나? | 6장 『항목별 호출 Function 매핑표』. |
