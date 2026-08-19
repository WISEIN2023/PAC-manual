---
id: org-master/03-bijeuniseu-yuhyeong-business-type-jeongui
doc: org-master
title: 3. 비즈니스 유형(Business Type) 정의
parent: docs/org-master/README.md
---

# 3. 비즈니스 유형(Business Type) 정의

비즈니스 유형(Business Type, BUSTY)은 조직이 수행하는 결산 업무의 성격을 분류하는 코드입니다. 회사코드·사업영역·결산단위 마스터에서 각 조직에 비즈니스 유형을 지정하며, 이 유형에 따라 결산 시나리오(Activity 구성)가 달라집니다.

## 3.1 ZLPAC0013 — 비즈니스 유형 정의

| 구분 | 내용 |  |  |
|---|---|---|---|
| 프로그램 / 트랜잭션 | ZLPAC0013 |  |  |
| 프로그램 설명 | Define Business Type (비즈니스 유형 정의) |  |  |
| 유지보수 테이블 | ZTPAC_BUSTY (Business Type Master) |  |  |
| 기능 | 결산 업무 유형(비즈니스 유형) 코드와 그 레벨(BLEVEL)을 정의합니다. |  |  |
| 필드 | 의미 | 설명 | 키 |
| Business Type | 비즈니스 유형 코드 | 키. 비즈니스 유형을 식별하는 코드 | ★ |
| TEXT | 비즈니스 유형명 | 유형 코드의 설명 텍스트 |  |
| Business Type Level | 유형 레벨 | 유형이 적용되는 조직 레벨 (A / C=회사코드 / B=사업영역 / K=결산단위) |  |
| Business Package | 비즈니스 패키지 | 유형이 속한 비즈니스 패키지 |  |
| Inactive | 삭제 플래그 | 삭제 표시 |  |
| 핵심 포인트<br>비즈니스 유형은 다른 조직 마스터(회사코드·사업영역·결산단위)가 참조하는 상위 기준 정보입니다. 이미 사용 중인 유형을 변경/삭제하면 해당 조직의 결산 시나리오에 영향을 줄 수 있으므로, 사용 여부를 먼저 확인한 뒤 조정하십시오.<br>사용 중인 유형을 변경한 경우<br>ZLPAC0050에서 법인별 Business Type을 변경해야 Map에 출력됩니다.<br>(이때는 Assigned된 내역을 삭제해야 변경 가능) |  |  |  |

## 3.2 ZLPAC0017 — 회사코드별 비즈니스 유형 정의

| 구분 | 내용 |  |  |
|---|---|---|---|
| 프로그램 / 트랜잭션 | ZLPAC0017 |  |  |
| 프로그램 설명 | Define Business Type By Company Code (회사코드 레벨 비즈니스 유형 정의) |  |  |
| 유지보수 테이블 | ZTPAC_COM_BUSTY (Business Type for Company Code Level) |  |  |
| 기능 | 회사코드 레벨에서 사용하는 비즈니스 유형 코드와 텍스트를 정의합니다. |  |  |
| 필드 | 의미 | 설명 | 키 |
| Bus.Type | 비즈니스 유형 코드 | 키. 회사코드 레벨 비즈니스 유형 | ★ |
| TEXT | 비즈니스 유형명 | 키. 유형 코드의 설명 텍스트 | ★ |
| Inactive | 삭제 플래그 | 삭제 표시(논리 삭제) |  |
| ⚠ 주의<br>유지보수 대상 테이블 ZTPAC_COM_BUSTY 의 데이터 사전(DDIC) 라벨은 ‘Business Type for Company Code Level(미사용)’ 로 등록되어 있습니다. 즉 이 테이블은 현재 운영에서 사용하지 않는 것으로 표기되어 있으므로, 본 프로그램을 사용하기 전에 반드시 실제 운영 환경에서의 사용 여부를 확인하시기 바랍니다. |  |  |  |
