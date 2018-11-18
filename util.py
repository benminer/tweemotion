import pandas as pd
import csv
import json
import re
from random import shuffle

thresholdCount = 6500


def readOurCsv(filePath):
    data = []
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_data = {}
            for key in row.keys():
                new_data[key] = row[key]
            data.append(new_data)
    return data


def readCsv(filePath):
    data = []
    with open(filePath, encoding='iso-8859-1') as csvfile:
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
        print(key, value)
        if value > thresholdCount:
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
    sentiment_ints = {}
    for i in range(1, len(sentiment_list) + 1):
        sentiment = sentiment_list[i - 1]
        sentiment_ints[sentiment] = i
    return sentiment_ints


def convertWordsToIntegers(words):
    word_ints = {}
    for i in range(1, len(words) + 1):
        word = words[i - 1]
        word_ints[word] = i
    return word_ints


def makeDictionary(data):
    words = {}
    for row in data:
        content = row['content']
        for word in str.split(content):
            regex = re.compile('[@]')
            alphabetOnly = re.compile('[^a-zA-Z]')
            if regex.match(word):
                continue
            word = alphabetOnly.sub('', word)
            if word.lower() in words.keys():
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1
    frequent_words = []
    for word, count in words.items():
        frequent_words.append({'word': word, 'count': count})

    frequent_words.sort(key=(lambda x: x['count']), reverse=True)
    print(len(frequent_words))
    # Remove the top 10 most common words and then get the 2000 most frequently used ones
    # Returns as list of words
    word_list = list(map(lambda x: x['word'], frequent_words))
    return word_list


def convertDataToInts(row, words):
    new_content = ''
    for word in row['content']:
        if word in words.keys():
            new_content += str(words[word]) + ' '
    row['content'] = new_content
    return row


def splitTrainingData(data):
    pos = data[0:6500]
    neg = data[6500:13000]
    neutral = data[13000:]

    training = pos[0:5000] + neg[0:5000] + neutral[0:5000]
    validation = pos[5000::2] + neg[5000::2] + neutral[5000::2]
    testing = pos[5001::2] + neg[5001::2] + neutral[5001::2]

    shuffle(training)
    shuffle(testing)
    shuffle(validation)

    return training, validation, testing


def writeCsv(filename, data):
    with open(filename, 'w') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def convertDataToBinary(data, sentiments):
    new_data = []
    for row in data:
        new_row = {}
        for sentiment in sentiments:
            if row['sentiment'] == sentiment:
                new_row[sentiment] = 1
            else:
                new_row[sentiment] = 0
        new_row['content'] = row['content']
        new_data.append(new_row)
    return new_data


def normalizeData(data):

    positiveCount = []
    negativeCount = []
    neutralCount = []

    for row in data:
        if row['positive'] and len(positiveCount) < thresholdCount:
            positiveCount.append(row)
        elif row['negative'] and len(negativeCount) < thresholdCount:
            negativeCount.append(row)
        elif row['neutral'] and len(neutralCount) < thresholdCount:
            neutralCount.append(row)
    newData = positiveCount + negativeCount + neutralCount
    return newData


if __name__ == '__main__':
    data = readCsv('./data/text_training_data_2.csv')
    data = removeUnusedSentiments(data)
    sentiments = getSentimentList(data)

    data = convertDataToBinary(data, sentiments)

    # Normalizing data to thresholdCount of each emotion
    data = normalizeData(data)

    words = makeDictionary(data)
    words = convertWordsToIntegers(words)
    with open('bag_of_words_2.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(words))

    for row in data:
        row = convertDataToInts(row, words)

    training_set, validation_set, testing_set = splitTrainingData(data)

    writeCsv('./data/training_set_2.csv', training_set)
    writeCsv('./data/validation_set_2.csv', validation_set)
    writeCsv('./data/testing_set_2.csv', testing_set)
