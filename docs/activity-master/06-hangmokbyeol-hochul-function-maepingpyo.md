---
id: activity-master/06-hangmokbyeol-hochul-function-maepingpyo
doc: activity-master
title: 6. 항목별 호출 Function 매핑표 (핵심 요약)
parent: docs/activity-master/README.md
---

# 6. 항목별 호출 Function 매핑표 (핵심 요약)

운영자가 ZLPAC0020에서 각 항목을 셋업할 때 실제로 호출되는 Function입니다. (모두 ZFPAC* 사용자정의 FM, 소스의 버튼 디스패치 로직으로 확인)

| 셋업 항목 | 화면 위치 / 버튼 | 호출 Function | 디스패치 Form |
|---|---|---|---|
| Business Package 조회 | 초기 화면 | ZFPAC_SET_BUPAK | GET_GS_100 |
| Detail Search | 초기 화면 버튼 | ZFPAC_PID_DETAIL_SEARCH | - |
| Closing Schedule 지정 | Schedule(SCH_ICON) | ZFPAC_CLOSING_ASSIGN | CALL_ZFPAC_CLOSING_ASSIGN |
| Linked Activity | Link(LINK_ICON) | ZFPAC_LINKED_PID_ASSIGN | CALL_ZFPAC_LINKED_PID_ASSIGN |
| 수행 주기(Period) | 기간(PER_ICON) | ZFPAC_PID_PERIOD | CALL_ZFPAC_PID_PERIOD |
| Activity Info/User Manual | Info(INFO_ICON) | ZFPAC_PID_INFO | CALL_ZFPAC_PID_INFO |
| Legacy URL/RFC (General) | URL(URL_ICON) | ZFPAC_SET_LEGACY_URL | CALL_SCREEN_LEGACY_URL |
| Legacy URL/RFC (Relative) | URL(URL_ICON, Rel.) | ZFPAC_SET_LEGACY_URL | CALL_SCREEN_LEGACY_URL5 |
| By Function (N) | By Function(BYFUNC_ICON) | ZFPAC_PID_BY_FUNCTION | CALL_ZFPAC_PID_BY_FUNCTION |
| Organization Skip | ORGSKIP_ICON | ZFPAC_SKIP_PID_ASSIGN | CALL_ZFPAC_SKIP_BY_FUNCTION |
| Trigger Define (X) | Trigger(CRS_ICON) | ZFPAC_SET_TRIGINFO | CALL_ZFPAC_SET_TRIGINFO |
| Rework Rule ID | Rework(REWORK_ICON) | ZFPAC_RULE_TO_ACTIVITY | CALL_ZFPAC_RULE_TO_ACTIVITY |
| Variant/Log Param (General) | Param(PARAM_ICON) | ZFPAC_REP_PARAM | CALL_ZFPAC_REP_PARAM |
| Relative Parameter | Param(PARAM_ICON, Rel.) | ZFPAC_REL_PARAM | CALL_ZFPAC_REL_PARAM |

> [ 안내 ]<br>표준 SAP 함수: VRM_SET_VALUES(드롭다운), DD_DOMVALUES_GET(도메인값), F4IF_INT_TABLE_VALUE_REQUEST(F4), LVC_FIELDCATALOG_MERGE(ALV), RS_VARIANT_EXISTS/CATALOG(Variant), ENQUEUE/DEQUEUE_EZ_ZTPAC_PROC(Lock).
