'''
Q. 아래의 주어진 문장에서 각 단어들의 빈도를 구해주세요.

sent = "그간 코로나19로 인한 장기간 여러 어려움에도 불구하고, 극복의 과정에 최선을 다 해주고 계신 NC사우님들께 다시 한번 깊은 감사의 인사 드립니다."
'''

import re

def wordCount(sent):
    wordcount = {}
    # 단어 갯수 count
    for w in sent.split():
        if w not in wordcount:
            wordcount[w] = 0
        wordcount[w] = wordcount[w]+1
    # value 값 기준으로 단어 정렬 
    sorted_wordcount = sorted(wordcount.items(), key=lambda item: -item[1])
    for k,v in sorted_wordcount:
        print(v, k)

def wordCount2(sent):
    wordcount = {}
    # 특수문자 처리 
    punct = re.findall('[^가-힣,A-Z,a-z,0-9, ]', sent) # 특수문자 list
    no_punct = re.sub('[^가-힣,A-Z,a-z,0-9, ]', '', sent).split() # 특수문자를 제외한 list
    # 단어 갯수 count
    for w in punct+no_punct:
        if w not in wordcount:
            wordcount[w] = 0
        wordcount[w] = wordcount[w]+1
    # value 값 기준으로 단어 정렬 
    sorted_wordcount = sorted(wordcount.items(), key=lambda item: -item[1])
    for k,v in sorted_wordcount:
        print(v, k)
    