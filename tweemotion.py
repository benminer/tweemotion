import util

data = util.readCsv('./data/text_emotion_full.csv', columns=['sentiment', 'content'])

print(data)
