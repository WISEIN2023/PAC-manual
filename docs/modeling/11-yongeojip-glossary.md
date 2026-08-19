---
id: modeling/11-yongeojip-glossary
doc: modeling
title: 11. 용어집 (Glossary)
parent: docs/modeling/README.md
---

# 11. 용어집 (Glossary)

본 문서에 등장하는 주요 용어·약어·오브젝트를 정리합니다. 오브젝트 항목은 MCP로 확인한 실제 표준 설명을 기준으로 합니다.

| 용어 / 오브젝트 | 설명 |
|---|---|
| PAC | Process Automatic Channel. 본 문서의 대상인 SAP 결산자동화 솔루션. |
| 모델링(Modeling) | 결산 작업(Activity)을 노드/링크로 연결해 프로세스 흐름을 정의하는 작업. PAC에서는 네트워크 그래프로 표현. |
| ZLPAC0030 | Maintain Standard Map. 표준 모델링 프로그램. |
| ZLPAC0040 | Maintain Organization Map. 조직 모델링 프로그램. |
| ZLPAC0031 | Maintain Global Package Standard Map. 글로벌 표준 모델링 프로그램. |
| ZLPAC0041 | Maintain Global Package Organization Map. 글로벌 조직 모델링 프로그램(회사코드 레벨). |
| ZLPAC0050 | Assign Organization to Business Package. Business Package에 조직(회사/사업영역/결산단위)을 등록하고 모델 매핑을 확인하는 프로그램(동일명 트랜잭션). |
| ZLPAC0020 | Define Activity Master. Activity Group 번호·명칭을 정의/확인하는 프로그램(동일명 트랜잭션). 모델링 전 준비 단계. |
| ZLPAC1050 | Maintain Special Role. 2·3 Level 모델링 수정 권한(Special Role)을 부여하는 프로그램(동일명 트랜잭션). |
| ZLPAC0140 | Display Modeling List. 모델링 결과를 레벨(1/2/3)별로 조회하는 프로그램(동일명 트랜잭션). 삭제 완료·최하위 모델링 확인에 사용. |
| Closing ID | 모델링 계층(Activity Group → Activity → Closing ID)의 최하위(최종) 레벨. Closing ID까지 모델링되어야 수행 가능. |
| Special Role (M / O) | ZLPAC1050에서 부여하는 모델링 수정 권한. M=Modeling-Std(표준 맵), O=Modeling-Org(조직 맵). (값은 운영 자료 기준, 현장확인) |
| Where Used List | 특정 Activity가 사용된 모든 모델링 목록. 전 법인 모델링 삭제 시 여기에 존재하는 모델링을 모두 삭제해야 함. |
| FI000 (삭제 에러) | 'It cannot be deleted because there is status history data.' 상태 이력 데이터가 존재하여 모델링을 삭제할 수 없을 때 표시되는 메시지. |
| Activities Not Exist | Node에 표시되는 메시지. Closing ID가 모델링되지 않은 경우 발생. (8.4 참조) |
| ZTPAC_STD_NODE | 표준 모델 노드 테이블. ZLPAC0140 조회의 기준 테이블 중 하나. |
| CWF | 운영 서버 모델링 변경 요청을 처리하는 담당(인원). 운영 서버는 CWF를 통해 요청 파일로 변경. |
| ZCL_PAC_NETGRAPH | 표준 설명 'Process Automatic Channel - Network'. 모든 모델링 프로그램이 공통으로 사용하는 네트워크 그래프 엔진 클래스. |
| ZCL_PAC_AUTH | PAC 권한 검사 클래스. CHECK_BUPAK_AUTH로 Business Package 관리 권한 확인. |
| ZCL_PAC_ORG | PAC 조직 처리 클래스. CHECK_VALID_ORG(조직 유효성), get_cunit_field_name(결산단위 라벨) 등 제공. |
| BUPAK / Business Package | 결산 업무 묶음의 최상위 식별자. 마스터: ZTPAC_BUPAK. |
| BUSTY / Business Type | 비즈니스 유형. 표준 맵 구분 키. 마스터: ZTPAC_BUSTY(BLEVEL 필드로 레벨 구분). |
| BLEVEL | Business Type의 레벨. 소스에서 A/C/B/K 값 사용 확인. 'C'는 글로벌 전환 조건. (전체 정의는 현장확인) |
| PCSGP / Activity Group | 액티비티 그룹. 모델을 그룹 단위로 구분. 값이 BUPAK와 같으면 최상위(1레벨)로 취급. |
| PACLVL (조직 레벨) | Business Package별 조직 기준 레벨. C=회사코드 / B=사업영역 / U=결산단위. ZTPAC_CONFIG에 저장. |
| REQ_BUKRS | 회사코드 필수 여부 플래그. 'X'이면 PACLVL이 B/U라도 회사코드 입력 필수. |
| GPID / Global Package ID | 여러 Business Package를 묶는 글로벌 패키지 식별자. 마스터: ZTPAC_GPID_MAST. |
| MAIN (대표 패키지) | 글로벌 패키지에 연결된 Business Package 중 대표 패키지 표시. ZTPAC_GPID-MAIN='X'. |
| BUKRS | 회사코드(Company Code). SAP 표준 필드. |
| GSBER | 사업영역(Business Area). SAP 표준 필드. CO 조직 등록 단위. |
| CUNIT | 결산단위(Closing Unit). PAC 필드. 화면 라벨은 패키지별로 다를 수 있음. |
| ZTPAC_CONFIG | PAC Global Config. Business Package별 PACLVL/REQ_BUKRS 등 설정 보관. |
| ZTPAC_CONFIG_COM/BA/UNI | 조직 등록 설정 테이블. 각각 회사코드/사업영역/결산단위 레벨 조직을 보관. |
| ZTPAC_ORG_NODE / ZTPAC_ORG_LINK | 조직 모델의 노드/링크(맵) 정보 테이블. ZLPAC0050 LINK 조회에 사용. |
| ENQUEUE / DEQUEUE | SAP 표준 잠금 설정/해제 함수. 모델링은 EZ_ZSPAC_LOCK, 조직 등록은 EZ_ZTPAC_CONFCOM 사용. |
| Web GUI 불가 | 모델링 화면은 ActiveX가 필요하여 Web GUI에서 실행 불가. SAP GUI 전용. |
| REPFLAG | 대표 조직 플래그. 조직 등록(ZLPAC0050)에서 사용. |
| SM12 | SAP 잠금 항목을 조회·관리하는 표준 트랜잭션. |
| ZTPAC_STD_LINK | 표준 모델의 노드 간 연결(링크) 테이블. 선행 노드(P_NODE) → 후행 노드(R_NODE). |
| ZTPAC_CLD_SNODE / ZTPAC_CLD_SLINK | 결산 확정(마감) 시점의 표준 모델 노드/링크 스냅샷. 결산월(CLMON) 단위로 보관. |
| ZTPAC_CLD_ONODE / ZTPAC_CLD_OLINK | 결산 확정(마감) 시점의 조직 모델 노드/링크 스냅샷. 결산월(CLMON) 단위로 보관. |
| CLMON | 결산 확정 스냅샷 테이블(ZTPAC_CLD_…)의 키인 결산월. 해당 월의 모델 상태를 구분. |
| LOEVM | 삭제 플래그. 모델링 테이블은 물리 삭제 대신 LOEVM = 'X' 로 논리 삭제 처리. |
| SCU3 | SAP 표준 테이블 변경 로그 조회 트랜잭션. PAC 모델링은 전용 이력 테이블이 없어 변경 이력을 SCU3로 확인. (9.4 참조) |
| P_NOPID | ZLPAC0140의 체크박스. 하위 Activity가 없는 노드만 조회. Level 1·2 선택 시에만 표시되며, 'Activities Not Exist' 노드 추적에 사용. |

