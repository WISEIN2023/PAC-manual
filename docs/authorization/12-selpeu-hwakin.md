---
id: authorization/12-selpeu-hwakin
doc: authorization
title: 11. 셀프 확인
parent: docs/authorization/README.md
---

# 11. 셀프 확인

## 11.1 개념 확인 문제

1. PAC Role, Participant, Special Auth의 차이를 각각 한 문장으로 설명해 보세요.
2. 사용자가 "Fiori 접속하자마자 오류"라고 하면 가장 먼저 무엇을 의심하나요?
3. "대시보드는 뜨는데 법인이 안 보인다"의 1차 원인은?
4. Master Role과 Variant Role 중 실제 사용자가 부여받는 것은?
5. ZLPAC0080과 ZLPAC7160은 각각 무슨 «예외»를 다루나요? (헷갈리기 쉬움)
6. ZLPACSYS의 검사방식 S/O/A와 Special Role 타입 A/T의 차이는?
7. Derive 후 ZPAC_BUPAK 값이 깨졌을 때 복원 도구는?

## 11.2 실습 과제 (운영 외 환경)

1. SU01에서 임의 테스트 사용자의 보유 Role 목록을 조회해 보기
2. SUIM으로 특정 PFCG Role을 가진 사용자 리스트 조회해 보기
3. AGR_1251에서 한 Variant Role의 ZPAC_BUPAK 값 확인해 보기
4. ZLPAC1000 화면에서 Participant 등록 화면 구조 살펴보기(저장 X)
5. SU53 화면을 열어 직전 권한오류 분석 방법 익히기

## 11.3 자주 하는 실수 체크

- Special Auth를 일반 사용자에게 부여 → 전체 법인 접근됨. 절대 주의
- Area Menu에 Tcode만 추가하고 Auth Object 부여를 빠뜨림
- PFCGMASSVAL를 Simulation 없이 Direct Execution
- Master Role에 P_PROGNAM=* 직접 입력(권한 T/F 가이드 위반) — Variant에서만 *
