---
id: pac-config/03-04-mailing
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.4 Mailing
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.4 Mailing

### 3.4.1 MAIL_OTYP — Mailing Output Style

**테이블-필드:** ZTPACSYS - MAIL_OTYP

**운영 설정(LG전자 설정) :** F : Full Address

#### 설정 설명

□ 메일링 표시방법을 선택

F : Full Address => 메일주소 전체를 표시한다

S : Short Address(Front @) => @ 앞부분만 표시한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_FUNC=>CONVERT_MAIL_ADDRESS(CM007)

#### 프로세스 관점 분석 (사용 로직)

메일 주소 표시 방법(F: Full Address / S: Short).

① CONVERT_MAIL_ADDRESS: 'S'이면 메일 주소를 '@' 기준으로 SPLIT하여 ID 부분만 표시. 메일 수신자 목록 등 주소 출력 경로에서 공통 사용.

#### 영향도 분석 (변경 시 영향)

표시 전용 설정 — 발송 자체에는 영향 없고 화면/메일 본문의 주소 표기 형식만 변경.
