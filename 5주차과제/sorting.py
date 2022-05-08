#2019038027 이동현
#문자와 숫자가 섞인 데이터 정렬하기

import random #랜덤 모듈을 불러옴

#숫자인지 문자인지 구별하여 숫자의 크기를 넘겨주는 함수
def extnum(hexnum):
    num = '' #숫자를 담는 문자열
    for b in hexnum: #hexnum에서 문자를 하나씩 꺼낸다
        d = b.isdigit() #꺼낸 문자가 숫자라면 True 아니라면 False 반환
        if d == True: #꺼낸 문자가 숫자라면 num에 추가한다
            num += b 

    return int(num) #num을 int형으로 바꿔 반환한다


S = 5 #리스트의 사이즈를 정한다

numlist = [] #숫자를 담는 리스트

for i in range(0, S): #hexalist에 S만큼 랜덤한 16진수를 넣는다
    num = str(hex(random.randrange(0, 5000))) # 0에서 5000까지 랜덤한 16진수 생성
    num = num.replace("0x", "") #문자열에서 0x를 제거한다
    numlist.append(num) #numlist에 추가

print("정렬 전의 list: ", numlist) #정렬 전의 numlist를 출력

#선택정렬을 사용하여 정렬
for i in range(0,S-1):
    for j in range(i+1,S):
        if extnum(numlist[i]) > extnum(numlist[j]): #문자열을 extnum함수로 보내 크기를 받아 비교한다
            numlist[i],numlist[j] = numlist[j], numlist[i]

print("정렬 후의 리스트",numlist) #정렬을 끝낸 리스트 출력




