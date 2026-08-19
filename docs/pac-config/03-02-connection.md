---
id: pac-config/03-02-connection
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.2 Connection
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.2 Connection

### 3.2.1 FRONT_DEST — Front End RFC Destination

**테이블-필드:** ZTPACSYS - FRONT_DEST

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

Front End 서버가 다른경우 RFC Destination을 정의

#### 참조 프로그램 / 오브젝트 (Where-used)

■ 정적 참조 미검출 (ZLPACSYS 관리 화면에서만 유지)

#### 프로세스 관점 분석 (사용 로직)

Front End 서버 분리 구성 시 RFC Destination.

① WBCROSSGT 필드레벨 Where-used 상 런타임 코드의 정적 참조가 검출되지 않음 — Front/Back 분리 아키텍처 대비용 예약 설정으로, 단일 서버 구성에서는 미사용.

#### 영향도 분석 (변경 시 영향)

현재 값을 변경해도 동작 변화 없음(정적 참조 없음).

Front-End 분리 구성 도입 시에만 의미를 가지며, 그 경우 URL 생성(ZCL_PAC_FUNC=>GET_URL) 경로 재검증 필요.

### 3.2.2 FIORI_URL — Fiori URL

**테이블-필드:** ZTPACSYS - FIORI_URL

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

Front End 서버가 다른경우 Fiori URL 정의

#### 참조 프로그램 / 오브젝트 (Where-used)

■ 정적 참조 미검출 (ZLPACSYS 관리 화면에서만 유지)

#### 프로세스 관점 분석 (사용 로직)

Front End 분리 시 Fiori URL.

① FRONT_DEST와 동일하게 정적 참조 미검출. 현재 URL 생성은 ZCL_PAC_FUNC=>GET_URL이 /UI2/CL_START_URL(자기 시스템 FLP 기준)로 처리하므로 본 필드는 미사용.

#### 영향도 분석 (변경 시 영향)

현재 값을 변경해도 동작 변화 없음. Front-End 분리 구성 도입 시 재검토 대상.
