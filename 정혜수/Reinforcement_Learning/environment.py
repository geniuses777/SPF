
# 투자할 항목의 차트 데이터를 관리하는 모듈
class Environment:

    PRICE_IDX = 4  # 종가의 위치

    # 생성자 (차트 데이터 할당)
    def __init__(self, chart_data=None):
        self.chart_data = chart_data
        self.observation = None
        self.idx = -1                      # 인덱스의 현재 위치

    # 차트 데이터의 처음으로
    def reset(self):
        self.observation = None
        self.idx = -1

    # 관측 데이터 가져오기 (가공한 데이터)
    def observe(self):
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]
            return self.observation
        return None

    # 관측 데이터로부터 종가 반환
    def get_price(self):
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None

    def set_chart_data(self, chart_data):
        self.chart_data = chart_data