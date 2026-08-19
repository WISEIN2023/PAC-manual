---
id: activity-master/07-yeongye-jakeop-sajeon-husok
doc: activity-master
title: 7. 연계 작업 (사전 · 후속)
parent: docs/activity-master/README.md
---

# 7. 연계 작업 (사전 · 후속)

## 7.1 사전 작업

1. **Trigger Code 정의 — ZLPAC0070:** Auto Trigger(X) 등록 전 사용할 Trigger Code를 먼저 정의. Trigger Source Type(Between Bus.Pkg / From Legacy / Between Org / From Other Module)과 Auto Next 등을 설정.
2. **Rework Rule ID 정의 — ZLPAC3000 / ZLPAC3010:** Rule ID 생성(Chart of Accounts·Description) 후 Rule Management에서 G/L 계정(From~To)·Company Code·Document Type 등 규칙 등록.
3. **Closing Category 동기화 — ZFCLR0010:** Closing Category 저장 시 계정정보를 I/F 받아 동일 Category명으로 Rework Rule ID 자동 생성. (LG운영서버에서 확인)

## 7.2 후속 작업 (Map 구성)

1. **Standard Map — ZLPAC0030:** Activity Master에 등록된 Sub-Group을 Node로 연결해 표준 Map 구성(Business Package·Activity Group·Business Type 조합).
2. **Organization Map — ZLPAC0040:** Standard Map을 기준으로 조직별 Map을 추가/변경. Organization Specific Activity·Back to Standard 지원.
