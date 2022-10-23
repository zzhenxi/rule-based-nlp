'''
Q. 주어진 문자열을 pl사전에 나오는 key의 value로 치환해 주세요. 
'''

import re

pl = {"aaa": "AA", "bbb": "BBBBB"}
txt = "sdskjld aaadskkkk fdfdf qqqbbbwqmf"

k=0
for m in re.finditer(f'{"|".join(pl.keys())}', txt):
    i,j = m.start(), m.end()
    a = m.group()
    b = a[0].upper()
    txt = txt[:i+k] + b +txt[j+k:]
    k+=len(b)-len(a)

print(txt)