from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import tensorflow.keras as keras


class LSTMModel(tf.keras.Model):

    def __init__(self, shape, prediction):
        super(LSTMModel, self).__init__()
        self.lstm = keras.layers.LSTM(64, return_sequences=True, input_shape=shape)
        self.lstm2 = keras.layers.LSTM(32, return_sequences=True)
        self.lstm3 = keras.layers.LSTM(32, activation='sigmoid')
        self.dense = keras.layers.Dense(prediction)

    def call(self, x):  # (batch_size, time_steps, input_dim)
        x = self.lstm(x)
        x = self.lstm2(x)
        x = self.lstm3(x)
        x = self.dense(x)
        return x

