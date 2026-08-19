---
id: pac-config
title: PAC Config 운영자 매뉴얼
category: 기반설정
version: v1.0
updated: ""
source: PAC Config 운영자 매뉴얼.docx
programs: [ZIPAC_COMMON, ZIPAC_SYSSCREEN, ZLPAC0010, ZLPAC0010_F01, ZLPAC0011, ZLPAC0018, ZLPAC0018_F01, ZLPAC0019_F01, ZLPAC0020, ZLPAC0020_ALV, ZLPAC0020_F01, ZLPAC0020_F02, ZLPAC0021_F01, ZLPAC0031, ZLPAC0050, ZLPAC0050_F01, ZLPAC0080, ZLPAC0080_F01, ZLPAC0093, ZLPAC0110, ZLPAC0110_F01, ZLPAC0120, ZLPAC0140, ZLPAC0140_MAIN, ZLPAC0150, ZLPAC0170, ZLPAC0600, ZLPAC1000, ZLPAC1000_F01, ZLPAC1010, ZLPAC1010F01, ZLPAC1011_F01, ZLPAC1020F01, ZLPAC1030, ZLPAC5060, ZLPAC5060_F01, ZLPAC5080, ZLPAC5100, ZLPAC5100_F01, ZLPAC5110]
tables: [ZTPACSYS, ZTPAC_CLD_OLINK, ZTPAC_CLD_ONODE, ZTPAC_CLD_SLINK, ZTPAC_CLD_SNODE, ZTPAC_CONFIG, ZTPAC_CONFIG_COM, ZTPAC_GPID, ZTPAC_LOG_DTL, ZTPAC_PROC, ZTPAC_PROC_AUTH, ZTPAC_PROC_RCLOS, ZTPAC_SCH_CONFIG, ZTPAC_SPAUTH, ZTPAC_STATUS, ZTPAC_STATUS_IDV, ZTPAC_STD_NODE, ZTPAC_TODO]
functions: [ZFPAC, ZFPAC_AUTH_CHG_MASS, ZFPAC_AUTOTRIG_CROSS_BUPAK, ZFPAC_AUTOTRIG_LEGACY, ZFPAC_CHECK_JOB_BALANCING, ZFPAC_CHECK_PRENODE, ZFPAC_CHGNODE_REASON, ZFPAC_CHK_ASSIGN_AUTH, ZFPAC_CIS_DISPLAY_SNID, ZFPAC_CIS_SIMUL_RERUN, ZFPAC_CLOSE_TODO, ZFPAC_CONFIRM_ITEM, ZFPAC_CREATE_BUPAK_JOB, ZFPAC_CREATE_GPID_JOB, ZFPAC_CREATE_PCSGP_JOB, ZFPAC_CREATE_SCH_JOB, ZFPAC_DIS_TRIG_STATUS, ZFPAC_GET_BUTTONS, ZFPAC_GET_CAN_START, ZFPAC_GET_GLOBAL_NODE, ZFPAC_GET_GLOBAL_TREE, ZFPAC_GET_MAIL_RECEIVER, ZFPAC_GET_MREADY_PID, ZFPAC_GET_NODE_FIORI, ZFPAC_GET_PORTAL_LINK, ZFPAC_GET_PROPERTIES, ZFPAC_GET_REQBUKRS_NODE, ZFPAC_GET_VARIANT, ZFPAC_LINK_CONNECT_CHANGE, ZFPAC_MAILING, ZFPAC_NEXT_AUTO_START, ZFPAC_OPEN_TODO, ZFPAC_PID_AUTHLIST, ZFPAC_PID_DETAIL_SEARCH, ZFPAC_PORTAL_NOTICE_LIST, ZFPAC_REWORK_START, ZFPAC_SCHID_CLOSE, ZFPAC_SEND_CIS_CONT, ZFPAC_SEND_CIS_MAIL, ZFPAC_SEND_COMPLETE_MAIL]
summary: Business Package Config(ZTPAC_CONFIG)와 System Config(ZTPACSYS)의 전 설정키를 키별로 설명·참조 프로그램·영향도까지 정리한 설정 사전
---

# PAC Config 운영자 매뉴얼

> Business Package Config(ZTPAC_CONFIG)와 System Config(ZTPACSYS)의 전 설정키를 키별로 설명·참조 프로그램·영향도까지 정리한 설정 사전

Business Package Config (ZTPAC_CONFIG) · System Config (ZTPACSYS)

## 목차

1. [1. 개요](01-gaeyo.md)
2. **2. Business Package Config (ZTPAC_CONFIG)**
    - [2.1 Oranization Setting](02-01-oranization-setting.md)
    - [2.2 Authorization](02-02-authorization.md)
    - [2.3 Additional Activation](02-03-additional-activation.md)
    - [2.4 Posting](02-04-posting.md)
    - [2.5 Display Level](02-05-display-level.md)
    - [2.6 Confirm Type Level](02-06-confirm-type-level.md)
    - [2.7 Logging](02-07-logging.md)
    - [2.8 Rework](02-08-rework.md)
    - [2.9 Mailing](02-09-mailing.md)
    - [2.10 To Do](02-10-to-do.md)
    - [2.11 Variant&Param](02-11-variant-param.md)
    - [2.12 Fiori Setting](02-12-fiori-setting.md)
    - [2.13 Modeling](02-13-modeling.md)
    - [2.14 Controls](02-14-controls.md)
    - [2.15 Auto Exectution](02-15-auto-exectution.md)
3. **3. System Config (ZTPACSYS)**
    - [3.1 Data Editable Setting](03-01-data-editable-setting.md)
    - [3.2 Connection](03-02-connection.md)
    - [3.3 Map Control](03-03-map-control.md)
    - [3.4 Mailing](03-04-mailing.md)
    - [3.5 To Do](03-05-to-do.md)
    - [3.6 Front Connection](03-06-front-connection.md)
    - [3.7 Organization Setup](03-07-organization-setup.md)
    - [3.8 ALV Set-up](03-08-alv-set-up.md)
    - [3.9 Language](03-09-language.md)
    - [3.10 Logging](03-10-logging.md)
    - [3.11 Individual Control](03-11-individual-control.md)
    - [3.12 Auto Refresh](03-12-auto-refresh.md)
    - [3.13 User Output FIeld](03-13-user-output-field.md)
    - [3.14 Employee Master](03-14-employee-master.md)
    - [3.15 Alarm Control](03-15-alarm-control.md)
    - [3.16 Special Auth Check](03-16-special-auth-check.md)
    - [3.17 Notice Auth Check](03-17-notice-auth-check.md)
    - [3.18 Skip Auth Check Rule](03-18-skip-auth-check-rule.md)
    - [3.19 Job Grouping](03-19-job-grouping.md)
    - [3.20 Target Group](03-20-target-group.md)
    - [3.21 Minimum Allowance Rate](03-21-minimum-allowance-rate.md)
    - [3.22 World Map](03-22-world-map.md)
    - [3.23 Link](03-23-link.md)
    - [3.24 Calendar](03-24-calendar.md)
    - [3.25 Link Connect](03-25-link-connect.md)
