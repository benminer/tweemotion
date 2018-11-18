import os
import util
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

training = util.readOurCsv('./data/training_set.csv')
validation = util.readOurCsv('./data/validation_set.csv')

training_data = []
training_labels = []
for row in training:
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    training_data.append(word_list)
    label = []
    for key in row.keys():
        if key != 'content':
            label.append(int(row[key]))
    training_labels.append(label)

validation_data = []
validation_labels = []
for row in validation:
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    validation_data.append(word_list)
    label = []
    for key in row.keys():
        if key != 'content':
            label.append(int(row[key]))
    validation_labels.append(label)

training_data = tf.keras.preprocessing.sequence.pad_sequences(training_data,
                                                              value=0,
                                                              padding='post',
                                                              maxlen=50)

validation_data = tf.keras.preprocessing.sequence.pad_sequences(validation_data,
                                                                value=0,
                                                                padding='post',
                                                                maxlen=50)

training_data = np.array(training_data)
training_labels = np.array(training_labels)
validation_data = np.array(validation_data)
validation_labels = np.array(validation_labels)

GLOVE_DIR = './data'
# Prepare embedding layer
embeddings_index = {}
f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

# vocab_size = 14673
vocab_size = 5000
epochs = 500
# sgd = tf.keras.optimizers.SGD(lr=0.01, momentum=0.1, decay=0.01/epochs, nesterov=False)
# rms = z

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, 32))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.7, noise_shape=None, seed=None))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dropout(0.5, noise_shape=None, seed=None))
# model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(5, activation=tf.nn.softmax))

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=[tf.keras.metrics.categorical_accuracy])

history = model.fit(training_data,
                    training_labels,
                    epochs=epochs,
                    batch_size=128,
                    validation_data=(validation_data, validation_labels),
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
