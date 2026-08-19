---
id: mailing/12-burok-b-yongeojip-glossary
doc: mailing
title: 부록 B. 용어집 (Glossary)
parent: docs/mailing/README.md
---

# 부록 B. 용어집 (Glossary)

| 용어 | 설명 |
|---|---|
| PAC | Process Automatic Channel. SAP 결산 작업을 자동 실행하는 결산자동화 솔루션. |
| Activity(액티비티) | PAC에서 결산 작업의 한 단위. 자동 실행되며 상태(준비/실행/완료/오류 등)가 변함. |
| PID | Activity(또는 처리 단위)를 식별하는 ID. 수신자/메일 설정의 기준 키 중 하나. |
| BUPAK | Business Package. PAC 설정의 최상위 묶음 단위. |
| BUKRS / GSBER / CUNIT | 회사코드 / 사업영역 / 결산단위(조직 키). |
| PACLVL (C/B/U) | 조직 레벨. C=법인(Company), B=사업영역(Business Area), U=기타조직. 제목·본문·템플릿이 이 레벨에 따라 분기. |
| 상태 코드 F/W/M/C | Activity 상태. F=실패, W=경고(재작업), M=수동준비(Manual Ready), C=완료. |
| Rework(재작업) | 자동 처리가 실패해 사람이 다시 작업해야 하는 상황. 전용 메일이 없고 에러(F/W) 메일이 이를 알림. |
| Manual Ready(수동준비) | 자동이 아니라 사람이 수동으로 처리하도록 준비된 단계. |
| CIS | Closing Inspection(결산점검). 결산 데이터의 재무 리스크를 시나리오로 검증. 제목 'Financial Risk Validation'. |
| SNID / CID | CIS의 점검 시나리오 ID / 점검 카테고리 ID. |
| To-Do(할 일) | PAC 전용 테이블에 기록되고 포털에 실시간 표시되는 알림 채널. |
| APC | ABAP Push Channel. WebSocket 기반으로 To-Do를 포털 화면에 실시간 푸시. |
| Signal(메신저) | PAC 외부의 알림 플랫폼. 엘지(LXI)에서는 To-Do 알림을 Signal To-Do와 인터페이스해 함께 수신함. (PAC 자체 메신저 발송 기능은 미구현) |
| BCS | Business Communication Services. SAP 표준 메일 발송 프레임워크. |
| SAPconnect / RSCONN01 | SAP의 외부 통신(메일) 게이트웨이 / 발송 큐를 처리하는 표준 프로그램. |
| SOST | SAPconnect 발송 큐 모니터 트랜잭션. 메일 실제 전송 상태 확인·재전송. |
| LOGKEY | 한 번의 발송을 식별하는 키. PAC 로그와 발송 상세(ZTPAC_MAIL_LOG)를 연결. |
| SENDTYPE | 메일 발송 유형 코드. A=알람, D=배포, E=Activity계열, C=CIS컨트롤러, R=CIS리뷰어. |
| XMAIL_ERR / _MRD / _COM | 사용자별 메일 수신 플래그(에러 / 수동준비 / 완료). |
| HTML 템플릿($필드$) | 메일 본문 양식. $필드명$ 자리에 발송 데이터가 치환되고, loop 마커로 표가 반복됨. |
| IS_DATA / IT_DATA1~9 | GET_HTML에 넘기는 데이터. IS_DATA=단건(헤더), IT_DATA1~9=여러 건(반복 표). |
| 배치 잡(Batch Job) | 지정 시각에 자동 실행되는 작업. 알람 메일은 예약 배치(ZLPAC7210)로 발송. |
