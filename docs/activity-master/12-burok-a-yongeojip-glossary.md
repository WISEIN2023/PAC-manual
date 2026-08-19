---
id: activity-master/12-burok-a-yongeojip-glossary
doc: activity-master
title: 부록 A. 용어집 (Glossary)
parent: docs/activity-master/README.md
---

# 부록 A. 용어집 (Glossary)

| 용어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. SAP 결산 작업을 자동 실행·관리하는 결산자동화 솔루션. |
| Activity (Closing ID) | PAC 결산 작업의 한 단위. 실제로 수행되는 프로그램이 설정된 최하위 레벨. |
| Activity Group / Sub-Group | Activity의 묶음(상위) / Closing ID의 묶음(중간) 레벨. |
| Business Package (BUPAK) | PAC를 구성하는 기본 수행 단위(최상위 묶음). |
| PID | Activity를 식별하는 ID(코드). 모든 세부 셋업의 기준 키. |
| Maintain Level | Activity Master 실행 Level. 모델링 Level(2/3)에 따라 표시 단계가 달라짐. |
| Activity Type | C=Closing Schedule, F=Confirmation, I=Closing Inspection, L=Legacy, M=Dummy, N=Function, T=Transaction, X=Auto Trigger. |
| Call Type | P=Program(표준·Auto 필수), T=Transaction(Manual 일부). |
| Auto / Manual | Auto=Start로 자동 수행, Manual=사용자가 직접 입력·Complete. |
| Relative | Monitoring Dashboard에서 Activity와 함께 보여줄 연관 프로그램/URL. |
| Rework(재작업) | 완료된 Activity에 추가 기표가 감지되어 재수행이 필요한 상태. Rework Rule ID로 감지. |
| Rework Rule ID | 재기표를 감지하는 규칙(G/L 계정 범위 등). ZLPAC3000/3010에서 정의. |
| Linked Activity | 선후행 관계의 후행 Activity 묶음. Linked Rework / Reset Linked에 사용. |
| Trigger Code | 타 시스템/모듈/조직/Bus.Pkg 간 완료 정보를 I/F 받아 상태 반영하는 코드(ZLPAC0070). |
| By Function (N) | Function Module 호출로 수행되는 Activity 유형. |
| Closing Schedule | 결산 마감 일정. 모델링과 연계해 특정 시점 자동 마감. |
| CIS / Closing Inspection | 결산점검. 시나리오(Category ID)로 결산 데이터 검증. |
| Map (Standard / Organization) | Activity Sub-Group을 Node로 연결한 프로세스 흐름도(ZLPAC0030/0040). |
| Variant / Param | 프로그램 실행 변형(Variant) / 호출 파라미터(Log Field·Screen Param·Constant). 합집합 수행. |
| Tcode vs 프로그램 | GetTransaction으로 구분. 본 화면 ZLPAC0020은 실제 Tcode. |
| MCP (ADT) | SAP ABAP Development Tools 연동. 본 매뉴얼의 객체 검증(읽기 전용)에 사용. |
