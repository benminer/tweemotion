import pandas as pd
import csv
import json
import re
from random import shuffle
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string

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

# Taken from https://www.kaggle.com/lystdo/lstm-with-word2vec-embeddings
def clean_text(text):
    ## Remove puncuation
    text = text.translate(string.punctuation)

    ## Convert words to lower case and split them
    text = text.lower().split()

    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w) >= 3]

    text = " ".join(text)
    ## Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    ## Stemming
    text = text.split()
    stemmer = SnowballStemmer('english')
    stemmed_words = [stemmer.stem(word) for word in text]
    text = " ".join(stemmed_words)

    return text


def makeDictionary(data):
    words = {}
    for row in data:
        content = clean_text(row['content'])
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
    word_list = list(map(lambda x: x['word'], frequent_words[20:10020]))
    return word_list


def convertDataToInts(row, words):
    new_content = ''
    for word in row['content']:
        if word in words.keys():
            new_content += str(words[word]) + ' '
    row['content'] = new_content
    return row


def splitTrainingData(data):
    # pos = data[0:6500]
    # neg = data[6500:13000]
    # neutral = data[13000:]

    training = data[0:30000]
    validation = data[30000::2]
    testing = data[30001::2]

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
    # data = normalizeData(data)

    words = makeDictionary(data)
    words = convertWordsToIntegers(words)
    with open('bag_of_words_2.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(words))

    # for row in data:
    #     row = convertDataToInts(row, words)

    # training_set, validation_set, testing_set = splitTrainingData(data)

    writeCsv('./data/data_set_2.csv', data)
    # writeCsv('./data/validation_set_2.csv', validation_set)
    # writeCsv('./data/testing_set_2.csv', testing_set)
