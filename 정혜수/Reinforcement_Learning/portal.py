
# 야후에서 주식 데이터를 획득하는 소스코드
from pandas_datareader import data
import fix_yahoo_finance
fix_yahoo_finance.pdr_override()

chart_data = data.get_data_yahoo(
    # 삼성
    '005930.KS',  # 코스피: KS, 코스닥: KQ
    '2016-01-01',
    '2017-12-31'
)