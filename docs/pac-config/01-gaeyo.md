---
id: pac-config/01-gaeyo
doc: pac-config
title: 1. 개요
parent: docs/pac-config/README.md
---

# 1. 개요

본 문서는 SAP 결산자동화 솔루션 PAC(Process Automatic Channel)의 Config 설정에 대한 운영자 매뉴얼이다. PAC Config는 Business Package 단위 설정(ZTPAC_CONFIG)과 시스템 전역 설정(ZTPACSYS)으로 구성되며, 각 필드에 대해 설정 의미, 참조 프로그램(Where-used), 프로세스 관점의 사용 로직, 변경 시 영향도를 기술한다.

## 1.1 관리 프로그램

□ ZLPAC0010 - Maintain Business Package Config

□ ZLPACSYS - Maintain Business Package Config

## 1.2 문서 구성

- 2장 : Business Package Config (ZTPAC_CONFIG) — BusPkg 단위 설정 46개 필드

- 3장 : System Config (ZTPACSYS) — 시스템 전역 설정 62개 필드

- 각 필드는 [기본 정보 / 설정 설명 / 참조 프로그램·오브젝트 / 프로세스 관점 분석 / 영향도 분석 / 운영 설정] 순으로 기술한다.

## 1.3 분석 근거

- 참조 프로그램 목록 : 운영 SAP 시스템의 필드레벨 Where-used(WBCROSSGT), 프로그램-테이블 크로스레퍼런스(D010TAB), 펑션모듈 디렉토리(TFDIR), 클래스 메소드 디렉토리(TMDIR) 조회 결과 기반.

- 프로세스/영향도 분석 : ZIPAC_COMMON, ZLPAC0010, ZCL_PAC 계열 클래스, 주요 펑션모듈 소스 분석 기반.

- "정적 참조 미검출" 표기는 코드 내 필드 단위 직접 참조가 없다는 의미이며, 구조 단위(SELECT *) 접근·동적 참조 가능성은 별도 기재함.

- 테스트/데모 오브젝트(Y*)는 참조 목록에서 제외함.
