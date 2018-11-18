from tensorflow import keras
import util

testing = util.readOurCsv('./data/training_set.csv')

testing_data = []
testing_labels = []
for row in testing:
    word_list = []
    for word in row['content'].split():
        word_list.append(int(word))
    testing_data.append(word_list)
    label = []
    for key in row.keys():
        if key != 'content':
            label.append(int(row[key]))
    testing_labels.append(label)

testing_data = keras.preprocessing.sequence.pad_sequences(testing_data,
                                                           value=0,
                                                           padding='post',
                                                           maxlen=50)

json_file = open('model-500-highDO.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)

loaded_model.load_weights('model-500-highDO.h5')

prediction = loaded_model.predict(testing_data[:5])
print(prediction)