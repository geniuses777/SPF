import numpy as np
from keras.models import Sequential
from keras.layers import Activation, LSTM, Dense, BatchNormalization
from keras.optimizers import sgd


# 주식을 매수할지 매도할지를 결정하는 역할 (신경망 - LSTM)
# dropout을 0.5로 정해서 과적합을 피함
class PolicyNetwork:
    def __init__(self, input_dim=0, output_dim=0, lr=0.01):
        self.input_dim = input_dim
        self.lr = lr

        # LSTM 신경망
        self.model = Sequential() 

        # 은닉층
        self.model.add(LSTM(256, input_shape=(1, input_dim),
                            return_sequences=True, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        self.model.add(LSTM(256, return_sequences=True, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        self.model.add(LSTM(256, return_sequences=False, stateful=False, dropout=0.5))
        self.model.add(BatchNormalization())
        # 출력층
        self.model.add(Dense(output_dim))
        self.model.add(Activation('sigmoid'))

        self.model.compile(optimizer=sgd(lr=lr), loss='mse')
        self.prob = None                  # prob : 가장 최근에 계산한 투자 행동별 확륙

    # prob 변수를 초기화
    def reset(self):
        self.prob = None

    # 신경망을 통한 투자 행동별 확률 계산
    def predict(self, sample):
        self.prob = self.model.predict(np.array(sample).reshape((1, -1, self.input_dim)))[0]
        return self.prob

    # 배치 학습을 위한 데이터 생성
    def train_on_batch(self, x, y):
        return self.model.train_on_batch(x, y)

    # 학습한 신경망을 파일로 저장
    def save_model(self, model_path):
        if model_path is not None and self.model is not None:
            self.model.save_weights(model_path, overwrite=True)

    # 파일로 저장한 신경망을 로드
    def load_model(self, model_path):
        if model_path is not None:
            self.model.load_weights(model_path)