---
id: mailing/06-html-meil-yangsik-jakseong-wonri
doc: mailing
title: 6. HTML 메일 양식 작성 원리
parent: docs/mailing/README.md
---

# 6. HTML 메일 양식 작성 원리

HTML 양식은 '빈칸이 뚫린 서류'이고, SAP 발송 프로그램이 그 빈칸을 실제 값으로 채워 메일을 보냅니다. 이 원리를 알아야 양식을 올바르게 수정할 수 있습니다.

## 6.1 값이 채워지는 자리: $필드명$

본문에 $필드명$ 형식으로 적으면, 발송 메서드가 넘긴 데이터에서 같은 이름의 필드 값으로 자동 치환됩니다. 빈칸 이름을 마음대로 정하는 것이 아니라, 발송 메서드가 넘기는 필드명과 똑같이 적어야 채워집니다.

## 6.2 단건 vs 여러 건(loop)

- **단건(헤더):** 값이 하나뿐인 정보(예: 안내문구, 회사명). 발송 메서드의 IS_DATA로 전달되며, $필드명$이 한 번 채워집니다.
- **여러 건(목록):** 줄이 여러 개인 표(예: 스케줄 목록). 발송 메서드의 IT_DATA1~9로 전달되며, loop 마커로 감싼 블록이 데이터 줄 수만큼 반복됩니다.

## 6.3 실제 예시 — 알람 메일

알람 메일 발송 코드(ZCL_PAC_MAIL)는 단건 헤더와 여러 건 목록을 아래처럼 넘깁니다.

> * 단건(헤더) → IS_DATA : TIME_TEXT (예: '...will be closed in 1 hours')<br>* 여러 건(목록) → IT_DATA1 : SCHID / SCH_PLNDT / SCH_PLNTM (스케줄 줄마다)<br>CALL METHOD zcl_pac_func=>get_html<br>EXPORTING iv_htmlid = ... iv_htmlgrp = <알람그룹><br>is_data = ls_header " 단건<br>it_data1 = lt_loop. " 여러 건

이를 받는 HTML 양식은 다음처럼 작성합니다.

> <p>$TIME_TEXT$</p> <!-- 단건: 한 번 채워짐 --><br><table><br><!-- loop 시작 --> 줄 수만큼 아래 행이 반복<br><tr><td>$SCHID$</td><td>$SCH_PLNDT$</td><td>$SCH_PLNTM$</td></tr><br><!-- loop 종료 --><br></table>

즉 loop 안에서 쓸 수 있는 빈칸 이름(예: $SCHID$)은, 발송 메서드가 IT_DATA1에 담는 필드명과 같아야 합니다. '어떤 함수가 어떤 값을 담는가'가 곧 'HTML에서 쓸 수 있는 필드'입니다.

## 6.4 중요한 한계

> [ 주의 / 확인 필요 ]<br>HTML에 새로운 $NEWFIELD$ 를 적는다고 값이 저절로 생기지 않습니다. 그 필드를 발송 메서드(ABAP)가 IS_DATA/IT_DATA1에 담아 넘겨줄 때만 채워집니다.<br>기존에 없던 데이터를 메일에 새로 넣으려면 HTML만으로는 불가능하며, 발송 메서드(예: SEND_MAIL_ALARM) 수정이 필요합니다. 디자인/문구/표 모양 변경은 HTML만으로 가능합니다.

> [ 참고 ]<br>정확한 loop 마커 문자열(시작/종료 표시)은 타입그룹 ZPAC0에 정의되어 있어 외부 조회가 제한됩니다. ZLPAC_HTML에서 기존 알람/배포 양식을 열어 실제 마커를 그대로 복사해 사용하는 것이 가장 안전합니다.
