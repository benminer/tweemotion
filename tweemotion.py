import util
import tensorflow as tf
import numpy as np

training_data = util.readCsv('./data/training_set.csv')
validation_data = util.readCsv('./data/validation_set.csv')

training_data = np.array(training_data)
validation_data = np.array(validation_data)

model = tf.keras.Sequential()
# Adds a densely-connected layer with 64 units to the model:
model.add(tf.keras.layers.Dense(64, activation='relu'))
# Add another:
model.add(tf.keras.layers.Dense(64, activation='relu'))
# Add a softmax layer with 10 output units:
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])