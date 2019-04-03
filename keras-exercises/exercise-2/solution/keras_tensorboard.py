import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard


sess = tf.Session()

def build_model(input_shape):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(2, input_shape=input_shape))
    model.compile(optimizer = 'adam', loss = 'mean_squared_error')

    return model

def run_session(model, session_name, data, labels):
    model.fit(data, labels, epochs=10, batch_size=32,
                    callbacks=[TensorBoard(log_dir='logs/' + session_name)])

# -------- Run this to see whether things work -------------------------------------------------------------------------

import numpy as np

def generate_dummy_data():
    x = np.asarray([[1,1],[2,2]])
    return np.repeat(x,100000,axis=0), np.repeat([1], 200000)

model = build_model((1,1))
data, labels = generate_dummy_data()
run_session(build_model((2,)),"keras_test", data, labels)