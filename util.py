import pandas as pd
import csv


def readCsv(filePath):
    data = []
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({'sentiment': row['sentiment'], 'content': row['content']})
    return data


def removeUnusedSentiments(data):
    sentiments = {}
    for row in data:
        sentiment = row['sentiment']
        if sentiment in sentiments.keys():
            sentiments[sentiment] += 1
        else:
            sentiments[sentiment] = 1
    print(sentiments)
    sentiments_list = []
    for key, value in sentiments.items():
        if value > 1000:
            sentiments_list.append(key)
    new_data = []
    for row in data:
        if row['sentiment'] in sentiments_list:
            new_data.append(row)
    return new_data


def cleanString(str):
    val = ''
    if 'the' in str:
        val = str.replace('the', '')
    if 'at' in str:
        val = str.replace('at', '')
    if 'and' in str:
        val = str.replace('and', '')
    if 'while' in str:
        val = str.replace('while', '')
    return val

if __name__ == '__main__':
    data = readCsv('./data/text_emotion_full.csv')
    print(removeUnusedSentiments(data))
