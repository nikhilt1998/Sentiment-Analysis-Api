import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from itertools import chain
import pickle, os

#Get the Tokenizer and the model
folder = os.path.dirname(os.path.abspath(__file__))
tokenizer_file = os.path.join(folder, 'tokenizer.pickle')
model_file = os.path.join(folder, 'Sentiment_RNN_model.h5')

with open(tokenizer_file, 'rb') as handle:
    tokenizer = pickle.load(handle)

model=keras.models.load_model(model_file)

class Model:
    def __init__(self, text_review):
        self.text_review=text_review
        self.MAX_LEN=36 # Maximum length of tokenized review from data

    def get_sentiment(self):

        #convert text review to list of numbers using tokenizer trained on the text corpus from data
        review_vec=aa=list(chain.from_iterable(tokenizer.texts_to_sequences(self.text_review.lower())))

        #add padding to the review vector to make it same length with the longest review from data i.e. 36
        review_vec=pad_sequences([review_vec], maxlen=self.MAX_LEN)

        #make prediction from the loaded model and get the output
        pred=model.predict(review_vec)[0][0]
        sentiment=""

        #Output layer activation function was sigmoid(values between 0 and 1)
        if(pred>=0.5):
            sentiment="Positive"
        else:
            sentiment="Negative"
        return sentiment
