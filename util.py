import pandas as pd


def readCsv(filePath):
    return pd.read_csv(filePath, header=1)


def toList(data):
    return pd.np.array(data)