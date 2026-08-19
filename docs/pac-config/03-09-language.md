---
id: pac-config/03-09-language
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.9 Language
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.9 Language

### 3.9.1 XMULTI_LAN — Active Multi Language Maintenance

**테이블-필드:** ZTPACSYS - XMULTI_LAN

**운영 설정(LG전자 설정) :** 미사용

#### 설정 설명

□ Multi Language를 활성화 한다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZCL_PAC=>CHECK_USE_MULTI_LANGUAGE(CM01Z)/CHECK_MULTI_LANGUAGE(CM020), ZLPAC0020_F01/TOP·ZLPAC0021_F01(Activity Master),

ZLPAC0140_MAIN, ZLPAC5060_F01/TOP, ZIPAC_SYSSCREEN, ZLPACSYS_O01

#### 프로세스 관점 분석 (사용 로직)

Multi Language(다국어 텍스트) 유지보수 활성화.

① ZCL_PAC=>CHECK_USE_MULTI_LANGUAGE가 표준 판정 API로, Activity Master(ZLPAC0020/0021)·모델링 리스트(ZLPAC0140)·결산점검(ZLPAC5060) 등에서 다국어 텍스트 입력 버튼/컬럼 활성화를 제어.

② ZIPAC_SYSSCREEN: 공통 화면 제어 Include에서 언어 관련 필드 표시 분기.

#### 영향도 분석 (변경 시 영향)

활성화 시 마스터 텍스트를 언어별로 관리해야 하므로 마스터 유지보수 공수 증가.

해제 시 로그인 언어 단일 텍스트로만 운영되어 다국어 사용자 화면에 미번역 텍스트 노출 가능.
