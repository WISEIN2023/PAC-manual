---
id: pac-config/02-09-mailing
doc: pac-config
title: 2. Business Package Config (ZTPAC_CONFIG) > 2.9 Mailing
parent: docs/pac-config/README.md
---

# 2. Business Package Config (ZTPAC_CONFIG)

## 2.9 Mailing

### 2.9.1 XMAIL — Mailling Active?

**테이블-필드:** ZTPAC_CONFIG - XMAIL

**운영 설정(LG전자 특화) :** 모두 활성

#### 설정 설명

□ X설정 :  PAC 메일링 활성화

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_CONFIRM_ITEM(LZPAC052U01), ZFPAC_AUTOTRIG_LEGACY(LZPAC054F01), ZFPAC_SEND_ERROR/MREADY/COMPLETE_MAIL(LZPAC202F01),

ZFPAC_SEND_CIS_MAIL/CONT(LZPACCIS0220/0230F01), ZCL_PAC=>UPDATE_PAC_STATUS(CM01X), ZLPAC1011_F01

#### 프로세스 관점 분석 (사용 로직)

PAC 메일링 활성화 여부(BusPkg 단위 마스터 스위치).

① ZCL_PAC=>UPDATE_PAC_STATUS: Activity 상태 변경(에러/Manual Ready/완료) 시 'X'인 경우에만 ZFPAC_MAILING 호출 경로 진입.

② ZFPAC_CONFIRM_ITEM: Manual Confirm 성공 후 'X'이면 ZFPAC_MAILING(IV_STATUS='C')으로 완료 메일 발송.

③ SAPLZPAC202(에러/Manual Ready/완료 메일 FM 세트)와 CIS 메일에서 발송 전 활성 여부 검사.

※ 알람 유형별 세분화는 ZTPACSYS의 XMAIL_ERR/MRD/COM + Participant 설정으로 결정.

#### 영향도 분석 (변경 시 영향)

해제 시 해당 BusPkg의 모든 메일 알람(에러/Manual Ready/완료/CIS)이 일괄 중단 — 담당자가 상태 변화를 인지하지 못해 결산 지연 위험.

활성 시 수신자(Participant)와 SENDER가 함께 정비되어 있어야 정상 발송됨.

### 2.9.2 SENDER — Sender E-mail

**테이블-필드:** ZTPAC_CONFIG - SENDER

**운영 설정(LG전자 특화) :** nerpsys@lge.com

#### 설정 설명

발송자 메일 주소를 입력. 메일 발송시 해당 메일주소로 발송이 된다

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZFPAC_SEND_ERROR/MREADY/COMPLETE_MAIL(LZPAC202F01), ZFPAC_SEND_CIS_MAIL(LZPACCIS0220F01),

ZFPAC_SEND_CIS_CONT(LZPACCIS0230F01) → ZCL_PAC_MAIL=>SEND_MAIL_*의 IV_SENDER로 전달

#### 프로세스 관점 분석 (사용 로직)

발송자 메일 주소.

① SAPLZPAC202의 각 발송 FM이 Config에서 SENDER를 읽어 ZCL_PAC_MAIL=>SEND_MAIL_ERROR/MREADY/COMPLETE의 IV_SENDER/IV_SENDERNAME으로 전달 → SET_SENDER(CL_CAM_ADDRESS_BCS)로 발신자 지정.

② CIS(결산점검) Controller/Reviewer 메일도 동일.

#### 영향도 분석 (변경 시 영향)

미등록/오등록 시 메일 발송 실패(BCS 오류) 또는 수신측 스팸 분류 가능 — 메일서버(SOST) 발신 정책과 일치해야 함.

발신 도메인 정책 변경 시 함께 갱신 필요.
