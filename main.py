from money.assets import Assets, Finance

if __name__ == '__main__':
    my_assets = Assets()
    my_finance = Finance()

    # 정기적으로 보고싶은 정보 ??? (요약보고서 - 메인페이지용)

    print(my_assets.df)

    # print('---- 기간 변경 ----')
    # print(my_assets.change_date('2022-01-01', '2022-12-31'))

    # print('---- 요약 출력 ----')
    # print(my_assets.get_summary())

    # print('---- 상세 출력 ----')
    # print(my_assets.get_summary('수입'))

    # print(my_assets.ndf[my_assets.ndf['connections']=='(주)크몽'])
