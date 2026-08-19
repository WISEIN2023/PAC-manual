---
id: pac-config/03-15-alarm-control
doc: pac-config
title: 3. System Config (ZTPACSYS) > 3.15 Alarm Control
parent: docs/pac-config/README.md
---

# 3. System Config (ZTPACSYS)

## 3.15 Alarm Control

### 3.15.1 XMAIL_ERR — Mailing Active when Error

**테이블-필드:** ZTPACSYS - XMAIL_ERR

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : 메일링 에러를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ ZLPAC1000_F01, ZLPAC1010F01, ZLPAC1011_F01, ZLPAC1020F01(Participant 관리 4종)

#### 프로세스 관점 분석 (사용 로직)

에러 발생 시 메일링 활성화(시스템 전역).

① Participant 관리 화면에서 '에러 메일 수신' 설정 컬럼을 활성화 — 실제 발송(ZFPAC_MAILING→ZFPAC_SEND_ERROR_MAIL)은 BusPkg의 XMAIL과 Participant별 수신 플래그를 조합하여 수신자 결정.

② 시스템 레벨에서 알람 유형 자체를 켜고 끄는 스위치.

#### 영향도 분석 (변경 시 영향)

해제 시 전 BusPkg에서 에러 메일 알람 유형 자체가 비활성 — BusPkg의 XMAIL이 켜져 있어도 에러 통지가 나가지 않아 장애 인지 지연 위험.

### 3.15.2 XMAIL_MRD — Mailing Active when Manual Ready

**테이블-필드:** ZTPACSYS - XMAIL_MRD

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : 메일링 매뉴얼 레디를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

Manual Ready 시 메일링 활성화.

① XMAIL_ERR과 동일 패턴 — Manual Ready 도달 시 담당자 메일 발송(ZFPAC_SEND_MREADY_MAIL) 유형 활성화.

#### 영향도 분석 (변경 시 영향)

해제 시 Manual Ready 통지가 중단되어 수작업 Activity의 착수 지연 위험 — Manual 작업이 많은 프로세스일수록 영향 큼.

### 3.15.3 XMAIL_COM — Mailing Active when Completed

**테이블-필드:** ZTPACSYS - XMAIL_COM

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : 메일링 완료를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

완료 시 메일링 활성화.

① Activity 완료 시 메일 발송(ZFPAC_SEND_COMPLETE_MAIL) 유형 활성화.

#### 영향도 분석 (변경 시 영향)

해제 시 완료 통지 중단 — 후속 확인 업무를 메일 기반으로 하던 담당자의 인지 지연.

### 3.15.4 XTODO_ERR — To Do Active when Error

**테이블-필드:** ZTPACSYS - XTODO_ERR

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : To Do 에러를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

에러 시 To Do 활성화.

① 에러 발생 시 To Do 발송(ZFPAC_OPEN_TODO IV_TYPE='E') 유형 설정 컬럼 활성화.

#### 영향도 분석 (변경 시 영향)

해제 시 에러 To Do 발행 중단 — 포털 To Do로 오류를 처리하는 운영 흐름 단절.

### 3.15.5 XTODO_MRD — To Do Active when Manual Ready

**테이블-필드:** ZTPACSYS - XTODO_MRD

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : To Do 매뉴얼 레디를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

Manual Ready 시 To Do 활성화.

① Manual Ready 시 To Do 발송(IV_TYPE='M') 유형 설정 컬럼 활성화.

#### 영향도 분석 (변경 시 영향)

해제 시 Manual Ready To Do 중단 — 수작업 착수 트리거 유실 위험.

### 3.15.6 XMSGR_ERR — Messenger Active when Error

**테이블-필드:** ZTPACSYS - XMSGR_ERR

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : 메신져 에러를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

에러 시 메신저 발송 활성화.

① 메신저 채널 알람의 에러 유형 설정 컬럼 활성화(발송은 별도 메신저 I/F 경유).

#### 영향도 분석 (변경 시 영향)

메신저 I/F 구성이 없는 환경에서는 설정해도 효과 없음 — I/F 구축과 세트.

### 3.15.7 XMSGR_MRD — Messenger Active when Manual Ready

**테이블-필드:** ZTPACSYS - XMSGR_MRD

**운영 설정(LG전자 설정) :** 미사용(LG전자는 필드없음)

#### 설정 설명

X 활성화시 : 메신져 매뉴얼 레디를 활성화 한다(Participant 필드가 활성화됨)

#### 참조 프로그램 / 오브젝트 (Where-used)

■ Participant 관리 4종(ZLPAC1000/1010/1011/1020)

#### 프로세스 관점 분석 (사용 로직)

Manual Ready 시 메신저 발송 활성화.

① 메신저 채널 알람의 Manual Ready 유형 설정 컬럼 활성화.

#### 영향도 분석 (변경 시 영향)

XMSGR_ERR과 동일 — 메신저 I/F 전제.
