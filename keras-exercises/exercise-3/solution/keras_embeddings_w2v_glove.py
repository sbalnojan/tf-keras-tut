import os
import numpy as np
from keras.layers import Embedding
from keras.initializers import Constant

# Functions adapted from https://github.com/keras-team/keras/blob/master/examples/pretrained_word_embeddings.py
def load_glove(GLOVE_DIR, dim="100d"):
    """ returns dict mapping word -> coeffs in 100d"""
    print('Indexing word vectors.')

    embeddings_index = {}
    with open(os.path.join(GLOVE_DIR, f'glove.6B.{dim}.txt')) as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs

    print('Found %s word vectors.' % len(embeddings_index))
    return embeddings_index

GLOVE_DIR = "glove.6B/"
embeddings_index = load_glove(GLOVE_DIR)
# embeddings_index["the"]

MAX_SEQUENCE_LENGTH = 1000
MAX_NUM_WORDS = 20000
EMBEDDING_DIM = 100
word_index={"the":1,"car":2,"drove":3,"fast":4, "faster":5, "automobile":6}

def generate_glove_embedding(MAX_NUM_WORDS,word_index,EMBEDDING_DIM,embeddings_index,MAX_SEQUENCE_LENGTH):
    # prepare embedding matrix
    num_words = min(MAX_NUM_WORDS, len(word_index)) + 1
    embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))
    for word, i in word_index.items():
        if i > MAX_NUM_WORDS:
            continue
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            # words not found in embedding index will be all-zeros.
            embedding_matrix[i] = embedding_vector

    # load pre-trained word embeddings into an Embedding layer
    # note that we set trainable = False so as to keep the embeddings fixed
    embedding_layer = Embedding(num_words,
                                EMBEDDING_DIM,
                                embeddings_initializer=Constant(embedding_matrix),
                                input_length=MAX_SEQUENCE_LENGTH,
                                trainable=False)

    return embedding_layer

embedding_layer = generate_glove_embedding(MAX_NUM_WORDS,word_index, EMBEDDING_DIM, embeddings_index, MAX_SEQUENCE_LENGTH)

from keras.models import Model
from keras.layers import Input
from keras.preprocessing.sequence import pad_sequences


inputs= Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(inputs)
model = Model(inputs, embedded_sequences)

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])

sentence_1 = np.asarray([1,2]) # the car
sentence_2 = np.asarray([1,6]) # the automobile
sentence_3 = np.asarray([3,4,5]) # drove fast faster

sample = pad_sequences([sentence_1,sentence_2,sentence_3],MAX_SEQUENCE_LENGTH)
preds = model.predict(sample)
np.linalg.norm([preds[0],preds[1]])
np.linalg.norm([preds[0],preds[2]])
np.linalg.norm([preds[2],preds[1]])