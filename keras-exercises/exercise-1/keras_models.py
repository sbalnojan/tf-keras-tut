from keras.models import Sequential
from keras.layers import Dense

def build_seq_model():
    """ Exercise 1a """
    model = Sequential()

    return model

from keras.models import Model
from keras.layers import Input

def build_model():
    """ Exercise 1a """
    return model

# Exercise 1c, understand calls, and what happens here
class InputDummy:
    """ Exercise 1b """

x = InputDummy()
x("this")

InputDummy()("that")

def build_longer_seq_model():
    """ Exercise 1c """

    model.summary()

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

