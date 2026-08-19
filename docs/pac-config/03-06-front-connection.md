---
id: pac-config/03-06-front-connection
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.6 Front Connection
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.6 Front Connection

### 3.6.1 XSECURE_URL — Active Secure URL?

**테이블-필드:** ZTPACSYS - XSECURE_URL

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

□ X 활성화시 : Fiori URL 연결시 암호화를 통해 URL을 변환해 전송한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC_FUNC=>ON_SECURE_URL(CM00W) ← ZFPAC_GET_PORTAL_LINK 등 URL 생성 전 경로

#### 프로세스 관점 분석 (사용 로직)

Fiori URL 연결 시 암호화 변환 활성화.

① ON_SECURE_URL: 모든 URL 생성 경로(포털 링크, 메일 링크)가 이 메소드를 통과하며, 'X'이면 URL을 암호화 변환하여 전송, 공백이면 원본 URL 그대로 반환.

#### 영향도 분석 (변경 시 영향)

활성화 시 생성되는 모든 딥링크 URL 형식이 바뀌므로 수신측(포털/브라우저)의 복호화 처리와 반드시 세트로 구성해야 함 — 단독 활성화 시 링크 전체가 깨질 수 있음.
