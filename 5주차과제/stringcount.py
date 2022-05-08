#2019038027 이동현
#문자열에서 문자의 발생빈도를 세는 프로그램

import  operator #operator 모듈 불러오기

text = '''내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞는 누가 나의 이름을 불러다오
그에게로 가서 나도 그의 꽃이 되고 싶다
우리들은 모두 무엇이 되고 싶다
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'''

textd = {} #text에서 한글만 추출한 후 담는 딕셔너리 생성

print("text 원본:", text)

#text에서 한글만 추출하고 몇번 나왔는지 카운트하여 textd에 저장
for t in text:
    if 'ㄱ' <= t and t <= '힣' : #t가 한글이라면
        if t not in textd.keys() : textd[t] = 0 #t를 새로운 key값으로 추가
        textd[t] += 1 #t의 밸류 1증가

#sorted함수를 사용하여 textd를 밸류값 기준으로 내림차순 정렬한다
texts = dict(sorted(textd.items(), key=operator.itemgetter(1), reverse=True))

print("--------------------")
print("문자      빈도수")
print("--------------------")

#texts의 키와 밸류를 출력한다
for key, value in texts.items():
    print(key,value)




