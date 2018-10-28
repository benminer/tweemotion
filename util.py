import pandas as pd
import csv
import json


def readCsv(filePath):
    data = []
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({'sentiment': row['sentiment'], 'content': row['content']})
    return data


def getSentimentList(data):
    sentiments = {}
    for row in data:
        sentiment = row['sentiment']
        if sentiment in sentiments.keys():
            sentiments[sentiment] += 1
        else:
            sentiments[sentiment] = 1
    sentiments_list = []
    for key, value in sentiments.items():
        if value > 1000:
            sentiments_list.append(key)
    return sentiments_list


def removeUnusedSentiments(data):
    new_data = []
    sentiments_list = getSentimentList(data)
    for row in data:
        if row['sentiment'] in sentiments_list:
            new_data.append(row)
    return new_data


def convertSentimentToIntegers(sentiment_list):
    sentiment_ints = []
    for i in range(1, len(sentiment_list) + 1):
        sentiment_ints.append({'integer': i, 'sentiment': sentiment_list[i-1]})
    return sentiment_ints


def convertWordsToIntegers(words):
    word_ints = []
    for i in range(1, len(words) + 1):
        word_ints.append({'integer': i, 'word': words[i - 1]})
    return word_ints


def makeDictionary(data):
    words = {}
    for row in data:
        content = row['content']
        for word in str.split(content):
            if word in words.keys():
                words[word] += 1
            else:
                words[word] = 1
    frequent_words = []
    for word, count in words.items():
        frequent_words.append({'word': word, 'count': count})

    frequent_words.sort(key=(lambda x: x['count']), reverse=True)
    # Remove the top 10 most common words and then get the 5000 most frequently used ones
    # Returns as list of words
    word_list = list(map(lambda x: x['word'], frequent_words[11:5011]))
    return word_list


if __name__ == '__main__':
    data = readCsv('./data/text_emotion_full.csv')
    sentiments = getSentimentList(data)
    sentiments = convertSentimentToIntegers(sentiments)
    with open('sentiments.json', 'w') as jsonfile:
        jsonfile.write(json.dumps({'sentiments': sentiments}))
    words = makeDictionary(data)
    word_list = convertWordsToIntegers(words)
    with open('bag_of_words.json', 'w') as jsonfile:
        dictionary = {'words': word_list}
        jsonfile.write(json.dumps(dictionary))
