import util
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import os
# import json

vocab_size = 62167

training = util.readOurCsv('./data/data_set_2.csv')
# validation = util.readOurCsv('./data/validation_set_2.csv')

training_df = pd.DataFrame.from_csv('./data/data_set_2.csv')
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts(training_df['content'])
sequences = tokenizer.texts_to_sequences(training_df['content'])
training_data = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=50)


# bagOfWords = None
# EMBEDDING_DIM = 50
#
# with open('bag_of_words_2.json') as json_data:
#     bagOfWords = json.load(json_data)
training_labels = []
for row in training:
    label = []
    for key in row.keys():
        if key != 'content':
            label.append(int(row[key]))
    training_labels.append(label)

training_labels = np.array(training_labels)
#
# validation_data = []
# validation_labels = []
# for row in validation:
#     word_list = []
#     for word in row['content'].split():
#         word_list.append(int(word))
#     validation_data.append(word_list)
#     label = []
#     for key in row.keys():
#         if key != 'content':
#             label.append(int(row[key]))
#     validation_labels.append(label)

# training_data = tf.keras.preprocessing.sequence.pad_sequences(training_data,
#                                                               value=0,
#                                                               padding='post',
#                                                               maxlen=50)
#
# validation_data = tf.keras.preprocessing.sequence.pad_sequences(validation_data,
#                                                                 value=0,
#                                                                 padding='post',
#                                                                 maxlen=50)


epochs = 10

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, 100, input_length=50))
model.add(tf.keras.layers.LSTM(100, dropout=0.4, recurrent_dropout=0.2))
model.add(tf.keras.layers.Dropout(0.5, noise_shape=None, seed=None))
model.add(tf.keras.layers.BatchNormalization())
# model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
# model.add(tf.keras.layers.GlobalAveragePooling1D())
# model.add(tf.keras.layers.Dense(64, activation=tf.nn.elu))
# model.add(tf.keras.layers.Dropout(0.7, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
# model.add(tf.keras.layers.Dropout(0.5, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(16, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

model.summary()

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              # loss='categorical_crossentropy',
              metrics=['categorical_accuracy', 'mean_absolute_error'])

history = model.fit(training_data,
                    training_labels,
                    batch_size=500,
                    epochs=epochs,
                    validation_split=0.3,
                    verbose=1)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")

# plot accuracy
history_dict = history.history

print("Test-Accuracy:", np.mean(history_dict["val_categorical_accuracy"]))

acc = history_dict['categorical_accuracy']
val_acc = history_dict['val_categorical_accuracy']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
