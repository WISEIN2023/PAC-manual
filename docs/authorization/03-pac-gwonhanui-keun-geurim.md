---
id: authorization/03-pac-gwonhanui-keun-geurim
doc: authorization
title: 2. PAC 권한의 큰 그림
parent: docs/authorization/README.md
---

# 2. PAC 권한의 큰 그림

PAC에서 사용자가 결산 작업(Activity)을 수행하려면 **서로 다른 3가지 권한 개념**을 모두 이해해야 합니다. 이 셋을 헷갈리지 않는 것이 권한 업무의 출발점입니다.

## 2.1 3대 핵심 개념

### ① PAC Role — "화면에 들어갈 수 있는가"

PAC 솔루션 사용을 위한 SAP 표준 권한입니다. Fiori Catalog(화면 접근 권한) + PAC Tcode 실행 권한으로 구성되며, PFCG Role 형태로 관리됩니다.

- **없으면 나타나는 증상:** Fiori 화면 접속 즉시 오류 발생
- **확인:** SU01에서 사용자가 보유한 Role 목록 확인

### ② Participant — "내가 이 법인/활동의 담당자인가"

PAC에 모델링된 각 Activity(활동)의 «담당자»를 지정하는 등록입니다. Business Package(BUPAK) · 조직 단위로 등록하며, 프로그램 ZLPAC1000에서 관리합니다.

- **없으면 나타나는 증상:** Closing Dashboard는 보이지만 법인 목록이 안 뜸 / Direct Link 미표시 / World Map 클릭 시 권한 오류

### ③ Special Auth(Special Role) — "Participant 없이도 수행 가능한 특수 권한"

Participant 등록 없이도 특정 Activity를 수행할 수 있도록 부여하는 특수 권한입니다. 프로그램 ZLPAC1050에서 등록·관리합니다.

**⚠️ 주의** Special Auth는 일반 사용자가 아닌 CWF 담당자·IT 인원 등 «관리 목적»으로만 부여합니다. 부여받으면 Participant 미등록 상태에서도 전체 법인의 모든 Activity에 접근되므로 신중하게 관리해야 합니다. CWF 담당자가 부여합니다.

## 2.2 Activity를 수행하려면 무엇이 필요한가

결산 Activity를 «실제로» 수행하려면 다음 조건이 동시에 충족되어야 합니다. **하나라도 빠지면 수행할 수 없습니다.**

1. **PAC Role** — Fiori 화면 접근 (필수)
2. **Participant 등록** — 해당 법인/조직의 담당자로 지정 (Special Auth 보유자는 예외)
3. **해당 Tcode의 SAP 실행 권한** — Activity에 연결된 Tcode를 실행할 수 있는 표준 권한
즉 «PAC Role + Participant»가 모두 완료되어야 수행 가능하며, 추가로 Activity에 걸린 Tcode 실행 권한도 별도로 있어야 합니다. 단 **Special Auth 보유자는 Participant 미등록 상태에서도 수행 가능**합니다.

## 2.3 증상별 1차 체크리스트 (가장 많이 쓰는 표)

| 사용자가 호소하는 증상 | 1차로 의심할 원인 | 확인 방법 |
|---|---|---|
| Fiori 접속하자마자 오류 | PAC Role(Fiori Catalog) 없음 | SU01 → Role 목록 |
| 대시보드는 보이는데 법인이 안 뜸 | Participant 미등록 | ZLPAC1000 등록 현황 |
| Direct Link에 Business Package가 안 보임 | Auth Group에 등록된 Role 미보유 | ZLPAC0010 / ZLPAC1030 |
| World Map에서 법인 클릭 시 권한 오류 | Participant 미등록 | ZLPAC1000 등록 현황 |
| 화면은 되는데 Activity 수행이 안 됨 | Tcode 실행 권한 부족 | SU53로 부족 Object 확인 |

**💡 핵심 한 줄** «접속 자체가 안 됨» = PAC Role 문제, «접속은 되는데 법인/활동이 안 보이거나 못함» = Participant 또는 Tcode 권한 문제.

## 2.4 권한 부여 흐름 — "화면 접근"과 "업무 수행"은 다르다

**📌 추가 메모** 이 절(2.4)과 다음 절(2.5)은 현업 사용자에게 PAC 권한 체계를 설명하기 위해 2026-07-03에 추가되었습니다.

SAP를 처음 접하는 현업 사용자가 가장 많이 혼동하는 지점이 «화면에 들어가는 것»과 «실제 결산업무(Activity)를 수행하는 것»을 같다고 여기는 것입니다. PAC에서 이 둘은 **서로 다른 단계**입니다.

먼저 **SAP PAC STD 권한(= PAC Role)**을 부여받아야 PAC 솔루션의 프로그램과 화면에 접근할 수 있습니다. 하지만 권한을 부여받은 사람이 곧바로 PAC의 결산 Activity를 수행할 수 있는 것은 **아닙니다.** 화면·프로그램에 «접근»만 가능한 상태입니다.

실제 Activity를 수행하려면, SAP PAC STD 권한을 부여받은 뒤 PAC 솔루션에서 해당 Activity의 «담당자»로 등록되어야 합니다. 이 Activity 담당자를 **Participant(참여자)**라고 부릅니다. 즉 **«권한 부여 → 참여자 등록»** 두 단계를 모두 거쳐야 비로소 업무 수행이 가능한 구조입니다.

