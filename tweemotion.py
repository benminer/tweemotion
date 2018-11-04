import util
import tensorflow as tf
import numpy as np

training = util.readCsv('./data/training_set.csv')
validation = util.readCsv('./data/validation_set.csv')

training_data = []
for row in training:
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    training_data.append(word_list)

training_labels = [row['sentiment'] for row in training]

validation_data = []
for row in validation:
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    validation_data.append(word_list)
validation_labels = [row['sentiment'] for row in validation]

training_data = tf.keras.preprocessing.sequence.pad_sequences(training_data,
                                                              value=0,
                                                              padding='post',
                                                              maxlen=80)

validation_data = tf.keras.preprocessing.sequence.pad_sequences(validation_data,
                                                                value=0,
                                                                padding='post',
                                                                maxlen=80)

training_data = np.array(training_data)
training_labels = np.array(training_labels)
validation_data = np.array(validation_data)
validation_labels = np.array(validation_labels)

vocab_size = 10000

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, 16))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(16, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1, activation=tf.nn.sigmoid))

model.summary()

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(training_data,
                    training_labels,
                    epochs=20,
                    batch_size=512,
                    validation_data=(validation_data, validation_labels),
                    verbose=1)
