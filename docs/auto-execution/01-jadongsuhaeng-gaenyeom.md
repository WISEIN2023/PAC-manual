---
id: auto-execution/01-jadongsuhaeng-gaenyeom
doc: auto-execution
title: 1. 자동수행 개념
parent: docs/auto-execution/README.md
---

# 1. 자동수행 개념

**PAC 구성 (3레벨)**

PAC는 Activity Group > Activity Sub-Group > Activity 의 3레벨 계층으로 구성할 수 있다. 필요 시 여러 조직/업무를 묶는 Business Package(1레벨) 및 Global Package(GPID)가 최상위 레벨로 추가된다.

**모델링 = 노드 + 링크**

PAC 모델링은 작업 단위인 노드(Activity)와, 노드 사이의 선행-후행 연결고리인 링크(Link)로 구성된다.

**수행 순서 규칙**

자동수행은 모델링된 순서를 따른다. 어떤 노드의 선행 노드가 모두 완료되어야 그 후행 노드가 실행된다. 선행 노드가 4개면 4개가 모두 완료되어야 후행 노드가 수행되고, 후행 노드가 병렬로 여러 개면 실제 수행도 동시에 병행 처리된다.

**상위→하위배치잡생성 구조**

자동수행은 상위 레벨부터 차례로 수행되며 Group 단위의 배치잡(Batch Job)을 만드는 구조다. ① 링크 순서상 수행 가능한 Activity Group을 수행(Group 배치잡 생성) → ② 그 Group 내에서 수행 가능한 Activity Sub-Group의 Job 생성 → ③ Sub-Group 내에서 수행 가능한 Activity를 실행하는 프로그램 레벨 배치잡 생성.

**상태 Refresh 순환**

Group 단위로 생성된 배치잡이 하위의 상태 변화에 따라 '수행 가능한 노드'를 계속 다시 조회(Refresh)하고, 그 결과로 다음 Job을 생성한다. 이 순환을 통해 전체 결산 프로세스가 자동으로 진행된다.

**BTP(배치 프로세스) 관리 필요**

PAC 자동수행은 구조상 배치잡이 많이 생성될 수밖에 없다. 따라서 시스템의 배치 워크 프로세스(BTP) 여유 상황을 고려한 생성량 조절(Balancing)과 모니터링이 반드시 필요하다.
