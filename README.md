# 자산관리 앱

## 데이터 포맷
| finance_records.tsv (수입 지출 데이터)
```tsv
date	category	detail	connections	amount	memo	link
2021-02-02	수입	사업	회사명	300000	강의	
```

| assets_records.tsv (자산 데이터)
```tsv
category	detail	code	memo	amount
현금				10000
예금	KB국민은행	70100200140450	주거래계좌	100000
주식	삼성전자	005930	코스피	10
```

* 카테고리에 대한 내용은 ./money/category.py 참고

## 핵심기능

1. 수입 지출 내역 입력 시 자산에 자동 반영 (작업 중)
    - 마지막 link에 자산 index번호 넣으면 자산정보 최신화 후 link 부분 삭제
    - 카테고리 "이동" 시 두 개 데이터 읽어 자산 이동

2. 자산, 재무 정보 입력 (작업 중)
    - add_data()

3. 수입 지출 관리 및 요약 정보
    - change_data() # 기간설정
    - get_summary() # 카테고리 별 총 금액
    - get_detail(category) # 해당 카테고리 내 detail 별 분포

