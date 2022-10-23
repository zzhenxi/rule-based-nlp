'''
패턴 기반 문자열 치환 문제
문제1) 2번 이상 반복되는 기호 및 공백을 하나로 치환하라. (단, 기호 뒤에는 공백 하나가 있어야 함)
'''

import re

txt = '인간적으로,,,,,,,   >>>>>>도구리 티셔츠<<<<<     팔아야 하는거 아니냐?????? 돈은 있으니 빨리 팔아라.... 아니, 팔아주세요.'
print('before:', txt)

k=0
for m in re.finditer('([^가-힣])\\1{2,}', txt):
    i,j = m.start(), m.end()
    edicted_txt = m.group()[0]
    txt = txt[:i+k] + edicted_txt + txt[j+k:]
    k+=len(edicted_txt)-len(m.group())

print('after:', txt)

'''
[result]
before: 인간적으로,,,,,,,   >>>>>>도구리 티셔츠<<<<<     팔아야 하는거 아니냐?????? 돈은 있으니 빨리 팔아라.... 아니, 팔아주세요.
after: 인간적으로, >도구리 티셔츠< 팔아야 하는거 아니냐? 돈은 있으니 빨리 팔아라. 아니, 팔아주세요.
'''


'''
사전 기반 문자열 치환 문제
문제2) 요미가나로 쓰여있는 일본어 문자열을 후리가나 사전을 참고하여 후리가나에서 한자로 치환하라.
* 요미가나 : 한자 단어 없이 그 발음만 쓰여진 문장
* 후리가나 : 한자의 읽는 방식을 히라가나로 표기한 것
'''


huri_dic={'わたし':'私', 'いちばん':'一番', 'すき':'好き', 'たべ':'食べ', 'もの':'物', 'まいにち':'毎日'}

yomi = 'わたしがいちばんすきなたべものはやっぱりチキンだ。まいにちたべられる。' 
# 내가 가장 좋아하는 음식은 역시 치킨이다. 매일 먹을 수 있다..
print('before:', yomi)

i = 0
while i < len(yomi):
    max_ngram = len(max(huri_dic, key=len))
    for j in range(min(len(yomi), max_ngram+i), i, -1): # 첫 인덱스는 포함할 필요 X, 마지막 인덱스는 포함하여야 하므로 거꾸로 반복
        ngram = yomi[i:j]
        if ngram in huri_dic:
            yomi = yomi[:i]+huri_dic[ngram]+yomi[j:]
            i += len(huri_dic[ngram])
            break
    else: 
        i += 1

print('after:', yomi)

'''
[result]
before: わたしがいちばんすきなたべものはやっぱりチキンだ。まいにちたべられる。
after: 私が一番好きな食べ物はやっぱりチキンだ。毎日食べられる。
'''