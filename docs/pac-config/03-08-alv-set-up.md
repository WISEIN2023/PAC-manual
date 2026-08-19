---
id: pac-config/03-08-alv-set-up
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.8 ALV Set-up
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.8 ALV Set-up

### 3.8.1 PAGING — Lines per Page

**테이블-필드:** ZTPACSYS - PAGING

**운영 설정(LG전자 설정) :** 30000

#### 설정 설명

ALV Manager를 사용하는 화면에서 한 화면에 보여지는 ALV 라인페이지수를 지정한다

- 해당 라인이 초과되는 경우 Page로 적용하여 한화면에 보이는 라인페이지를 제한한다 (화면 성능을 위해)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CIS_DISPLAY_SNID(LZPACCIS0010U01)

#### 프로세스 관점 분석 (사용 로직)

ALV Manager 사용 화면의 페이지당 라인 수.

① 결산점검 시나리오 결과 조회(ZFPAC_CIS_DISPLAY_SNID)에서 대용량 결과를 PAGING 단위로 나누어 표시 — 과도한 라인 표시로 인한 메모리/렌더링 부하 방지.

#### 영향도 분석 (변경 시 영향)

값을 키우면 한 화면 표시량이 늘어나는 대신 대용량 조회 시 응답 지연/메모리 사용 증가.

지나치게 작으면 페이지 이동이 잦아져 사용성 저하.
