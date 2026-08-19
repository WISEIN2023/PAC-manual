---
id: mailing/10-lxi-meilring-teukhwa-rojik-jeongri
doc: mailing
title: 10. LXI 메일링 특화 로직 정리
parent: docs/mailing/README.md
---

# 10. LXI 메일링 특화 로직 정리

PAC 메일링은 와이즈인(WS) 표준 서버와 LG전자(LXI) 서버가 별도로 운영되며, LXI에는 고객 특화(CSP) 로직이 반영되어 있습니다. 이 장은 WS ↔ LXI 차이와 LXI 전용 오브젝트를 정리한 것으로, 소스 이관·유지보수 전에 반드시 먼저 확인하세요.

> [ 주의 — WS→LXI 메일 발송 로직 이관 금지 ]<br>와이즈인(WS) 서버의 메일 발송 로직을 LXI 서버로 그대로 이관하면 안 됩니다. LXI에는 CSP(고객 특화) 로직이 반영되어 있어, WS 소스를 덮어쓰면 특화 로직이 유실됩니다.<br>특히 ZFPAC_SEND_*_MAIL 계열과 HTML 변환 CSP(ZFPAC_CSP_*_HTML)는 LXI 전용으로 분리되어 있으므로, 이관 시 반드시 대상 서버를 구분하세요.

## 10.1 WS ↔ LXI 차이 · 핵심 원칙

- **메일 발송 시점(공통):** Activity의 Status가 바뀔 때 / Alarm이 발송될 때 / 결산 일정이 배포될 때 메일이 발화됩니다.
- **완료(Complete) 수신 추가:** LXI 요청으로 Complete 상태에서도 메일을 수신하도록 추가되었습니다. 완료 메일 본문에는 해당 Activity의 참여자 리스트까지 포함됩니다. (3.1 참고)
- **에러 vs Rework 분리:** WS는 별도의 Rework 전용 펑션이 없어 에러 메일이 재작업 알림을 겸합니다. LXI는 에러 메일과 Rework 메일을 별도 펑션으로 구분했습니다(개발 본수 산정 목적).
- **본문·HTML 변환 분리:** 메일 본문 구성과 HTML 변환 로직을 CSP로 분리했습니다(개발 본수 산정 목적). 디자인·문구뿐 아니라 변환 로직 자체가 CSP 오브젝트로 나뉘어 있습니다.
- **SEND_MAIL_REWORK:** 와이즈인(WS) 서버에서는 미사용입니다. Rework 발송 체인(ZFPAC_CSP_SEND_REWORK_MAIL → SEND_MAIL_REWORK → ZFPAC_CSP_REWORK_HTML)은 LXI에만 존재합니다.

## 10.2 발송 흐름 (상태 변경 → 메일)

Activity 상태가 바뀌면 아래 순서로 상태별 메일링 발송 로직이 수행됩니다.

ZCL_PAC_LOG=>WRITE_LOG_DETAIL   (액티비티 상태 변경 기록)

│

▼

ZCL_PAC=>UPDATE_PAC_STATUS      (상태별 메일링 발송 로직 수행)

│

▼

ZFPAC_MAILING                   (IV_STATUS = F / W / M / C 분기)

│

▼

상태별 발송 펑션 → ZCL_PAC_MAIL=>SEND_MAIL_*  →  (LXI) ZFPAC_CSP_*_HTML

일정 배포·마감 알람은 상태 흐름과 별개로 ZCL_PAC_MAIL=>SEND_MAIL_DIST / SEND_MAIL_ALARM로 발송되며, 이 두 메서드 내부의 HTML 변환 로직도 LXI에서 CSP로 분리했습니다.

## 10.3 발송 펑션 ↔ 메서드 ↔ HTML 변환 CSP 매핑

ZFPAC_SEND_MAIL(단일 발송 출구)은 공통이며 변화가 없습니다. 상태·이벤트별 발송 펑션과 LXI에서 분리한 HTML 변환 CSP의 대응은 다음과 같습니다.

| 발송 펑션(진입) | 메서드 (ZCL_PAC_MAIL) | HTML 변환 CSP | 비고 |
|---|---|---|---|
| ZFPAC_SEND_ERROR_MAIL | SEND_MAIL_ERROR | ZFPAC_CSP_ERROR_HTML | 에러 메일 |
| ZFPAC_CSP_SEND_REWORK_MAIL | SEND_MAIL_REWORK | ZFPAC_CSP_REWORK_HTML | Rework 메일 — LXI 전용 |
| ZFPAC_SEND_MREADY_MAIL | SEND_MAIL_MREADY | (분리 미적용) | 수동준비. Todo+메일 발송(WS·LXI 공통 추가) |
| ZFPAC_SEND_COMPLETE_MAIL | SEND_MAIL_COMPLETE | ZFPAC_CSP_COMPLETE_MAIL | 완료 메일 |
| (알람 트리거) | SEND_MAIL_ALARM | ZFPAC_CSP_CLOSING_ALARM_HTML | 마감 알람 |
| (배포 트리거) | SEND_MAIL_DIST | ZFPAC_CSP_CLOSING_DIST_HTML | 결산 일정 배포 |
| ZFPAC_SEND_MAIL | (단일 발송 출구) | (공통 · 변화 없음) | 제목 구성 + 최종 발송 |

> [ 확인 필요 — MREADY HTML 분리 ]<br>위 매핑에서 수동준비(MREADY) 메일은 HTML 변환 로직이 분리되지 않은 것으로 표기되어 있으나, LXI 신규 오브젝트 목록(10.4)에는 ZFPAC_CSP_MREADY_HTML이 존재합니다. 실제 사용(연결) 여부는 운영 소스에서 확인이 필요합니다.

## 10.4 LXI 전용 신규 오브젝트 (CSP)

LXI에서 ZFPAC_SEND_*_MAIL 내부의 HTML 변환 로직 등을 별도로 분리하며 신규 생성한 오브젝트입니다. WS 이관 시 덮어쓰지 않도록 주의합니다.

- **ZFPAC_CSP_CLOSING_ALARM_HTML —** 마감 알람 메일 HTML 변환
- **ZFPAC_CSP_CLOSING_DIST_HTML —** 결산 일정 배포 메일 HTML 변환
- **ZFPAC_CSP_ERROR_HTML —** 에러 메일 HTML 변환
- **ZFPAC_CSP_MREADY_HTML —** 수동준비 메일 HTML 변환 (사용 여부 확인 필요 — 10.3 참고)
- **ZFPAC_CSP_REWORK_HTML —** Rework 메일 HTML 변환
- **ZFPAC_CSP_SEND_REWORK_MAIL —** Rework 메일 발송(진입) 펑션
