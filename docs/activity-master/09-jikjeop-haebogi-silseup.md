---
id: activity-master/09-jikjeop-haebogi-silseup
doc: activity-master
title: 9. 직접 해보기 실습
parent: docs/activity-master/README.md
---

# 9. 직접 해보기 실습

아래 실습은 SAP GUI에서 직접 따라 하며 익히는 용도입니다. (AI가 대신 실행하지 않습니다.)

| 등급 | 의미 |
|---|---|
| 🟢 조회 | 보기만 하므로 운영 시스템에서도 가능 |
| 🟡 쓰기 | 등록·저장 등 변경 — 연습은 반드시 테스트 시스템에서, 운영(PRD)에서는 금지 |

**실습 1 — Activity Master 구조 조회 🟢**

1. ZLPAC0020 실행 → Business Package·Maintain Level 입력.
2. 좌측 Tree에서 Group > Sub-Group > Activity 계층을 펼쳐 확인.
3. Activity 행을 선택해 General/Relative 탭과 각 속성 아이콘(버튼)을 눈으로 확인.
**실습 2 — 설정 테이블 조회 🟢**

1. SE16N → ZTPAC_PROC(Activity 정의) 조회. PID·REPTY(Type)·XAUTO 확인.
2. ZTPAC_RELATIVE(연관 프로그램), ZTPAC_REWORK_LKD(Linked), ZTPAC_RW_RULEID(Rework) 조회.
**실습 3 — Activity 신규 등록 🟡 (테스트 시스템)**

1. ZLPAC0020 변경 모드 → Sub-Group 선택 → Activity 행 추가(코드 자동 채번).
2. Activity Type=T 선택, Auto?·Skip First Screen·Variant 등 설정.
3. 필요 시 [Schedule]/[Rework]/[Link] 버튼으로 세부 속성 설정 → 저장.
4. SE16N으로 ZTPAC_PROC에 저장 결과 확인.

> [ 디버깅 포인트 ]<br>실습 중 값이 의심되면 8.2 디버깅 포인트 표를 참고해 중단점을 건다.
