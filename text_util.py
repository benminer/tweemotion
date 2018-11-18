import os
from util import writeCsv

TEXT_DATA_DIR = './data/text'


def text_to_csv():
    data = []
    for name in os.listdir(TEXT_DATA_DIR):
        with open(os.path.join(TEXT_DATA_DIR, name)) as f:
            for line in f:
                row = {}
                line = line.split()
                try:
                    row['sentiment'] = line[1]
                    row['content'] = ' '.join(line[2:])
                    data.append(row)
                except IndexError:
                    print('error')

    writeCsv('text_training_data_2.csv', data)


if __name__ == '__main__':
    text_to_csv()
