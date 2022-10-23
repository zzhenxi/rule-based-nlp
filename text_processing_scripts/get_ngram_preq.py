'''
Q. uni bi tri gram-gram 빈도 구하기 (~6/2)
- 문장부호를 하나의 어절로 취급 
'''
import re


txt = "Biden, who met with Andersson and Finnish President Sauli Niinisto in the Oval Office before making public remarks, did not reference any specific security measures the United States would provide the two countries before their membership is finalized. The application period is seen as a particularly vulnerable one, because the two countries are defying years of Russian threats against joining NATO but don’t yet fall under the alliance’s security umbrella."


# helper
def counting(word_list):       
    wordcount = {}
    for w in word_list:
        if w not in wordcount:
            wordcount[w] = 0
        wordcount[w] = wordcount[w]+1
    sorted_wordcount = sorted(wordcount.items(), key=lambda item: -item[1])
    for k,v in sorted_wordcount:
        print(v, k)

### wordCount
def wordCont(n_gram:int, txt):
    gram_list = []
    txt = txt.lower()
    word_list = re.sub('(?=[.,])', ' ', txt).split(' ')
    
    for n in range(n_gram):
        for idx in range(len(word_list)-n):
            gram_list.append(' '.join(word_list[idx:idx+(n+1)])) # n started from 0 (need to plus 1)
            
    counting(gram_list) # use counting function 

### sylCount
def sylCount(n_gram:int, txt):
    gram_list = []
    word_list = txt.lower().split(' ')
    for w in word_list: 
        for n in range(n_gram):
            for idx in range(len(w)-n):
                gram_list.append(w[idx:idx+(n+1)])  
    counting(gram_list)





wordCont(3, txt)
'''
[result]

preq n-gram
6 the
3 ,
2 before
2 security
2 two
2 countries
2 is
2 .
2 the two
2 two countries
2 the two countries
1 biden
1 who
'''

sylCount(3, txt)
'''
[result]
51 e
38 i
31 n
30 t
29 a
28 s
26 r
21 o
16 u
16 l
14 d
13 c
12 h
11 f
10 re
9 b
9 th
9 in
9 p
7 m
'''