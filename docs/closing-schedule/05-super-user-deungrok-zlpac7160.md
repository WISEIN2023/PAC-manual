---
id: closing-schedule/05-super-user-deungrok-zlpac7160
doc: closing-schedule
title: 5. Super User 등록 (ZLPAC7160)
parent: docs/closing-schedule/README.md
---

# 5. Super User 등록 (ZLPAC7160)

## 5.1 개요 및 용도

**화면명** Posting Super User Registration    **T-Code** ZLPAC7160

결산 일정 체킹과 상관없이 기표가 가능하도록 Super User를 등록하는 프로그램입니다. Posting Block 상태에서, 등록한 User에 한하여 특정 G/L 계정에 대해 입력한 조직·기간 동안의 기표를 허용합니다.

> 주의<br>기표의 통제 및 예외 처리는 임시 전표·전기 전표를 수행하는 시점의 로그인 유저에 따라 통제됩니다. 따라서 Super User 등록 여부를 결정할 때에는 전표 생성/승인 시점의 사용자를 등록해야 합니다.

## 5.2 입력 항목

| 항목 | 설명 |
|---|---|
| Email | Email로 사용자를 입력. Search Help(F4)로 사용자명·SAP ID 등의 조건으로 검색하여 선택 |
| G/L From | 기표를 허용할 G/L 계정 입력 |
| Valid to Date | 유효 기간(일자) 설정. 수시로 변경 가능 |
| Valid to Time | Super User의 유효 시간 설정. 수시로 변경 가능 |
| Exception Reason | 예외 유저 등록 사유 입력 |

> 시스템 확인 — Super User 저장 구조<br>Super User 등록 내역은 테이블 ZTPAC_SCH_EXCEPT(Super Key user Registration for Closing Schedule)에 저장됩니다.<br>주요 필드: USRID(사용자) · SMTP_ADDR(Email) · FHKONT(G/L From) · THKONT(G/L To) · VALIDTO(Valid to Date) · VALIDTM(Valid to Time) · REASON(Exception Reason). 회사코드/사업영역/년월이 키로 사용되어, 등록한 조직·기간 동안만 예외가 적용됩니다.

![closing-schedule 화면](../../assets/closing-schedule/img31.png)

[ZLPAC7160] Posting Super User Registration — 예외 기표 사용자 등록
