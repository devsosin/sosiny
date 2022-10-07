import pandas as pd
from datetime import datetime
from .category import _finance_category, _assets_category

class Money:
    '''
    돈 관리 클래스
    df = 전체 데이터프레임
    ndf = 현재 가공중인 데이터프레임
    '''

    def get_df(self, category):
        '''
        특정 카테고리의 데이터프레임 반환
        '''
        return self.money_ndf[self.money_ndf['category']==category]
    
    def get_date(self):
        try:
            return self._sd.strftime('%Y-%m-%d') + ' ~ ' + self._ed.strftime('%Y-%m-%d')
        except:
            return '설정된 기간이 없습니다.'

    def change_date(self, start_date:str, end_date:str) -> pd.DataFrame:
        '''
        기간을 설정하는 함수입니다.
        '''
        
        self._sd = datetime.strptime(start_date, '%Y-%m-%d')
        self._ed = datetime.strptime(end_date, '%Y-%m-%d')

        self.ndf = self.df[(self._sd <= self.df['date']) & (self.df['date'] <= self._ed)]

        return self.pagination(1)

    def pagination(self, page) -> pd.DataFrame:
        '''
        페이지네이션
        '''
        return self.ndf[(page-1)*10:page*10]
    
    def get_summary(self, category=None) -> dict:
        '''
        데이터 요약
        '''

        if category:
            return self.as_money(self.ndf[self.ndf['category']==category].groupby('detail').sum(numeric_only=True).to_dict()['amount'])
        else:
            return self.as_money(self.ndf.groupby('category').sum(numeric_only=True).to_dict()['amount'])

    @staticmethod
    def _read_file(file_path='./finance_records.tsv'):
        money_records = []
        with open(file_path, 'r', encoding='utf-8') as f:
            header = f.readline().rstrip().split('\t')
            for data in [l.rstrip('\n').split('\t') for l in f.readlines()]:
                money_records.append(data)
        return {
            'data': money_records,
            'columns': header
        }

    @staticmethod
    def as_money(my_dict:dict) -> dict:
        '''
        금액에 , 추가
        '''
        return {k: format(my_dict[k], ',') for k in  my_dict}


class Finance(Money):
    '''
    수입 지출 클래스
    '''

    FINANCE_CATEGORY = _finance_category

    def __init__(self) -> None:
        # 수입 지출 데이터 읽기
        self.df = pd.DataFrame(**self._read_file('./finance_records.tsv')).astype({'date': 'datetime64[ns]', 'amount': 'int'})
        self.ndf = self.df
        super().__init__()

class Assets(Money):
    '''
    자산관리 클래스
    '''
    ASSETS_CATEGORY = _assets_category

    # DB에서 데이터 읽어오기 (특정 유저의)
    def __init__(self) -> None:
        # 자산 데이터 읽기
        self.df = pd.DataFrame(**self._read_file('./assets_records.tsv')).astype({'amount': 'int'})
        self.ndf = self.df
        super().__init__()
    
