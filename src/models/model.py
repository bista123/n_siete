from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense


class LSTMModel(tf.keras.Model):

    def __init__(self):
        super(LSTMModel, self).__init__()
        self.lstm = LSTM(units=20)
        self.dense = Dense(units=1)

    def call(self, x):  # (batch_size, time_steps, input_dim)
        x = self.lstm(x)  # (batch_size, lstm_dim)
        x = self.dense(x)  # (batch_size, dense_dim)
        return x


model = LSTMModel()
model.compile(optimizer='adam', loss='mean_squared_error')
