from keras.models import Sequential, Model
from keras.layers import Embedding, Lambda
import keras.backend as K

def build_model():
    """ Exercise 3a) """
    model = Sequential()
    model.add(Embedding(1001, 100, input_length=1))
    return model

model = build_model()

# Let's observe the output
import numpy as np

input = np.random.randint(1000)
input = np.expand_dims(input,axis=0) # batch

model.compile('rmsprop', 'mse')
model.summary()

model.predict(input)

# ----------------------------------------------------------------------------------------------------------------------

def build_model_2():
    """ Exercise 3b) """
    model = Sequential()
    model.add(Embedding(1001, 100, input_length=1))
    model.add(Lambda(lambda x: K.mean(x, axis=-1)))
    return model

model = build_model()

# ------------------- Run this -----------------------------------------------------------------------------------------

def generate_dummy_data():
    """ Generate data and labels for each batch of 10 one label. """
    x = np.arange(1,1001)
    arr = np.arange(1,101)
    y = np.repeat(arr,10)
    return x, y

data, labels = generate_dummy_data()

a = np.asarray([[1],[9],[11],[370], [371]])
model.predict(a)
# > How close are the "predictions" for the pairs that are supposed to be "close" by our definition?

# ------------------- Run this -----------------------------------------------------------------------------------------
# Now we fit our embedding to our data
model.fit(data,labels, epochs=100)
model.predict(a)

def get_intermed_output(model, layer_name, input):
    """ Create a model just with your one layer with it's weights. """
    intermediate_layer_model = Model(inputs=model.input,
                                     outputs=model.get_layer(layer_name).output)
    return intermediate_layer_model.predict(input)

# This is supposed to show you, that indeed the embedding layer has "learned" in the most basic way
# the different classes

get_intermed_output(model,"embedding_7", a)