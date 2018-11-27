import util
import tensorflow as tf
import numpy as np
import pandas as pd
import tokenizer as tk

vocab_size = 56997

training = util.readOurCsv('./data/data_set_2.csv')
# validation = util.readOurCsv('./data/validation_set_2.csv')

training_df = pd.DataFrame.from_csv('./data/data_set_2.csv')
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(training_df['content'])
sequences = tokenizer.texts_to_sequences(training_df['content'])
training_data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=50)

tk.save_tokenizer(tokenizer)

training_labels = []
for row in training:
    label = []
    for key in row.keys():
        if key != 'content':
            label.append(int(row[key]))
    training_labels.append(label)

training_labels = np.array(training_labels)

epochs = 10

model = tf.keras.Sequential()

# Bag Of Words
model.add(tf.keras.layers.Embedding(vocab_size, 100, input_length=50))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(64, activation=tf.nn.elu))
model.add(tf.keras.layers.Dropout(0.4, noise_shape=None, seed=None))
model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.2, noise_shape=None, seed=None))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

# RNN
# model.add(tf.keras.layers.Embedding(vocab_size, 100, input_length=50))
# model.add(tf.keras.layers.LSTM(128, dropout=0.4, recurrent_dropout=0.2))
# model.add(tf.keras.layers.Dropout(0.4, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dropout(0.2, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

# CNN
# model.add(tf.keras.layers.Embedding(vocab_size, 100, input_length=50))
# model.add(tf.keras.layers.Conv1D(64, 5, activation='relu'))
# model.add(tf.keras.layers.MaxPooling1D(pool_size=4))
# model.add(tf.keras.layers.Dropout(0.4, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dropout(0.2, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

# CNN + RNN
# model.add(tf.keras.layers.Embedding(vocab_size, 100, input_length=50))
# model.add(tf.keras.layers.Conv1D(64, 5, activation='relu'))
# model.add(tf.keras.layers.MaxPooling1D(pool_size=4))
# model.add(tf.keras.layers.LSTM(64, dropout=0.4, recurrent_dropout=0.2))
# model.add(tf.keras.layers.Dropout(0.4, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dropout(0.2, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Flatten())
# model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['categorical_accuracy'])

early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)

history = model.fit(training_data,
                    training_labels,
                    batch_size=500,
                    epochs=epochs,
                    validation_split=0.05,
                    verbose=1,
                    callbacks=[early_stopping])

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")