'''
Q. 아래의 a 텍스트를 b 텍스트와 같이 tag를 정제하세요. 정제시 두가지 조건을 지켜주세요. (여기서 유의할 점은 opening tag와 closing tag의 쌍 입니다.) 
    1. br, li, p 태그는 원본 그대로 유지
    2. br, li, p 태그 이외의 태그는 '/htag숫자' 로 정제 
 
a = "<div data-contents-type="text">드디어 이번 이벤해서<div data-contents-type= "text">올 축6 붉귀, 푸귀, 쌍체반 2개 6짤 만들었는데</div><div data-contents-type="text">창고에 썩던 걍 검귀 하나 질렀는데 다이렉트로 6 뜨네요;;; 축이 아니고 걍이라 이거 애매한데 ;;;;&nbsp;</div><div data-contents-type="text"><br></div><div data-contents-type="text">이거 축6 만들라면 다음 이벤때 걍검귀 하나 또 6 만들고 합쳐야 하는데, 그돈씨 축5 사냥꾼 <strong>팬던트</strong> 6가고 말지요.</div><div data-contents-type="text">검귀가 사냥할때 도움되나요? &gt; 착용은 어차피 2개만 되니깐 3개중 2개만 쓰기도 하고 애매하네요;;;</div><div data-contents-type="text">논피서버고 은기사 <li>던전2층</li>이랑 <li>본던2층</li>, <li>버땅 사냥</li>만 갑니다. 89쪼렙 깡통기사라서요</div><p>댓글 미리 감사드립니다.</p></div>"
b = "<htag1>드디어 이번 이벤해서<htag2>올 축6 붉귀, 푸귀, 쌍체반 2개 6짤 만들었는데</htag2><htag3>창고에 썩던 걍 검귀 하나 질렀는데 다이렉트로 6 뜨네요;;; 축이 아니고 걍이라 이거 애매한데 ;;;;&nbsp;</htag3><htag4><br></htag4><htag5>이거 축6 만들라면 다음 이벤때 걍검귀 하나 또 6 만들고 합쳐야 하는데, 그돈씨 축5 사냥꾼 <htag6>팬던트</htag6> 6가고 말지요.</htag5><htag7>검귀가 사냥할때 도움되나요? &gt; 착용은 어차피 2개만 되니깐 3개중 2개만 쓰기도 하고 애매하네요;;;</htag7><htag8>논피서버고 은기사 <li>던전2층</li>이랑 <li>본던2층</li>, <li>버땅 사냥</li>만 갑니다. 89쪼렙 깡통기사라서요</htag8><p>댓글 미리 감사드립니다.</p></htag1>"
'''

import re 

def convert_tag(txt, tag_to_pass={}):
    k = 0
    stack = []
    tag_num = 1
    
    for m in re.finditer('<.*?>', txt):
        tag = m.group()
        t = re.sub('</?|>', '', tag)
        if t not in tag_to_pass:
            if not tag.startswith('</'):
                stack.append(tag_num)
                add_tag = f'<htag{tag_num}>'
                tag_num += 1
            else: 
                use_num = stack.pop()
                add_tag = f'</htag{use_num}>'
            i,j = m.start(), m.end()
            txt = txt[:i+k] + add_tag + txt[j+k:]
            k += len(add_tag)-len(tag)
    return txt

txt = '<div data-contents-type="text">드디어 이번 이벤해서<div data-contents-type= "text">올 축6 붉귀, 푸귀, 쌍체반 2개 6짤 만들었는데</div><div data-contents-type="text">창고에 썩던 걍 검귀 하나 질렀는데 다이렉트로 6 뜨네요;;; 축이 아니고 걍이라 이거 애매한데 ;;;;&nbsp;</div><div data-contents-type="text"><br></div><div data-contents-type="text">이거 축6 만들라면 다음 이벤때 걍검귀 하나 또 6 만들고 합쳐야 하는데, 그돈씨 축5 사냥꾼 <strong>팬던트</strong> 6가고 말지요.</div><div data-contents-type="text">검귀가 사냥할때 도움되나요? &gt; 착용은 어차피 2개만 되니깐 3개중 2개만 쓰기도 하고 애매하네요;;;</div><div data-contents-type="text">논피서버고 은기사 <li>던전2층</li>이랑 <li>본던2층</li>, <li>버땅 사냥</li>만 갑니다. 89쪼렙 깡통기사라서요</div><p>댓글 미리 감사드립니다.</p></div>'
tag_to_pass = {'br', 'li', 'p'}

convert_tag(txt, tag_to_pass)

'''
[result]
'<htag1>드디어 이번 이벤해서<htag2>올 축6 붉귀, 푸귀, 쌍체반 2개 6짤 만들었는데</htag2><htag3>창고에 썩던 걍 검귀 하나 질렀는데 다이렉트로 6 뜨네요;;; 축이 아니고 걍이라 이거 애매한데 ;;;;&nbsp;</htag3><htag4><br></htag4><htag5>이거 축6 만들라면 다음 이벤때 걍검귀 하나 또 6 만들고 합쳐야 하는데, 그돈씨 축5 사냥꾼 <htag6>팬던트</htag6> 6가고 말지요.</htag5><htag7>검귀가 사냥할때 도움되나요? &gt; 착용은 어차피 2개만 되니깐 3개중 2개만 쓰기도 하고 애매하네요;;;</htag7><htag8>논피서버고 은기사 <li>던전2층</li>이랑 <li>본던2층</li>, <li>버땅 사냥</li>만 갑니다. 89쪼렙 깡통기사라서요</htag8><p>댓글 미리 감사드립니다.</p></htag1>'
'''
