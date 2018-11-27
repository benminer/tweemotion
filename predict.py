from tensorflow import keras
from util import clean_text
from tokenizer import load_tokenizer
import numpy as np


def load_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights('model.h5')
    return loaded_model


def predict_sentiment(texts):
    model = load_model()
    tokenizer = load_tokenizer()

    for text in texts:
        texts[texts.index(text)] = clean_text(text)

    texts = np.array(texts)

    sequences = tokenizer.texts_to_sequences(texts)

    data = keras.preprocessing.sequence.pad_sequences(sequences, maxlen=50)

    prediction = model.predict(data)
    keras.backend.clear_session()
    return prediction.tolist()


if __name__ == '__main__':
    test = ["Testing can be fun if it works!"]
    print(predict_sentiment(test))
