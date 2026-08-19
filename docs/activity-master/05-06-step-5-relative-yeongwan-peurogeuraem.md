---
id: activity-master/05-06-step-5-relative-yeongwan-peurogeuraem
doc: activity-master
title: 5. 초기 운영자 셋업 절차 (단계별) > 5.6 STEP 5 — Relative(연관 프로그램) 등록 (Relative 탭)
parent: docs/activity-master/README.md
---

# 5. 초기 운영자 셋업 절차 (단계별)

## 5.6 STEP 5 — Relative(연관 프로그램) 등록 (Relative 탭)

Monitoring Dashboard에서 Activity와 함께 보여줄 연관 프로그램/URL을 등록합니다.

| 항목 | 설정 내용 |
|---|---|
| Activity | General 탭에서 등록한 Group/Sub/Activity 기재 |
| Relative Type | Dashboard 표시 분류 (T·R·M·E·U 등) |
| Transaction Code | 연결할 T-Code (Type T/R/M/E 시 필수) |
| Legacy URL / RFC Destination | 연결 URL / RFC Destination (Type U 시 필수) |
| Shown Sequence / Relative Text | 표시 순서 / 설명 Text |
| Call Type | T=Manual 일부 / P=표준·Auto 필수 |
| Skip First Screen / Variant | 조회화면 Skip / Variant 설정 |

> [ ✔ 검증 ]<br>[URL]\(Relative 탭) → ZFPAC_SET_LEGACY_URL (FG ZPAC017). 디스패치 Form CALL_SCREEN_LEGACY_URL5.<br>[Param]\(Relative 탭) → ZFPAC_REL_PARAM (FG ZPAC025, 'Assign Relative Parameter').

> [ 화면 캡처 필요 ]<br>Relative 탭에서 연관 프로그램(T-Code/URL) 등록 ALV를 캡처.