## 자주 묻는 질문 (FAQ)

| 증상 / 질문 | 원인 및 조치 |
|---|---|
| 모델링했는데 ZLPAC0140에서 보이지 않음 | 최하위인 Closing ID까지 모델링되어 있는지 확인. (ZLPAC0140 기본 조회 레벨이 최하위이므로 Closing ID 미모델링 시 조회되지 않음) |
| Node에 'Activities Not Exist' 메시지가 나옴 | Closing ID가 모델링되지 않은 경우. 최종 레벨(Closing ID)을 Setup해야 함. (8.3 참조) |
| 모델링 삭제가 안 됨 (FI000) | 상태 이력 데이터가 존재하는 경우. 해당 Activity의 Where Used List에 있는 모든 모델링을 먼저 삭제. (8.2 참조) |
| 2·3 Level 모델링이 수정권한 없음 | ZLPAC1050에서 해당 권한(Standard=M / Organization=O)이 부여되어 있는지 확인. (7.2 참조) |
| CO에서 해당 법인 결산 마감 되었는데 Monitoring 화면에 COG004 Activity가 진행이 되지 않은 상태로 보임 | Company Level Map에는 없지만 BA에는 모델링이 되어 있어서 생긴 문제. BA 모델링 1레벨 삭제 필요. 이미 결산이 마감된 시점에는 ZTPAC_CLD_ONODE 테이블에 데이터 입력해줘야 함. (운영X) |
