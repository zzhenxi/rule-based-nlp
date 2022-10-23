'''
Q. 주어진 pl과 src를 사용하여 longest matching을 구현해 주세요. 
'''

pl = { "ab": "xxx", "cde": "yyy", "rr": "QQ", "cdefgh": "zzz", "z" : "X"}
src = "qqq abcde rrr abcdefghz"

'''
코드 설명
- 가장 긴 문자열부터 <***>으로 치환하여 두번째 반복문에서 일괄 치환
- 순서대로 저장되는 list의 특성 사용 (2)
- <> 를 붙여준 이유는 ngram의 시작과 끝을 구별하기 위해서 (3)
'''

import re

def longest_matching(pl, src):

    maxlen = len(max(pl, key=len))

    cg_list = []
    for j in range(maxlen, 0, -1):
        for i in range(len(src)-(i-1)):
            if src[i:i+j] in pl:
                cg_list.append(pl[src[i:j+i]]) # (2)
                a = len(src[i:i+j])*'*'
                src = src[:i]+f'<{a}>'+src[j+i:] # (3)

    for i in range(maxlen, 0, -1):
        s = '\*'*i
        while re.search(f"<{s}>", src): 
            m = re.search(f"<{s}>", src)
            src = src[:m.start()]+cg_list.pop(0)+src[m.end():]

    print(src)

'''
[result]
qqq xxxyyy QQr xxxzzzX
'''