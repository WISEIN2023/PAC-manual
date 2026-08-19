---
id: activity-master/10-unyeong-juuisahang-hwakin-pilyo-hangmok
doc: activity-master
title: 10. 운영 주의사항 (확인 필요 항목)
parent: docs/activity-master/README.md
---

# 10. 운영 주의사항 (확인 필요 항목)

1. Group/Sub/Activity 코드는 자동 채번이라 변경 불가 — 명명체계(Bus.Pkg+G/S+번호)와 생성 순서를 사전에 관리.
2. 이미 모델링(Map)·수행이력(ZTPAC_STATUS)이 있는 Activity는 Move To/삭제 제한.
3. Auto Trigger(X)는 ZLPAC0070 사전 정의 필수. Between 유형은 Inbound/Outbound 모두 설정.
4. Rework Rule ID는 ZFCLR0010 동기화로 생성되므로 신규 Category는 회계팀과 동기화 시점 협의. (ZFCLR0010은 본 시스템 미검증)
5. Skip Enable은 운영 권장사항 아님 — 결산 조직/기간별 Skip 허용 인원 별도 관리하는 방식으로 관리.
6. Variant와 Param은 합집합 수행, Variant 생성 Parameter는 수정 불가.
7. 각 버튼의 저장 시점이 다름(내부 저장형 vs 본화면 동시 저장형) — 5.7 참고.
