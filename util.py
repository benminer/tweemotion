import pandas as pd


def readCsv(filePath):
    return pd.read_csv(filePath, header=1)


def toList(data):
    return pd.np.array(data)


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
