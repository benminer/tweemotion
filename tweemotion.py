import util

data = util.readCsv('./data/text_emotion_full.csv')
array = util.toList(data)

sentimentAndContent = []

# 1 is sentiment, 3 is content
for item in array:
    sentimentAndContent.append({'sentiment': item[1], 'content': item[3]})


for item in sentimentAndContent:
    content = item['content']
    if 'the' in content:
        content = content.replace('the', '')
    if 'a' in content:
        content = content.replace('a', '')
    item['content'] = content

#
print(sentimentAndContent)
