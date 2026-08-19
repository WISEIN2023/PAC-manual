---
id: fiori-sapgui-call/02-selreksyeon-hwamyeon-paramiteo-hochul
doc: fiori-sapgui-call
title: 2. 셀렉션 화면 파라미터 (호출 인터페이스)
parent: docs/fiori-sapgui-call/README.md
---

# 2. 셀렉션 화면 파라미터 (호출 인터페이스)

Fiori가 ZLPAC_FTCODE 를 호출할 때 넘기는 값은 모두 이 셀렉션 화면 파라미터로 수신됩니다. 파라미터는 조직·기간을 지정하는 블록(B1)과 호출 대상을 지정하는 블록(B2)으로 나뉩니다.

## 2.1 조직 · 기간 파라미터 (Block B1)

호출되는 대상 화면에 넘겨줄 결산 조직·기간 정보입니다. 대상 트랜잭션의 동일 파라미터에 매핑됩니다.

| 파라미터 | 데이터 타입 | 의미 |
|---|---|---|
| P_BUPAK | ZPAC_BUPAK | Business Package (결산 패키지 식별자) |
| P_GJAHR | GJAHR | 회계 연도 |
| P_MONAT | MONAT | 회계 기간(월) |
| P_BUKRS | BUKRS | 회사 코드(법인) |
| P_GSBER | GSBER | 사업 영역(Business Area) |
| P_CUNIT | ZPAC_CUNIT | 기타 조직 단위(Other Org) |

## 2.2 호출 대상 파라미터 (Block B2)

어떤 화면을 어떤 방식으로 열지를 결정하는 핵심 파라미터입니다. 이 값들의 조합이 3장의 분기 판정 기준이 됩니다.

| 파라미터 | 데이터 타입 | 의미 · 판정 역할 |
|---|---|---|
| P_TCODE | SY-TCODE | 직접 호출할 트랜잭션 코드 |
| P_PID | ZPAC_PID | Activity(Process) ID. Activity 정의 마스터 조회 키 |
| P_CID | ZPAC_CID | 결산점검 Category ID |
| P_RTYPE | ZPAC_REL_TYPE | Relative 호출 유형(값 존재 시 Relative 분기) |
| P_TDTYPE | ZPAC_TODO_TYPE | To-Do 유형(값 존재 시 To-Do 분기) |
| P_ITMSEQ | ZPAC_ITMSEQ | Item Sequence(Relative 호출에 전달) |

> ■ 시스템 확인 — 셀렉션 화면 정의<br>인클루드 ZLPAC_FTCODE_SCR 기준, 블록 B1(P_BUPAK·P_GJAHR·P_MONAT·P_BUKRS·P_GSBER·P_CUNIT) / 블록 B2(P_TCODE·P_PID·P_CID·P_RTYPE·P_TDTYPE·P_ITMSEQ)로 확인됨.
