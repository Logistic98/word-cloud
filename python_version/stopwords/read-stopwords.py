# -*- coding: utf-8 -*-

import codecs


def read_stopwords(path):
    stop_words = set()
    for word in codecs.open(path, 'r', 'utf-8', 'ignore'):
        stop_words.add(word.strip())
    return stop_words


if __name__ == '__main__':
    path = './stopwords.txt'
    stop_words = read_stopwords(path)
    print(stop_words)
