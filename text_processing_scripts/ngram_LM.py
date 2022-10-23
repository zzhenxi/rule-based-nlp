'''
Q. 주어진 '05.corpus.txt' 코퍼스에서 tri-gram 범위에서 '학교에' 다음에 나올 수 있는 어절들을 구하여 확률이 높은 순으로 나열해 주세요.  

[예시]
-8.895126285496707      ('학교에',)
-11.72000467288991      ('학교에', '갈')
-12.2308302966559       ('학교에', '가야')
-12.2308302966559       ('학교에', '가는')
-12.2308302966559       ('학교에', '가지')
-12.460726491743127     ('학교에', '가는', '것을')
-12.460726491743127     ('학교에', '갈', '수')
-12.636295404764065     ('학교에', '오지')
-12.636295404764065     ('학교에', '갔습니다.')
-12.636295404764065     ('학교에', '못')
-12.636295404764065     ('학교에', '가고')
-12.636295404764065     ('학교에', '대해')
-13.153873672303073     ('학교에', '가지', '않고')
-13.153873672303073     ('학교에', '가야', '하는')
-13.153873672303073     ('학교에', '안가는', '날마다')
-13.153873672303073     ('학교에', '진학하지', '못했을')
-13.153873672303073     ('학교에', '갈', '때')
-13.153873672303073     ('학교에', '가진', '않겠지요?')
'''

import math

class tri_gram_LM:
    def __init__(self, FILE_PATH):
        self.FILE_PATH = FILE_PATH
        self.TGT_WORD = ''
        self.result_dic = {}
        
    def set_tgt_word(self, TGT_WORD):
        self.TGT_WORD = TGT_WORD

    def LM(self):
        n_gram = 3
        save_dic = {}
        uni_total = 0
        bi_total = 0
        tri_total = 0

        with open(self.FILE_PATH) as fo:
            for line in fo:
                tk_list = line.split()
                tk_num = len(tk_list)
                uni_total += tk_num
                bi_total += tk_num - 1
                tri_total += tk_num - 2

                for i in range(tk_num): # '학교에'가 샘플 내 한번 이상 반복될 수 있음
                    if tk_list[i] == self.TGT_WORD:
                        for n in range(n_gram):
                            key = tuple(tk_list[i:i+n+1])
                            if key not in save_dic:
                                save_dic[key] = 0
                            save_dic[key] += 1
                            if i+n+1 == tk_num:
                                break

        for k, v in save_dic.items():
            n_gram = len(k)
            if n_gram == 1:
                self.result_dic[k] = math.log(v/uni_total)
            elif n_gram == 2:
                self.result_dic[k] = math.log(v/bi_total)
            else:
                self.result_dic[k] = math.log(v/tri_total)
                
    def print_result(self):
        self.LM()
        sorted_result = sorted(self.result_dic.items(), key=lambda item: -item[1])

        for k,v in sorted_result:
            print(v, k)


my_ml = tri_gram_LM('05.corpus.txt')
my_ml.set_tgt_word('학교에')
my_ml.set_tgt_word('갈')
my_ml.print_result()

'''
[result]
-7.57565340725165 ('갈',)
-8.565395045556066 ('갈', '수')
-10.174213521443539 ('갈', '수', '있는')
-10.52900477171078 ('갈', '거예요.')
-10.662536164335302 ('갈', '거야.')
-10.816067407615934 ('갈', '수', '있나요?')
-10.816686844162561 ('갈', '때')
-11.104368916614343 ('갈', '거예요')
-11.172742351554666 ('갈', '수', '있을')
-11.222151952270725 ('갈', '수가')
-11.355683344895247 ('갈', '겁니다.')
-11.355683344895247 ('갈', '수도')
-11.50921458817588 ('갈', '수', '있습니까?')
-11.50921458817588 ('갈', '수', '있도록')
'''