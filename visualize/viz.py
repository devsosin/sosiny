import pandas as pd

import matplotlib.pyplot as plt
from money.assets import Finance
import seaborn as sns

# %matplotlib inline

from matplotlib import font_manager as fm, rc

fontpath = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
font = fm.FontProperties(fname=fontpath, size=9)

rc('font', family = 'AppleGothic')


class Visualize:

    def __init__(self, finance: Finance) -> None:
        self.finance = finance
        pass


    def __del__(self) -> None:
        pass

    def make_piechart(self, start_date="" , end_date="", category=""):
        if start_date and end_date:
            self.finance.change_date(start_date, end_date)
        summary = self.finance.get_summary(category)
        ratio_int = [int(v.replace(',', '')) for v in summary.values()]
        ratio = [v/sum(ratio_int) for v in ratio_int]
        colors = sns.color_palette('pastel')
        wedgeprops={'width': 0.6, 'edgecolor': 'w', 'linewidth': 2}

        fig = plt.figure()
        fig.patch.set_facecolor('white')
        fig.set_size_inches(18, 10)
        plt.pie(ratio, labels=summary.items(), autopct='%.1f%%', counterclock=False, colors=colors, wedgeprops=wedgeprops)
        plt.text(-1.5, 1, s=category + ' ' + self.finance.as_money({'value': sum(ratio_int)})['value'] + '원', fontdict={'size': 14})
        plt.show()

    def make_barplot(self, start_date="" , end_date="", category=""):
        if start_date and end_date:
            self.finance.change_date(start_date, end_date)

        x = self.finance.get_summary(category).keys()
        y = [int(v.replace(',', '')) for v in self.finance.get_summary(category).values()]
        colors = sns.color_palette('pastel')
        plt.figure(figsize=(15, 8))
        ax = plt.bar(x=x, height=y, color=colors)
        plt.bar_label(ax, labels=[f'{x:,d}원' for x in ax.datavalues])
        plt.title(category + ' ' + format(sum(y), ',')+ '원' if category else '종합')
        plt.show()

    def make_lineplot(self, category="수입", y_limit=None):
        sum_df = self.finance.df[self.finance.df['category']==category].set_index(['date']).groupby(pd.Grouper(freq="M")).sum()
        plt.figure(figsize=(15, 8))
        sns.lineplot(x='date', y='amount', data=sum_df, color=sns.color_palette('pastel')[0])
        for x, y in zip(sum_df.index, sum_df['amount']):
            if y_limit and y > y_limit:
                target_y = int(y_limit-y_limit//10)
            else:
                target_y = y-5000
            plt.text(x=x, y=target_y, s='{:,d}원'.format(y), color='black')

        plt.xticks(sum_df.index)
        plt.xticks(rotation=30, ha='right')
        if y_limit:
            plt.ylim(0, y_limit)
        plt.show()
