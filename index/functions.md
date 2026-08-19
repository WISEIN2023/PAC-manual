<!-- 이 파일은 docs/ 원본에서 자동 생성됩니다. 직접 수정하지 마세요. -->

# 함수 · 클래스 인덱스

`ZFPAC*` Function Module과 `ZCL_*` 클래스 역인덱스입니다.

## Function Module (106건)

| ID | 설명 | 상세 위치 |
|---|---|---|
| `ZFPAC` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) · [activity-master](../docs/activity-master/06-hangmokbyeol-hochul-function-maepingpyo.md#6-항목별-호출-function-매핑표-핵심-요약) |
| `ZFPACL_CHK_REWORK_FCV` |  | [rework](../docs/rework.md#23-activity-master에-rework-rule-지정-zlpac0020) |
| `ZFPAC_AUTH_CHG_MASS` |  | [pac-config](../docs/pac-config/03-13-user-output-field.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_AUTOTIRG_LEGACY` |  | [auto-trigger](../docs/auto-trigger/01-auto-trigger-gaeyo.md#12-auto-trigger와-일반-자동수행xauto의-차이) |
| `ZFPAC_AUTOTRIG` |  | [auto-trigger](../docs/auto-trigger/05-trigger-sudong-jaesilhaeng-reset-bangbeop.md#52-수동-재실행-절차) |
| `ZFPAC_AUTOTRIG_CHECK` | Legacy / Other Module에서 들어오는 Trigger의 사전 유효성 검증 전용 | [auto-trigger](../docs/auto-trigger/04-auto-trigger-dongjak-jogeon-mit-enjin-dongjak.md#43-후행이-일부-미완료-상태에서도-실행되는-이유) · [auto-trigger](../docs/auto-trigger/07-yongeojip-glossary.md#7-용어집-glossary) |
| `ZFPAC_AUTOTRIG_CROSS` |  | [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#41-자동수행-호출-트리-선행--후행) |
| `ZFPAC_AUTOTRIG_CROSS_BUPAK` | TRIG_TYPE = B (Between Business Package)인 경우 호출 | [pac-config](../docs/pac-config/02-15-auto-exectution.md#참조-프로그램--오브젝트-where-used) · [auto-execution](../docs/auto-execution/06-yeongye-hamsu-mesodeu-sangse-peuroseseu.md#6-연계-함수--메소드-상세-프로세스-관점) |
| `ZFPAC_AUTOTRIG_CROSS_ORG` | TRIG_TYPE = O (Between Organization)인 경우 호출 | [auto-trigger](../docs/auto-trigger/04-auto-trigger-dongjak-jogeon-mit-enjin-dongjak.md#43-후행이-일부-미완료-상태에서도-실행되는-이유) · [auto-trigger](../docs/auto-trigger/05-trigger-sudong-jaesilhaeng-reset-bangbeop.md#52-수동-재실행-절차) |
| `ZFPAC_AUTOTRIG_LEGACY` | Function Module | [pac-config](../docs/pac-config/02-09-mailing.md#참조-프로그램--오브젝트-where-used) · [auto-trigger](../docs/auto-trigger/02-gwanryeon-obeujekteu-seolmyeong.md#23-주요-function-module--클래스) |
| `ZFPAC_AUTOTRIG_OTHERS` | TRIG_TYPE = S (From Other Module)인 경우 호출 | [auto-trigger](../docs/auto-trigger/04-auto-trigger-dongjak-jogeon-mit-enjin-dongjak.md#43-후행이-일부-미완료-상태에서도-실행되는-이유) · [auto-trigger](../docs/auto-trigger/05-trigger-sudong-jaesilhaeng-reset-bangbeop.md#52-수동-재실행-절차) |
| `ZFPAC_CALL_APC` | 프로세스 변경에 따른 화면 Refresh | [apc](../docs/apc.md#21-pac에서-사용하는-3개의-apc) |
| `ZFPAC_CALL_APC_NOTICE` | 공지사항 저장 시 APC 메시지를 발송하는 PAC 함수. Function Group: ZPAC111 | [notice](../docs/notice.md#21-프로그램-개요) · [apc](../docs/apc.md#21-pac에서-사용하는-3개의-apc) |
| `ZFPAC_CALL_APC_TODO` | To Do에 대한 APC 발생 | [apc](../docs/apc.md#21-pac에서-사용하는-3개의-apc) |
| `ZFPAC_CHECK_JOB_BALANCING` | ← CREATE_BATCHJOB·GET_CAN_START·GLOBAL_GET_CAN_START | [pac-config](../docs/pac-config/03-20-target-group.md#참조-프로그램--오브젝트-where-used) · [pac-config](../docs/pac-config/03-21-minimum-allowance-rate.md#설정-설명) |
| `ZFPAC_CHECK_PRENODE` | ← CREATE_PCSGP_JOB | [pac-config](../docs/pac-config/02-15-auto-exectution.md#참조-프로그램--오브젝트-where-used) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#41-자동수행-호출-트리-선행--후행) |
| `ZFPAC_CHGNODE_REASON` |  | [pac-config](../docs/pac-config/02-13-modeling.md#프로세스-관점-분석-사용-로직) |
| `ZFPAC_CHK_ASSIGN_AUTH` |  | [pac-config](../docs/pac-config/02-06-confirm-type-level.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_CIS_DISPLAY_SNID` |  | [pac-config](../docs/pac-config/02-10-to-do.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_CIS_RERUN_CONDITION` |  | [schedule-job](../docs/schedule-job.md#72-실제-activity-수행에-사용되는-function) |
| `ZFPAC_CIS_SIMUL_RERUN` |  | [pac-config](../docs/pac-config/03-19-job-grouping.md#참조-프로그램--오브젝트-where-used) · [schedule-job](../docs/schedule-job.md#72-실제-activity-수행에-사용되는-function) |
| `ZFPAC_CLOSE_TODO` | To-Do 종료(Close) 함수. 함수 그룹 ZPAC260. CWF·Signal Close 동시 호출 | [todo](../docs/todo/05-miwanryo-to-do-cheori-bangbeop.md#51-zfpac_close_todo-pac-측-종료) · [pac-config](../docs/pac-config/03-05-to-do.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_CLOSING_ASSIGN` | Assign Schedule ID to Activity ID | [activity-master](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) · [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) |
| `ZFPAC_CLOSING_SCHID` |  | [auto-execution](../docs/auto-execution/06-yeongye-hamsu-mesodeu-sangse-peuroseseu.md#6-연계-함수--메소드-상세-프로세스-관점) |
| `ZFPAC_CONFIRM_ITEM` | 수기 확정. 확정 후 AFTER_CONF 충족 시 ZFPAC_NEXT_AUTO_START로 후행 자동수행 | [pac-config](../docs/pac-config/02-01-oranization-setting.md#프로세스-관점-분석-사용-로직) · [pac-config](../docs/pac-config/02-06-confirm-type-level.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_CREATE_ALARM_BATCH` | Create Alarm Batch | [authorization](../docs/authorization/10-lgjeonja-teukhwa-jeongri.md#97-결산-cwf-보유-권한-점검-메일링) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#35-마감-알람alarm-메일) |
| `ZFPAC_CREATE_BATCHJOB` | 모든 레벨(GPID/BUPAK/PCSGP/PID)의 Job 생성 공통 함수. JOB_OPEN/SUBMIT/JOB_CLOSE와 밸런싱·중복방지 포 | [authorization](../docs/authorization/08-03-posting-user-gipyoyujeo-vs-execute-user.md#733-기표유저psnam는-어떤-규칙으로-정해지나--직접-찾는-법) · [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-6-sail_process_id--핵심) |
| `ZFPAC_CREATE_BUPAK_JOB` | ← EXECUTE_ACTION(PCSGP_START) / → ZFPAC_CREATE_BATCHJOB | [pac-config](../docs/pac-config/02-03-additional-activation.md#참조-프로그램--오브젝트-where-used) · [pac-config](../docs/pac-config/02-15-auto-exectution.md#프로세스-관점-분석-사용-로직) |
| `ZFPAC_CREATE_GPID` |  | [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#42-동일-진입점execute_action의-형제-오퍼레이션) |
| `ZFPAC_CREATE_GPID_JOB` | ← EXECUTE_ACTION(PCSGP_START) / → ZFPAC_CREATE_BATCHJOB | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) · [pac-config](../docs/pac-config/02-15-auto-exectution.md#프로세스-관점-분석-사용-로직) |
| `ZFPAC_CREATE_PCSGP_JOB` | ← EXECUTE_ACTION, SAIL_GLOBAL_PROCESS, CREATE_PROCESS_GROUP_JOB / → SAIL_PROCESS | [pac-config](../docs/pac-config/02-03-additional-activation.md#참조-프로그램--오브젝트-where-used) · [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-2-zgwpac_main--action-import--pcsgp_start) |
| `ZFPAC_CREATE_PID_JOB` | 실행유저(EXNAM) 결정 | [authorization](../docs/authorization/08-03-posting-user-gipyoyujeo-vs-execute-user.md#73-posting-user기표유저-vs-execute-user실행유저) · [authorization](../docs/authorization/11-teureobeulsyuting-jeungsang-wonin-jochi.md#104-업무별-디버깅-진입점-빠른-참조) |
| `ZFPAC_CREATE_SCH_JOB` |  | [pac-config](../docs/pac-config/02-04-posting.md#참조-프로그램--오브젝트-where-used) · [schedule-job](../docs/schedule-job.md#72-실제-activity-수행에-사용되는-function) |
| `ZFPAC_CSP` |  | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#10-lxi-메일링-특화-로직-정리) |
| `ZFPAC_CSP_AC_IF` |  | [activity-master](../docs/activity-master/05-04-step-3-rework-rule-id-deungrok-jaejakeop.md#54-step-3--rework-rule-id-등록-재작업-감지) · [activity-master](../docs/activity-master/08-teureobeulsyuting-dibeoging-gaideu.md#83-운영-사례--zfclr0010--ac-category-동기화-덤프) |
| `ZFPAC_CSP_CHECK_BUKRS_AUTH` |  | [authorization](../docs/authorization/10-lgjeonja-teukhwa-jeongri.md#911-고객사-특화-권한-체크-로직-화면) · [authorization](../docs/authorization/13-peuroseseu-gaeyo-participant-process-overview.md#고객사-특화-lge) |
| `ZFPAC_CSP_CLOSING_ALARM_HTML` | (알람 트리거) | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#103-발송-펑션--메서드--html-변환-csp-매핑) |
| `ZFPAC_CSP_CLOSING_DIST_HTML` | (배포 트리거) | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#103-발송-펑션--메서드--html-변환-csp-매핑) |
| `ZFPAC_CSP_COMPLETE_MAIL` | 완료 메일 | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#103-발송-펑션--메서드--html-변환-csp-매핑) |
| `ZFPAC_CSP_ERROR_HTML` | 에러 메일 | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#103-발송-펑션--메서드--html-변환-csp-매핑) |
| `ZFPAC_CSP_LEG_SCHIF` |  | [closing-schedule](../docs/closing-schedule/02-define-schedule-id-zlpac7010.md#271-active-legacy-if--schedule-인터페이스-lg-특화) · [closing-schedule](../docs/closing-schedule/09-yongeojip-glossary.md#9-용어집-glossary) |
| `ZFPAC_CSP_LEG_SCHIF_EPS` |  | [closing-schedule](../docs/closing-schedule/02-define-schedule-id-zlpac7010.md#271-active-legacy-if--schedule-인터페이스-lg-특화) |
| `ZFPAC_CSP_MREADY_HTML` |  | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#104-lxi-전용-신규-오브젝트-csp) |
| `ZFPAC_CSP_REWORK_HTML` | Rework 메일 — LXI 전용 | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#101-ws--lxi-차이--핵심-원칙) |
| `ZFPAC_CSP_SEND_REWORK_MAIL` | Rework 메일 — LXI 전용 | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#101-ws--lxi-차이--핵심-원칙) |
| `ZFPAC_DISPLAY_POST_DOC` | 전기 문서 내역 화면 표시 | [log-management](../docs/log-management/06-gwanryeon-johoe-hamsu.md#61-함수-목록) |
| `ZFPAC_DIS_TRIG_STATUS` |  | [pac-config](../docs/pac-config/03-13-user-output-field.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_EMP_INFO_SH_EXIT` | [PAC] Employee Info Search help Exit (그룹 ZPAC241) | [authorization](../docs/authorization/08-05-sawonmaseuteo-insamaseuteo-yeongyewa-exit.md#752-활용범위--어디서-이-정보를-쓰나) · [authorization](../docs/authorization/14-burok-peurogeuraem-teibeul-keulraeseu-sap.md#123-클래스--함수--odata) |
| `ZFPAC_GET_BUTTONS` |  | [pac-config](../docs/pac-config/02-05-display-level.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_CAN_START` | ← Fiori 조회, SAIL_GLOBAL_PROCESS / → CHECK_CAN_RUN | [pac-config](../docs/pac-config/02-08-rework.md#설정-설명) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#41-자동수행-호출-트리-선행--후행) |
| `ZFPAC_GET_GLOBAL_NODE` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_GLOBAL_TREE` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_MAIL_RECEIVER` | Closing Schedule Distribution Mail | [pac-config](../docs/pac-config/03-13-user-output-field.md#참조-프로그램--오브젝트-where-used) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#34-배포distribution-메일) |
| `ZFPAC_GET_MREADY_PID` | Manual Ready 대상 감지 함수(함수 그룹 ZPAC280) | [pac-config](../docs/pac-config/02-06-confirm-type-level.md#참조-프로그램--오브젝트-where-used) · [todo](../docs/todo/02-yuhyeongbyeol-to-do-peuroseseu.md#22-결산-일정-배포-시-감지-배치-생성) |
| `ZFPAC_GET_NODE_FIORI` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#프로세스-관점-분석-사용-로직) · [pac-config](../docs/pac-config/02-05-display-level.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_PORTAL_LINK` |  | [pac-config](../docs/pac-config/02-12-fiori-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_PROPERTIES` |  | [pac-config](../docs/pac-config/02-05-display-level.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_REQBUKRS_NODE` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GET_RUNNING_JOB` | ← CREATE_BUPAK/PCSGP_JOB, SAIL_PROCESS_GROUP | [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-3-b-zfpac_create_bupak_job-business-package--1레벨) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#41-자동수행-호출-트리-선행--후행) |
| `ZFPAC_GET_VARIANT` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_GLOBAL_GET_CAN_START` | ← CREATE_GPID_JOB, GET_CAN_START / → SELECT_NODE_EXECUTABLE | [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-3-a-zfpac_create_gpid_job-global-package-레벨) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#41-자동수행-호출-트리-선행--후행) |
| `ZFPAC_GOS_DELETE` |  | [activity-master](../docs/activity-master/05-01-step-1-activity-group-sub-group-jeongui.md#51-step-1--activity-group--sub-group-정의-general-탭) |
| `ZFPAC_JOB_SCH_DETAIL` |  | [schedule-job](../docs/schedule-job.md#21-신규-배치잡-생성) |
| `ZFPAC_JOB_SCH_ORG_DETAIL` |  | [schedule-job](../docs/schedule-job.md#21-신규-배치잡-생성) |
| `ZFPAC_LEGACY_LINK` | Function (ZPAC270) | [fiori-sapgui-call](../docs/fiori-sapgui-call/04-hochul-yuhyeongbyeol-sangse-dongjak.md#47-레거시-url-연계--call_url) · [fiori-sapgui-call](../docs/fiori-sapgui-call/06-unyeong-yujibosu-jeomgeom-gaideu.md#62-증상별-점검-가이드) |
| `ZFPAC_LINKED_PID_ASSIGN` | Assign Linked Acitivty ID | [activity-master](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) · [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) |
| `ZFPAC_LINK_CONNECT_CHANGE` | Link 연결 변경 | [pac-config](../docs/pac-config/03-25-link-connect.md#참조-프로그램--오브젝트-where-used) · [fiori-action](../docs/fiori-action.md#12-action-목록) |
| `ZFPAC_LOG_DISPLAY` | Display Activity Log | [log-management](../docs/log-management/06-gwanryeon-johoe-hamsu.md#61-함수-목록) · [monitoring](../docs/monitoring/02-gongtong-giban-yoso-jinhaenghyeonhwang.md#24-건수-더블클릭--로그-연계) |
| `ZFPAC_LOG_PARAM_INIT` | Get Common Parameter Initial Value — 공통 파라미터 초기값을 조회한다 | [log-management](../docs/log-management/06-gwanryeon-johoe-hamsu.md#61-함수-목록) |
| `ZFPAC_LOG_POSTDOC` | 전기 완료 전표 목록 반환 | [log-management](../docs/log-management/06-gwanryeon-johoe-hamsu.md#61-함수-목록) |
| `ZFPAC_MAILING` | PAC - Mailling Process | [pac-config](../docs/pac-config/02-09-mailing.md#프로세스-관점-분석-사용-로직) · [mailing](../docs/mailing/04-juyo-teuraenjaeksyeon-peurogeuraem-hamsu.md#42-핵심-함수function-module) |
| `ZFPAC_NEXT_AUTO_START` | ZPAC05x | [pac-config](../docs/pac-config/02-01-oranization-setting.md#프로세스-관점-분석-사용-로직) · [pac-config](../docs/pac-config/02-15-auto-exectution.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_OPEN_TODO` | To-Do 발생(Open) 함수. 함수 그룹 ZPAC260. TDTYPE별 분기 | [pac-config](../docs/pac-config/02-10-to-do.md#참조-프로그램--오브젝트-where-used) · [pac-config](../docs/pac-config/03-15-alarm-control.md#프로세스-관점-분석-사용-로직) |
| `ZFPAC_ORG_AUTH` | ZPAC04x | [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-2-zgwpac_main--action-import--pcsgp_start) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#42-동일-진입점execute_action의-형제-오퍼레이션) |
| `ZFPAC_PAC_MONITOR` | 조직·액티비티별 상태 건수를 집계해 돌려주는 공통 함수(진행현황 계열의 데이터 소스) | [monitoring](../docs/monitoring/02-gongtong-giban-yoso-jinhaenghyeonhwang.md#21-데이터-소스--함수-zfpac_pac_monitor) · [monitoring](../docs/monitoring/03-aektibitibyeol-moniteoring-zlpac-monitor-act.md#32-처리-흐름) |
| `ZFPAC_PID_AUTHLIST` |  | [pac-config](../docs/pac-config/03-13-user-output-field.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_PID_BY_FUNCTION` | Define Execution Function by Pid | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--by-function-n) |
| `ZFPAC_PID_DETAIL_SEARCH` | Detail Search by Pid | [pac-config](../docs/pac-config/02-06-confirm-type-level.md#참조-프로그램--오브젝트-where-used) · [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) |
| `ZFPAC_PID_INFO` | Activity Info. Management | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-01-step-1-activity-group-sub-group-jeongui.md#51-step-1--activity-group--sub-group-정의-general-탭) |
| `ZFPAC_PID_PERIOD` | Assign Activity Period | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--transaction-t) |
| `ZFPAC_PORTAL_NOTICE_LIST` |  | [pac-config](../docs/pac-config/03-17-notice-auth-check.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_REL_PARAM` | Assign Relative Parameter | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-06-step-5-relative-yeongwan-peurogeuraem.md#56-step-5--relative연관-프로그램-등록-relative-탭) |
| `ZFPAC_REP_PARAM` | Assign Common Parameter | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--transaction-t) |
| `ZFPAC_RESET_FROM_HERE` | Reset From Here 메뉴 | [fiori-action](../docs/fiori-action.md#12-action-목록) |
| `ZFPAC_RESET_ITEM` | Reset 메뉴 | [fiori-action](../docs/fiori-action.md#12-action-목록) |
| `ZFPAC_RESET_LINKED` | Link된 Activity Reset | [fiori-action](../docs/fiori-action.md#12-action-목록) |
| `ZFPAC_REWORK_START` |  | [pac-config](../docs/pac-config/02-08-rework.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_RULE_TO_ACTIVITY` | Assign Re-work Rule ID to Activity | [activity-master](../docs/activity-master/01-munseo-gaeyo.md#11-자주-묻는-질문faq--빠른-찾기) · [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) |
| `ZFPAC_SCHID_CLOSE` |  | [pac-config](../docs/pac-config/02-08-rework.md#참조-프로그램--오브젝트-where-used) |
| `ZFPAC_SEND` |  | [mailing](../docs/mailing/10-lxi-meilring-teukhwa-rojik-jeongri.md#10-lxi-메일링-특화-로직-정리) |
| `ZFPAC_SEND_CIS_CONT` | 발송 함수 | [pac-config](../docs/pac-config/02-09-mailing.md#참조-프로그램--오브젝트-where-used) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#36-결산점검cis-메일--컨트롤러--리뷰어) |
| `ZFPAC_SEND_CIS_MAIL` | 발송 함수 | [pac-config](../docs/pac-config/02-09-mailing.md#참조-프로그램--오브젝트-where-used) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#36-결산점검cis-메일--컨트롤러--리뷰어) |
| `ZFPAC_SEND_COMPLETE_MAIL` | Activity Complete Mailing | [pac-config](../docs/pac-config/03-15-alarm-control.md#프로세스-관점-분석-사용-로직) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#31-완료complete-메일) |
| `ZFPAC_SEND_ERROR` |  | [pac-config](../docs/pac-config/02-09-mailing.md#참조-프로그램--오브젝트-where-used) · [mailing](../docs/mailing/14-burok-d-mcp-geomjeung-girok.md#부록-d-mcp-검증-기록) |
| `ZFPAC_SEND_ERROR_MAIL` | Activity Error Mailing | [pac-config](../docs/pac-config/03-15-alarm-control.md#프로세스-관점-분석-사용-로직) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#32-에러error-메일--재작업rework-메일) |
| `ZFPAC_SEND_MAIL` | Send Mail | [mailing](../docs/mailing/02-pac-meilring-gaenyeom-japgi.md#23-메일-전체-동작-흐름) · [mailing](../docs/mailing/04-juyo-teuraenjaeksyeon-peurogeuraem-hamsu.md#42-핵심-함수function-module) |
| `ZFPAC_SEND_MREADY_MAIL` | Activity Error Mailing(라벨) | [pac-config](../docs/pac-config/03-15-alarm-control.md#프로세스-관점-분석-사용-로직) · [mailing](../docs/mailing/03-meil-jongryubyeol-sangse.md#33-manual-ready-메일) |
| `ZFPAC_SET_BUPAK` | Business Package 조회 | [activity-master](../docs/activity-master/04-hwamyeon-guseong-mit-jinip.md#41-초기-조회-조건-selection-screen) · [activity-master](../docs/activity-master/06-hangmokbyeol-hochul-function-maepingpyo.md#6-항목별-호출-function-매핑표-핵심-요약) |
| `ZFPAC_SET_LEGACY_URL` | Set Legacy URL | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--legacy-url-t--x--l) |
| `ZFPAC_SET_TRIGINFO` | Set Trigger Information | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--auto-trigger-x) |
| `ZFPAC_SKIP_PID_ASSIGN` | Assign Organization Skip By Pid | [activity-master](../docs/activity-master/03-gwanryeon-teuraenjaeksyeon-hamsu-teibeul.md#32-항목-셋업-시-호출되는-핵심-함수--검증) · [activity-master](../docs/activity-master/05-02-step-2-activity-jeongui-activity-type-call.md#activity-type--by-function-n) |
| `ZFPAC_STD_AUTH` |  | [authorization](../docs/authorization/14-burok-peurogeuraem-teibeul-keulraeseu-sap.md#내부-호출관계-요약-소스-확정) |
| `ZFPAC_STOP_PCSGP_JOB` | 실행 중인 그룹 배치잡을 중단 | [auto-execution](../docs/auto-execution/03-suhaeng-dangyebyeol-sangse-peuroseseu.md#단계-2-zgwpac_main--action-import--pcsgp_start) · [auto-execution](../docs/auto-execution/04-peurogeuraem-hochulgwangye-seonhuhaeng.md#42-동일-진입점execute_action의-형제-오퍼레이션) |
| `ZFPAC_TZONE_CONVERT` |  | [log-management](../docs/log-management/06-gwanryeon-johoe-hamsu.md#62-zfpac_log_display--display-activity-log) |
| `ZFPAC_USER_AUTH` | 기표유저(PSNAM) 결정 | [pac-config](../docs/pac-config/02-04-posting.md#참조-프로그램--오브젝트-where-used) · [authorization](../docs/authorization/08-03-posting-user-gipyoyujeo-vs-execute-user.md#733-기표유저psnam는-어떤-규칙으로-정해지나--직접-찾는-법) |
| `ZFPAC_USRID_INFO_SH_EXIT` | [PAC] Employee Info Search help Exit (그룹 ZPAC241) | [authorization](../docs/authorization/08-05-sawonmaseuteo-insamaseuteo-yeongyewa-exit.md#752-활용범위--어디서-이-정보를-쓰나) · [authorization](../docs/authorization/14-burok-peurogeuraem-teibeul-keulraeseu-sap.md#123-클래스--함수--odata) |

## 클래스 (16건)

| ID | 설명 | 상세 위치 |
|---|---|---|
| `ZCL_APC_WSP_EXT_ZPAC` |  | [apc](../docs/apc.md#3-apc--amc-생성-및-환경-구성) |
| `ZCL_PAC` | Process Automatic Channel Main | [pac-config](../docs/pac-config/01-gaeyo.md#13-분석-근거) · [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZCL_PAC_AUTH` | 각 프로그램 공통 권한 체크(CHECK_ORG_AUTH / CHECK_AUTH_HQ / CHECK_SPECIAL_AUTH / CHECK_AUTH | [pac-config](../docs/pac-config/02-02-authorization.md#프로세스-관점-분석-사용-로직) · [pac-config](../docs/pac-config/02-07-logging.md#설정-설명) |
| `ZCL_PAC_CIS` |  | [fiori-action](../docs/fiori-action.md#23-조직권한-체크-zfpac_org_auth) |
| `ZCL_PAC_CLOSING` | ← 모든 CREATE_*_JOB, CONFIRM_ITEM, AUTOTRIG | [pac-config](../docs/pac-config/02-14-controls.md#참조-프로그램--오브젝트-where-used) · [authorization](../docs/authorization/11-teureobeulsyuting-jeungsang-wonin-jochi.md#104-업무별-디버깅-진입점-빠른-참조) |
| `ZCL_PAC_FIORI` |  | [monitoring](../docs/monitoring/09-gwanrijayong-sangtae-gwanri-zlpacstatusm.md#93-스케줄-관리-모드-schedule-plan) · [monitoring](../docs/monitoring/12-yongeojip-glossary.md#122-프로그램--함수--클래스) |
| `ZCL_PAC_FUNC` |  | [pac-config](../docs/pac-config/02-12-fiori-setting.md#프로세스-관점-분석-사용-로직) · [pac-config](../docs/pac-config/02-14-controls.md#참조-프로그램--오브젝트-where-used) |
| `ZCL_PAC_LOG` |  | [log-management](../docs/log-management/04-log-cheori-gujo-zcl-pac-log.md#4-log-처리-구조-zcl_pac_log) · [pac-config](../docs/pac-config/02-04-posting.md#참조-프로그램--오브젝트-where-used) |
| `ZCL_PAC_MAIL` | 메일 엔진 — 수신자 구성·제목·HTML 본문·발송·로그 (SEND_MAIL_xxx 9종) | [pac-config](../docs/pac-config/02-09-mailing.md#참조-프로그램--오브젝트-where-used) · [mailing](../docs/mailing/02-pac-meilring-gaenyeom-japgi.md#23-메일-전체-동작-흐름) |
| `ZCL_PAC_MTM` |  | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) |
| `ZCL_PAC_NETGRAPH` | 표준 설명 'Process Automatic Channel - Network'. 모든 모델링 프로그램이 공통으로 사용하는 네트워크 그래프 엔진  | [pac-config](../docs/pac-config/02-13-modeling.md#참조-프로그램--오브젝트-where-used) · [modeling](../docs/modeling/01-modelring-gibon-gaenyeom.md#12모델링-방법) |
| `ZCL_PAC_ORG` | PAC 조직 처리 클래스. CHECK_VALID_ORG(조직 유효성), get_cunit_field_name(결산단위 라벨) 등 제공 | [pac-config](../docs/pac-config/02-01-oranization-setting.md#참조-프로그램--오브젝트-where-used) · [authorization](../docs/authorization/08-05-sawonmaseuteo-insamaseuteo-yeongyewa-exit.md#75-사원마스터인사마스터-연계와-exit-on_get_userinfo--화면의-사용자-정보는-어디서-오나) |
| `ZCL_PAC_SAIL` | 자동수행 핵심 엔진. 선행완료→후행실행, 병렬·대기·재시도, 노드 유형별 처리 전반 → 변경 시 수행 순서·안정성 전반 영향 | [pac-config](../docs/pac-config/02-03-additional-activation.md#참조-프로그램--오브젝트-where-used) · [authorization](../docs/authorization/08-03-posting-user-gipyoyujeo-vs-execute-user.md#733-기표유저psnam는-어떤-규칙으로-정해지나--직접-찾는-법) |
| `ZCL_PAC_TODO` | To-Do 생성/종료/수신자 결정 | [mailing](../docs/mailing/04-juyo-teuraenjaeksyeon-peurogeuraem-hamsu.md#43-핵심-클래스class) |
| `ZCL_ZGWPAC_MAIN_DPC_EXT` | Fiori 참여자 OData 처리(목록 조회·상태) | [pac-config](../docs/pac-config/02-12-fiori-setting.md#참조-프로그램--오브젝트-where-used) · [authorization](../docs/authorization/09-gwanryeon-odata-chamgo.md#8-관련-odata-참고) |
| `ZCL_ZGWPAC_MONITOR_DPC_EXT` |  | [pac-config](../docs/pac-config/03-07-organization-setup.md#참조-프로그램--오브젝트-where-used) |
