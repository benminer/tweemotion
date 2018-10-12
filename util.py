import pandas as pd


def readCsv(filePath, columns):
    return pd.read_csv(filePath, names=columns)