import util
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

training = util.readOurCsv('./data/training_set.csv')
validation = util.readOurCsv('./data/validation_set.csv')

training_data = []
training_labels = []
for row in training:
    if int(row['sadness']) == 0 and int(row['worry']) == 0:
        continue
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    training_data.append(word_list)
    label = []
    for key in row.keys():
        if key == 'sadness' or key == 'worry':
            label.append(int(row[key]))
    training_labels.append(label)

validation_data = []
validation_labels = []
for row in validation:
    if int(row['sadness']) == 0 and int(row['worry']) == 0:
        continue
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    validation_data.append(word_list)
    label = []
    for key in row.keys():
        if key == 'sadness' or key == 'worry':
            label.append(int(row[key]))
    validation_labels.append(label)

training_data = tf.keras.preprocessing.sequence.pad_sequences(training_data,
                                                              value=0,
                                                              padding='post',
                                                              maxlen=20)

validation_data = tf.keras.preprocessing.sequence.pad_sequences(validation_data,
                                                                value=0,
                                                                padding='post',
                                                                maxlen=20)

training_data = np.array(training_data)
training_labels = np.array(training_labels)
validation_data = np.array(validation_data)
validation_labels = np.array(validation_labels)

vocab_size = 5000

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, 16))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=[tf.keras.metrics.categorical_accuracy])

history = model.fit(training_data,
                    training_labels,
                    epochs=100,
                    batch_size=512,
                    validation_data=(validation_data, validation_labels),
                    verbose=1)

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
