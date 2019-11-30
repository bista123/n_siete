import pandas as pd
import os
import numpy as np


def load_data():
    path = os.getcwd()
    if path == '/content':
        data_csv = pd.read_csv('/content/drive/My Drive/weather_forecast/data/processed/temperatures4.csv')
    else:
        data_csv = pd.read_csv(path + '/../../data/processed/temperatures4.csv')

    train_split = int(len(data_csv) * 0.8)
    data = data_csv[['LA-HLY-TEMP-NORMAL', 'PH-HLY-TEMP-NORMAL', 'SF-HLY-TEMP-NORMAL', 'LV-HLY-TEMP-NORMAL']]
    data.index = data_csv['DATE']

    data_mean = data[:train_split].mean(axis=0)
    data_std = data[:train_split].std(axis=0)
    data = np.array((data - data_mean) / data_std)

    return data, train_split


def prepare_data(dataset, target, start, end, look_back, prediction, step):
    data = []
    labels = []

    start_index = start + look_back
    if end is None:
        end = len(dataset) - prediction

    for i in range(start_index, end):
        indices = range(i - look_back, i, step)
        data.append(dataset[indices])

        labels.append(target[i:i + prediction])
    return np.array(data), np.array(labels)


def prepare_dataset(dataset, train_split, look_back, num_predictions, step):
    x_train, y_train = prepare_data(dataset, dataset[:, 1], 0, train_split, look_back, num_predictions, step)
    x_val, y_val = prepare_data(dataset, dataset[:, 1], train_split, None, look_back, num_predictions, step)
    # x_test, y_test = prepare_data(dataset, dataset[:, 1], test_split, None, look_back, num_predictions, step)

    return x_train, y_train, x_val, y_val


def create_time_steps(length):
    time_steps = []
    for i in range(-length, 0, 1):
        time_steps.append(i)
    return time_steps
