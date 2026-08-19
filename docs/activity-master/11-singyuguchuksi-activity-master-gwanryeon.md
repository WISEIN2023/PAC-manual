---
id: activity-master/11-singyuguchuksi-activity-master-gwanryeon
doc: activity-master
title: 11. 신규구축시 Activity Master 관련 업무(LXI 예시)
parent: docs/activity-master/README.md
---

# 11. 신규구축시 Activity Master 관련 업무(LXI 예시)

1. Business Package 업무단위 별 수행할 Activity List 를 엑셀로 취합받는다
2. 취합받은 Activity + Tcode 리스트를 일괄 등록한다.
3. 추후 신규 프로그램에 대해서는 컨설턴트가 직접 Activity Master를 업데이트 하게 되며, PAC에서 수행시 세팅될 Paramter , Variant에 대한 세팅도 PAC에서 교육 후 직접 수행하게 된다.
4. 전반적인 셋업 관련 문의사항에 대해서 지원하고, 실제 PAC상에서의 테스트 중 Auto, Manual 수행시 호출방식 또는 필수 파라미터 셋업에 대해서 문의가 가장 빈번하다.
5. PAC 상에서의 수행이 정상적으로 이루어지는지 테스트할 때 PAC컨 입장에서 이야기할수 있는부분 -> 선후행 명확한 경우 linked activity 등록 가이드 -> 기표 발생 Acitviy 의 경우 PAC 로깅 메시지 처리시 전표번호가 담겨야 한다고 가이드(자동수행시 별도 스크린을 확인하는 것이 아니기때문에, 수행결과를 log에 남아있는 전표번호로 확인할수 있도록) . 전표번호를 log에 담아주게 되면, PAC에서 ALV를 통해서 해당 전표 리스트를 별도로 확인할수있게 프로그램 호출이 가능함.  ->법인별 Variant 를 다르게 사용할 경우에 대한 등록 방법 가이드 (ZLPAC0040 에서 개별로 매핑하는 방법과, Activity Master에서  Param 에서 법인별 variant를 적용하는 방법이 있음) ->Variant 가 개발과 동일하게 없는경우 호출시 오류발생할수 있음.
6. Activity Master 에 등록된 Tcode의 일괄변경 ZAA->ZAB 이런식으로  ->ZTPAC_PROC 에서 TCODE 변경-> ZTPAC_LOG_PARAM 의 PGM  필드도 수정해서 재등록 필요 -> ZTPAC_RELATIVE의 파라미터도 변경 필요 -> ZTPAC_REL_PARAM의 TCODE도 변경해서 다시 저장해야함. 이때 ZTPAC_RELATIVE와 RKEY 가 반드시 일치해야 정상적으로 적용된다.
7. 모델링 레벨의 변경 2레벨->3레벨 (참고, 내용복기필요함
- Zlpac0010에서 모델링 레벨 변경 불가하므로 ZTPAC_CONFIG 테이블에서 변경
- Ztpac_proc 테이블에서 Activity Group을 Activity Sub group으로 복사,
- Activity Sub group의 PCSGP는 Activity Group으로 등록.
- Activity 의PCSGP는 Activity Group이 아닌 신규생성한 Activity Sub group으로 변경하여 저장.
- 모델링에서는 ZTPAC_STD_NODE에서 Activity Sub Group 만 추가?
추가필요내용

Trigger 관련 셋업에 대한 자세한 내용은 Trigger 운영자 매뉴얼을참고한다.

Pac 수행시 parameter /variant 관련 펑션 메모 추가 필요
