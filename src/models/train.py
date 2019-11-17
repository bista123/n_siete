import tensorflow.keras as keras
from tensorflow.keras.callbacks import CSVLogger
from datetime import datetime
import os


def train(model, x_train, y_train, x_val, y_val, epochs, batch_size):
    if os.getcwd() == '/content':
        checkpoint_path = "/content/drive/My Drive/weather_forecast/models/cp.ckpt"
        log_path = '/content/drive/My Drive/weather_forecast/logs/'
    else:
        checkpoint_path = "../../models/cp.ckpt"
        log_path = '../../logs/train/'
    csv_logger = CSVLogger(log_path + 'log_' + datetime.now().strftime("%d_%m_%H-%M-%S") + '.log', append=True,  separator=';')

    model = model
    model.compile(optimizer='adam', loss='mean_squared_error')

    cp_callback = keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                  save_weights_only=True,
                                                  verbose=1)

    trained_model = model.fit(x=x_train,
                              y=y_train,
                              epochs=epochs,
                              batch_size=batch_size,
                              callbacks=[cp_callback, csv_logger],
                              validation_data=(x_val, y_val))
    model.summary()

    return model
