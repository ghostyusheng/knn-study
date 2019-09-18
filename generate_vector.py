#!/usr/bin/env python3
import pymysql
import re
from pypinyin import lazy_pinyin
from pyhanlp import HanLP
import numpy as np

db = pymysql.connect(host='172.26.192.107', user='root', password='root', db='engine-service', charset='utf8')
cursor = db.cursor()


def query(sql):
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
    except Exception as e:
        print(e)
        return
    return res


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


def main():
    sql = """
        SELECT a.titles AS app_titles,
           a.tags,
           b.title  AS developer_title
        FROM   app a
           JOIN developer b
             ON a.developer_id = b.`id`
        LIMIT 100
    """
    res = query(sql)
    V = []
    WORD = {}
    TAG = []
    DATASET = []
    for i in res:
        (app_titles, tags, developer_title) = (i[0], i[1], i[2])
        app_titles = set(preFilter(app_titles.split(',')))
        tags = preFilter(tags.split(','))
        #developer_title = preFilter(developer_title)

        tag_vector = []
        for tag in tags:
            if tag not in TAG:
                TAG.append(tag)
            tag_index = TAG.index(tag)
            tag_vector.append(str(tag_index))

        for app in app_titles:
            terms = HanLP.segment(app)
            word_vecs = []
            for term in terms:
                if term.word.strip():
                    word = term.word
                    if WORD.get(word):
                        word_vec = WORD[word]
                    else:
                        word_vec = str(np.random.random() * 10)
                        WORD[word] = word_vec
                    word_vecs.append(word_vec)
            DATASET.append((
                app, word_vecs, tag_vector
            ))

    open('app_tags.txt', 'w').writelines('\n'.join(TAG))

    fp = open('word_vecs.txt', 'w')
    for word, word_vec in WORD.items():
        fp.writelines('{}|{}\n'.format(word, word_vec))

    fp = open('dataset.txt', 'w')

    for ele in DATASET:
        app, word_vec, tag_vector = ele
        fp.writelines("{}|{}|{}\n".format(app, ','.join(word_vec), ','.join(tag_vector)))    
        
    print('done')


if __name__ == '__main__':
    main()
