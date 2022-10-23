'''
Q. 주어진 txt에서 2개 초과로 반복되는 문자들을(예.aaa) 대문자 1개로(예.A) 치환하여 out과 같이 출력해 주세요. (~6/9)
'''

import re

txt = 'sdskjld aaadskkkk fdfdmmmmmkkf qqqbbbwqmfff'
out = 'sdskjld AdsK fdfdMkkf QBwqmF'

def replace_str(txt):
    out_str = ''
    for i, c in enumerate(txt):
        try :
            if c == out_str[-1].lower(): # previous c is uppercase & same as current c
                continue
        except :
            pass
        if txt[i:i+3] == c*3:
            out_str = out_str+c.upper()
        else : 
            out_str = out_str+c
    print(out_str)


replace_str(txt)
'''
[result]
sdskjld AdsK fdfdMkf QBwqmF
'''

def replace_str_v2(txt):
    k=0
    for m in re.finditer('(.)\\1{2,}', txt):
        i,j = m.start(), m.end()
        a = m.group()
        b = a[0].upper()
        txt = txt[:i+k] + b + txt[j+k:]
        k+=len(b)-len(a)
    print(txt)