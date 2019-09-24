# pip3 install JPype1==0.7.0
import re
from pyhanlp import HanLP


black_list = ['教程','怎么','在哪','详解','攻略','下载','教学','评测','推荐','技能','技巧','选择','装备','什么','关','期']


# 过滤描述性关键词
def filterDescPhrase(kw):
    GOOD = 1 
    BAD = 0
    good_term_count = 0

    for black_word in black_list:
        if black_word in kw:
            return BAD
    res = HanLP.segment(kw)
    #print(res)
    for item in res:
        word = item.word
        len_word = len(word)
        if len_word >= 2: 
            good_term_count += 1
            if good_term_count > 3:
                return BAD
    return GOOD


def main():
    is_good = filterDescPhrase('九阴真经手游少林的天梯思路')
    print('is_good : ', is_good)


if __name__ == '__main__':
    main()
