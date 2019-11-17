from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import tensorflow.keras as keras


class LSTMModel(tf.keras.Model):

    def __init__(self, shape):
        super(LSTMModel, self).__init__()
        self.lstm = keras.layers.LSTM(32, return_sequences=True, input_shape=shape)
        self.lstm2 = keras.layers.LSTM(16, activation='relu')
        self.dense = keras.layers.Dense(12)

    def call(self, x):  # (batch_size, time_steps, input_dim)
        x = self.lstm(x)
        x = self.lstm2(x)
        x = self.dense(x)
        return x