**흐름화면 접근 → 업무 수행까지**

① SAP PAC STD 권한(PAC Role) 부여         |   → PAC 프로그램·화면 접근 가능 ② 아직 결산 Activity 수행은 불가         |   → PAC에서 Participant(참여자) 등록 필요 ③ 해당 조직/Activity의 참여자로 등록됨         | ④ 결산 Activity 수행 가능

| 단계 | 무엇이 결정되나 | 빠지면 나타나는 증상 |
|---|---|---|
| SAP PAC STD 권한(PAC Role) | PAC 프로그램·화면에 «접근»할 수 있는가 | 화면 접속 자체가 안 됨 |
| Participant(참여자) 등록 | 해당 조직/Activity를 «수행»할 수 있는가 | 화면은 열리나 법인·Activity 목록이 안 뜨거나 수행 불가 |

### Business Package 전체를 수행하려면 — Controller

만약 특정 **Business Package(결산 단위)**의 «모든 Activity»를 수행할 수 있는 담당자로 등록하고자 한다면 **Controller**로 등록하면 됩니다. 그렇게 일괄로 관리하지 않는다면, Activity 레벨별로 참여자를 개별 등록·관리해야 합니다.

- **Controller 등록:** 해당 Business Package의 법인별 모든 Activity를 수행할 수 있는 담당자가 됨 (실무 절차는 5.1 참고)
- **Activity 레벨 등록:** Activity별로 담당자를 나누어 등록·관리

### 예시 — 재무회계(FI) 결산을 수행하려면

1. 재무회계(FI) Business Package의 결산을 수행하려면 PAC 화면에 접속해야 한다.
2. PAC 화면에 접속하려면 SAP PAC Role을 부여받아야 한다.
3. Role을 부여받으면 화면 접근은 되지만, 각각의 Activity를 수행할 수 있는 것은 아니다.
4. 실제 Activity 수행을 위해서는 결산을 수행할 각 조직의 참여자(Participant)로 등록되어야 한다.

## 2.5 참여자 등록 주체와 권한 3단계 분리 (LG전자)

그렇다면 «누가» 참여자를 등록하는가? 참여자 등록·관리의 주체는 현업 사용자 중 **관리자 포지션**에 있는 사람으로 지정합니다. LG전자를 예로 들면 RAC(지역회계센터) 담당자들이 법인회계팀 일반 사용자들에게 특정 Activity별로 담당자를 지정하는 방식입니다.

일반 회계 담당자는 스스로 참여자를 등록하지 않고, 특정 업무를 수행해야 할 때 이 관리자에게 «등록을 요청»하는 구조입니다. 따라서 일반 사용자가 참여자 등록을 하지 못하도록 **SAP PAC STD Role을 분리해 별도로 관리**합니다.

이에 PAC에서는 권한을 다음 세 가지로 분리합니다.

| 권한 구분 | 주 대상 | 참여자(Participant) 등록 / 권한 범위 |
|---|---|---|
| PAC IT 권한 | IT 운영·관리 담당 | (운영·관리 목적) |
| PAC 회계팀 관리자용 권한 | 회계팀 관리자(예: 파트장) | ✔ 참여자 등록·관리 가능 (+ Activity Master·Modeling 수정) |
| PAC 일반사용자용 권한 | 일반 회계 담당자 | ✘ 불가 → 관리자에게 등록 요청 |
| 예외처리 필요 | 연결회계팀 담당자 | ✘ 참여자 미등록 → 전 법인 «조회» 권한만 부여 |

**📌 화면의 조직 리스트가 조회되는 기준** PAC의 여러 화면에서 조회되는 각 Business Package별 «조직 리스트»는 참여자 등록 기준에 따라 표시됩니다. 즉 참여자로 등록된 조직만 그 사용자의 화면에 나타납니다. 그리고 이 참여자는 «PAC 회계팀 관리자용 권한»을 가진 사람이 등록합니다.

**📌 LG전자 사례 — 전 법인 조회 권한** LG전자는 ZV_FCW_HQ_SUBSIDIARY 권한을 받으면 전체 법인을 조회할 수 있는 구조입니다. 그래서 연결회계팀 담당자는 ZV_FCW_CONSOLIDATION 권한에 추가로 ZV_FCW_HQ_SUBSIDIARY 권한을 받아 전 법인 모니터링도 가능하도록 했습니다.

**📌 연결회계팀 예외처리 (일반 원칙)** 연결회계팀 담당자는 일반적으로 특정 법인의 결산을 «수행»하는 것이 아니라 «전 법인의 결산 진행 현황»을 확인해야 합니다. 담당 조직만 등록하는 참여자(Participant) 구조와 달리, 요청 시 참여자 등록 없이 전 법인에 대한 «조회 권한»만 부여하는 예외처리가 필요합니다(수행 권한이 아닌 조회 전용). ※ LXI에 어떻게 적용했는지는 추가 메모 필요.

**💡 정리** ① 화면 접근 = SAP PAC STD 권한(PAC Role) → ② 업무 수행 = Participant 등록 → ③ 참여자 등록 주체 = PAC의 관리자 레벨로 설정한 권한 보유자. 일반 사용자는 관리자에게 등록을 요청한다.
