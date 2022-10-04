from money.assets import Assets


if __name__ == '__main__':
    my_assets = Assets()
    print('---- 기간 변경 ----')
    print(my_assets.change_date('2022-01-01', '2022-12-31'))

    print('---- 요약 출력 ----')
    print(my_assets.get_summary())

    print('---- 상세 출력 ----')
    print(my_assets.get_summary('수입'))
