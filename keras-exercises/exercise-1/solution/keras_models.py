from keras.models import Sequential
from keras.layers import Dense

def build_seq_model():
    """ Exercise 1a """
    INPUT_SHAPE=(10,)
    model = Sequential()
    model.add(Dense(2, input_shape=INPUT_SHAPE))

    return model

from keras.models import Model
from keras.layers import Input

def build_model():
    """ Exercise 1a """
    INPUT_SHAPE=(10,)
    inputs = Input(shape=INPUT_SHAPE)
    outputs = Dense(2)(inputs)
    model = Model(inputs=inputs, outputs=outputs)

    return model

# Exercise 1c, understand calls, and what happens here
class InputDummy:
    """ Exercise 1b """
    def __call__(self, this):
        print(this)

x = InputDummy()
x("this")

InputDummy()("that")

def build_longer_seq_model():
    """ Exercise 1c """
    INPUT_SHAPE=(10,)
    model = Sequential()
    model.add(Dense(2, input_shape=INPUT_SHAPE))
    model.add(Dense(20))
    model.add(Dense(2))

    model.summary()
    return model

# ----------------------------------------------------------------------------------------------------------------------
# ---- Template part
import numpy as np

def generate_dummy_data():
    x = np.asarray([1,1,1,1,1,1,1,1,1,1])
    x=x.reshape(1,-1)
    print(f"the shape is: {x.shape}")
    return x

# Generate dummy data
x = generate_dummy_data()

# We just pick random optimizer/loss/metrics to get things running.

# Your .Sequential() model
model = build_seq_model()
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
print("we predict, without training for now...")
pred = model.predict(x)
print("we predict: ", pred, f" our predicted vector has the shape {pred.shape}")

# Your .Model() model
model = build_model()
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
print("we predict, without training for now...")
pred = model.predict(x)
print("we predict: ", pred, f" our predicted vector has the shape {pred.shape}")

# Your longer .Sequential() model
model = build_longer_seq_model()
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
print("we predict, without training for now...")
pred = model.predict(x)
print("we predict: ", pred, f" our predicted vector has the shape {pred.shape}")

