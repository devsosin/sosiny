from money.assets import Assets, Finance

from visualize.viz import Visualize

if __name__ == '__main__':
    my_assets = Assets()
    my_finance = Finance()

    my_viz = Visualize(my_finance)

    # 자산데이터 최신화
    my_finance.sync_assets(my_assets)

    # print(my_finance.df['link'][0])
    # print(type(my_finance.df['link'][0]))

    # 데이터 추가
    # my_finance.add_data(*[{
    #     'date': '2022-10-10',
    #     'category': '수입',
    #     'detail': '테스트',
    #     'connections': '',
    #     'amount': '0',
    #     'memo': '',
    #     'link': '',
    # },
    # {
    #     'date': '2022-10-10',
    #     'category': '수입',
    #     'detail': '테스트',
    #     'connections': '',
    #     'amount': '0',
    #     'memo': '',
    #     'link': '',
    # }])

    print('---- 기간 변경 ----')
    print(my_finance.change_date('2023-02-01', '2023-02-28'))

    print('---- 요약 출력 ----')
    print(my_finance.get_summary())

    # print('---- 상세 출력 ----')
    # print(my_assets.get_summary('수입'))

    # print(my_assets.ndf[my_assets.ndf['connections']=='(주)크몽'])

    my_viz.make_piechart(start_date='2023-01-01',end_date='2023-01-31', category='수입')

    my_viz.make_barplot(start_date='2023-01-01',end_date='2023-01-31', category='변동지출')

    my_viz.make_lineplot(category='고정지출')

