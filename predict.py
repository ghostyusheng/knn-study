#!/usr/bin/env python3
import pymysql
import re
import sys
import math
from pypinyin import lazy_pinyin
from pyhanlp import HanLP
import numpy as np



def filterSpecialChar(s, char = ' '):
    #s = ' '.join(lazy_pinyin(s))
    s = s.lower()
    s = re.sub('[\\\.\!\/_,$%^*()+\"\'+|\[\]+——！，。？、~@#￥%……&*（）:：<>《》{}【】¥;"“」`「～\-–™x27\f\n\r\t\v]+', char, s).strip()
    s = re.sub(' +', ' ', s)
    return s


def preFilter(data):
    if type(data) == list:
        for i in range(len(data)):
            data[i] = filterSpecialChar(data[i])
        return data
    return data

    #s = "英雄联盟"
    #res = HanLP.segment(s)
    #res = [i.word for i in res]
    #print(res)

def main():
    WORD = {}
    TAG = {}
    K = 15

    res = open('word_vecs.txt', 'r').readlines()
    for i in res:
        word, word_vec = i.split('|')
        WORD[word] = word_vec

    res = open('app_tags.txt', 'r').readlines()
    for i in range(len(res)):
        word = res[i]
        TAG[i+1] = word

    s = sys.argv[1]
    res = HanLP.segment(s)
    target_vecs = [WORD.get(i.word, None) for i in res]

    res = open('dataset.txt', 'r').readlines()
    distances = []
    mp = {}
    for I in range(len(res)):
        i = res[I]
        app, word_vecs, tag_vecs = i.split('|')
        dis = 0
        for target_vec in target_vecs:
            for word_vec in word_vecs.split(','):
                dis += (float(target_vec) - float(word_vec)) ** 2
        dis = math.sqrt(dis) / len(target_vecs)
        mp[dis] = I
        distances.append(dis)
    distances.sort()
    predict_typs = [mp[i] for i in distances[:K]]
    #print(TAG)
    #print(predict_typs)
    print([TAG.get(i, None) for i in predict_typs])

if __name__ == '__main__':
    main()
