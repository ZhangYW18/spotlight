import os
import time
import pickle
from keras.models import load_model

import re

from keras.preprocessing.sequence import pad_sequences
from nltk import SnowballStemmer
from nltk.corpus import stopwords


TEXT_CLEANING_RE = r'@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+|[0-9]+'

# POSITIVE = 0
# NEGATIVE = 1
# NEUTRAL = 2
POSITIVE = 'Positive'
NEGATIVE = 'Negative'
NEUTRAL = 'Neutral'

SEQUENCE_LENGTH = 300

EPOCHS = 8


print('loading models...')
model = load_model('/Users/victor/Git/my/spotlight/index/static/models/model.h5')
model._make_predict_function()
tokenizer = pickle.load(open('/Users/victor/Git/my/spotlight/index/static/models/tokenizer.pkl', 'rb'))
print('load success!')


def preprocess(tweet):
    stop_words = stopwords.words("english")
    stemmer = SnowballStemmer("english")
    tweet = re.sub(TEXT_CLEANING_RE, ' ', str(tweet).lower()).strip()
    tokens = []
    for token in tweet.split():
        if token not in stop_words:
            tokens.append(stemmer.stem(token))
    return " ".join(tokens)


def decode_sentiment(score, include_neutral=True, threshold=0.65):
    if include_neutral:
        label = NEUTRAL
        if score <= 1-threshold:
            label = NEGATIVE
        elif score >= threshold:
            label = POSITIVE
        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE


def predict(input, include_neutral=True):
    # predict
    input_processed = preprocess(input)
    text = str(input_processed).split()
    global tokenizer, model
    start_at = time.time()
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    score = model.predict([x_test])[0]
    print("score: ", score)
    label = decode_sentiment(score, include_neutral=include_neutral)
    print("label: ", label)
    return {"label": label, "score": float(score),
            "elapsed_time": time.time() - start_at}


def train(input, feedback):
    input_processed = preprocess(input)
    text = str(input_processed).split()
    x = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    y = [int(feedback)]
#    y = y.reshape(-1, 1)
    global model
    print('training...')
    model.fit([x], y, epochs=EPOCHS)


if __name__ == '__main__':
    predict("I feel happy")
    predict("I feel sad")
    predict("i don't know what i'm doing")
